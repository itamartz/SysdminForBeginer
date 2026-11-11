---
week: 05
day: 1
os: windows
milestone: M1
optional: false
---
# Week 05 · Day 1 — Build the lab + first Windows Server

## Why it matters
Everything you learn from now on happens in your lab. If you have no place to break things, you learn nothing.
Today you build it: a hypervisor and your first server VM. You met all these words in week 1 day 5 — now you use them.

## Task
1. **Hypervisor.** On Windows 11 Pro: open "Turn Windows features on or off", tick **Hyper-V**, reboot. On vCenter: confirm you can create a VM in your folder.
2. **ISO.** Download **Windows Server 2022 Evaluation** (free for 180 days) from the Microsoft Evaluation Center. Note where the file is saved.
3. **Create the VM** `DC01`: Generation 2, 2 vCPU, 4 GB RAM, 60 GB disk, network = **Default Switch** (Hyper-V) or your lab port group (vCenter). Attach the ISO as the DVD drive.
4. Start the VM and install Windows Server 2022 **Standard (Desktop Experience)**. Set the Administrator password. Store it in a password manager, not on paper.
5. Open PowerShell inside the VM and run:
   ```powershell
   hostname
   Get-ComputerInfo | Select-Object OsName, OsVersion, CsTotalPhysicalMemory
   ipconfig /all
   ```
   Make sure you understand every line of `ipconfig /all`: IPv4 Address, Subnet Mask, Default Gateway, DNS Servers, DHCP Enabled (week 2 words).

## Break it
Shut down the VM. Change its RAM to 512 MB. Boot it. Observe: slow? fails? Put it back to 4 GB.
Write down what you saw, how long it took, and what Microsoft's minimum RAM is for this edition.

## Submit
- Output of the three commands above
- Hypervisor used and the VM settings you chose
- What happened at 512 MB
- 5 lines: what I learned

## Rubric
| Points | Criterion |
|--------|-----------|
| 3 | VM runs, outputs show Windows Server 2022, hostname and an IP |
| 2 | 512 MB experiment done and described |
| 2 | Can explain DHCP vs static and what the default gateway is for |
| 2 | Reflection in own words |
| 1 | Clean submission |
