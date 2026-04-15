# 🚨 DDoS Attack Guide

## 📌 What is DDoS?
A Distributed Denial of Service (DDoS) attack is when multiple systems send huge traffic to a server, making it slow or completely down.

👉 Goal: Denial of Service (service unavailable)

---

## ⚡ Types of DDoS Attacks

### 1. Volumetric Attack
Floods network bandwidth with massive traffic.

Examples:
- UDP Flood
- ICMP Flood

---

### 2. Protocol Attack
Targets server resources and connections.

Examples:
- SYN Flood
- Ping of Death

---

### 3. Application Layer Attack
Sends normal-looking requests to overload the server.

Examples:
- HTTP GET Flood
- HTTP POST Flood

---

## 🔥 Amplification Attacks

- DNS Amplification
- NTP Amplification
- SNMP Amplification

👉 Small request → Huge response → victim overloaded

---

## 🔍 Detection (SOC Level)

- Sudden traffic spike
- Too many requests from multiple IPs
- Unusual log patterns

---

## 🛡️ Prevention

- Use CDN (Cloudflare)
- Rate limiting
- Web Application Firewall (WAF)
- Load balancing

---

## 🎯 Conclusion

Different techniques...  
Same goal — Denial of Service.

---

## 👨‍💻 Author

Soumojit Das  
Future SOC Analyst & pentester 