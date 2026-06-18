# TA0009 - Collection

## What is Collection?

Collection is the stage where attackers gather valuable data before stealing it from the environment.

Goal:

- Collect sensitive files
- Gather credentials
- Capture screenshots
- Collect business data
- Prepare for Exfiltration

Collection usually happens before Data Exfiltration.

---

## Attacker Objectives

- Gather sensitive documents
- Locate financial data
- Capture credentials
- Collect screenshots
- Identify valuable information

---

## Common Collection Techniques

### 1. Data from Local System (T1005)

Attackers collect files from the compromised host.

Examples:

- PDF files
- Excel files
- Documents
- Databases

SOC Detection:

- Unusual file access
- Bulk file reads

---

### 2. Data from Network Shared Drive (T1039)

Attackers access shared folders.

Examples:

- HR Share
- Finance Share
- Executive Share

SOC Detection:

- Large file access
- Unusual network share activity

---

### 3. Screen Capture (T1113)

Attackers take screenshots.

Goal:

- Capture sensitive information
- Gather credentials

SOC Detection:

- Screenshot utilities
- Suspicious user activity

---

### 4. Clipboard Collection (T1115)

Attackers collect clipboard contents.

Examples:

- Passwords
- Sensitive text

SOC Detection:

- Clipboard monitoring tools
- EDR alerts

---

### 5. Archive Collected Data (T1560)

Attackers compress data before exfiltration.

Examples:

zip
rar
7z

SOC Detection:

- Large archive creation
- Unusual compression activity

---

## Important Log Sources

- EDR
- File Access Logs
- Sysmon
- Windows Security Logs
- SIEM

---

## SOC Analyst Investigation Process

### Step 1

Validate alert.

### Step 2

Identify collected data.

Questions:

- Which files were accessed?
- Which shares were accessed?

### Step 3

Review User Activity.

Questions:

- Legitimate business activity?
- Suspicious access pattern?

### Step 4

Review Process Activity.

Questions:

- Archive tools used?
- PowerShell involved?

### Step 5

Review Timeline.

Questions:

- Discovery occurred earlier?
- Lateral Movement detected?

### Step 6

Correlate Evidence.

- EDR
- SIEM
- File Logs
- Sysmon

### Step 7

Determine:

- True Positive
- False Positive

### Step 8

Containment

Actions:

- Isolate endpoint
- Disable account
- Preserve evidence

### Step 9

Escalate if required

---

## Real SOC Example

Alert:

Mass File Access Detected

Investigation:

EDR
↓
User accessed 500+ files

File Logs
↓
Finance Share accessed

Process Activity
↓
7zip.exe executed

Timeline
↓
Discovery and Lateral Movement occurred earlier

Conclusion:

True Positive

Action:

- Isolate endpoint
- Disable account
- Escalate to SOC L2

---

## Interview Questions

1. What is Collection?
2. Why do attackers collect data?
3. What is Archive Collected Data?
4. Why are screenshots valuable to attackers?
5. How would you investigate mass file access?
6. Which logs help detect Collection activity?

---

## Key Takeaway

Collection is the stage where attackers gather valuable information before stealing it.

Detecting Collection early can stop Data Exfiltration and reduce business impact.