# 🌐 Networking Basics (ARP, Subnet Mask, DHCP)

---

## 📌 1. ARP (Address Resolution Protocol)

### 🔹 What is ARP?
ARP is used to map an IP address to a MAC address inside a local network.

👉 Simple:
IP → MAC conversion

---

### 🔹 How ARP Works

1. Device wants to send data to an IP
2. It checks ARP cache
3. If not found → sends ARP Request (broadcast)
4. Target device replies with MAC address
5. Communication starts

---

### 🔹 Example

IP: 192.168.1.1  
MAC: AA:BB:CC:DD:EE:FF

---

### 🚨 Security Risk

- ARP Spoofing / Poisoning  
👉 Attacker changes MAC mapping  
👉 Can perform MITM attack

---

## 📌 2. Subnet Mask

### 🔹 What is Subnet Mask?

A subnet mask divides network and host portions of an IP address.

👉 Example:
IP: 192.168.1.10  
Subnet: 255.255.255.0

---

### 🔹 How it Works

- Network part → identifies network  
- Host part → identifies device  

---

### 🔹 Common Subnets

- 255.255.255.0 → /24  
- 255.255.0.0 → /16  
- 255.0.0.0 → /8  

---

### 🔹 Why Important?

- Organizes network  
- Improves performance  
- Helps routing  

---

## 📌 3. DHCP (Dynamic Host Configuration Protocol)

### 🔹 What is DHCP?

DHCP automatically assigns IP address to devices in a network.

---

### 🔹 DHCP Process (DORA)

1. Discover → Client searches for DHCP server  
2. Offer → Server offers IP  
3. Request → Client accepts  
4. Acknowledge → Server confirms  

👉 Short: DORA process

---

### 🔹 Example

Device connects to WiFi → Gets IP automatically

---

### 🚨 Security Risk

- Rogue DHCP server  
👉 Attacker gives fake IP  
👉 Can redirect traffic

---

## 🎯 Conclusion

- ARP → IP to MAC mapping  
- Subnet Mask → Network division  
- DHCP → Automatic IP assignment  

---

## 👨‍💻 Author

Soumojit Das  
Future SOC Analyst