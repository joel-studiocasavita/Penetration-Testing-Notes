# misc | to be organized


### Timestamping web requests/posts
This is useful when trying to generate password reset tokens that are based on time values.
```
date +%s%3N && curl -s -i -X 'POST' --data-binary 'id=guest' 'http://server/RequestPasswordReset.jsp' && date +%s%3N 1582038122371 
```
Use sites such as www.EpochConverter.com to convert time stamps from burp   
The date header does not provide the millisecond presicion as that value is always set to 000

`time.time()` gives millisecond time for in python 
