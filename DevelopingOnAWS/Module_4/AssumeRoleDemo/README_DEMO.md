* connect to [console](https://637423642269.signin.aws.amazon.com/console) using user contractor and password that should appear in IDE terminal
* go to cloudShell and create a bucket (should fail)

```
aws s3 mb s3://marc-charouk-assume-role-demo-test
```

* who am i ?

```
aws sts get-caller-identity
```

* assume role 

```
aws sts assume-role --role-arn "arn:aws:iam::637423642269:role/S3access" --role-session-name DevOnAWS > tempCredentials.json
```

* display temporary credentials returned by assume role cmd

```
jq '.' tempCredentials.json
```

* export programmatic credentials in environment variables

```
export AWS_ACCESS_KEY_ID=$(jq '.Credentials.AccessKeyId' -r tempCredentials.json)
export AWS_SECRET_ACCESS_KEY=$(jq '.Credentials.SecretAccessKey' -r tempCredentials.json)
export AWS_SESSION_TOKEN=$(jq '.Credentials.SessionToken' -r tempCredentials.json)

```

* check environment variables values

```
echo $AWS_ACCESS_KEY_ID
echo $AWS_SECRET_ACCESS_KEY
echo $AWS_SESSION_TOKEN

```

* who am i ?

```
aws sts get-caller-identity
```

* try to create bucket

```
aws s3 mb s3://marc-charouk-assume-role-demo-test
```

* remove bucket

```
aws s3 rb s3://marc-charouk-assume-role-demo-test
```