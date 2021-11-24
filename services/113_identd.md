## TCP 113 identd

Identifies the user of a tcp service.  

```
nc -vn <ip> 113
<remote port>,<local port>
```
nmap will automatically perform identd enumeration, if the service is available, when using the `-sC` or `-A` scanning switches.  
