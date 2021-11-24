## TCP 389 LDAP

### Query LDAP for users
`ldapsearch -H ldap://[IP]:[Port] -x -LLL -s sub -b "dc=<dcname>,dc=<dcname>"`
