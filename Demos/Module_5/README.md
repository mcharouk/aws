Bucket Name

```
test-marccharouk-674648573
```

policy that gives public permissions to download any file

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::test-marccharouk-674648573/*"
            ]
        }
    ]
}
```

IP whitelist

```
{
    "Version": "2012-10-17",
    "Id": "SourceIP",
    "Statement": [
        {
            "Sid": "SourceIP",
            "Effect": "Deny",
            "Principal": "*",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::test-marccharouk-674648573",
                "arn:aws:s3:::test-marccharouk-674648573/*"
            ],
            "Condition": {
                "NotIpAddress": {
                    "aws:SourceIp": "37.65.15.118/32"
                }
            }
        },
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::test-marccharouk-674648573/*"
        }
    ]
}
```