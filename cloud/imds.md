## Instance Metadata (IMDS)

Requests can be made from the locahost to `169.254.169.254` to retrieve metadata for the instance of the host.  
IMDSv1 does not support authentication.
IMDSv2 Supports authentication.  
It is possible to have both versions enabled simulatanously for a host.
```
http://169.254.169.254/latest/meta-data/
http://[fd00:ec2::264]/latest/meta-data/

$ curl http://169.254.169.254/latest/meta-data/
```

By browsing through the "directory" structure returned through the webrequest, it may be possible to find sensitive data, such as keys.  
```
$ curl http://169.254.169.254/latest/meta-data/public-keys/0/
openssh-key
```
