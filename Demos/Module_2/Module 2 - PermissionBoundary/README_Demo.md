# Permission Boundary Demo

* Show TechLeadRole Policies.
  *  Especially the one that denies creating a role without the permission boundary attached, or detaching a policy
* Assume TechLeadRole
* Create Role named **LambdaRole**
  * Trusted entity : lambda service
  * Policies attached : TechLeadLambdaPolicy
* Try to create the role without the permission boundary, it should fail
* Attach PermissionBoundaryPolicy to lambdaRole
* Create the Role
* Attach the Role to the lambda PermissionBoundary (Configuration -> Permissions -> Edit)
* Show Lambda Code
* Test the Lambda
* check the logs to see the effect of policies


