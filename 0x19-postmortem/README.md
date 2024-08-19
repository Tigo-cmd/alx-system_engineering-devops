# **Postmortem: Unauthorized Access to Customer Database**

## **Incident Overview**

**Date & Time:**  
**August 19th, 2024, at 00:00 hours**

On August 19th, 2024, at 00:00 hours, our Intrusion Detection System (IDS) detected suspicious activity from an unidentified IP address. This activity triggered a global outage of our Web Application Firewall (WAF), leading to the following consequences:

- 100% of incoming web traffic was not filtered for security threats.
- 40% of customer websites were exposed to potential security breaches.
- Increased risk of Distributed Denial of Service (DDoS) attacks and data breaches.

## **Timeline of Events**

### **August 19th, 2024**

**00:01:**

- The IDS triggered an alert for suspicious activity targeting a web application server. Simultaneously, an alert was generated for a WAF system failure.
- The alert indicated an attempted exploitation of a SQL injection vulnerability.

**00:20:**

- The security team observed that the WAF system was unresponsive and began an investigation to identify the source of the attack.
- The team isolated the affected web application server to prevent further unauthorized access attempts.
- Initial assumptions pointed to a network connectivity issue, leading the investigation to focus on routing and switching equipment.

**00:30:**

- The team analyzed server logs to assess the extent of the breach.
- The initial investigation suggested a successful SQL injection attack, potentially compromising a customer database.
- A software bug in the WAF system's rule update process was also discovered.

**01:00:**

- The specific customer data accessed during the breach was identified. This included customer names, email addresses, and hashed passwords.

**02:00:**

- The team began patching the SQL injection vulnerability on the web application server and identified a failover configuration issue, which was also resolved.
- Additional security measures were implemented to strengthen the application’s security.

**05:00:**

- The security team completed the patching process, confirmed the security of the web application server, and deployed a fix to restore the WAF system.

**06:00:**

- A communication plan was drafted to inform affected customers about the incident, including details of the breach, the potentially compromised data, and the steps taken to mitigate risks.

**07:00:**

- Official communication was sent to affected customers via email, explaining the incident and recommending actions such as password resets.

## **Root Cause Analysis**

The root cause of the incident was a successful SQL injection attack against a vulnerable web application server. The attacker exploited a misconfigured Web Application Firewall, allowing them to inject malicious SQL code into database queries and gain unauthorized access to the customer database.

## **Contributing Factors**

- **Unpatched Vulnerability:** The web application server contained a known SQL injection vulnerability that had not been patched.
- **Misconfigured WAF:** The WAF was misconfigured, allowing the attacker to bypass critical security controls.
- **Insufficient Input Validation:** The application lacked adequate input validation mechanisms to prevent malicious code injection attempts.

## **Resolution and Preventive Measures**

- **Patched Vulnerability:** The security team successfully patched the SQL injection vulnerability on the web application server.
- **Reconfigured WAF:** The WAF was reconfigured with proper failover settings and updated rules to block similar attacks.
- **Enhanced Application Security:** Additional security measures were implemented to strengthen the overall security posture of the web application.
- **Customer Notification:** Affected customers were promptly informed about the incident through email communication.

## **Preventive Recommendations**

- **Regular Security Audits:** Implement a program for regular security audits of web applications and infrastructure to proactively identify and address vulnerabilities.
- **Data Encryption:** Consider implementing encryption for sensitive customer data stored in databases to minimize the impact of potential breaches.
- **Secure Coding Practices:** Adopt secure coding practices, including regular vulnerability assessments, to reduce security risks.
- **Robust Incident Response Plans:** Ensure that robust incident response plans are in place, allowing for prompt and effective communication with affected customers during security incidents.

