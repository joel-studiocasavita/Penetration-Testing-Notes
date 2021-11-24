# Bash 

### Basic Bash Loop
```
for i in $(command); do <something to > $i; done
```
### Reading through a text file line by line
```
while read line; do echo $line; done < inputfile
```
### Removing \r characters from files
```
tr -d '\r' < [inputfile] > [outputfile]
```
### providing scripted input to executable
```
echo <input 1>;sleep(1);echo <input 2>| <executable>
```
### Conditional Statements

```
#spaces matter

if [ "$i" == "somestring" ]; then
   do something
else
   do something else
fi

# elif can be used as an "else if" statement

```
### Conditional Operators
|Operator|Description|
|---|---|
|-eq| Returns true if two numbers are equivalent|
|-lt| Returns true if a number is less than another number|
|-gt| Returns true if a number is greater than another number|
|==| Returns true if two strings are equivalent|
|!=| Returns true if two strings are not equivalent|
|!| Returns true if the expression is false|
|-d| Check the existence of a directory|
|-e| Check the existence of a file|
|-r| Check the existence of a file and read permission|
|-w| Check the existence of a file and write permission|
|-x| Check the existence of a file and execute permission|

### Shell Operators
|oeprator|Description|
|---|---|
|;| Execute next command when the first finishes
|&| Execute command in the background |
|&&| Execute next command if the previous exited with status 0|
|\|\|| execute next command if the previous exited with any status other than 0 (opposite of &&)|

