# VPC


see what is AWS Graviton
BYOIP : how it works

# EC2

* la base de l'EC2 est l'AMI
  * Prebuilt
    * contient une configuration très basique
  * AWS Marketplace
    * contient des soft qui sont fournis par des tiers. Gain du temps potentiel sur la configuration du soft.
  * Custom
    * Si on a besoin de configuration custom. Partageable avec d'autres comptes, même en public via la marketplace...
    * Besoin de maintenance pour installer des nouveaux patchs par exemple
    * Parler de la possibilité d'installer les soft avec le user data. Ce qui permet d'avoir quelque chose de plus dynamique et de plus flexible.


## Shared and Dedicated Tenancy

Dedicated instance : physically separated hardware from other customers. 
    * A hardware can have multiple slots where VM will be instantiated.
    * all slots on the hardware will be reserved for a single customer on a dedicated tenancy
    * if all instances on a single physical hardware are stopped, hardware could be reallocated to another client

Dedicated host : le hardware est dédié au client. Licensing models may require that.

## EC2 naming conventions

c5n.xlarge

* C : instance family
* 5 : instance generation. When there are newer, they are more efficient, so we could pick a lower instance size. Are not necessarily more expensive, sometimes less because AWS wants people to use them.
* n : attribute : can point out some characteristic that differntiate it from others . n = more networking capability
* xlarge : size

Difference is in the ratio compute/memory

* c : compute optimized
* r : ram optimized
* m,t : in the middle (general purpose)
Other families 
* Storage optimized
* Accelerated compute (GPU)

## EC2 lifecycle

Stop an instance is equivalent to switch it off. Basically, the disks are retained (EBS-backed instances), so we can start from where it has been stopped.
Hibernate means memory state is retained. So boot start time is reduced. Long running process can go on without interruption. Great if there is a in memory caching layer.

## EC2 instance key pairs

Windows ne supporte pas les key pairs. 
Aws génère un mdp d'administrateur et l'encrypte avec une clé publique. On en peut le décrypter qu'avec une clé privé.
une fois qu'un EC2 est up, on peut changer la méthode d'authentification pour en faire ce qu'on veut. Par exemple passer sur un mode user/mot de passe

## EBS volume types

2 main categories
* SSD
  * general purpose : gp2, gp3
  * provisioned iops : io1, io2
* HDD : cheaper
  * throughtput optimized
  * cold HDD : archive, less frequently accessed

## EC2 pricing

### Reserved instances

* Standard : commit to an instance type 
* Convertible : change the attributes of instance type as long it's equal or higher (less discount). To follow the generation releases. M5 to m6 for ex.

### Savings plans

* Compute saving plans
* EC2 instance saving plans : flexible about Size, OS, Tenancy


## Storage

### Object Storage

* objects are all at the same level (no hierarchy). They are all stored in the same repository.
* metadata can be extremely detailed.
* communication through an API which make it agnostic to file system, language, etc...

Pros : 
* unlimited scalability

Cons : 
* Cannot modify a portion of an object. They are immutable.
* Slower

use cases : archives, backup and restore, big data analytics, media content, static websites

### File storage

* All data is saved in a single file.
* organized in sub directories. Easy to explore and organize

Pros : 
* good for file sharing, editing
* performance

### Block storage

* divide data into blocks, each block has its own ID and store it in a manner it's fast to retrieve. 
It can spread blocks in different hard disks which makes it flexible.

Pros
* very fast / high throughput. Convenient to modify large files with frequent access (as it's divided into blocks)
* operating system agnostic


## Glacier

* Vault Lock controls how data can be used
* Resource policy that can be locked. Policy says Who can retrieve it, Data retention time...
* Data is offline, harder to tampered with.
* No URL to access Glacier data


## S3 access points

* decomposition of a bucket policy into multiple access points which each have their own policies.
* A bucket policy have a 20 Kb limit size.
* access points can be accessed through internet or through VPC only.
* Principals can be restricted to use s3 only through a specific access point.


## EFS

* mount target in each AZ to be able to mount it.
* NFSv4
* EFS is multi AZ (standard, one Zone, ...). Take a look at others
* Automatically grows and shrink
* Different storage class : Standard, IA, OneZone

* Performance mode : General purpose or Max I/O.
  * General purpose offers better I/O. One Zone always use General purpose
  * Max I/O : previous generation performance type that is designed for highly parallelized workloads that can tolerate higher latencies

* Throughput modes:
  * Elastic : unpredictable throughput requirements
  * Provisioned : steady state throughput requirements
  * Bursting : throughput increase with storage size. Burst means it will use unused capacities when there is a peak.

* By default, EFS trust the user id that mount. It uses posix style permissions.
* EFS Access point to control 
  * the mount point location / folder
  * the user that will be used to access EFS.

## FSx

* For Windows File Server
  * for windows, but with Samba linux system can mount
  * obtain a managed windows file server
  * supports AD authentication
* for Lustre : clustered file systems (HPC)
  * Parallel file system
  * SSD-based
  * Supports hundred of thousands of cores
  * big data / ML / media processing
  * integrates with S3. Data stored in S3 and presented by Lustre

## Storage Gateway

* search infos for tape gateway and volume gateway...

* file gateway : like a file sharing system but backed by S3
* volume gateway : offers block storage. Data is stored on S3 using iSCSI protocol. asynchronously can backup point in time snapshots (EBS snapshots). 
Use service snapshot scheduler or AWS Backup.
It's more like a drive attached to an operating system, but it's located remotely. Two modes : Cached and Stored
* tape gateway : using iSCSI protocol, stores virtual tapes in S3 Glacier. Dive deeper...
* FSx File Gateway : file share system to be accessed from on premise (windows file system). SMB protocol. Acts like a NFS

* OpenZFS
* NetApp OnTAP -> take a look at those


## EBS multi attach

Limitations : 
* up to 16 instances
* supported exclusively on provisioned iops
* can't change the volume type or size
* single AZ

## EC2 Image Builder

Define a pipeline that : 
* install EC2 with scripting
* Create an AMI
* Execuite tests on AMI
* Authorize other accounts to build an EC2 from AMI / Create a copy for each account, OU, etc... in other AWS regions
* Lifecycle management by deprecate / disable / remove old AMIs

## CloudFront Pricing

* Data Transfer Out
* Lambda@Edge / Cloudfront functions
* number of requests made to cloudfront
* data transfer between cloudfront and origin (regional data transfer)
* Cache Invalidation
* Origin Shield requests


deep dive in that

Does traffic go over the internet when two instances communicate using public IP addresses, or when instances communicate with a public AWS service endpoint?
No. When using public IP addresses, all communication between instances and services hosted in AWS use AWS's private network. Packets that originate from the AWS network with a destination on the AWS network stay on the AWS global network, except traffic to or from AWS China Regions.

In addition, all data flowing across the AWS global network that interconnects our data centers and Regions is automatically encrypted at the physical layer before it leaves our secured facilities. Additional encryption layers exist as well; for example, all VPC cross-region peering traffic, and customer or service-to-service Transport Layer Security (TLS) connections. 

# Local zone

Netflix uses local zones to provide Virtual desktops to their employees (EC2). They need good bandwidth as they design special effects. Latency < 10ms

Tape Gateway : Ryanair have reduced their archives cost by 65 % (Tape gateway + Deep glacier)


# Outposts

## Rack vs Server

Rack 

* Amazon Elastic Compute Cloud (EC2)
* Amazon Elastic Block Store (EBS)
* Amazon Simple Storage Service (S3)
* Amazon Relational Database Service (RDS)
* Amazon Elasticache
* Application Load Balancer (ALB)
* VMware Cloud.
* Other AWS Services

Server 

* Amazon Elastic Compute Cloud (EC2)
* AWS IoT Greengrass
* Amazon Sagemaker Edge Manager.