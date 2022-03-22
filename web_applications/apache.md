## Possible Apache Config File locations

```
/etc/httpd/httpd.conf
/etc/httpd/conf/httpd.conf
/etc/apache2/apache2.conf
/etc/apache2/httpd.conf
/usr/local/apache2/apache2.conf
/usr/local/apache/conf/httpd.conf
/usr/local/etc/httpd/httpd.conf
/opt/apache2/apache2.conf
```


## Possible Webdav password location
```
<serverroot>/webdav/passwd.dav
/etc/apache2/passwd.dav
```

## Uploading files to webdav
```
$ cadaver http://hostname[:port]/path
put <file>
```
