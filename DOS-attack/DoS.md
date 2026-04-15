# 🚨 Denial of Service (DoS) Attack

---

## 📌 What is DoS?

A Denial of Service (DoS) attack is when a single system sends excessive requests to a target server to make it unavailable.

👉 Goal: Disrupt service availability

---

## ⚡ DoS vs DDoS

| Feature | DoS | DDoS |
|--------|-----|------|
| Source | Single system | Multiple systems (botnet) |
| Traffic | Limited | Massive |
| Detection | Easier | Harder |

---

## 🔍 Types of DoS Attacks

### 1. Traffic Flooding
Sends huge number of requests  
Example: UDP Flood

---

### 2. Resource Exhaustion
Consumes server memory/CPU  
Example: SYN Flood

---

### 3. Application Attack
Targets application layer  
Example: HTTP request flood

---

## 🔧 How Attack Works

1. Attacker selects target
2. Sends repeated requests
3. Server resources get exhausted
4. Legitimate users cannot access

---

## 🚨 Indicators (SOC Level)

- High CPU or memory usage
- Sudden increase in traffic
- Slow server response
- Service unavailable

---

## 🛡️ Prevention

- Rate limiting
- Firewall rules
- Load balancing
- Monitoring tools

---

## ⚠️ Example Scenario

A single attacker sends thousands of requests per second to a login page.

👉 Result:
- Server slows down
- Users cannot login

---

## 🎯 Goal

Make the system unavailable

---

## 👨‍💻 Author

Soumojit Das  
Future SOC Analyst & pentester.