## Enabling Database Logs

### mysql
```
sudo nano /etc/mysql/my.cnf

[mysqld]
...
general_log_file        = /var/log/mysql/mysql.log
general_log             = 1
```
### postgresql
```
sudo nano postgresql.conf

log_statement = 'all'

```
## PHP 
```
sudo nano /etc/php5/apache2.php.ini

display_errors = On
```

## Linux 

### strace
monitors system calls and signals 
```
strace <binary file>
```

### ltrace
Monitors calls to library functions
```
ltrace <binary file
```

## Monitoring the Log files
```
# tail a log file periodically and highlight the line containing the keyword in red. 
tail -f <log file> | sed -r "s/(.*keyword.*)/`printf "\033[31m"`\1`printf "\033[0m"`/g"
```
### ANSI Color Codes. 
Black: \u001b[30m  
Red: \u001b[31m  
Green: \u001b[32m  
Yellow: \u001b[33m  
Blue: \u001b[34m  
Magenta: \u001b[35m  
Cyan: \u001b[36m  
White: \u001b[37m  
Reset: \u001b[0m  

### Sample Logs to Monitor
```
#webserver
/var/log/apache2/access.log
/var/log/apache2/error.log

#database
/var/log/mysql.log
/var/log/mysql.err
/var/log/mysql/mysql.log
/var/log/mysql/mysql.err

#any application specific logs
```
