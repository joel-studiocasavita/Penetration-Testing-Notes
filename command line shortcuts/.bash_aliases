#start services
alias webserver='sudo python3 -m http.server 80'
alias smbserver='sudo smbserver.py files .'

#netcat listerners for multiple ports
alias nc_21='sudo nc -lvp 21'
alias nc_22='sudo nc -lvp 22'
alias nc_80='sudo nc -lvp 80'
alias nc_443='sudo nc -lvp 443'
alias nc_445='sudo nc -lvp 445'
alias nc_4444='nc -lvp 4444'
alias nc_8000='nc -lvp 8000'
alias nc_8080='nc -lpv 8080'

#upgrading reverse shells
alias upgradeshell='stty raw -echo ; fg'
