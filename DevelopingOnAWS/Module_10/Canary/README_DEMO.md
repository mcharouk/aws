# Canary Release With API Gateway

* show stage variable named **lambdaAlias**
* show integration request, must point to **Blue** Alias
* change it to 

```
arn:aws:lambda:eu-west-3:637423642269:function:CanaryDemo:${stageVariables.lambdaAlias}
```

* publish a new Lambda version
* create a new Alias **Green** and point it to the new version
* change permission of Green version to allow API Gateway to call it. **SourceARN** will appear in cloudformation outputs
* in api gateway **Prod** stage, create a canary deployment and override the lambdaAlias variable to **Green**
* redeploy the api to the stage
* in stage, in deployment history section, switch the new deployment to active state
* test the deployment with stage invoke URL
* Finally promote the canary release