# Layer 3 - Network Layer

## Definition

The **Network Layer** is the **third layer** of the OSI Model. It is responsible for identifying devices using logical addresses (IP addresses) and routing data packets from the source network to the destination network.

Unlike the Data Link Layer, which works within the same local network, the Network Layer enables communication between different networks.

---

# Purpose

The primary purpose of the Network Layer is to deliver data packets from the source device to the correct destination across one or more interconnected networks.

---

# Responsibilities

The Network Layer is responsible for:

- Logical Addressing
- Packet Routing
- Path Selection
- Packet Forwarding
- Fragmentation
- Packet Reassembly
- Inter-network Communication

---

# How It Works

When a user visits:

```
https://github.com
```

The Network Layer:

1. Receives data from the Transport Layer.
2. Adds Source IP Address.
3. Adds Destination IP Address.
4. Determines the best route.
5. Sends the packet to the next router.
6. Continues until the destination is reached.

---

# Data Unit

The Protocol Data Unit (PDU) of the Network Layer is:

```
Packet
```

---

# Logical Address

The Network Layer uses:

```
IP Address
```

Example

```
192.168.1.15
```

Unlike MAC addresses, IP addresses can change depending on the network.

---

# Common Protocols

| Protocol | Purpose |
|----------|---------|
| IPv4 | Logical Addressing |
| IPv6 | Next-generation IP |
| ICMP | Error Reporting |
| IPsec | Secure IP Communication |
| IGMP | Multicast Communication |

---

# IPv4

IPv4 uses a **32-bit address**.

Example

```
192.168.1.10
```

---

# IPv6

IPv6 uses a **128-bit address**.

Example

```
2001:db8::1
```

It was introduced to solve IPv4 address exhaustion and improve scalability.

---

# Routing

Routing is the process of selecting the best path for data to travel between networks.

Routers use routing tables to determine where packets should be forwarded.

---

# Router

A Router is a Layer 3 device that forwards packets between different networks based on IP addresses.

Example:

```
Home Network

↓

Router

↓

Internet

↓

Web Server
```

---

# Packet Forwarding

Each router examines the destination IP address and forwards the packet toward its destination using the best available route.

---

# Fragmentation

If a packet is larger than the Maximum Transmission Unit (MTU), it may be divided into smaller fragments for transmission.

The destination system reassembles the fragments into the original packet.

---

# ICMP

Internet Control Message Protocol (ICMP) is used for diagnostics and error reporting.

Common examples include:

- Ping
- Traceroute
- Destination Unreachable
- Time Exceeded

---

# TTL (Time To Live)

TTL limits how many routers a packet can pass through before it is discarded.

Each router decreases the TTL value by 1.

When TTL reaches 0, the packet is dropped.

---

# NAT (Network Address Translation)

NAT allows multiple private devices to share a single public IP address.

Benefits:

- Conserves IPv4 addresses
- Hides internal network addresses
- Improves network scalability

---

# Real-World Example

Suppose your computer wants to access:

```
https://github.com
```

The Network Layer:

- Adds your Source IP address.
- Adds GitHub's Destination IP address.
- Selects the best route.
- Sends packets through multiple routers.
- Delivers the packets to GitHub's server.

---

# Communication Flow

```
Transport Layer

↓

Network Layer

↓

Data Link Layer
```

---

# Common Devices

Layer 3 devices include:

- Router
- Layer 3 Switch
- Firewall (Layer 3 capable)

---

# Key Points

- Layer 3 is called the Network Layer.
- It uses IP addresses for communication.
- It is responsible for routing.
- Routers operate at Layer 3.
- The PDU is a Packet.
- IPv4 and IPv6 operate at this layer.
- ICMP is used for diagnostics.
- NAT allows private networks to access the Internet.

---

# Summary

The Network Layer enables communication between different networks by using logical addressing and routing. It determines the best path for packets, forwards them through routers, and ensures they reach the correct destination. Understanding this layer is fundamental for networking, troubleshooting, and cybersecurity.