# Permission Boundary Demo

## Tech lead permissions

### Role

Role Name
```
TechLeadRole
```

### Policy

Policy Name
``` 
S3AndSQSFullAccess
```

* Give aws managed policies
* Alternative

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Statement1",
            "Effect": "Allow",
            "Action": [
                "sqs:*",
                "s3:*"
            ],
            "Resource": [
                "*"
            ]
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
                "s3:*"
            ],
            "Resource": "*"
        }
    ]
}
```