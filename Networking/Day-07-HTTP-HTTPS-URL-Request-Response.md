# Day 07 – HTTP, HTTPS, URL, HTTP Request & Response

> **SOC Analyst Networking Series**

---

# Learning Objectives

After completing this chapter, you will understand:

- What is HTTP
- What is HTTPS
- Difference between HTTP & HTTPS
- What is a URL
- HTTP Request
- HTTP Response
- Common HTTP Methods
- Common HTTP Status Codes
- Browser to Website Communication
- SOC Analyst Perspective

---

# What is HTTP?

HTTP (HyperText Transfer Protocol) is an Application Layer protocol used for communication between a client (browser) and a web server.

Default Port:

```
80
```

HTTP is **not encrypted**, meaning anyone intercepting the traffic can potentially read its contents.

---

# HTTP Communication

```
Browser
   │
HTTP Request
   │
Web Server
   │
HTTP Response
   │
Browser
```

---

# Advantages

- Fast
- Simple
- Lightweight
- Supported by every browser

---

# Disadvantages

- No Encryption
- Credentials travel in plain text
- Vulnerable to Man-in-the-Middle (MITM) attacks
- Data can be intercepted

---

# What is HTTPS?

HTTPS (HyperText Transfer Protocol Secure) is HTTP running over TLS (Transport Layer Security).

Default Port:

```
443
```

HTTPS encrypts communication between the client and the server.

---

# HTTPS Communication

```
Browser

↓

TLS Handshake

↓

Encrypted Tunnel

↓

HTTP Request

↓

Web Server

↓

HTTP Response

↓

Browser
```

---

# HTTPS Provides

### Confidentiality

No one can read the transmitted data.

---

### Integrity

Data cannot be modified during transmission without detection.

---

### Authentication

The browser verifies the server's identity using a digital certificate.

---

# HTTP vs HTTPS

| HTTP | HTTPS |
|------|-------|
| Port 80 | Port 443 |
| No Encryption | TLS Encryption |
| Less Secure | More Secure |
| Plain Text | Encrypted |
| Vulnerable to MITM | Resistant to MITM |

---

# What is a URL?

URL stands for **Uniform Resource Locator**.

It tells the browser where and how to access a resource.

Example:

```
https://www.example.com/login?id=100
```

---

# URL Structure

```
https://www.example.com/login?id=100
```

Protocol

```
https://
```

Domain

```
www.example.com
```

Path

```
/login
```

Parameter

```
?id=100
```

---

# HTTP Request

An HTTP Request is sent from the client to the web server.

Contains:

- Method
- URL
- Headers
- Body (optional)

Example

```
GET /index.html HTTP/1.1

Host: example.com

User-Agent: Chrome
```

---

# Common HTTP Methods

## GET

Retrieve data.

Example

```
GET /home
```

---

## POST

Send data to the server.

Example

```
POST /login
```

---

## PUT

Update existing data.

---

## DELETE

Delete resources.

---

## HEAD

Retrieve only headers.

---

## OPTIONS

Shows supported HTTP methods.

---

# HTTP Response

The server sends an HTTP Response back to the client.

Contains:

- Status Code
- Headers
- Body

Example

```
HTTP/1.1 200 OK

Content-Type: text/html
```

---

# Common HTTP Status Codes

### 200 OK

Request successful.

---

### 201 Created

Resource created successfully.

---

### 301 Moved Permanently

Permanent redirect.

---

### 302 Found

Temporary redirect.

---

### 400 Bad Request

Invalid request.

---

### 401 Unauthorized

Authentication required.

---

### 403 Forbidden

Access denied.

---

### 404 Not Found

Requested resource not found.

---

### 500 Internal Server Error

Server encountered an internal error.

---

### 503 Service Unavailable

Server temporarily unavailable.

---

# Browser to Website Flow

```
User enters URL

↓

Browser checks cache

↓

DNS Resolution

↓

IP Address received

↓

TCP Three-Way Handshake

↓

TLS Handshake (HTTPS)

↓

HTTP Request

↓

Web Server

↓

HTTP Response

↓

Browser renders webpage
```

---

# SOC Analyst Perspective

A SOC Analyst should monitor:

- Suspicious HTTP POST requests
- Long-lived HTTPS sessions
- Large outbound uploads
- Repeated HTTP requests
- Suspicious User-Agent strings
- Unusual HTTP methods
- Connections to malicious domains
- Large numbers of 401 or 404 responses
- Beaconing behavior
- Possible Data Exfiltration over HTTPS

---

# Important Notes

- HTTPS traffic is encrypted, but **encrypted does not mean safe**.
- Malware frequently uses HTTPS for Command and Control (C2).
- Large HTTPS uploads may indicate possible data exfiltration.
- HTTP alone is **not** malicious.
- HTTPS alone is **not** evidence of malware.

Always follow the SOC investigation process:

```
Evidence

↓

Facts

↓

Indicators

↓

Hypothesis

↓

More Evidence

↓

Conclusion
```

Never jump to conclusions without sufficient evidence.

---

# Interview Questions

### Q1. What is HTTP?

### Q2. What is HTTPS?

### Q3. Difference between HTTP and HTTPS?

### Q4. What is a URL?

### Q5. Explain an HTTP Request.

### Q6. Explain an HTTP Response.

### Q7. Difference between GET and POST?

### Q8. What is TLS?

### Q9. Which port does HTTPS use?

### Q10. Can malware use HTTPS?

**Answer:**

Yes.

HTTPS encrypts communication but does **not** guarantee that the traffic is legitimate. Attackers and malware often use HTTPS for Command and Control (C2), malware downloads, and data exfiltration.

---

# Summary

- HTTP = Port 80, No Encryption
- HTTPS = Port 443, TLS Encryption
- URL identifies a web resource
- HTTP Request is sent by the client
- HTTP Response is returned by the server
- HTTPS can also be abused by attackers
- Always base conclusions on evidence, not assumptions