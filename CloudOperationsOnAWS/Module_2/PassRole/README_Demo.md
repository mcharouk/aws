* any name to lambda function

* To create the lambda, assume the following role

```
DevLambdaAdminRole
```

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