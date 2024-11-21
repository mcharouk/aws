# Table of Contents

- [Table of Contents](#table-of-contents)
- [Module 1 : intro to cloud operations](#module-1--intro-to-cloud-operations)
- [Module 2 : Access management](#module-2--access-management)
- [Module 3 : System Discovery](#module-3--system-discovery)
  - [CloudShell](#cloudshell)
  - [AWS Config](#aws-config)
- [Module 4 : Deploy And Update Resources](#module-4--deploy-and-update-resources)
  - [Tagging](#tagging)
  - [AMI](#ami)
  - [User data scripts](#user-data-scripts)
  - [Control Tower](#control-tower)
    - [Control tower customization architecture](#control-tower-customization-architecture)
    - [Control tower account factory customization](#control-tower-account-factory-customization)
    - [Proactive controls](#proactive-controls)
- [Module 5 : Automate Resource Deployment](#module-5--automate-resource-deployment)
  - [Cloudformation](#cloudformation)
  - [Service Catalog](#service-catalog)
- [Module 6 : Manage Resources](#module-6--manage-resources)
  - [Explorer](#explorer)
  - [OpsCenter](#opscenter)
  - [AWS Chatbot](#aws-chatbot)
  - [Incident Manager](#incident-manager)
  - [Automation Document](#automation-document)
    - [Automation Document vs Step functions](#automation-document-vs-step-functions)
  - [Change Manager](#change-manager)
  - [Application Manager](#application-manager)
  - [Fleet Manager](#fleet-manager)
  - [State Manager / Maintenance Windows](#state-manager--maintenance-windows)
  - [Patch Manager](#patch-manager)
    - [AWS-AmazonLinux2023DefaultPatchBaseline](#aws-amazonlinux2023defaultpatchbaseline)
    - [Custom baselines](#custom-baselines)
- [Module 7 : Configure Highly Available systems](#module-7--configure-highly-available-systems)
  - [NLB](#nlb)
    - [Metrics](#metrics)
    - [Pricing](#pricing)
  - [Demo](#demo)
- [Module 8 : Automate Scaling](#module-8--automate-scaling)
  - [Autoscaling policies](#autoscaling-policies)
  - [License manager](#license-manager)
    - [Tag custom architecture](#tag-custom-architecture)
    - [Host resource group](#host-resource-group)
- [Module 9 : Monitor and maintain system health](#module-9--monitor-and-maintain-system-health)
- [Module 10 : Data Security and System Auditing](#module-10--data-security-and-system-auditing)
  - [Access Analyzer](#access-analyzer)
    - [Analyzers](#analyzers)
  - [GuardDuty](#guardduty)
    - [Findings examples](#findings-examples)
    - [Findings](#findings)
  - [Inspector](#inspector)
- [Module 11 : Operate Secure and Resilient networks](#module-11--operate-secure-and-resilient-networks)
  - [Cloudfront](#cloudfront)
    - [Conditional requests](#conditional-requests)
  - [ACM](#acm)
- [Module 12 : Mountable Storage](#module-12--mountable-storage)
  - [EBS](#ebs)
    - [Performance](#performance)
    - [Updating an EBS](#updating-an-ebs)
    - [Multi Attach](#multi-attach)
  - [EFS](#efs)
- [Module 13 : Object Storage](#module-13--object-storage)
  - [Express One-Zone](#express-one-zone)
  - [S3 access logs](#s3-access-logs)
  - [Glacier retrievals](#glacier-retrievals)
- [Module 14 : Cost Reporting - Alerts Optimization](#module-14--cost-reporting---alerts-optimization)
  - [Cost Explorer](#cost-explorer)
  - [Cost and Usage reports](#cost-and-usage-reports)
  - [Cost Anomaly Detection](#cost-anomaly-detection)
  - [CloudWatch Billing Alarm](#cloudwatch-billing-alarm)
  - [AWS Budget](#aws-budget)
  - [Trusted Advisor](#trusted-advisor)
  - [Cost Optimization Hub](#cost-optimization-hub)
  - [S3 costs](#s3-costs)

# Module 1 : intro to cloud operations

* Demo on Well-architected tool
* Don't deep too much on aws services specified in the slides at the end
* The story is what really changes for a sysops when he goes on the cloud
  * capacity planning / guessin
  * ephemeral environments
  
* Operational priorites
  * don't over prepare, but know your priorities
  * Share learning : share not only information, but AMI, Lambda blue prints, cloudformation stacks, etc...

* Well architected tool : story from ArchitectingOnAWS

# Module 2 : Access management

* Demo
  * PassRole
  * SCP
  * [Policy Generator](https://awspolicygen.s3.amazonaws.com/policygen.html) / [Policy simulator](https://policysim.aws.amazon.com)

# Module 3 : System Discovery

* Demo
  * System Manager ou AWS Config, mais voir en fonction de ce qu'on voit déjà dans les labs.
  * Ca peut être aussi de montrer Session Manager, la configuration et la partie audit.
  * Session Manager. Port forward sur du RDP Windows

## CloudShell

* /mnt/efs : temp data (does not persist across sessions)
* /mnt/persistent : persistent data
* use S3 when need more space
* git is installed so use it to save code
* not suitable for long running process (close after 20 min of inactivity)


## AWS Config

* AWS Config peut s'intégrer avec Systems Manager Inventory pour détecter les changements dans l'inventaire et stocker l'historique des changements (applications installées, windows registry, etc...)
* AWS Config s'intègre à Organizations dans un double sens
  * un Aggregator à configurer dans le compte d'administrateur. On peut aggéger les configurations et findings de différents comptes ou de tous les comptes d'une organisation donnée
  * Des Organization rules peuvent être définis dans le compte d'administrateur qui se déploieront dans les comptes de l'organization. Cela permet de manager des règles communes de manière centralisé
* AWS Config à des capacités de recherche dans l'inventaire (feature named *Advanced Queries*)
  * SQL-like
  * NLP (Bedrock)
* Track relationship between items. This example queries all EC2 and ENI link to a specific SG

```
SELECT 
    resourceId 
WHERE 
    resourceType IN ('AWS::EC2::Instance', 'AWS::EC2::NetworkInterface') 
    AND relationships.resourceId = 'sg-abcd1234'
```
* [More information](https://docs.aws.amazon.com/config/latest/developerguide/querying-AWS-resources.html)

# Module 4 : Deploy And Update Resources

* Demo
  * EC2 image Builder : peut être aborder d'abord les AMIs. Lancer image builder, faire la partie sur les tags, et ensuite revenir sur le résultat de l'image Builder  
  * Tag Policies ?

## Tagging

* [Tagging best practices blog](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/building-your-tagging-strategy.html)
* [Tagging examples 1](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/defining-and-publishing-a-tagging-schema.html)
* [Tagging examples 2](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-use-cases.html)

* Tagging Categories
  * Finance and Line of Business : mainly for cost
  * Governance and Compliance : categorization of data and business criticity
  * Operations and Development : environment, depreciations
  * Security : what controls must be applied

* Tag Policy in AWS Organizations

* Resource Groups 
  * AWS Config can apply a configuration specific to a group
  * CloudWatch can aggregate metrics of a resource group
  * SSM Automation can be applied to a resource group  
  * IAM Policies can be applied on a resource group 
  * EventBridge can send event when a resource in a resource group changes.
  * [Services that integrate with Resource groups](https://docs.aws.amazon.com/ARG/latest/userguide/integrated-services-list.html)

## AMI

* on AMI creation
  * process reboot EC2 by default before creating image (this can be changed though)
  * take a snapshot of all EBS volumes attached. Create snapshots before will make the process faster as snapshots works in increments.
  * Register image and create image : register is the process of making AMI available to yourself or other accounts for use.
  * Register image can be used to create an AMI from an EBS snapshot instead of creating it from an EC2 instance.
* Specific on windows : Sysprep (which is a windows commanda) must be launched before creating an AMI.
  * Sysprep removes all system-specific information, such as 
    * computer name
    * user accounts
    * security identifiers (SIDs)
  * This allows the image to be deployed on different hardware without conflicts.

## User data scripts

* On user data scripts
  * user data script by default run only on the first boot of instance
  * cloud-init (open-source package that provides a standard, cross-platform way to customize cloud instances at launch time) offers MIME multi-part archive feature. It allows user data script to run at [every boot](https://repost.aws/knowledge-center/execute-user-data-ec2). Set cloud_final_modules to ALWAYS for that.
  * logs can be found at /var/log/cloud-init.log and /var/log/cloud-init-output.log
  * can check user-data from metadata, in case user-data has some env variables in a cloudformation template
  * it's possible to see the logs from the instance properties (Troubleshoot and monitor menu)

## Control Tower

### Control tower customization architecture

* [Control tower customization architecture](https://docs.aws.amazon.com/controltower/latest/userguide/architecture.html)
  * does not create any account, but deploys resources post creation.
  * good to implement transversal controls or create resources 
  * [Manifest file guide](https://docs.aws.amazon.com/controltower/latest/userguide/cfct-manifest-file-resources-section.html)
  * Types of customizations
    * Enable Config in the Management Account
    * Enable CloudTrail Organisational Trail for Data Events
    * Enable EC2 Default EBS Encryption
    * Configure a Hardened IAM Account Password Policy
    * Enable S3 Block Public Access at the Account Level
    * Configure AWS Account Alternate Contacts
    * Enable IAM Access Analyzer and Configure for Delegated Administration
    * Enable GuardDuty and Configure for Delegated Administration
    * Enable Macie and Configure for Delegated Administration
    * Enable Security Hub and Configure for Delegated Administration

### Control tower account factory customization

Account Factory Customization is an account creation blueprint
  * good if resources are specific to a type of account. Not practical to implement transversal rules here as they will have to be replicated on all concerned blueprints

### Proactive controls

* Examples of proactive controls
  * Require that point-in-time recovery for an Amazon DynamoDB table is activated
  * Require an Amazon ECS task definition to have a specific memory usage limit
  * Require an Amazon RDS database cluster to have encryption at rest configured
  * Require an Amazon S3 bucket to have versioning enabled
* Proactive Controls are about services configurations. These configurations might be too low level for SCPs.


# Module 5 : Automate Resource Deployment

* Demo on Service Catalog

* Cloud formation: could be useless if audience uses Terraform.
  * Demo with init scripts and wait conditions. 
  * Demo with stackset on multiple regions

## Cloudformation

* CreationPolicy only blocks current resource, not all the stack, unlike WaitCondition
* CreationPolicy only available for following resources
  * EC2
  * ASG
  * AppStream
* cfn-wire contains logs of signal calls from EC2 to Cloudformation. It can be used to debug for example a network issue between cloudformation and EC2

## Service Catalog

* Tag options are specified by end users at product creation time
* [Auto tags](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/autotags.html) : default tags generated by Service Catalog

# Module 6 : Manage Resources

* Demo
  * AppConfig / Parameter Store
  * Automation Document with State Manager

## Explorer

* Explorer shows aggregated data on all resources. Application Manager show aggregated data on a set of resources. Data shown is not exactly the same
  * Widgets
  * Filters
  * Direct link to service screens
  * Group by Account, region, tag
  * Reporting (csv generation on S3 bucket)

* OpsCenter, Explorer and Change Manager integrates with AWS Organizations.

## OpsCenter

* Standardize format of operational work items (OpsItem) while providing contextual data 
* Features
  * Automatic and Manual creation
  * Searchable
  * Bulk Edit (Status, Priority, Severity, Category)
  * Remediation (Define Runbooks with System Manager Automation)
  * Notification
  * Summary reports (KPIs dashboard)
* can integrate data from cloudtrail logs. Here are some examples
  * **Unauthorized API Calls**: CloudTrail logs can capture API calls made to AWS services, including those that may be unauthorized or suspicious. An OpsItem could be created to investigate and remediate any unauthorized API calls.

  * **Resource Configuration Changes**: CloudTrail logs record changes made to AWS resources, such as creating, modifying, or deleting resources. An OpsItem could be created to track and investigate any unexpected or unauthorized resource configuration changes.

  * **Failed Deployments**: CloudTrail logs can capture failed deployments or provisioning attempts, which could indicate an issue with your infrastructure or deployment process. An OpsItem could be created to investigate and resolve these failures.

  * **Security Incidents**: CloudTrail logs can record security-related events, such as changes to IAM policies or roles, or access to sensitive resources. An OpsItem could be created to investigate and respond to potential security incidents identified from the CloudTrail logs.

  * **Compliance Violations**: CloudTrail logs can be used to monitor for compliance violations, such as resources being created or modified outside of your organization's policies. An OpsItem could be created to address and remediate any identified compliance issues.

## AWS Chatbot

* Chatbot is a service that improves productivity. It allow to [execute cmd](https://docs.aws.amazon.com/fr_fr/chatbot/latest/adminguide/intro-to-the-aws-cli-in-slack.html) on AWS resources from a chat platform. It supports
  * Amazon Chime
  * Slack
  * Teams
* The chat channel can also be notified from AWS Services events, through EventBridge or SNS. For example a cloudwatch alarm in alarm state, or an incident manager response plans trigger.
* It can be integrated with Amazon Q

## Incident Manager

* Possible to create a cloudwatch alarm that creates an opsitem and related to a specific response plan
* A runbook is basically an automation document, where we can have automated tasks (a script on anything of this type) and manual steps.
* When each of the step is resumed, it creates a timeline. In the timeline we can see how long each step took, start time/end time. In the timeline, all actions are logged, like for example if someone has added a metric in the cloudwatch dashboard, the time the cloudwatch alarm has been raised, etc...
* post analysis will display a page that resumes the incident with a page that displays questions about what happened and what could be done to improve. New Opsitems can be automatically created from post analysis answers.
* AWS managed post analysis template could be used or any custom defined template

## Automation Document

* Example of Command / Session Document

```
AWSFleetManager-DeleteUser
```

* Example of Automation Document

```
AWS-AttachEBSVolume
```

more complex one

```
AWS-AttachIAMToInstance
```

### Automation Document vs Step functions

* Automation offers more integration with systems manager feature.
  * executeScript (python script or powershell)
  * invokeCommand (Run command)
  * run instance
  * create ami
  * ...
  * can access all current runbooks and modify them to creéte new ones
* Automation has less features on action flows (no parallel or map for example)
* Step functions has better integrations with some services like Glue, SNS, etc...
* Use case 
  * Automation : operations
  * Step functions : business workflows

## Change Manager

* request change through change templates
* associate approvers to change templates (through SNS topics)
* different level of approvers can be defined
* integrates with change calendar
* attach automation document to change templates. Can be run on schedule or as soon as change is approved
* possible to create changes without any approvment process
* cloudwatch alarm to monitor change, and rollback if alarm is triggered

## Application Manager

* View CloudFormation Stacks, Applications (based on tags, resource groups), service catalogs, automation document in a single pane of glass
* Display opsitems, cost explorer widget, application insights, alarms, cloudwatch logs
* See resources associated with application. 
  * Can execute runbooks on each of these resources
  * Can see AWS Config, cloudtrail logs, alarms related to these resources

## Fleet Manager

* Fleet Manager allows to connect to instances, view file structure, log files, change windows registry... without to ssh to the instance. It's a convenient way to manage a fleet of servers.

## State Manager / Maintenance Windows
* State manager vs Maintenance Windows
  * They both can run scripts on schedule on a set of instance.
  * State manager [can run commands as soon as](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-state-manager-targets-and-rate-controls.html#systems-manager-state-manager-targets-and-rate-controls-about-targets:%7E:text=If%20you%20create%20new,uses%20an%20Automation%20runbook.) a new instance is created for example by an autoscaling group. Maintenance windows works only by schedules.
  * State manager report instances that do not comply, they can be seen in application manager for example, or Compliance. Maintenance Windows do not report anything
  * Maintenance Windows can run Automation documents. State manager runs only RunCommands on managed nodes, although it can run automation documents on other resources like S3

## Patch Manager

### AWS-AmazonLinux2023DefaultPatchBaseline

* Approves all operating system patches 
  * that are classified as "Security" and that have a severity level of "Critical" or "Important".
  * that are classified as "BugFix"
* Patches are auto-approved seven days after release. 

### Custom baselines

* Choose operating system
* Choose product (corresponds more or less to OS version)
* Example of classification
  * Security
  * BugFix
  * Enhancement
  * Recommended
  * NewPackage
* Severity (Low to Critical)

# Module 7 : Configure Highly Available systems

## NLB

### Metrics

* Active Flow Count : Number of connections in the time period
* New Flow Count : Number of new connections in the time period
* ConsumedLBCapacityUnits : LCU impact pricing. See dedicated section for that 
* Reset packets are used to abruptly terminate TCP connections :

  * When a host receives a packet for a port that isn't open
  * To reject an unwanted connection attempt
  * When a host detects an invalid segment or sequence number
  * To clear a "half-open" connection (where one side has closed but the other hasn't)

Can indicate a TCP RST attack where an actor tries to interrupt communication between two adresses

### Pricing

* charged only on the dimension with the highest usage. 
* An LCU contains:
  * 25 new connections per second.
  * 3,000 active connections per minute or 1,500 active connections per minute while using Mutual TLS.
  * 1 GB per hour for Amazon Elastic Compute Cloud (EC2) instances, containers, and IP addresses as targets, and 0.4 GB per hour for Lambda functions as targets. When using the Mutual TLS feature, data processed includes the bytes for the certificate metadata that the load balancer inserts into headers for every request that is routed to the targets.
  * 1,000 rule evaluations per second

## Demo

* Avoir 2 ELB qui pointe sur une application sur 2 régions différentes
* Créer une private hosted zone Route 53 associé aux deux VPC
* Créer un record failover qui pointe sur les deux ALB
* Créer un health check sur les 2 ALB
* Pour simplifier, on peut créer juste 2 instances EC2 au lieu de 2 ALBs

# Module 8 : Automate Scaling

* On peut faire une démo et montrer comment on crée une spot fleet
* On peut faire une démo sur license manager. Il faut créer une AMI custom et lier une licence custom à l'AMI. Ensuite créer des EC2 pour dépasser la limite de licence que l'on a configuré.

## Autoscaling policies

* For cooldown period vs instance warm-up
  * Warm-up is available for simple, step and target tracking policy. 
  * Warm-up good for application that takes time to start. 
  * Cooldown is not available for target tracking.
  * During a cooldown period, when a scheduled action starts at the scheduled time, it can trigger a scaling activity immediately without waiting for the cooldown period to expire
  * It's possible to define a cooldown for scale-in and scale-out activities that will override the default one.
  * The cooldown period helps to prevent the Auto Scaling group from launching or terminating additional instances before the previous scaling activity takes effect. Instance warmup is more made for application that takes time to start.

## License manager

### Tag custom architecture

[Automate licenses detection using Tags and Lambdas](https://aws.amazon.com/blogs/modernizing-with-aws/automatically-create-self-managed-licenses-in-multiple-accounts-using-tags/)
* This is an architecture that can update nb of licenses by using tags, and is based on lambdas triggered by EventBridge, when a stackset have been deployed

### Host resource group

* on peut créer des host resource group afin de lancer automatiquement des EC2 sur un ensemble de Dedicated Hosts qui consomment la même license.
* AWS se chargera d'incrémenter ou décrementer la license en fonction de la création/suppression de nouveaux Dedicated Hosts

# Module 9 : Monitor and maintain system health

Demo : 
* Eventbridge : SNS Mail when an EC2 instance starts
* CloudWatch log insights
* CloudWatch metric insights
* X-Ray

# Module 10 : Data Security and System Auditing

[Zelkova](https://aws.amazon.com/blogs/security/protect-sensitive-data-in-the-cloud-with-automated-reasoning-zelkova/)

Demo : 
* [Demo IAM Access Analyzer](https://github.com/aws-samples/aws-iam-access-analyzer-samples?tab=readme-ov-file#validate-policy-apis)
* Permission Boundary
* Show Cloudtrail

## Access Analyzer

* Can be integrated in AWS Organizations (delegated administator account) 

### Analyzers

* analyze external identities (no additional charge)
* unused access analyser (paid feature)
    * it consists of comparing cloud trail logs with iam permissions.
    * policy generation : generation of a policy that matches cloud trail activity to grant least privilege principle. 
* policy validation : checks regarding best practices. Free to use
* Custom policy checks : checks regarding custom rules. Paid feature. 
    * Comparing to permission boundary, this feature is not restrictive
    * It can be used to identify issues, if permission boundaries or scp does not apply on some accounts in the organization.

## GuardDuty

### Findings examples
  
* EC2
  * detect use of an EC2 to perform a ddos attack
  * bitcoin mining
  * under port scan attack
  * Malware
* RDS
  * Login attempts
* IAM
  * AWS API Calls from an IP address that is included on a threat list. IP list can be provided by a third party or by current organization.

### Findings

* in JSON
* findings contains info about
  * what happened
  * by who
  * to what resources
  * when and where
* A severity is associated (Low, Medium, High)
* [Automatic Archiving](https://docs.aws.amazon.com/guardduty/latest/ug/findings_suppression-rule.html)


## Inspector

* Package vulnerability
  * Amazon Inspector assesses software installed through APT, YUM, or Microsoft Installer
* Network reachability package
  * if a port is exposed to internet through IGW, VGW ro VPC Peering connection. It's the agentless package. 
* Code Vulnerability
  * containers, lambda, ec2. Use CodeGuru Detector library.
* Can integrate with Teamcity, Jenkins, Github actions...

* [list of common vulnerabilities by region](https://docs.aws.amazon.com/inspector/v1/userguide/inspector_cves.html)
* [CVE official site](https://cve.mitre.org/)
* CVE Examples 
  * CVE-2024-39807
  * CVE-2024-39830
*  [list of code findings](https://github.com/aws-samples/amazon-codeguru-detectors). Behind the scene, Inspector uses [CodeGuru Detector Library](https://docs.aws.amazon.com/codeguru/detector-library/)

# Module 11 : Operate Secure and Resilient networks

Demo
* Pourrait reprendre ma démo sur les networks ACL / Sec Group de l'archiOnAWS
* reprendre la demo sur le WAF

## Cloudfront 

### Conditional requests

* when an object expires, it is not necessarily evicted from the cache. It just means, on next call, Cloudfront will call origin to get a newer version
* object can be evicted if other objects are more frequently called, cloudfront evict it to save space for those other objects.
* When cloudfront sends a request to the origin, to fetch the latest data, If it receives a 304 response (Not Modified), it will return the object in its cache, instead of getting the page from the origin.
* Conditional requests can be used from the browser to cloudfront, or from cloudfront to the origin
* For Conditional requests on custom origin, the origin must manually manage the headers. On S3 it is managed natively

## ACM

Some intermediate CAs benefits :

* Compromise isolation. If an issue CA is compromised, damage reduced to CAs signed by the intermediate CA only
* Root CA can be left offline, which enhances security posture
* specific certificated policies or validation requirements can be added to intermediate CAs, providing more flexibility
* Intermediate CAs could be managed by different people. This setup can scale on maintenance

Issuing CA has the operational responsability of issuing certificates with some Public Key infrastructure. They receive authority from root CA or intermediate CAs

# Module 12 : Mountable Storage

Demo : 
* compliqué car ca parle bcp de backup, et les backup ca prend du temps... On peut se contenter de montrer sur la console, notamment de montrer Backup
* a la limite faire une demo sur EFS : faire un EFS, et monter le mount point sur 2 EC2 ou Lambda et partager un fichier
* On pourrait aussi faire un mount point sur un bucket S3 avec [mountpoint](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mountpoint.html)

##  EBS

### Performance

* GP3
  * performance does not depend on the volume size
* GP2
  * performance relative to the volume size
  * performance is burstable
  * Throughput  
    * Volumes < 170 GB : Max 128 Mbps
    * 170 Gb < Volumes < 334 GB : Max 250 Mbps
    * volumes > 334 GB : 250 Mbps
* IOPS :
  * Like GP2, IOPS is tied to volume size but
    * IOPS : Maximum of 500 IOPS / GB allocated
    * GP2 : Maximum of 3 IOPS / GB allocated
  * EBS-Optimized instances deliver dedicated throughput to EBS depending on the instance type used. Example
    * a m4.large has a max Throughput of 56.25 Mbps
    * a m7a.8xlarge has a max Throughput of 1350 Mbps
    * listing [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html#current)

### Updating an EBS

When we make a change on EBS (like changing disk size or performance), we have to wait 6 hours before we can do another operation of this type on the volume

### Multi Attach

* only Nitro instances
* EBS must be an IO optimized
* same AZ
* clustered file system. Example : 
  * General Parallel File System (GPFS), 
  * Microsoft Cluster Shared Volumes (CSV)
  * Global File System 2 (GFS2) for Linux.

## EFS

* General purpose : limited to 35 000 IOPS
* Max I/O : Unlimited IOPS
* Max I/O has higher latency so it's recommended in most cases to use General Purpose
* In General Purpose mode, cloudwatch metric PercentIOLimit indicates how close workload is to IOPS limit.

# Module 13 : Object Storage

* Montrer la replication en plus de ce que je montre d'habitude

## Express One-Zone
 
* Directory buckets
  * no flat storage, organized in directories
  * Only use storage class One-Zone
* [Use case Express One Zone](https://aws.amazon.com/blogs/storage/clickhouse-cloud-amazon-s3-express-one-zone-making-a-blazing-fast-analytical-database-even-faster/)
* En général ce sont des use cases qui matchent bien avec S3 (analytics, data science, données non structurées), write-once/read-many mais avec quelques spécificités
  * besoin d'un accès à faible latence
  * bcp de petits fichiers. La latence de S3 standard est en effet négligeable si il s'agit de gros fichiers. C'est le nombre de fichiers qui pose surtout problème.
  * Exemple : on souhaite récupérer plein d'images pour faire du training de machine learning. Le temps de récupération de ces images se fera sentir sur un S3 standard.
*  [Explications](https://community.aws/content/2ZDARM0xDoKSPDNbArrzdxbO3ZZ/s3-express-one-zone)
  * stocke les données sur une seule AZ, réduit la latence je pense en particulier en écriture. Amélioration en lecture surtout qd le compute se trouve dans la même AZ.
  * Un directory bucket récupère à sa création de la puissance pour supporter plusieurs dizaines de milliers de transactions par secondes (IO). Il ne croit pas graduellement en fonction de la demande comme sur les autres classes, donc il n'a pas de problème en cas de burst soudain comme c'est le cas pour des workloads de machine learning.
  * a un concept de session pour s'authentifier. Il ne s'authentifie pas à chaque requête mais plutôt est basé sur un token qu'on repasse pendant un temps determiné, pour minimiser la latence dû à l'authentification. La session donne accès à la totalité du bucket en lecture, ou écriture ou ReadWrite. Pas de distinction entre les objets d'un bucket.
* Up to 10x times faster than S3 standard
* Requests costs are reduced (50%)


* Use cases
  * ML
  * Interactive data analytics
  * HPC
  * Financial modeling
  * media content workloads (Visual Effects, rendering, and transcoding needs)

## S3 access logs

* Timeliness and delivery events are not guaranteed
* As it's not integrated with Cloudwatch, a custom solution has to be implemented for alerting
* Less detailed than CloudTrail events

## Glacier retrievals

* Expedited : comes with On-Demand or Reserved Capacity. On-demand gives no guarantee that capacity will be available when needed.
* Standard (with or without batch). With Batch uses S3 batch operations
  * Glacier Flexible : Batch Operations starts within minutes and takes 3-5 hours to complete
  * Glacier Deep archive : Batch operations starts after 9 hours and finish within 12 hours

# Module 14 : Cost Reporting - Alerts Optimization

Demo compliqué sur ce sujet, on peut montrer la console.



## Cost Explorer

retention : default to 14 months, can be extended to 38 months at a monthly granularity

## Cost and Usage reports

* longer retention
* break down by resource Id
* Export report to Quicksight, Redshift, etc... More control on permissions (line and column level access)    

## Cost Anomaly Detection

* can segment by AWS service
* can evaluate specific 
  * cost allocation tags
  * member accounts within an organization (AWS Organizations)
  * cost categories

## CloudWatch Billing Alarm

Cloudwatch billing alarm was released in 2012 and budget was released in 2015. So the first one is more a legacy feature. 
* Has more limited filter capacities
* Does not trigger on based on forecasted usage, only on current usage.

## AWS Budget

[Budget Filters](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create-filters.html)

## Trusted Advisor

* You see the same findings that Compute Optimizer but with more delay (up to 48 hours)
* Trusted advisor has much more cost optimization checks and covers also other topics than cost
* Cost Management provides recommandations for savings plans and reserved instances, not covered by compute optimizer but provided by Trusted Advisor. Probably the same result.

* Trusted Advisor Covers (more than compute optimizer)
  * EIP
  * Underutilized Redshift clusters
  * Idle load balancers
  * lambda functions with excessive timeouts or high error rates
  * S3 cost optimizations
  * ECR without lifecycle policies
  * Amazon Comprehend (NLP service) underutilized endpoints

## Cost Optimization Hub

Cost Optimization Hub generates recommendations for the following resources:

* From Compute Optimizer
  * EC2 instances
  * ASG
  * EBS
  * Lambda
  * ECS
  * Amazon RDS DB instances (compute & storage)
* From Commitments
  * Compute Saving Plans
  * EC2 Instance Saving plans
  * SageMaker Saving plans
  * Reserved Instances
    * EC2
    * RDS
    * OpenSearch
    * Redshift
    * Elasticache 


## S3 costs

* Object tags cannot be used as cost allocation tags

* [S3 costs at object level](https://aws.amazon.com/blogs/big-data/analyze-amazon-s3-storage-costs-using-aws-cost-and-usage-reports-amazon-s3-inventory-and-amazon-athena/)