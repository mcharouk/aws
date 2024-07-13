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

* AWS Config peut s'intégrer avec Systems Manager Inventory pour détecter les changements dans l'inventaire et stocker l'historique des changements (applications installées, windows registry, etc...)
* AWS Config s'intègre à Organizations dans un double sens
  * un Aggregator à configurer dans le compte d'administrateur. On peut aggéger les configurations et findings de différents comptes ou de tous les comptes d'une organisation donnée
  * Des Organization rules peuvent être définis dans le compte d'administrateur qui se déploieront dans les comptes de l'organization. Cela permet de manager des règles communes de manière centralisé

# Module 4 : Deploy And Update Resources

* Demo
  * EC2 image Builder : peut être aborder d'abord les AMIs. Lancer image builder, faire la partie sur les tags, et ensuite revenir sur le résultat de l'image Builder  
  * Tag Policies ?

## Tagging

* [Tagging strategy best practices](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/building-your-tagging-strategy.html)

* Tagging Categories
  * Finance and Line of Business : mainly for cost
  * Governance and Compliance : categorization of data and business criticity
  * Operations and Development : environment, depreciations
  * Security : what controls must be applied

* Tag Policy in AWS Organizations
* [Tagging examples](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-use-cases.html)

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
  * take a snapshot of all EBS volumes attached. Create snapshots before will make the process faster as snpashots works in increments.
  * register image and create image : register is the process of making AMI available to yourself or other accounts for use.
  * Register image can be used to create an AMI from an EBS snapshot instead of create image that uses an EC2 instance.
* Specific on windows : Sysprep (which is a windows commanda) must be launched before creating an AMI.
  * Sysprep removes all system-specific information, such as the computer name, user accounts, and security identifiers (SIDs). This allows the image to be deployed on different hardware without conflicts.

## User data scripts

* On user data scripts
  * user data script by default run only on the first boot of instance
  * cloud-init (open-source package that provides a standard, cross-platform way to customize cloud instances at launch time) offers MIME multi-part archive feature. It allows user data script to run at [every boot](https://repost.aws/knowledge-center/execute-user-data-ec2). Set cloud_final_modules to ALWAYS for that.
  * logs can be found at /var/log/cloud-init.log and /var/log/cloud-init-output.log
  * can check user-data from metadata, in case user-data has some env variables in a cloudformation template
  * it's possible to see the logs from the instance properties (Troubleshoot and monitor menu)

## Control Tower

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


Account Factory Customization is an account creation blueprint
  * good if resources are specific to a type of account. Not practical to implement transversal rules here as they will have to be replicated on all concerned blueprints

* Examples of proactive controls
  * Require that point-in-time recovery for an Amazon DynamoDB table is activated
  * Require an Amazon ECS task definition to have a specific memory usage limit
  * Require an Amazon RDS database cluster to have encryption at rest configured
  * Require an Amazon S3 bucket to have versioning enabled
* Proactive Controls are about services configurations. These configurations might be too low level for SCPs.


# Module 5 : Automate Resource Deployment

* Demo on Service Catalog
* [Service catalog example](https://aws.amazon.com/blogs/machine-learning/part-2-how-natwest-group-built-a-secure-compliant-self-service-mlops-platform-using-aws-service-catalog-and-amazon-sagemaker/) and [associated customer success story](https://aws.amazon.com/solutions/case-studies/natwest-group-case-study/?did=cr_card&trk=cr_card)

* Cloud formation: could be useless if audience uses Terraform.
  * Demo with init scripts and wait conditions. 
  * Demo with stackset on multiple regions

## Service Catalog

* Tag options are specified by end users at product creation time
* [Auto tags](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/autotags.html) : default tags generated by Service Catalog

# Module 6 : Manage Resources

* Demo
  * AppConfig / Parameter Store
  * Automation Document with State Manager

* Fleet Manager allows to connect to instances, view file structure, log files, change windows registry... without to ssh to the instance. It's a convenient way to manage a fleet of servers.
* State manager vs Maintenance Windows
  * They both can run scripts on schedule on a set of instance.
  * State manager [can run commands as soon as](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-state-manager-targets-and-rate-controls.html#systems-manager-state-manager-targets-and-rate-controls-about-targets:%7E:text=If%20you%20create%20new,uses%20an%20Automation%20runbook.) a new instance is created for example by an autoscaling group. Maintenance windows works only by schedules.
  * State manager report instances that do not comply, they can be seen in application manager for example, or Compliance. Maintenance Windows do not report anything
  * Maintenance Windows can run Automation documents. State manager runs only RunCommands on managed nodes, although it can run automation documents on other resources like S3

* Explorer shows aggregated data on all resources. Application Manager show aggregated data on a set of resources. Data shown is not exactly the same

* OpsCenter, Explorer and Change Manager integrates with AWS Organizations.

## OpsCenter

can integrate data from cloudtrail logs. Here are some examples : 

* **Unauthorized API Calls**: CloudTrail logs can capture API calls made to AWS services, including those that may be unauthorized or suspicious. An OpsItem could be created to investigate and remediate any unauthorized API calls.

* **Resource Configuration Changes**: CloudTrail logs record changes made to AWS resources, such as creating, modifying, or deleting resources. An OpsItem could be created to track and investigate any unexpected or unauthorized resource configuration changes.

* **Failed Deployments**: CloudTrail logs can capture failed deployments or provisioning attempts, which could indicate an issue with your infrastructure or deployment process. An OpsItem could be created to investigate and resolve these failures.

* **Security Incidents**: CloudTrail logs can record security-related events, such as changes to IAM policies or roles, or access to sensitive resources. An OpsItem could be created to investigate and respond to potential security incidents identified from the CloudTrail logs.

* **Compliance Violations**: CloudTrail logs can be used to monitor for compliance violations, such as resources being created or modified outside of your organization's policies. An OpsItem could be created to address and remediate any identified compliance issues.

## AWS Chatbot

* Chatbot is a service that improves productivity. It allow to perform actions on AWS resources from a chat platform. It supports
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

## Change Manager

* request change through change templates
* associate approvers to change templates (through SNS topics)
* different level of approvers can be defined
* integrates with change calendar
* attach automation document to change templates. Can be run on schedule or as soon as change is approved
* possible to create changes without any approvment process
* cloudwatch alarm to monitor change, and rollback if alarm is triggered

# Module 7 : Configure Highly Available systems

## NLB

### Metrics

Common scenarios for an RST (Reset) packet :

* When a host receives a packet for a port that isn't open
* To reject an unwanted connection attempt
* When a host detects an invalid segment or sequence number
* To clear a "half-open" connection (where one side has closed but the other hasn't)

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
  * The cooldown period helps to prevent the Auto Scaling group from launching or terminating additional instances before the previous scaling activity takes effect. Instance warmup is more made for application that takes time to start.

## License manager

[Automate licenses detection using Tags and Lamdbas](https://aws.amazon.com/blogs/modernizing-with-aws/automatically-create-self-managed-licenses-in-multiple-accounts-using-tags/)

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

* Access Analyzer
  * analyze external identities (no additional charge)
  * unused access analyser (paid feature)
    * it consists of comparing cloud trail logs with iam permissions.
  * policy validation : checks regarding best practices. Free to use
  * Custom policy checks : checks regarding custom rules. Paid feature. 
    * Comparing to permission boundary, this feature is not restrictive
    * It can be used to identify issues, if permission boundaries or scp does not apply on some accounts in the organization.
  * policy generation : generation of a policy that matches cloud trail activityt to grant least privilege principle.
  * Can be integrated in AWS Organizations (delegated administator account) 

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
    * AWS API Calls from an IP address that is included on a threat list

### Findings

* in JSON
* findings contains info about
  * what happened
  * by who
  * to what resources
  * when and where
* A severity is associated
* Automatic Archiving


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

# Module 11 : Operate Secure and Resilient networks

Demo
* Pourrait reprendre ma démo sur les networks ACL / Sec Group de l'archiOnAWS
* reprendre la demo sur le WAF

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
* IOPS :
  * Like GP2, IOPS is tied to volume size but
    * IOPS : Maximum of 500 IOPS / GB allocated
    * GP2 : Maximum of 3 IOPS / GB allocated

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

* Directory buckets
  * no flat storage, organized in directories
  * Only use storage class One-Zone
* Montrer la replication en plus de ce que je montre d'habitude
* [Use case Express One Zone](https://aws.amazon.com/blogs/storage/clickhouse-cloud-amazon-s3-express-one-zone-making-a-blazing-fast-analytical-database-even-faster/)
*  [Explications](https://community.aws/content/2ZDARM0xDoKSPDNbArrzdxbO3ZZ/s3-express-one-zone)
  * stocke les données sur une seule AZ, réduit la latence je pense en particulier en écriture. Amélioration en lecture qd le compute se trouve dans la même AZ.
  * Un directory bucket récupère à sa création de la puissance pour supporter plusieurs dizaines de milliers de transactions par secondes. Il ne croit pas graduellement en fonction de la demande comme sur les autres classes, donc il n'a pas de problème en cas de burst soudain comme c'est le cas pour des workloads de machine learning.
  * a un concept de session pour s'authentifier. Il ne s'uthentifie pas à chaque requête mais plutôt est basé sur un token qu'on repasse pendant un temps determiné, pour minimiser la latence dû à l'authentification. La session donne accès à la totalité du bucket en lecture, ou écriture ou ReadWrite. Pas de distinction entre les objets d'un bucket.

* Use cases
  * ML
  * Interactive data analytics
  * HPC
  * Financial modeling
  * media content workloads (Visual Effects, rendering, and transcoding needs)



# Module 14 : 

Demo compliqué sur ce sujet, on peut montrer la console.

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

[https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create-filters.html](budget filters)

## Trusted Advisor

* in Trusted Advisor
  * You see the same findings that Compute Optimizer but with more delay (up to 48 hours)
  * Trusted advisor has much more cost optimization checks and covers also other topics than cost
  * Cost Management provides recommandations for savings plans and reserved instances, not covered by compute optimizer but provided by Trusted Advisor. Probably the same result.

## Cost Optimization Hub

Cost Optimization Hub generates recommendations for the following resources:

* EC2 instances
* ASG
* EBS
* Lambda
* ECS
* Amazon RDS DB instances (compute & storage)
* Commitment
  * Compute Saving Plans
  * EC2 Instance Saving plans
  * SageMaker Saving plans
  * Reserved Instances
    * EC2
    * RDS
    * OpenSearch
    * Redshift
    * Elasticache 
