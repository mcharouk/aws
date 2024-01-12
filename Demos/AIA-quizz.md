# IAM

Quel problème pose le least privilege principle ?

Multi account : 
* Plus facile de mettre des restrictions spécifiques en fonction de l'environnement,
des applications, ou de la réglementation.
* Si un compte doit être HIPAA compliant, pas la peine d'imposer ses contraintes à tout le monde.
* Si l'organisation des personnes, des rôles et des responsabilités différe d'un env à un autre, plus facile de séggreger. Chacun à son pré, et on ne prend pas le risque que les administrateurs se marchent dessus.
* Plus facile de gérer les coûts car ils sont liés directement à un compte.
* Service Quotas
* Blast Radius


# Infrastructure

What do you consider personally being the best driver to move to the cloud ?
* Cost
* Time To Market
* Innovation
* No infra maintenance
* Security
* Easy and (near) unlimited scaling

What benefits of Local Zone over Edge locations ?

* Services are cheaper on Local Zone
* Compliance with data residency requirements
* Reduced latency for globalized workloads
* Reduced latency for localized workloads

For what can AZs can be used for ? 

* High availability
* Disaster Recovery
* Content Delivery Network

What proposition is not a pillar of AWS Well architected Framework ?

* Sustainability
* Cost Optimization
* Security
* High Availability


# Compute

What instance family is ideal for intensive deep learning training ?
* General Purpose
* Memory Optimized
* Compute Optimized
* Accelerated Computing

What is the advantage of instance store vs EBS ?
* Low latency / High IOPS
* Can be easily attached and detached from an EC2 instance
* Data Durability
* Price

I'm constrianed by regulation to have all my VMs on a single tenant hardware. What is the best solution for that ?

* Dedicated Instance
* Dedicated Host
* On Demand Instances
* Spot Instances

# Storage

Users wants to work concurrently on the same files. What is the ideal AWS storage for that use case ?
* EBS
* S3
* EFS
* FSx For Lustre

What is the easiest way to maintain S3 access policies at large scale ?
* Identity based policies
* Bucket policy
* Access points
* Block Public access policy

I want to migrate my data to the cloud to decrease my infrastructure size on premise but without changing my user habits, still provide low latency for frequently accessed files. What is the best solution for that ?

* AWS File Gateway
* AWS DataSync
* AWS FSx for Windows
* AWS Snowball Edge

# Database

What can i use to scale my write operations on RDS ?

* Multi AZ
* Read Replicas
* Vertical Scaling
* Global Tables

How can i secure authorizations to my RDS Data ?

* IAM
* Encryption at rest
* GRANT statements
* Block public access

What are differences between Aurora and RDS ?

* Data durability is better on Aurora
* Aurora has its own proprietary extension of SQL which is highly optimized
* Aurora can scale automatically
* Aurora is HA by default whereas RDS is HA only if multi AZ is activated

# Monitoring

I have a workload which needs a static IP to be exposed to the consumer applications (they have a whitelist based on IP adresses)
Which Load balancer should i use ? 

* Network Load Balancer
* Application Load Balancer
* Gateway Load Balancer
* Classic Load Balancer

At what level can VPC flow logs be activated ?

* ENI
* Security Group
* Subnet
* VPC

I need to raise an alert if a user has been able to connect without MFA. What service should i use to catch this event ?

* Cloudtrail
* Cloudwatch
* Not possible to do that
* VPC Flow Logs

# Automation


# Networking 1

How can i give internet access to a resource in a private subnet to download some patches ?

* Create an internet gateway and attach it to a public subnet
* Change the route table to point to the NAT Gateway
* Create a NAT Gateway in a private subnet
* Create a NAT Gateway in a public subnet

My EC2 instance is hosting a web application with HTTPS in a public subnet. My NACLs and Security Group allows all inbound connections on port 443.
When i try to reach it with its ip, i still cannot connect to my application. What can be a reason for that ?

* My NACL outbound rules are misconfigured
* My security group outbound rules are misconfigured
* Route table of EC2 subnet is misconfigured
* I'm using the private ip instead of the public ip

# Networking 2

What can we do to make a VPN Connection HA ?

* Create 2 Virtual Gateways
* Provision 2 Customer Gateway
* Create 2 SSL connections 
* VPN Connection is natively HA

What can we do to access S3 privately from a VPC ? 

* Nothing, private connectivity is automatically managed by AWS
* Create an Interface endpoint
* Create a Gateway endpoint
* Create a virtual private Gateway

What are advantages of using VPC Peering ?

* Cost
* Flexibility
* Easy to setup
* Scale to a global network

# Containers

Why do we need a container orchestrator ?

* Manage containers tagging an versioning
* It is a mandatory tool to be able to run containers
* Manage container scheduling on the cluster
* Improve security

I have containers that take part of an HPC cluster. Which compute model should i use ?

* ECS on Fargate
* EKS on Fargate
* ECS on EC2
* EKS on EC2

# Serverless

I need to save my clickstream data in near real time to AWS OpenSearch Service in order to analyze the data. What is the easiest way to achieve that ?

* SQS -> Lambda -> OpenSearch
* SNS -> Lambda -> OpenSearch
* Kinesis Firehose -> Opensearch
* Kinesis Streams -> Lambda -> OpenSearch

What are differences between API Gateway and ALB ?

* API Gateway doesn't incurve cost when there is no request.
* API Gateway can call Lambdas. ALB can only call containers and EC2 workloads.
* API Gateway can handle quotas and throttling
* API Gateway can load balance traffic between EC2 instances

I need to decouple producers and consumers. Many different consumers can consume data coming from a single producer. What is the best choice ?

* Kinesis streams
* SNS
* SQS
* Use SNS and SQS

# Edge

Cloudfront can be used for what usage ?

* Reduce latency for end users
* Improves security posture
* Data residency regulations
* Need intensive compute capabilites closer to the user

In route 53, what routing policy is the best choice to improve latency for my end users ?

* Latency
* GeoProximity
* GeoLocation
* EdgeLocation

# Backup

How can we backup Glacier Data on a different region ?

* CRR S3 feature
* SRR S3 feature
* Lifecycle policies

How can we backup EBS on a different region

* EBS is a multi region service. Does not need to be backed up
* Create a snapshot. The snapshot is automatically stored in another region
* Create a snapshot and copy it in another region
* Use cross region replication feature

How can we backup DynamoDB in another region ?

* Use Global tables
* Use Backups and copy them in a different region
* Use Multi-AZ capability
* DynamoDB replicates automatically its data in another region

How can we backup EFS Data in another region ?

* EFS is already a multi region service
* Use CRR feature of EFS
* Use AWS Datasync to synchronize data
* Use point in time snapshots




