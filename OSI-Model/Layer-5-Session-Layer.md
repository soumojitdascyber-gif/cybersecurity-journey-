# Layer 5 - Session Layer

## Definition

The **Session Layer** is the **5th layer** of the OSI Model. It is responsible for establishing, managing, maintaining, and terminating communication sessions between two devices.

A **session** is a temporary connection that allows two systems to exchange data continuously.

---

# Purpose

The main purpose of the Session Layer is to control communication between applications by creating and managing sessions.

It ensures that communication starts correctly, stays active during data exchange, and ends properly when communication is complete.

---

# Responsibilities

The Session Layer is responsible for:

- Session Establishment
- Session Maintenance
- Session Termination
- Authentication
- Authorization
- Synchronization
- Dialog Control
- Checkpoint Recovery

---

# How It Works

Suppose you log into:

```
https://github.com
```

The Session Layer performs the following tasks:

1. Creates a communication session.
2. Maintains the session while browsing.
3. Keeps the user authenticated.
4. Synchronizes communication.
5. Terminates the session when the user logs out.

---

# Data Unit

The Session Layer handles:

```
Data
```

---

# Common Protocols

| Protocol | Purpose |
|----------|---------|
| NetBIOS | Session management |
| RPC (Remote Procedure Call) | Remote communication |
| PPTP | VPN sessions |
| SIP | VoIP session management |
| SMB Session Service | File sharing sessions |

---

# Session Phases

## 1. Session Establishment

Creates a communication session.

Example:

```
Client -----> Server

Session Started
```

---

## 2. Session Maintenance

Keeps communication active while data is exchanged.

Example:

```
User browsing website

↓

Session Active
```

---

## 3. Session Termination

Ends the communication safely.

Example:

```
Logout

↓

Session Closed
```

---

# Dialog Control

The Session Layer manages who can transmit data.

Two communication modes:

- Half Duplex
- Full Duplex

Example:

Walkie-talkie → Half Duplex

Phone Call → Full Duplex

---

# Synchronization

Large files are divided into checkpoints.

If communication is interrupted, transmission resumes from the last checkpoint instead of starting over.

Example:

Downloading a 5 GB file.

Internet disconnects at 4 GB.

Download resumes from 4 GB.

---

# Authentication

Before allowing communication, the Session Layer helps maintain authenticated sessions.

Example:

Username

↓

Password

↓

Session Created

---

# Real-World Example

Suppose you are watching a YouTube video.

The Session Layer:

- Creates the session.
- Maintains the connection.
- Keeps the stream active.
- Ends the session when you close the browser.

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
```

---

# Real-Life Analogy

Imagine a phone call.

You dial the number.

↓

The call connects.

↓

You talk.

↓

You end the call.

This entire process is similar to how the Session Layer works.

---

# Common Applications

- Zoom
- Microsoft Teams
- Google Meet
- Skype
- WhatsApp Calls
- Remote Desktop
- VPN Connections

---

# Key Points

- Layer 5 is called the Session Layer.
- It establishes communication sessions.
- It maintains active sessions.
- It synchronizes communication.
- It controls dialogs.
- It terminates sessions safely.
- It supports checkpoint recovery.

---

# Summary

The Session Layer is responsible for creating, managing, and terminating communication sessions between devices. It ensures reliable communication by maintaining active sessions, handling synchronization, supporting authentication, and properly ending sessions after communication is complete.