# Email Phishing

## Definition

Email phishing is a social engineering attack where attackers send fraudulent emails to trick victims into revealing sensitive information, downloading malware, or visiting malicious websites.

Email phishing is one of the most common initial access techniques used by cybercriminals and threat actors.

---

## Objectives of Email Phishing

- Steal credentials
- Deliver malware
- Gain initial access
- Financial fraud
- Data theft

---

## Common Indicators

### Suspicious Sender Address

Example:

support@micr0soft-security.com

Instead of:

support@microsoft.com

---

### Urgent Language

Examples:

- Your account will be suspended
- Immediate action required
- Verify your account now

---

### Suspicious Links

Examples:

- hxxps://microsooft-login[.]com
- hxxps://secure-update-account[.]com

---

### Unexpected Attachments

Common malicious attachment types:

- .exe
- .zip
- .iso
- .docm
- .xlsm
- .js

---

## Email Phishing Attack Flow

1. Attacker creates a phishing email.
2. Victim receives the email.
3. Victim clicks a malicious link or attachment.
4. Credentials or system access are compromised.
5. Attacker gains initial access.

---

## SOC Analyst Investigation

### Check Email Header

Analyze:

- Sender IP
- Return Path
- SPF
- DKIM
- DMARC

### Check URLs

Investigate:

- Domain reputation
- URL redirects
- Typosquatting domains

### Check Attachments

Analyze:

- File hash
- File type
- Sandbox results

### Check User Activity

Verify:

- Link clicked or not
- File executed or not
- Credential entered or not

---

## Relevant Logs

- Email Gateway Logs
- Proxy Logs
- DNS Logs
- Authentication Logs
- EDR Logs
- Sysmon Logs

---

## MITRE ATT&CK

### T1566 - Phishing

Tactic:

- Initial Access

---

## Detection Tips

Look for:

- Multiple phishing emails
- Suspicious attachments
- New external domains
- Credential harvesting attempts
- Unusual authentication activity

---

## Key Takeaway

Email phishing remains one of the most successful attack methods because it targets human behavior rather than technical vulnerabilities. SOC analysts must investigate phishing alerts carefully to determine whether the activity is a false positive or a genuine security incident.