# dotnet


### Analyzing a DLL or .exe with DnsSpy

1. Drag the file into the window or click load in the menu and choose a file. 
2. It is possible to search by looking at the bottom right and then clicking on 'search' or by going to search from the menu. 
3. To find cross-reference do the following. right-click on a function in the menu on the left with all functions, then click on Analysis. Now we see the cross-reference. 
4. To edit a class do the following. Right-click on a method, then Edit Class, after which you can now make adjustments. Then we click on Compile and then on File -> Save all to overwrite the original version. 

### Dangerous functions

```
<———————Acquire User-Supplied Data————→ 

QueryString 
Params 
Item 
Form 
ServerVariables // 
Headers // 
Files // Returns a collection of fi les uploaded by the user. 
Cookies // 
HttpMethod // Returns the method used in the HTTP request. 
InputStream // 
BinaryRead // 
Ex: string lastname = Request.QueryString[“lastname”]; 

<——————RFI & LFI—————> 
    Server.Execute(path) //executes an ASP file from inside another ASP file 

<————Directory Traversal———> 
    Open a file 
    FileStream fs = File.Open(“C:\\temp\\” + userinput,FileMode.OpenOrCreate); 

    Some constructor method is used to read a file. 
    1. System.IO.FileStream 
    2. System.IO.StreamReader 
    3. System.IO.StreamWriter 
    Ex: FileStream fs = new FileStream(“F:\\tmp\\” + userinput,FileMode.OpenOrCreate); 

<—————OS Command Injection—→ 
    string cmd= @"/C ping" + Request.QueryString[“hostname”]; /* @ means do not interpret control character inside string */ 
    ProcessStartInfo info = new ProcessStartInfo(“cmd.exe”, cmd); 
    Process.Start(info); 

<——————-SQL Injection———→ 
Following classes that can be used to create and execute a SQL statement. If these are not used with parameterized value and user input is not properly sanitize/filter SQL injection might be possible. 
    1. System.Data.SqlClient.SqlCommand 
    2. System.Data.SqlClient.SqlDataAdapter 
    3. System.Data.Oledb.OleDbCommand 
    4. System.Data.Odbc.OdbcCommand 
    5. System.Data.SqlServerCe.SqlCeCommand 
    Ex 1: 
    string query = “select username, password from user where username=’” + username + “’ & password=’” + password + ""’; 
    OdbcCommand command = new OdbcCommand(query, connection); 
    comand.ExecuteNonQuery(); 

Ex 2: 
var query = “SELECT * FROM User WHERE Username = ’” + username “’”; 
SqlCommand command = new SqlCommand(query , connection); 
SqlDataReader reader = command.ExecuteReader(); 

<——————-XSS————————→ 
    Response.Write() 
    <%= searchTermFromUser %> 

<——————-XXE————————→ 
Vulnerable Parser 

    XmlDocument < v4.5.2+ 
    XPathNavigator < v4.5.2+ 
    XPathNavigator < v4.5.2+ 

<——————Serialization————> 
    Deserialize Binary to Object 
    BinaryFormatter bf = new BinaryFormatter(); 
    FileStream fsin = new FileStream(“xyz.binary”, FileMode.Open, FileAccess.Read); 
    obj = (class) bf.Deserialize(fsin); 

    Deserialize XML to Object 
    XmlSerializer xs = new XmlSerializer(typeof(class)); 
    FileStream fsin = new FileStream(“xyz.xml”, FileMode.Open, FileAccess.Read); 
    obj=(class)xs.Deserialize(fsin); 

    Deserialize Json to Object 
    // Deserializing json data to object using JavaScriptJsonSerializer 
    string jsonData =@’{"Name":“C-sharpcorner”,“Description”:“Share Knowledge”}’; 
    JavaScriptSerializer js = new JavaScriptSerializer(); 
    class object = js.Deserialize(jsonData); 

// Deserializing json data to object using Json.NET 
string json =@’{"Name":“C-sharpcorner”,“Description”:“Share Knowledge”}’; 
class Obj = JsonConvert.DeserializeObject(json); 

// Deserializing json data to object using DataContractJsonSerializer 
string json = “{\”Username\“:\”raj\“,\”Password\“:\”insecure\“}”; 
var ms = new MemoryStream(Encoding.Unicode.GetBytes(json)) 
DataContractJsonSerializer deserializer = new DataContractJsonSerializer(typeof(class)); 
class Obj = (class)deserializer.ReadObject(ms); 
```
