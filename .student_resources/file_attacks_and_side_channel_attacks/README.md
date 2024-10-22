# File Attacks and Side Channel Attacks

## File Attacks

A file attack is an attack where threat actors use certain file types, usually a *.DOCX, *.XLSX, or *.PDF. Designed to entice users to open the document or follow a malicious link in a document. If the file in is embedded with malicious code, the code will be executed when the document is opened.

The [urgent_finance_review.xlsm](urgent_finance_review.xlsm) spreadsheet is a common file attack approach that is sent in a convincing email. The example only has a simple prompt box. However, it is only a few more lines of code to silently install key logging software with back to base reporting to the threat actor.

## How to countermeasure file attacks

- Countermeasure common vulnerabilities

     [Cross Frame Scripting - XFS](..\XFS\README.md)
     [Cross Site Request Forgery - CSRF](..\CSRF\README.md)
     [Cross Site Scripting - XSS](..\XSS\README.md)
     [Broken Authentication and Session Management](..\broken_authentication_and_session_management\README.md).

- Implement [Two Factor Authentication - 2FA](..\two_factor_authentication\README.md).
- End User education
- White list firewalls
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
