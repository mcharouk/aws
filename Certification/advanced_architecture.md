# Proton

* Templates to deploy infrastructure for serverless and container-bases applications
* looks like Service catalog, as we can see who uses an outdated template and update it on one-click. 
  * But in Service Catalog, only consumers can update their product
  * In Proton, Administrator can update the product used by consumers
* Administators provide an environment template to create an environment
* Developers provide a service template to create a service deployed on an environment
* Proton is meant to deploy a full application (infra + service), Service Catalog focuses more on infra
* Note that Proton templates could use a service catalog product

# Route 53

* health check types
  * HTTP
  * HTTPS
  * TCP


# Service Catalog

* launch constraints
  * constraints on the iam role that can execute the template
* template constraints
  * restricts parameters that can be provided to a template
* stack set constraints
* Tag options

# IoT

* TwinMaker
  *  create virtual twins of a physical device to update or get information, event when physical device is disconnected
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

* security investigation service that helps analyze, investigate, and identify the root cause of security findings or suspicious activities in AWS environments
* Collects data from (not exhaustive)
  *  CloudTrail logs
  *  VPC Flow Logs
  *  GuardDuty findings.
* uses machine learning, statistical analysis, and graph theory to generate visualizations and insights for more efficient security investigations.
* does not work cross-region. It aggregates data for a single region only.

# Accounts

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
* Agentless needs
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

# Lambda

* memory used and allocated is only available in lambda logs, not in metrics

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

* how to create an AMI from existing EC2
  * commmand ec2-bundle-vol
  * upload bundle to S3 : ec2-upload-bundle
  * register AMI : register-image


# Disaster Recovery

## CloudEndure

## Elastic Disaster Recovery
