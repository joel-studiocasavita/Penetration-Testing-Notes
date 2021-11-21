
## Installing and Configuring the Access Point

### VM Configuration (If applicable)

Set the Network Adapter for the guest OS to `Bridged (Autodetect)`.  

gw 192.168.4.1


```
sudo apt update && sudo apt install isc-dhcp-server


```
# /etc/dhcp/dhcpd.conf                          

subnet 192.168.160.0 netmask 255.255.255.0 {
    default-lease-time 600;
    max-lease-time 7200;
    option domain-name "wifi";
    option domain-name-servers 192.168.160.2;
    range 192.168.160.10 192.168.160.250;
    option subnet-mask 255.255.255.0;
    option broadcast-address 192.168.160.255;
    option routers 192.168.160.1;
}

```

```
$ sudo airmon-ng

PHY     Interface       Driver          Chipset

phy0    wlan0           rt2800usb       Ralink Technology, Corp. RT5572
```

```
$ sudo airmon-ng start wlan0

Found 2 processes that could cause trouble.
Kill them using 'airmon-ng check kill' before putting
the card in monitor mode, they will interfere by changing channels
and sometimes putting the interface back in managed mode

    PID Name
    496 NetworkManager
   2084 wpa_supplicant

PHY     Interface       Driver          Chipset

phy0    wlan0           rt2800usb       Ralink Technology, Corp. RT5572
                (mac80211 monitor mode vif enabled for [phy0]wlan0 on [phy0]wlan0mon)
                (mac80211 station mode vif disabled for [phy0]wlan0)

$ sudo airbase-ng -c 11 -e freewifi wlan0mon                           1 ⨯
11:17:25  Created tap interface at0
11:17:25  Trying to set MTU on at0 to 1500
11:17:25  Trying to set MTU on wlan0mon to 1800
11:17:26  Access Point with BSSID DC:4E:F4:06:DA:53 started.
```

```
# rename monitoring interface accordingly
sudo ifconfig at0 192.168.160.1 netmask 255.255.255.0
sudo ifconfig at0 mtu 1400
sudo route add -net 192.168.160.0 netmask 255.255.255.0 gw 192.168.160.1
sudo echo 1 > /proc/sys/net/ipv4/ip_forward  #may need to be root.  Sudo didn't work
sudo iptables -t nat -A PREROUTING -p udp -j DNAT --to 192.168.160.1
sudo iptables -P FORWARD ACCEPT
sudo iptables --append FORWARD --in-interface wlan0mon -j ACCEPT
sudo iptables --table nat --append POSTROUTING --out-interface eth0 -j MASQUERADE
sudo iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000
```

```
sudo touch /var/lib/dhcp/dhcpd.leases
sudo dhcpd -cf /etc/dhcp/dhcpd.conf -pf /var/run/dhcpd.pid at0


