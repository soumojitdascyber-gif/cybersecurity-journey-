# Clone Phishing

## Definition

Clone phishing is a phishing attack where an attacker copies a legitimate email that was previously sent to a victim and replaces the original attachment or link with a malicious one.

The cloned email appears almost identical to the legitimate email, making it difficult for users to identify the threat.

---

## Objectives

- Credential theft
- Malware delivery
- Initial access
- Account compromise
- Data theft

---

## How Clone Phishing Works

1. Attacker obtains a legitimate email.
2. Copies the email content.
3. Replaces the attachment or URL with a malicious version.
4. Sends the cloned email to the victim.
5. Victim trusts the email and interacts with the malicious content.

---

## Example Scenario

Original Email:

Subject:
Project Report Q2

Attachment:
Q2_Report.pdf

---

Clone Phishing Email:

Subject:
Project Report Q2 (Updated)

Attachment:
Q2_Report.pdf.exe

or

Link:
hxxps://fake-company-sharepoint[.]com

---

## Common Indicators

### Unexpected Updated Documents

The email claims that a previous file has been updated.

### Suspicious Attachments

Examples:

- .exe
- .iso
- .zip
- .docm
- .xlsm

### Suspicious URLs

Fake:

hxxps://micros0ft-login[.]com

Legitimate:

https://microsoft.com

---

## Attack Flow

1. Legitimate email identified.
2. Email cloned.
3. Malicious content inserted.
4. Email delivered.
5. User clicks link or opens attachment.
6. System compromise occurs.

---

## SOC Analyst Investigation

### Email Analysis

Review:

- Sender address
- Reply-To address
- SPF
- DKIM
- DMARC

### Attachment Analysis

Check:

- File hash
- File extension
- Sandbox results
- Malware behavior

### URL Analysis

Investigate:

- Domain reputation
- Redirect chains
- Newly registered domains

### Endpoint Analysis

Review:

- PowerShell activity
- Process creation
- Registry modifications
- Network connections

---

## Relevant Logs

- Email Gateway Logs
- DNS Logs
- Proxy Logs
- Authentication Logs
- EDR Logs
- Sysmon Logs

---

## MITRE ATT&CK

### T1566 - Phishing

### T1566.001 - Spearphishing Attachment

### T1566.002 - Spearphishing Link

Tactic:

- Initial Access

---

## Detection Techniques

Look for:

- Similar email subjects
- Unexpected attachment changes
- Suspicious domains
- Multiple recipients receiving identical emails
- Unusual endpoint behavior after email delivery

---

## Prevention

- Email filtering
- Attachment sandboxing
- URL reputation checks
- Security awareness training
- Multi-Factor Authentication (MFA)

---

## Key Takeaway

Clone phishing is dangerous because it abuses trust in legitimate communications. Since the email closely resembles a real message, users are more likely to interact with malicious links or attachments, leading to compromise.