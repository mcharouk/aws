Powershell Commands

```
Get-Location
$env:AdministratorDocumentsPath = 'C:\Users\Administrator\Documents'
$env:AdministratorDocumentsPath
Get-ChildItem -Path $env:AdministratorDocumentsPath
$testFileName = $env:AdministratorDocumentsPath + '\testFile.txt'
if (Test-Path $testFileName) {
  Remove-Item $testFileName
}
New-Item $testFileName -ItemType File -Value "The first sentence in our file."
Add-Content $testFileName "The second sentence in our file."
Get-Content -Path $testFileName
Get-ChildItem -Path $env:AdministratorDocumentsPath
```

Start port forwarding / get output of cloudformation stack, it's more dynamic

```
aws ssm start-session --target i-0c18c79a4842c50bf --document-name AWS-StartPortForwardingSession --parameters "localPortNumber=54321, portNumber=3389" --region eu-west-3
```

Windows instance RDP connection

* Host : 
``` 
localhost:54321
```

* User

```
[InstanceId]\Administrator
```

* Password : decrypt password with a key pair