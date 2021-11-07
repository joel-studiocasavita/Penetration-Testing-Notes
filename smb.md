# TCP 445  

## Linux

*smbv1 is sometimes disabled by default.  To enable:
```
nano /etc/smbd/smb.conf  
#under the "[global]" section add:
client min protocol = NT1
```

To view shares:  
`$ smbclient -L <HOST>`  

To connect to a share
`$ smbclient \\\\remotehost\\share -U <user>`

### smbclient commands

```
PROMPT OFF = Removes "are you sure" messages
RECURSE ON = Wildcards includes subfolders
mget = download multiple files

```
### Enum4Linux  
Enumerates system information from smb port.  

`enumb4linux <ip/host>`  

### smbmap
Enumerates smb shares  

```
# lists all files under share\folder
smbmap -H <smb IP address>  -u <username> -p <password> -r <share\directory>

#
```
