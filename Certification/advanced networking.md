# IPV6

* Dual Stack supported for all DX VIFs (private, public, transit)
* Site-To-Site VPN does not support dual stack (Must create separate VPN connections)
* Site-To-Site VPN supports IpV6 on a TGW but not on a VGW
* TGW supports Ipv6 but needs an IpV6 attachment
* Public subnets are no use when using Egress only Internet Gateway
* Cannot choose IPv6 ranges, are all public. (no private ips)
* EKS does not support dual stack for pods and services. Must use Nitro instances or Fargate.


# Site-to-site VPN

## Basics 

* Two tunnels for HA (default), one in each AZ.
* 10 VPN Connections max for one VGW
* Open ports
  * TCP 50 and UDP 500. 
  * UDP 4500 for NAT Traversal

## HA

Static routing
* active/active : asymmetric routing should be enabled in CGW (already the case on AWS side)
* active/passive : tunnel which is UP is used for both directions. CGW handles failover

Dynamic routing
* parameters like CIDR prefixes, Local pref, AS PATH and MED can be used to influence the path.


## Accelerated Site-to-site VPN

* On premise will be redirected to a global accelerator endpoint
* Works only when attached to a transit gateway.
* NAT-traversal is required

## Certificates

* Certificate-based authentication uses digital certificates instead of pre-shared keys for IKE authentication.
* Certificates are issued from the ACM Private Certificate Authority.

# Direct Connect 

## Public vif

### Failovers

* active/active
    * private ASN : Not possible
    * public ASN : same prefix and path

* active/passive

    * private ASN : use CIDR specific prefixes
	* public ASN : use Local pref and Shortest AS PATH
		
### Scope BGP Communities

* OnPrem -> AWS
    * 7224:9300 (Global)
    * 7224:9200 (Continental)
    * 7224:9100 (Local)
* AWS -> OnPrem
    * 7224:8200 (Continent)
    * 7224:8100 (Local)
    * Must put a filter on customer side based on BGP community


## Private VIF

* longest prefix match first
* if two VIFs from Two DX locations, use the geographically closest one (can happen when using DX Gateway)
* if two VIFs are on the same DX location, choose Local Preference and then choose shortest AS PATH

* if two VIFs are in the same region, you can use AS PATH. If they are not in the same region this DOES NOT work. Use Local Preference instead.

* if a site-to-site VPN is set as backup, ensure that 
    * prefixes are the same
    * linked to the same VGW

## Local Preference BGP Communities

* 7224:7300: High
* 7224:7200: Medium
* 7224:7100: Low

## LAG

Letter of Authorization and Connecting Facility Assignment (LOA-CFA) is specific to each connection. 

If 2 connections should be added to an existing LAG, 2 more LAG must be requested

## Billing

* Port hours are billed to account that owns DX connection
* Data transfer charges are billed to the account that owns the resources that sends the traffic

## MacSec

* Hardware encryption
* no performance impact
* by port
* **CKA** (Connectivity Key Association ) is a pre-shared key
* Exchange **CKN** (Connection Key Name) and validate **ICK** (Integrity Check Key )
* A **Security Association Key** (SAK) is generated and distributed through MKA (MacSec Key Agreement) messages
* Data is encrypted with SAK

CKA and CKN to be provided when configuring a Direct Connect

## Direct Connect Gateway

* Sitelink used to allow communication between on-premises dc connected to DGW. Works with Transit VIF and private VIF

# CloudFront

## Edge Processing

* Lambda@Edge
    * Longer execution Times
    * CPU and Memory adjustable
    * Code Depends on a 3rd Lib
    * Use external services for processing
    * file system access or body processing
* CloudFront functions
    * Cache Key manipulation
    * Header Manipulation
    * URL rewrites / redirects
    * Request authentication / authorisation (JWT validation)

## Protocol Policy

### Viewer Protocol Policy

* Redirect HTTP To HTTPS
* HTTPS Only
* HTTP Only

### Origin Protocol Policy

* Match Viewer
* HTTP And HTTPS
* HTTPS Only

## Signed URLS

### Canned policy vs Custom policy

These policies restricts the usage of a signed URL

custom policy
* you can reuse it for multiple files
* you can specify a start time
* specify the IP range that can access the content
* results in a longer url (BASE64 encoded)

you can specify an expiration time for both policies

# Transit Gateway

## Attachments

* an attachment can propagate to 20 route tables
* an attachment can be associated with only 1 route table
* Resources that reside in Availability Zones where there is no transit gateway 
attachment cannot reach the transit gateway


## Multicast


* a subnet maps to a single domain
* different groups on a single domain.
* IGMP uses to subscribe/unsubscribe groups, but can be static as well
* A non-Nitro instance cannot be a multicast sender.
* When using a non-Nitro instance as 
a receiver, Source/Destination check must be disabled

## Shared TGW

* Through RAM
* Site-to-site VPN must be created in the same account that shared TGW
* Share only in ReadOnly mode.

# Routing tables

## Basic rules

* Cannot remove the default _local_ vpc route
* Cannot have two static routes that have the same destination

## Priority

* Longest prefix Match
* Static over propagated. if prefix are the same, VGW tends to not be prioritized because usually we enable the dynamic propagation. 
* For VGW router, DX Propagated over VPN static over VPN propagated

# BYOIP

## Preparation

Generate 
* RSA private key pair using AES 256
* public key
* X.509 certificate

## RIR Configuration

* add the certificate in RIR (Regional Internet Registry)
* Create a ROA (Route Origin Authorization) to allow AWS to advertise address range

# Global Accelerator

* no need of a public ip behind it, unlike CloudFront.
* still an internet gateway is required
  
Custom routing can be used to customize which resource will be called. Only supports VPC Subnet endpoints (no NLB, no ALB...).

# Route 53

## Routing policies

### simple policy vs multi value

It's possible to attach multiple IPs to a simple policy BUT not possible to attach a healthcheck to a simple policy. All ips will be systematically returned to client

Multi value allows to associate health check, returning only the healthy endpoints.

### IP Based routing

IP Based routing is routing based on the ip of client.
2 clients with different ips, on the same domain they will get back a different destination ip

## Healthchecks

Health checks on IP needs a public IP even if in a private hosted zone. That's why it's better to use CloudWatch alarms for health checks in a Private Hosted Zone

## Resolver

### Priorities

When records are declared in a private hosted zone, and an outbound resolver is configured in the same vpc, resolver takes precedence over private hosted zone records.

System rule can be used to override this priority for sub domains.

### Scaling

* it's possible to add IP addresses for a current resolver to scale.
* An ip address can handle 10 000 queries/s. 
* Max 6 ip addresses for a single resolver

## DNSSEC

* verify that a DNS record has not been tampered
* 2 keys
  * KSK : manged by customer
  * ZSK : managed by AWS
* Steps 
  * Lower TTL and SOA
  * Enable DNSSEC and create a KSK
  * Create a DS (Delegation Signer) record in the **parent** zone 
  * Monitor for errors KSK renewal, DNSSECInternalFailure

# ASN

* CloudHub : each customer gateway with a unique ASN
* Transit Gateway : Use unique ASNs for peered transit gateways (TGW peering does not use BGP, but may use it in the future. Maybe CloudWAN use it ?)

7224 is AWS public ASN.

2 bytes
* Public ASN : 1 to 64495
* Private ASN : 64512 to 65534

4 bytes
* Public ASN : 1 to 2147483647
* Private ASN : 4200000000 to 4294967294

 


# ENA

Multi flow (MPTCP)
* Take full advantage of ENA
* Full Bandwidth available when in same region
* 50% of bandwidth usage when cross region, or IGW or DX
* Limitation to 5 Gbps if instance < 32 vCPU

Single flow

* Limitation to 5 Gbps when not in a placement group
* With ENA Express, up to 25 Gbps

ENA Activation

* All instance type except T family supports ENA.
* OS or AMI must support it. Just pick the right AMI.

# ECS

* can only attach 5 target group to a single service
* if multiple target groups, must use rolling update controller type
* ip target type mandatory for NLB when using awsvpc mode
* containers can belong to multiple target groups
* dynamic host port mapping used to have multiple containers on a single instance. ENI will be assigned an ephemeral port that will point to a specific container and port

## Network modes

* host mode : container uses underlying host ports
  * Not recommended. Does not work on Fargate
  * it's not possible to have multiple instance of the same task on a single node. 
  * Ports have to be assigned in static way.
  
* bridge mode : port mapping between container and host  
  * multiple container instances can run on the same host.
  * Ports can be assigned static or dynamic.
  * In a dynamic, the mappings are automatically updated in CloudMap or in ELB
  * Issues for a service to service communication as ports mapping are ephemeral
  * Not supported on Fargate
 
* awsvpc : ENI and IP assigned to each task
  * each task with its own security group
  * Only option supported by Fargate
  * don't need dynamic port mapping has each task has its own IP. they can be mapped on the same port.
  * The main disadvantage is number of tasks is limited by the number of ENI, and number of IP it supports (depends on the instance). ENI trunking can alleviate the issue.

# SES

* port 587 for TLS (smtp) must be used to encrypt the data.
* port 465 is a TLS wrapper, that lets the client's responsibility to encrypt the flow.

# Traffic Mirroring

Traffic mirroring DOES NOT inspect packets !
* filters can be setup that works similar to NACL (first rule match)
* can be redirected to an ENI, NLB or GLB
* On NLB or GLB, messages are received out-of-order

# Security Groups

Default security group of a a default VPC : 
* allows inbound connections from itself
* allows all outbound connections

Newly created security group : 
* No inbound rules (implicit deny)
* allows all outbound connections


# Private NAT Gateway

* A consumer wants to get data from a producer
* Put resources in a dedicated subnet (non routable), for both producer and consumer
* Create a NAT Gateway in a routable subnet, on consumer side.
* Create an ALB in the producer routable subnet.
* Communication flow through NAT Gateway, an ALB on the other side, which redirects in the non routable address of the producer

In the middle there might be a TGW or some VGW if overlapping addresses are on premise.

# ALB

/27 subnet at least mandatory for ALB.
ALB takes 8 Ip addresses

X-Forwarded-For header cannot be used in a condition rule. http-header must be used for that purpose.


# EKS

## Network Topology

* Dedicated subnets to communicate with control plane
* EKS provisions 2-4 IPs in each AZ
* Recommended to have at least 6 ips (16 recommended) in each AZ

## NAT
Allows to translate pod address instead of Node Primary IP Adress.


External NAT to true means the NAT is not managed by the node, but by a NAT Gateway

```
AWS_VPC_K8S_CNI_EXTERNALSNAT=true
```

## Security groups

Allow trunk of ENIs to attach specific Security group to a pod group

```
ENABLE_POD_ENI=true 
```

* only Linux
* if IpV6 only works with Fargate
* Nitro based instances : Node instances should be listed in limits.go file 
with IsTrunkingCompatible: true

## Load Balancing 

**!! Only for NLB !!**

```
externalTrafficPolicy=Cluster
externalTrafficPolicy=Local
```

Cluster mode
* Client IP not preserved (take Node Ip Address instead)
* evenly distributed traffic

Local Mode
* Traffic unevenly distributed. Always redirected to the same node.
* client ip address is preserved



For ALB, client id is in X-Forwarder-For header

## Custom Networking

On a single node : 
* One ENI in a routable CIDR range
* Other ENIs in a non routable CIDR Range.

Pods are created in the non rootable space, but NAT translation must be activated on node level

```
AWS_VPC_K8S_CNI_CUSTOM_NETWORK_CFG=true
AWS_VPC_K8S_CNI_EXTERNALSNAT=false
```

## ENI and IP Allocation

* MINIMUM_IP_TARGET : minimum number of ip addresses allocated on node initialization
* WARM_IP_TARGET : number of IP addresses in L-IPAMD warm pool
* WARM_ENI_TARGET : How many ENI L-IPAMD keeps available so that pods are immediately assigned an IP Address when scheduled
* WARM_PREFIX_TARGET : number of prefixes (/28 blocks) assigned to an ENI
* MAX_ENI : maximum ENI attached to a node

# CIDR Ranges

| cidr range  | int. number | termine par  |
| ----------- | ----------- | ------------ |
| 10.0.0.0/17 | 256/2 = 128 | 10.0.127.255 |
| 10.0.0.0/18 | 128/2 = 64  | 10.0.63.255  |
| 10.0.0.0/19 | 64/2 = 32   | 10.0.31.255  |
| 10.0.0.0/20 | 32/2 = 16   | 10.0.15.255  |
| 10.0.0.0/21 | 16/2 = 8    | 10.0.7.255   |
| 10.0.0.0/22 | 8/2 = 4     | 10.0.3.255   |
| 10.0.0.0/23 | 4/2 = 2     | 10.0.1.255   |

# Shared VPC

* dedicated subnets in production for each participant to reduce blast radius, avoid ip exhaustion...
* can have shared VPC for non production, for a sandbox for example
* Dedicated subnets for shared AWS infra components : NAT Gateway, Firewall, Internet Gateway, Private Link, etc...