# Smishing (SMS Phishing)

## Definition

Smishing, short for SMS Phishing, is a social engineering attack where attackers use text messages (SMS) to trick victims into revealing sensitive information, clicking malicious links, or downloading malware.

Smishing combines phishing techniques with mobile communication to target users directly through their phones.

---

## Objectives

- Credential theft
- Financial fraud
- Malware delivery
- Personal information theft
- Account takeover

---

## How Smishing Works

1. Attacker sends a fraudulent SMS message.
2. Victim receives the message.
3. Message creates urgency or fear.
4. Victim clicks a malicious link or responds.
5. Attacker steals credentials or installs malware.

---

## Common Smishing Scenarios

### Banking Alert

Example:

"Your bank account has been locked. Verify now."

### Delivery Scam

Example:

"Your package delivery failed. Click here to reschedule."

### Prize Scam

Example:

"Congratulations! You have won ₹50,000. Claim now."

### OTP Theft

Example:

"Share your OTP to verify your account."

---

## Common Indicators

- Unexpected SMS messages
- Urgent requests
- Shortened URLs
- Requests for OTPs
- Requests for credentials
- Unknown sender numbers

---

## Attack Flow

1. SMS delivered.
2. Victim trusts the message.
3. Victim clicks malicious URL.
4. Fake login page opens.
5. Credentials stolen.
6. Attacker gains access.

---

## SOC Analyst Investigation

### Analyze SMS Content

Check:

- Sender information
- Embedded URLs
- Social engineering tactics

### URL Analysis

Investigate:

- Domain reputation
- Domain age
- Redirect chains

### Authentication Review

Look for:

- Suspicious logins
- Failed login attempts
- MFA events

### Endpoint Review

Check:

- Browser activity
- Malware execution
- Suspicious applications

---

## Relevant Logs

- DNS Logs
- Proxy Logs
- Authentication Logs
- EDR Logs
- Mobile Device Management (MDM) Logs

---

## MITRE ATT&CK

### T1566 - Phishing

### T1660 - Phishing via SMS

Tactic:

- Initial Access

---

## Detection Techniques

Look for:

- Users accessing newly registered domains
- Credential submissions to suspicious websites
- Multiple users visiting the same phishing URL
- Unusual authentication activity

---

## Prevention

- User awareness training
- MFA implementation
- URL filtering
- Mobile security solutions
- Verification of suspicious messages

---

## Key Takeaway

Smishing is a mobile-based phishing attack that exploits user trust and urgency through SMS messages. Because mobile devices are widely used, smishing remains a highly effective technique for credential theft and fraud.