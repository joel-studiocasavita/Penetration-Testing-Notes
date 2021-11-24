# TCP 143 imapd  

### Connecting to imapd  
`nc -nv <ip> 143`  

### Authentication

#### Plain login 
`login <username@server> <password>`  

#### SASL Login
`authenticate login`  
Prompts will be base64 encoded.  The username and passwords must be base64 encoded and entered separately.  

#### SASL Plain Login  

First base64 encode the username and password together.
```
echo -en "\0someuser@example.atmailcloud.com\0My_P@ssword1" | openssl base64
AHNvbWV1c2VyQGV4YW1wbGUuYXRtYWlsY2xvdWQuY29tAE15X1BAc3N3b3JkMQ==
```
in imapd  
`authenticate plain` 

### Retrieving email  
```
namespace                               - lists the mailboxes available
list "<mailbox>" "*"                    - list all folders in a mailbox
select "<folder>"                       - selects a folder  
fetch <message number> RFC822           - displays a message  
store <message number> (\Deleted)       - moves a message to the \Deleted folder
expunge                                 - permanently deletes messages (in Deleted folder)
```

