# Module 3 : Environment

## Demo

* AWS API with Postman
* CodeWhisperer
* Deploy a Lambda with VSCode Toolkit

## AWS Signature

* create a hashed string from request parameters
* create a signing key with secret access key and other parameters (date, region, service)
* encrypt the hashed string with the signing key, and pass it in headers or query parameters
* AWS will apply the same process when it receives the request. If the same string is found, the request is accepted
* The request must reach AWS within 5 minutes, or AWS will deny the request (protection against replay attacks)


## SDK metrics
* [SDK metrics](https://boto3.amazonaws.com/v1/documentation/api/1.17.109/guide/sdk-metrics.html#definitions-for-sdk-metrics) helps diagnose communication issues between client and AWS
  * Number of API calls that fails because of client errors
  * Number of API calls that fails because of server errors
  * End ot end latency
  * Throttle count (reached throttle limit of AWS services)
* For Java, you can enable that in [SDK](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/metrics-list.html)
* Available for .NET too

## AWS CLI

[AWS CLI Builder (not official)](https://awsclibuilder.com/home) is a nice tool to generate aws cli commands

## AWS SDK

[Example of adjusting api retries parameters](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/retries.html#configuring-a-retry-mode)

# Module 4 : Permissions

## Demo

* Permissions Boundary
  * but instead of showing denied statement on the console, can use the cli for that
* Different profile with programmatic access
* Can show assumeRole result with SessionToken
* Can show policy simulator

# Module 5 : Storage 1

## Demo

* Bucket Versioning
* Bucket Policies
* Access Points

# Module 6 : Storage 2

## Demo

* Multipart Upload With low-level commands
* Pre-signed URL
* S3 Batch Operations
* Static Web Hosting with CORS configuration

# Module 7 : Database 1

## Demo

* NoSQL Workbench
* DynamoDB Local
* Java : Document interfaces and object persistent interface. We see them in Module 8...

# Module 8 : Database 2

## Demo

* CRUD operations with DynamoDBMapper

# Module 9 : Compute

## Demo

* Show cold start
* Docker Container and Lambda
* Layers
* Aliases with API Gateway

# Module 10 : Gateway

* Difference between HTTP API and REST API
* Etudier comment fonctionnent les websockets de manière macro sur l'API Gateway
* API Gateway swagger extensions

## Demo

* Canary release
* Swagger import/export. Swagger extensions are showed in Lab 6
* Query validation. Shown in Lab 5

# Module 11 : Micro services

* Strangler Pattern diagrams

## Demo

* Step functions

# Module 12 : Access

## Demo

* Webapp with user pools and identity pools
* Explore the [React sample](https://docs.aws.amazon.com/cognito/latest/developerguide/getting-started-test-application-react.html) provided by AWS

## Cognito

A an app client is a configuration specific to a mobile or web application

settings at app client level

* analytics
* hosted UI (self-managed Cognito users)
* resource servers and custom scopes
* Threat protection (action you can define if account is compromised). This can happen when users reuse credentials at more than one site, or when they use insecure passwords
* Attribute read and write permissions (ability to read or write user attributes from your specific application)
* Token expiration and revocation
* Authentication flows

# Module 13

## Demo

* Rancher Desktop not compatible with sam invoke. Can only demonstrate sam local generate-events for example
* Can show a SAM template with deployment of a serverless API, a serverless function and a simple table

# Module 14

## Demo

* Logs insights
* X-ray is shown in the lab