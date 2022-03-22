
## Common code vulnerabilities

### PHP
**publicly available routes/pages**

```
grep -rnw <webpath> -e "^.*user_location.*public.*" --color
```  
<br>  

**The Eval() function**  
The `eval()` function in php will parse the string supplied to it into PHP code.  Great for RCE  

**PHP Filters**
| Filter | Description | Example |
|--|--|--|  
|expect|Executes system commands, but is not enabled by default| `expect://ls`|  
|input|Send Payload through POST method on PHP | `php://input` |
|filter|Wrapper filter useful in bypassing attack signatures. Use this to retrieve php file using a vulnerable php page | without encoding:<br>`php://filter/resource=page.txt`<br>with encoding<br>`php://filter/convert.base64-encode/resource=<file>`<br>`http://example.com/index.php?page=php://filter/convert.base64-encode/resource=/var/www/html/db.php` | 
|data|Inject php code directly into a url||

### Java  
```
doGet  
doPost  
doPut  
doDelete  
doCopy  
doOptions  

grep -rnwi <path> -e doGet -e doPost -e doPut -d doDelete -e doCopy -e doOptions
```
<br>

### SQL Queries 
```
grep -rnw <webpath> -e "^.*?query.*?select.*?" --color
```
<br>  

**Authentication Methods**  

<br>  

**Input validation**  
