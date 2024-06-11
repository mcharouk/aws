# Prerequisities

* Policy to create : EC2ProductPolicyForServiceCatalog

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "iam:GetRole",
                "iam:PassRole",
                "iam:DetachRolePolicy",
                "iam:DeleteRolePolicy",
                "iam:CreateRole",
                "iam:DeleteRole",
                "iam:AttachRolePolicy",
                "iam:PutRolePolicy",
                "iam:GetRolePolicy"
            ],
            "Resource": "arn:aws:iam::*:role/*"
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": "s3:GetObject",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "s3:ExistingObjectTag/servicecatalog:provisioning": "true"
                }
            }
        },
        {
            "Sid": "VisualEditor2",
            "Effect": "Allow",
            "Action": [
                "cloudformation:SetStackPolicy",
                "iam:CreateInstanceProfile",
                "iam:DeleteInstanceProfile",
                "sns:*",
                "iam:GetInstanceProfile",
                "iam:RemoveRoleFromInstanceProfile",
                "iam:ListInstanceProfileTags",
                "iam:ListInstanceProfiles",
                "cloudformation:GetTemplateSummary",
                "iam:AddRoleToInstanceProfile",
                "cloudformation:DescribeStacks",
                "iam:ListInstanceProfilesForRole",
                "cloudformation:DescribeStackEvents",
                "cloudformation:CreateStack",
                "cloudformation:DeleteStack",
                "ssm:*",
                "cloudformation:UpdateStack",
                "ec2:*",
                "servicecatalog:*",
                "iam:UntagInstanceProfile",
                "cloudformation:ValidateTemplate",
                "iam:TagInstanceProfile"
            ],
            "Resource": "*"
        }
    ]
}
```
* Role to create : EC2ProductPolicyForServiceCatalogRole

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "",
            "Effect": "Allow",
            "Principal": {
                "Service": "servicecatalog.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

* Upload cloud formation template in an S3 bucket

# Product creation

* Create a portfolio
* In portfolio action
  * Create a product
  * Create a launch constraint
  * Create an Access to allow administrator role

# Product creation

Provisioned Product Name
```
LinuxApacheTestProductInstance
```

Get Last parameter store key values for linux AMIs. Run that on a Windows Shell

```
aws ssm get-parameters-by-path ^
    --path /aws/service/ami-amazon-linux-latest ^
    --query Parameters[].Name
```

AMI Parameter Store Key

```
/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-6.1-x86_64
```

# Links

[Service catalog reference architecture](https://github.com/aws-samples/aws-service-catalog-reference-architectures)