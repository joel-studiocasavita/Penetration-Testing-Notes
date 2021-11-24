## TCP 22 ssh

## Creating SSH Keys

```
$ ssh-keygen
cp id_rsa.pub authorized_keys
chmod 644 ./authorized_keys
```
Then copy the authorized keys to the remote machine under the appropriate profile   
```
/home/user/.ssh/authorized_keys
```

## Connecting to a remote system using SSH keys
```
$ ssh <user>@<remotehost> -i <path to private key>
```

## Tunneling 
### Port Forwarding
```
ssh <user>@<remotehost> -L <localport>:<target IP address><target port>
```
additional port forwards can be added using additional -L switches  
  
### Reverse Port Forwarding  
```
ssh <user>@<remotehost> -R <Remoteport>:<local IP address><local port>
```
