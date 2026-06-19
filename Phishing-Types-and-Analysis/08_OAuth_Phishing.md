# OAuth Phishing

## Definition

OAuth Phishing is a phishing attack where attackers trick users into granting permissions to a malicious OAuth application instead of stealing their username and password directly.

The attacker abuses OAuth authorization mechanisms to gain access to user resources through access tokens.

---

## What is OAuth?

OAuth (Open Authorization) is an authorization framework that allows third-party applications to access resources without requiring the user's password.

Examples:

- Microsoft 365
- Google Workspace
- GitHub
- Slack

---

## Objectives

- Account compromise
- Email access
- Cloud data access
- Persistence
- Data theft

---

## How OAuth Phishing Works

1. Attacker creates a malicious OAuth application.
2. Victim receives a phishing email.
3. Victim clicks the OAuth consent link.
4. Victim sees a legitimate Microsoft or Google login page.
5. Victim grants permissions.
6. Attacker receives OAuth access tokens.
7. Attacker gains access to user resources.

---

## Example Scenario

Victim receives:

Subject:

"Shared Document Available"

The link redirects to:

Microsoft OAuth Consent Page

Application Requests:

- Read Emails
- Read Contacts
- Read Files
- Maintain Access

Victim clicks:

"Accept"

The attacker now has access without knowing the password.

---

## Why OAuth Phishing Is Dangerous

### MFA May Not Help

Even if Multi-Factor Authentication is enabled, a user can still grant malicious permissions.

---

### No Password Theft Required

The attacker gains access through tokens rather than credentials.

---

### Long-Term Access

OAuth tokens can provide persistent access to cloud resources.

---

## Common Indicators

- New OAuth application consent
- Unexpected cloud application access
- Unusual mailbox activity
- Suspicious file downloads
- Token abuse

---

## Attack Flow

1. Phishing email delivered.
2. Victim clicks consent link.
3. OAuth permission granted.
4. Access token issued.
5. Attacker accesses resources.
6. Data theft or persistence achieved.

---

## SOC Analyst Investigation

### Cloud Audit Logs

Review:

- New application consent events
- OAuth authorization events
- Token issuance logs

---

### Authentication Logs

Check:

- Successful logins
- MFA activity
- New devices
- New locations

---

### Mailbox Investigation

Review:

- Email forwarding rules
- Mailbox permissions
- Suspicious email activity

---

### Application Investigation

Verify:

- Application publisher
- Application permissions
- Risk level

---

## Relevant Logs

- Microsoft Entra ID Logs
- Azure AD Logs
- Google Workspace Logs
- Cloud Audit Logs
- Authentication Logs
- EDR Logs

---

## MITRE ATT&CK

### T1528 - Steal Application Access Token

### T1550 - Use Alternate Authentication Material

Tactics:

- Credential Access
- Persistence
- Defense Evasion

---

## Detection Techniques

Look for:

- New OAuth applications
- Excessive permissions
- Unknown application publishers
- Unusual cloud access
- Suspicious mailbox rule creation

---

## Prevention

- User awareness training
- Admin consent policies
- OAuth application review
- Conditional Access Policies
- Regular permission audits

---

## Key Takeaway

OAuth phishing is a modern cloud-based phishing technique that abuses trust in legitimate authorization systems. Instead of stealing passwords, attackers obtain access tokens, making detection and monitoring of OAuth permissions critical for SOC analysts.