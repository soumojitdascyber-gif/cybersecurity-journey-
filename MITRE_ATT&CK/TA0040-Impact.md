# TA0040 - Impact

## What is Impact?

Impact is the stage where attackers achieve their final objective by disrupting, destroying, encrypting, or manipulating systems and data.

Goal:

- Cause business disruption
- Encrypt files
- Destroy data
- Damage reputation
- Generate financial loss

Impact is often the most visible stage of an attack.

---

## Attacker Objectives

- Deploy ransomware
- Destroy critical data
- Stop business operations
- Encrypt files
- Disrupt services

---

## Common Impact Techniques

### 1. Data Encrypted for Impact (T1486)

Attackers encrypt files and demand ransom.

Examples:

- LockBit
- Conti
- BlackCat
- WannaCry

SOC Detection:

- Mass file modifications
- Rapid file encryption
- Ransom note creation

---

### 2. Data Destruction (T1485)

Attackers permanently delete data.

Examples:

- File wiping
- Database deletion

SOC Detection:

- Mass deletion events
- Unusual file removal

---

### 3. Service Stop (T1489)

Attackers stop security or business services.

Examples:

- SQL Service
- Backup Service
- Antivirus Service

SOC Detection:

- Service termination
- Unexpected service failures

---

### 4. Disk Wipe (T1561)

Attackers destroy operating systems and disks.

Examples:

- Shamoon
- NotPetya

SOC Detection:

- Disk modification activity
- Boot failure indicators

---

### 5. Defacement (T1491)

Attackers alter websites or applications.

Examples:

- Website defacement
- Message replacement

SOC Detection:

- Website modifications
- Unauthorized changes

---

## Important Log Sources

- EDR
- Sysmon
- Windows Security Logs
- File Integrity Monitoring
- SIEM
- Backup Logs

---

## SOC Analyst Investigation Process

### Step 1

Validate alert.

### Step 2

Identify impact activity.

Questions:

- Encryption?
- Deletion?
- Service disruption?

### Step 3

Review Endpoint Activity.

Questions:

- Which process caused impact?
- Which user initiated activity?

### Step 4

Review Timeline.

Questions:

- Initial Access?
- Persistence?
- Credential Access?
- Exfiltration?

### Step 5

Determine Scope.

Questions:

- Number of affected hosts?
- Number of affected users?

### Step 6

Correlate Evidence.

- EDR
- SIEM
- Sysmon
- Security Logs

### Step 7

Containment

Actions:

- Isolate affected hosts
- Disable compromised accounts
- Block malicious infrastructure

### Step 8

Recovery

Actions:

- Restore backups
- Rebuild systems
- Validate integrity

### Step 9

Escalate

- SOC L2
- Incident Response Team
- Management

---

## Real SOC Example

Alert:

Mass File Encryption Detected

Investigation:

EDR
↓
Thousands of file modifications

Files
↓
.extension.locked

Ransom Note
↓
README_RECOVER_FILES.txt

Timeline
↓
Initial Access → Persistence → Credential Access → Lateral Movement → Encryption

Conclusion:

True Positive

Severity:

Critical

Action:

- Isolate all affected systems
- Disable compromised accounts
- Activate Incident Response Plan

---

## Interview Questions

1. What is Impact in MITRE ATT&CK?
2. What is ransomware?
3. How would you investigate mass file encryption?
4. What is the difference between Exfiltration and Impact?
5. Why are backups important?
6. How would you respond to a ransomware incident?

---

## Key Takeaway

Impact is the final stage where attackers achieve their objective.

If earlier stages are missed, Impact is often where the organization experiences the most damage.