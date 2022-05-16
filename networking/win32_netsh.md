`netsh` is a built in Windows command line executable for interacting with the operating system network services.  

**Port Forwarding**

```
# setting up a local port forward to a remote address
netsh interface portproxy add v4tov4 listenaddress=0.0.0.0 listenport=<PORT> connectaddress=<REMOTE IP> connectport=<REMOTE PORT>

# Viewing existing port forwards
netsh interface portproxy show all

# Removing all existing tcp port forwards
netsh interface portproxy reset
