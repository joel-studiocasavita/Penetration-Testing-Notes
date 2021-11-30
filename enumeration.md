## Port Scanning  

### Nmap

Simples Full tcp port scan with output file
`# nmap -A -p- -oA <filename> <target>`

Full tcp port scan with service and Operating System identification  
`nmap -sS -sV -Pn -p- -oG <OUTPUT FILE> <IP | NETWORK> -vv`

Using a target file  
`nmap -sS -sV -Pn -p- -oG <OUTPUT FILE> -iF <TARGET FILE>` 

Output hosts and ports to csv file  
``` 
echo "host,status,protocol,port,service,version";  
egrep -v "^#|Status: Up" ./targets_ports.nmap | cut -d' ' -f2,4- | \  
sed -n -e 's/Ignored.*//p'  | \  
awk '{for(i=2; i<=NF; i++) {a=a" "$i}; split(a,s,","); for(e in s) { split(s[e],v,"/");printf "%s,%s,%s,%s,%s,%s%s\n" , $1,v[2], v[3], v[1], v[5],v[6],v[7]}; a="" }'  
```

Nmap Operating System ID  
`nmap -O -oG <OUTPUTFILE>`      
```
cat <NMAPRESULTS> | while read line; do echo $line | awk -F ' ' '{ for (i=1;i<=NF;i++) if ($i == "OS:") { printf "%s %s ", $1,$2; j=i; while ($j!="Seq") {printf $j" "; j++} printf "\n"}}';done  
```

Find nmap xml files with online hosts
```for i in $(find . -name *.xml); do grep -il "1 host up" $i | cut -d '/' -f 2 >> live.txt; done```

## DNS Enumeration (passive)

#### Find subdomains  
```
sudo apt install subfinder  
subfinder -d <domain>
```
#### Resolve DNS (passive)
```
nmap -sL -iL <target list> -oG <filename> -vvv
```

## Website enumeration

### whatweb
Queries the webserver to identify webapps running on the server. 
```
whatweb <url>
```

### dirb  
```
$ dirb <url> <wordlist> -o <outputfile>
``` 

### gobuster  
```
$ gobuster dir --url <url> -w <wordlist> -o <outputfile>
```
### wfuzz
```
wfuzz -w <wordlist> --hc 404 <url>/FUZZ
```
### dirbuster (Java Gui)  
```
$ dirbuster
```  

### nmap  
```
$ nmap <targetIP> -p <port> --script=http-enum -oN <outputfile>
```  
