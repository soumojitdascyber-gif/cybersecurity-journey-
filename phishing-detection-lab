# 🚨 Phishing Detection & Analysis Lab

## 📌 Overview
This repository demonstrates how phishing attacks are detected, analyzed, and investigated from a SOC analyst perspective. The project focuses on phishing attack chains, endpoint behavior, network indicators, and incident response techniques used in modern cybersecurity operations.

---

# ⚔️ What is Phishing?

Phishing is a social engineering attack used by threat actors to:
- Steal credentials
- Deploy malware
- Gain unauthorized access
- Establish persistence
- Perform data exfiltration

Modern phishing attacks combine:
- Social engineering
- Malware delivery
- PowerShell abuse
- Command & Control (C2)
- Defense evasion techniques

to compromise systems and users.

---

# 🔥 Phishing Attack Lifecycle

## 1. Reconnaissance
Attackers collect information about targets:
- Email addresses
- Company information
- Employee roles
- Social media data

Goal:
Increase phishing success rate.

---

## 2. Delivery
The malicious payload is delivered through:
- Email attachments
- Fake login pages
- SMS messages
- QR codes
- Social engineering messages

Common attachment types:
- `.docm`
- `.xlsm`
- `.zip`
- `.html`

---

## 3. Execution
Victim opens the attachment or clicks the malicious link.

Suspicious behaviors:
```text
winword.exe → powershell.exe
excel.exe → cmd.exe
```

Indicators:
- Encoded PowerShell
- Script execution
- Macro abuse
- Fileless malware

---

## 4. Credential Theft / Malware Execution

Attackers may:
- Steal credentials
- Execute malware
- Download payloads
- Abuse legitimate Windows tools

Common LOLBins:
- powershell.exe
- mshta.exe
- rundll32.exe
- certutil.exe

---

## 5. Persistence
Attackers maintain access using:
- Registry Run Keys
- Scheduled Tasks
- Startup folders
- WMI Event Subscriptions

---

## 6. Command & Control (C2)

The infected system communicates with attacker infrastructure.

Indicators:
- Beaconing traffic
- Rare domains
- HTTPS communication
- DNS anomalies
- Fixed interval connections

Example:
```text
Host connects to external IP every 60 seconds
```

---

# 🧠 Types of Phishing

## 🎯 Spear Phishing
Targeted phishing against specific users or organizations.

---

## 👑 Whaling
Phishing attacks targeting executives or high-level employees.

---

## 📱 Smishing
SMS-based phishing attacks.

---

## 📞 Vishing
Voice-call phishing attacks.

---

## 🌐 Clone Phishing
Legitimate emails cloned and modified with malicious content.

---

## 💼 Business Email Compromise (BEC)
Attackers compromise business communication for financial fraud or credential theft.

---

# 🔍 Detection Techniques

## 📧 Email Indicators
- Suspicious sender domain
- Misspelled domains
- Urgent language
- Unexpected attachments
- Fake login pages

Example:
```text
micr0soft-support.com
```

---

## 💻 Endpoint Indicators

### Suspicious Process Chains
```text
winword.exe → powershell.exe
excel.exe → cmd.exe
```

### Additional Indicators
- Encoded PowerShell
- LSASS memory access
- Unusual child processes
- Scheduled task creation

---

## 🌐 Network Indicators

### DNS Indicators
```text
ajd92k.domain.com
pqowie.domain.com
```

Possible signs:
- DNS tunneling
- Beaconing
- Malware communication

### C2 Indicators
- Fixed interval traffic
- Rare outbound connections
- Encrypted HTTPS communication

---

# 🛡️ Detection Tools

## Sysmon
Used for:
- Process creation monitoring
- Network connection logs
- PowerShell activity analysis

Important Event IDs:
- Event ID 1 → Process Creation
- Event ID 3 → Network Connection
- Event ID 7 → Image Load
- Event ID 11 → File Creation

---

## SIEM Platforms
- Splunk
- ELK Stack
- Microsoft Sentinel

Used for:
- Threat detection
- Alert correlation
- Log analysis
- Threat hunting

---

## EDR Solutions
- Microsoft Defender
- CrowdStrike
- SentinelOne

Used for:
- Behavioral detection
- Endpoint visibility
- Incident response

---

# ⚡ Incident Response Workflow

## Step 1: Identification
- Validate alerts
- Review logs
- Identify malicious activity

---

## Step 2: Containment
- Isolate infected host
- Block malicious IP/domain
- Disable compromised accounts

---

## Step 3: Eradication
- Remove malware
- Delete persistence
- Reset credentials

---

## Step 4: Recovery
- Restore systems
- Monitor for reinfection

---

## Step 5: Lessons Learned
- Improve detections
- Enhance security awareness
- Update defensive controls

---

# 🧠 MITRE ATT&CK Mapping

| Tactic | Technique |
|--------|-----------|
| Initial Access | Phishing |
| Execution | PowerShell |
| Persistence | Scheduled Task |
| Defense Evasion | Obfuscation |
| Credential Access | Credential Dumping |
| Lateral Movement | PsExec |
| Command & Control | HTTPS Beaconing |

---

# 🚨 Common SOC Investigation Questions

- Did the user interact with the attachment?
- Was PowerShell executed?
- Were any external connections established?
- Was persistence created?
- Was lateral movement attempted?
- Were credentials compromised?

---

# 🎯 Learning Outcomes

- Understanding phishing attack chains
- Detecting malicious behavior
- Investigating suspicious logs
- Understanding SOC workflows
- Improving threat detection skills

---

# 📌 Disclaimer
This project is created strictly for educational and defensive cybersecurity purposes only.