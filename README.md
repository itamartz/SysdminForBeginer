# Sysadmin Journey — Windows + Linux (RHEL family)

A self-running mentor website. The learner opens it, sees one task a day, does it in the lab, pastes the result,
and Claude grades it. Pass unlocks the next day. No teacher needed. ~2–3 h/day, 12 months, beginner → senior.

## Run it (Docker)
1. `cp .env.example .env` and fill it in: `APP_PASSWORD` (learner login), `ANTHROPIC_API_KEY`, `SECRET_KEY`.
2. `docker compose up -d --build`
3. Open `http://<server>:8080`, enter the password, start with week 1 day 1.

`data/progress.db` holds all progress; `curriculum/` holds the tasks (weeks 2+ are generated on demand and saved there).
Back up both folders.

## For the learner
- **Today**: read the task. Do it. Break it on purpose. Fix it. Write 5 lines on what you learned.
- Paste everything in the box and submit. You get a score out of 10 and feedback. 7+ = pass.
- The mentor may ask you one "why" question before scoring — answer it in the same box.
- Lab only. Never run a task against a production machine.

## Layout
`app/` Flask site · `curriculum/` roadmap + daily tasks · `data/` SQLite · `checks/` verification scripts (from week 5)
`CLAUDE.md` + `.claude/commands/` — optional: the same curriculum also works inside Claude Code (`/today`, `/review`).
