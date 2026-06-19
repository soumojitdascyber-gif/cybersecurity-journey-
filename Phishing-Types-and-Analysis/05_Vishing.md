# Vishing (Voice Phishing)

## Definition

Vishing, short for Voice Phishing, is a social engineering attack where attackers use phone calls or voice messages to trick victims into revealing sensitive information, credentials, banking details, or security codes.

Unlike traditional phishing, vishing relies on voice communication to gain trust and manipulate victims.

---

## Objectives

- Credential theft
- Financial fraud
- Banking information theft
- Account takeover
- Identity theft

---

## How Vishing Works

1. Attacker obtains the victim's phone number.
2. Attacker impersonates a trusted organization.
3. Victim receives a phone call.
4. Victim is pressured to provide information.
5. Attacker uses the stolen information for malicious purposes.

---

## Common Vishing Scenarios

### Fake Bank Support

Example:

"Your bank account has been compromised. Please verify your account details immediately."

---

### Fake Technical Support

Example:

"This is Microsoft Support. Your computer is infected with malware."

---

### Government Impersonation

Example:

"Your national identification has been linked to suspicious activity."

---

### OTP Theft

Example:

"We need your OTP to verify your account."

---

## Common Indicators

- Unsolicited phone calls
- Requests for passwords
- Requests for OTP codes
- Threatening language
- Urgent action requests
- Caller claiming authority

---

## Social Engineering Techniques

### Fear

Victim is threatened with account suspension or legal action.

### Urgency

Victim is pressured to act immediately.

### Authority

Attacker impersonates a trusted institution.

### Trust Exploitation

Victim believes the caller is legitimate.

---

## Attack Flow

1. Call initiated.
2. Trust established.
3. Sensitive information requested.
4. Victim provides information.
5. Attacker gains access.

---

## SOC Analyst Investigation

### Authentication Review

Check:

- Unusual logins
- Failed login attempts
- MFA activity
- Account compromise indicators

### User Validation

Confirm:

- Whether the user received a suspicious call
- Information disclosed during the call

### Endpoint Investigation

Review:

- Recent downloads
- Remote access software installation
- Suspicious processes

### Network Investigation

Analyze:

- DNS activity
- Proxy logs
- External connections

---

## Relevant Logs

- Authentication Logs
- VPN Logs
- DNS Logs
- Proxy Logs
- EDR Logs
- Sysmon Logs

---

## MITRE ATT&CK

### T1598 - Phishing for Information

### T1566 - Phishing

Tactics:

- Initial Access
- Credential Access

---

## Detection Techniques

Look for:

- Account compromise after support-related calls
- MFA approval following suspicious phone activity
- New device logins
- Unusual geographic logins
- Password resets followed by successful logins

---

## Prevention

- Security awareness training
- MFA implementation
- Verification of caller identity
- Never sharing OTPs or passwords
- Reporting suspicious calls

---

## Key Takeaway

Vishing is a voice-based social engineering attack that exploits trust, urgency, and authority to steal sensitive information. Organizations must combine user awareness, MFA, and continuous monitoring to reduce the risk of successful vishing attacks.