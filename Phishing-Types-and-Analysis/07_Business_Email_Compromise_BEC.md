# Business Email Compromise (BEC)

## Definition

Business Email Compromise (BEC) is a sophisticated cyberattack where attackers impersonate trusted individuals such as executives, vendors, suppliers, or business partners to manipulate employees into transferring money, sharing sensitive information, or performing unauthorized actions.

BEC attacks often rely on social engineering rather than malware.

---

## Objectives

- Financial fraud
- Wire transfer fraud
- Invoice fraud
- Credential theft
- Sensitive data theft

---

## How BEC Works

1. Attacker researches the target organization.
2. Identifies executives, finance teams, or vendors.
3. Creates a convincing email impersonating a trusted person.
4. Requests an urgent payment or sensitive information.
5. Victim complies with the request.
6. Organization suffers financial or data loss.

---

## Common BEC Scenarios

### CEO Fraud

An attacker impersonates the CEO and requests an urgent wire transfer.

Example:

"Please transfer ₹5,00,000 immediately. This is confidential."

---

### Vendor Email Compromise

An attacker impersonates a vendor and requests payment to a new bank account.

---

### Payroll Fraud

An attacker requests changes to employee salary payment information.

---

### Invoice Fraud

A fake invoice is sent to the finance department requesting payment.

---

## Common Indicators

- Urgent financial requests
- Confidential payment requests
- Unexpected bank account changes
- Executive impersonation
- Slightly modified domains

Examples:

- company.com (legitimate)
- companny.com (malicious)

---

## Attack Flow

1. Reconnaissance.
2. Executive or vendor impersonation.
3. Social engineering.
4. Financial request.
5. Payment initiated.
6. Financial loss occurs.

---

## SOC Analyst Investigation

### Email Analysis

Review:

- Sender address
- Reply-To address
- Domain reputation
- SPF
- DKIM
- DMARC

### Authentication Analysis

Check:

- Suspicious logins
- Impossible travel events
- MFA events
- New device logins

### Financial Verification

Confirm:

- Payment legitimacy
- Vendor validation
- Executive approval process

### Endpoint Investigation

Review:

- Email activity
- Browser activity
- Account compromise indicators

---

## Relevant Logs

- Email Gateway Logs
- Authentication Logs
- VPN Logs
- DNS Logs
- Proxy Logs
- EDR Logs

---

## MITRE ATT&CK

### T1566 - Phishing

### T1586 - Compromise Accounts

### T1656 - Impersonation

Tactics:

- Initial Access
- Credential Access
- Collection

---

## Detection Techniques

Look for:

- Executive impersonation
- Newly registered domains
- Suspicious email forwarding rules
- Login activity from unusual locations
- Financial requests outside normal business processes

---

## Prevention

- Multi-Factor Authentication (MFA)
- Executive awareness training
- Vendor verification procedures
- Email authentication (SPF, DKIM, DMARC)
- Payment approval workflows

---

## Key Takeaway

Business Email Compromise (BEC) is one of the most financially damaging cyberattacks. Unlike traditional phishing, BEC often relies on social engineering and trust rather than malware, making detection and verification critical for SOC teams.