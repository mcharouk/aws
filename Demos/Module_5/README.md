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
                "arn:aws:s3:::demo-staticwebhosting-marccharouk-76857485/*"
            ]
        }
    ]
}
```