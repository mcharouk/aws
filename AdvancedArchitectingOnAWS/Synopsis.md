# Module 2 : Single to Multiple Accounts


# Module 3 : Hybrid Connectivity

## ECMP

* Equal-Cost-Multi-Path
* The system acts like a load balancer and transmit the packet to multiple gateways behind the router that can reach the same destination.
* It consists of playing with BGP preferences (Local preference, weight) to give all connections the same weight.

## Direct Connect

### Quotas

* 50 Public or private VIF per Direct Connect connection (hard limit)
* 20 VGW per Direct Connect Gateway
  
### Public VIF

* connect to AWS Services without traversing the public internet
  * improved performance and security
  * can lower DTO rates. Don't have any additional cost compared to an interface endpoint
  * Don't need to explicitly call interface endpoint. Public IPs are redirected to Public VIF
  * Public VIF works for all public services, no need to create a public vif for each service, like interface endpoint
  * Public VIF can be used for all AWS regions, not just the Direct Connect one

### Site-to-site VPN

For connection on public VIF
   * the Customer Gateway IP advertised to AWS must be a public IP Address
   * a new Site-to-site VPN has to be created for each VPC
For connection on a transit VIF
  * no public ip adresses are needed
  * connection is made on TGW so there is only one VPN to create for all VPC behind the TGW

### MacSec

* Level 2 encryption
* no performance impact
* MACsec is supported on 10 Gbps , 100 Gbps, and 400 Gbps dedicated Direct Connect connections. 
* Must check that Dx location supports that.
* Check that your device on-premise supports MacSec.
* Create a CKN/CAK pair for the MACsec secret key

# Module 4 : Specialized Infrastructure

## VMWare Cloud on AWS

* SDDC is an account managed by VMWare. It's splitted in two parts
  * Management Gateway : utility tools 
    * vCSA
      * Centralized management platform for vSphere environments
      * Provides a web-based interface for managing virtual infrastructure
    * ESXi
      * Bare-metal hypervisor that installs directly on physical servers
      * Enables creation and management of virtual machines
    * NSX
      * Software-defined networking and security solution
      * Provides network virtualization and micro-segmentation
      * Enables creation of virtual networks and security policies
      * Offers distributed firewalling and load balancing
    * vSAN
      * Software-defined storage solution for hyper-converged infrastructure
      * Pools direct-attached storage devices to create a distributed shared datastore
      * Still can use EBS or EFS as storage but it's not the default solution of VMWare.
  * Compute Gateway : VMs created on physical hosts. 
* when provisioning the SDDC, the user is asked how many physical hosts should be reserved. This can be changed afterwards.
* Provide a customer account. Gives authorization by executing a cloudformation template to the SDDC to provide access to the SDDC account.
* VMWare VMs appears as ENI in customer account
* VMs can access all AWS Ressources in VPC (RDS for ex.) and all AWS Services through VPC private endpoints.
* Hybrid mode can be activated on SDDC to have a single pane of glass of all assets deployed on premises and on AWS.
* Allows to seamlessly 
  * migrate VMs on public cloud (storage & compute)
  * execute DR on public cloud
  * on-demand capacity for dev and test purposed for example.

## Outpost

* two LAG have to be established
  * LACP is a protocol that group multiple physical connection in a single logical connection. 
  * Main benefit is to improve resilience and bandwidth
* Each LAG has 2 VLANs
  * Service Link VLAN : connectivity between outpost and AWS
  * Local Gateway VLAN : connectivity between outpost and on-premise services
* BGP connectivity for both Service Link and Local Gateway
* Internet access can be provided to outpost resources by IGW of VPC or by on premise router
* For Service Link  
  * Can be through public internet
  * Through Direct Connect with public VIF
  * Through Direct Connect with private VIF

## WaveLength

* [WaveLength locations](https://aws.amazon.com/wavelength/locations/)
* CSP : communications service providers

# Module 5 : Connecting Networks

# Module 6 : Containers

## Placement Constraints and Strategies

* Fargate Tasks does not support placement constraints. Fargate tries to spread tasks among multiple AZs to improve availability, but customer has no control on that. 
* Use EC2 instances to apply custom placement constraints
* Cluster Queries are expressions to group objects by AZ, instance type, or any custom attribute that can be set at container instances.
* Task Placement Constraints : define which instances will be used for tasks. At least one instance must match the constraint.
  * distinctInstance : Place each task on a distinct instance
  * memberOf. Place task on container instances that satisfy an expression (can use custom attributes and cluster queries)
* Task Placement Strategies
  * binpack (save maximum resources): can be configured with CPU or Memory
  * random
  * spread (by instances id, or AZ)
* When managing EC2 instances, if an EC2 instance is terminated while it was in stopped status, ECS will not deregister it from the cluster automatically, you have to do it explicitly with the CLI.

# Module 7 : CI/CD

## CodeGuru

* CodeGuru Reviewer
  * Code Quality
  * Detect potential defects
* CodeGuru security
  * Security Scans
* CodeGuru Profiler
  * helps diagnose performance issues, works within a live environment. 
  * Need to modify the code to use it, and add dependencies.
* [Detector Library](https://docs.aws.amazon.com/codeguru/detector-library/). 
  * Has been renamed in Amazon Q Detector library
  * contains security and code quality checks
* Integrates with Github or Gitlab
* Integrates with Amazon Q
* Reviews accessible also on CodeGuru Console

## CodePipeline

* can integrate with other third party tools
  * Jenkins
  * TeamCity
  * XebiaLabs


# Module 9 : Securing datastore


## SSL Handshake

* Client send to the server a Hello message. It sends to the server
  * a client random (it's a random string)
  * TLS version supported
  * Cipher suites supported
* Server replies to the client by sending
  * a server random (random string)
  * its certificate
  * Cipher suites chosen to encrypt the data
* Client checks server certificate is signed by a CA the client trusts
* Client sends a pre master key encrypted with public key of certificate
* Server decrypts the pre master key with the private key it owns
* with pre master key, a session key is generated with client random and server random exchanged.
* session key is used for encryption operation afterwards

# Module 11 : Migrating Workloads


## Business Drivers

* Cloud migration business drivers:
  * Digital transformation
  * Going global quickly, migration and acquisition (M&A)
  * Agility and staff productivity
  * Internet of Things (IoT) and Artificial Intelligence/Machine Learning (AI/ML)
  * Improved operational resilience, scalability, and security
  * Data center consolidation
  * Cost reduction
  * Outsourcing changes – end of life with hardware and software (EOL HW/SW)

* Main Common drivers
  * Cost reduction
  * Workforce Productivity
  * Operational Resilience

## Migration Practices

* Communicate strategy broadly. How we want to achieve and why
* Cloud Governance Model. How managing access, account factory, separation of duties
* Train Staff
* Take Time to shape how operations will happened in the cloud (tools and processes)
* Know which assets you will migrate. Identify difficulties to minimize risks during migration. 

## Cloud Adoption Readiness Tool

* Answer a set of 47 questions
* Get recommendations on how to improve
* Get report that shows maturity to communicate it clearly

## MRA (Migration Readiness Assessment)

* Outcomes
  * An understanding of where an organization is in its cloud journey
  * Identified areas of strength and weakness from a cloud-readiness perspective
  * An action plan to resolve the identified gaps, so the organization can migrate at scale without having to pause to solve foundational issues

## Migration Evaluator

### Gathering Data

* Data can be collected by a tool or manually, providing a file
* The tool uses a non-intrusive, agentless collector to gather data
* automatically collects and inventories **your on-premises resources**, including servers, virtual machines, databases, and more.
* It collects data also on usage, not only static data
* Can be installed for bare metal or virtual machines discovery
* Inventory discovery works seamlessly across different environments such as VMware, Hyper-V, Windows, Linux, Active Directory, and SQL Server infrastructures.
* [Overview](https://d1.awsstatic.com/migration-evaluator-resources/migration_evaluator_overview.pdf)

### Insights

* The collected data is presented in detailed reports, allowing you to analyze the current infrastructure’s usage and performance, which aids in making informed decisions about migration to AWS.
* Available in the tool itself, or can be exported on a daily basis on AWS Migration Hub
* Provides a [one-page summary](https://d1.awsstatic.com/asset-repository/Migration_Evaluator_Quick_Insights_Sample_Report.pdf) for business stakeholders
* Breaks down costs by infrastructure and software licenses, offering a clear view of potential savings based on current usage patterns.

### Business Case

* you can request a Migration Evaluator Business Case. This advanced feature includes access to a team of AWS solution architects who will work with you to:
  * Understand your specific migration objectives, such as exiting a data center, transitioning from capital expenditures (cap-ex) to operational expenditures (op-ex), or altering software licensing strategies.
  * Use gathered data to identify the most appropriate migration patterns suited to your goals.

## MPA (Migration Portfolio Assessment)

* MPA are provided by AWS employees or partners, not available directly from Console
* Import data from file or **Application Discovery Service**

MPA helps you 
* consolidate the customer infrastructure data in one place
* build the business case by providing **TCO comparison between On-Premises and AWS**
* Estimate the **migration cost**
* **Plan the migration** through R-type strategies
* Application prioritization
* Dependency grouping
* Wave plans
* Some estimations are automatic (on AWS core services), some can be manual
* AWS Core services includes EC2, dedicated hosts, RDS, S3, EBS, network, admin, and aws support costs

## Application Discovery Service

* Agentless is installed centrally (one for many servers)
* as OVA on VMWare vCenter
* Covered by Agentless (Configurable)
  * VM inventory
  * configuration
  * Performance history such as CPU, memory, and disk usage
  * Version, edition and schemas of Databases (Oracle, MySQLServer, Postgresql, MySQL)
  * Network connections
* Covered by Agent (decentralized installation)
  * System configuration
  * System performance
  * Network Connection
  * Running processes
  * Collect higher resolution metric data (timeseries)
* Agent and Agentless can be both used at the same time
* Data is collected in Migration Hub
* Can optionnaly send data to S3 buckets and then use Quicksight or Athena for advanced analytics

## Application Migration Service

* install an Agent on the Source Server. Now can work with agentless on VmWare env.
* Replicate all block level data of all volumes attached to the instance (one can choose which one to copy)
* Can choose for each volume the appropriate destination volume.
* A Replication instance will be created on AWS that will replicate the data on one or multiple  EBS volumes
* When requesting a test or cutover instance, AWS will spin up an EC2 converter server that will convert EBS to a bootable volume on AWS
* After that operation (sub minute), an EC2 instance will be spin up that uses the EBS volumes
  * It's possible to launch a test instance before doing the real cutover
* When doing a cutover, stop all activity on source server, execute the migration, and redirect traffic to the new machine
* When a cutover or a test instance has been spin up, Replication is not stopped. It is stopped only when cutover has been finalized
* Launch template can be provided to instruct how EC2 instances should be created.
* Ability to group servers by Waves for mass migration, and group servers by a logical application to identify dependencies between servers


## Migration Hub Refactor Spaces

Easily build an infrastructure that can support Strangler Pattern.

* Define 3 acounts
  * One account as the refactor env. It contains an API Gateway that redirects traffic to the right backend (micro service or monolith)
  * One account as the microservice env
  * One account as the monolith env (which can be migrated on AWS or exists on Premise)
* Define routes (creates method integration in API Gateway) that defines where the traffic should be redirected

## AWS SCT

### Conversion

* can convert a schema into another schema of another DB engine
* conversion can be automatically written or completed manually
* can add data transformation rules that will be applied by DMS
* can convert ETL jobs into Glue jobs or Redshift SQL (more details [here](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP-converting-etl.html))

### SCT Agents
* For datawarehouse migration, with a help of an agent
  *  can extract data from the database to S3 or Snowball Edge
  *  Then another agent can copy data from s3 to Redshift
  *  Can parallelize with multiple agents
  *  Usually faster than DMS (thanks to parallelization) but no ongoing replication

### DMS integration

*  SCT can work with a local (on-premise) DMS replication instance. DMS replication instance will copy an initial load on S3, or S3 Snowball Edge
*  DMS replication instance will perform on going replication on S3
*  When Snowball Edge content is copied on S3, DMS will ingest data in the target database, and all ongoing changes.
*  

# Module 13 : Architecting for the edge

## Cloudfront signed cookies

### Canned policy vs Custom policy

These policies restricts the usage of a signed URL

custom policy
* you can reuse it for multiple files
* you can specify a start time
* specify the IP range that can access the content
* results in a longer url (BASE64 encoded)

you can specify an expiration time for both policies

## Cloudfront functions

### Limitations

* can't access the body of a request
* 10 Kb of code
* no file system access
* no external calls
* Javascript only
* max 2 Mb memory
* limited execution time (max is disclosed but you can monitor how close it in % from the maximum)

### Benefits

* consumes less resource
* Scale immediately to handle millions of requests per second
* submillisecond startup times

## Lambda@Edge vs Cloudfront functions

* Lambda@Edge runs on Regional Edge cache, whereas cloudfront Functions runs on Edge Location

Use Lambda when 

* long-running functions
* adjustable memory 
* Dependency on third libraries
* External calls

## Global Accelerator

* use edge locations, like cloudfront
* uses anycast
  * provides a set of IP adresses (2 ipv4 + 2 ipv6 eventually)
  * redirects the traffic to the nearest resource associated with that IP Address
* resources associated with Global Accelerator can be private, enhancing security
* Global Accelerator routes traffic the the healthy destination in case of regional failure.
* Global Accelerator 
  * listens to a port
  * redirects traffic from a port to a endpoint group
  * an endpoint group can contain multiple resources associated with a weight
  * a resource can be
    * NLB
    * ALB
    * EIP
    * EC2
* [Custom Routing accelerators](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-aws-global-accelerator-custom-routing-accelerators/) can be created to customize mapping between caller and the resource called
  * Global accelerator creates a static map between ip address and port exposed and ip addresses and port of private resources 
  * Then the client application can retrieve this static mapping and choose with a custom logic which resource it will call

* Pricing
  * fixed fee / hour
  * DTO (normal EC2 DTO)
  * Traffic between regions (price depends on source and target region)
  * Public IP addresses are charged at standard rate