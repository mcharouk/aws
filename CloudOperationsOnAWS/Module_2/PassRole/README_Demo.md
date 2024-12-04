* Assume the following role

```
DevLambdaAdminRole
```

* Create lambda with following name 

```
PassRoleLambdaTest
```

* provide Role named **Admin-NetworkFirewallPolicyEditorRole** to lambda. IT should work

* switch back to admin role and update policy of DevLambdaAdminRole

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "IAMAccessOnAllResources",
            "Effect": "Allow",
            "Action": [
                "iam:GetPolicy",
                "iam:GetPolicyVersion",
                "iam:GetRole",
                "iam:GetRolePolicy",
                "iam:ListAttachedRolePolicies",
                "iam:ListRolePolicies",
                "iam:ListRoles"
            ],
            "Resource": "*"
        },
        {
            "Sid": "IAMAccessOnDevResources",
            "Effect": "Allow",
            "Action": [
                "iam:PassRole"
            ],
            "Resource": [
                "arn:aws:iam::637423642269:role/Dev-*"
            ],
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": "lambda.amazonaws.com"
                }
            }
        }
    ]
}
```

* provide Role named **Admin-NetworkFirewallPolicyEditorRole** to lambda. It should be denied
* provide Role named **Dev-UpdateProductRole**. It should work