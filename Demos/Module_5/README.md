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

IP whitelist
```
{
  "Id": "SourceIP",
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "SourceIP",
      "Action": "s3:*",
      "Effect": "Deny",
      "Resource": [
        "arn:aws:s3:::DOC-EXAMPLE-BUCKET",
        "arn:aws:s3:::DOC-EXAMPLE-BUCKET/*"
      ],
      "Condition": {
        "NotIpAddress": {
          "aws:SourceIp": [
            "37.65.15.118/32"
          ]
        }
      },
      "Principal": "*"
    }
  ]
}
```