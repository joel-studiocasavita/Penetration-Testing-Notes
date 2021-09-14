# Windows Services  

## powershell
```
get-process
```
## WMIC

### Default Process List
```
wmic process list
```
### Executable Command
```
wmic process get ProcessID,Name,CommandLine
```
## Tasklist Command

### List services and users
```
tasklist /v
```

processes are running as "SYSTEM"  
`tasklist /v /fi "username eq system"`  
