# S3

## Bucket Name
```
test-marccharouk-674648573
```
## Public bucket policy

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

## IP whitelist bucket policy

```
{
    "Version": "2012-10-17",
    "Id": "SourceIP",
    "Statement": [
         {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::test-marccharouk-674648573/*"
        },
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
        }       
    ]
}
```

## Glacier Vault Policy

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "deny-based-on-archive-age",
            "Effect": "Deny",
            "Principal": "*",
            "Action": "glacier:DeleteArchive",
            "Resource": "arn:aws:glacier:eu-west-3:637423642269:vaults/hello",
            "Condition": {
                "NumericLessThan": {
                    "glacier:ArchiveAgeInDays": "365"
                }
            }
        }
    ]
}
```