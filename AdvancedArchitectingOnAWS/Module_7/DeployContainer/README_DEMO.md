# CodeBuild Project

* Project Name
```
PushToECR
```

* Source Provider : GitHub
* Credential : Custom source credential
* Credential type : Github App
* Fill in connection, Repository
* Source version : main

* Primary source webhook events
  * uncheck webhook (managed by codepipeline)
* Environment
  * Existing Service Role : CodeBuildServiceRole
  * Keep checked Allow CodeBuild to modify this service role
  * Additional Configuration : Add env variables
    * AWS_DEFAULT_REGION : eu-west-3
    * AWS_ACCOUNT_ID : copy account id
    * IMAGE_TAG : latest
    * IMAGE_REPO_NAME : cicd-sample-app
* Buildspec
  * Use a buildspec file
* Leave everything else as default

# CI Pipeline

* create a new Pipeline in CodePipeline
* select Build Custom Pipeline

## Pipeline settings

* Pipeline Name

```
BuildAndDeployPipeline
```

* Advanced Settings
  * Artifact Store
    * Custom location : provide bucket that ends with cicd-artifacts

## Source Stage

* Source Provider : Github (via Github App)
* Connection : sample-app-repo
* Repository : sample-app
* default branch : main

## Build Stage

* Build Provider
  * Other Build Providers : AWS CodeBuild
* Project Name : PushToECR
* Leave everything else as default

## Deploy Stage

* Skip Deploy stage (doing it later)

# CodeDeploy Resources

* create a new CodeDeploy Application
* Name

```
cicd-sample-app
```

* create a Deployment Group
* Name

```
prod-cicd-sample-app
```

* Service Role

```
ECS-CICD-CodeDeployServiceRole
```

* Cluster Name

```
ECS-CICD-Cluster
```

* Select Load Balancer
* Target Group 1 : select one that starts with Deploy-Appli (was created by Fargate Service automatically)
* Target Group 2 : sample-app-green-tg
* Reroute traffic immediately
* deployment configuration : Linear10PercentEvery1Min
* Can show options on Alarms (but don't provide anything)

# Create Deploy Pipeline


## Pipeline settings

## Deploy Stage

* Add Stage

```
Deploy
```

* Add Action name

```
DeployOnECS
```

* Action Provider : ECS (Blue/Green)
* Input Artifacts : select source artifacts
* select code deploy application name and deployment group
* ECS Task Definition
  * input Artifact : SourceArtifact
  * leave default (taskdef.json)
* CodeDeploy AppSpec File
  * input Artifact : SourceArtifact
  * leave default (appspec.yaml)

* Click on Save
