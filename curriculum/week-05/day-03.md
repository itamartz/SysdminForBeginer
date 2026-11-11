---
week: 05
day: 3
os: windows
milestone: M1
optional: false
---
# Week 05 · Day 3 — Windows: hostname, static IP, basic network tools

## Why it matters
A server needs a fixed address and a sensible name. A server on a DHCP address is a server that breaks at 3 AM when the lease changes.
Today you give `DC01` its identity and use the four tools you will run every day: `ipconfig`, `ping`, `nslookup`, `Test-NetConnection`.

## Task
1. Rename the server:
   ```powershell
   Rename-Computer -NewName DC01 -Restart
   ```
2. Pick a static IP in your lab subnet (look at `ipconfig /all` from day 1 — if DHCP gave `172.20.x.50`, use `172.20.x.10`). Set it:
   ```powershell
   Get-NetAdapter
   New-NetIPAddress -InterfaceAlias "Ethernet" -IPAddress <IP> -PrefixLength <mask bits> -DefaultGateway <gw>
   Set-DnsClientServerAddress -InterfaceAlias "Ethernet" -ServerAddresses <gw or 8.8.8.8>
   ```
   Explain to yourself: what does PrefixLength 24 mean? How many addresses are in such a network?
3. Verify:
   ```powershell
   ipconfig /all
   ping 8.8.8.8
   nslookup microsoft.com
   Test-NetConnection microsoft.com -Port 443
   ```
4. Ping `LNX01` by IP. Record the result.

## Break it
Set the default gateway to a wrong address (for example `.254` when the real one is `.1`). Run the four commands from step 3 again.
Which fail? Which still work? Why does `ping 8.8.8.8` fail while pinging `LNX01` still works? Fix the gateway.

## Submit
- Output of step 3 (working state)
- Output of the same commands with the wrong gateway, and your explanation
- 5 lines: what I learned

## Rubric
| Points | Criterion |
|--------|-----------|
| 3 | Hostname DC01, static IP, internet works, name resolution works |
| 2 | Wrong-gateway experiment: correctly identifies local vs remote traffic |
| 2 | Can explain subnet mask / PrefixLength |
| 2 | Reflection in own words |
| 1 | Clean submission |
