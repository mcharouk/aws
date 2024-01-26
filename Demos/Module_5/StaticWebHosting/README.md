# Static Web Hosting Demo

## Purpose
Show S3 capability to host a static website

## Steps 

* Turn off Block Public Access
* Update Bucket Policy

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

* index.html for index page
* 404.html for error page