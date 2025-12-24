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


## new development : SAM sync

* at start of the demo, dev and prod are already deployed
* goal of demo is to make a change in dev, and a change in production using canary release mode
* show samconfig.toml
  * stack name are different in dev or production
  * parameter override in production
  * show conditions in template

### test sync without watch feature

* change lambda code
* execute command
```
sam sync --code
```
* execute Powershell script named invokeDevAPI.ps1 (in root folder)

### test sync with watch feature

* launch synchronization mode in a dedicated terminal (can take on or two minutes)

```
sam sync --stack-name SAMDemoStack --watch
```

* if this command fails, remove the .aws-sam directory and re-execute the same command
* change lambda code, check time it's taking to redeploy, should be about 7s
* execute Powershell script named invokeDevAPI.ps1 (in root folder)

## Deployments

* change Lambda Code
* Build new version

```
sam build
```

### Canary deployment

* show sam template code
  * sections on alarm
  * section on deployment mode (Canary10Percent5Minutes)
* deploy second production version

```
sam deploy --config-env prod
```

* execute Powershell script named invokeProdAPI.ps1 (in root folder) to see call distribution
* show weighted alias in lambda
* show code deploy deployment in console
* can fail an alarm to demonstrate rollback

```
aws cloudwatch set-alarm-state --alarm-name LatestVersionErrorGreaterThanZeroAlarm-prod --state-value ALARM --state-reason test
```
