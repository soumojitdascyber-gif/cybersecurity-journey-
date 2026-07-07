# Layer 1 - Physical Layer

## Definition

The **Physical Layer** is the **first and lowest layer** of the OSI Model. It is responsible for transmitting raw binary data (bits) over a physical medium such as cables, fiber optics, or wireless signals.

This layer focuses on the physical connection between devices rather than the data itself.

---

# Purpose

The primary purpose of the Physical Layer is to establish, maintain, and transmit electrical, optical, or radio signals between devices.

---

# Responsibilities

The Physical Layer is responsible for:

- Bit Transmission
- Physical Connectivity
- Signal Encoding
- Signal Transmission
- Data Rate Control
- Cable Standards
- Physical Topology

---

# How It Works

When a device sends data:

1. The Data Link Layer sends a frame.
2. The Physical Layer converts the frame into bits (0s and 1s).
3. The bits are transmitted through cables, fiber optics, or wireless signals.
4. The receiving device converts the bits back into a frame and forwards it to the Data Link Layer.

---

# Data Unit

The Protocol Data Unit (PDU) of the Physical Layer is:

```

Bits

```

---

# Transmission Media

The Physical Layer uses different transmission media.

### Guided Media

- Twisted Pair Cable (UTP/STP)
- Coaxial Cable
- Fiber Optic Cable

### Unguided Media

- Wi-Fi
- Bluetooth
- Infrared
- Radio Waves

---

# Network Topologies

Common physical network topologies include:

- Bus
- Star
- Ring
- Mesh
- Tree

---

# Common Devices

Devices operating at Layer 1 include:

- Hub
- Repeater
- Modem (Physical Signal Conversion)
- Network Cables
- Fiber Optic Cable
- Connectors

---

# Signal Types

The Physical Layer transmits data using:

- Electrical Signals
- Optical Signals
- Radio Signals

---

# Communication Flow

```

Data Link Layer

↓

Physical Layer

↓

Transmission Medium

↓

Receiving Device

```

---

# Real-World Example

Suppose you connect your laptop to a router using an Ethernet cable.

The Physical Layer:

- Converts data into bits.
- Sends the bits through the Ethernet cable.
- Delivers the bits to the router.
- The router forwards the data to the next layer.

---

# Common Standards

Some common Physical Layer standards include:

- Ethernet (IEEE 802.3)
- Wi-Fi (IEEE 802.11)
- Bluetooth
- USB
- Fiber Optic Standards

---

# Key Points

- Layer 1 is called the Physical Layer.
- It transmits raw bits.
- It uses electrical, optical, or wireless signals.
- It defines cables, connectors, and transmission media.
- Hubs and Repeaters operate at this layer.
- The PDU is Bits.

---

# Summary

The Physical Layer forms the foundation of the OSI Model. It is responsible for transmitting raw bits through physical media such as cables and wireless signals. Without the Physical Layer, communication between devices would not be possible, making it the essential building block of all network communication.