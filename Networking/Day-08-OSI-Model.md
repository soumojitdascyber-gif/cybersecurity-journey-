# Day 08 – OSI Model (Open Systems Interconnection)

> SOC Analyst Networking Series

---

# Learning Objectives

After completing this chapter, you will understand:

- What is the OSI Model?
- Why the OSI Model is Important
- The 7 Layers of the OSI Model
- Data Flow Through the OSI Model
- Common Protocols
- Common Devices
- Real-World Example
- SOC Analyst Perspective
- Interview Questions

---

# What is the OSI Model?

The **OSI (Open Systems Interconnection) Model** is a conceptual framework that explains how devices communicate over a network.

It divides network communication into **7 layers**, where each layer has a specific responsibility.

---

# Why is the OSI Model Important?

The OSI Model helps us:

- Understand network communication
- Troubleshoot networking issues
- Learn protocols
- Analyze cyber attacks
- Investigate network traffic

For SOC Analysts, understanding the OSI Model is essential for identifying where an attack occurs.

---

# The 7 Layers

```
+-----------------------+
| Layer 7 | Application |
+-----------------------+
| Layer 6 | Presentation|
+-----------------------+
| Layer 5 | Session     |
+-----------------------+
| Layer 4 | Transport   |
+-----------------------+
| Layer 3 | Network     |
+-----------------------+
| Layer 2 | Data Link   |
+-----------------------+
| Layer 1 | Physical    |
+-----------------------+
```

---

# Layer 7 – Application

Purpose:

Provides network services directly to users.

Examples:

- HTTP
- HTTPS
- FTP
- SMTP
- DNS

Examples of Applications

- Chrome
- Firefox
- Outlook

SOC Perspective

Look for:

- HTTP Requests
- DNS Queries
- Phishing
- Web Traffic

---

# Layer 6 – Presentation

Purpose:

Formats and encrypts data.

Functions

- Encryption
- Decryption
- Compression
- Encoding

Examples

- TLS
- SSL
- JPEG
- PNG

SOC Perspective

HTTPS uses TLS at this layer.

---

# Layer 5 – Session

Purpose

Creates, manages, and terminates communication sessions.

Examples

- NetBIOS
- RPC

SOC Perspective

Session hijacking attacks target this layer.

---

# Layer 4 – Transport

Purpose

Reliable communication between devices.

Protocols

- TCP
- UDP

Functions

- Segmentation
- Flow Control
- Error Recovery

SOC Perspective

Investigate:

- TCP Handshake
- TCP Reset
- UDP Traffic
- Port Scanning

---

# Layer 3 – Network

Purpose

Routes packets between networks.

Protocols

- IP
- ICMP

Devices

- Router

SOC Perspective

Monitor:

- Source IP
- Destination IP
- Routing
- Traceroute

---

# Layer 2 – Data Link

Purpose

Transfers data within the same network.

Protocols

- Ethernet
- ARP

Address Used

MAC Address

Devices

- Switch

SOC Perspective

Monitor:

- MAC Addresses
- ARP Spoofing
- VLAN Activity

---

# Layer 1 – Physical

Purpose

Transmits raw electrical or optical signals.

Examples

- Ethernet Cable
- Fiber Cable
- Wi-Fi Radio Signals

Devices

- Hub
- Cable
- Repeater

SOC Perspective

Usually handled by network engineers.

---

# Data Flow

Application

↓

Presentation

↓

Session

↓

Transport

↓

Network

↓

Data Link

↓

Physical

↓

Internet

↓

Destination Device

---

# Data Unit

Layer 7–5

Data

↓

Layer 4

Segment

↓

Layer 3

Packet

↓

Layer 2

Frame

↓

Layer 1

Bits

---

# Common Protocols by Layer

| Layer | Protocols |
|--------|-----------|
| Application | HTTP, HTTPS, DNS, FTP, SMTP |
| Presentation | TLS, SSL |
| Session | RPC, NetBIOS |
| Transport | TCP, UDP |
| Network | IP, ICMP |
| Data Link | Ethernet, ARP |
| Physical | Fiber, Ethernet Cable |

---

# Common Devices

| Layer | Device |
|--------|--------|
| L7 | Proxy Server |
| L4 | Firewall |
| L3 | Router |
| L2 | Switch |
| L1 | Hub, Cable |

---

# Real-World Example

User opens:

https://www.google.com

↓

DNS resolves the domain

↓

TCP Three-Way Handshake

↓

TLS Handshake

↓

HTTP GET Request

↓

Google Server

↓

HTTP Response

↓

Browser displays the webpage

---

# SOC Analyst Perspective

A SOC Analyst investigates multiple OSI layers.

Layer 7

- HTTP
- HTTPS
- DNS

Layer 4

- TCP
- UDP
- Port Activity

Layer 3

- IP Address
- ICMP

Layer 2

- MAC Address
- ARP

Understanding the OSI Model helps analysts identify where suspicious activity occurs.

---

# Key Takeaways

- OSI has 7 layers.
- Each layer has a unique function.
- TCP works at Layer 4.
- IP works at Layer 3.
- ARP works at Layer 2.
- HTTP and DNS work at Layer 7.
- TLS provides encryption.
- The OSI Model is a foundation for networking and cybersecurity.

---

# Interview Questions

### 1. What is the OSI Model?

### 2. How many layers does the OSI Model have?

### 3. Which layer uses TCP?

Answer:

Layer 4 (Transport)

---

### 4. Which layer uses IP?

Answer:

Layer 3 (Network)

---

### 5. Which layer uses ARP?

Answer:

Layer 2 (Data Link)

---

### 6. Which layer uses HTTP?

Answer:

Layer 7 (Application)

---

### 7. Which device works at Layer 3?

Answer:

Router

---

### 8. Which device works at Layer 2?

Answer:

Switch

---

### 9. Why is the OSI Model important for SOC Analysts?

Answer:

It helps analysts understand network communication, identify attack locations, analyze traffic, and troubleshoot incidents.

---

# Summary

OSI Model

Layer 7 → Application

Layer 6 → Presentation

Layer 5 → Session

Layer 4 → Transport

Layer 3 → Network

Layer 2 → Data Link

Layer 1 → Physical

Mastering the OSI Model is essential for networking, packet analysis, and SOC investigations.