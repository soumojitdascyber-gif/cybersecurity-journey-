# Day 09 – Switch, Hub, MAC Address, MAC Address Table, Broadcast Domain & Collision Domain

# Introduction

Understanding how devices communicate inside a Local Area Network (LAN) is one of the most important networking fundamentals for cybersecurity.

In this guide, we'll cover:

- Hub
- Switch
- MAC Address
- MAC Address Table (CAM Table)
- Broadcast Domain
- Collision Domain

---

# 1. What is a Hub?

A Hub is a Layer 1 (Physical Layer) networking device.

It simply receives incoming data and sends it to every connected device.

It does not know the destination.

### Characteristics

- Works on Layer 1
- No MAC Address learning
- Sends data to all devices
- Low performance
- Half Duplex

### Example

PC A → Hub

Hub sends the data to:

- PC B
- PC C
- PC D

Everyone receives the packet.

---

# 2. What is a Switch?

A Switch is a Layer 2 (Data Link Layer) networking device.

Unlike a hub, a switch sends data only to the correct destination device.

It uses MAC Addresses to make forwarding decisions.

### Characteristics

- Works on Layer 2
- Learns MAC Addresses
- Uses MAC Address Table
- Better performance
- Full Duplex

### Example

PC A wants to communicate with PC C.

The switch forwards the frame only to PC C.

---

# Hub vs Switch

| Feature | Hub | Switch |
|----------|------|---------|
| OSI Layer | Layer 1 | Layer 2 |
| Uses MAC Address | No | Yes |
| Intelligent | No | Yes |
| Collision | High | Very Low |
| Speed | Slow | Fast |
| Security | Low | Better |

---

# 3. What is a MAC Address?

MAC stands for Media Access Control.

A MAC Address is a unique physical address assigned to every Network Interface Card (NIC).

Example:

00:1A:2B:3C:4D:5E

Think of it as the identity card of your network device.

---

# Why is MAC Address Important?

A switch uses MAC Addresses to identify connected devices.

Without MAC Addresses, a switch cannot forward frames correctly.

---

# 4. What is a MAC Address Table?

A MAC Address Table (also called CAM Table) is stored inside a switch.

It keeps track of:

- MAC Address
- Connected Port

Example

| MAC Address | Port |
|-------------|------|
| AA:AA:AA | Fa0/1 |
| BB:BB:BB | Fa0/2 |
| CC:CC:CC | Fa0/3 |

When data arrives, the switch checks this table and forwards it to the correct port.

---

# 5. What is a Broadcast Domain?

A Broadcast Domain is the area where broadcast traffic reaches every device.

Example:

PC A sends a broadcast message.

Every device in the same network receives it.

Broadcasts do not cross routers.

---

# 6. What is a Collision Domain?

A Collision Domain is the area where two devices can transmit data at the same time, causing a collision.

Hub:

All connected devices share one collision domain.

Switch:

Each switch port has its own collision domain.

This greatly improves network performance.

---

# Quick Comparison

| Concept | Description |
|----------|-------------|
| Hub | Sends data to every device |
| Switch | Sends data only to the correct device |
| MAC Address | Unique hardware address |
| MAC Address Table | Stores MAC-to-Port mapping |
| Broadcast Domain | Area where broadcast traffic spreads |
| Collision Domain | Area where packet collisions occur |

---

# Real-Life Example

Imagine a classroom.

Hub:

The teacher shouts one message to the whole class.

Everyone hears it.

Switch:

The teacher quietly hands a note to only one student.

Only that student receives it.

---

# Why It Matters in Cybersecurity

Understanding these concepts helps with:

- Network troubleshooting
- Packet analysis
- Traffic monitoring
- SOC investigations
- Wireshark analysis
- Network security fundamentals

---

# Summary

✔ Hub works on Layer 1.

✔ Switch works on Layer 2.

✔ Every network device has a unique MAC Address.

✔ Switches store MAC Addresses in a MAC Address Table.

✔ Broadcast traffic reaches every device inside a Broadcast Domain.

✔ Switches reduce collisions by creating separate Collision Domains.