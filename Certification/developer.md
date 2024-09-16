# IAM

* GetSessionToken used to input MFA credentials and retrieve temp credentials. It must be called with long-term user credentials.

# AWS CLI

* For pagination use
  * --page-size
  * --max-items
  * --starting-token


# EC2

* Multi volume snapshots can snapshot all or part of an EC2 instance. So Resource Type must be Instance when starting a snapshot from the console
* to enable detailed monitoring

```
aws ec2 monitor-instances --instance-ids [instances-comma-separated-list]
```

## EC2 instance connect

* Necessary steps
  * Configure IAM roles to be able to connect with Instance Connect
  * Open Inbound SSH on SG
  * EC2 instance connect must be installed on instance (manual install or use an AMI where it is already installed)
  * Optionally install EC2 Instance Connect CLI locally if connection is not browser based


## Capacity Reservations

* Capacity reservation can be shared accross all accounts whether on the same organization or not.
* Capacity reservation is only supported for Zonal instances, not regional instances
* Capacity Reservation implies no discount and no commitment. It's just a feature to guarantee availability on some EC2 instances types on need. But there are additional charges during the time of reservation (same pricing that if EC2 was up and running).
* Suppose you have Reserved instances. You release the EC2 instance so that anyone else can take benefit of the discount, he will have the guarantee they will be able to provision such instance, particularly if they are on a highly demanded EC2 instance.

## Reserved Instances

* It's possible to queue purchase of reserved instances, to be sure reserved instances will be covered without any interruption.
* Can be queued only on Regional Reserved Instances (not Zonal) and not for Reserved Instances from other sellers than AWS. 

## Dedicated host recovery

* Dedicated host recovery is a feature that automically recover dedicated host in case of issues like
  * Loss of network connectivity
  * Loss of system power
  * Hardware or software issues on the physical host
* The old Dedicated host will not be released if some instances like using instance-store are running on the physical host. Manual recovery must be made in this case (manual copy of the data for example).

# SQS

* To change Visibility Timeout

```
aws sqs change-message-visibility --queue-url myQueue --receipt-handle MyReceipt --visibility-timeout 30
```

* user SQS Extended Client Library to manage payload on S3 (if payload exceeds 256 Ko). Available in Python or Java
* DLQ and Standard queue must reside in same region and account and must be of the same type (Standard or FIFO)
* Create Delay queues to delay the delivery of message to consumer. It's a queue with the Delivery Delay set to something > 0


# ECR

* to retag docker images, use put-image and --image-tag option

```
aws ecr put-image --repository-name myRepo --image-manifest manifest.json --image-tag myImageTag
```

* enhanced scanning to use inspector and activate continuous scanning. Must specify filter, without it, no images will be scanned
* use **docker manifest push** instead of **docker push** to push multi architecture images

# CodeDeploy

* Lifecycle
  * ApplicationStop
  * BeforeInstall
  * AfterInstall
  * ApplicationStart
  * ValidateService
* If deployment log file has been deleted, codeDeploy service must be restarted to create a new one
* No need to install agent when using with ECS or Lambda. Only EC2 or On-premise requires Agent.
* To deploy an ECS task, the required params are container name, container port and task definition

# Code Build

* Phases
  * Install
  * Pre_build
  * Build
  * Post_build

* For each phase, we give parameters
  * run-as (linux user name)
  * on-failure (ABORT or CONTINUE)
  * commands (all commands to run)
  * finally (run even if a command fails)

* custom images can be pulled from ECR, Docker hub or any private registry
* CodeBuild doesn't cache the image
* you can use CodeBuild Agent, which is a local version of CodeBuild, to quickly debug an issue in the build

* CodeBuild can cache the artifacts either on S3 or in local.
  * Local stores the cache in the container host. It should be used when the build are very frequent, and the artifacts are big in size. [Doc is here](https://confluence.eulerhermes.com/pages/editpage.action?pageId=228559429)

# CodePipeline

* code pipeline can have multiple stages. Each stage can have multiple actions that can be run in parallel.

# XRay

* -o option to run daemon locally (not on EC2 instance)

```
~/xray-daemon$ ./xray -o
```
* X ray can work cross-regions
* to configure it cross account
  * Configure X-Ray daemon to use an IAM instance role
  * Create a role in the target account and allow roles in each sub-accouts to assume it.
* Enable **Active Tracing** when there is no upstream service that has x-ray activated
* Trace header is excluded from SQS message size. It's not part of a message content, but is part of a default http header
* Lambda environment variables
  * _X_AMZN_TRACE_ID : Contains Tracing Header
  * AWS_XRAY_CONTEXT_MISSING : determine behavior when trying to log data to x ray but tracing header is not available
  * AWS_XRAY_DAEMON_ADDRESS : address of x ray daemon to send directly to xray without using SDK
* Default Sampling rule : One request per second & 10 % of any additional request / host
* there are [filters](https://docs.aws.amazon.com/xray/latest/devguide/xray-console-filters.html) that can be used in the console to filter X Ray traces
  * **Service** keyword takes all traces generated by a specific service
  * **edge(ServiceA, ServiceB)** select all traces between A and B
  * **annotation\[key\]** filters by annotation
  * **group.name** or **group.arn**
* to work on ECS
  *  X-ray agent must be deployed as a **sidecar**
  *  A correct IAM **task** role must be provided

# Beanstalk

* for custom platform, needs to specify AMI and associated region
* cron.yaml file must be provided if a worker must also run periodic tasks
* Beanstalk creates a new version of application each time a new code is uploaded. Packages are stored on S3 and must be explicity deleted if needed (Lifecycle policies)
* Configurations (in .ebextensions) and code must be provided in a single zip file
* ElasticBeanstalk does not manage any Cloudfront distribution, though it can be created apart.

# DynamoDB

* for TTL, any field name can be chosen for the expiry timestamp
* can use DynamoDBCrudPolicy policy to give access
* On a Query, it's possible to return Consumed Capacity. 3 values can be provided
  * NONE (default)
  * TOTAL (amount of RCU)
  * INDEXES (amount of RCU for each table and index that was accessed)
* DynamoDB Streams are in near real time. To process them in real time, they must use Kinesis Adapter.

## Locking

* Optimistic Locking
  * update based on a version number. Only can update the item if the version has not changed. Prevents changes that can be made by others.
* Pessimistic Locking
  * It locks the object in the database, preventing users to update it. This operation can interrupt user operations.
* Overly optimistic locking
  * for scenarios where there is no concurrency on a single item. No checks are performed.

# Kinesis 

* IteratorAge (now deprected in favour of **IteratorAgeMilliseconds**). Time difference between now and last GetRecord call to the stream. This can indicates that consumer is lagging to process all messages 

# Lambda

* MobileSDK can be used to get easy information on devices using Context object.
* Weighted alias : percentage is a number between 0 and 1
* When processing an SQS queue, property ReportBatchItemFailures helps re-processing only items that have failed when processing a batch of items
* When publishing a new version, must specify the current version id. This is to prevent multiple developers publishing versions at the same time that results into conflicts.
* multi-architecture container images are not supported for Lambda with Docker
* By default, there's a limit of 1000 concurrent executions for all lambda functions in an account (can be increased to 10 000s)
* Lambda will keep at least 100 executions unreserved. Max reserved concurrency by default is 900 executions.

# Exceptions

Status Code 429 is for Too Many Requests. Raised when some services are throttling.

# S3

* Object Lock is tied to a specific version of an object
* Expedited Retrieval is not possible from Glacier Deep Archive.
* PrincipalOrgPaths condition in Principal to control access to a specific OU
* Consistency model
  * if you delete a bucket and immediately list all buckets, the old bucket might still appear in the list
  * After a successful write of a **new** object, OR an **overwrite** or **delete** of an existing object, any subsequent read request immediately receives the latest version of the object. 
  * strong consistency for list operations. After a write, you can immediately perform a listing of the objects in a bucket with any changes reflected. 

# Fault Injection Simulator

Template : 
  * Action Set
  * Targets
    * Can specify AWS Resources with Ids, Tags or Resource Filters
  * Stop Conditions

# Certificate Manager

* [Certificate Revocation](./devops.md#certificate-revocation)


# SNS

* Delivery Policy can be set at topic or subscription level
* Delivery Policy aims to deliver failed messages to a DLQ (SQS)
* DLQ and subscriptions must be created in the same region

# SAM

* to deploy locally in integration tests, run

```
sam local start-lambda
```

* to deploy localy and test manually, run 

```
sam local invoke
```

# KMS

* LocalCryptoMaterialsCache is provided by AWS SDK and help caching data keys for reuse.

# Parameter Store

* to get a secret string decrypted or unencrypted use flag

```
--with-decryption | --no-with-decryption
```

* parameter store params can be shared accross accounts (from Feb 2024)

# ELB

* Cross-Zone Load Balancing is always enabled by default for **ALB**
* When ALB does not have any registered target group, it throws an 503 exception (Service Unavailable)

# Billing And Cost Management

* IAM User access must be explicitly activated in Billing and Cost Mgt to allow Users to see the data
* AWS requires approximately **5** weeks of usage data to generate budget **forecasts**

# ASG

* Target Tracking Policy does not support directly scaling based on ApproximateNumberOfMessages. But it's possible to calculate a custom metric taking account of ApproximateNumberOfMessages, Number of instances in ASG, and acceptable backlog size per instance to use target tracking. More details [here](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-using-sqs-queue.html)

# Caching

* a flavor of mix of lazy loading and write through caching strategy, is to write the data in the backend and invalidate the cache, instead of just setting a TTL to the key. It can lower the amount of memory the cache uses, by only storing the keys that are effectively used

# CloudFront

* Failover
  * routes all incoming requests to the primary origin, even when a previous request failed over. It only sends requests to 2ndary after a request the the primary fails.
  * Only failover on GET, HEAD or OPTIONS method.
* CloudFront functions works only on a viewer request, not for an origin request. Lambda@Edge are the only option in this case. 
* Viewer requests are triggered before getting data from the cache or just after retrieving data from the cache.

# API Gateway

* charged only for method-level metrics, not for stage or API-level metrics.
* For enabling Cloudwatch method level metrics, 
  * you have to provide a specific IAM role that enables API Gateway to write to CloudWatch Logs.
  * you have to enable STS for the region
* The cache can be invalidated by the client by setting an HTTP Header. Authorization can be activated to allow only specific users to invalidate it.
* an API Key must be associated with a usage plan to gain access. The usage plan defines on what API, stages, methods it operates. To associate api keys with a usage plan , use **CreateUsagePlanKey** operation

# ECS

* Cluster Queries are expressions to group objects by AZ, instance type, or any custom attribute that can be set at container instances.
* Task Placement Constraints : define which instances will be used for tasks. At least one instance must match the constraint.
  * distinctInstance : Place each task on a distinct instance
  * memberOf. Place task on container instances that satisfy an expression (can use custom attributes and cluster queries)
* Task Placement Strategies
  * binpack (save mximum resources): can be configured with CPU or Memory
  * random
  * spread (by instances id, or AZ)
* When managing EC2 instances, if an EC2 instance is terminated while it was in stopped status, ECS will not deregister it from the cluster automatically, you have to do it explicitly with the CLI.

# Cloudwatch

* it's possible to change the KMS key associated to a log group, but it must be done with the CLI only