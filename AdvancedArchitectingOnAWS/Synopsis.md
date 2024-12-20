# Table of contents

- [Table of contents](#table-of-contents)
- [Module 2 : Single to Multiple Accounts](#module-2--single-to-multiple-accounts)
  - [Control Tower](#control-tower)
- [Module 3 : Hybrid Connectivity](#module-3--hybrid-connectivity)
  - [Client VPN](#client-vpn)
    - [Protocols](#protocols)
    - [Connectivity](#connectivity)
    - [Components](#components)
  - [Site-to-site VPN](#site-to-site-vpn)
    - [Dead peer connection](#dead-peer-connection)
    - [Nat-T](#nat-t)
    - [ECMP](#ecmp)
  - [Direct Connect](#direct-connect)
    - [Quotas](#quotas)
    - [Public VIF](#public-vif)
    - [Site-to-site VPN](#site-to-site-vpn-1)
  - [Resiliency](#resiliency)
  - [Failover](#failover)
    - [MacSec](#macsec)
  - [Route 53](#route-53)
    - [DNSSEC](#dnssec)
- [Module 4 : Specialized Infrastructure](#module-4--specialized-infrastructure)
  - [Storage Gateway](#storage-gateway)
  - [VMWare Cloud on AWS](#vmware-cloud-on-aws)
  - [Local Zones](#local-zones)
  - [Outpost](#outpost)
  - [WaveLength](#wavelength)
- [Module 5 : Connecting Networks](#module-5--connecting-networks)
  - [Transit Gateway Multicast](#transit-gateway-multicast)
  - [Transit Gateway Network Manager](#transit-gateway-network-manager)
- [Module 6 : Containers](#module-6--containers)
  - [Launch types](#launch-types)
  - [Placement Constraints and Strategies](#placement-constraints-and-strategies)
    - [Placement Strategies](#placement-strategies)
    - [Placement constraints](#placement-constraints)
    - [Tasks group](#tasks-group)
  - [Capacity provider](#capacity-provider)
  - [Networking mode](#networking-mode)
  - [Task definition](#task-definition)
  - [Container Insights](#container-insights)
  - [EKS Distro](#eks-distro)
  - [EKS anywhere](#eks-anywhere)
- [Module 7 : CI/CD](#module-7--cicd)
  - [CodeGuru](#codeguru)
  - [CodePipeline](#codepipeline)
    - [Out of the box Action (not exhaustive)](#out-of-the-box-action-not-exhaustive)
    - [Custom Actions](#custom-actions)
    - [Immutable vs Blue Green](#immutable-vs-blue-green)
- [Module 8 : High Availability - DDoS](#module-8--high-availability---ddos)
  - [Shield Advanced](#shield-advanced)
  - [AWS WAF Security Automations](#aws-waf-security-automations)
  - [Network Firewall](#network-firewall)
- [Module 9 : Securing datastore](#module-9--securing-datastore)
  - [Key Rotation](#key-rotation)
  - [Cloudtrail example](#cloudtrail-example)
  - [Asymetric keys](#asymetric-keys)
  - [CloudHSM](#cloudhsm)
  - [SSL Handshake](#ssl-handshake)
  - [Secrets Manager](#secrets-manager)
- [Module 10 : Large Scale Data Stores](#module-10--large-scale-data-stores)
  - [Storage Class analysis](#storage-class-analysis)
  - [Intelligent Tiering](#intelligent-tiering)
  - [S3 Inventory](#s3-inventory)
  - [Storage Lens](#storage-lens)
- [Module 11 : Migrating Workloads](#module-11--migrating-workloads)
  - [Business Drivers](#business-drivers)
  - [Migration Practices](#migration-practices)
  - [Cloud Adoption Readiness Tool](#cloud-adoption-readiness-tool)
  - [MRA (Migration Readiness Assessment)](#mra-migration-readiness-assessment)
  - [Migration Evaluator](#migration-evaluator)
    - [Gathering Data](#gathering-data)
    - [Insights](#insights)
    - [Business Case](#business-case)
  - [MPA (Migration Portfolio Assessment)](#mpa-migration-portfolio-assessment)
  - [Application Discovery Service](#application-discovery-service)
  - [Application Migration Service](#application-migration-service)
  - [Migration Hub Refactor Spaces](#migration-hub-refactor-spaces)
  - [AWS SCT](#aws-sct)
    - [Conversion](#conversion)
    - [SCT Agents](#sct-agents)
    - [DMS integration](#dms-integration)
- [Module 13 : Architecting for the edge](#module-13--architecting-for-the-edge)
  - [Cloudfront signed cookies](#cloudfront-signed-cookies)
    - [Canned policy vs Custom policy](#canned-policy-vs-custom-policy)
  - [Cloudfront functions](#cloudfront-functions)
    - [Limitations](#limitations)
    - [Benefits](#benefits)
  - [Lambda@Edge vs Cloudfront functions](#lambdaedge-vs-cloudfront-functions)
  - [Global Accelerator](#global-accelerator)
    - [Standard Accelerators](#standard-accelerators)
    - [Custom Routing Accelerators](#custom-routing-accelerators)
    - [Pricing](#pricing)

# Module 2 : Single to Multiple Accounts

## Control Tower

* possible to add custom shared account
  * no specific process for that
  * create an account, setup it manually and enroll it in an appropriate OU
* To customize account by other means
  * listen to Control Tower events in Eventbridge (CreateManagedAccount event)
  *  possible to execute a lambda to setup the account.
     * Lambda can assume the role AWSControlTowerExecution to perform actions in the target account.
     * it can do pretty much anything, like executing a step function, executing cloudformation stack sets, etc...
* Possible to use CfCT to customize landing zone. It's a pre built architecture that automate account setup and does not rely on service catalog (triggered on eventbridge event)

# Module 3 : Hybrid Connectivity

## Client VPN

### Protocols

* OpenVPN protocol (UDP or TCP, default to UDP)
* Uses TLS for secure communication
* Authentication 
  * SAML based
  * Active directory
  * Mutual authentication (certificate)

### Connectivity

* [multiple connections](https://aws.amazon.com/blogs/networking-and-content-delivery/using-aws-client-vpn-to-scale-your-work-from-home-capacity/)
  * connect to a target VPC subnet
  * can access other VPCs via VPC peering or Transit Gateway
  * can access on premise resources via private connections
  * can access aws services privately
  * can access internet through VPC IGW (can be integrated with Network Firewall or other appliances)

### Components

* Authorization rules can be provided to authorize some users that belong to a specific group to reach only a specific ip range
* Route table indicates which target of VPN endpoint are valid independently from the users

## Site-to-site VPN

### Dead peer connection

* deadPeerConnection is like a health check mechanisms. After some timeout the peer is considered as not joinable. Possible actions : 
  * Do Nothing
  * Close the tunnel
  * Restart the tunnel
* on CGW side, it can detect failure and start failover automatically

### Nat-T 

* Nat traversal consists of having a server that performs NAT in front of the router that acts as a customer gateway.
* Nat traversal is stateful and supports inbound connections as well, so ideal for peer-to-peer connections.
* Nat traversal keeps the same advantages of NAT
  * fewer public IP addresses
  * hide private IP addresses
* Mandatory for accelerated site-to-site connections.

### ECMP

* Equal-Cost-Multi-Path
* The system acts like a load balancer and transmit the packet to multiple gateways behind the router that can reach the same destination.
* It consists of playing with BGP preferences (Local preference, weight) to give all connections the same weight.
* only supported with BGP, and with TGW connection

## Direct Connect

### Quotas

* 50 Public or private VIF per Direct Connect connection (hard limit)
* 20 VGW per Direct Connect Gateway
* frame size up to 9 023 bytes (maximum packet size)
  
### Public VIF

* connect to AWS Services without traversing the public internet
  * improved performance and security
  * can lower DTO rates. Don't have any additional cost compared to an interface endpoint
    * from AWS Europe to on prem in Europe
      * Direct connect $0.0200 per GB
      * EC2 : $0.09 per GB for first 10 TB / month
      * EC2 (max mass discount): $0.05 per GB for vol > 150 Tb / month
  * Don't need to explicitly call interface endpoint. Public IPs are redirected to Public VIF
  * Public VIF works for all public services, no need to create a public vif for each service, like interface endpoint
  * Public VIF can be used for all AWS regions, not just the Direct Connect one

### Site-to-site VPN

* [VPN Over public VIF](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect-aws-transit-gateway-vpn.html)
   * Create a connection between on prem network and site-to-site vpn endpoints
   * the Customer Gateway IP advertised to AWS must be a public IP Address
   * Then create an IP Sec connection to the Transit Gateway directly
   * When it was the only option available, to use a private IP address, customer had to manage a VPN on EC2 to establish IPSec connectivity through Direct Connect
   * Private IP VPN solved that burden

## Resiliency

* AWS has [SLA engagement](https://aws.amazon.com/directconnect/sla/?did=sla_card&trk=sla_card) depending on the setup. 
* If SLA are not met, AWS can redeem credits to customer
* The conditions depends on the client setup. Maximum resiliency have the best SLA.

## Failover

* How to detect failure in direct connect connection
  * Cloudwatch metrics : connection state, BGP state
  * Health Dashboard
  * BFD (Bidirectional Forwarding Detection) if it has been activated
* How to detect failure in VPN connection
  * TunnelState CloudWatch metric
  * API calls / Cloudwatch synthetics
  * Dead peer detection
* Failover parameters are more typically set on customer side
  * Typically BGP parameters are used to favor traffic on Direct Connect during normal traffic
    * Local preference to influence traffic to AWS
    * to influence inbound traffic from AWS
      * MED values
      * Shortes AS Path
  * When a failover occurs
    * AWS removes routes in routing table that were propagated by DX.
    * if BGP session is down, all routes learned on premise by DX will be removed automatically. 
    * Site to site VPN routing will remain, so it will become the preferred path defacto
    * Just make sure that all BGP parameters are ok, and that nobody has added some static routes that may disturb the failover process

### MacSec

* Level 2 encryption
* no performance impact
* MACsec is supported on 10 Gbps , 100 Gbps, and 400 Gbps dedicated Direct Connect connections. 
* Must check that Dx location supports that.
* Check that your device on-premise supports MacSec.
* Create a CKN/CAK pair for the MACsec secret key

## Route 53

### DNSSEC

* exchange private / public keys
  * private key stays on authoritative servers
  * public keys given to resolvers
* When a record is returned, a signature is also sent generated with record, domain name, record type (A, AAAA, etc...), and other metadata such as an expiration date.
* resolver decrypts signature and check if it matches with authoritative response
* if it doesn't match, an error is raised to the client

# Module 4 : Specialized Infrastructure

## Storage Gateway

* One limitation on Storage Gateway
  * suppose multiple gateways refer to the same S3 bucket for example, for example in different locations
  * cache in those different gateways won't be synchronize anyway
  * could potentially do some solution to evict from the cache object based on their update, but this could to a lot refresh, latency, etc...
  * Storage gateway is not really meant for that setup, so it could require a different solution

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
  * Compute Gateway
    * enables communication between VM and external networks
    * firewalls to control traffic
    * Facilitates internet connectivity to workloads
* when provisioning the SDDC, the user is asked how many physical hosts should be reserved. This can be changed afterwards.
* Provide a customer account. Gives authorization by executing a cloudformation template to the SDDC to provide access to the SDDC account.
* VMWare VMs appears as ENI in customer account
  * Natively, VMs have only access to resources in that particular VPC
  * [Other options](https://aws.amazon.com/blogs/architecture/augmenting-vmware-cloud-on-aws-workloads-with-native-aws-services/) might be configured to access to resources in multiple VPC in multiple accounts. It uses a VMWare component called VMWare Transit Connect (VTGW)
* VMs can access all AWS Ressources in VPC (RDS for ex.) and all AWS Services through VPC private endpoints.
* Hybrid mode can be activated on SDDC to have a single pane of glass of all assets deployed on premises and on AWS.
* Allows to seamlessly 
  * migrate VMs on public cloud (storage & compute)
  * execute DR on public cloud
  * on-demand capacity for dev and test purposed for example.

## Local Zones

* in the console, go to EC2
* in the menu go to Settings
* go to the Zones tab to enable a local zone
* when creating a subnet, select the local zone that was enabled
* create resource in the local zone subnet

## Outpost

* two LAG have to be established
  * LAG purpose is to group multiple physical connections to a single logical connection
  * Uses LACP protocol for that purpose
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
* Use cases : Smart factories, Connected Vehicules
* 
# Module 5 : Connecting Networks

* CloudWAN when network is complex and span multiple regions as there is dynamic propagation of routes between multiple regions

## Transit Gateway Multicast

* Benefits
  * Reduces network bandwidth usage
  * Improves scalability
  * Lower server load
  * real time data delivery

* Use cases
  * Streaming, Video conferencing
  * Network management (DNS updates, DHCP services)
  * Financial Services : Stock market data distribution, real time trading information, financial news feeds
  * Gaming : Multiplayer, gamestate synchronization
  * Data distribution : software updates, database replication, file distribution, CDN
  * IoT : Sensor data distribution, industrial control systems
  * DR : Alert systems, public safety annoucements

## Transit Gateway Network Manager

* Site : registering a physical location (typically branch office, head quarters, etc...)
* Links : connection between device and site
* Devices : Some physical or virtual appliance that can be associated with AWS resources, or on premise (through a link)
* Customer Gateway associations
  * Customer Gateway will be already created if TGW is associated with an hybrid connection.
  * associate a CGW to a device and optionally a link. 

# Module 6 : Containers

* EKS works with docker or containerd
* ECS works only with Docker
* ECS Agent is open source. 

## Launch types

ECS can run 
* on EC2
* on Fargate
* on any VMs (ECS anywhere)

* ECS Anywhere is the capacity to launch ECS tasks on instances external to AWS. But the control plan is still managed by AWS.

## Placement Constraints and Strategies

* Fargate Tasks does not support placement constraints. Fargate tries to spread tasks among multiple AZs to improve availability, but customer has no control on that. 
* Use EC2 instances to apply custom placement constraints
* Priorities (in this strict order)
  * identify instances that have enough CPU, RAM, etc...  
  * identify instances that satisfy placement constraints
  * identify instances that satisfy placement strategies (defined at Service level , or on running a task)
* Task placement strategies are a best effort. Amazon ECS still attempts to place tasks even when the most optimal placement option is unavailable. 
* However, Task placement constraints are binding, and they can prevent task placement.
* if placement constraints are not met
  * task remain in PENDING state
  * an event is sent in EventBridge to notify that task has not been instantiated
  * still the scheduler will keep the task in the queue, waiting to the constraint to be satisfied
  * Cloudwatch alarms can be triggered if a task remain in pending state for some period of time.

### Placement Strategies

* Task Placement Strategies
  * binpack (save maximum resources): can be configured with CPU or Memory
  * random
  * spread
    * by instances id
    * by AZ (default behavior)

### Placement constraints


* Task Placement Constraints : define which instances will be used for tasks. At least one instance must match the constraint.
  * distinctInstance : Place each task on a distinct instance 
  * memberOf. Place task on container instances that satisfy an expression (can use custom attributes and cluster queries)
  * Cluster Queries are expressions to group objects by AZ, instance type, or any custom attribute that can be set at container instances.
  * Examples

selects G2 instances that aren't in the us-east-1d Availability Zone.

```
attribute:ecs.instance-type =~ g2.* and attribute:ecs.availability-zone != us-east-1d
```

instances that are hosting tasks in the service:production group.

```
task:group == service:production
```

### Tasks group

* Tasks can be placed into a group. 
  * strategies and placement constraints will be applied to the group.
  * by default, group name = task definition family name

## Capacity provider

* in a single cluster, can run tasks on Fargate or EC2
* Only one capacity provider will have a *base* that will define how many tasks should be run at minimum
* *weight* is the percentage of tasks that run on a capacity provider

## Networking mode

* Only for EC2 launch type
  * awsvpc
    * the task has an ENI allocated.
    * can have its own public ip address, and its own security group
  * bridge
    * Uses Docker's built-in virtual network
    * map container port to an EC2 instance port
      * static port : cannot run more than a single task instance on an EC2 instance
      * dynamic port : Docker chooses a random unused port in ephemeral port range
        * must open broad ranges of port to make sure firewall will not block the traffic
        * ECS will update Load balancer or Cloud Map dynamically to match assigned ports
    * Security group is at EC2 level, not at task level, because containers share the same ENI
  * host
    * rigid, has the port used on EC2 is the same as the container
    * not recommended by AWS. 
      * Subject to port conflict
      * Cannot run more than a single task instance on an EC2 instance

## Task definition

* Family (just a name)
* launch types
* Task Execution Role
* Network Mode
* Runtime platform
  * Linux/Windows
* Task size (CPU/Mem)
* Container definitions
  * A task might contain multiple containers. Define here ECR URI, CPU/Mem, Port mapping, mount points, secrets, logs, linux users, etc...
* Placement constraints (strategies are defined at ECS service level)
* Volumes

## Container Insights

* Metrics on CPU, memory, disk, network
* Diagnostics information on restart failures for ex.
* Collect raw [performance log events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-reference-performance-logs-ECS.html)
  * Metrics aggregated at cluster, node, task, service level.
  * Can create custom metric from these raw performance log events
  * [Collected Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-ECS.html)
  * [Container Insights with Enhanced observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-enhanced-observability-metrics-ECS.html). It offers more metrics
* Automatic dashboards

## EKS Distro

* CNI plugins
* CoreDNS
* etcd
* CSI sidecars
* aws-iam-authenticator
* Kubernetes Metrics Server
* Kubernetes

## EKS anywhere

* full cluster Kubernetes that run on EKS Distro distribution but it has more tooling around 
  * installation and update EKS
  * Diagnostic and logging
  * Pre-configured K8S add-ons
    * CNI
    * CoreDNS
    * kube-proxy
    * AWS Distro for OpenTelemetry
    * EBS CSI Driver
    * EFS CSI Driver
    * Cluster Autoscaler
    * Metrics Server
  * Support
  * Can integrate easily with 
    * IAM for cluster authorizations
    * Systems Manager
  * Management Console integration (EKS Connector)

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

### Out of the box Action (not exhaustive)

* For build step action
  * ECR
  * CodeBuild
  * *Jenkins*
  * *TeamCity*
* For deploy steps
  * *XebiaLabs*
  * CloudFormation
  * CodeDeploy
  * S3
  * ECS
  * AppConfig

### Custom Actions

* Lambda
* Job Worker that pulls for jobs and send responses by using CodePipeline APIs

### Immutable vs Blue Green

* idea of immutable deployments is 
  * to create a whole environment
  * switch traffic all at once. 
  * Then old environment is deleted.
  * The main point here is that there is no in-place deployment, a new infra is always created from scratch
* Blue Green looks like immutable but 
  * it allows a more progressive traffic switch
  * old environment could be kept for quick rollback long after the release
* Immutable deployments can be implemented by using a blue/green strategy, but not the opposite.

# Module 8 : High Availability - DDoS

## Shield Advanced

* When protecting an EIP address, Shield Advanced can replicate NACL rules on the public subnet where it resides at the border of AWS. it allows supporting much bigger volume
* Shield advanced can monitor health checks of associated resources (must be provided explicitly). This helps to detect a DDoS attack and lower the threshold Shield will react.
* Shield integrates with WAF. It can
  * add IP addresses to deny
  * apply rate limiting rules
  * block an attack that has an identified signature

## AWS WAF Security Automations

* Application Log Parser
  * parse Cloudfront and ALB logs 
  * identify IP addresses that generated more **errors** than the defined quota
  * Block IP Addresses with WAF for a customer-defined period of time

* WAF Log Parser
  * parse Cloudfront and ALB logs 
  * identify IP addresses that **sent more requests** than the defined quota
  * Block IP Addresses with WAF for a customer-defined period of time
* IP List Parser
  * Hourly Update IP Reputation list from these 3 suites
    * Spamhaus DROP and EDROP lists
    * Proofpoint Emerging Threats IP list
    * Tor exit node list
* Access Handler
  * a Lambda can be integrated in CloudFront or ALB (used by the application). This Lambda is meant to be accessed by content scrapper or bots that might be looking for a vuln.
  * the Lambda extracts the source IP address and add it to the IP blacklist of WAF

## Network Firewall

* Stateless or stateful rules (like NACL and Sec Group)
* Domain filtering
  * black list or white list some domain
  * filter based on content- [Suricata rules](https://docs.suricata.io/en/latest/rules/index.html#)
  * Some [Suricata examples](https://docs.aws.amazon.com/network-firewall/latest/developerguide/suricata-examples.html)


# Module 9 : Securing datastore

## Key Rotation

* can enable automatic rotation or on demand rotation (can use both at the same time)
* Old material is never deleted, but the key alias is pointed to the new key
* KMS will by itself select the right key that was used to encrypt the data.
  *  Basically it stores in metadata of the object, the version used to encrypt it.
  *  No re-encryption is needed after a key rotation
*  When using imported keys
   *  when the key is deleted the id is not. 
   *  It's possibe to re-import the key to use it again
   *  These keys can be deleted without a waiting period
   *  Can specify an expiration time when importing the key
*  AWS-Managed keys are rotated every year (cannot be changed)
*  When using imported key or external key store, if old keys are deleted, data will have to be re-encrypted with new key

## Cloudtrail example

* it's a decrypt operation with a symmetric key (encryption context works only for symmetric keys)

* DecryptResult : decrypt a ciphertext string
* Keyid : KMS key used to encrypt
  * Not mandatory if key is symmetric because this info can be retrieved in object metadata (added to the ciphertext blob) 
* Encryption context : additional security. 
  * It's a plain text string that must be given for decryption (same that was used for encryption). 
  * Only works with symmetric keys

## Asymetric keys

* private key stored in AWS. Never leaves AWS.
* public key can be given to anyone. 
  * Anyone who own this key can encrypt data without having to access KMS API.
  * only private key can decrypt the data
* Limitations
  * Most of AWS Services uses only Symmetric encryption
  * No automatic rotation
  * No key import
  * limitations of object size that can be encrypted
  * less performant

## CloudHSM

* can create a cluster. Can add or remove nodes up to 28.
* active/active
* synchronization between clusters members is automatic
* AWS manages Load balancing
* Quorum authentication : some operations needs at least *n* users to execute them (approval workflow)
  * create or delete users
  * change user password
* As a convenience, define CloudHSM as an external key store of KMS, and use KMS APIs to generate data keys.
  * encryption is done on the HSM cluster
  * keys are stored in the HSM cluster
* can use AWS Encryption SDK to generate data keys. 
  * It supports KMS, CloudHSM and third parties HSM. 
  * It's an open source project that facilitates envelope encryption process
* pricing : hourly price per HSM. 
  * For ex. 2,18 $ per hour per HSM in Paris region. 
  * Approx. 1500 $ / month / cluster

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

## Secrets Manager

* [Rotation lambdas samples](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas)

# Module 10 : Large Scale Data Stores

## Storage Class analysis

* Can be specified by prefix, by object tags, or for all bucket objects
* Can generate a csv export daily
* Provides only recommendations from Standard to IA
* Observes data access patterns for 30 days or longer before giving a results
* First results in 24 to 48 hours
* Analysis basis : storage size and number of bytes transferred out per age group
* provide visual dashboards
* classified as Frequently accessed or infrequently accessed
* CSV provides a RecommendedObjectAgeForSIATransition

## Intelligent Tiering

* Actions that Automatically moves back objects to Standard class
  * Downloading or copying object
  * Invoking CopyObject, UploadPartCopy, replicating with Batch Replication
  * Invoking GetObject, PutObject, RestoreObject, CompleteMultiPartUpload, ListParts
* Lifecycle default rules 
  * Objects are moved in IA after 30 days
  * Moved to Archived Instant Access Tier after 90 days
  * Archive Access Tier (optional) : Move customizable from 90 to 730 days
  * Deep Archive Access Tier (Optional): Move customizable from 180 to 730 days

## S3 Inventory

* [Available fields](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-inventory.html)
* daily or weekly basis
* eventual consistency (some objects might not appear immediately)

## Storage Lens

* can create a Storage Lens Group with object tags
* Storage Lens can filter by storage class
* not possible to combine those two filters in dashboard
* To have more customized results
  * Get Storage Lens export Data (CSV, Parquet)
  * Perform a custom analysis with Athena for ex.
  * Can also join with S3 Inventory export to gain more flexibility
* Provide recommendations
  * Cost Optimization
  * Data protection
  * Access Management
  * Performance
  * Storage Management
* Metrics in those categories
  * Summary metrics
    * total volume
    * object count
  * Cost Optimization metrics
    * incomplete multipart uploads
    * S3 lifecycle rule count (nb of rules on non current version, nb of rules that expires objects...)
  * Data protection
    * % of encrypted data
    * % of replicated objects
    * volume of objects that are locked
    * MFA delete
  * Access Management metrics
    * around S3 object ownership
  * Event metrics
    * S3 event notifications  
  * Performance metrics
    * for Transfer acceleration
  * ACtivity metrics
    * nb of put requests, get requests, Bytes uploaded, downloaded, etc..
  * Detailed Status code metrics
    * count of status code (5XX, 4XX, 2XX, etc...)

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

### Standard Accelerators

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

### Custom Routing Accelerators

* [Custom Routing accelerators](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-aws-global-accelerator-custom-routing-accelerators/) can be created to customize mapping between caller and the resource called
  * Global accelerator creates a static map between ip address and port exposed and ip addresses and port of private resources 
  * Then the client application can retrieve this static mapping and choose with a custom logic which resource it will call

* Some limitations
  * no healthcheck
  * no load balancing
  * only redirects to EC2 instances

### Pricing

* fixed fee / hour
* DTO (normal EC2 DTO)
* Traffic between regions (price depends on source and target region)
* Public IP addresses are charged at standard rate