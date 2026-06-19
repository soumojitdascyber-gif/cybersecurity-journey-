# Spear Phishing

## Definition

Spear phishing is a highly targeted phishing attack aimed at a specific individual, department, or organization.

Unlike traditional phishing, spear phishing uses personalized information to increase the chances of success.

---

## Objectives

- Credential theft
- Initial access
- Malware delivery
- Financial fraud
- Corporate espionage

---

## How Spear Phishing Works

1. Attacker gathers information about the victim.
2. Creates a customized phishing email.
3. Uses trusted names, companies, or colleagues.
4. Victim clicks the link or opens the attachment.
5. Attacker gains access to the environment.

---

## Common Information Used

- Employee name
- Job title
- Company name
- Manager name
- Social media information
- Publicly available data

---

## Example

Subject:

"Updated Project Report - Urgent Review Required"

The email appears to come from a manager or colleague and contains a malicious attachment.

---

## Common Indicators

### Personalized Content

- Uses victim's name
- References ongoing projects
- References company activities

### Suspicious Attachments

- .docm
- .xlsm
- .zip
- .iso

### Suspicious Links

- Fake Microsoft 365 pages
- Fake Google login pages
- Fake VPN portals

---

## SOC Analyst Investigation

### Email Analysis

Review:

- Sender address
- Header information
- SPF
- DKIM
- DMARC

### Attachment Analysis

Check:

- File hash
- Sandbox results
- Malware indicators

### URL Analysis

Check:

- Domain age
- Reputation
- Redirect chain

### Endpoint Analysis

Review:

- Process creation
- PowerShell activity
- Network connections
- Registry modifications

---

## Relevant Logs

- Email Logs
- DNS Logs
- Proxy Logs
- Authentication Logs
- EDR Logs
- Sysmon Logs

---

## MITRE ATT&CK

### T1566.001 - Spearphishing Attachment

### T1566.002 - Spearphishing Link

Tactic:

- Initial Access

---

## Detection Techniques

Look for:

- Unusual sender domains
- Suspicious attachments
- External emails targeting executives
- Multiple users receiving similar emails
- Abnormal login activity after email delivery

---

## Prevention

- Security awareness training
- Email filtering
- Multi-Factor Authentication (MFA)
- Attachment sandboxing
- URL reputation checks

---

## Key Takeaway

Spear phishing is more dangerous than traditional phishing because it is specifically designed for the target. The use of personalized information significantly increases the likelihood of a successful compromise.