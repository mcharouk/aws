# Permission Boundary Demo

## Tech lead permissions

### Role

Role Name
```
LambdaRole
```

### Policy Without CloudShell

* Give aws managed policies
  * AmazonS3FullAccess
  * AmazonSQSFullAccess
  
### Policy With CloudShell

Policy Name

```
S3AndSQSFullAccess
```

Policy

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "sqs:*",
                "s3:*",
                "cloudshell:*"
            ],
            "Resource": "*"
        }
    ]
}
```

## PermissionBoundary policy

Policy Name
```
S3AndSNSFullAccess
```

Policy Statement

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "sns:*",
                "s3:*",
                "cloudshell:*"
            ],
            "Resource": "*"
        }
    ]
}
```


## Command lines

### Config file

```
[profile lambdarole]
role_arn = arn:aws:iam::637423642269:role/LambdaRole
region = eu-west-3
```

alternative : assume lambdaRole in console and use CloudShell to execute commands without profile param

### SQS

create topic sqs (denied because of permission boundary)

```
aws sqs create-queue --queue-name sqs-demo-queue
```

### SNS

create topic sns (denied because no resource based policy)

```
aws sns create-topic --name sns-demo-topic
```

### S3

create s3 bucket (allowed)

```
aws s3api create-bucket --bucket marccharouk-permissionboundary-demo-657489457  --create-bucket-configuration LocationConstraint=eu-west-3
```

List buckets

```
aws s3api list-buckets
```

delete s3 bucket

```
aws s3api delete-bucket --bucket marccharouk-permissionboundary-demo-657489457
```