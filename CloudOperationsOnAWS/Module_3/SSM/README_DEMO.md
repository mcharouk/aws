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

* for port forwarding command, take cloudformation stack output
* for windows rdp connection, take cloudformation stack output for both
  * host
  * username
* Password : decrypt password with a key pair. Private key can be retrieved in parameter store