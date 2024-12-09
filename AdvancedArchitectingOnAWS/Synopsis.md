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
* Take Time to shape how operations will happened in the clou (tools and processes)
* Know which assets you will migrate. Identify difficulties to minimize risks during migration.

## MRA (Migration Readiness Assessment)

* Outcomes
  * An understanding of where an organization is in its cloud journey
  * Identified areas of strength and weakness from a cloud-readiness perspective
  * An action plan to resolve the identified gaps, so the organization can migrate at scale without having to pause to solve foundational issues

