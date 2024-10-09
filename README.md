> [!CAUTION]
> # DISCLAIMER
> __This progressive web app has been designed with a range of security vulnerabilities. The app has been specifically designed for students studying the [NESA HSC Software Engineering Course](https://curriculum.nsw.edu.au/learning-areas/tas/software-engineering-11-12-2022/content/n12/fa039e749d). The app is NOT secure and should only be used in a sandbox environment.__

<hr style="border: 0.1rem solid #d1d9e0;background:#d1d9e0"/>

# The Unsecure PWA
Your client, "The Unsecure PWA Company", has engaged you as a software engineering security specialist to provide expert advice on the security and privacy of their application. This progressive web app is currently in the testing and debugging phase of the software development lifecycle. 

## The task
You are to run a range of security tests and scans along with a white/grey/black box analysis of the application/source code to identify as many security and privacy vulnerabilities as possible. You are then required to prepare a professionally written report for your client that includes:
1. An overview of your approach to the technical analysis.
2. Document out-of-the-scope privacy and security issues of your report, including;
    - Security or privacy issues that cannot be mitigated by technical engineering solutions
    - Security issues that must be tested in the production environment
4. Identify all security or privacy vulnerabilities you discovered and provide an impact assessment of each.
5. Provide recommendations for "The Unsecure PWA Company's" security and privacy by design approach going forward.  
6. Design and develop implementations using HTML/CSS/JS/SQL/JSON/Python code and/or web content changes as required to patch each vulnerability you discover.

---

> [!TIP]
> ## Teaching advice:
>
> This app has been designed as either a teaching tool, an assessment tool or an assessment as a learning tool. __As a teaching tool__ the teacher can use the app to demonstrate discrete vulnerabilities and then teach the preferred patch method. __As an assessment tool__ the students should be taught the knowledge and skills, then given the app to analyse and report on before designing and developing appropriate patches (patching all will be time-prohibitive). __As an assessment as a learning tool__ teachers can teach vulnerabilities in the app and then support students to design and develop patches while assessing them formatively.

---

## Support

To support students first understanding specific security vunerabilities and privacy issues and then follow a best practice approach to patching them, the links below have been provided with most resources provided from the [.student_resources folder](.student_resources) and specifically aligned to the [NESA Course Specifications](https://library.curriculum.nsw.edu.au/341419dc-8ec2-0289-7225-6db7f2d751ef/94e1eb0a-0df7-4dbe-9b72-5d5e0d17143a/software-engineering-11-12-higher-school-certificate-course-specifications.PDF) and [NESA Software Engineering Syllabus](https://curriculum.nsw.edu.au/learning-areas/tas/software-engineering-11-12-2022/content/n12/fa039e749d).

### Security testing support

- [Security testing approaches](.student_resources\security_testing_approaches\README.md) for the NESA Software Engineering Syllabus.
- [Web Security Testing Guide \(WSTG\) Project](https://owasp.org/www-project-web-security-testing-guide/v42/) a very detailed resource for web application developers.
- [ZAPROXY](https://www.zaproxy.org/) Open source penetration testing application
- [XSS test scripts](.student_resources\XSS\README.md#Non-destructive_XSS_Test_Scripts).
- [SQL Injections test scripts](https://www.w3schools.com/sql/sql_injection.asp).

### Privacy issues support

- [Australian Government Privacy](https://www.ag.gov.au/rights-and-protections/privacy).
- [How to create an app that complies with data privacy regulations](https://moldstud.com/articles/p-how-to-create-an-app-that-complies-with-data-privacy-regulations).
- [Australian Government - Responding to cyber security incidents](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/ism/cyber-security-guidelines/guidelines-cyber-security-incidents)

### Security support

- [The Open Worldwide Application Security Project](https://owasp.org/) is the most current and accurate source of knowledge about web application security.
- [Best practices in protecting flask applications](https://escape.tech/blog/best-practices-protect-flask-applications/).

### Solution implementation support

- [Cross Frame Scripting XFS](.student_resources\XFS\README.md).
- [Cross-Site Request Forgery (CSRF)](.student_resources\CSRF\README.md).
- [Defensive Data Handling](.student_resources\defensive_data_handling).
- [Creating an API with Flask](.student_resources\flask_safe_API\README.md).
- [Secure form attributes](.student_resources\secure_form_attributes\README.md).
- [Two Factor Authentication (2FA)](.student_resources\two_factor_authentication\README.md).
- [Flask broken authentication solution](https://brightsec.com/blog/broken-authentication-impact-examples-and-how-to-fix-it/).
- [SSL encryption for localhost 127.0.0.1](https://hackernoon.com/how-to-get-sslhttps-for-localhost-i11s3342).
- [Flask session management](https://pythonbasics.org/flask-sessions/)
- [Cross Site Scripting XSS](.student_resources\XSS_scripts\README.md).
- [SQL Injections](.student_resources\SQL_Injection).
- [Content Security Policy](.student_resources\content_security_policy\README.md)

---

> [!IMPORTANT]
> # Dependencies
>
> - VSCode
> - Python 3+
> - Flask pip install flask
> - The Resources in [.student_resources](.student_resources/) requires additonal Dependencies please refer to the documentation.

---

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/TempeHS/The_Unsecure_PWA">The Unsecure PWA</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/benpaddlejones">Ben Jones</a> is licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1" alt=""></a></p>
