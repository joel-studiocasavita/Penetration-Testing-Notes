# misc | to be organized


### Timestamping web requests/posts
This is useful when trying to generate password reset tokens that are based on time values.
```
date +%s%3N && curl -s -i -X 'POST' --data-binary 'id=guest' 'http://server/RequestPasswordReset.jsp' && date +%s%3N 1582038122371 
```
Use sites such as www.EpochConverter.com to convert time stamps from burp   
The date header does not provide the millisecond presicion as that value is always set to 000

`time.time()` gives millisecond time for in python 

### Sending sequential web requests
```
import requests,sys 
if len(sys.argv) != 2: 
 print "(+) usage: %s <target>" % sys.argv[0] 
 sys.exit(-1) 

target = "http://%s:8080/batch" % sys.argv[1] 
request_1 = '{"method":"get","path":"/profile"}' 
request_2 = '{"method":"get","path":"/item"}' 
request_3 = '{"method":"get","path":"/item/$1.id"}' 

json = '{"requests":[%s,%s,%s]}' % (request_1, request_2, request_3) 
r = requests.post(target, json) 

print r.text 

```
