# Resource Access Manager

## Create Resource Share

* In this demo, we will share 
  * a subnet
  * a security group

* in RAM menu, in settings, note that Enable sharing with AWS Orga must be checked (by default it is not)
* create a resource share

```
SubnetShareDemo
```

* In resources, select Subnets
* select private subnet
* In resources, select Security groups
* select SharedSecurityGroup

* in Step 3 (Grant Access to principals)
  * select the option *Allow sharing only wihtin your organization*
  * Associate the Resource share with sandbox OU

## Test Sharing

* Connect to the sandbox account
* Create an EC2 instance
  * name
  * in the shared subnet
  * with the shared security group

```
MyWebServer
```
  
* Note that EC2 instance cannot be seen in VPC Owner account, only by the EC2 owner account
