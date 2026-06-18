# TA0008 - Lateral Movement

## What is Lateral Movement?

Lateral Movement is the stage where attackers move from one compromised system to another system inside the network.

Goal:

- Expand access
- Reach critical systems
- Find Domain Controllers
- Access sensitive data
- Increase attack impact

After gaining access to one machine, attackers rarely stop there.

---

## Attacker Objectives

- Access more systems
- Reach privileged accounts
- Find Domain Controllers
- Access critical servers
- Prepare for exfiltration

---

## Common Lateral Movement Techniques

### 1. Remote Desktop Protocol (RDP) (T1021.001)

Attackers use RDP to access remote systems.

Example:

mstsc.exe

SOC Detection:

- Unusual RDP logins
- New source locations
- After-hours access

---

### 2. SMB / Windows Admin Shares (T1021.002)

Attackers move files and execute commands through SMB.

Examples:

ADMIN$
C$
IPC$

SOC Detection:

- SMB connections
- Unusual file transfers
- Administrative share access

---

### 3. PsExec (T1569)

PsExec allows remote command execution.

Example:

psexec.exe

SOC Detection:

- Service creation
- Remote process execution
- Administrative activity

---

### 4. Remote Services

Examples:

- WinRM
- SSH
- RDP

SOC Detection:

- New remote sessions
- Unexpected authentication activity

---

### 5. Pass-the-Hash

Attackers use password hashes instead of passwords.

Goal:

- Authenticate without knowing password

SOC Detection:

- Authentication anomalies
- Suspicious lateral logins

---

## Important Log Sources

- Windows Security Logs
- EDR
- Sysmon
- Authentication Logs
- Active Directory Logs
- Firewall Logs

---

## SOC Analyst Investigation Process

### Step 1

Validate alert.

### Step 2

Identify lateral movement activity.

Questions:

- Which host initiated connection?
- Which host received connection?

### Step 3

Review Authentication Logs.

Questions:

- Which account was used?
- Was login expected?

### Step 4

Review Endpoint Activity.

Questions:

- PsExec?
- RDP?
- SMB?

### Step 5

Review Timeline.

Questions:

- Credential theft occurred earlier?
- Discovery activity observed?

### Step 6

Correlate Evidence.

- SIEM
- EDR
- Sysmon
- AD Logs

### Step 7

Determine:

- True Positive
- False Positive

### Step 8

Containment

Actions:

- Isolate affected hosts
- Disable compromised accounts
- Block remote access

### Step 9

Escalate if required

---

## Real SOC Example

Alert:

Suspicious RDP Login

Investigation:

Authentication Logs
↓
User logged into 5 systems within 10 minutes

EDR
↓
Credential dumping detected earlier

Timeline
↓
Discovery activity before login

Conclusion:

True Positive

Action:

- Disable account
- Isolate systems
- Escalate to SOC L2

---

## Interview Questions

1. What is Lateral Movement?
2. Why do attackers perform Lateral Movement?
3. What is PsExec?
4. What is Pass-the-Hash?
5. How would you investigate suspicious RDP activity?
6. Which logs are useful for detecting Lateral Movement?

---

## Key Takeaway

Lateral Movement allows attackers to expand control across the network.

Early detection can prevent attackers from reaching critical servers and Domain Controllers.