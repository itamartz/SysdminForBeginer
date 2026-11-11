---
week: 01
day: 3
os: windows
milestone: M0
optional: false
---
# Week 01 · Day 3 — What an operating system does

## Why it matters
The **operating system** (OS) — Windows, Linux, macOS — is the program that runs all other programs. It talks to the hardware, manages files, users, and network, and runs **services**: programs that work in the background with no window (printing, updates, time sync).
When something "doesn't work", a sysadmin asks: is a service stopped? Is there an error in the logs? Today you meet both.

## Task
1. Open **Settings** (`Win+I`) and the old **Control Panel** (`Win+R`, `control`). Both change the OS. Find where each one shows: installed programs, network settings, user accounts. Windows is in the middle of moving everything from Control Panel to Settings — you need to know both.
2. Press `Win+R`, type `services.msc`. This lists every service. Find these and write their Status and Startup type: `Windows Update`, `Print Spooler`, `Windows Time`, `DHCP Client`. Double-click one and read its Description.
3. Press `Win+R`, type `eventvwr`. This is **Event Viewer**: the OS diary. Go to **Windows Logs → System**. Find the most recent **Error** or **Warning**. Write down: Date, Source, Event ID, and the first line of the message. Search the web for "Event ID <number> <source>" and write one line on what it means.
4. Open **Settings → Windows Update → Update history**. Write down the last 3 updates installed and their dates. Updates are the #1 security task of a sysadmin.

## Break it
In `services.msc`, right-click **Print Spooler → Stop**. Open Settings → Printers. What changed? Try to print a test page (any printer, even "Microsoft Print to PDF"). What error do you see?
Now go back to Event Viewer → System and find the event that says the service stopped. Then **Start** the service again and find the "started" event. This is how you prove what happened and when.

## Submit
- Status/Startup type of the four services
- The Event Viewer error: date, source, ID, message, your one-line meaning
- Last 3 updates
- What broke when Print Spooler stopped, and the two event log entries (stop and start) with their Event IDs
- 5 lines: what I learned

## Rubric
| Points | Criterion |
|--------|-----------|
| 3 | Services, event, and update info collected correctly |
| 2 | Print Spooler experiment done and both log entries found |
| 2 | Can explain what a service is and why Event Viewer matters |
| 2 | Reflection in own words |
| 1 | Clean submission |
