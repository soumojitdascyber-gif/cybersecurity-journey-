# Day 06 - DNS Detection & SOC Use Cases

# Introduction

DNS is one of the most important data sources for SOC Analysts.

Attackers frequently use DNS for:

- Command and Control (C2)
- Data Exfiltration
- Malware Communication
- Domain Generation Algorithms (DGA)
- Beaconing

DNS logs help analysts identify suspicious activity before major damage occurs.

---

# Why DNS Monitoring is Important

DNS is used by almost every application.

When malware wants to communicate with an attacker server, DNS resolution is often the first step.

Example:

Infected Host
↓
DNS Query
↓
Malicious Domain
↓
Attacker Server

---

# DNS Detection Use Cases

## 1. DGA Domain Detection

### What is DGA?

DGA (Domain Generation Algorithm) generates random domains.

Example:

xj29skd82.com
a8dj3kd92.net
k2jd82js.org

Malware uses DGA domains to avoid detection.

### Indicators

- Random characters
- Newly registered domains
- High NXDOMAIN responses

### Detection Logic

Look for:

- Random-looking domains
- Unusual DNS patterns
- High failed DNS lookups

---

## 2. DNS Tunneling Detection

### What is DNS Tunneling?

Attackers can send data through DNS requests.

Purpose:

- Data Exfiltration
- Command and Control

Tools:

- DNScat2
- Iodine

### Indicators

- Very long DNS queries
- Base64 encoded strings
- High volume DNS traffic

Example:

YWJjMTIzNDU2Nzg5.example.com

### Detection Logic

Look for:

- Long subdomains
- Repeated TXT requests
- Excessive DNS traffic

---

## 3. DNS Beaconing Detection

### What is Beaconing?

Malware periodically contacts a C2 server.

Example:

Every 5 minutes

Host A
↓
malicious-domain.com

### Indicators

- Regular intervals
- Same domain repeatedly queried
- Low but consistent traffic

### Detection Logic

Look for:

- Repeating patterns
- Consistent timing intervals

---

## 4. Newly Registered Domains

### Why Important?

Attackers often create domains shortly before attacks.

Example:

Created:
2 days ago

Domain:
security-update-login.com

### Indicators

- New domain
- Low reputation
- No business history

### Detection Logic

Check:

- WHOIS
- VirusTotal
- Domain age

---

## 5. Excessive NXDOMAIN Responses

### What is NXDOMAIN?

DNS server cannot find requested domain.

Example:

abcxyz123.com

Response:

NXDOMAIN

### Indicators

- High NXDOMAIN count
- Random domains
- DGA activity

### Detection Logic

Investigate hosts generating large NXDOMAIN volumes.

---

## 6. Suspicious Geographic DNS Requests

### Indicators

- Unusual countries
- Rare regions
- Unexpected communication

Example:

Company located in India

DNS requests suddenly resolve domains hosted in:

- Russia
- North Korea
- Iran

### Detection Logic

Compare activity against normal business behavior.

---

# DNS Investigation Process

## Step 1

Identify suspicious domain.

Example:

update-storage-sync.com

---

## Step 2

Check DNS Logs

Questions:

- Which host queried?
- How many times?
- Which user?

---

## Step 3

Check EDR

Questions:

- Which process initiated request?
- Parent process?
- PowerShell involved?

---

## Step 4

Check Firewall Logs

Questions:

- Outbound traffic?
- Data transfer volume?

---

## Step 5

Check Threat Intelligence

Tools:

- VirusTotal
- AbuseIPDB
- URLScan

---

## Step 6

Determine:

- True Positive
- False Positive

---

## Step 7

Containment

Actions:

- Block domain
- Block IP
- Isolate endpoint
- Reset credentials

---

# SOC Interview Questions

1. What is DNS Beaconing?
2. What is DNS Tunneling?
3. What is DGA?
4. What is NXDOMAIN?
5. How can attackers use DNS for Data Exfiltration?
6. How would you investigate a suspicious DNS query?
7. Why are DNS logs important in SOC?
8. How can you detect DNS Tunneling?
9. What indicators suggest DGA activity?
10. How would you confirm a DNS alert is malicious?

---

# Key Takeaways

- DNS is a critical data source for SOC analysts.
- Malware often uses DNS before communication.
- DNS Tunneling can be used for Data Exfiltration.
- DGA domains help malware evade detection.
- Beaconing indicates potential C2 communication.
- DNS logs should always be correlated with EDR, Firewall, and SIEM data.