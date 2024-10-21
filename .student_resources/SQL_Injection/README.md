# SQL Injection

A SQL injection attack consists of inserting or "injecting" SQL code via the input data from the client to the application. A successful SQL injection exploit can read sensitive data from the database and modify database data (Insert/Update/Delete). SQL injection attacks are a type of injection attack in which SQL commands are injected into data-plane input to affect the execution of predefined SQL commands.

[W3Schools has a range of SQL Injection examples with explanations](https://www.w3schools.com/sql/sql_injection.asp)

## How to penetrate test for this vulnerability

1. In any form, try known SQL injections.

    - `105 OR 1=1`
    - `" OR ""="`
    - `105; DROP TABLE users`

```SQL
--You need to force:
SELECT * FROM users WHERE username = '{user entered username}' AND password = '{user entered password}';
--To always evaluate as True:
SELECT * FROM users WHERE username = '105' OR 1=1 AND password = '105' OR 1=1;
```

2. Runtime errors are a sign that the vulnerability can be exploited.
3. You may need to try different combinations of `'` and `"` within the SQL injection to ensure the backend SQL query constructs are syntactically correct.

## How to countermeasure this vulnerability

- Regular [code reviews](../security_testing_approaches/README.md#Code_review)
- Avoid languages like PHP
- Implement an [API](..\flask_safe_API\README.md) with built-in security as the interface to the SQL database
- Implement [Defensive data handling](../defensive_data_handling/README.md).
- Require authentication before accepting any form of input
- Never construct queries with concatenating and binary comparison, i.e. `cur.execute(f"SELECT * FROM users WHERE username == '{username}' AND password == '{password}'")`.
- Use query parameters, i.e. `cur.execute('SELECT * FROM users WHERE username == ? AND password == ?', (username, password))`.
- Salt database table names with a 5-character random string
