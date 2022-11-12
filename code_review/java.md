# java

## Deserialization
The following terms are useful for looking up: 

  XMLDecoder with external user-defined parameters. 
  XStream together with fromXML 
  ObjectInputStream () with readObject 
  readObject 
  readObjectNodData 
  readResolve 
  readExternal 
  ObjectInputStream.readUnshared 
  Serializable 
  
## Web Servlet Methods
doGET  
doPost  
doPut  
doDelete  
doCopy  
doOptions. 

## Dangerous Functions
```
<—————-Directory Traversal————→

Open a file
File f = new File(“filePath”, userinput);
Reading & Writing file
java.io.FileInputStream
java.io.FileOutputStream
java.io.FileReader
java.io.FileWriter
Ex: FileInputStream fis = new FileInputStream(“filePath” + userinput);

<—————-SSRF————→

Open a URL
InputStream in = new URL.openStream()
where url = User supplied Input
```

https://docs.guardrails.io/docs/vulnerabilities/java/insecure_use_of_dangerous_function

## Dangerous imports
```
import java.util.Random
# Results can be reproduced given the seed value.  SecureRandom doesn't have this issue.
```

## web.xml file

Java web applications use a deployment descriptor file to determine how URLs map to servlets, which URLs require authentication, and other information. This file is named web.xml, and resides in the app's WAR under the WEB-INF/ directory. web.xml is part of the servlet standard for web applications.
