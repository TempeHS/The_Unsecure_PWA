# Race Conditions

A race condition occurs when two or more threads can access shared data and try to change it at the same time. Because the thread scheduling algorithm can swap between threads at any time, you need to consider the order in which the threads will attempt to access the shared data. Therefore, the result of the change in data is dependent on the thread scheduling algorithm, i.e. both threads are "racing" to access/change the data.

## Vulnerability example - shopping cart theft

Exploiting race conditions for 'Shopping cart theft' is common when inadequate session management has been implemented. The threat actor will send quick succession POST requests with a discount voucher. Because the session management has been poorly designed, the voucher can be applied to the shopping cart multiple times, and goods can be purchased with unintended discounts.

Consider the following algorithm run in parallel threads for a shopping cart discount voucher system:

| Processor | Thread 1 | Thread 2 |
| ------ | ------ | ------ |
| 01 | `BEGIN apply_voucher(v, cart)` | |
| 02 | | `BEGIN apply_voucher(v, cart)`|
| 03 |  `IF GET voucher_applied() = TRUE` | |
| 04 |  `RETURN` | |
| 05 |  `ENDIF` | |
| 06 |  | `IF GET voucher_applied() = TRUE` |
| 07 |  | `RETURN` |
| 08 |  | `ENDIF` |
| 09 | `apply_disc(calc_disc(v), cart)` | |
| 10 | `SET voucher_applied(TRUE)` | |
| 11 | | `apply_disc(calc_disc(v), cart)` |
| 12 | | `SET voucher_applied(TRUE)` |
| 13 | `RETURN render_front_end()` | |
| 14 | `END apply_voucher` | |
| 15 | | `RETURN render_front_end()` |
| 16 | | `END apply_voucher`  |

In this example, the vulnerability is easily exploited because of the processing time between the GET (or check) and the SET, which allows the discount to be applied multiple times.

### Race conditions managed

```pseudocode
    BEGIN apply_voucher(v_id, cart, sessionID)
        WHILE GET voucher_process_lock(sessionID) is TRUE
            do nothing
        ENDWHILE
        SET voucher_lock(sessionID, TRUE)
        GET voucher_applied()
        apply_disc(calc_disc(v_id), cart)
        SET disc_applied(True)
        SET voucher_process_lock(sessionID, FALSE)
        return render_front_end(sessionID)
    END apply_voucher
```

## Vulnerability example - timing attack

The below example will help you understand how a threat actor can exploit a complex side channel attack vector involving both race conditions and broken authentication/session management vulnerabilities. Unmanaged race conditions and poor session management allow the successful return token for a public user to be confused with the unsuccessful return token for an administrator user, granting the threat actor authentication with escalated user authorisation.

1. Perform a [reverse DNS search](https://viewdns.info/reverseip) and place the infrastructure under load through a DoS attack, such as a script that sends repeated GET requests at short intervals (usually run from multiple clients simultaneously) for all sites hosted on the webserver. 

```html
<iframe src="http://127.0.0.1:5000" id="myFrame"></iframe>
<script>
function myFunction() {
  document.getElementById('myFrame').contentWindow.location.reload();
  setTimeout(myFunction, 1); //1 = 1 millisecond
}
myFunction();
</script>
```

2. Run a script that calls a condition at timed intervals which are adjusted to phish for the correct timing of the exploit.

```html
<form id="hack" target="csrf-frame" action="http://localhost:5000/" method="POST" autocomplete="off">
    <input name="username" value="administrator">
    <input name="password" value="???">
</form>
<form id="hack2" target="csrf-frame" action="http://localhost:5000/" method="POST" autocomplete="off">
    <input name="username" value="joe.normal">
    <input name="password" value="password123">
</form>
<script>
function submitHack() {
    document.getElementById("hack").submit();
    setTimeout(submitHack, 100); //Hack is submitted every 0.1 seconds
}
function timeHack2() {
    let time = Math.floor(Math.random() * 100);
    setTimeout(submitHack2, time); //Hack is submitted randomly every 0 to 0.1 seconds 
    setTimeout(timeHack, time+1); // reschedule hack attempt
}
function submitHack2() {
    document.getElementById("hack2").submit();
}
submitHack();
timeHack2();
</script>
```

## How to penetrate test for a Race Conditions vulnerability

Race conditions are very hard to penetrate manually. Usually, a software engineer will use a pen-testing application designed to send repeat requests strategically timed apart.

## How to secure against this attack

1. Consider multithreading in any shared resource process, including (discounts, login processes, session ID creation, etc).
2. Implement a lock using the 'session ID' as a key in the algorithm, and most importantly, minimise the processing time between the lock's GET (or check) and SET.
3. Implement unique 'session IDs' which can not be brute forced or calculated. For example install and configure [Flask Session](https://flask-session.readthedocs.io/en/latest/)
4. Encrypt all form inputs asynchronously. For example, use [CSRF Protect](https://flask-wtf.readthedocs.io/en/0.15.x/csrf/).
5. Implement rate limiting so a session can only make 1 request per 5 seconds. For example, install and configure [Flask Limiter](https://flask-limiter.readthedocs.io/en/stable/)
