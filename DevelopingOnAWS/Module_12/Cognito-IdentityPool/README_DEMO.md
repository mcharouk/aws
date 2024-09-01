## Identity pool creation

* create an identity pool
* role name

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


