# Access point

## delegate access to access point policy

This policy must be added to bucket S3 policy

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "270188911144"
            },
            "Action": "*",
            "Resource": [
                "arn:aws:s3:::accesspointdemo-marccharouk-548675484",
                "arn:aws:s3:::accesspointdemo-marccharouk-548675484/*"
            ],
            "Condition": {
                "StringEquals": {
                    "s3:DataAccessPointAccount": "270188911144"
                }
            }
        }
    ]
}
```

## Access point policy

(object folder in resource path is mandatory)

for folder 1
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Statement1",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::270188911144:role/TechLead"
            },
            "Action": [
                "s3:GetObject",
                "s3:PutObject"
            ],
            "Resource": "arn:aws:s3:eu-west-3:270188911144:accesspoint/accesspointfolder1/object/folder1/*"
        }
    ]
}
```

## Minimal access policies to IAM

TechLead Should have this policy attached

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:GetAccessPoint",
                "s3:ListAllMyBuckets",
                "s3:ListAccessPoints",
                "s3:ListBucket",
                "s3:ListMultiRegionAccessPoints"
            ],
            "Resource": "*"
        }
    ]
}
```