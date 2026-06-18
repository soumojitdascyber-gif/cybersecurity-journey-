# TA0004 - Privilege Escalation

## What is Privilege Escalation?

Privilege Escalation is the process where an attacker gains higher permissions than originally granted.

Goal:

- Gain Administrator privileges
- Gain SYSTEM privileges
- Access restricted resources
- Disable security controls

Without Privilege Escalation, attackers are often limited in what they can do.

---

## Attacker Objectives

- Become Administrator
- Become SYSTEM
- Access sensitive data
- Dump credentials
- Move laterally

---

## Common Privilege Escalation Techniques

### 1. Valid Accounts (T1078)

Attackers abuse privileged accounts.

Examples:

- Domain Admin
- Local Administrator

SOC Detection:

- Unexpected admin logins
- Privileged account abuse

---

### 2. Token Manipulation (T1134)

Attackers steal or impersonate access tokens.

Purpose:

- Gain higher privileges
- Bypass restrictions

SOC Detection:

- Privilege changes
- Suspicious process access

---

### 3. Exploitation for Privilege Escalation (T1068)

Attackers exploit OS vulnerabilities.

Examples:

- Windows privilege escalation exploits
- Kernel vulnerabilities

SOC Detection:

- Exploit activity
- Suspicious process behavior

---

### 4. Access Token Theft

Attackers steal tokens from privileged processes.

SOC Detection:

- LSASS access attempts
- Sysmon Event ID 10

---

### 5. UAC Bypass

Attackers bypass User Account Control.

SOC Detection:

- Unexpected elevated processes
- UAC bypass indicators

---

## Important Log Sources

- Windows Security Logs
- Sysmon
- EDR Telemetry
- Authentication Logs
- Privileged Account Logs

---

## SOC Analyst Investigation Process

### Step 1

Validate alert.

### Step 2

Identify privilege escalation activity.

Questions:

- New admin account?
- Token abuse?
- UAC bypass?

### Step 3

Review Authentication Logs.

Questions:

- Which account gained privileges?
- Was login expected?

### Step 4

Review Process Activity.

Questions:

- Which process triggered escalation?
- Parent-child relationship?

### Step 5

Check Timeline.

Questions:

- What happened before escalation?
- Any PowerShell activity?

### Step 6

Correlate Evidence.

- SIEM
- EDR
- Sysmon
- Security Logs

### Step 7

Determine:

- True Positive
- False Positive

### Step 8

Containment

Actions:

- Disable account
- Isolate endpoint
- Revoke privileges

### Step 9

Escalate if required

---

## Real SOC Example

Alert:

New User Added to Domain Admins Group

Investigation:

Windows Event ID 4728
↓
User added to privileged group

Authentication Logs
↓
Unusual admin activity

EDR
↓
PowerShell execution detected

Conclusion:

True Positive

Action:

- Remove user from group
- Disable account
- Isolate endpoint
- Escalate to SOC L2

---

## Interview Questions

1. What is Privilege Escalation?
2. Why do attackers need Privilege Escalation?
3. What is Token Manipulation?
4. What Event IDs indicate privilege changes?
5. How would you investigate a Domain Admin creation alert?
6. What is UAC Bypass?

---

## Key Takeaway

Privilege Escalation allows attackers to gain higher permissions and deeper control over a system.

Detecting Privilege Escalation early can prevent credential theft, lateral movement, and domain compromise.