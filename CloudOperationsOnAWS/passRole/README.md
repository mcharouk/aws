* NetworkFirewallPolicyEditor
* Role associated : Admin-NetworkFirewallPolicyEditorRole

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "network-firewall:UpdateFirewallPolicyChangeProtection",
                "network-firewall:AssociateFirewallPolicy",
                "network-firewall:UpdateFirewallPolicy",
                "network-firewall:DeleteFirewallPolicy",
                "network-firewall:CreateFirewallPolicy"
            ],
            "Resource": "*"
        }
    ]
}
```

* UpdateProductPolicy
* Dev-UpdateProductRole

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "sqs:DeleteMessage",
                "dynamodb:PutItem",
                "sqs:ReceiveMessage",
                "sqs:SendMessage"
            ],
            "Resource": "*"
        }
    ]
}
```


* DevPassRolePolicy
* DevLambdaAdminRole

LambdaFullAccess

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [                
                "lambda:*"                
            ],
            "Resource": "*"
        }
    ]
}
```

Original policy 


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
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": "lambda.amazonaws.com"
                }
            }
        }
    ]
}
```

Updated Policy

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