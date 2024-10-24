> [!CAUTION]
> # DISCLAIMER
> __This progressive web app has been designed with a range of security vulnerabilities. The app has been specifically designed for students studying the [NESA HSC Software Engineering Course](https://curriculum.nsw.edu.au/learning-areas/tas/software-engineering-11-12-2022/content/n12/fa039e749d). The app is NOT secure and should NOT be used in a production environment.__

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

## Dependencies & Deployment

### Dependencies

- VSCode
- Python 3+
- Flask pip install flask
- The Resources and samples in [.student_resources](.student_resources/) require additional dependencies. Please take a look at the README.md in each folder.

### Deployment

```bash
git clone https://github.com/TempeHS/The_Unsecure_PWA.git
CD THE_UNSECURE_PWA
python main.py
```

> [!Important]
> Because the repository contains a range of commonly used cracks and hacks (which should not be a surprise, as that is what the app & repository contents are modelling). Your operating system will likely identify a 'Zip Download' from GitHub as containing Trojans and block the download. Use `git clone https://github.com/TempeHS/The_Unsecure_PWA.git` in VSCode to download the code base. If you are concerned by the warning, please feel free to code review yourself or email me [benjamin.jones21@det.nsw.edu.au](mailto:benjamin.jones21@det.nsw.edu.au).

Once deployed, the app can be accessed on either:
- [http://localhost:5000](http://localhost:5000)
- [http://127.0.0.1:5000](http://127.0.0.1:5000)
- [http://{10.185.x.x}:5000](http://10.185.0.0:5000) where 10.185.x.x is the LAN IP address for the host

> [!Tip]
> Many of the resources in [.student_resources](.student_resources/) have been written assuming the student is running the app locally, so http://127.0.0.1:5000 has been used. If the teacher is hosting the app and students are black-box testing, then the html/js in the examples will need changing to reference the LAN IP address [http://{10.185.x.x}:5000](http://10.185.0.0:5000) of the host.

---

## Support

To support students first understanding specific security vulnerabilities and privacy issues and then follow a best practice approach to patching them, the links below have been provided with most resources provided from the [.student_resources folder](.student_resources) and specifically aligned to the [NESA Course Specifications](https://library.curriculum.nsw.edu.au/341419dc-8ec2-0289-7225-6db7f2d751ef/94e1eb0a-0df7-4dbe-9b72-5d5e0d17143a/software-engineering-11-12-higher-school-certificate-course-specifications.PDF) and [NESA Software Engineering Syllabus](https://curriculum.nsw.edu.au/learning-areas/tas/software-engineering-11-12-2022/content/n12/fa039e749d).

### Security support

- [Security testing approaches](.student_resources\security_testing_approaches\README.md) for the NESA Software Engineering Syllabus.
- [Web Security Testing Guide \(WSTG\) Project](https://owasp.org/www-project-web-security-testing-guide/v42/) a very detailed resource for web application developers.
- [ZAPROXY](https://www.zaproxy.org/) Open source penetration testing application

### Privacy issues support

- [Australian Government Privacy](https://www.ag.gov.au/rights-and-protections/privacy).
- [How to create an app that complies with data privacy regulations](https://moldstud.com/articles/p-how-to-create-an-app-that-complies-with-data-privacy-regulations).
- [Australian Government - Responding to cyber security incidents](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/ism/cyber-security-guidelines/guidelines-cyber-security-incidents)

### Solution implementation support

- [Broken Authentication and Session Management](.student_resources\broken_authentication_and_session_management\README.md).
- [Content Security Policy - CSP](.student_resources\content_security_policy\README.md)
- [Create a safe API with Flask](.student_resources\flask_safe_API\README.md).
- [Cross Frame Scripting - XFS](.student_resources\XFS\README.md).
- [Cross Site Request Forgery - CSRF](.student_resources\CSRF\README.md).
- [Cross Site Scripting - XSS](.student_resources\XSS\README.md).
- [Encrypting passwords](.student_resources\encrypting_passwords\README.md).
- [Exception management](.student_resources\defensive_data_handling\README.md#exception-handling).
- [Defensive data handling](.student_resources\defensive_data_handling\README.md).
- [Race conditions](.student_resources/race_conditions)
- [Secure input form attributes](.student_resources\secure_form_attributes\README.md).
- [SQL injection](.student_resources\SQL_Injection\README.md).
- [SSL encryption for localhost 127.0.0.1](https://hackernoon.com/how-to-get-sslhttps-for-localhost-i11s3342) - external link.
- [Two Factor Authentication - 2FA](.student_resources\two_factor_authentication\README.md).

---

## Cybersecurity Definitions

| Metalanguage | Definition |
| --- | --- |
| Attack vector | An approach to exploiting multiple vulnerabilities |
| Brute force | uses trial and error to crack a system or software |
| Exploit | The act of using a vulnerability to enter or compromise software or system |
| Phishing | A wide base attack that is 'fishing' for success |
| Social engineering | Use of deception to manipulate individuals into divulging confidential or personal information |
| Spear phishing | A targetted attack where the threat actor has personal knowledge of the victim |
| Threat actor | A person or group with malicious intentions |
| Vulnerability | A weakness in a system, hardware or software |
| Whale phishing | A targetted attack by a threat actor where the victim is known to have escalated authorisation in a system or software |

---

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/TempeHS/The_Unsecure_PWA">The Unsecure PWA</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/benpaddlejones">Ben Jones</a> is licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1" alt=""></a></p>
