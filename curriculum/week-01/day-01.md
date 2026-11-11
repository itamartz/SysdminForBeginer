---
week: 01
day: 1
os: windows
milestone: M0
optional: false
---
# Week 01 · Day 1 — What is inside your computer

## Why it matters
A sysadmin's job is to keep computers working. Before you can fix one, you need to know its parts and what each part does.
Today you look inside your own PC without opening it. Four parts matter most:
- **CPU** (processor) — does the calculations. More cores = more things at once.
- **RAM** (memory) — short-term workspace. Empties when the PC turns off.
- **Disk** (storage: SSD or HDD) — long-term storage. Keeps files when the PC is off.
- **GPU** (graphics card) — draws the screen.

## Task
1. Press `Ctrl+Shift+Esc` to open **Task Manager**. Click **Performance**. Click each of CPU, Memory, Disk, GPU and write down: CPU name and number of cores, total RAM in GB, disk size and type (SSD/HDD), GPU name.
2. Press `Win+R`, type `msinfo32`, Enter. This is **System Information**. Write down: OS Name, System Manufacturer, System Model, BIOS Version, "Installed Physical Memory".
3. Press `Win+R`, type `cmd`, Enter. A black window opens — this is the **command prompt**, a way to give the computer text commands. Type:
   ```
   systeminfo
   ```
   Wait for it to finish. Find the same facts you found in steps 1 and 2. Three tools, one truth.
4. In Task Manager, click **Processes**. Sort by Memory (click the column header). Which program uses the most RAM right now? Which uses the most CPU?

## Break it
Open your web browser and open 25 tabs of different websites. Watch Task Manager → Performance → Memory while you do it. Write down the RAM "In use" number before and after. Then close all the tabs and watch it drop.
What would happen if RAM reached 100%? (Hint: look at the "Committed" number — the PC starts using the disk as fake RAM, which is very slow.)

## Submit
- The spec list: CPU, cores, RAM, disk size/type, GPU, OS name, manufacturer/model, BIOS version
- The top RAM and top CPU process names
- RAM before/after the 25 tabs, and your explanation of what happens at 100%
- 5 lines: what I learned

## Rubric
| Points | Criterion |
|--------|-----------|
| 3 | Complete spec list from all three tools |
| 2 | 25-tabs experiment done with numbers |
| 2 | Can explain the difference between RAM and disk, and what happens when RAM is full |
| 2 | Reflection in own words |
| 1 | Clean submission |
