# Certificates

* a wildcard certificate can only match sub domains but not different domain names
* To service multiple domain names on the same ALB for example
  * associate multiple domain to an ALB listener by uploading all SSL certificates to the listener
  * For Cloudfront
    * use Cloudfront SNI (works only for browsers that supports it)
    * use dedicated IP Address for each domain (work for all browsers)

# IAM

* to allow an account of an external organization to access a service in our org, it's a best practice to use an external id.
* The external account will have to provide the external id to assume the role. It's meant to avoid the Confused Deputy problem. The external id is somehting that must only be known by the two parties and should not be easy to guess by other parties, acts pretty much like a password, or an api key.

# Proton

* Templates to deploy infrastructure for serverless and container-based applications
* looks like Service catalog, as we can see who uses an outdated template and update it on one-click. 
  * But in Service Catalog, only consumers can update their product
  * In Proton, Administrator can update the product used by consumers
* Administrators provide an environment template to create an environment
* Developers provide a service template to create a service deployed on an environment
* Proton is meant to deploy a full application (infra + service), Service Catalog focuses more on infra
* Note that Proton templates could use a service catalog product

# Route 53

## Health Check Types

* HTTP
* HTTPS
* TCP

## Resolvers

* By default Route53 can resolve all AWS default domain names and Private hosted zone domain names
* Outbound resolvers are needed to resolve any other kind of domain
  * On Premise domain names
  * Custom domain names inside a VPC (for example on a self hosted DNS, or domain name of a Managed Active Directory Service)
* For that, create the outbound resolver, and create a forwarding rule.
* There is also a notion of Conditional Forwarder, which is specific to AD. It's meant to establish a trust relationship with another AD.

## Application Recovery Controller

* it's a service that uses Route53 health checks.
* it's made for complex failover scenarios, multi AZ or multi Region
* it monitors the application as a whole not just a components individually
* it offers a on/off switch to failover which provides more control on failover scenarios
* Main components
  * Routing Controls: On/off switches hosted on a cluster that manage traffic to cells. They are integrated with health checks in Route 53 and act as the primary mechanism for controlling traffic flow
  * Control Panels: Groups of related routing controls that allow for organized management of routing decisions. The default control panel is created automatically when a cluster is created.
  * Safety Rules: Added to routing controls to prevent unintended consequences during recovery actions. These help ensure that traffic routing changes are made safely
  * Readiness Checks monitors recovery environment 
    * Resource quotas
    * capacity
    * configuration for multi-Region applications
    * suggest remediation when needed
  * Recovery Groups: Collections of resources that are recovered together during a failure event

# Service Catalog

* launch constraints
  * constraints on the iam role that can execute the template
* template constraints
  * restricts parameters that can be provided to a template
* stack set constraints : select the account and regions where the stack could be deployed
* Tag options

# IoT

* TwinMaker
  *  create virtual twins of a physical device to update or get information, even when physical device is disconnected
  *  create digital twins applications, for instance dashboards embedding 3D scenes with Grafana.
* Device Management
  * Device Registry (Things)
  * Things groups (static or dynamic)
  * Remote Management
  * Monitor status
* Device Defender
  * Auditing : proper device identity, authentication, and data encryption
  * Threat detection : identify unusual device behaviors
  * Alerting
* IoT rules
  * works with IoT Core. Based on rules forward data on multiple backends
* IoT events
  * react to events by alerting or triggering actions. Actions consists of sending data to a backends
    * firehose, ddb, MQTT topic, lambda, sns, sqs, iotSiteWise, etc...

# Amazon Detective

* Security investigation service that helps analyze, investigate, and identify the root cause of security findings or suspicious activities in AWS environments
* Collects data from (not exhaustive)
  *  CloudTrail logs
  *  VPC Flow Logs
  *  GuardDuty findings.
* uses machine learning, statistical analysis, and graph theory to generate visualizations and insights for more efficient security investigations.
* does not work cross-region. It aggregates data for a single region only.

# Organizations

## Accounts

* Process to move an account from an organization to another
  * Remove it from old organization to get rid of old constraints (cannot add to a new org if it still attached to the old one)
  * Add account to the new organization
  * reconfigure IAM roles, policies and security settings to align with new org.
  * For policies, need 2 actions
    * organizations:DescribeOrganization
    * organizations:MoveAccount

* Only 2 ways to add accounts to an organization
  * create an account within the org
  * send invitation to existing account to join the org

* There are only 2 options
  * Consolidated Billing : unlock only consolidated billing
  * All features : unlock all features that works with Organizations such as SCP

## Services

* you can enable or disable trusted access so that a service can retrieve information about the accounts, root, OUs, and policies for your organization
* This allows a service to work cross account, integrated to the organization
* AWS recommends to activate this feature by acting on the specific service API / console, instead of activating it on Organization console
* For instance for RAM to use Organization, use enable-sharing-with-aws-organization cmd in RAM client API.

## Backups

* Backup policies allow you to centrally manage and apply backup plans to the AWS resources across an organization's accounts.
* It creates immutable backup plans in the selected OU or accounts
* It's possible to specify partial backup policies, that will be completed by policies provided in child OUs.
* Effective way to manage backups centrally

## Tag policies

* Tag policies helps to have compliant tag values
* still a SCP is necessary to make the tag mandatory

# CodeCommit

* to detect access keys in codeCommit, multiple options
  * CodeGuru Reviewer
  * Lambda triggered on each commit that check the code with open source libraries
  * CodeBuild step instead of lambda

# CloudFormation

* CodePipeline can trigger directly CloudFormation from a pipeline, which is enough in non prod env.
* You can run a CodeBuild step with a tool like TaskCat to test cloudformation changes before deploying them
* In production env, you may want to use CodeDeploy with Cloudformation to monitor the release, to perform blue/green deployments, etc...


# RDS

## Multi AZ with Read Replicas

* [Article](https://aws.amazon.com/blogs/aws/amazon-rds-multi-az-db-cluster/)
* Use 2 read Replicas instead of a Multi AZ instance. 
  * At least one read replica will be replicated synchronously (a tx is committed if at most one replica has replicated the data)
* Benefits
  * write operations are faster (because of hardware behind the scene, and because they write to a local storage, not an EBS volume)
  * failover typically faster (lt 35 s vs 60-120s)
  * MultiAZ instance can be used for read operations like a read replica
  * replication is faster

## Read Replicas

* Read replica cannot be instantiated on premise
* to replicate on Prem, use DMS
* It's possible to use RDS on VMWare to instantiate a RDS on premise. But it's not just the read replica, it's the whole setup

# Config

* if rules targets a global service (IAM for example), it should be deployed only on a single region

# VPC

## VPC Flow Logs

* Possible targets
  * S3
  * Cloudwatch
  * Data Firehose

## Ipv6

* no need to recreate the VPC to add an IPv6 Cidr block
* For public subnets, change route table to add Ipv6 cidr blocks to redirect to IgW
* For private subnets, eventually add route to egress-only IgW
* Must explicitly add IpV6 addresses to existing instances.

## VPN With Direct Connect

* Only 2 options
  * Connection with Public VIF
  * Connection with Transit VIF
  * Not possible with Private VIF

# Beanstalk

## Managed Platform updates

* It's a managed feature to update infrastructure
* Can choose update level
  * Minor versions and patches
  * Patch only
* Can choose maintenance windows

## Custom domains for Cognito

* when this option is enabled, it creates a cloudfront distribution with an associated ACM certificate.
* To update the certificate, 2 options :
  * remove custom domain name for Cognito. This will remove Cloudfront distribution
  * remove association between ACM and Cloudfront, by updating ACM certificate. Old certificate can be deleted afterwards.

# Migration

* Application Discovery **Agent** can only send data to Application Discovery **Service**, not to S3 directly
* Agentless requirements
  * IAM User that can export data to AWS Service
  * On-premise firewall to open outbound traffic to AWS

# DMS

## Encryption

* replication instance volume is encrypted and it cannot be disabled.
* By default, it uses aws/dms key but client can provide a custom KMS Key

# Authentication

For SAML IdP, here is the process:

* get SAML metadata document from IdP
* create SAML IAM Identity Provider in AWS console
* Configure trust relationship
* create SAML assertions for authentication response 

# Secret Manager

## Rotation strategy

* Single user
  * one user, one password. 
  * There is a short time period where db password changes and secret manager is not updated yet.
  * Automatic retries will normally be enough to recover
  * Fit to most common use cases
* Alternating users
  * two users are created. One previous, one current
  * the secrets are updated alternatively.
  * Less chance to have deny response because of password

# S3

* to activate Object Locking, a new bucket must be created

# Aurora

* Write forwarding
  * secondary clusters **forward** SQL statements that perform write operations to the **primary cluster**.
  * primary cluster updates the source and then propagates resulting changes back to all secondary AWS Regions.
  * This way, the primary cluster is the source of truth and always has an up-to-date copy of all the data



# Lambda

* memory used and allocated is only available in lambda logs, not in metrics
* Lambda burst concurrency is about 500-3000 requests per second (depending on the region). Make sure it's enough for your usage. 
  * If you receive 100 requests/sec, and the average duration of each invocation is 1s, then the nb of total exec env is 100.
  * If you receive 100 requests/sec, and the average duration of each invocation is 500ms, then the nb of total exec env is 50.


# KMS 

* suppose there is only one user that is declared as admin of a KMS key
* If the user leaves the organization, the only way to take back control of the key is to contact AWS Support
* Even root user cannot fix that

# Licences

* Trust Advisor can make some licensing checks on SQL Server instances

# CloudFormation

* Stacksets can be deployed across individual accounts or regions
* integrated also with AWS Organizations, to deploy on all accounts of a OU for example

# Timestream

* Memory storage
  * High throughput **writes**, fast point in time queries 
* Magnetic storage
  * Low throughput **writes**, fast analytical queries, long term storage

# EC2

## AMI

* how to create an AMI from existing EC2
  * command ec2-bundle-vol
  * upload bundle to S3 : ec2-upload-bundle
  * register AMI : register-image

## Placement group

* Not necessary to restart the whole placement group to add a new node to it. 
* This may be requires if an explicit error is raised, especially for cluster placement groups.
* Before moving an EC2 to or from a placement group, it must be in stopped state.
  
## Virtualization types

There are two virtualization types : HVM and PV. 

PV is more a legacy one that does not support all enhanced feature of EC2 for networking or GPU processing.
They work only on old generation.

## Hyper Threading

Intel Hyper-Threading Technology makes a single physical processor appear as multiple logical processors. Most HPC applications will benefit from disabling hyperthreading.

# Disaster Recovery

## CloudEndure

* Legacy service (replaced by Elastic Disaster Recovery)

## Elastic Disaster Recovery

* DR from an AWS region to another
* DR from On-premise to AWS
* replicates block storage to EBS
* Manage failover
* Failback capability (fallback to primary site when outage is over)
* Can recover on specific point in time
* Low RPO and RTO
* It looks like MGN but it's a different agent

# SQS

* visibility timeout can be adjusted [per message](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ChangeMessageVisibility.html) with ChangeMessageVisibility action.

# Cloudfront

* To change the cache duration for an individual file, you can configure your origin
  * to add a **Cache-Control** header with the **max-age** or **s-maxage** directive
  * to add an **Expires** header to the file.

# AWS App Runner

* It's a service that can deploy **containerized web applications** in the cloud without the need to deal with an infrastructure. 

* Manages
  * Infrastructure
  * Load Balancing
  * AutoScaling
  * Security
  * Deployment
  * Monitoring
  * Patching
  * Domain name / certificate

## Main Components

* Source: Git or ECR
* Service: The running application
* Runtime: **If using source code**, runtime environment (e.g., Python, Node.js)
* Configuration: This includes settings for building, deploying, and running your application. You can provide this through the console, API, or an apprunner.yaml file in your repository.
* Connection: If using a private source code repository, you'll need to establish a connection between App Runner and your repository provider.
* VPC Connector (optional): For applications that need to access resources in a VPC.
* Custom Domain (optional): To use your own domain name for the App Runner service.
* Pay as you go : Billing based on CPU and Memory consumption

# Athena

* Federated Query works with Lambdas to access and query external databases.

# AppFlow

* Integration Service
  * Fully managed service for securely transferring data between SaaS applications and AWS services
  * No coding required, point-and-click interface
  * Supports both batch and event-driven data transfers

* Supported Connections:
  * Source connectors: Salesforce, ServiceNow, Zendesk, Slack, etc.
  * Destination connectors: S3, Redshift, Snowflake, etc.
  * Supports bi-directional data flow for some connectors

* Security Features:
  * Data encryption in transit and at rest
  * Private connectivity using AWS PrivateLink
  * Field-level encryption for sensitive data
  * Integration with AWS KMS for key management

* Flow Configuration:
  * Trigger types: Schedule-based, Event-driven, On-demand
  * Data mapping and transformation capabilities
  * Filter conditions to control what data is transferred
  * Error handling and retry mechanisms
  
* Integration Patterns:
  * Data synchronization between applications
  * Data consolidation in data lakes/warehouses
  * Real-time data processing
  * Backup and archival of SaaS data

# Amazon Lightsail

## Key Concepts

- Lightsail is a simplified compute service that provides virtual private servers (VPS)
- Designed for simpler workloads, small websites and applications
- Fixed monthly pricing with bundled resources (compute, storage, bandwidth)

## Important Features
- Pre-configured application stacks (LAMP, MEAN, Node.js etc)
- Managed databases (MySQL, PostgreSQL)
- Load balancers
- Block storage
- Static IP addresses
- DNS management
- Automatic snapshots
- VPC peering with other AWS services

## Common Scenarios

- Small website hosting
- Dev/test environments
- Simple application hosting
- WordPress and other CMS deployments
- Small database hosting

## Limitations

- Limited scaling capabilities compared to EC2
- Restricted instance sizes
- Regional availability constraints
- Limited integration with some AWS services

# Amazon Lex

## Key Concepts
- Fully managed service for building conversational interfaces (chatbots)
- Uses automatic speech recognition (ASR) and natural language understanding (NLU)
- Same technology that powers Alexa
- Supports both voice and text interactions

## Important Features

1. **Conversation Management**
   - Intents
   - Slots
   - Utterances
   - Session management
   - Context management
   - Prompts and responses

2. **Language Support**
   - Multiple languages
   - Custom vocabulary
   - Slot type variations
   - Built-in intents
    
# Amazon Personalize

## Key Concepts
- Fully managed machine learning service for personalization
- Uses same technology as Amazon.com
- Creates custom ML models for recommendations
- Real-time personalization capabilities

## Important Features

1. **Solution Types**
   - User-Personalization
   - Similar-Items
   - Personalized-Ranking
   - HRNN (Hierarchical Recurrent Neural Networks)
   - SIMS (Similar Items)
   - Popularity-Count

2. **Data Management**
   - Dataset Groups
   - Interaction Datasets
   - User Datasets
   - Item Datasets
   - Real-time event tracking
   - Batch data import

3. **Model Training**
   - AutoML
   - Custom recipes
   - HPO (Hyperparameter Optimization)
   - Model evaluation metrics

# Elastic Transcoder

## Key Concepts
- Fully managed media transcoding service
- Converts media files between formats
- Pay-per-use pricing model
- Supports various input/output formats
- Integrated with S3 for storage

## Important Features
1. **Job Management**
   - Transcoding jobs
   - Job pipeline management
   - Job status monitoring
   - Notifications
   - Progress tracking

2. **Format Support**
   - Video formats (MP4, MPEG, etc.)
   - Audio formats (MP3, AAC, etc.)
   - Web optimized formats
   - DRM support
   - Thumbnails generation

3. **Pipeline Configuration**
   - Input/output bucket configuration
   - IAM role settings
   - Notifications setup
   - Queue management
   - Regional settings
  
# Device Farm

## Key Concepts
- Fully managed service for testing apps on real devices
- Supports mobile and web applications
- Cross-platform testing capabilities
- Both automated and manual testing options
- Pay-per-use pricing model

## Important Features
1. **Testing Types**
   - Automated testing
   - Remote access testing
   - Network configuration
   - Device state management
   - Custom test environments

2. **Device Support**
   - Physical devices
   - Multiple device types
   - Various OS versions
   - Different form factors
   - Geographic locations

3. **Test Frameworks**
   - Appium
   - XCUITest
   - Espresso
   - Calabash
   - Built-in fuzz testing


# AWS Amplify

## Key Concepts

- Full-stack development platform
- Frontend and backend development tools
- CI/CD capabilities
- Hosting and deployment service
- Framework agnostic

## Important Features
1. **Development Tools**
   - CLI interface
   - Admin UI
   - Libraries & SDKs
   - Visual Studio Code extension
   - Studio for UI development

2. **Backend Capabilities**
   - API (REST/GraphQL)
   - Authentication
   - Storage
   - Functions
   - Database
   - Push notifications

3. **Frontend Support**
   - React
   - Angular
   - Vue
   - iOS
   - Android
   - Flutter

## Common Use Cases
1. **Web Applications**
   - Single page applications
   - Progressive web apps
   - Static websites
   - Full-stack applications
   - Serverless applications

2. **Mobile Applications**
   - Native iOS apps
   - Native Android apps
   - Cross-platform apps
   - Offline-enabled apps
   - Real-time applications


