# Demo

## Bucket name

bucket name : 

```
marccharouk-demo-45756383
```

## Bucket Policy

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Stmt1405592139000",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": [
                "arn:aws:s3:::marccharouk-demo-45756383/*"
            ]
        }
    ]
}
```