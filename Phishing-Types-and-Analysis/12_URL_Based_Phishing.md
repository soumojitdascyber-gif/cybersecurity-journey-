# URL-Based Phishing

## Definition

URL-Based Phishing is a phishing attack where attackers use malicious URLs to redirect victims to fraudulent websites designed to steal credentials, financial information, or deliver malware.

The attacker attempts to make the malicious URL appear legitimate to trick users into trusting and visiting the website.

---

## Objectives

- Credential theft
- Financial fraud
- Malware delivery
- Session hijacking
- Account compromise

---

## How URL-Based Phishing Works

1. Attacker creates a fake website.
2. Generates a malicious URL.
3. Sends the URL through email, SMS, social media, or messaging platforms.
4. Victim clicks the link.
5. Fake website collects credentials or delivers malware.
6. Attacker gains access to accounts or systems.

---

## Common URL-Based Phishing Techniques

### Typosquatting

Attackers register domains similar to legitimate websites.

Examples:

Legitimate:

microsoft.com

Malicious:

micros0ft.com

---

### Homograph Attack

Uses visually similar characters.

Example:

paypaI.com

(The uppercase "I" replaces the lowercase "l")

---

### URL Shortening

Attackers hide malicious URLs using shortened links.

Examples:

- bit.ly
- tinyurl.com

---

### Fake Login Pages

Impersonates:

- Microsoft 365
- Google Workspace
- Banking Portals
- VPN Portals

---

## Common Indicators

- Misspelled domains
- Unexpected redirects
- Shortened URLs
- Suspicious login pages
- Recently registered domains

---

## Attack Flow

1. Phishing message delivered.
2. Victim clicks URL.
3. Fake website opens.
4. Credentials entered.
5. Information sent to attacker.
6. Account compromised.

---

## Example Scenario

Email Subject:

Microsoft Password Expiration Notice

URL:

hxxps://micros0ft-login[.]com

Victim enters:

- Username
- Password
- MFA Code

Attacker gains access.

---

## SOC Analyst Investigation

### URL Analysis

Check:

- Domain reputation
- WHOIS information
- Domain age
- Redirect chains

---

### DNS Analysis

Investigate:

- DNS queries
- Suspicious domains
- Newly observed domains

---

### Proxy Analysis

Review:

- Visited URLs
- HTTP requests
- HTTPS requests
- User activity

---

### Authentication Analysis

Check:

- Failed logins
- Successful logins
- MFA events
- Impossible travel

---

## Relevant Logs

- DNS Logs
- Proxy Logs
- Firewall Logs
- Authentication Logs
- EDR Logs
- Web Security Logs

---

## MITRE ATT&CK

### T1566.002 - Spearphishing Link

### T1189 - Drive-by Compromise

Tactics:

- Initial Access
- Credential Access

---

## Detection Techniques

Look for:

- Newly registered domains
- Domains with poor reputation
- Multiple users visiting the same suspicious URL
- Credential submissions to unknown websites
- Abnormal authentication activity

---

## Prevention

- Security Awareness Training
- URL Filtering
- DNS Security Controls
- Multi-Factor Authentication (MFA)
- Secure Web Gateways

---

## Key Takeaway

URL-Based Phishing is one of the most common phishing techniques used by attackers. SOC analysts must investigate suspicious URLs, monitor DNS activity, analyze authentication logs, and identify malicious domains before attackers can compromise user accounts.