# Demo

## Bucket name

* create bucket

```
marccharouk-demo-45756383
```

* upload logo.png
* uncheck all related to block public access
* make bucket public

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

* Activate Block public access feature
* Show public access has been denied