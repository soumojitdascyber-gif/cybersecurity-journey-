# TA0002 - Execution

## What is Execution?

Execution is the stage where an attacker runs malicious code on a target system after gaining initial access.

Goal:

- Execute malware
- Run commands
- Launch scripts
- Establish attacker control

Without execution, the attacker cannot continue the attack chain.

---

## Common Execution Techniques

### 1. PowerShell (T1059.001)

Attackers use PowerShell to:

- Download malware
- Execute scripts
- Contact C2 servers
- Dump credentials

Example:

powershell.exe -enc <Base64>

SOC Detection:

- Event ID 4688
- Sysmon Event ID 1
- Encoded commands
- Office spawning PowerShell

---

### 2. Command and Scripting Interpreter (T1059)

Examples:

- CMD
- PowerShell
- Python
- Bash

Example:

cmd.exe /c whoami

SOC Detection:

- Unusual command execution
- Parent-child process analysis

---

### 3. Windows Management Instrumentation (WMI) (T1047)

Attackers use WMI for:

- Remote execution
- Reconnaissance
- Persistence

Example:

wmic process call create

SOC Detection:

- WMI activity
- Remote process creation

---

### 4. Scheduled Tasks (T1053)

Attackers create tasks to execute malware.

Example:

schtasks /create

SOC Detection:

- New task creation
- Unexpected task execution

---

### 5. User Execution (T1204)

User unknowingly runs malware.

Examples:

- Opening malicious attachment
- Running fake software
- Clicking malicious file

SOC Detection:

- User activity
- Suspicious file execution

---

## Important Log Sources

- Sysmon Event ID 1
- Windows Event ID 4688
- EDR Telemetry
- PowerShell Logs
- Security Logs

---

## SOC Analyst Investigation Process