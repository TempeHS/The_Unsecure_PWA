# Race Conditions

A race condition occurs when two or more threads can access shared data and they try to change it at the same time. Because the thread scheduling algorithm can swap between threads at any time, you don't know the order in which the threads will attempt to access the shared data. Therefore, the result of the change in data is dependent on the thread scheduling algorithm, i.e. both threads are "racing" to access/change the data.

This exploit is very common in a 'Shopping cart theft' exploit because of inadequate session management. Were the threat actor will send quick sucession post resquests with a discount voucher. If session management has not been properly design the vouch can be applied multiple times.

Consider the following algorythm run in parrallel for a shopping cart discount voucher system:
| Order | Process 1 | Process 2 |
| ------ | ------ | ------ | 
| 01 | `BEGIN apply_voucher(v, cart)` | |
| 02 | | `BEGIN apply_voucher(v)`|
| 03 |  &nbsp;&nbsp;&nbsp;&nbsp;`GET voucher_applied()` | |
| 04 | | &nbsp;&nbsp;&nbsp;&nbsp;`GET voucher_applied()`
| 05 |  &nbsp;&nbsp;&nbsp;&nbsp;`apply_disc(calc_disc(v), cart)` |
| 06 | &nbsp;&nbsp;&nbsp;&nbsp;`SET disc_applied(True)` | |
| 07 | |  &nbsp;&nbsp;&nbsp;&nbsp;`apply_disc(calc_disc(v), cart)` |
| 08 | | &nbsp;&nbsp;&nbsp;&nbsp;`SET disc_applied(True)` |
| 09 | &nbsp;&nbsp;&nbsp;&nbsp;`render_front_end()` | |
| 10 | `END apply_voucher` | |
| 11 | | &nbsp;&nbsp;&nbsp;&nbsp;`render_front_end()` | 
| 12 | | `END apply_voucher`  |

In this example the vulnerability is easily exploited because of the processing time between the check and the set. Allowing the discount to be applied multiple times.

## How to secure against this attack
1. Consider multithreading in any shared resources (discounts, logins, sessions) and implement a lock by session id alogorithm and minimise processing time between the SET and the GET (or check) of the lock.
2. Ensure sesison ID's can not be brute forced or calc|ulated


```psuedocode
    BEGIN apply_voucher(v_id, cart, sessionID)
        WHILE GET voucher_lock(sessionID) is TRUE
            do nothing
        ENDWHILE
        SET voucher_lock(sessionID,TRUE)
        GET voucher_applied()
        apply_disc(calc_disc(v_id), cart_items)
        SET disc_applied(True)
        render_front_end()
        SET voucher_lock(sessionID, FALSE)
    END apply_voucher
```


