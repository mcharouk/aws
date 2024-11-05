# Base commands

sam init

```
sam init --name my-sam-new-app --app-template hello-pt --package-type Zip --runtime python3.11 --application-insights --architecture x86_64  --dependency-manager pip --tracing
```

build template

```
sam build
```


Validate template

```
sam validate
```


Example of generating an event

```
sam local generate-event apigateway aws-proxy
```


# Deployment and environment

* show samconfig.toml
  * stack name are different in dev or production
  * parameter override in production
  * show conditions in template

* deploy first version in dev. Save API Gateway URL in a temp file (used to demonstrate sync feature)

```
sam deploy
```

* deploy first production version. Save API Gateway URL in a temp file (used to demonstrate canary rel feature)

```
sam deploy --config-env prod
```

## new development : SAM sync

### test sync without watch feature

* change lambda code
* execute command
```
sam sync --code
```

* execute Powershell script in another terminal (for clarity)

```
Invoke-RestMethod -Uri [URLProvidedAsCFOutput]
``` 

### test sync with watch feature

* launch synchronization mode in a dedicated terminal

```
sam sync --watch
```
* change lambda code, check time it's taking to redeploy, should be about 7s

* execute Powershell script
```
Invoke-RestMethod -Uri [URLProvidedAsCFOutput]
```

## Deployments

* change Lambda Code

* Build new version

```
sam build

```

* update script ./invokeAPI.ps1 with api gateway URL (provided as output in CF)

### Canary deployment

* show codedeploy
* deploy second production version

```
sam deploy --config-env prod
```

* execute script ./invokeAPI.ps1 to see the distribution of calls
* can fail an alarm to demonstrate rollback

```
aws cloudwatch set-alarm-state --alarm-name LatestVersionErrorGreaterThanZeroAlarm-prod --state-value ALARM --state-reason test
```
