# TA0003 - Persistence

## What is Persistence?

Persistence is the stage where an attacker ensures continued access to a compromised system even after reboot, logout, password change, or system restart.

Goal:

- Maintain access
- Survive reboots
- Avoid losing foothold
- Return later without re-exploitation

Without Persistence, attackers may lose access to the system.

---

## Attacker Objectives

- Long-term access
- Maintain control
- Survive system reboot
- Prepare for future actions

---

## Common Persistence Techniques

### 1. Registry Run Keys (T1547.001)

Attackers modify registry keys to launch malware automatically during startup.

Example:

HKCU\Software\Microsoft\Windows\CurrentVersion\Run

SOC Detection:

- Registry modifications
- Autorun entries
- Sysmon Event ID 13

---

### 2. Startup Folder (T1547.001)

Attackers place malicious files inside startup folders.

Example:

Startup Folder

C:\Users\User\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup

SOC Detection:

- New startup files
- Unexpected executables

---

### 3. Scheduled Tasks (T1053)

Attackers create tasks that execute automatically.

Example:

schtasks /create

SOC Detection:

- New task creation
- Unusual scheduled tasks

Windows Event IDs:

- 4698
- 4702

---

### 4. Windows Services (T1543)

Attackers create or modify services.

Example:

sc create malware_service

SOC Detection:

- New services
- Service modifications

Windows Event ID:

7045

---

### 5. WMI Event Subscription (T1546)

Attackers create WMI subscriptions for persistence.

SOC Detection:

- WMI activity
- Unexpected WMI subscriptions

---

## Important Log Sources

- Sysmon
- Windows Security Logs
- EDR Telemetry
- Registry Logs
- Service Creation Logs

---

## SOC Analyst Investigation Process

### Step 1

Validate alert.

### Step 2

Identify persistence mechanism.

Questions:

- Registry?
- Service?
- Scheduled Task?
- Startup Folder?

### Step 3

Review Process History.

Questions:

- Which process created persistence?
- Parent process?

### Step 4

Check Timeline.

Questions:

- When was persistence created?
- Was PowerShell involved?

### Step 5

Review User Activity.

Questions:

- Legitimate admin action?
- Malicious behavior?

### Step 6

Correlate Evidence.

- SIEM
- EDR
- Sysmon

### Step 7

Determine:

- True Positive
- False Positive

### Step 8

Containment.

Actions:

- Remove persistence
- Isolate endpoint
- Kill related processes

### Step 9

Escalate if required.

---

## Real SOC Example

Alert:

New Scheduled Task Created

Investigation:

Windows