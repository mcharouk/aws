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

* [Policy generator](https://awspolicygen.s3.amazonaws.com/policygen.html)
* [Policy simulator](https://policysim.aws.amazon.com)

# Module 3 : System Discovery

* Demo
  * System Manager ou AWS Config, mais voir en fonction de ce qu'on voit déjà dans les labs.
  * Ca peut être aussi de montrer Session Manager, la configuration et la partie audit.
  * Session Manager. Port forward sur du RDP Windows

* AWS Config peut s'intégrer avec Systems Manager Inventory pour détecter les changements dans l'inventaire (applications installées, windows registry, etc...)

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
* Specific on windows : Sysprep (which is a windows commanda) must be launched before creating an AMI.
  * Sysprep removes all system-specific information, such as the computer name, user accounts, and security identifiers (SIDs). This allows the image to be deployed on different hardware without conflicts.

## User data scripts

* On user data scripts
  * user data script by default run only on the first boot of instance
  * cloud-init (open-source package that provides a standard, cross-platform way to customize cloud instances at launch time) offers MIME multi-part archive feature. It allows user data script to run at [every boot](https://repost.aws/knowledge-center/execute-user-data-ec2). Set cloud_final_modules to ALWAYS for that.
  * logs can be found at /var/log/cloud-init.log and /var/log/cloud-init-output.log
  * can check user-data from metadata, in case user-data has some env variables in a cloudformation template
  * it's possible to see the logs from the instance properties (Troubleshoot and monitor menu)

# Module 5 : Automate Resource Deployment

* Demo on Service Catalog
* [Customer Success Story Service Catalog](https://aws.amazon.com/solutions/case-studies/expedia-service-catalog-case-study/?did=cr_card&trk=cr_card)
* [Service catalog example](https://aws.amazon.com/blogs/machine-learning/part-2-how-natwest-group-built-a-secure-compliant-self-service-mlops-platform-using-aws-service-catalog-and-amazon-sagemaker/) and [associated customer success story](https://aws.amazon.com/solutions/case-studies/natwest-group-case-study/?did=cr_card&trk=cr_card)
* Cloud formation: could be useless if audience uses Terraform.
  * Demo with init scripts and wait conditions. 
  * Demo with stackset on multiple regions

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

# Module 7 : Configure Highly Available systems

ALB / Route 53

Demo : 
    * Avoir 2 ELB qui pointe sur une application sur 2 régions différentes
    * Créer une private hosted zone Route 53 associé aux deux VPC
    * Créer un record failover qui pointe sur les deux ALB
    * Créer un health check sur les 2 ALB
    * Pour simplifier, on peut créer juste 2 instances EC2 au lieu de 2 ALBs

# Module 8 : Automate Scaling

* On peut faire une démo et montrer comment on crée une spot fleet
* On peut faire une démo sur licence manager. Il faut créer une AMI custom et lier une licence custom à l'AMI. Ensuite créer des EC2 pour dépasser la limite de licence que l'on a configuré.
* Faudra surtout créer des whiteboards pour expliquer le cooldown period, instance warmup period notamment. Expliquer à quoi ca sert
* Expliquer les différentes termination policies
* Expliquer les suspended processes. A quoi ca sert, dans quel cas.
Compliqué de faire une démo sur ce sujet


* For cooldown period vs instance warm-up
  * Warm-up is available for simple, step and target tracking policy. 
  * Warm-up good for application that takes time to start. 
  * Cooldown is not available for target tracking.

# Module 9 : Monitor and maintain system health

Demo : 
* Eventbridge : SNS Mail when an EC2 instance starts
* CloudWatch log agent
* Create a metric from logs
* X-Ray

# Module 10 : Data Security and System Auditing

[Zelkova](https://aws.amazon.com/blogs/security/protect-sensitive-data-in-the-cloud-with-automated-reasoning-zelkova/)

Demo : 
* [Demo IAM Access Analyzer](https://github.com/aws-samples/aws-iam-access-analyzer-samples?tab=readme-ov-file#validate-policy-apis)
* Permission Boundary
* Show Cloudtrail

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
    * IP Calls from an IP address that is included on a threat list

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

# Module 11 : Operate Secure and Resilient networks

Demo
* Pourrait reprendre ma démo sur les networks ACL / Sec Group de l'archiOnAWS
* VPC flow logs avec Cloudwatch Insights
* reprendre la demo sur le WAF

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
* IOPS : like GP2. Performance depends on volume size

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

# Module 13 : Object Storage

* Montrer la replication en plus de ce que je montre d'habitude
* [Use case Express One Zone](https://aws.amazon.com/blogs/storage/clickhouse-cloud-amazon-s3-express-one-zone-making-a-blazing-fast-analytical-database-even-faster/)

# Module 14 : 

Demo compliqué sur ce sujet, on peut montrer la console.

Voir un peu Cost Anomaly Detection

[https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create-filters.html](budget filters)

Cloudwatch billing alarm was released in 2012 and budget was released in 2015. So the first one is more a legacy feature. 
* Has more limited filter capacities
* Does not trigger on based on forecasted usage, only on current usage.

* in Trusted Advisor
  * You see the same findings that Compute Optimizer but with more delay (up to 48 hours)
  * Trusted advisor has much more cost optimization checks and covers also other topics than cost
  * Cost Management provides recommandations for savings plans and reserved instances, not covered by compute optimizer but provided by Trusted Advisor. Probably the same result.