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

* Create an image and push it to ECR
* Create an ECS Cluster, ECS Service, ECS Task Definition
* Run the application

## Possible issues

* straightforward lab as it's just copy/paste cmds in an EC2 instance
* make sure placeholders are correctly replaced

to save Nano file : Ctrl + O and press Enter
to exit Nano : Ctrl + X                                             