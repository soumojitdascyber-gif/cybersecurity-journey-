# MFA Fatigue Attack

## Definition

MFA Fatigue Attack, also known as MFA Bombing or Push Fatigue, is a social engineering attack where attackers repeatedly send Multi-Factor Authentication (MFA) requests until the victim eventually approves one.

The attacker exploits user frustration, confusion, or carelessness to gain unauthorized access.

---

## Objectives

- Account compromise
- Initial access
- Privilege escalation
- Persistence
- Data theft

---

## How MFA Fatigue Works

1. Attacker obtains valid credentials.
2. Attacker attempts to log in.
3. MFA request is sent to the victim.
4. Victim denies the request.
5. Attacker repeatedly sends MFA requests.
6. Victim becomes frustrated.
7. Victim accidentally or intentionally approves the request.
8. Attacker gains access.

---

## Example Scenario

The victim receives:

MFA Request #1 → Denied

MFA Request #2 → Denied

MFA Request #3 → Denied

MFA Request #15 → Approved

The attacker successfully logs in.

---

## Why MFA Fatigue Is Dangerous

### Valid Credentials Already Exist

The attacker already knows the username and password.

---

### Social Engineering Component

The victim becomes overwhelmed by repeated notifications.

---

### MFA Bypass

The attacker bypasses MFA through user approval rather than technical exploitation.

---

## Common Indicators

- Multiple MFA requests
- Repeated login attempts
- Login approvals after several denials
- Unusual geographic locations
- New device logins

---

## Attack Flow

1. Credential theft.
2. Login attempt.
3. MFA challenge generated.
4. MFA spam initiated.
5. User approves request.
6. Account compromised.

---

## SOC Analyst Investigation

### Authentication Analysis

Review:

- Failed login attempts
- Successful login events
- MFA approval logs
- MFA denial logs

---

### User Verification

Confirm:

- Did the user approve the request?
- Did the user initiate the login?

---

### Device Investigation

Check:

- New devices
- New browsers
- New IP addresses

---

### Geolocation Analysis

Review:

- Impossible travel events
- Foreign IP addresses
- Unusual locations

---

## Relevant Logs

- Authentication Logs
- Azure AD Logs
- Microsoft Entra ID Logs
- Okta Logs
- VPN Logs
- EDR Logs

---

## MITRE ATT&CK

### T1621 - Multi-Factor Authentication Request Generation

### T1110 - Brute Force

Tactics:

- Credential Access
- Initial Access

---

## Detection Techniques

Look for:

- Excessive MFA requests
- Multiple MFA denials
- Login success after repeated MFA failures
- Unusual device registrations
- New geographic locations

---

## Prevention

- Number Matching MFA
- FIDO2 Security Keys
- Conditional Access Policies
- User Awareness Training
- Risk-Based Authentication

---

## Key Takeaway

MFA Fatigue attacks exploit human behavior rather than technical vulnerabilities. SOC analysts must closely monitor authentication logs, MFA events, and user activity to detect and respond before attackers gain access.