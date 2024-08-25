Validate template

```
sam validate
```

build template

```
sam build
```


## SAM sync

```
sam sync --stack-name SAMDemoStack --watch
```

Powershell invoke API

```
Invoke-RestMethod -Uri https://8xkfai1c6g.execute-api.eu-west-3.amazonaws.com/Prod
```

* change lambda code, check time it's taking to redeploy, should be about 7s

## Deployments

* change Lambda Code
* Execute Command

```
sam deploy --stack-name SAMDemoStack --s3-bucket marc-charouk-samdemo-576758948 --capabilities CAPABILITY_IAM --parameter-overrides Environment=prod
```

* execute script ./invokeAPI.ps1 to see the distribution of calls
* can fail an alarm to demonstrate rollback

```
aws cloudwatch set-alarm-state --alarm-name LatestVersionErrorGreaterThanZeroAlarm --state-value ALARM --state-reason test
```
