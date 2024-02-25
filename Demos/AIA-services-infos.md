# Module 4 : Compute

## EC2

### EC2 lifecycle

* Stop an instance is equivalent to switch it off. Basically, the disks are retained (EBS-backed instances), so we can start from where it has been stopped.
* Hibernate means memory state is retained. So boot start time is reduced. Long running process can go on without interruption. Great if there is a in memory caching layer.

## EBS / Instance Store

### EBS Multi Attach

Limitations : 
* up to 16 instances
* supported exclusively on provisioned iops
* can't change the volume type or size
* single AZ

### Instance store

* [instance store throughput](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/general-purpose-instances.html#general-purpose-ssd-perf)

# Module 5 : Storage

## EFS

### Performance and Throughput

* Performance mode : General purpose or Max I/O.
  * General purpose offers better I/O. One Zone always use General purpose
  * Max I/O : previous generation performance type that is designed for highly parallelized workloads that can tolerate higher latencies

* Throughput modes:
  * Elastic : unpredictable throughput requirements
  * Provisioned : steady state throughput requirements
  * Bursting : throughput increase with storage size. Burst means it will use unused capacities when there is a peak.

### User permissions

* By default, EFS trust the user id that mount. It uses posix style permissions.

* EFS Access point to control
  * the mount point location / folder
  * the user that will be used to access EFS.

# Module 12 : Edge Services

## Route 53

### Routing policies

* Routing policies not supported by private hosted zone
  * Geoproximity
  * Ip-based routing (map a user ip list to a specific resource)
  * 
## CloudFront 

### Pricing

* Data Transfer Out
* Lambda@Edge / Cloudfront functions
* number of requests made to cloudfront
* data transfer between cloudfront and origin (regional data transfer)
* Cache Invalidation
* Origin Shield requests

## Outposts

### Rack vs Server

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
