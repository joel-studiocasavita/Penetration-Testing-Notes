
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

## Windows Patches
#### List Windows Patches  
```
wmic qfe list
```
## Other
#### unzip an archive
```
#powershell
PS C:\> expand-archive <archivename>
```
Shutdown and Reboot
#### Reboot
```
shutdown /r
```
#### Shutdown
```
shutdown /s
```
Default time-out period to execute the command is 30 seconds.  A `/t <0-600>` can be added to the command line to shorten or extend the time-out.  

#### Abort Shutdown
May only be used during time-out period
```
shutdown /a
```
