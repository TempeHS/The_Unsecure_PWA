# Cross Frame Scripting

Cross-frame scripting (XFS) is an attack that combines malicious JavaScript with an iframe that loads a legitimate page in an effort to steal data from an unsuspecting user. This attack is usually only successful when combined with social engineering. An example would consist of an attacker convincing the user to navigate to a web page the attacker controls. The attacker’s page then loads malicious JavaScript and an HTML iframe pointing to a legitimate site. Once the user enters credentials into the legitimate site within the iframe, the malicious JavaScript steals the keystrokes.

[This example](index.html) demonstrates how easy it is to spoof a webpage, in this case, the Unsecure PWA.

This attack is particularly effective on mobile devices, as the browser hides most of the URL, and the spoofing page only requires some HTML and some inline JS. That is why XFS coupled with SMS scams are some of the most successful.

> [!NOTE]
> Make sure the Unsecure PWA is being served at [http://127.0.0.1](http://127.0.0.1) before opening the demonstration page.  
> `python main.py`

As a more sophisticated attack, the threat actors would:

1. Serve both sites through a proxy circumventing any CORS CSP policy
2. Have a back-to-base script that intercepts and transmits input data (username, password, credit card, etc) without the user knowing.
3. Have a threat actor listening for inputs and interacting/handling the victim, which is how 2FA is often bypassed.

How to secure against this attack

1. End user education.
2. Monitor HTTP logs for unusually repetitive GET calls.
3. Implement a Content Security Policy (CSP) preventing `<iframe>` loading.
