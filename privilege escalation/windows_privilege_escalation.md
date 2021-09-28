[Unquoted Service Paths](#unquoted-service-paths)  
[Missing Windows Patches](#missing-windows-patches)  



## Unquoted Service Paths
```
 wmic service get name,pathname,displayname,startmode | findstr /i auto | findstr /i /v "C:\Windows\\" | findstr /i /v """
 ```
##### Example
C:\Program Files\A Subfolder\B Subfolder\C Subfolder\SomeExecutable.exe  
In order to run SomeExecutable.exe, the system will interpret this path as follows:  
1. C:\Program.exe
2. C:\Program Files\A.exe
3. C:\Program Files\A Subfolder\B.exe
4. C:\Program Files\A Subfolder\B Subfolder\C.exe
5. C:\Program Files\A Subfolder\B Subfolder\C Subfolder\SomeExecutable.exe  

If C:\Program.exe is not found, then C:\Program Files\A.exe would be executed. If C:\Program Files\A.exe is not found, then C:\Program Files\A Subfolder\B.exe would be executed and so on.  

*source: https://medium.com/@SumitVerma101/windows-privilege-escalation-part-1-unquoted-service-path-c7a011a8d8ae
 
 
## Missing Windows Patches  
```
wmic qfe list
```

## Enabled Always Elevate in the Registry

