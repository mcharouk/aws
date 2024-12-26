# Lab 1 : Private endpoint

## Summary

* Interact With S3 with a public instance
* Create interface endpoint
* Interact with interface endpoint with a private instance
* Change a interface endpoint resource policy to only allow access to a specific bucket

## Possible issues

* connect on the wrong instance
* Assign wrong security group to interface endpoint
* Create interface endpoint in the wrong VPC
* Interface endpoint can take some minutes to work after creating it
* Replace placeholders in S3 policy endpoint

# Lab 2 : Transit Gateway

## Description

* 4 VPC and TGW in one region / 1 VPC and TGW in another region
* first add connectivity to 4 VPC in the primary region by creating a TGW
* peer the 2 TGW in the 2 regions
* Test connectivity between two regions
* Blackhole on VPC B and D to deny traffic
* Bonus
  * create a global network in TGW Network Manager
  * try Route Analyzer


## Possible issues

* Check attachments to route tables
* Check TGW route table itself
* Check subnet route tables
* to enable connectivity between TGW 
  * check attachments on both sides
  * check TGW route tables on both sides
  * normally subnet route table should be ok, after first time it has been changed (On Task 5)

# Lab 3 : ECS on Fargate

## Description

* Create an image and push it to ECR
* Create an ECS Cluster, ECS Service, ECS Task Definition
* Run the application

## Possible issues

* straightforward lab as it's just copy/paste cmds in an EC2 instance
* make sure placeholders are correctly replaced

to save Nano file : Ctrl + O and press Enter
to exit Nano : Ctrl + X

# Lab 4 : Setting up a data lake with Lake Formation

## Description

* Setup lake formation
  * register data location
  * Grant a role for data location access
  * set permissions
  * Create a database
* Create a Glue crawler
* Run an Athena query

## Possible issues

* When register the S3 location, provide the appropriate role
* you have to click on boxes to provide retro compatibility for glue direct access. In Task 5 of this lab, user will remove those settings to activate lake formation accesses.
* When setting the crawler
  * check location
  * check iam role (AdminGlueServiceRole)
  * target db

# Lab 5 : Migrating an On-Premises NFS Share Using AWS DataSync and Storage Gateway

## Description

* Task 1 : copy some data on nfs source
  * First connect to the **client**
  * mount the server instance folder
  * copy some files
  * connect to the **server** instance
  * make a ls to check all files have been copied on the server
* Task 2 : Deploy and activate a datasync agent
* Task 3 : create and run a datasync task to copy data on s3
  * connect to the **server** instance to give access to data sync agent
* Task 4 : Create and activate a File Storage Gateway
* Task 5 : Create a NFS Share on the File Gateway and reconfigure the client to call it

## Possible issues

* when giving access to datasync agent, must connect to the server instance, not the client
* must use t3.xlarge for file gateway and data sync agent or it will fail create
* for file gateway, add a volume of 150 Gb. Do not change the root volume.
* to mount file gateway, copy/paste the linux cmd provided in the storage gateway console and replace [MountPath] by /mnt/nfs