"""Self-running sysadmin mentor site: one task a day, Claude grades it, next day unlocks."""
import json, os, pathlib, re, sqlite3, time
import anthropic, markdown
from flask import Flask, redirect, render_template_string, request, session

ROOT = pathlib.Path(__file__).resolve().parent.parent
CUR = ROOT / "curriculum"
DB = pathlib.Path(os.environ.get("DATA_DIR", ROOT / "data")) / "progress.db"
PASSWORD = os.environ["APP_PASSWORD"]
MODEL = "claude-opus-5-5"

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)
client = anthropic.Anthropic()

MENTOR = """You are a senior Windows + Linux (RHEL family) sysadmin mentoring a total beginner through a daily task.
Language: write feedback in the language the learner wrote in (English or Hebrew); commands, paths and errors stay in English.
Plain and short; the learner is a total beginner, so explain any term the first time you use it.
Grade the learner's submission against the task's ## Rubric (10 points). Pass = score >= 7 AND all four parts present:
task outputs, break-it done, fix explained, 5-line reflection in their own words.
Rules: never give the answer. On fail set status "retry" with ONE hint. If understanding is unclear, set status "question"
and ask ONE "why" question (score 0, wait for the answer). Be direct, no praise padding, feedback max 6 lines.
Lab only: if the learner mentions a production hostname, warn them. Reply ONLY with the JSON object."""

GRADE_SCHEMA = {"type": "object", "properties": {
    "status": {"type": "string", "enum": ["pass", "retry", "question"]},
    "score": {"type": "integer"}, "feedback": {"type": "string"}},
    "required": ["status", "score", "feedback"], "additionalProperties": False}


def db():
    DB.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(DB)
    con.executescript("""CREATE TABLE IF NOT EXISTS thread(task TEXT, role TEXT, content TEXT, ts REAL);
        CREATE TABLE IF NOT EXISTS result(task TEXT, score INT, status TEXT, feedback TEXT, ts REAL);""")
    return con


def next_task(task):
    w, d = map(int, re.findall(r"\d+", task))
    return f"week-{w:02d}/day-{d + 1:02d}" if d < 5 else f"week-{w + 1:02d}/day-01"


def current_task(con):
    last = con.execute("SELECT task FROM result WHERE status='pass' ORDER BY ts DESC LIMIT 1").fetchone()
    return next_task(last[0]) if last else "week-01/day-01"


def claude(system, messages, schema=None, max_tokens=16000):
    kw = {"output_config": {"format": {"type": "json_schema", "schema": schema}}} if schema else {}
    r = client.beta.messages.create(model=MODEL, max_tokens=max_tokens, system=system, messages=messages,
                                    betas=["server-side-fallback-2026-07-01"], fallbacks="default", **kw)
    if r.stop_reason == "refusal":
        raise RuntimeError("The grader declined this request; rephrase your submission.")
    return next(b.text for b in r.content if b.type == "text")


def task_text(task):
    p = CUR / f"{task}.md"
    if not p.exists():
        w, d = re.findall(r"\d+", task)
        if int(w) > 56:
            return None
        prev = f"week-{int(w):02d}/day-{int(d)-1:02d}" if int(d) > 1 else f"week-{int(w)-1:02d}/day-05"
        read = lambda name: (CUR / name).read_text(encoding="utf-8")
        system = "You write one day of a sysadmin curriculum, in English only. Output only the markdown file, same format and depth as the example."
        prompt = (f"ROADMAP:\n{read('00-roadmap.md')}\n\nTEMPLATE:\n{read('_day-template.md')}\n\n"
                  f"EXAMPLE (previous day, {prev}):\n{read(prev + '.md')}\n\n"
                  f"Write week {w} day {d} from its row in the roadmap's weekly themes table (the table header explains which OS each day covers). "
                  f"Weeks 1-4 run on the learner's own Windows PC (no VMs); assume no prior knowledge.")
        text = claude(system, [{"role": "user", "content": prompt}])
        text = re.sub(r"^```\w*\n|\n```$", "", text.strip())
        p.parent.mkdir(exist_ok=True)
        p.write_text(text, encoding="utf-8")
    return p.read_text(encoding="utf-8")


def render_task(md):
    body = re.sub(r"^---.*?---\s*", "", md, count=1, flags=re.S).split("## Rubric")[0]
    return markdown.markdown(body, extensions=["tables", "fenced_code"])


HEAD = """<!doctype html><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1">
<title>Sysadmin Journey</title><style>
body{font-family:system-ui;max-width:860px;margin:2rem auto;padding:0 1rem;line-height:1.5;background:#fafafa;color:#222}
pre{background:#eee;padding:.6rem;overflow:auto}code{background:#eee;padding:0 .2rem}table{border-collapse:collapse}td,th{border:1px solid #ccc;padding:.3rem .6rem}
textarea{width:100%;height:16rem;font-family:monospace}.msg{border-left:4px solid #999;padding:.4rem .8rem;margin:.6rem 0;white-space:pre-wrap}
p,li,h1,h2,h3,td,th,.msg,textarea{unicode-bidi:plaintext;text-align:start}pre,code{direction:ltr;unicode-bidi:isolate}
.pass{border-color:#2a2}.retry{border-color:#c33}.question{border-color:#e90}.err{color:#c33}button{padding:.5rem 1.2rem;font-size:1rem}nav a{margin-right:1rem}
</style><nav><a href="/">Today</a><a href="/progress">Progress</a><a href="/logout">Logout</a></nav>"""

PAGE = HEAD + """{% if done %}<h1>Finished the whole roadmap. Go be a senior.</h1>{% else %}
<p><b>{{task}}</b></p><div dir=auto>{{html|safe}}</div><hr>
{% for role, c in thread %}<div class="msg {{c.status if role=='assistant' else ''}}" dir=auto>{% if role=='assistant' %}<b>Mentor ({{c.score}}/10):</b> {{c.feedback}}{% else %}<b>You:</b> {{c}}{% endif %}</div>{% endfor %}
{% if error %}<p class=err>{{error}}</p>{% endif %}
<form method=post action=/submit><textarea name=text placeholder="Paste your outputs, what you broke and fixed, and 5 lines of what you learned" required></textarea><br><button>Submit for review</button></form>{% endif %}"""

PROGRESS = HEAD + """<h2>Progress</h2><table><tr><th>Date<th>Task<th>Score<th>Status<th>Feedback</tr>
{% for t, s, st, fb, ts in rows %}<tr><td>{{ts}}</td><td>{{t}}</td><td>{{s}}</td><td>{{st}}</td><td dir=auto>{{fb}}</td></tr>{% endfor %}</table>"""

LOGIN = '<form method=post style="margin:4rem auto;width:20rem;font-family:system-ui"><h2>Sysadmin Journey</h2><input type=password name=password placeholder=Password autofocus> <button>Enter</button></form>'


def thread_rows(con, task):
    rows = con.execute("SELECT role, content FROM thread WHERE task=? ORDER BY ts", (task,)).fetchall()
    return [(r, json.loads(c) if r == "assistant" else c) for r, c in rows]


@app.before_request
def guard():
    if request.endpoint != "login" and not session.get("ok"):
        return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST" and request.form.get("password") == PASSWORD:
        session["ok"] = True
        return redirect("/")
    return LOGIN


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


@app.route("/")
def today():
    con = db()
    task = current_task(con)
    md = task_text(task)
    return render_template_string(PAGE, task=task, done=md is None, html=render_task(md or ""),
                                  thread=thread_rows(con, task), error=request.args.get("e"))


@app.route("/submit", methods=["POST"])
def submit():
    con = db()
    task = current_task(con)
    text = request.form["text"].strip()[:40000]
    con.execute("INSERT INTO thread VALUES(?,?,?,?)", (task, "user", text, time.time()))
    con.commit()
    msgs = [{"role": r, "content": c if r == "user" else json.dumps(c, ensure_ascii=False)} for r, c in thread_rows(con, task)]
    try:
        grade = json.loads(claude(f"{MENTOR}\n\nTASK:\n{task_text(task)}", msgs, GRADE_SCHEMA))
    except Exception as e:  # submission is already saved; show the error and let them resubmit
        return redirect(f"/?e={type(e).__name__}: {str(e)[:200]}")
    con.execute("INSERT INTO thread VALUES(?,?,?,?)", (task, "assistant", json.dumps(grade, ensure_ascii=False), time.time()))
    if grade["status"] != "question":
        con.execute("INSERT INTO result VALUES(?,?,?,?,?)", (task, grade["score"], grade["status"], grade["feedback"], time.time()))
    con.commit()
    return redirect("/")


@app.route("/progress")
def progress():
    rows = [(t, s, st, fb, time.strftime("%Y-%m-%d", time.localtime(ts))) for t, s, st, fb, ts in
            db().execute("SELECT task, score, status, feedback, ts FROM result ORDER BY ts")]
    return render_template_string(PROGRESS, rows=rows)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
