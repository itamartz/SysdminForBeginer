---
week: 05
day: 2
os: linux
milestone: M1
optional: false
---
# Week 05 · Day 2 — First Rocky Linux server

## Why it matters
Half the servers in the world run Linux. Today you install **Rocky Linux 9** — a free twin of Red Hat Enterprise Linux (RHEL), which is what the company runs.
No desktop, no mouse: this is how it looks in production. You already know the shell from week 3 (WSL); now it is a real server.

## Task
1. Download the **Rocky Linux 9 minimal ISO** from rockylinux.org.
2. Create VM `LNX01`: 2 vCPU, 2 GB RAM, 30 GB disk, same network as `DC01`. Hyper-V: Generation 2 and set Secure Boot to **Microsoft UEFI Certificate Authority** (or disable it).
3. Install with **Minimal Install**. Set the root password. Create a user with your name and tick "Make this user administrator".
4. Log in as your user (not root) and run:
   ```bash
   whoami
   hostname
   cat /etc/os-release
   ip a
   sudo dnf -y update
   ```
   What is the difference between `root` and a user with `sudo`? Why do admins not work as root all day?
5. Ping `DC01` by IP from `LNX01`. Does it work? If not, write down why you think it fails (you fix networking on day 4).

## Break it
Run `sudo dnf -y update` again — nothing to do. Now run `dnf -y update` **without** sudo. Read the error. Explain it.
Then run `touch /etc/test.txt` without sudo. Read the error. Same reason? Why?

## Submit
- Output of the step 4 commands (the dnf update output can be the last 10 lines)
- Ping result to DC01 and your explanation
- The two errors from "Break it" and why they happen
- 5 lines: what I learned

## Rubric
| Points | Criterion |
|--------|-----------|
| 3 | Rocky 9 runs, non-root user with sudo, system updated |
| 2 | Both errors explained: permissions, not a broken command |
| 2 | Can explain why you do not work as root daily |
| 2 | Reflection in own words |
| 1 | Clean submission |
