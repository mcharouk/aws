# Steps

## config.json

* user credentials refers to *john.foo* user. 
  * I'm using it with environment variables
* role refers to a role named *S3AdminRole* created by CF who has S3 full access policy
  * I'm using it to force the role in the code

## Actions to take

* execute script credentials-priority.py

* Initial State should be 

```
unset_aws_profile = True
load_env_variables = False
load_credentials_in_code = False
```

| option_name              | value | expected_result                                               |
| ------------------------ | ----- | ------------------------------------------------------------- |
| unset_aws_profile        | True  | take default user in .aws/config                              |
| unset_aws_profile        | False | take profile in .aws/config specified in AWS_PROFILE variable |
| load_env_variables       | True  | take john.foo credentials provided in config.json             |
| load_credentials_in_code | True  | take S3 admin role credentials loaded in the code             |

