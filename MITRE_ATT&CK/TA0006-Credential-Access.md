# TA0006 - Credential Access

## What is Credential Access?

Credential Access is the stage where attackers attempt to steal usernames, passwords, tokens, hashes, and authentication secrets.

Goal:

- Steal credentials
- Gain privileged access
- Move laterally
- Access critical systems

---

## Attacker Objectives

- Obtain passwords
- Dump hashes
- Steal tokens
- Gain domain access
- Become Domain Admin

---

## Common Credential Access Techniques

### 1. LSASS Memory Dumping (T1003.001)

LSASS stores authentication information in memory.

Attackers dump LSASS to extract credentials.

Tools:

- Mimikatz
- ProcDump

SOC Detection:

- Sysmon Event ID 10
- LSASS access attempts
- EDR alerts

---

### 2. Credential Dumping (T1003)

Attackers dump credentials from:

- SAM Database
- LSASS
- Cached Credentials

SOC Detection:

- Suspicious process access
- Mimikatz indicators

---

### 3. Brute Force (T1110)

Attackers attempt multiple passwords.

Examples:

- VPN Brute Force
- RDP Brute Force
- O365 Brute Force

SOC Detection:

- Multiple failed logins
- Account lockouts
- Authentication anomalies

---

### 4. Password Spraying (T1110.003)

Attackers use one password against many accounts.

Example:

Password = Welcome123

Users:

- user1
- user2
- user3

SOC Detection:

- Same password attempt pattern
- Multiple account failures

---

### 5. Input Capture / Keylogging (T1056)

Attackers record user keystrokes.

Goal:

- Steal credentials
- Capture sensitive information

SOC Detection:

- Suspicious keyboard hooks
- EDR behavioral alerts

---

## Important Log Sources

- EDR
- Sysmon
- Windows Security Logs
- Authentication Logs
- VPN Logs
- Active Directory Logs

---

## SOC Analyst Investigation Process

### Step 1

Validate alert.

### Step 2

Identify credential theft indicators.

Questions:

- LSASS accessed?
- Brute force observed?
- Password spraying activity?

### Step 3

Review Authentication Logs.

Questions:

- Failed logins?
- Successful login after failures?

### Step 4

Review Endpoint Activity.

Questions:

- Mimikatz?
- ProcDump?
- PowerShell abuse?

### Step 5

Correlate Evidence.

- EDR
- SIEM
- Sysmon
- Authentication Logs

### Step 6

Determine:

- True Positive
- False Positive

### Step 7

Containment

Actions:

- Disable affected account
- Reset passwords
- Isolate endpoint

### Step 8

Escalate if required

---

## Real SOC Example

Alert:

LSASS Access Detected

Investigation:

Sysmon Event ID 10
↓
powershell.exe accessing lsass.exe

EDR
↓
Credential Dumping Alert

Timeline
↓
PowerShell executed before LSASS access

Conclusion:

True Positive

Action:

- Isolate endpoint
- Reset credentials
- Escalate to SOC L2

---

## Interview Questions

1. What is Credential Access?
2. What is LSASS?
3. Why do attackers target LSASS?
4. What is Password Spraying?
5. Difference between Brute Force and Password Spraying?
6. How would you investigate a credential dumping alert?

---

## Key Takeaway

Credentials are one of the most valuable assets for attackers.

If attackers steal credentials, they can often move throughout the environment without exploiting additional vulnerabilities.