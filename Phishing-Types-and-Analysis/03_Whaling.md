# Whaling

## Definition

Whaling is a highly targeted phishing attack that focuses on high-profile individuals such as CEOs, CFOs, directors, executives, and senior management personnel.

Because these individuals often have access to sensitive information and financial resources, they are considered "big fish" or "whales."

---

## Objectives

- Financial fraud
- Business Email Compromise (BEC)
- Credential theft
- Data theft
- Executive account compromise

---

## Why Executives Are Targeted

Executives usually have:

- Access to sensitive data
- Financial approval authority
- High-level privileges
- Access to strategic business information

A successful compromise can cause significant financial and reputational damage.

---

## How Whaling Attacks Work

1. Attacker researches the executive.
2. Collects information from LinkedIn, company websites, and social media.
3. Creates a convincing phishing email.
4. Sends a fake invoice, legal notice, or urgent request.
5. Victim clicks the link or opens the attachment.
6. Attacker gains access or steals information.

---

## Common Whaling Scenarios

### Fake CEO Email

An attacker impersonates the CEO and requests an urgent fund transfer.

### Legal Notice Scam

The executive receives a fake legal complaint requiring immediate review.

### Tax or Financial Documents

Fake financial reports containing malicious attachments.

---

## Common Indicators

- Urgent financial requests
- Executive impersonation
- External sender pretending to be internal
- Unusual payment instructions
- Unexpected confidential document requests

---

## SOC Analyst Investigation

### Email Analysis

Review:

- Sender domain
- Return path
- SPF
- DKIM
- DMARC

### Attachment Analysis

Check:

- File hash
- Sandbox results
- Malware behavior

### Authentication Analysis

Investigate:

- Successful logins
- Failed login attempts
- Impossible travel events
- MFA bypass attempts

### Endpoint Analysis

Review:

- PowerShell execution
- Process creation
- Network connections
- Persistence mechanisms

---

## Relevant Logs

- Email Security Logs
- Authentication Logs
- DNS Logs
- Proxy Logs
- EDR Logs
- Sysmon Logs

---

## MITRE ATT&CK

### T1566 - Phishing

### T1586 - Compromise Accounts

Tactics:

- Initial Access
- Credential Access

---

## Detection Techniques

Look for:

- Executive impersonation
- Unusual financial requests
- External domains resembling internal domains
- Abnormal executive account activity
- Login attempts from unusual locations

---

## Prevention

- Executive security awareness training
- MFA implementation
- Email security controls
- Domain monitoring
- Financial verification procedures

---

## Key Takeaway

Whaling is one of the most dangerous phishing attacks because it targets high-value individuals with elevated privileges. A successful whaling attack can lead to financial loss, data breaches, and organizational compromise.