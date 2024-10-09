# SQL Injection

A SQL injection attack consists of inserting or " injecting " a SQL query via the input data from the client to the application. A successful SQL injection exploit can read sensitive data from the database and modify database data (Insert/Update/Delete). SQL injection attacks are a type of injection attack in which SQL commands are injected into data-plane input to affect the execution of predefined SQL commands.

# Examples of SQL injections
[W3Schools has a range of SQL Injection examples](https://www.w3schools.com/sql/sql_injection.asp)

## How to secure against this attack

- Code review
- Avoid languages like PHP
- Use API with built-in security as the interface to the SQL database
- Defensive data handling
- Require authentication before accepting any text form data
- Never construct queries with concatenating and binary comparison
- Use query parameters ie `cur.execute('SELECT * FROM users WHERE username == ? AND password == ?', (username, password))`.
- Salt database table names with 5-character random string
