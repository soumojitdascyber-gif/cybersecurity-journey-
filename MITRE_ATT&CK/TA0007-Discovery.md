# TA0007 - Discovery

## What is Discovery?

Discovery is the stage where attackers gather information about the compromised environment.

Goal:

- Identify users
- Identify computers
- Identify servers
- Identify privileges
- Map the network

Before moving deeper into a network, attackers first need to understand their environment.

---

## Attacker Objectives

- Find valuable targets
- Identify privileged users
- Discover domain controllers
- Locate sensitive systems
- Plan lateral movement

---

## Common Discovery Techniques

### 1. Account Discovery (T1087)

Attackers identify users and accounts.

Commands:

whoami

net user

query user

SOC Detection:

- User enumeration
- Unusual account discovery

---

### 2. System Information Discovery (T1082)

Attackers gather system information.

Commands:

systeminfo

hostname

ver

SOC Detection:

- Reconnaissance commands
- Suspicious command execution

---

### 3. Network Service Discovery (T1046)

Attackers identify active systems and services.

Commands:

ping

net view

nmap

SOC Detection:

- Port scanning
- Service enumeration

---

### 4. Network Configuration Discovery (T1016)

Attackers gather network information.

Commands:

ipconfig

route print

arp -a

SOC Detection:

- Network reconnaissance activity

---

### 5. Domain Trust Discovery (T1482)

Attackers identify domain relationships.

Commands:

nltest

Get-ADDomain

SOC Detection:

- Active Directory enumeration

---

### 6. Group Discovery (T1069)

Attackers identify privileged groups.

Commands:

net group

Get-ADGroup

SOC Detection:

- Privileged group enumeration

---

## Important Log Sources

- EDR
- Sysmon
- Windows Security Logs
- PowerShell Logs
- Active Directory Logs
- SIEM

---

## SOC Analyst Investigation Process

### Step 1

Validate alert.

### Step 2

Identify discovery activity.

Questions:

- Which command was executed?
- Which user executed it?

### Step 3

Review Parent Process.

Questions:

- Was PowerShell involved?
- Was CMD involved?

### Step 4

Review Timeline.

Questions:

- What happened before discovery?
- Any phishing activity?

### Step 5

Correlate Evidence.

- EDR
- Sysmon
- SIEM
- AD Logs

### Step 6

Determine:

- True Positive
- False Positive

### Step 7

Containment

Actions:

- Isolate endpoint
- Monitor affected account
- Investigate further activity

### Step 8

Escalate if required

---

## Real SOC Example

Alert:

Suspicious Discovery Activity

Investigation:

4688 Process Creation
↓
cmd.exe

Commands:
↓
whoami
ipconfig
net user
net group

EDR
↓
Multiple reconnaissance commands detected

Timeline
↓
PowerShell execution occurred earlier

Conclusion:

True Positive

Action:

- Isolate endpoint
- Escalate to SOC L2

---

## Interview Questions

1. What is Discovery?
2. Why do attackers perform Discovery?
3. What does whoami do?
4. What information does ipconfig provide?
5. Why is net user important during investigations?
6. How would you investigate suspicious reconnaissance activity?

---

## Key Takeaway

Discovery helps attackers understand the environment before moving further.

Many attacks become visible when attackers start enumerating users, systems, groups, and network information.