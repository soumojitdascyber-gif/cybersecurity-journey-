# Layer 6 - Presentation Layer

## Definition

The **Presentation Layer** is the **6th layer** of the OSI Model. It is responsible for translating, formatting, encrypting, and compressing data so that both the sender and receiver can understand the information correctly.

It acts as the **translator** between the Application Layer and the lower OSI layers.

---

# Purpose

The main purpose of the Presentation Layer is to ensure that data is presented in a format that both communicating systems can understand.

It also provides:

- Data Translation
- Data Encryption
- Data Decryption
- Data Compression
- Data Decompression

---

# Responsibilities

The Presentation Layer is responsible for:

- Translating data formats
- Encrypting sensitive information
- Decrypting encrypted data
- Compressing data before transmission
- Decompressing received data
- Character encoding conversion
- Data formatting

---

# How It Works

When a user visits:

```
https://github.com
```

The Application Layer creates the request.

Before the request moves to the lower layers:

- Data is converted into a standard format.
- HTTPS encrypts the data using TLS/SSL.
- The encrypted data is sent to the Transport Layer.

When the server replies:

- The Presentation Layer decrypts the received data.
- Decompresses it if necessary.
- Converts it into a readable format.
- Passes it to the Application Layer.

---

# Data Unit

Like the Application Layer, the Presentation Layer handles:

```
Data
```

---

# Common Protocols and Standards

| Protocol / Standard | Purpose |
|---------------------|---------|
| SSL | Secure communication (Legacy) |
| TLS | Secure encrypted communication |
| ASCII | Character encoding |
| Unicode | Universal character encoding |
| JPEG | Image format |
| PNG | Image format |
| GIF | Image format |
| MP3 | Audio compression |
| MP4 | Video format |
| MPEG | Video compression |

---

# Common Functions

- Encryption
- Decryption
- Compression
- Decompression
- Data Translation
- Character Encoding
- File Format Conversion

---

# Real-World Example

Suppose a user logs into an online banking website.

Presentation Layer performs:

1. Encrypts the username and password using TLS.
2. Sends encrypted data to lower layers.
3. Receives encrypted server response.
4. Decrypts the response.
5. Displays readable information to the user.

---

# Communication Flow

```
Application Layer

↓

Presentation Layer

↓

Session Layer
```

---

# Real-Life Analogy

Imagine two people speaking different languages.

One speaks English.

The other speaks Japanese.

A translator stands between them and converts each language into one the other can understand.

The Presentation Layer works exactly like that translator.

---

# Common Technologies

- SSL
- TLS
- Base64 Encoding
- JPEG
- PNG
- GIF
- Unicode
- ASCII
- MP3
- MPEG

---

# Key Points

- Layer 6 is called the Presentation Layer.
- It translates data between different systems.
- It encrypts and decrypts sensitive information.
- It compresses and decompresses data.
- TLS and SSL operate at this layer.
- It ensures applications receive readable data.

---

# Summary

The Presentation Layer ensures that data exchanged between systems is readable, secure, and efficient. It handles translation, encryption, decryption, and compression before passing data between the Application Layer and the Session Layer. Without this layer, different systems would struggle to interpret each other's data correctly.