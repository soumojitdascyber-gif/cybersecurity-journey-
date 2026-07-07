# Layer 4 - Transport Layer

## Definition

The **Transport Layer** is the **4th layer** of the OSI Model. It is responsible for ensuring reliable or fast end-to-end communication between two devices by transmitting data from one host to another.

It determines how data is delivered, whether reliably using TCP or quickly using UDP.

---

# Purpose

The primary purpose of the Transport Layer is to provide end-to-end communication between applications running on different devices.

It ensures that data reaches the correct application using port numbers.

---

# Responsibilities

The Transport Layer is responsible for:

- End-to-End Communication
- Data Segmentation
- Data Reassembly
- Flow Control
- Error Detection
- Error Recovery
- Reliable Data Delivery
- Multiplexing
- Port Addressing

---

# How It Works

When a user downloads a file:

1. The Application Layer creates the data.
2. The Transport Layer divides the data into smaller segments.
3. Each segment is assigned source and destination ports.
4. The segments are sent to the Network Layer.
5. The destination Transport Layer reassembles all segments into the original data.

---

# Data Unit

The Protocol Data Unit (PDU) of the Transport Layer is:

```
Segment
```

---

# Transport Layer Protocols

| Protocol | Description |
|----------|-------------|
| TCP | Reliable communication |
| UDP | Fast communication |

---

# TCP (Transmission Control Protocol)

TCP is a connection-oriented protocol that guarantees reliable communication.

### Features

- Reliable
- Connection-Oriented
- Error Checking
- Flow Control
- Ordered Delivery
- Retransmission

### Examples

- HTTP
- HTTPS
- FTP
- SSH
- SMTP

---

# UDP (User Datagram Protocol)

UDP is a connectionless protocol designed for speed.

### Features

- Faster than TCP
- No Handshake
- No Error Recovery
- No Ordered Delivery
- Low Overhead

### Examples

- DNS
- VoIP
- Online Gaming
- Live Streaming
- DHCP

---

# TCP vs UDP

| TCP | UDP |
|------|------|
| Reliable | Faster |
| Connection-Oriented | Connectionless |
| Error Recovery | No Recovery |
| Ordered Delivery | No Ordering |
| Larger Overhead | Smaller Overhead |

---

# Port Numbers

Ports identify which application should receive the data.

Examples:

| Port | Service |
|------|----------|
| 20/21 | FTP |
| 22 | SSH |
| 25 | SMTP |
| 53 | DNS |
| 80 | HTTP |
| 110 | POP3 |
| 143 | IMAP |
| 443 | HTTPS |
| 3389 | RDP |

---

# TCP Three-Way Handshake

Before communication begins, TCP establishes a connection.

```
Client

   SYN

────────────►

Server

◄────────────

 SYN + ACK

────────────►

ACK

Connection Established
```

---

# TCP Connection Termination

TCP uses a Four-Way Handshake to close a connection.

```
FIN

↓

ACK

↓

FIN

↓

ACK
```

---

# Flow Control

Flow Control prevents a fast sender from overwhelming a slow receiver.

This helps avoid packet loss and improves communication reliability.

---

# Error Detection

TCP uses sequence numbers and acknowledgments to detect missing or damaged segments.

If a segment is lost, TCP retransmits it.

---

# Segmentation

Large data is divided into smaller segments before transmission.

The destination system reassembles all segments into the original data.

---

# Multiplexing

Multiple applications can communicate simultaneously using different port numbers.

Example:

Browser → Port 443

Email → Port 25

SSH → Port 22

---

# Real-World Example

When downloading a PDF from a website:

- Browser sends an HTTPS request.
- TCP establishes a connection.
- The file is divided into segments.
- Each segment is delivered reliably.
- The destination reassembles the complete file.

---

# Communication Flow

```
Application Layer

↓

Presentation Layer

↓

Session Layer

↓

Transport Layer

↓

Network Layer
```

---

# Common Devices

Although the Transport Layer mainly handles logical communication, Layer 4-aware devices include:

- Layer 4 Firewall
- Load Balancer

---

# Key Points

- Layer 4 is called the Transport Layer.
- TCP provides reliable communication.
- UDP provides fast communication.
- The Transport Layer uses port numbers.
- TCP uses the Three-Way Handshake.
- TCP ensures ordered and reliable delivery.
- UDP is commonly used for real-time applications.

---

# Summary

The Transport Layer ensures efficient communication between applications by managing segmentation, reliability, flow control, and port addressing. It supports both TCP for reliable communication and UDP for high-speed communication, making it one of the most important layers in the OSI Model.