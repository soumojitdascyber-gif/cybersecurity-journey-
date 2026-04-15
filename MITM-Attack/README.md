# 🎭 Man-in-the-Middle (MITM) Attack

---

## 📌 What is MITM?

A Man-in-the-Middle (MITM) attack occurs when an attacker secretly intercepts communication between a user and a server.

👉 Goal: Intercept, read, or modify data

---

## 🧠 Simple Idea

User ↔ Attacker ↔ Server

👉 User thinks communication is secure  
👉 But attacker is in the middle

---

## ⚡ Types of MITM Attacks

### 1. ARP Spoofing
Attacker sends fake ARP messages  
👉 Changes MAC-IP mapping  
👉 Traffic goes through attacker

---

### 2. DNS Spoofing
Attacker redirects user to fake website  
👉 Example: fake login page

---

### 3. Evil Twin Attack
Fake WiFi network created  
👉 User connects → attacker captures data

---

## 🔍 How Attack Works

1. Attacker positions between user & server  
2. Intercepts communication  
3. Can read or modify data  
4. Sends data to real server  

---

## 🚨 Indicators (SOC Level)

- Certificate warnings  
- Unusual network traffic  
- Unexpected redirects  
- Suspicious ARP entries  

---

## 🛡️ Prevention

- Use HTTPS  
- Verify SSL certificates  
- Use VPN  
- Avoid public WiFi  
- Enable MFA  

---

## ⚠️ Real-Life Scenario

User connects to free WiFi at a cafe  
👉 Attacker creates fake WiFi  
👉 Captures login credentials  

---

## 🎯 Goal

Steal sensitive information

---

## 👨‍💻 Author

Soumojit Das  
Future SOC Analyst & pentester 