## SSM Setup

* Role for instance : AmazonSSMRoleForInstancesQuickSetup

* [Link on SSM Cloudwatch setup](https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/install-cloudwatch-systems-manager.html)

* Create a sec group with HTTP inbound allowed

## CloudWatch
* create a parameter store (/cloudwatch/agent/config/apache) 
* create a custom document that includes 
  * AWS-ConfigureAWSPackage with Name as AmazonCloudWatchAgent
  * AmazonCloudWatch-ManageAgent document
* Run document on EC2

* check that cloudwatch log agent installed in /opt/aws/amazon-cloudwatch-agent/

## Inventory

* Create association with AWS-GatherSoftwareInventory