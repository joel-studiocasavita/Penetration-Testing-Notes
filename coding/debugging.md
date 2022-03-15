## Database

### mysql
```
sudo nano /etc/mysql/my.cnf

[mysqld]
...
general_log_file        = /var/log/mysql/mysql.log
general_log             = 1
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

