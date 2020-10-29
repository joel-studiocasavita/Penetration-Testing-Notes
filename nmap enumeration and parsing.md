#Nmap Commands#

##Nmap Operating System ID##

```nmap -O -oG <output file>

cat <output file> | while read line; do echo $line | awk -F ' ' '{ for (i=1;i<=NF;i++) if ($i == "OS:") { printf "%s %s ", $1,$2; j=i; while ($j!="Seq") {printf $j" "; j++} printf "\n"}}';done
```

