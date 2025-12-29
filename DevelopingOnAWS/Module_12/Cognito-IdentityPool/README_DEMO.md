## Identity pool creation

* create an identity pool
* create a new iam role (through Identity Pool creation form) with name below

```
IdentityPoolTestRole
```

* Leave **Role Settings** to default
* in **Attributes for access control** section, choose custom mappings  
  * Tag Key
  ``` 
  department
  ```
  * Claim
  ``` 
  custom:department
  ```

* put any name for identity pool
* don't activate basic authentication
  
## Identity pool post creation

* to the newly created role
  * add policy named **IdentityPoolTestPolicy** (give access to s3)
  * add to trust policy action **sts:TagSession**. Needed for [attribute for access control](https://docs.aws.amazon.com/cognito/latest/developerguide/using-afac-with-cognito-identity-pools.html)

```
"Action": ["sts:AssumeRoleWithWebIdentity","sts:TagSession"]
```

## Show code

Code is in test-identity-pools.py. Steps

* authenticate with IDP (cognito user pool) to get id token
* get an identity id from id token. It's a identity specific to identity pool which is mapped to a user. It will create it if it does not exist.
* get temporary credentials with identity id and id token
* try to get object from S3
