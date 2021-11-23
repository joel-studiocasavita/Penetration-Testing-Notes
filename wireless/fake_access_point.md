
## Installing and Configuring the Access Point

### VM Configuration (If applicable)

Set the Network Adapter for the guest OS to `Bridged (Autodetect)`.  

```
sudo apt update && sudo apt install -y hostapd dnsmasq wireless-tools iw wvdial

```
## /etc/hostapd/hosapd.conf                          
*Change the wireless interface name accordingly*
```
# cat /etc/hostapd/hostapd.conf 
interface=wlan0
driver=nl80211
ssid=FreeWifi
channel=1
# Yes, we support the Karma attack.
#enable_karma=1
```

## /etc/dnsmasq.conf
*Change the wireless interface name accordingly*
```
cat /etc/dnsmasq.conf      
log-facility=/var/log/dnsmasq.log
interface=wlan0
dhcp-range=10.0.0.10,10.0.0.250,12h
dhcp-option=3,10.0.0.1
dhcp-option=6,10.0.0.1
#no-resolv
log-queries
```

## Interface IP commands
*Change the wireless interface name accordingly*
```
sudo ifconfig wlan0 10.0.0.1 netmask 255.255.255.0
sudo ifconfig wlan0 mtu 1400
sudo route add -net 10.0.0.0 netmask 255.255.255.0 gw 10.0.0.1
```

## IPtable Rules
*Change the interface names accordingly*  
*wlan0 = AP / eth0 = internet*

```
sudo iptables --flush
sudo echo 1 > /proc/sys/net/ipv4/ip_forward
sudo iptables -A FORWARD -i wlan0 -o eth0 -j ACCEPT
sudo iptables -A FORWARD -i eth0 -o wlan0 -m state --state ESTABLISHED,RELATED -j ACCEPT
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
```

## Disable Network Manager
```
sudo systemctl stop NetworkManager.service
```

## Start the Services
```
sudo /etc/init.d/hostapd start
sudo /etc/init.d/dnsmasq start
```
