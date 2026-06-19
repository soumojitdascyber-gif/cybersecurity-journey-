# Pharming

## Definition

Pharming is a cyberattack that redirects users from legitimate websites to malicious websites without their knowledge.

Unlike phishing, where users are tricked into clicking a malicious link, pharming can redirect users even when they enter the correct website address.

---

## Objectives

- Credential theft
- Financial fraud
- Malware delivery
- Identity theft
- Data theft

---

## How Pharming Works

Pharming attacks manipulate the domain name resolution process to redirect victims to attacker-controlled websites.

When a user enters a legitimate domain, the request is redirected to a malicious server.

---

## Types of Pharming

### DNS Poisoning

The attacker modifies DNS records so users are redirected to malicious websites.

Example:

User enters:

www.bank.com

DNS returns:

Attacker-controlled IP address

---

### Hosts File Manipulation

The attacker modifies the victim's local hosts file.

Example:

192.168.1.100 bank.com

The victim is redirected to a fake website.

---

### Router Compromise

The attacker compromises a router and changes DNS settings.

All connected devices become affected.

---

## Attack Flow

1. DNS or host file is compromised.
2. User enters a legitimate website address.
3. Request is redirected.
4. Fake website loads.
5. Victim enters credentials.
6. Attacker steals information.

---

## Pharming vs Phishing

### Phishing

- Requires user interaction.
- Uses fake emails or messages.
- Relies on social engineering.

### Pharming

- Does not always require user interaction.
- Uses DNS manipulation.
- Redirects users automatically.

---

## Common Indicators

- Unexpected login pages
- SSL certificate warnings
- DNS anomalies
- Incorrect website content
- Multiple users reporting redirection

---

## Example Scenario

User visits:

https://www.bank.com

Instead of reaching the legitimate website, they are redirected to a fake banking portal controlled by the attacker.

The victim enters:

- Username
- Password
- OTP

The attacker steals the information.

---

## SOC Analyst Investigation

### DNS Analysis

Review:

- DNS queries
- DNS responses
- DNS server changes

---

### Endpoint Analysis

Check:

- Hosts file modifications
- Suspicious processes
- Malware indicators

---

### Network Analysis

Investigate:

- DNS traffic
- Suspicious outbound connections
- Network anomalies

---

### Router Investigation

Verify:

- DNS configuration
- Administrative access logs
- Unauthorized changes

---

## Relevant Logs

- DNS Logs
- Proxy Logs
- Firewall Logs
- EDR Logs
- Sysmon Logs
- Network Security Logs

---

## MITRE ATT&CK

### T1557 - Adversary-in-the-Middle

### T1584 - Compromise Infrastructure

### T1565 - Data Manipulation

Tactics:

- Initial Access
- Credential Access
- Collection

---

## Detection Techniques

Look for:

- DNS record changes
- Unusual DNS responses
- Multiple users redirected to the same IP
- SSL certificate mismatches
- Hosts file modifications

---

## Prevention

- DNSSEC implementation
- Secure DNS providers
- Endpoint protection
- Router security hardening
- User awareness training

---

## Key Takeaway

Pharming is a dangerous attack because victims may visit malicious websites even when entering legitimate URLs. SOC analysts must monitor DNS activity, endpoint changes, and network behavior to detect and respond to pharming attacks effectively.