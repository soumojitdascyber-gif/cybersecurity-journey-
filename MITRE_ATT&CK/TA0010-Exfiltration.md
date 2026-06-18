# TA0010 - Exfiltration

## What is Exfiltration?

Exfiltration is the stage where attackers transfer stolen data from the victim environment to an external destination.

Goal:

- Steal sensitive information
- Transfer collected data
- Avoid detection
- Complete attack objectives

Exfiltration is often the final stage before attackers achieve their mission.

---

## Attacker Objectives

- Steal company data
- Steal customer information
- Transfer credentials
- Leak financial records
- Expose intellectual property

---

## Common Exfiltration Techniques

### 1. Exfiltration Over Web Services (T1567)

Attackers use:

- Dropbox
- Google Drive
- OneDrive
- Mega

SOC Detection:

- Large uploads
- Unusual cloud usage
- Suspicious outbound traffic

---

### 2. Exfiltration Over C2 Channel (T1041)

Attackers send stolen data through existing C2 channels.

Examples:

- HTTP
- HTTPS
- DNS

SOC Detection:

- Large outbound traffic
- Suspicious beaconing
- Data transfers to malicious domains

---

### 3. DNS Exfiltration (T1048)

Attackers hide stolen data inside DNS requests.

Example:

passwords.company.attacker.com

SOC Detection:

- Long DNS queries
- High DNS request volume
- Encoded subdomains

---

### 4. Exfiltration to Cloud Storage

Attackers upload stolen files to cloud services.

Examples:

- Google Drive
- Dropbox
- Mega

SOC Detection:

- Unexpected uploads
- Large outbound transfers

---

### 5. Archive and Compress Data (T1560)

Before exfiltration attackers often:

- ZIP files
- Compress folders
- Encrypt archives

Tools:

- WinRAR
- 7-Zip
- ZIP

SOC Detection:

- Large archive creation
- Unusual compression activity

---

## Important Log Sources

- DNS Logs
- Firewall Logs
- Proxy Logs
- EDR
- SIEM
- NetFlow
- Cloud Logs

---

## SOC Analyst Investigation Process

### Step 1

Validate alert.

### Step 2

Identify outbound transfer.

Questions:

- What data left?
- Where was it sent?

### Step 3

Review Destination.

Questions:

- Cloud service?
- Suspicious domain?
- Threat intelligence match?

### Step 4

Review File Activity.

Questions:

- Which files accessed?
- Archive created?

### Step 5

Review Timeline.

Questions:

- Collection occurred earlier?
- C2 communication present?

### Step 6

Correlate Evidence.

- DNS Logs
- Firewall Logs
- EDR
- SIEM

### Step 7

Determine:

- True Positive
- False Positive

### Step 8

Containment

Actions:

- Block destination
- Isolate endpoint
- Disable compromised account

### Step 9

Escalate if required

---

## Real SOC Example

Alert:

Large Outbound DNS Traffic

Investigation:

DNS Logs
↓
Thousands of long DNS queries

EDR
↓
7zip.exe created archive

Timeline
↓
Collection activity detected earlier

Threat Intelligence
↓
Destination domain malicious

Conclusion:

True Positive

Action:

- Block domain
- Isolate endpoint
- Escalate to SOC L2

---

## Interview Questions

1. What is Exfiltration?
2. Why do attackers compress files before exfiltration?
3. What is DNS Exfiltration?
4. How would you investigate large outbound traffic?
5. Which logs help detect data theft?
6. Difference between Collection and Exfiltration?

---

## Key Takeaway

Exfiltration is the stage where attackers steal data from the environment.

Detecting Exfiltration quickly can prevent major data breaches and business impact.