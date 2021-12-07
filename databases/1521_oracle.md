## TCP 1521 oracle

### Oracle Commands
```
# Get the db version information
SELECT banner FROM v$version
SELECT version FROM v$instance

# Comment
--comment

# Enumerating db contents
# Listing the tables
SELECT * FROM all_tables
or
SELECT TABLE_NAME FROM all_tables

# Listing columns
SELECT * FROM all_tab_columns WHERE table_name = 'TABLE_NAME'
or
SELECT column_name FROM all_tab_columns WHERE table_name = 'TABLE_NAME'
```
