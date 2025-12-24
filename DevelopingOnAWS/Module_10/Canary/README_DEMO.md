# Canary Release With API Gateway

* show stage variable named **lambdaAlias**
* show integration request, must point to **Blue** Alias
* change it to 

```
arn:aws:lambda:eu-west-3:637423642269:function:CanaryDemo:${stageVariables.lambdaAlias}
```

* publish a new Lambda version
* create a new Alias **Green** and point it to the new version
* change permissions of Green alias (not the version) to allow API Gateway to call it. 
  * add a Resource-based policy statements
  * select API Gateway as AWS Service
  * In Statement Id, put anything
  * in Source ARN, put the  **SourceARN** in cloudformation outputs
  * for Action, select lambda:InvokeFunction
* in api gateway **Prod** stage, create a canary deployment and override the lambdaAlias variable to **Green**
* Redeploy the api to the stage, so that the endpoint with the stage variable will be taken into account.
* In stage tab, in deployment history section, switch the new deployment to active state
* Test the deployment with stage invoke URL
* Promote the canary release