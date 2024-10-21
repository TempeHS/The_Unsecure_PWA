# Cross Frame Scripting

Cross-frame scripting (XFS) is an attack that combines malicious JavaScript with an iframe that loads a legitimate page in an effort to steal data from an unsuspecting user. This attack is usually only successful when combined with social engineering. An example would consist of an attacker convincing the user to navigate to a web page the attacker controls. The attacker’s page then loads malicious JavaScript and an HTML iframe pointing to a legitimate site. Once the user enters credentials into the legitimate site within the iframe, the malicious JavaScript steals the keystrokes.

## How to penetrate test for this vulnerability

1. Create a simple webpage that loads the source website in an `<iframe>`. [index.html](index.html) demonstrates how easy it is to spoof a website, in this case, the Unsecure PWA.
2. If the page loads, then it is likely this vulnerability can be exploited.
3. Write a script to read the form data in the iframe and post it to a threat actor every 10 seconds.

```html
<script>
    setTimeout(intercept, 10000);
    function intercept() {
        let iframe = document.getElementById("myFrame");
        let theirUsername = iframe.contentWindow.document.getElementById('username').value;
        console.log(theirUsername);
        setTimeout(intercept, 10000);
    }
</script> 
```

This attack is particularly effective on mobile devices, as the browser hides most of the URL, and the spoofing page only requires some HTML and some inline JS. That is why XFS, coupled with SMS phishing, are some of the most successful.

### As a more sophisticated attack, the threat actors would

1. Serve both sites through a proxy circumventing any CORS [Content Security Policy (CSP)](../content_security_policy/README.md).
2. Have a back-to-base script that intercepts and transmits input data (username, password, credit card, etc) without the user knowing.
3. Have a threat actor listening for inputs and interacting/handling the victim, which is how [2FA](..\two_factor_authentication\README.md) is often bypassed.

## How to countermeasure this vulnerability

1. End user education.
2. Monitor server [logs](..\defensive_data_handling\README.md#Logging) for unusually repetitive GET calls.
3. Implement a [Content Security Policy (CSP)](../content_security_policy/README.md) blocking `<iframe>` loading.
