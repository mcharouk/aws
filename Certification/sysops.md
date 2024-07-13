# ASG

## EC2 Termination

terminate an instance in ASG without changing its desired capacity

```
terminate-instance-in-auto-scaling-group --instance-id <value>  --no-should-decrement-desired-capacity
```

## Suspended processes

* If you suspend **AZRebalance** and a scale-out or scale-in event occurs, the scaling process **still tries to balance the Availability Zones**. For example, during scale-out, it launches the instance in the Availability Zone with the fewest instances.

- If you suspend the **Launch** process, **AZRebalance neither launches new instances nor terminates existing instances**. This is because AZRebalance terminates instances only after launching the replacement instances.

- If you suspend the **Terminate** process, your Auto Scaling group can grow up to **10%** larger than its maximum size because **this is allowed temporarily** during rebalancing activities. If the scaling process cannot terminate instances, your Auto Scaling group could remain above its maximum size until you resume the Terminate process.


## Scale in protection

It's possible to [protect resources from scaling in](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-instance-protection.html#instance-protection-instance)

* at EC2 instance level
* at ASG level

Sample command

```
aws autoscaling set-instance-protection --instance-ids i-5f2e8a0d --auto-scaling-group-name my-asg --protected-from-scale-in
```

# S3

* HTTP error 503 Slow Down indicates that the number of requests to your S3 bucket is high. It can indicate a bucket where one or multiple objects have millions of versions.
* a Content-MD5 value can be passed as a request header to check the integrity of the file
* MFA Delete. Without MFA
  * cannot delete any object
  * cannot change versioning state of a cluster

# Glacier

* To save costs on Glacier it's better to store large files over small files
  * A fixed amount of storage is added to the objects which are used for metadata
  * There is a one time transition charge to Glacier, per object.


# KMS

Provide these headers to encrypt with a customer provided key

* x-amz-server-side​-encryption​-customer-**algorithm** (must be AES256)
* x-amz-server-side​-encryption​-customer-**key** (256-bit, base64-encoded encryption key)
* x-amz-server-side​-encryption​-customer-**key-MD5** (a digest to check key has not been altered)
* x-amz-server-side​-encryption​ is used to designated the encryption mode (AES-256, aws:kms)


# RDS

RDS Proxy can improve high availability when a failover occurs

# EC2

* if EC2 stays in Pending state and terminates, it can be due to :
  * EBS volume limit has been reached
  * EBS Snapshot is corrupted
  * Root EBS volume is encrypted and you don't have permission on the key 

* To aggregate EC2 instances metrics, it is necessary to activate detailed monitoring

# ALB

## Stick Session
* sticky sessions can be defined at the **target group** level
* Based on cookies
  * Duration-based stickiness : cookie named AWSALB
  * Application-based stickiness
    * It allows users to maintain stickiness across load balancers that are chained together

## Listener Rules

* by default, ALB considers last value of query parameters when calling a lambda function. **Multi-value** headers must be enabled to pass all query parameters to a lambda


# IAM

* IAM Identity Center uses permission sets to define policies. Permission sets ultimately get created as IAM roles in a given AWS account, with trust policies that allow users to assume the role through the AWS IAM Identity Center

# Cloudfront

* Reports
  * Cache statistics : hit, misses and errors
  * popular objects : nb of requests, hit/misses/errors
  * top referrers: domains of websites that originated the most HTTP and HTTPS requests
  * usage reports: nb requests by destination and protocol
  * viewer reports: type of devices, browsers operating systems and locations

* Websocket
  * The client send an HTTP request with the upgrade protocol header. 
  * Server responds to it and connectivity over WebSocket protocol is established


# WAF

* regarding AWS managed rules, rules cannot be changed, but action can be changed to count, allowing traffic

# Cloudwatch

* it's possible to aggregate mutliple configuration files by using append-config option. File names must be different

# Route 53

* not possible to configure health checks details on an ALIAS record

# Site-to-site VPN

* BGP is a TCP protocol with default port 179
* TunnelState metric can be used to determine the status of VPN tunnel. It will be 1 when BGP state is an established state. For other states it will be 0.
  

![BGP states](BGP-states.png)


# EBS

* EBS Direct API can be used to create EBS snapshots, **read data** from snapshots, and **identify differences** between snapshots.
* To resolve performance degradation on first time access due to a restore
  * For initialization of the entire volume. IT can take a lot of time depending on instance size and bandwidth supported.
  * Enable fast snapshot (additional charges)
* First time access can be slow because EBS make volume available asap, but data loading is still loading in background. If a process access a block that was not yet loaded, EBS will upload the block from s3 to restore it (lazy loading). This is the cause of latency.

# Storage Gateway

* HA mode for storage gateway
  * Supported on VmWare only
    * A cluster with vSphere HA enabled
    * A shared datastore
* CachePercentDirty is a metric that indicates the amount of data that has not yet been loaded on S3 when using a File Gateway.