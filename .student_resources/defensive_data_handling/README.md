# Defensive Data Handling

## Input validation

Input validation is a security control where input is checked to be valid data. It is best practice to validate data on entry to the application before it is stored or processed. If data is not valid it should be discarded and UI feedback provided to the user.

- [form field attributes](..\secure_form_attributes/README.md) demonstrates best praticies in front-end data validation.
- [Python regular expressions, REGEXR and binary selection](data_handler.py) demonstrates different approaches to prevent a code injection in the back-end. 

## Data sanitisation

Data sanitisation is where data is 'sanitised' or cleaned for processing or storing. This is the process of replacing any potentially malicious characters with non-processing codes so the text will render as expected, but no processing will occur. For example the malicious string **`"';DROP TABLE users"`** when sanitised will be stored as **\&#39;\&#59;DROP TABLE users** but will be render as **`&#39;&#59;DROP TABLE users'**.

### Data sanitisation methods

- The best practice is to make all strings web-safe before storing or processing them using a library like [Python html](https://docs.python.org/3/library/html.html).
- Content loaded from a JSON file is loaded after all JavaScript has been executed, so any malicious code in a JSON will never be executed by the browser.*
- [Jinga2](https://jinja.palletsprojects.com/en/3.1.x/) (built into Flask) converts all strings into web-safe strings before rendering on the front end.*

*_These countermeasures are reactive but are still recommended as best practice in the situation that malicious code bypasses proactive defensive measures._

## Exception Handling

Exception handling is essential in defensive data handling as a malicious user may attempt to exploit the application by providing it with invalid input to attempt to trigger a vulnerability. While simple boolean analysis is the minimum. Students should be familiar with [Python exception handling](https://docs.python.org/3/tutorial/errors.html), specifically the [try](https://docs.python.org/3/reference/compound_stmts.html#try) statement. The Backend data validation with [regular expressions, REGEXR and binary selection](data_handler.py) provides a detailed example of this applied to defensive data handing.

## Logging

Developing and implementing logging as part of defensive data handling improves a developer's chances of detecting malicious behaviour. A log entry should be made with every error, exception or unexpected behaviour, and it should include sufficient details of the event to allow for improvement of data handling practices. A developer and their organisation should include cyclical log reviews as part of the software development lifecycle.
> [!Note]
> [logging is recommended as best practice by the Australian Signals Directorate's Australian Cyber Security Centre](https://www.cyber.gov.au/resources-business-and-government/maintaining-devices-and-systems/system-hardening-and-administration/system-monitoring/best-practices-event-logging-threat-detection).
