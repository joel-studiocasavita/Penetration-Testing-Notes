## TCP 1433 mssql  

### MSSQL Commands
```
# Get the db version information
SELECT @@VERSION; 

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
