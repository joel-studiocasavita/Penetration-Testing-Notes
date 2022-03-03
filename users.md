# Users 

## Adding Users

### Linux

**Create a user**  
`-m` Creates a home directory for the user under `/home`  
`-s` Assigns a specific shell to use  
```
adduser -m -s /usr/bin/zsh <username>
```
<br>

**Assigning new users to groups**  
`-g` assigns the user to a primary group.  
`-G` assigns the user to secondary groups.  This switch will accept a comma separated list of groups   

```
useradd -g users -G developers,wheel <username>
```
<br>

**Assigning existing Users to groups**
`-a` adds a user to a group  
`-d` removes a user from a group  
`-G` a comma separated list of groups  

```
sudo usermod -a -G <groupname> <username>
```
<br>

**Set/Change user's password**

```
sudo passwd <username>
```
