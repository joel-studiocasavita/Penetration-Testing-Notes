# java

## compiling java code

```
javac -source <version> -target <version> <java file> // compiles a java file 
echo "Main-Class: test" > META-INF/MANIFEST.MF // is required 
jar cmf META-INF/MANIFEST.MF <jar file> <class file> 
```

