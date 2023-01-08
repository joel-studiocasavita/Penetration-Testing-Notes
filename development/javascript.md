# Javascript

### External Script Reference
`<script src = https://somelocation/script.js></script>`

### Message Box
`alert("Hello World");`

### Making a Post Request
```
fetch('https://example.com/post', {method: 'POST',headers: {'Accept': 'application/json','Content-Type': 'application/json'},
  body: JSON.stringify({ "id": 78912 })})
.then(response => response.json())
.then(response => console.log(JSON.stringify(response)))
```
