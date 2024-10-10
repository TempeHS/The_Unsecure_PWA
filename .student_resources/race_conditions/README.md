# Race Conditions

A race condition occurs when two or more threads can access shared data and try to change it at the same time. Because the thread scheduling algorithm can swap between threads at any time, you need to consider the order in which the threads will attempt to access the shared data. Therefore, the result of the change in data is dependent on the thread scheduling algorithm, i.e. both threads are "racing" to access/change the data.

This exploit is very common in a 'Shopping cart theft' exploit because of inadequate session management. The threat actor will send quick succession POST requests with a discount voucher. If session management has not been properly designed, the voucher can be applied to the shopping cart multiple times, and goods can be purchased with unintended discounts.

Consider the following algorithm run in parallel threads for a shopping cart discount voucher system:
| Processor | Thread 1 | Thread 2 |
| ------ | ------ | ------ | 
| 01 | `BEGIN apply_voucher(v, cart)` | |
| 02 | | `BEGIN apply_voucher(v)`|
| 03 |  &nbsp;&nbsp;&nbsp;&nbsp;`IF GET voucher_applied()` = TRUE | |
| 04 |  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`return` | |
| 05 |  &nbsp;&nbsp;&nbsp;&nbsp;`ENDIF` | |
| 06 |  | &nbsp;&nbsp;&nbsp;&nbsp;`IF GET voucher_applied()` = TRUE |
| 07 |  | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`return` |
| 08 |  | &nbsp;&nbsp;&nbsp;&nbsp;`ENDIF` |
| 09 |  &nbsp;&nbsp;&nbsp;&nbsp;`apply_disc(calc_disc(v), cart)` |
| 10 | &nbsp;&nbsp;&nbsp;&nbsp;`SET voucher_applied(True)` | |
| 11 | |  &nbsp;&nbsp;&nbsp;&nbsp;`apply_disc(calc_disc(v), cart)` |
| 12 | | &nbsp;&nbsp;&nbsp;&nbsp;`SET voucher_applied(True)` |
| 13 | &nbsp;&nbsp;&nbsp;&nbsp;`render_front_end()` | |
| 14 | `END apply_voucher` | |
| 15 | | &nbsp;&nbsp;&nbsp;&nbsp;`render_front_end()` | 
| 16 | | `END apply_voucher`  |

In this example, the vulnerability is easily exploited because of the processing time between the GET (or check) and the SET, which allows the discount to be applied multiple times.

## How to secure against this attack
1. Consider multithreading in any shared resources (discounts, logins, session ID creation, etc), implement a lock by 'session ID' algorithm, and minimise processing time between the SET and the GET (or check) of the lock.
2. Implement unique 'session IDs' which can not be brute forced or calculated
3. Use the 'session ID' in all processes and explicitly return to the specified 'session ID'
4. Use asynchronous encryption for all form inputs. For example, use [CSRF Protect](https://flask-wtf.readthedocs.io/en/0.15.x/csrf/).

```pseudocode
    BEGIN apply_voucher(v_id, cart, sessionID)
        WHILE GET voucher_process_lock(sessionID) is TRUE
            do nothing
        ENDWHILE
        SET voucher_lock(sessionID,TRUE)
        GET voucher_applied()
        apply_disc(calc_disc(v_id), cart)
        SET disc_applied(True)
        SET voucher_process_lock(sessionID, FALSE)
        return render_front_end(sessionID)
    END apply_voucher
```


