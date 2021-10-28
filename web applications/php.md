## The Eval() function
The `eval()` function in php will parse the string supplied to it into PHP code.  Great for RCE  

## PHP Filters
| Filter | Description | Example |
|--|--|--|  
|expect|Executes system commands, but is not enabled by default| `expect://ls`|  
|input|Send Payload through POST method on PHP | `php://input` |
|filter|Wrapper filter useful in bypassing attack signatures. Use this to retrieve php file using a vulnerable php page | without encoding:<br>`php://filter/resource=page.txt`<br>with encoding<br>`php://filter/convert.base64-encode/resource=<file>`<br>`http://example.com/index.php?page=php://filter/convert.base64-encode/resource=/var/www/html/db.php` | 
|data|Inject php code directly into a url||

