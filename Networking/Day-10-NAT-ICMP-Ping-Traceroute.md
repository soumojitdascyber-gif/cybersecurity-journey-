# Day 10 — NAT, ICMP, Ping & Traceroute

## 1. NAT — Network Address Translation

### Definition

NAT stands for Network Address Translation.

NAT is a technique used by a router to translate private IP addresses into a public IP address so that devices inside a private network can communicate with the Internet.

### Why NAT is Needed

Devices inside a home or office network normally use private IP addresses.

Common private IP ranges are:

- 10.0.0.0/8
- 172.16.0.0/12
- 192.168.0.0/16

These private IP addresses are not directly routable on the public Internet.

NAT allows multiple private devices to share a public IP address.

### Simple Example

    Laptop  →  192.168.1.10
    Phone   →  192.168.1.11
    PC      →  192.168.1.12
                    |
                    v
               NAT Router
                    |
                    v
              Public IP
                    |
                    v
                 Internet

The router performs NAT when devices communicate with the Internet.

### Types of NAT

#### Static NAT

One private IP is mapped to one public IP.

    192.168.1.10  ↔  103.x.x.10

#### Dynamic NAT

Private IP addresses are mapped to available public IP addresses from a public IP pool.

#### PAT — Port Address Translation

PAT is also called NAT Overload.

Multiple private devices can share one public IP by using different port numbers.

    192.168.1.10:5000 ─┐
    192.168.1.11:5001 ─┼──→ NAT Router → Public IP
    192.168.1.12:5002 ─┘

PAT is very common in home Wi-Fi routers.

### Real-Life Example

When a phone, laptop, and PC use the same Wi-Fi:

    Phone   → 192.168.1.10
    Laptop  → 192.168.1.11
    PC      → 192.168.1.12
                  |
                  v
             Wi-Fi Router
                  |
                  v
              Public IP
                  |
                  v
               Internet

All devices can access the Internet through the router's public IP.

### Key Point

NAT mainly solves the problem of limited public IPv4 addresses and allows private networks to communicate with the Internet.

---

## 2. ICMP — Internet Control Message Protocol

### Definition

ICMP stands for Internet Control Message Protocol.

ICMP is used for network control, error reporting, and diagnostic communication.

It works together with IP and is commonly used by tools such as Ping and Traceroute.

### Important Point

ICMP is not TCP and it is not UDP.

It is a separate protocol used mainly for network diagnostics and control messages.

### Common ICMP Messages

Important ICMP messages include:

- Echo Request
- Echo Reply
- Destination Unreachable
- Time Exceeded

### Echo Request and Echo Reply

Ping commonly uses:

    Echo Request  →  Destination
    Echo Reply    ←  Destination

If the destination responds, the sender receives an Echo Reply.

### Time Exceeded

Traceroute makes use of ICMP Time Exceeded messages.

When the TTL of a packet reaches zero, a router can send an ICMP Time Exceeded message back to the sender.

### Destination Unreachable

A device may send an ICMP Destination Unreachable message when a destination or network cannot be reached.

---

## 3. Ping

### Definition

Ping is a network troubleshooting tool used to check whether a destination is reachable and to measure approximate round-trip response time.

### Basic Command

    ping 8.8.8.8

You can also ping a domain:

    ping google.com

### How Ping Works

    Your Computer
          |
          | ICMP Echo Request
          v
      Destination
          |
          | ICMP Echo Reply
          v
    Your Computer

If the destination responds, the computer receives an Echo Reply.

### Example

    64 bytes from 8.8.8.8: time=20 ms

The response time gives an approximate idea of network latency.

### What Ping Can Tell Us

Ping can help check:

- Basic connectivity
- Whether a destination is responding
- Approximate latency
- Packet loss

### Latency

Latency is the time taken for data to travel between two points.

Example:

    time=20 ms

This means the measured round-trip response time is approximately 20 milliseconds.

### Packet Loss

Packet loss occurs when packets sent from one device do not successfully receive a response.

Example:

    Request timeout

Possible causes include:

- Network problems
- Destination not responding
- Firewall filtering ICMP
- Routing problems
- Temporary packet loss

### Important Point

A failed ping does not always mean that the destination is completely down.

Some devices or servers may block ICMP packets while still providing other services normally.

---

## 4. Ping a Domain vs Ping an IP

### Ping an IP Address

    ping 8.8.8.8

This directly sends traffic toward the IP address.

### Ping a Domain

    ping google.com

When a domain name is used, DNS resolution is involved before communication with the destination.

    google.com
        |
        v
    DNS Resolution
        |
        v
    IP Address
        |
        v
    ICMP Ping

Therefore, if a domain cannot be resolved, pinging the domain may fail even when basic IP connectivity is working.

---

## 5. Traceroute

### Definition

Traceroute is a network diagnostic tool used to identify the path packets take from the source device to a destination.

It shows intermediate network hops between the source and destination.

### Linux Command

    traceroute google.com

### Windows Command

    tracert google.com

### Simple Example

    Your PC
       |
       v
    Router 1
       |
       v
    Router 2
       |
       v
    Router 3
       |
       v
    Destination

Each router shown in the path is called a hop.

### What is a Hop?

A hop is one network device, usually a router, through which a packet passes while travelling toward its destination.

Example:

    PC → Router 1 → Router 2 → Router 3 → Server

Here, Router 1, Router 2, and Router 3 are intermediate hops.

---

## 6. How Traceroute Works

Traceroute uses the TTL value of IP packets.

TTL stands for Time To Live.

The TTL value is reduced when a packet passes through a router.

When TTL reaches zero, the router can discard the packet and send an ICMP Time Exceeded message back.

Traceroute uses this behavior to discover the path.

### Simplified Example

First packet:

    TTL = 1

    PC → Router 1

    TTL expires at Router 1
    Router 1 → ICMP Time Exceeded

Second packet:

    TTL = 2

    PC → Router 1 → Router 2

    TTL expires at Router 2
    Router 2 → ICMP Time Exceeded

Third packet:

    TTL = 3

    PC → Router 1 → Router 2 → Router 3

    TTL expires at Router 3
    Router 3 → ICMP Time Exceeded

By increasing TTL step by step, traceroute can discover the path.

---

## 7. Traceroute Example

A traceroute result may look like:

    1    192.168.1.1
    2    10.x.x.x
    3    ISP Router
    4    Another Router
    5    Destination

The number represents the hop number.

For example:

    1 → First hop
    2 → Second hop
    3 → Third hop
    4 → Fourth hop
    5 → Destination

### If a Hop Shows *

Sometimes traceroute may show:

    * * *

This does not automatically mean that the network is broken.

Possible reasons include:

- Router does not respond to traceroute probes
- Firewall filtering
- ICMP filtering
- Network configuration

The traffic may still continue through the network.

---

## 8. Ping vs Traceroute

### Ping

Ping mainly answers:

    "Can I reach the destination?"

It is useful for:

- Connectivity testing
- Measuring approximate latency
- Checking packet loss

### Traceroute

Traceroute mainly answers:

    "What path does the traffic take to reach the destination?"

It is useful for:

- Finding intermediate hops
- Understanding the network path
- Troubleshooting routing problems

### Easy Memory Trick

    PING
    ↓
    Can I reach it?

    TRACEROUTE
    ↓
    How does the traffic reach it?

---

## 9. Ping and Traceroute in Troubleshooting

Suppose a website cannot be accessed.

A simple troubleshooting process can be:

    Check Network
          |
          v
    Ping Default Gateway
          |
          v
    Ping Public IP
          |
          v
    Check DNS
          |
          v
    Run Traceroute
          |
          v
    Identify Possible Problem

### Step 1 — Check Local Gateway

    ping 192.168.1.1

If this works, your device may be able to communicate with the local router.

### Step 2 — Check Public IP Connectivity

    ping 8.8.8.8

If this works, basic Internet connectivity may be working.

### Step 3 — Check Domain

    ping google.com

If the IP works but the domain does not, DNS resolution may be the problem.

### Step 4 — Check the Path

Linux:

    traceroute google.com

Windows:

    tracert google.com

This can help identify where the network path may have a problem.

---

## 10. NAT + ICMP + Ping + Traceroute Together

These concepts can be understood together.

Suppose a laptop wants to reach a server on the Internet.

    Laptop
    Private IP
    192.168.1.10
          |
          v
      NAT Router
          |
          | Public IP
          v
       Internet
          |
          v
       Router 1
          |
          v
       Router 2
          |
          v
       Server

NAT translates the private IP when traffic leaves the private network.

ICMP can be used for diagnostic communication.

Ping can check whether the destination responds.

Traceroute can help show the path and intermediate hops.

---

## 11. Basic Commands

### Ping an IP

    ping 8.8.8.8

### Ping a Domain

    ping google.com

### Traceroute on Linux

    traceroute google.com

### Traceroute on Windows

    tracert google.com

### Windows Ping

    ping 8.8.8.8

---

## 12. Important Terms

### NAT

Translates private IP addresses to public IP addresses.

### Private IP

An IP address used inside a private/local network.

Examples:

    192.168.x.x
    10.x.x.x
    172.16.x.x – 172.31.x.x

### Public IP

An IP address used for communication over the public Internet.

### ICMP

A protocol used for network control, error reporting, and diagnostics.

### Ping

A tool used to test connectivity and measure approximate response time.

### Traceroute

A tool used to discover the network path to a destination.

### Hop

A router or network device through which a packet passes.

### Latency

The time taken for data to travel between two points.

### Packet Loss

When packets fail to successfully reach the destination or receive a response.

### TTL

Time To Live. It limits how many router hops a packet can pass through before being discarded.

### DNS

Domain Name System.

DNS translates domain names such as google.com into IP addresses.

---

## 13. Quick Revision

    NAT
     ↓
    Private IP → Public IP

    ICMP
     ↓
    Network diagnostic/control messages

    Ping
     ↓
    Checks connectivity + latency

    Traceroute
     ↓
    Shows path + hops

    DNS
     ↓
    Domain name → IP address

---

## 14. Final Difference

    NAT
    → Translates IP addresses

    ICMP
    → Provides network control and diagnostic messages

    Ping
    → Checks whether a destination responds

    Traceroute
    → Shows the path and intermediate hops

    DNS
    → Resolves domain names into IP addresses

---

# Day 10 Summary

Today I learned:

- NAT
- Private IP and Public IP
- Static NAT
- Dynamic NAT
- PAT / NAT Overload
- ICMP
- Echo Request
- Echo Reply
- Destination Unreachable
- Time Exceeded
- Ping
- Latency
- Packet Loss
- Traceroute
- TTL
- Network Hops
- Ping vs Traceroute
- DNS and basic troubleshooting

## Key Takeaway

    NAT        → Private IP to Public IP translation
    ICMP       → Network diagnostic/control protocol
    Ping       → Checks connectivity and response time
    Traceroute → Checks network path and hops
    DNS        → Converts domain names to IP addresses

**Day 10 Completed — Networking Fundamentals 🚀**