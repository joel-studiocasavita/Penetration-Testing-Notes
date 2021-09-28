
## Windows Services

#### listing Services
All Services  
```
sc query
```
A specific service  
```
sc qc <servicename>
```
## Processes
#### Listing processes with all info
```
tasklist /v
```
#### Killing a process
```
taskkill /PID <pid#>
```
For multiple PIDS, just add additional /PIDs  

### unzip an archive
```
#powershell
PS C:\> expand-archive <archivename>
```
