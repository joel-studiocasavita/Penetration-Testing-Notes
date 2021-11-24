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
