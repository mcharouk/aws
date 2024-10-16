# Permission Boundary Demo

## Tech lead permissions

### Role

Role Name
```
LambdaRole
```

### Identity Based Policy

Policy Name
``` 
S3AndSQSFullAccess
```

* Give aws managed policies

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
                "s3:*"
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

### SQS

create topic sqs (denied because of permission boundary)

```
aws sqs create-queue --queue-name sqs-demo-queue --profile lambdarole
```

### SNS

create topic sns (denied because no policy allow action)

```
aws sns create-topic --name sns-demo-topic --profile lambdarole
```

### S3

create s3 bucket (allowed)

```
aws s3api create-bucket --bucket marccharouk-permissionboundary-demo-657489457 --profile lambdarole
```

List buckets

```
aws s3api list-buckets --profile lambdarole
```

delete s3 bucket

```
aws s3api delete-bucket --bucket marccharouk-permissionboundary-demo-657489457 --profile lambdarole
```