## Identity pool creation

* create an identity pool
* create a new iam role with name

```
IdentityPoolTestRole
```

* Leave **Role Settings** to default
* in **Attributes for access control** section, choose custom mappings
  * Claim
  ``` 
  custom:department
  ```
  * Tag Key
  ``` 
  department
  ```

* put any name for identity pool
  
## Identity pool post creation

* to the newly created role
  * add policy named **IdentityPoolTestPolicy**
  * add to trust policy action **sts:TagSession**. Needed for [attribute for access control](https://docs.aws.amazon.com/cognito/latest/developerguide/using-afac-with-cognito-identity-pools.html)

```
"Action": ["sts:AssumeRoleWithWebIdentity","sts:TagSession"]
```

## Show code

Code is in test-identity-pools.py. Steps

* authenticate with IDP (cognito user pool)
* get an identity id. It's a identity specific to identity pool which is mapped to a user. It will create it if it does not exist.
* get temporary credentials with identity id and id token
* try to get object from S3

