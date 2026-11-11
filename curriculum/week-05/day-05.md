---
week: 05
day: 5
os: both
milestone: M1
optional: false
---
# Week 05 · Day 5 — Finish the lab: WIN11 + LNX02, snapshots, your lab runbook

## Why it matters
Senior admins do not remember — they write. Today you finish the four VMs, snapshot them all, and write the runbook for building the lab from zero.
In week 49 you will rebuild everything from this document alone.

## Task
1. Create `WIN11` (Windows 11 Enterprise Evaluation ISO, 2 vCPU, 4 GB) and `LNX02` (Rocky 9 minimal, same settings as LNX01). Static IPs `.20` and `.12`. Hostnames set.
2. All four VMs ping each other by IP. Fill this table in your submission: VM, Hostname, IP, OS.
3. Take a snapshot / checkpoint of every VM named `week05-clean`.
   Hyper-V (on the host): `Checkpoint-VM -Name DC01 -SnapshotName week05-clean`. vCenter: right-click the VM → Snapshots.
4. Write `runbook-lab.md`: every step you did this week to build the lab, in order, with the exact commands. Short. Someone else should be able to follow it.

## Break it
On LNX02: `sudo rm -rf /etc/NetworkManager` (yes, really — it is a lab). Reboot. Observe. Now **restore the snapshot** and confirm it is back.
That is the whole point of snapshots. When would you *not* trust a snapshot? (Hint: databases, Active Directory.)

## Submit
- The 4-VM table + ping proof (one ping from each VM to one other)
- `runbook-lab.md` (paste it)
- What happened after the rm, and after the restore
- 5 lines: what I learned this **week**

## Rubric
| Points | Criterion |
|--------|-----------|
| 3 | 4 VMs up, static IPs, all ping each other, snapshots exist |
| 2 | Snapshot restore done and explained; answers when snapshots are not enough |
| 2 | Runbook is followable by a stranger |
| 2 | Weekly reflection shows real understanding |
| 1 | Clean submission |
