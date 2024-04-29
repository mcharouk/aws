# Module 1

## Data centers

* Perimeter Layer
* Infrastructure Layer
* Data Layer
* Environmental layer

# Module 2 : Account Security

# Principals

* Role session duration : [between 1 and 12 hours](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtosessionduration.html)

## Policies

* [IAM evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html#policy-eval-denyallow)

# Module 3 : Networking

## EIP

### BYOIP

[Process diagram](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-byoip.html#prepare-for-byoip)

* Create a ROA (Route Origin Authorization) in your RIR (Regional Internet Registry). This ROA is used to authenticate IP advertisment to AWS
* Provision an address range for use in AWS. AWS verify with a self-signed certificate that the client owns the address range (it matches with the one used to create the ROA)
* Use command advertise-byoip-cidr to advertise an ip range from AWS. 
  * AWS recommends you deactivate other places that can advertise this same address range, otherwise AWS can't guarantee that traffic to the address range will enter their network.

# Module 4 : Compute

## EC2

### EC2 lifecycle

* Stopping an instance is equivalent to switch it off. Basically, the disks are retained (EBS-backed instances), so we can start from where it has been stopped.
* Hibernate means memory state is retained. So boot start time is reduced. Long running process can go on without interruption. Great if there is a in memory caching layer.

## EBS / Instance Store

### EBS Multi Attach

[Limitations](https://docs.aws.amazon.com/fr_fr/AWSEC2/latest/UserGuide/ebs-volumes-multi.html#considerations) : 
* up to 16 instances
* supported exclusively on provisioned iops
* can't change the volume type or size
* single AZ

### Instance store

* [Instance store throughput](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/general-purpose-instances.html#general-purpose-ssd-perf)

# Module 5 : Storage

## EFS

### Performance and Throughput

* Performance mode : General purpose or Max I/O.
  * General purpose offers better I/O. One Zone always use General purpose
  * Max I/O : previous generation performance type that is designed for highly parallelized workloads that can tolerate higher latencies

* [Throughput modes](https://docs.aws.amazon.com/efs/latest/ug/performance.html#throughput-modes):
  * Elastic : unpredictable throughput requirements
  * Provisioned : steady state throughput requirements
  * Bursting : throughput increase with storage size. Burst means it will use unused capacities when there is a peak.

### User permissions

* By default, EFS trust the user id that mount. It uses posix style permissions.

* EFS Access point to control
  * the mount point location / folder
  * the user that will be used to access EFS.

# Module 10 : Networking 2

## Direct Connect
* [List of Direct Connect Partners](https://aws.amazon.com/directconnect/partners/)

# Module 11 : Serverless

## SNS

* Retries works for AWS managed service (Lambda, SQS, ...) and HTTP endpoint
* Archiving and replaying events is supported only for FIFO topics

# Module 12 : Edge Services

## Route 53

### Routing policies

* Routing policies not supported by private hosted zone
  * Geoproximity
  * Ip-based routing (map a user ip list to a specific resource)
  
### Transfer a DNS Service to Route 53

* Get the current DNS configuration (records to duplicate)
* Create a public hosted zone in Route 53
* Create all records in the newly created zone
* Lower TTL settings of NS record to 15 minutes (to roll back in case)
* Wait two days to ensure the new NS record TTL has propagated
* Update the NS record to use the Route 53 name servers
* Monitor traffic for the domain 
* Change NS record TTL on Route 53 to a higher value (two days)

### Transfer domain registration to Route 53

To [Transfer domain registration](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-transfer-to-route-53.html#domain-transfer-to-route-53-requirements)

* can be done through the console. High level steps requires
  * unlocking the domain in the current registrar
  * Get an authorization code from the current registrar
  * Renew your domain registration before transferring it (not mandatory, depends on the current registrar)
  * Click the link in the confirmation email


## CloudFront

### Pricing

* Requests
  * Number of requests made to cloudfront
  * Origin Shield requests
* Network
  * Data Transfer Out
  * Data transfer between cloudfront and origin (regional data transfer)
* Compute
  * Lambda@Edge / Cloudfront functions
* Cache
  * Cache Invalidation

### Differences OAI / OAC

* Temporary credentials
* Support S3 bucket KMS encryption
* OAC supports HTTP requests: 
  * GET, PUT, POST, PATCH, DELETE, OPTIONS, and HEAD. 
* OAI does not support POST or DELETE (write operations)

## Outposts

### Rack vs Server
[Services available](https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html#services)