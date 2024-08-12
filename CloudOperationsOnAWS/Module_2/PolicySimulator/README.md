# Policy generator & Simulator

!!! Must be connected on an account where there is no SCP to work !!!

* [Policy Generator](https://us-east-1.console.aws.amazon.com/iam/home?region=eu-west-3#/policies/create)
* Create a Policy 
  * that allows read operations for Lambda service
  * With Resources 
    * name starts with dev-
    * Remove account part
  * With conditions ResourceTag / Key Project / StringEquals / ProjectA

* [Policy Simulator](https://policysim.aws.amazon.com/)
  * Test on Lambda function with following ARN

```
arn:aws:lambda:eu-west-3::function:dev-myFunction
```