# 🔐 Brute Force Attack

## 📌 What is Brute Force?
A brute force attack is a method where an attacker tries multiple username and password combinations to gain unauthorized access.

👉 Goal: Guess correct credentials

---

## ⚡ Types of Brute Force Attacks

### 1. Simple Brute Force
Attacker tries all possible password combinations.

### 2. Dictionary Attack
Uses a list of common passwords.

Example:
- 123456
- password
- admin123

### 3. Credential Stuffing
Uses leaked username-password data from other sites.

### 4. Hybrid Attack
Combination of dictionary + brute force.

---

## 🔍 How Attack Works

1. Attacker selects target (login page)
2. Uses automated tools/scripts
3. Tries multiple passwords rapidly
4. Gains access if correct match found

---

## 🚨 Indicators of Brute Force (SOC Level)

- Multiple failed login attempts
- Same IP trying different passwords
- Multiple accounts targeted from one IP
- Unusual login time/location

---

## 📊 Example Log

IP: 192.168.1.5 - Failed login  
IP: 192.168.1.5 - Failed login  
IP: 192.168.1.5 - Failed login  
IP: 192.168.1.5 - Successful login  

⚠️ Possible brute force detected

---

## 🛡️ Prevention

- Use strong passwords
- Enable Multi-Factor Authentication (MFA)
- Account lockout after multiple failed attempts
- Rate limiting
- CAPTCHA

---

## 🔧 Tools Used by Attackers

- Hydra
- Burp Suite
- Medusa

---

## 🎯 Goal

Unauthorized access to system

---

## 👨‍💻 Author

Soumyajit Das  
Future SOC Analyst