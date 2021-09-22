1. Enumeration
  nmap port scan
  Common ports
  FTP
    Anonymous Login?
    Common Credentials? admin/admin
    
    
   smbclient get all files:
   recurse (toggles recursive mode)
   prompt (toggles Y/N requests)
   mget *
  
## Command Line 
### Linux  
Viewing formatted text files  
`less -R <file>`  

### Windows  
"Grep" function in Windows  
`findstr /I "<string>"` 

Query LDAP for users
`ldapsearch -H ldap://[IP]:[Port] -x -LLL -s sub -b "dc=<dcname>,dc=<dcname>"`

Downloading from Windows Command line  
`certutil.exe -urlcache -f http://target/remotefile localfile`

### Notes  

- when generating a shell on windows, use windows/shell_reverse_tcp
