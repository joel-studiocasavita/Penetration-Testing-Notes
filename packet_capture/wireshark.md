### Finding passwords in PCAP with Wireshark
Set the filter to `http.request.method==POST` and then 'Follow the TCP Stream'

OR

Tools --> Credentials  


### Finding hostname in TLS packets using Wireshark

1. Set a display filter
```
ssl.handshake.extension.type==0
```

2. Select a `CLIENT HELLO` packet and select the `Server Name` field.
```
Transport Layer Security
   Handshake Protocol: Client Hello
      Extension: server_name
         Server Name Indication extension
            Server Name:
```
3. Right click on the `Server Name` field and select `Apply as a column`.


### Simple filters
Just type these into the display filter field to display only those type of packets.

```
dns
http
```
