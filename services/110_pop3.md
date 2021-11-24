## POP3

### Connecting to pop3
```
nc -v <ip address> 110
or
telnet <ip address> 110
```

### Logging into POP3
```
USER <username>
PASS <password>
```
### POP3 Commands
```
DELE <message number>                 - delete a particular message  
LIST                                  - lists mailbox messages
QUIT                                  - ends the pop3 session
RETR <message number>                 - retrieve and display a particular message
RSET                                  - resets the session reverting all changes
STAT                                  - displays the number of mailbox messages
TOP <message numer> <number of lines> - retrieve and display the start of a message

```
