---
week: 01
day: 5
os: windows
milestone: M0
optional: false
---
# Week 01 · Day 5 — Servers, virtual machines and your first runbook

## Why it matters
In week 5 you will build a lab of virtual machines. Today you learn the words so that week makes sense:
- **Server** — a computer whose job is to serve others: files, websites, logins. Usually no screen, lives in a rack or the cloud.
- **Virtual machine (VM)** — a fake computer running as a program inside a real one. You can have 4 "computers" on one PC.
- **Hypervisor** — the program that runs VMs. Windows has one built in: **Hyper-V**. Companies use **VMware vCenter**.
- **ISO** — a file that is an exact copy of an install DVD. You "insert" it into a VM to install an OS.
- **Snapshot** — a saved state of a VM. Break the VM, restore the snapshot, it is as if nothing happened.
Sysadmins also write things down. A **runbook** is a step-by-step document so anyone can repeat a task. You write your first one today.

## Task
1. Check if your PC can run VMs: Task Manager → Performance → CPU → look for **Virtualization: Enabled**. If it says Disabled, search the web for "enable virtualization BIOS <your PC model>" and write down the steps (do not do them yet unless you are comfortable).
2. Check your Windows edition: Settings → System → About. Hyper-V needs **Pro/Enterprise/Education**. Write down your edition and how much free disk space you have (`Get-PSDrive C` in PowerShell). The lab needs ~150 GB.
3. Watch one short video (search "what is a virtual machine" and "what is a hypervisor", ~10 min total). Then explain, in your own words, 3 lines each: VM, hypervisor, ISO, snapshot. No copy-paste.
4. Write your first runbook: `Documents\sysadmin-journey\week01\runbook-my-pc.md` with: PC specs (from day 1), Windows edition, virtualization status, free disk, the 4 services from day 3 and their startup types. Short, in a list. A stranger should understand it.
5. Write a glossary file `glossary.md` with 15 terms you met this week (CPU, RAM, extension, path, service, Event ID, PowerShell, prompt, VM, ISO, ...). One line each, your words.

## Break it
Nothing to break today. Instead: give your runbook to someone (a friend, a colleague) and ask them to read it back to you. Every question they ask is a hole in the document. Fix the holes.

## Submit
- Virtualization status, Windows edition, free disk space
- Your 4 explanations (VM, hypervisor, ISO, snapshot)
- The runbook and the glossary (paste both)
- 5 lines: what I learned this **week**

## Rubric
| Points | Criterion |
|--------|-----------|
| 3 | Virtualization, edition and disk checked; runbook complete |
| 2 | Glossary has 15 terms in own words |
| 2 | The 4 explanations are correct and in own words |
| 2 | Weekly reflection shows real understanding |
| 1 | Clean submission |
