---
week: 05
day: 4
os: linux
milestone: M1
optional: false
---
# Week 05 · Day 4 — Linux: hostname, static IP with nmcli, firewalld

## Why it matters
Same identity work as yesterday, on the Linux side. The tool is `nmcli` (NetworkManager's command line).
On the way you meet **firewalld**, the #1 reason "it doesn't ping" on RHEL-family systems.

## Task
1. Hostname:
   ```bash
   sudo hostnamectl set-hostname lnx01
   hostnamectl
   ```
2. Find the connection name and set a static IP (same subnet as DC01, for example `.11`):
   ```bash
   nmcli con show
   sudo nmcli con mod "<name>" ipv4.method manual ipv4.addresses <IP>/24 ipv4.gateway <gw> ipv4.dns <gw or 8.8.8.8>
   sudo nmcli con up "<name>"
   ip a
   ip route
   cat /etc/resolv.conf
   ```
3. Verify:
   ```bash
   ping -c 3 8.8.8.8
   ping -c 3 rockylinux.org
   ping -c 3 <DC01 IP>
   ```
4. From DC01, ping LNX01. Does it answer? Check with `sudo firewall-cmd --list-all` on LNX01.

## Break it
Block ping (ICMP) on LNX01:
```bash
sudo firewall-cmd --add-icmp-block=echo-request
```
Ping from DC01 again. Then from LNX01 ping DC01 — does *outgoing* still work? Why?
Remove the block (`--remove-icmp-block=echo-request`). Then check: was that change permanent? What does `--permanent` do and why does it exist?

## Submit
- Output of `hostnamectl`, `ip a`, `ip route`, the three pings, `firewall-cmd --list-all`
- Ping results during the ICMP block, both directions, with explanation
- Your answer about `--permanent`
- 5 lines: what I learned

## Rubric
| Points | Criterion |
|--------|-----------|
| 3 | Hostname lnx01, static IP, internet + DNS work, DC01 and LNX01 ping both ways |
| 2 | ICMP-block experiment explained (inbound vs outbound) |
| 2 | Can explain runtime vs permanent firewalld config |
| 2 | Reflection in own words |
| 1 | Clean submission |
