---
week: 01
day: 4
os: windows
milestone: M0
optional: false
---
# Week 01 · Day 4 — The command line

## Why it matters
Clicking works for one computer. Sysadmins manage hundreds, so they type commands and later turn them into scripts.
Windows has two command lines: the old **cmd** and the modern **PowerShell**. You will use PowerShell most, but you must read both.
Today's commands all deal with files and folders — the same things you clicked yesterday.

## Task
1. Open PowerShell: right-click Start → **Terminal** (or `Win+R`, `powershell`). The line ending in `>` is the **prompt**; it shows where you are.
2. Move around and look:
   ```powershell
   Get-Location            # where am I?  (cmd: cd)
   Set-Location ~\Documents\sysadmin-journey   # go somewhere  (cmd: cd path)
   Get-ChildItem           # list what is here  (cmd: dir)
   Get-ChildItem -Recurse  # list everything below, too
   ```
3. Make and read things:
   ```powershell
   New-Item -ItemType Directory week01\cli        # mkdir
   Set-Location week01\cli
   "hello from the command line" | Out-File test.txt
   Get-Content test.txt                            # cmd: type test.txt
   Copy-Item test.txt copy.txt                     # cmd: copy
   Rename-Item copy.txt renamed.txt                # cmd: ren
   Get-ChildItem
   ```
4. Get help without the web:
   ```powershell
   Get-Help Get-ChildItem -Examples
   Get-Command *service*        # find commands by keyword
   Get-Service | Where-Object Status -eq Running   # yesterday's services.msc, as text
   ```
   PowerShell commands are **Verb-Noun**: `Get-`, `Set-`, `New-`, `Remove-`, `Start-`, `Stop-`. Guess the command to stop a service. Check with `Get-Command`.
5. Open **cmd** (`Win+R`, `cmd`) and do step 2 again with `cd`, `dir`, `type`. Same ideas, older words.

## Break it
In your `cli` folder run `Remove-Item renamed.txt`. Now open the Recycle Bin. Is it there? (No. The command line does not use the Recycle Bin. Deleted means deleted. This is why sysadmins check twice.)
Then type a command with a typo: `Get-Childitm`. Read the whole red error. Which words tell you what went wrong? Errors are instructions, not punishment.

## Submit
- Output of `Get-ChildItem -Recurse` from `sysadmin-journey`
- The command you guessed for stopping a service
- The Recycle Bin result and the full typo error text, with the words that explain it
- 5 lines: what I learned

## Rubric
| Points | Criterion |
|--------|-----------|
| 3 | Folder/file work done in PowerShell and repeated in cmd |
| 2 | Delete and typo experiments done and explained |
| 2 | Can explain Verb-Noun and how to find a command without the web |
| 2 | Reflection in own words |
| 1 | Clean submission |
