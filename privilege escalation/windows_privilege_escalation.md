
## Unquoted Service Paths
```
 wmic service get name,pathname,displayname,startmode | findstr /i auto | findstr /i /v "C:\Windows\\" | findstr /i /v """
 ```
 
## Missing Windows Patches  
```
wmic qfe list
```
