# Attachment-Based Phishing

## Definition

Attachment-Based Phishing is a phishing attack where attackers deliver malicious files through email attachments to compromise systems, steal credentials, or deploy malware.

The victim is tricked into opening a malicious attachment that appears legitimate.

---

## Objectives

- Malware delivery
- Initial access
- Credential theft
- Ransomware deployment
- Data theft

---

## How Attachment-Based Phishing Works

1. Attacker creates a malicious file.
2. File is attached to a phishing email.
3. Victim opens the attachment.
4. Malicious code executes.
5. System becomes compromised.

---

## Common Malicious File Types

### Executable Files

- .exe
- .msi
- .scr

### Script Files

- .bat
- .cmd
- .js
- .vbs
- .ps1

### Office Documents

- .docm
- .xlsm
- .pptm

### Archive Files

- .zip
- .rar
- .7z
- .iso

### Shortcut Files

- .lnk

---

## Common Attack Scenarios

### Fake Invoice

Subject:

Invoice Payment Required

Attachment:

Invoice.docm

---

### HR Resume Scam

Subject:

Job Application

Attachment:

Resume.zip

---

### Delivery Notification

Subject:

Package Delivery Failed

Attachment:

Delivery_Details.iso

---

## Attack Flow

1. Phishing email delivered.
2. User opens attachment.
3. Macro or script executes.
4. Malware downloaded.
5. Persistence established.
6. Attacker gains access.

---

## SOC Analyst Investigation

### Email Analysis

Review:

- Sender address
- Email headers
- SPF
- DKIM
- DMARC

---

### Attachment Analysis

Check:

- File hash
- File extension
- File reputation
- Sandbox results

---

### Endpoint Analysis

Review:

- Process creation
- PowerShell execution
- Registry modifications
- Persistence mechanisms

---

### Network Analysis

Investigate:

- DNS requests
- C2 communications
- Suspicious outbound traffic

---

## Important Sysmon Events

### Event ID 1

Process Creation

Example:

winword.exe → powershell.exe

---

### Event ID 3

Network Connection

Detects outbound connections.

---

### Event ID 7

Image Loaded

Useful for DLL analysis.

---

### Event ID 11

File Creation

Detects file creation activities.

---

### Event ID 13

Registry Value Set

Detects persistence attempts.

---

## Relevant Logs

- Email Gateway Logs
- DNS Logs
- Proxy Logs
- EDR Logs
- Sysmon Logs
- Windows Security Logs

---

## MITRE ATT&CK

### T1566.001 - Spearphishing Attachment

### T1204 - User Execution

### T1059 - Command and Scripting Interpreter

Tactics:

- Initial Access
- Execution

---

## Detection Techniques

Look for:

- Office spawning PowerShell
- Suspicious macro execution
- Script execution from temp folders
- New outbound connections
- Fileless malware activity

---

## Prevention

- Email filtering
- Attachment sandboxing
- Macro restrictions
- User awareness training
- Endpoint protection

---

## Key Takeaway

Attachment-Based Phishing remains one of the most effective attack methods because it combines social engineering with malware delivery. SOC analysts should focus on attachment analysis, process execution, and network activity to identify and contain threats quickly.