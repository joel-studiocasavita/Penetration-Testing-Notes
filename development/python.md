## Configuring python virtual environment
```
# install virtual environment
sudo apt install virtualenv

## starting environment

# for python 3
virtualenv -p /path/to/python3/bin <path to new environment>

# for python 2
virtualenv -p /path/to/python2/bin <path to new environment>

source <path to new environment>/bin/activate

## exit environment
deactivate
```

## Installing Pip for Python 2
```
sudo apt update
curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py
sudo python2 get-pip.py
```

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
    
def main():
    words = "Hello world!"
    function_1(words)
    exit()

if __name__=="__main__":
    main()
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
# Disable the self-signed certificate warnings
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


url = 'URL'
proxies = {'http':'http://127.0.0.1:8080','https':https://127.0.0.1:8080'}

headers = {}
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
headers["Content-Type"] = "application/x-www-form-urlencoded"

r = requests.get(url,header=headers,proxies=proxies,verify=False)
# verify=False disables the self-signed certificate verification
response_code = r.status_code
headers = r.headers
response = r.text
json_response = r.json()
print(response)
```


### Basic http POST request
```
import requests

url = 'URL'
headers = {"Header_1":"Header_1_value","Header_2":"Header_2
data = {'username':'admin', 'password':'password123'}
r = requests.post(url,params=data,header=headers,verify=False)
response = r.text
print(response)
```
### Session Based http request
```
import requests
# Disable the self-signed certificate warnings
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

s = requests.Session()

url = 'URL'
proxies = {'http':'http://127.0.0.1:8080','https':https://127.0.0.1:8080'}

headers = {}
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
headers["Content-Type"] = "application/x-www-form-urlencoded"

r = s.get(url,header=headers,proxies=proxies,verify=False)
# verify=False disables the self-signed certificate verification
response_code = r.status_code
headers = r.headers
response = r.text
json_response = r.json()
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

### Writing a csv file
```
import csv

header = ['first','second','third']
data = ['first thing','second thing','third thing']

with open(file, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for row in data:
         writer.writerow(row)      
```

### Working with Json

```
import json

#Converting a json string to a dict object

# a json string
data = '{"id":"1","name":"leroy","hobby":"gaming"}'

# use loads for json object
j = json.loads(data)

print(j["hobby"])

# to convert python object (non-json) to a json string, use dumps

# a python dict object
data_dict = {
    "id":1,
    "name":"leroy",
    "has_blue_eyes":False
    }

j = json.dumps(data_dict)
print(j)

```
### Managing a subprocess

```
import psutil # for managing the pid
import subprocess # for executing the subprocesses
import time

def startWebServer(port):
    print("[+] starting webserver")
    proc = subprocess.Popen('python3 -m http.server %s' % port, shell=True)
    return proc

def stopWebServer(pid):
    print("[-] stopping webserver")
    parent = psutil.Process(pid) # identify the parent pid process
    for proc in parent.children(recursive=True): # kill any children processes
        proc.kill()
    parent.kill() # kill any parent processes 
    return

if __name__ == "__main__":
    port = '9000' # port number for webserver
    proc = startWebServer(port) # start the webserver and get the parent pid
    # proc.wait() # This will pause the main program until the subprocess completes. 
    time.sleep(10) # wait 10 seconds
    stopWebServer(proc.pid) # stop the webserver using the process pid
    
    exit()
```


### Multi-Threading (To Do)
