## Steps to activate static web hosting

* create bucket **marccharouk-staticwebhosting**
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
                "arn:aws:s3:::marccharouk-staticwebhosting/*"
            ]
        }
    ]
}
```
* upload error.html and index.html (in html_pages local folder) in the root of s3 bucket

```
aws s3 cp html_pages s3://marccharouk-staticwebhosting/ --recursive
```

* activate static web hosting

```
aws s3 website s3://marccharouk-staticwebhosting/ --index-document index.html --error-document error.html
```

## CORS configuration

In CORS configuration (permissions tab) of the bucket that contains assets, provide this config
```
[
    {
        "AllowedHeaders": [
            "Authorization"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "http://marccharouk-staticwebhosting.s3-website.eu-west-3.amazonaws.com"
        ],
        "ExposeHeaders": [
            "Access-Control-Allow-Origin"
        ]
    }
]
```

* Allows GET methods from provided domain
* Authorized to send header Authorization
* Can return header Access-Control-Allow-Origin to be processed by client