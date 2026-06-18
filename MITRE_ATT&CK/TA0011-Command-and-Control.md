# TA0011 - Command and Control (C2)

## What is Command and Control?

Command and Control (C2) is the stage where a compromised system communicates with an attacker-controlled server.

Goal:

- Receive attacker commands
- Send stolen data
- Maintain remote control
- Execute additional payloads

Without C2, attackers lose control of the infected system.

---

## Attacker Objectives

- Maintain communication
- Receive commands
- Download malware
- Upload stolen data
- Control infected endpoints

---

## Common Command and Control Techniques

### 1. Web Protocols (T1071.001)

Attackers use:

- HTTP
- HTTPS

Example:

Malware connects to:

https://evil-domain.com

SOC Detection:

- Suspicious outbound connections
- Rare domains
- Unusual User-Agent strings

---

### 2. DNS Tunneling (T1071.004)

Attackers abuse DNS for communication.

Example:

data.secret.company.com.attacker.com

SOC Detection:

- Long DNS queries
- High DNS request volume
- DNS beaconing

---

### 3. Beaconing

Malware periodically checks in with C2.

Example:

Every 5 minutes:

Host → C2 Server

SOC Detection:

- Regular connection intervals
- Repeated outbound traffic

---

### 4. Encrypted Channels

Attackers hide communication using:

- HTTPS
- TLS
- VPN

SOC Detection:

- Suspicious encrypted traffic
- Unusual destinations

---

### 5. Non-Standard Ports

Attackers avoid common ports.

Examples:

- 4444
- 8081
- 1337

SOC Detection:

- Unexpected outbound ports
- Firewall alerts

---

## Important Log Sources

- DNS Logs
- Firewall Logs
- Proxy Logs
- EDR
- SIEM
- NetFlow

---

## SOC Analyst Investigation Process

### Step 1

Validate alert.

### Step 2

Identify communication channel.

Questions:

- DNS?
- HTTP?
- HTTPS?

### Step 3

Review Destination.

Questions:

- Known malicious?
- Newly registered domain?
- Threat intelligence hit?

### Step 4

Review Beaconing Pattern.

Questions:

- Same interval?
- Same destination?

### Step 5

Review Endpoint Activity.

Questions:

- Malware present?
- PowerShell execution?
- Persistence detected?

### Step 6

Correlate Evidence.

- DNS Logs
- Firewall Logs
- EDR
- SIEM

### Step 7

Determine:

- True Positive
- False Positive

### Step 8

Containment

Actions:

- Isolate endpoint
- Block IP/domain
- Kill malicious process

### Step 9

Escalate if required

---

## Real SOC Example

Alert:

DNS Beaconing Detected

Investigation:

DNS Logs
↓
Requests every 60 seconds

Threat Intelligence
↓
Domain flagged as malicious

EDR
↓
PowerShell execution detected

Timeline
↓
Persistence established earlier

Conclusion:

True Positive

Action:

- Block domain
- Isolate endpoint
- Escalate to SOC L2

---

## Interview Questions

1. What is Command and Control?
2. Why do attackers need C2?
3. What is DNS Tunneling?
4. What is Beaconing?
5. How would you investigate suspicious outbound traffic?
6. Which logs are useful for C2 detection?

---

## Key Takeaway

Command and Control allows attackers to remotely control infected systems.

Detecting C2 communication can stop attackers before data theft and major damage occur.