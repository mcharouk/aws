* create an identity pool
* role name

```
IdentityPoolTestRole
```

* add to role policy named **IdentityPoolTestPolicy**
* add to trust policy action **sts:TagSession**. Needed for [attribute for access control](https://docs.aws.amazon.com/cognito/latest/developerguide/using-afac-with-cognito-identity-pools.html)
* in custom mappings
  * Tag Key : preferred_username 
  * Claim : preferred_username
* put any name for identity pool
