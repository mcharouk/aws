# Module 3 : Environment

## Demo

* AWS API with Postman
* CodeWhisperer
* Deploy a stack and check it with VSCode Toolkit (AWS explorer)


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
  * End to end latency
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
* Different profile with programatic access
* Can show assumeRole result with SessionToken
* Can show policy simulator

# Module 5 : Storage 1

## Demo

* Bucket Versioning
* Bucket Policies
* Access Points

## Headers

ETag is hash of the object. Can be used to check integrity

# Module 6 : Storage 2

## Demo

* Multipart Upload With low-level commands
* Pre-signed URL : we see that in a lab (don't remember which one)
* S3 Batch Operations
* Static Web Hosting with CORS configuration

## Pre-signed URL

give a use case (draw.io)


# Module 7 : Database 1

## Demo

* NoSQL Workbench
* DynamoDB Local

# Module 8 : Database 2

## Demo

* CRUD operations with DynamoDBMapper

## 

* [Counter in DDB](https://aws.amazon.com/blogs/database/implement-resource-counters-with-amazon-dynamodb/)

# Module 9 : Compute

## Demo

* Show cold start (execute a lambda twice. Second time log in cold start section will not run)
* Docker Container and Lambda
* Layers
* Aliases with API Gateway. included in API Gateway Canary Demo

* AWS lets 30 min. to demo the lambda
* We can take time to show 
  * cloudwatch metrics / logs
  * environment variables
  * aliases / versions
  * take time to show how it looks like, all the different tabs

## Lambda code

### Stream of event 

it's possible to get a stream of event, in a sense of input stream / output stream. This way the client can serialize the event like he wants to. For example we can stream the event to convert it directly to an object. There's an example [here](https://docs.aws.amazon.com/lambda/latest/dg/java-handler.html#java-handler-interfaces)

### Advice

* Decouple business logic from lambda handler. The idea is to decouple lambda handler which is bind to lambda context from business logic. This way, it's easier to unit test the code, no need to reference anything related to lambda in the test code.

## Lambda limits

* nb layers : 5
* package size (**layers included**) : 50 Mb zipped, 250 Mb unzipped
* container image code : 10 GB
* payload size (Not adjustable)
  * synchronous : 6 MB
  * asynchronous : 256 Ko

## Layers

* Python : ideally, create a wheel file, but a simple script file can be part of a layer
* Java : create a JAR
* .NET : Runtime Package Store feature. It takes as input a .csproj that lists all dependencies. [More on that](https://aws.amazon.com/blogs/developer/aws-lambda-layers-with-net-core/)

## Extensions

* An internal extension can be used to add capabilities directly to the handler code because it runs in the same process. For example intercept all http calls to log them or add some headers or anything
* An external extension does not run within the same process, it works asynchronously, and so it does not impact function performance
* Lambda extension comes as a **lambda layer**
* Third parties extensions
  * Dynatrace, datadog, etc... provides external extensions to add monitoring metrics, traces, etc..
  * Hashicorp Vault : extension to make available passwords to lambda, without making lambda code aware of Vault
  * AWS : AppConfig, Lambda Insights, ADOT, AWS Parameters and secrets, CodeGuru Profiler (analyze code performance and provide recommendations)

## Permissions

* In push mode (synchronous / asynchronous), resource based policies must be updated to authorize the event services (S3, SNS, APIGw) to invoke lambda
* In pull mode, it's the execution role that must be updated -> because it's the lambda the fetch the service

## Concurrency

* Reserved Concurrency : maximum number of concurrent instances allocated to the function. It's to avoid throttling, for example if a maximum quota account have been reached. No other function will be able to use the reserved concurrency. Use it for critical lambda functions that cannot afford to fail because of that reason. Incurs **NO** additional charges.
* Provisioned Concurrency : it's the number of instances to pre-warm, to avoid cold start penalty. Incurs additional charges

# Module 10 : Gateway

* [Difference between HTTP API and REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-vs-rest.html). To resume, HTTP API is more basic but cheaper
  * no WAF integration
  * no Edge location (only regional)
  * no X-Ray tracing
  * no request validation / request body transformation
  * no cache
  * no canary release
  * no api keys, no quotas, no throttling
* Etudier comment fonctionnent les websockets de manière macro sur l'API Gateway
* API Gateway swagger extensions

## Demo

* Canary release
* Swagger import/export. Swagger extensions are showed in Lab 6
* Query validation. Shown in Lab 5

# Module 11 : Micro services

* Strangler Pattern diagrams
* [Saga Pattern with step function](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-the-serverless-saga-pattern-by-using-aws-step-functions.html)

## Demo

* Step functions

# Module 12 : Access

## Demo

* Webapp with user pools and identity pools
* Explore the [React sample](https://docs.aws.amazon.com/cognito/latest/developerguide/getting-started-test-application-react.html) provided by AWS

## Oauth 2.0

* Expliquer les différents mode d'authent : Client Credentials, Implicit (pourquoi ce n'est pas secure), Authorization Code

## Cognito

### App Client

A an app client is a configuration specific to a mobile or web application

settings at app client level

* analytics
* hosted UI (self-managed Cognito users)
* resource servers and custom scopes
* Threat protection (action you can define if account is compromised). This can happen when users reuse credentials at more than one site, or when they use insecure passwords
* Attribute read and write permissions (ability to read or write user attributes from your specific application)
* Token expiration and revocation
* Authentication flows
  * public client (no secret required) to interact with Cognito
  * confidential client (client secret required)
  * client secret (a fixed string that your app must use in all API requests to the app client)

 ### Scopes

 * scopes are linked to an app client, not possible to associate a user or a group to a scope.
 * scopes can seggregate permissions between applications, not end-users.

# Module 13 : Devops

## Demo

* Rancher Desktop not compatible with sam invoke. Can only demonstrate sam local generate-events for example
* Can show a SAM template with deployment of a serverless API, a serverless function and a simple table

# Module 14 : Debug

## Demo

* Logs insights
* X-ray is shown in the lab