# SSM Demo

## Session logging activation

### S3 Bucket

* Normally ssm session logging should already be activated by a script
* If not, activate SSM session logging (with S3 Bucket)
  * can require encryption as S3 bucket has S3 managed encryption activated
  * s3 prefix
```
session-logs
```

### Cloudwatch 

* don't require encryption
* might need to restart SSM agent to make it work

```
Stop-Service AmazonSSMAgent
```

```
Start-Service AmazonSSMAgent
```
* reconnect to a new session

## Execute commands

* Connect to EC2 Instance with SSM (Windows) and execute following commands

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

* disconnect from terminal session

## Port forwarding for RDP

* for port forwarding command, take cloudformation stack output
* for windows rdp connection, take cloudformation stack output for both
  * host
  * username
  * for password : decrypt password with a key pair. Private key can be retrieved in parameter store

