# KMS Key

* Symmetric
* For Encrypt And Decrypt operations
* Alias

```
DemoS3Key
```
  
* Key Administrator. Select Role that contains this string

```
AWSAdministratorAccess
```

* In Key Policy section, note that section that allows IAM to give identity-based permissions
* In Key properties, show Key Rotation Section
* Try to schedule for deletion, show the duration you can set, and confirmation required

# S3 Bucket

* Create S3 Bucket with the customer managed Key

```
aws-training-marccharouk-ssekms
```


* Assume the role S3Administrator and try to upload an object to the bucket (there is sampleFile.txt in this folder for example). 
* Upload should fail because Lack of permissions.
* go to KMS Key Property, Key Policy section
* Add S3Administrator Role as key User
* Show KMS Resource policy after the change
* Try again to upload the file. It should succeed
