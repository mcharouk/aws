# Demo Steps

* connect to console (private navigation) with credentials 
  
* user

```
contractor
```
* password

```
Contractor2024!
```

## Bucket creation

* who am i ?
```
aws sts get-caller-identity
```

* create bucket (should fail)

```
aws s3 mb s3://marc-charouk-assume-role-demo
```

* assume S3ContractorRole

```
aws sts assume-role --role-arn "arn:aws:iam::637423642269:role/ContractorS3Role" --role-session-name ContractorS3Role > roleCredentials.json
```

* display reponse content

```
cat roleCredentials.json
```

* copy credentials info and export in env variables

```
export AWS_ACCESS_KEY_ID=$(cat roleCredentials.json | jq -r '.Credentials.AccessKeyId')
export AWS_SECRET_ACCESS_KEY=$(cat roleCredentials.json | jq -r '.Credentials.SecretAccessKey')
export AWS_SESSION_TOKEN=$(cat roleCredentials.json | jq -r '.Credentials.SessionToken')
```

* display environment variables

```
echo $AWS_ACCESS_KEY_ID
echo $AWS_SECRET_ACCESS_KEY
echo $AWS_SESSION_TOKEN
```

* who am i ?
```
aws sts get-caller-identity
```


* create bucket

```
aws s3 mb s3://marc-charouk-assume-role-demo
```

* remove bucket

```
aws s3 rb s3://marc-charouk-assume-role-demo
```