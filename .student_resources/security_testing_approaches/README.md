# Security Testing Approaches

Software Engineers should consider security and privacy at every phase of the SDLC to ensure that security is an integral part of the development process. As an application moves through phases of the SDLC, the cost of patching a vulnerability increases.

| Phase | Security by Design Processes |
| -------- | ------- |
| Requirements definition | <ul><li>Gather specific security and privacy requirements</li><li>Vulnerability assessment</li></ul> |
| Determining specifications | <ul><li>Explict security and privacy specifications</li><li>Risk assessment</li></ul> |
| Design | <ul><li>Threat modelling</li><li>Security design review</li><li>Security tests included in test designs</li></ul> |
| Development | <ul><li>Code reviews</li><li>Static application security testing</li></ul> |
| Integration | <ul><li>Risk assessment</li><li>Code reviews</li><li>Dynamic application security testing</li><li>Grey-box penetration testing</li></ul> |
| Testing and debugging | <ul><li>Code reviews</li><li>Static application security testing</li><li>Dynamic application security testing</li><li>Penetration testing</li></ul> |
| Installation | <ul><li>Penetration testing</li><li>Vulnerability assessment</li></ul> |
| Maintenance | <ul><li>Log monitoring & reporting</li><li>Vulnerability assessment</li></ul> |

## Code review
Code review is the process of thoroughly examining and evaluating an application's source code to identify potential security vulnerabilities at the code level. It is a manual approach to white-box testing.

| Area of focus | Questions to ask |
| -------- | ------- |
| Privacy | <ul><li>Is sensitive data stored that is not required for the application?</li><li>Is sensitive data in error logged to the log files?</li><li>Are passwords encryted before storage or use?</li><li>Can users download and delete their data?</li><li>Are users provided access to the privacy policy?</li><li>Are users who shouldn't have access to the log files able to access them (any or all employees)?</li></ul> |
| Authentication | <ul><li>Are application users authenticated, or are they all treated as anonymous users?</li><li>What factors are used for authentication (such as passwords, tokens, and certificates)?</li><li>If passwords are being used, are there any policies regarding complexity or age in place?</li></ul> |
| Authorization | <ul><li>Are there different roles that users can be given depending on the applications’ function?</li><li>Is the authorization data cached checked for each incoming request?</li><li>Are there any private, sensitive data files stored in the web root that are not authorized for the regular user?</li></ul> |
| Data Validation | <ul><li>Is the user-submitted data validated?</li><li>Is data validated as soon as it comes in from the user or when it is used by the code?</li><li>How is the data validation accomplished (whitelisting, blacklisting, min/max, etc.)?</li><li>Are you using a database? If so, are you passing arguements</li></ul> |
| Exception/Error Handling | <ul><li>What approach(s) for error handling is being used?</li><li>What kind of details about an error are displayed to the user?</li><li>Are errors logged with enough detail for analysis?</li><li>Are database errors logged with enough detail for analysis?</li></ul> |
| Session Management | <ul><li>Is there any way the application manages or stores session state, and if so, how?</li><li>How is the session id being generated?</li><li>Is the previous session deleted when a user logs into the site and creates a new session?</li><li>Are tokens used for session management? If yes, what algorithm is used?</li><li>Any timeouts for sessions?</li></ul> |
| Logging | <ul>Is any logging being used within the code?<li>Where are generated log messages sent?</li><li>Are you logging any input that is not validated first or data that has failed validation?</li><li>Are log messages time-stamped?</li><li>  </li><li>Is any sensitive data written to a log (e.g., password, API key, etc.)?</li></ul> |
| Encryption | <ul>Are there any encryption algorithms used within the code at all?  (SSL, TLS, RSA?)</li><li>Are passwords encrypted before use with a 'salt' and a 'hash' algorithm></li><li>Where did you get the library's implementation, and what version is it using?</li></ul> |

---

## Static application security testing (SAST)

Static application security testing (SAST), or static analysis, is a testing methodology that analyzes source code to find security vulnerabilities. It is usually an automated approach to white-box testing that scans an application before the code is compiled.

[List of SAST tools](https://owasp.org/www-community/Source_Code_Analysis_Tools)

GitHub integrates a range of SAST tools; read the [GitHub Security Scan documentation](https://docs.github.com/en/code-security).

| *SAST advantages* | *SAST disadvantages* |
| -------- | ------- |
| - Reduction in manual effort | - Unable to detect business logic flaws |
| - Time efficient | - Cannot discover runtime issues |
| - Can be performed at the early stages of the SDLC | - Not well suited to track issues where user input is involved |
| - Offers 100% code coverage | - Requires access to the source code |
| - Provide an elaborate report | - Unable to provide application Specific Recommendations |

---

## Dynamic application security testing (DAST)
Dynamic application security testing (DAST) is a testing methodology in which testers examine an application while it’s running but have no knowledge of the application’s internal interactions or designs at the system level and no access or visibility of application source code. This is an automated approach to black-box testing.

[List of DAST tools](https://owasp.org/www-community/Vulnerability_Scanning_Tools)

| *DAST advantages* | *DAST disadvantages* |
| -------- | ------- |
| Produces virtually no false positives | Requires working application to be tested |
| Can discover runtime issues | Needs special testing infrastructure and customization |
| Can discover issues based on user interaction with the software | Often performed towards the end of the software development cycle |
| Does not require access to the source code | Does not cover all code paths |

## Vulnerability assessment

A vulnerability assessment is a systematic review of a system's security weaknesses. It evaluates whether the system is susceptible to any known vulnerabilities, assigns severity levels to those vulnerabilities, and recommends remediation or mitigation. The focus of a vulnerability assessment is infrastructure, processes, and practices. It is more about the organisation than the source code of a single application.

### Specific vulnerability assessments

- *Host assessment* – The assessment of critical servers, which may be vulnerable to attacks.
- *Network assessment* – The assessment of policies and practices to prevent unauthorized access to private or public networks and network-accessible resources.
- *Database assessment* – The assessment of databases and data systems for vulnerabilities and misconfigurations, identifying rogue datasets/databases or insecure dev/test environments.
- *Application scans* – The identification of security vulnerabilities in web applications and their source code using DAST & SAST approaches.

### Threat Modelling vulnerabilities
Threat modelling is the process of using hypothetical scenarios, system diagrams, and testing to help secure systems and data. By identifying vulnerabilities, helping with risk assessment, and suggesting corrective action, threat modelling helps improve cybersecurity and trust in key business systems.

<table>
<tr>
    <td><strong>Threat</strong></td>
    <td>A threat actor will intercept a username and password and then use the credentials to gain access to the system</td>
</tr>
<tr>
    <td><strong>Countermeasure</strong></td>
    <td>2FA has been implemented</td>
</tr>
</table>

## Penetration testing

> [!Warning]
> Students MUST be extremely aware of the legal implications of performing unauthorised penetration testing. Students MUST only perform penetration tests on their applications or peers' applications with expressed permission.

Penetration testing (or pen testing) is a security exercise in which a cyber-security expert attempts to find and exploit vulnerabilities in a computer system. The purpose of this simulated attack is to identify any weak spots in a system’s defences that attackers could exploit by deploying the same strategies. Penetration testing requires the use of both automated tools and brute-force attacks.

### Types of penetration testing

- *White-box pen test* - In a white-box pen test, the tester will perform tests with full knowledge of the application, often live watching the logs as they perform tests.
- *Grey-box pen test* - In a grey-box pen test, the tester will perform tests with some knowledge on the application.
- *Black-box pen test* - In a black-box pen test, the tester is given no background or insight into the source code and is only provided the front end of the application.
- Organisational level penetration testing such as _Covert pen test_, _External pen test_ and _Internal pen test_ are not in the scope of this course.

### Brute force testing tools/support

- [XSS test scripts](.student_resources\XSS\README.md#Non-destructive_XSS_Test_Scripts) some sample scripts to apply to input boxes to test for XSS vulnerabilities.
- [SQL Injections test scripts](https://www.w3schools.com/sql/sql_injection.asp) some sample scripts to apply to login and input boxes to test for SQL injection vulnerabilities.
- [Common usernames & passwords](https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials) to inpit to any dictionary or bruteforce test.
- [Simple HTTP Request Tool](.student_resources\flask_safe_API\index.html) a simple website to test HTTP requests for a localhost website.
- [CyberChef - The Cyber Swiss Army Knife](https://gchq.github.io/CyberChef/) A simple, intuitive web app for analysing and decoding data.

### Pen testing tools/support

- [ZAPROXY](https://www.zaproxy.org/) Open source penetration testing application.
- [View DNS](https://viewdns.info/) suite of DNS and hosting scanning tools.
- [MX Toolbox](https://mxtoolbox.com/NetworkTools.aspx) All of your MX record, DNS, blacklist and SMTP diagnostics in one integrated tool.
- [SSL Tools](https://www.ssllabs.com/projects/index.html) suite of SSL scanning tools.
- [Postman](https://www.postman.com/) A tool to test API's and applications.
- [Wireshark](https://www.wireshark.org/about.html) the world's foremost network protocol analyser.
- [A expensive list of open source pen-testing tools](https://www.esecurityplanet.com/applications/open-source-penetration-testing-tools/).

> [!Caution]
> For the [NESA software engineering syallabus](https://curriculum.nsw.edu.au/learning-areas/tas/software-engineering-11-12-2022/overview); students only need to know that penetration testing tools exist and have basic experience with using a tool and it's reporting capabilities. Students should not spend excessive time comparing or testing different tools.
