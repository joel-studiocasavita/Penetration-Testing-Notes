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
# Disable the self-signed certificate warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


url = 'URL'
headers = {"Header_1":"Header_1_value","Header_2":"Header_2_value"}
r = requests.get(url,header=headers,verify=False)
# verify=False disables the self-signed certificate verification
response_code = r.status_code
headers = r.headers
response = r.text
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

### Working with Json (To Do)

### Multi-Threading (To Do)
