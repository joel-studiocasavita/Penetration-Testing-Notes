### Comparison Operators  


|Example|	Name	|Result|
|:--:|:--:|:--:|
|$a == $b|	Equal|	true if $a is equal to $b after type juggling.|
|$a === $b|	Identical|	true if $a is equal to $b, and they are of the same type.|
|$a != $b|	Not equal	|true if $a is not equal to $b after type juggling.|
|$a <> $b|	Not equal|	true if $a is not equal to $b after type juggling.|
|$a !== $b|	Not identical|	true if $a is not equal to $b, or they are not of the same type.|
|$a < $b|	Less than	|true if $a is strictly less than $b.|
|$a > $b|	Greater than	|true if $a is strictly greater than $b.|
|$a <= $b|	Less than or equal to	|true if $a is less than or equal to $b.|
|$a >= $b|	Greater than or equal to	|true if $a is greater than or equal to $b.|
|$a <=> $b|	Spaceship	| An int less than, equal to, or greater than zero when $a is less than, equal to, or greater than $b, respectively.|

### Magic Hashes

```
php > echo md5('240610708');
0e462097431906509019562988736854
php > var_dump('0e462097431906509019562988736854' == '0');
bool(true)
```
### Abused methods
```
exec_shell
exec
system
doll
create_function
require
move_uploaded_file
unserialize
serialize
eval
popen
<backtick>
pcntl_exec
preg_replace (with /e modifer)
include
include_once
```
