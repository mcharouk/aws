# CodeCommit

## Security

* PowerUser : access to all functionalities except deleting repositories and resources associated (CloudWatch logs for ex.)
* By default, encrypted at rest and at transit
* approval rule templates can be created to specify who can validate pull requests and number of validation required
* Supports tag conditions in iam policies
* Branch Security (IAM to specify actions authorized on a specific branch)


## Events

* CodeCommit can send notifications on **SNS** or **AWS Chatbot** on git actions (branch, comments, pull requests changes). EventBridge can catch those events too. The target resources must be in the same region than CodeCommit. 
* Repository events (like cloning a repo, or commiting) are not tracked by **Notifications**. To catch those events, a **trigger** must be used with a Lambda function

## Cross region replication

* Cross region replication with Lambda and ECS Task for low latency. ECS Task clone the repo and push it to another region.

# CodePipeline

* Source, Build, Test, Deploy, Invoke
* Artifacts on S3
* Manual Approval trigger SNS notification
* multi region : codepipeline must have permission on every region. It handles the copying of input artifacts from one region to the other.
* Parallel jobs : all jobs must have the same **runOrder** property. They must be included in the same action group.
* working with CloudFormation, it's possible to override parameters, used if parameters are unknown before the pipeline starts
* There is no cloudwatch metrics for codepipeline. Monitoring is done via Cloudtrail or EventBridge
* When copying artifacts to and from s3 with source and destination in different accounts
  * S3 source bucket must be encrypted with a customer managed KMS key
  * S3 source bucket must have versionning enabled

# CodeBuild

* VPC, KMS integration, Parameter Store, Secret Manager
* Support Java, Ruby, Python, Go, Node.js, Android, .Net, Php
* Managed images
  * Ubuntu
  * Windows Server
* Custom image
  * Docker image
* Supports ECR in another account : just provide the full URI of ECR registry
* Phase : install, pre build, build, post build
* Artifacts (S3) and cache
  * S3 needs to have versionning and encryption enabled
* Can be triggered by a WebHook (From Github for example)
* Pattern that add a comment in a pull request when it fails (with EventBridge and Lambda)
* Test reports in following format
  * JUnit XML, NUnit XML, NUnit3 XML
  * Cucumber JSON, TestNG XML, Visual Studio TRX



# Code Deploy

## Deployment groups

* Deployment group can be based on tag resources only for EC2. Works with EC2 ASG, EC2 instances and on-premises instances.

## Deployments mode

### Lambda

  * Linear : Add X % every Y min
  * Canary : Test X % then switch to 100 %
  * All At once

### ECS

* (Only Blue/Green). Use Weighted target groups 
* Linear
* Canary
* AllAtOnce

Note : CodeDeploy Agent is not required

### EC2
* HalfAtATime
* OneAtATime
* AllAtOnce
* Custom

* Blue/Green
  * managed by tags either on EC2 or on ASG (better as it's dynamic)
  * BlueInstanceTerminationOption to notify if blue env should be destroyed after release
  * ActionTerminate : Specify how long blue env must be kept alive

!! No Canary, No Linear !!

* an appspec.yml file must be provided to specify
  *  what should be deployed in the instance
  *  what lifecycle hooks to run in response of deployment events

## Deployment hooks

### Lambda

* BeforeAllowTraffic
* AfterAllowTraffic
 
### ECS

* BeforeInstall
* AfterInstall
* AfterAllowTestTraffic
* BeforeAllowTraffic
* AfterAllowTraffic

### EC2

  * Hooks when Blocking Traffic
    * BeforeBlockTraffic
    * AfterBlockTraffic
  * During installation
    * ApplicationStop
    * BeforeInstall
    * AfterInstall
    * ApplicationStart
    * ValidateService
  * Hooks when Allow Traffic
    * BeforeAllowTraffic
    * AfterAllowTraffic

## Troubleshooting

* InvalidSignatureException – Signature expired: [time] is now earlier than [time]
  * Time must be set correctly on EC2 instance

## Deployment Process

* By default on EC2, CodeDeploy removes all files of previous deployments to install a new version. 
* For files that were not installed by previous deployments but are there (for example added manually), it's possible to specify what to do with them
  * Fail the deployment
  * Overwrite the content
  * Retain the content

## On Premises

* on an OnPremise instance, CodeDeploy [can be used with an IAM Role](https://docs.aws.amazon.com/codedeploy/latest/userguide/register-on-premises-instance-iam-session-arn.html).
  * Possible to use an IAM user but it's deprecated

* Remove a tag from an on premise instance to temporarily exclude it from deployments.

```
aws deploy remove-tags-from-on-premises-instances
```

* On premises instance should be able to run as sudo or root
* Port 443 must be opened at least to communicate with AWS endpoints

# CodeArtifact

* Nexus Like
* Can proxy a public artifact repository. Only 1 external connection per repo is allowed
* Integration with EventBridge. Can trigger a pipeline when a new version of a package is created for example
* Resource Policy for cross account access

# CodeGuru

* CodeGuru Reviewer must be associated to 
  * a repo (CodeCommit, Github, BitBucket)
  * S3

# EC2 Image Builder

* Launch by CloudFormation to create a new AMI
* Share AMI with RAM

# CloudFormation

## Dynamic references

* 60 dynamic references max (SSM PS, SSM)

## Protection against termination

* Termination Protection : protection on the stack itself, not the resources in the stack (Stack Policy for that)
* Stack Policy
  * use to protect some resources of unintentional deletion, or update
  * Must explicitly Allow (implicit deny)

* DeletionPolicy : how deleting a resource should be managed. Possible values: 
  * Delete
  * Retain
  * Snapshot
* UpdateReplacePolicy  : how updating a resource should be managed. Possible values: 
  * Delete
  * Retain
  * Snapshot

## StackSet

* a template in an admin account. 
* Can deploy in multiple accounts and regions. 
* When a stackset is updated, all children are automatically updated.
* Must delete all Stacks before deleting a stackset
* Parameters can be overriden for specific regions.
* When deleting a stack from a stackset, it's possible to retain the stack by enabling **RetainStacks** option.

* 2 permission models
  * self managed permission : Trust between master and target accounts are managed by users using IAM roles
  * service managed permission : enable all features and activate trusted access in AWS Organizations.

## Helper Scripts

Scripts to install packages on an EC2 instance

* cfn-init : install packages, create files, start services.
* cfn-signal : WaitCondition, CreationPolicy. A cfn-signal is sent when it's ok.
* cfn-get-metadata : easily get metadata from a resource
* cfn-hup : daemon to check for updates to metadata and execute custom hooks on changes

## Drift detection

* to detect a drift, values should all be explicitly defined in the template, even it's equal to the default value.
* There's a drift detection check in AWS Config. DetectStackDrift function of Cloudformation can throttle and can generate errors.
* To solve a drift manually
  * Change the resources manually to resynchronize the stack
  * *ContinueUpdateRollback* can continue the rollback even if some resources have failed. Use *ResourcesToSkip* request parameter
  * When deleting a stack, it's possible to retain resources so that the stack will not fail to delete (but the resources will have to be cleaned manually)
* Drift of custom resources are not supported


## Custom resource

* When a custom resource is triggered (lambda for ex), a **S3 pre-signed url** is included in the request. 
The resource must respond using the url to notify the step is completed. Otherwise the step will remain in CREATE_IN_PROGRESS state in cloudformation.

* Tokens can be sent to a Lambda or a SNS topic

## Intrinsic functions

* can only be used in sections 
  * resource properties
  * outputs
  * metadata attributes
  * update policy attributes

## Passwords

* NoEcho attribute to display the value with ***

## S3 interactions

CloudFormation detects a template in S3 has been changed only if one of the following has changed : 
* S3 bucket
* S3 object key
* S3 object version

## Parameters

CloudFormation can fetch the value of a parameter in parameter store.

Parameters must be one of these types : 

```
AWS::SSM::Parameter::Name   -> used to get the name of the parameter, for example to check if the parameter exist
AWS::SSM::Parameter::Value<String>
AWS::SSM::Parameter::Value<List<String>>
AWS::SSM::Parameter::Value<Any AWS type>
```


## Specifics

### Engine Version

**EngineVersion** parameter to change the engine version of RDS. This operation generates downtime, use a read replica to minimize it.

### Exception

* **Insufficient Capabilities Exception** appears when CloudFormation is triggered by CodePipeline.
* it means that stack is trying to create an IAM role but it doesn't have those specified capabilities.
* Enable IAM Capability on CodePipeline to fix the issue.


# SAM (CloudFormation)

* SAM Connectors to manage permissions (policies) between serverless services
* It's possible to instantiate also non serverless resources in a SAM template as SAM is just an extension of Cloudformation templates

# SSM

* Document : YAML or JSON, defines a set of commands
* Run Command
  * Run a document or a simple command on a set of resources (use resource groups)
  * No SSH needs
  * Rate Control / Error Control
* Automation
  * Run documents of type Automation
  * EventBridge, Maintenance Windows, AWS Config (Remediation)

# ASG

## Scaling

* predictive scaling. Forecast based on past numbers and activate automatically scheduled scaling
* Target Tracking scaling : scale on a cloudwatch metric : i want the CPU stays at around 40%
* Step scaling : based on a cloudwatch alarm : if CPU > 70 %, increase of 2 instances
* Scheduled actions : for predictive patterns

* Metrics to scale on
  * CPU
  * RequestCountPerTarget (to be sure request count per EC2 is stable)
  * Average Network In/Out (if application is network bound)

## Lifecycle
* Lifecycle scripts can be executed on Pending and Terminating states
*  Integration with EventBridge, SQS and SNS

## Termination policy

* Default Termination Policy
  * AZ with the most instances
  * select older instance
  * closest to the next billing hour

* When there is a mix instance groups (On-Demand + Spot), ASG will first determine which group to terminate.

* Customizable (Newest instances, Allocation strategy (spot for ex))

* When rebalancing, ASG creates new instances before deleting new ones. This leads to a temporary unbalanced configuration.

## Warm pools

to avoid long startup issues

* maintain pool of pre initialized instances
*  Warm Pool Instance State:  what state to keep your 
Warm Pool instances in after initialization
(Running, Stopped, Hibernated)
* they do not affect scaling policies while in the pool
* Instance Reuse Policy : instance that returns in the warm pool instead of being terminated 

## Update Policy

* It's a CloudFormation feature, related to ASG.

### Replacing Update

* Replace ASG with a new one instead of updating instances in current ASG.  
* Can Rollback to the old version in case of issues
```
{
  "AutoScalingReplacingUpdate": {
    "WillReplace" : True
  }
}
```

* CLI complete-lifecycle-action to tell cloudformation the application has been installed and can be put into InService state.

### Rolling Update

* WaitOnResourceSignals : if set to true, cloudformation will wait for a *PauseTime*. If it does not receive any signal, it will rollback
* MinSuccessfulInstancesPercent: Threshold of failed instances to rollback the stack

## Troubleshooting

* Put the instance in Standby state
* Lifecycle hook can work too but it has a default timeout of 60 min
* Suspend Health check process or terminate process might work too
* Suspending AddToLoadBalancer is possible. The instances will start, but not attached. When resuming, they will have to be attached **manually**

 ## Notifications

 ASG can send notification to SNS on some events : 

 * launch
 * terminate
 * fail to launch
 * fail to terminate

# Application Auto Scaling

* Possible to schedule scaling for Lambda Provisioned Concurrency.

# ELB

* health checks don't work with payload regex, only https status codes.


# Cloudwatch

## Subscription filters
  * OpenSearch (don't need to use Firehose for that !)
  * Kinesis (Stream or Firehose)
  * Lambda

!!! cannot stream on S3 but can periodically export to S3 !!!

## Retention

* Metrics are retained for 15 months max.

## Connectors

* Alarms cannot trigger a Lambda function. SNS must be set as an intermediate step to trigger a Lambda.

## Cross-account observability

* easily share logs of multiple accounts to one single centraliazed account
* include CloudWatch logs, metrics and X-Ray traces
* This can be setup by adding manually accounts or through AWS Organizations.

# AppFlow

* Transfer data from SAS partners (like SalesForce, SAP, ZenDesk) to AWS Services (S3, Redshift)

# App Runner

* a service to easily deploy containerized application. 
* No need to manage autoscaling groups, load balancers. Very managed.

* can take source code from ECR or GitHub

# App2Container 

* Identify processes that can be containerized
* Analyze Runtime dependencies (processes and network ports)
* Migrate a legacy application in a container. 
* Create a CI//CD Pipeline
* Deploy on App Runner, ECS or EKS
* Generate CloudFormation templates for infrastructure


# Elastic Beanstalk

## Configuration Priorities
The properties are applied in this order (most prior to least)
* Settings applied directly to the environment (API)
* Saved configurations
* Configuration files (.ebextensions)
* Default values

## ebextensions

  * **packages** : install libraries. installation order within a package manager isn't guaranteed. Supported package manager : 
    * Yum
    * RubyGems
    * python
    * rpm
  * **groups** : creation of unix groups
  * **users** : creation of unix users
  * **sources** : unpack a source from a URL in a target directory
  * **files**  : create files. Content taken from a URL or from inline content
  * **commands** : run before webapplication and servers are setup
  * **services** : start or stop a service when instance is launched
  * **container_commands** : can be launched after servers has been set and just before application version is deployed


## Configuration

* leader-only flag used to launch the script only on a single instance

* By default, Beanstalk uses EC2 with non persistent local storage. For persistent storage (like EBS), it has to be explicitly configured.

* Dockerrun.aws.json (v2) is a file used to describe multi container applications. an ECS task is created for each container.

* cron.yaml works only in a worker mode, not in web server mode

## Monitoring

* Beanstalk has a enhanced health reporting & monitoring feature
  * Capture system and web server metrics
  * Provide a colour that describe the overall status of the stack.

## Version lifecycle policies

EB versions are not deleted by default.
Lifecycle policies can be used to automatically remove them.

## Blue/Green

There is no Blue/Green option in Beanstalk. 
* Application have to be deployed on 2 Beanstalk environments 
* a CNAME swap can be initiated with CLI. 
* The swap option is not supported by CloudFormation.


# ECS

* Using **latest** tag does not ensure to use latest version as images won't be updated if a new version is released. Restart ECS agent for that
* It's possible to refer to the SHA-256 digest of the image but it's an explicit reference to the image. It's not dynamic like latest
* with awslogs driver, policy to write in CloudWatch must be defined at instance level, not task level.
* To redeploy on a new ECS platform version, select **Force New Deployment** at the ECS service level

# API Gateway

* API Gateway does not integrate directly with an ALB. A NLB must be used as intermediate.

# DynamoDB

* Kinesis can be used instead of Streams. They are suited for massive scale.

# X Ray

to install X Ray on an ECS Cluster

* XRay communicates on UDP 2000
* Install X Ray daemon in a docker image and deploy it in the cluster as a daemon. 
* Use port mappings and network modes so that applicative tasks can communicate with X-Ray image

# EventBridge

## Targets

(not exhaustive)

* Processing
  * API Gateway
  * API
  * **ECS Task** 
  * Lambda
  * Glue
  * StepFunction
* Notification
  * EventBus (EventBridge)
  * Kinesis Firehose
  * Kinesis Stream
  * SNS 
  * SQS
* CI/CD - Automation
  * CodeBuild
  * CodePipeline
  * System Manager Automation / Run Command
* Logs
  * **CloudWatch Log Group**
* EC2
  * **EBS CreateSnapshot API**
  * **EC2 Terminate/Stop/Reboot**
* Security
  * Inspector

**!!! Note there is no S3 as direct target !!!**

## Object-Level events

* To receive object level events (like S3 PUT or GET), CloudTrail must be configured to track these data events.


# Macie

* Discover sensitive data on S3
* Detects Risk of unauthorized access or inadvertent data leaks


# OpsWorks

## Overview

* Stacks are group of resources constituting a full stack application
* Stacks are composed of layers. It's a group of EC2 that serves a purpose. Ex : DB, Backend, Frontend...
* Layers have a lifecycle. Custom cookbooks run in a lifecycle event 
  * Setup
    * Occurs after an instance is finished booting
  * Configure
    * instance enters or leaves the online state
  * Deploy
  * Undeploy
  * Shutdown
  
* Recipes are provided at stack level. Custom cookbooks can be provided but the corresponding option must be checked

* By default, 5 mins waiting for an EC2 response before considering it as a failed instances

* OpsWorks supports deploying containers

* When attaching an existing ELB to OpsWorks, it de-registered all the instances attached to it.

* A stack cannot mix Windows and Unix instances, but both are supported separately

# IAM

* IAM access advisor can be used to see the last time a policy or a service has been used and by which entity

# CoPilot

* init : create an application
* env : create an environment
* services : long running ECS services
  * Front end services
    * Request-Driven Web Service : App Runner
    * Static Site : S3 + CloudFront
    * Load Balanced Web Service : ELB
  * Back End service
    * Internal Load Balancer
  * Worker
    * Pub/Sub pattern
* jobs : ECS scheduled jobs
* pipelines : CI/CD pipelines 


# AWS Proton

* a service to create standardized templates. Developer provides the code, select the template, and application is deployed.
* to be used for containers or serverless applications

# AWS Config

* Config push all the changes to SNS, not possible to filter the events at a fine grained level. EventBridge can do that.

# ACM

* ACM can be used to publish private certificates.

## Certificate Revocation

### CRL Entries

  * CRL entries are deployed on an S3 bucket-> disable public access, read S3 through CloudFront. 
  * The client download the CRL entries and process it in local. 
    * Consumes more memory
    * revocation can take 60 minutes to be broadcasted.
    * As the list can be cached, it can contain stale data.

### OCSP
  * notify endpoints they have been revoked without the need for customers to operate infrastructure themselves
  * It's an URL to call to know if certificate has been revoked. The client browser will call the endpoint. 
  * A custom URL can be provided for custom branding or custom security considerations.
  * Consumes more bandwidth
  * revocation can take 30 min to be broadcasted.

# S3

## Lifecycle policies

* it's possible to add a filter rule based on a tag or prefix (or combination)

## Integrity validation

* 2 methods to validate integrity
  * Provide MD5 digest in Content-MD5 parameter. 
    * AWS will check that the MD5 of the target object is the same.
  * Examine the object ETag. 
    * Check the value is the same than a MD5 kept in local. 
    * ETag change only if object change. Metadata changes does not impact ETag.

* Checksum of a multipart upload is not the checksum of the entire object, but a checksum based on its individual parts checksum.

# Service Quotas

* a service view and manage quotas from a central point
* integrates with AWS Organizations (must enable trusted access between 2 services)
* integrates with Cloudwatch to warn when quotas are about to be reached.

# SQS

* scaling integrates the number of messages visible per instance (backlog per instance)
  * use cloudwatch metric ApproximateNumberOfMessagesVisible
  * divide this metric by the number of EC2 instances in InService State
* compare this metric with the acceptable backlog per instance
  * acceptable latency / average time it takes to process a message

Ex : 
* 0.1 s to process a message and 10 s is the max acceptable latency = 10 / 0.1 = 100  messages per instance.
* compare 100 messages with ApproximateNumberOfMessagesVisible / nb of instances
* if the value is > 100 then trigger a scale out event
