# Roadmap — beginner → senior sysadmin (Windows + RHEL-family Linux)

~13 months, 5 tasks/week, 2–3 h/task. Weeks 1–4 are fundamentals (CompTIA A+ Core 1/2 level) on the learner's own PC — no lab, no prior knowledge assumed.
From week 5 both OSes run in parallel: a Windows skill and its Linux twin in the same week. Lab: Hyper-V or vCenter. Target VMs: `DC01` (Windows Server), `WIN11` (client), `LNX01`, `LNX02` (Rocky Linux 9).

## Milestones (each one is proven by doing, not by a quiz)
| # | Milestone | Proven when the learner can… |
|---|-----------|------------------------------|
| M0 | Fundamentals (A+ level) | Explain what CPU/RAM/disk/OS/file/IP/DNS/VM/ISO are, use Explorer, Task Manager, cmd/PowerShell and a Linux shell on their own PC, follow the 6-step troubleshooting method |
| M1 | Lab builder | Build all 4 VMs from ISO, static IPs, they ping each other |
| M2 | Filesystem & permissions | Explain and fix NTFS ACLs and Linux rwx/ownership on a broken share |
| M3 | Users & auth | Manage local users, groups, sudoers, Windows local policy |
| M4 | Networking | Diagnose DNS/DHCP/gateway/firewall failures with ipconfig, nslookup, ss, nmcli, firewall-cmd |
| M5 | Services & logs | Find why a service failed using Event Viewer and journalctl, and fix it |
| M6 | Active Directory | Promote DC, join clients, OUs, groups, GPO, troubleshoot a failed join |
| M7 | Linux server ops | SSH keys, systemd units, dnf, SELinux basics, cron |
| M8 | Scripting | PowerShell + Bash scripts that run unattended and alert on failure |
| M9 | Storage & backup | Disks, LVM, Storage Spaces, backup + tested restore |
| M10 | Monitoring & hardening | Baseline monitoring, patching, hardening checklists for both OSes |
| M11 | Virtualization & infra | Manage the hypervisor itself, snapshots, templates, resources |
| M12 | Senior habits | Incident post-mortem, change plan, runbook, teaching a task to someone else |

## Weekly themes (used to generate day files)
Weeks 1–4: the row lists each day. From week 5: days 1,3 = Windows column, days 2,4 = Linux column, day 5 = both + weekly runbook.
| Weeks | Theme | Windows side | Linux side |
|-------|-------|--------------|------------|
| 1 | Your own PC, inside and out (M0, A+ Core 1) | D1 hardware: CPU/RAM/disk/GPU via Task Manager, msinfo32, systeminfo · D2 files, folders, paths, extensions, hidden files · D3 what an OS does: Settings, services.msc, Windows Update, Event Viewer first look · D4 command line: cmd + PowerShell basics (cd, dir, mkdir, copy, type, Get-Help) · D5 what a server, VM, ISO, hypervisor are; check CPU virtualization support; PC spec-sheet runbook | — |
| 2 | Networking fundamentals on your own PC (M0, A+ Core 1) | D1 IP, subnet mask, gateway, DNS via ipconfig /all · D2 ping, tracert, nslookup: what each proves · D3 router admin page, DHCP leases, Wi-Fi vs Ethernet · D4 ports and connections: netstat, what a service listens on · D5 draw your home network; glossary of 20 terms | — |
| 3 | Linux first contact with WSL (M0) | D1 `wsl --install` a RHEL-family distro (AlmaLinux 9 if listed in `wsl --list --online`, else Ubuntu), ls/cd/pwd/cat/man · D2 files and paths: /, /home, /etc, /var; touch, mkdir, cp, mv, rm · D3 permissions: ls -l, chmod, chown, sudo · D4 packages and services: dnf/apt, systemctl status · D5 compare Windows vs Linux side by side; week runbook | RHEL family via WSL |
| 4 | Security and operational basics (M0, A+ Core 2) | D1 accounts: admin vs standard user, UAC, create a standard user and try to install software · D2 Windows Defender, firewall on/off effect, password manager, MFA · D3 backups: File History, restore a deleted file, 3-2-1 rule · D4 the 6-step troubleshooting method applied to a real issue on your PC; write a ticket · D5 week review; glossary complete; ready-for-lab checklist | — |
| 5 | Lab + first contact (M1) | Install Server, hostname, IP | Install Rocky, hostname, IP |
| 6 | Shell basics | PowerShell: Get-*, pipes, help | Bash: ls, cd, cat, grep, man, pipes |
| 7 | Filesystem & permissions (M2) | NTFS, icacls, shares | chmod/chown, mount, /etc layout |
| 8 | Users & groups (M3) | net user, lusrmgr, local policy | useradd, groups, sudoers, passwd |
| 9 | Networking I (M4) | ipconfig, DNS client, hosts file | nmcli, /etc/hosts, resolv.conf |
| 10 | Networking II (M4) | Windows Firewall, netstat, Test-NetConnection | firewalld, ss, nc, tcpdump basics |
| 11 | Services & logs (M5) | services.msc, Event Viewer, Get-WinEvent | systemctl, journalctl, /var/log |
| 12 | Remote admin | RDP, WinRM, PowerShell remoting | SSH, keys, scp, tmux |
| 13–14 | Active Directory I (M6) | Promote DC01, DNS, join WIN11, OUs, users | Join LNX01 to AD with sssd |
| 15–16 | Active Directory II (M6) | GPO, groups, delegation, troubleshooting joins | sudo via AD groups, kerberos basics |
| 17–18 | Packages & updates | WSUS basics, winget, patch cycle | dnf, repos, kernel updates, reboot plan |
| 19–20 | Scripting I (M8) | PowerShell functions, params, error handling | Bash variables, loops, exit codes |
| 21–22 | Scripting II (M8) | Scheduled tasks, logging, email alert | cron/systemd timers, logging, alert |
| 23–24 | Storage (M9) | Disk Management, Storage Spaces, quotas | fdisk, LVM, xfs, fstab |
| 25–26 | Backup & restore (M9) | Windows Server Backup, system state | rsync, tar, snapshot, tested restore |
| 27–28 | Web & file services | IIS, DFS, print | nginx/httpd, NFS, Samba |
| 29–30 | Security hardening (M10) | Local policy baseline, BitLocker, LAPS | SELinux enforcing, sshd hardening, fail2ban |
| 31–32 | Monitoring (M10) | Performance Monitor, counters, alerts | top/htop, sar, Prometheus node_exporter |
| 33–34 | Virtualization (M11) | Hyper-V/vCenter: templates, snapshots, resources | KVM basics, cloud-init |
| 35–36 | Certificates & TLS | AD CS, cert enrollment | openssl, Let's Encrypt, trust store |
| 37–38 | Troubleshooting weeks | Injected incidents: broken DNS, full disk, failed service | Same, Linux side |
| 39–40 | Automation | DSC / Ansible against Windows | Ansible against Linux |
| 41–44 | Build a real service end-to-end | Documented, monitored, backed up Windows app server | Same, Linux app server |
| 45–48 | Senior habits (M12) | Change plan, runbook, post-mortem, capacity plan | Same |
| 49–52 | Capstone | Rebuild the whole lab from your own runbooks in one week | |
| 53–56 | Review & gaps | Re-do weakest milestones from progress file | |

Senior = can be left alone with a broken system, fixes it, documents it, and prevents it next time.
