# Layer 2 - Data Link Layer

## Definition

The **Data Link Layer** is the **second layer** of the OSI Model. It is responsible for transferring data between devices on the same local network (LAN). It uses **MAC addresses** to identify devices and ensures reliable communication over the physical medium.

---

# Purpose

The primary purpose of the Data Link Layer is to deliver data frames from one device to another within the same network segment.

---

# Responsibilities

The Data Link Layer is responsible for:

- Physical Addressing (MAC Address)
- Framing
- Error Detection
- Media Access Control
- Local Network Communication
- Flow Control

---

# How It Works

When a device wants to send data to another device on the same LAN:

1. The Network Layer sends a packet to the Data Link Layer.
2. The Data Link Layer adds Source and Destination MAC addresses.
3. The packet becomes a Frame.
4. The frame is transmitted through the Physical Layer.
5. The receiving device verifies the destination MAC address.
6. If the MAC address matches, the frame is accepted.

---

# Data Unit

The Protocol Data Unit (PDU) of the Data Link Layer is:

```
Frame
```

---

# Physical Address

The Data Link Layer uses:

```
MAC Address
```

Example:

```
00:1A:2B:3C:4D:5E
```

A MAC address is permanently assigned to a network interface card (NIC) by the manufacturer.

---

# Sublayers

The Data Link Layer consists of two sublayers:

### Logical Link Control (LLC)

Responsible for:

- Error checking
- Flow control
- Communication with the Network Layer

---

### Media Access Control (MAC)

Responsible for:

- MAC addressing
- Frame transmission
- Access to the physical medium

---

# Ethernet

Ethernet is the most widely used Data Link Layer technology for wired LAN communication.

Characteristics:

- Uses MAC addresses
- Transfers Frames
- Supports high-speed communication

---

# ARP (Address Resolution Protocol)

ARP maps an IP address to a MAC address within the same local network.

Example:

```
IP Address

↓

ARP Request

↓

MAC Address

↓

Frame Transmission
```

---

# Switch

A Switch is a Layer 2 device.

Functions:

- Learns MAC addresses
- Builds a MAC Address Table
- Forwards frames only to the correct destination port
- Reduces unnecessary network traffic

---

# Broadcast

If the destination MAC address is unknown, the switch broadcasts the frame to all devices within the local network.

---

# VLAN (Virtual LAN)

A VLAN divides a physical network into multiple logical networks.

Benefits:

- Improved Security
- Reduced Broadcast Traffic
- Better Network Management

---

# Communication Flow

```
Network Layer

↓

Data Link Layer

↓

Physical Layer
```

---

# Common Devices

Devices operating at Layer 2 include:

- Switch
- Bridge
- Network Interface Card (NIC)
- Wireless Access Point (Layer 2 functionality)

---

# Key Points

- Layer 2 is called the Data Link Layer.
- It uses MAC addresses for communication.
- The PDU is a Frame.
- Switches operate at Layer 2.
- ARP resolves IP addresses to MAC addresses.
- Ethernet is the most common Layer 2 technology.
- VLANs improve network segmentation and management.

---

# Summary

The Data Link Layer enables reliable communication between devices within the same local network. It uses MAC addresses for device identification, encapsulates packets into frames, supports Ethernet communication, and relies on switches for efficient frame forwarding. Understanding Layer 2 is essential for networking, troubleshooting, and building a strong foundation in cybersecurity.