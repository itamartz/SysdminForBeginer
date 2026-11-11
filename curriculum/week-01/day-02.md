---
week: 01
day: 2
os: windows
milestone: M0
optional: false
---
# Week 01 · Day 2 — Files, folders and paths

## Why it matters
Everything on a computer is a file in a folder. A **path** is the address of a file, like `C:\Users\Dana\Documents\report.docx`.
Sysadmins read and type paths all day. Today you learn to see the real file system, not the pretty version Windows shows you.
Key terms: **drive** (`C:`), **folder** (also called directory), **file extension** (the `.docx` part — tells Windows which program opens it), **hidden file**.

## Task
1. Open **File Explorer** (`Win+E`). Click **View → Show → File name extensions** and **Hidden items**. Now you see the truth: every file has an extension, and some folders were hidden.
2. Go to `C:\`. Write down what these folders are for (look inside, then search the web for one line each): `Windows`, `Program Files`, `Program Files (x86)`, `Users`, `ProgramData`.
3. Go to `C:\Users\<your name>`. Find `AppData` (hidden). Look inside `AppData\Local` and `AppData\Roaming`. This is where programs keep their settings.
4. Create this folder tree in your Documents folder, by hand:
   ```
   Documents\sysadmin-journey\week01\notes
   Documents\sysadmin-journey\week01\screenshots
   ```
   Inside `notes`, create a text file `day02.txt` and write one line in it. Right-click the file → Properties. Write down its full path and its size in bytes.
5. Click in the Explorer address bar and type a path by hand: `C:\Windows\System32`. This folder holds the core of Windows. Find `cmd.exe` and `notepad.exe`. Programs are files too.

## Break it
Rename `day02.txt` to `day02.jpg`. Double-click it. What happens and why? (Windows picked a program by the extension, but the content is still text.)
Rename it back. Then try to rename `C:\Windows\System32\notepad.exe`. What stops you? That protection is called **permissions** — a big topic for week 3 and week 7.

## Submit
- One line each for the five `C:\` folders
- Full path and byte size of `day02.txt`
- What happened with `.jpg` and with renaming notepad.exe, and why
- 5 lines: what I learned

## Rubric
| Points | Criterion |
|--------|-----------|
| 3 | Extensions and hidden items shown, folder tree created, path and size correct |
| 2 | Both break-it experiments done and explained |
| 2 | Can explain what an extension is and what AppData is for |
| 2 | Reflection in own words |
| 1 | Clean submission |
