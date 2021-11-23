## tcpdump  

### Capture specific ports

`# tcpdump -i eth0 '<port #>'`

### Windows  

To start the capture  

`netsh trace start capture=yes`

To specify an IP address  
`netsh trace start capture=yes IPv4.Address=x.x.x.x`
To end the capture  
`netsh trace stop`

By default, capture file is located in `%USERPROFILE%\Appdata\Local\Temp\NetTraces\NetTrace.etl`

The file needs to be converted to PCAP in order to view with WireShark:  
https://github.com/microsoft/etl2pcapng
     
