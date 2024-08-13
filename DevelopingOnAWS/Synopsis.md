# Module 3 : Environment

## Demo

* AWS API with Postman
* CodeWhisperer

## AWS Signature

* create a hashed string from request parameters
* create a signing key with secret access key and other parameters (date, region, service)
* encrypt the hashed string with the signing key, and pass it in headers or query parameters
* AWS will apply the same process when it receives the request. If the same string is found, the request is accepted
* The request must reach AWS within 5 minutes, or AWS will deny the request (protection against replay attacks)


## SDK metrics
* [SDK metrics](https://boto3.amazonaws.com/v1/documentation/api/1.17.109/guide/sdk-metrics.html#definitions-for-sdk-metrics) helps diagnose communication issues between client and AWS
* Requires CloudWatch Agent installed on the client

# Module 4 : Permissions

## Demo

* Permissions Boundary
* Different profile with programmatic access
* Can show assumeRole result with SessionToken

# Module 5 : Storage 1

# Module 6 : Storage 2