# Bash Shortcuts

### Removing \r characters from files
`tr -d '\r' < [inputfile] > [outputfile]`

### Reading through a text file line by line
```
while read line; do echo $line; done < inputfile
```
