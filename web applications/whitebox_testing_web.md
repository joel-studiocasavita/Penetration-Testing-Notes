
### Starting Points

**publicly available routes/pages**

```
grep -rnw <webpath> -e "^.*user_location.*public.*" --color
```  
<br>  

**java search terms**  
doGet  
doPost  
doPut  
doDelete  
doCopy  
doOptions  

```
grep -rnwi <path> -e doGet -e doPost -e doPut -d doDelete -e doCopy -e doOptions
```
<br>

**SQL Queries**  
```
grep -rnw <webpath> -e "^.*?query.*?select.*?" --color
```
<br>  

**Authentication Methods**  

<br>  

**Input validation**  
