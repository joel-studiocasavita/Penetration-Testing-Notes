### Changing default Python interpreter to version 3 on Linux
```
update-alternatives --install /usr/bin/python python /usr/bin/python3 1
```


### Basic Python Starter Code
```
#!/bin/python
# program description

# imports here

def function_1(s): #function
    print(s)
    return  

if __name__=="__main__":
    words = "Hello world!"
    function_1(words)
    exit()
```


### Reading and interating through a file
```
f = open(file,"r")
lines = f.readlines()

for line in lines:
  print(line)
```


### Basic http GET request
```
import requests

url = 'URL'
r = requests.get(url)
response_code = r.status_code
headers = r.headers
response = r.text
print(response)
```


### Basic http POST request
```
import requests

url = 'URL'
parameters = {'username':'admin', 'password':'password123'}
r = requests.post(url,params=parameters)
response = r.text
print(response)
```


### Downloading a file
```
import requests

url = 'URL/file.txt'
save_file_name = r'c\some\path\filename'
r = requests.get(url)
with open(save_file_name,'wb') as f:
    f.write(r.content)
```

