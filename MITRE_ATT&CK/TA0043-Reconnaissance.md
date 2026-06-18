# TA0043 - Reconnaissance

## What is Reconnaissance?

Reconnaissance is the stage where attackers gather information about a target before launching an attack.

Goal:

- Identify targets
- Gather intelligence
- Find weaknesses
- Plan attacks

Reconnaissance happens before Initial Access.

---

## Attacker Objectives

- Find employees
- Discover domains
- Identify public services
- Gather email addresses
- Map attack surface

---

## Common Reconnaissance Techniques

### 1. Active Scanning (T1595)

Attackers scan:

- Websites
- Servers
- Open Ports

Tools:

- Nmap
- Masscan

---

### 2. Gather Victim Identity Information (T1589)

Examples:

- Employee names
- Email addresses
- Phone numbers

Sources:

- LinkedIn
- Company Website

---

### 3. Gather Victim Network Information (T1590)

Examples:

- Domains
- IP Addresses
- DNS Records

Tools:

- Whois
- nslookup
- dig

---

### 4. Gather Victim Org Information (T1591)

Examples:

- Company structure
- Technologies used
- Vendors

---

## Important Data Sources

- WHOIS
- DNS Records
- Search Engines
- LinkedIn
- Shodan

---

## Real Example

Attacker:

LinkedIn
↓
Employee Discovery

Company Website
↓
Email Format Discovery

DNS Enumeration
↓
Subdomain Discovery

Result:
Targeted Phishing Campaign

---

## Interview Questions

1. What is Reconnaissance?
2. Difference between Active and Passive Recon?
3. Why is Recon important?
4. What tools are used during Recon?

---

## Key Takeaway

Reconnaissance helps attackers understand a target before launching an attack.