# TA0001 - Initial Access

## What is Initial Access?

Initial Access is the first stage of the cyber attack lifecycle where an attacker gains entry into a system, network, application, or cloud environment.

Without Initial Access, an attack cannot begin.

---

## Attacker Objectives

- Gain initial foothold
- Access internal resources
- Start the attack chain
- Prepare for persistence and privilege escalation

---

## Common Initial Access Techniques

### 1. Phishing (T1566)

Attackers send malicious emails containing:

- Malicious attachments
- Malicious links
- Fake login pages

Example:

User receives a fake Microsoft 365 login page and enters credentials.

SOC Detection:

- Suspicious email activity
- URL clicks
- Office spawning PowerShell
- Credential theft attempts

---

### 2. External Remote Services (T1133)

Attackers abuse:

- VPN
- RDP
- Citrix
- SSH

Example:

Brute-force attack against VPN portal.

SOC Detection:

- Multiple failed logins
- Login from unusual locations
- Impossible travel alerts

---

### 3. Drive-by Compromise (T1189)

A user visits a compromised website and malware is downloaded automatically.

SOC Detection:

- Browser exploit activity
- Suspicious downloads
- Unexpected process execution

---

### 4. Supply Chain Compromise (T1195)

Attackers compromise trusted software or updates.

Example:

SolarWinds Attack

SOC Detection:

- Unexpected outbound connections
- Suspicious software behavior

---

## Important Log Sources

- EDR
- SIEM
- Firewall Logs
- DNS Logs
- Email Security Gateway
- Windows Security Logs

---

## SOC Analyst Investigation Process

1. Validate the alert
2. Collect evidence
3. Check source IP
4. Review user activity
5. Analyze authentication logs
6. Review DNS activity
7. Check EDR telemetry
8. Determine True Positive or False Positive
9. Escalate if required

---

## Interview Questions

1. What is Initial Access?
2. Why is Initial Access important?
3. What are common Initial Access techniques?
4. How would you investigate a phishing alert?
5. What logs would you review for an Initial Access incident?

---

## Key Takeaway

Initial Access is the attacker's entry point into the environment.

Early detection at this stage can prevent the entire attack lifecycle from progressing.