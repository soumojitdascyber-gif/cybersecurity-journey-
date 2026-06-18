# TA0005 - Defense Evasion

## What is Defense Evasion?

Defense Evasion is the stage where attackers attempt to avoid detection by security tools, analysts, and monitoring systems.

Goal:

- Hide malicious activity
- Bypass security controls
- Avoid detection
- Continue attack operations

---

## Attacker Objectives

- Evade EDR detection
- Evade Antivirus
- Evade SIEM alerts
- Remain hidden

---

## Common Defense Evasion Techniques

### 1. Obfuscated Files or Information (T1027)

Attackers hide malicious code.

Examples:

- Base64 Encoding
- Packed Malware
- Encrypted Scripts

SOC Detection:

- Encoded PowerShell
- Suspicious command lines

---

### 2. Disable Security Tools (T1562)

Attackers disable:

- Windows Defender
- EDR
- Antivirus

Example:

Disable Defender using PowerShell

SOC Detection:

- Security service stopped
- Defender disabled

---

### 3. Clear Windows Event Logs (T1070.001)

Attackers remove evidence.

Example:

wevtutil cl Security

SOC Detection:

- Event ID 1102
- Log clearing activity

---

### 4. Masquerading (T1036)

Attackers rename malware to look legitimate.

Examples:

svch0st.exe
explorer_update.exe

SOC Detection:

- Unusual file paths
- Suspicious parent-child process

---

### 5. Indicator Removal on Host (T1070)

Attackers delete:

- Logs
- Scripts
- Malware artifacts

SOC Detection:

- File deletion events
- Missing logs

---

## Important Log Sources

- EDR Telemetry
- Windows Security Logs
- Sysmon
- Defender Logs
- SIEM

---

## SOC Analyst Investigation Process

### Step 1

Validate alert.

### Step 2

Identify evasion activity.

Questions:

- Log cleared?
- Defender disabled?
- Encoded PowerShell?

### Step 3

Review Process Activity.

Questions:

- Parent process?
- Command line?

### Step 4

Review Timeline.

Questions:

- What happened before evasion?

### Step 5

Correlate Evidence.

- EDR
- SIEM
- Sysmon

### Step 6

Determine:

- True Positive
- False Positive

### Step 7

Containment

Actions:

- Isolate endpoint
- Re-enable security controls
- Kill malicious process

### Step 8

Escalate if required

---

## Real SOC Example

Alert:

Windows Event Logs Cleared

Investigation:

Event ID 1102
↓
Security Log Cleared

EDR
↓
PowerShell executed

Timeline
↓
Credential dumping detected before log clearing

Conclusion:

True Positive

Action:

- Isolate endpoint
- Escalate to SOC L2
- Preserve evidence

---

## Interview Questions

1. What is Defense Evasion?
2. Why do attackers clear logs?
3. What Event ID indicates Security Log clearing?
4. What is Masquerading?
5. How would you investigate a Defender disable alert?

---

## Key Takeaway

Defense Evasion helps attackers stay hidden.

A successful attacker is often the one who remains undetected the longest.