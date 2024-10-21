# Cross-Site Request Forgery (CSRF)

Cross-Site Request Forgery (CSRF) is an attack that forces an end user to execute unwanted actions on a web application in which they’re currently authenticated. With a little help of social engineering (such as sending a link via email or chat), an attacker may trick the users of a web application into executing actions of the attacker’s choosing. If the victim is a normal user, a successful CSRF attack can force the user to perform state-changing requests like transferring funds, changing their email address, and so forth. If the victim is an administrative account, CSRF can compromise the entire web application. A CSRF attack generally requires an internal threat actor to provide insight into the internal workings of the API or system, which makes it one of the more challenging cyber vulnerabilities to mitigate.

## How to penetrate test for a this vulnerability

1. Create a simple webpage with a duplicate form that declares the `value` attribute for each form input. See [/index.html](/index.html), which is set up as an example whale or spear phishing attack that a threat actor would use to exploit the vulnerability through a targeted victim who is known to have administration-level authorisation.
2. Submit the form. In the example, this is done by clicking the 'click to claim' link.
3. If you are doing white-box testing, look in the log and users table of the database to see if the user was added. If you are doing black-box testing, try the credentials and see if they are successful in logging in.

## How to countermeasure this vulnerability

- Implement [Flask WTForms](https://flask-wtf.readthedocs.io/en/1.2.x/), which generates and requires a unique secret key by default.
- Implement business knowledge access levels.
- End-user education.
- HTTPS encryption.
- End-user education.
- Implement a CORS [Content Security Policy (CSP)](../content_security_policy/README.md).
- Understand how the attack can be executed in the specific context of the application and user, then [code review](../security_testing_approaches/README.md#Code_review) with specific scenarios in mind.
- Implement three-factor authentication (3FA) for administrative operations.
- Separate production and development environments.
- White-list firewall policies
