# Module 3 : System Discovery

## Experian

[Experian](https://aws.amazon.com/solutions/case-studies/experian-case-study/?did=cr_card&trk=cr_card)

* Global Technology company in data and analytics
* needed a solution to help manage security alerts arising from its cloud environments.
* standardize and automate security protocols to address the root cause of the security alerts.
* "How can we best give our clients the tools that provide them flexibility in their environments functionality without compromising security?"

* Used AWS Config + AWS Lambda for alerting and automatic remediation 
* Experian has applied standardized security controls to over 400 of its accounts, and the number is continually growing
* By using AWS Config, Experian enjoys visibility and can correct misconfiguration in 2–5 minutes, compared to 24 hours using third-party tools.
* Experian decreased the number of security alerts in its Amazon S3 buckets (as they work on data use cases, s3 is a central service in their workload) by 80 percent from June to August 2021

# Module 5 : Automate Resource Deployment

## Expedia

[DBaaS for Expedia](https://aws.amazon.com/solutions/case-studies/expedia-service-catalog-case-study/?did=cr_card&trk=cr_card)

### Context 
* Expedia : 9,000 applications across more than 400 AWS accounts

* Expedia Group wanted to facilitate simple, self-serve database provisioning across its developer teams. 
* It needed a way to enforce good governance and best practices while keeping the provisioning process simple and manageable

### Solution 

* has developed a DBaaS platform with Service Catalog
* support many database technologies, SQL and NoSQL
* Developers use the AWS Service Catalog console to view the products that they can deploy, input basic information such as database type and tags, and then launch the database
* Cerebro takes care of the underlying network configurations and sets up monitoring and security parameters automatically by pushing CloudFormation templates into the new accounts

### Results

* Developers had to wait a few days after submitting a ticket to the database team, but now developers can deploy a database themselves in only a few minutes
* Because the process is so simple, developers can spend more time focusing on their work rather than on database configurations


## NatWest Group

[AWS Blog](https://aws.amazon.com/blogs/machine-learning/part-2-how-natwest-group-built-a-secure-compliant-self-service-mlops-platform-using-aws-service-catalog-and-amazon-sagemaker/) and [customer success story](https://aws.amazon.com/solutions/case-studies/natwest-group-case-study/?did=cr_card&trk=cr_card)

### Context

* NatWest Group is a relationship bank for a digital world that provides financial services to more than 19 million customers across the UK
* The process of creating new environments took from a few days to weeks or even months.
* A reliance on central platform teams to build, provision, secure, deploy, and manage infrastructure and data sources made it difficult to onboard new teams to work in the cloud.
* Teams who decided to migrate their workloads to the cloud had to go through an elaborate compliance process. 
* Each infrastructure component had to be analyzed separately, which increased security audit timelines.
* The teams had to read a set of documentation guides written by platform teams. 
* Initial environment setup was complex. 
* Technical challenges often made it difficult to onboard new team members. 
* After the development environments were configured, the route to release software in production was similarly complex and lengthy.
* need for automation and standardization as a precursor to quick and efficient project delivery on AWS

### Solution

Teams now can deploy in self service
* A Studio environment
* Studio user profiles
* Model deployment pipelines
* Training pipelines
* Inference pipelines
* A system for monitoring and alerting

### Results 

NatWest can now provision new, scalable, and secure AWS environments in a matter of hours, compared to days or even weeks

# Module 12 : Mountable Storage

## PLANA

[PLANA, Pioneers the Future of Advanced Aviation on AWS](https://aws.amazon.com/solutions/case-studies/plana-case-study/?did=cr_card&trk=cr_card)

* design hybrid eVTOL aircraft for urban and regional environments
* objective : production ready by 2028
* encountered inefficiencies within their traditional workstation setup, resulting in time-consuming simulations
* faced high costs because it relied on engineering software that is charged on an hourly basis
* Migrated on AWS HPC Stack
  * ParallelCluster
  * EC2 on EFA (Elastic Fabric Adapter)
  * FSx for Lustre

Note : ParallelCluster is an open source tool (released by AWS) that can automate clusters using a text file or a GUI. Integrates with Slurm or AWS Batch (both are scheduler that will create resources based on the submitted jobs)

### Results

* 70 percent reduction in HPC simulation costs by using
  * combination of On-Demand and Spot-Instance
  * C5n HPC instances
  * Amazon FSx for Lustre 
  * AWS ParallelCluster for configuring HPC resources for each simulation quickly and flexibly.
* The airflow simulations can now be completed in 5−8 hours instead of 10 days

# Module 13 : Object Storage

[Clickhouse - S3 Express One Zone](https://aws.amazon.com/blogs/storage/clickhouse-cloud-amazon-s3-express-one-zone-making-a-blazing-fast-analytical-database-even-faster/)

## Context
* ClickHouse Cloud is a SaaS solution offering a separated storage and compute architecture for running ClickHouse, a columnar database management system designed for real-time analytics.
* This architecture leverages Amazon S3 for primary data storage, offering benefits like scalability, cost efficiency, and ease of use.
* However, achieving low query latency for real-time applications while relying on object storage presented a challenge.
Initial solutions involved implementing a sophisticated caching layer on local disks, which proved costly and complex to manage.

## Issue

* Balancing Performance and Cost: ClickHouse Cloud needed to achieve low query latency comparable to local disk performance while leveraging the cost-effectiveness and scalability of Amazon S3 as the primary data store.
* Caching Layer Limitations: The existing caching layer on local disks, while effective in improving performance, introduced significant costs and operational overhead due to data replication and synchronization across multiple Availability Zones.

## Solution

### Solution Description

Leveraging Amazon S3 Express One Zone: ClickHouse Cloud adopted the newly launched Amazon S3 Express One Zone storage class for both primary data storage and caching.

* S3 Express One Zone as Primary Storage: This approach aimed to improve query performance for cold data (data not present in the cache) by leveraging the low latency and high throughput of S3 Express One Zone.
* S3 Express One Zone as Caching Layer: This strategy aimed to replace the local disk-based caching layer with a more cost-effective and operationally efficient solution by storing a single copy of cached data in S3 Express One Zone, accessible across multiple Availability Zones.


### Technology Used
Amazon S3 Express One Zone: A new storage class offering single-digit millisecond latency and high throughput, optimized for performance-sensitive applications.

### Key Performance Indicators

* Query Latency for Cold Data: Using S3 Express One Zone as the primary storage resulted in an average **36%** improvement in query latency **for cold data**, with some queries experiencing up to a **283%** improvement.
* Caching Layer TCO: Replacing the local disk-based caching layer with S3 Express One Zone is expected to deliver up to a **65% reduction in TCO** for storing cached data due to reduced storage needs and elimination of data synchronization costs.
* Cost per Request: S3 Express One Zone offers a 50% reduction in request costs compared to S3 Standard, further contributing to cost savings.