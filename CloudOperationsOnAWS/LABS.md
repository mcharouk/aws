# Lab 1

## Lab description : system manager inventory & config

The goal of the lab is to
* setup systems manager inventory
* connect to an EC2 instance with Systems Manager (just to see, it's not related to other tasks in the lab)
* setup AWS config to continuously detect changes
* setup some rule : all user that have policies attached are marked as non compliant. Because policies should be attached to a group or to a role
* explore Systems Manager inventory screens

## Step Details


* Task 1 : Setup Inventory
  * Go to setup inventory, and Manually select the instances
* Task 2 : Connect to Session manager
  * Nothing really can fail
* Task 3 : AWS Config
  * Select Continuous recording
  * Remove rule that blocks all resources
  * click on service linked role
  * choose rule ec2-instance-managed-by-systems-manager
  * might takes 5 min to display compliance status
* Task 4 : AWS Config IAM Rule
  * normally some resources should be not compliant
* Task 5 : Only exploration of inventory screens
  * Redirected to Fleet Manager


# Lab 2 : resource groups, tags and cloudformation

## Lab description

* Use application composer to update a cloudformation template (consists of adding an AppServer, copy/paste the AppServer 1 config and change the Tag with key Name)
* create a resource group and add tags (cost-center = production to all ec2 instances). Tag only app servers
* Use CloudFormation dirft detection feature to detect changes on tag and fix the template to add new tag key to all app servers

## Step details

* if stack fails, delete it and recreate it

# Lab 3 : System manager commands

## Lab description

* configure Systems Manager to that it logs **command document** output to cloudwatch logs
  * create cloudwatch log group
* create and run command document by resource group. Document installs Apache Web Server on EC2 instance
* create a document to update content of apache web server
* run a managed automation document that resizes an instance

## Step Details

* Task 1 : create a cloudwatch log group
* Task 2 : create a command document
  * Task 2.2 : run the command
    * choose the right resource group
    * For logging, unselect S3 and select cloudwatch log group. The log group name is a free text, so careful the name that has been provided. IF the wrong log group has been provided, AWS will create a new one automatically with corresponding name.
  * Test EC2 has Apache installed on it. in URL specify http instead of https.
  * Other tasks : run an update command and retest EC2 url to see the change.
* Task 3 : create an automation document
  * The document
    * tests if instance type provided is different than the one given. If it's not the case the step fails, but it still proceeds by updating the instance do the desired type
    * if so, it stop it, change instance size attribute, and restart it after a configurable wait time.
* Task 4
  * Check the logs in cloudwatch

# Lab 4 : Cloudwatch

## Lab description


* update systems manager version on EC2 instances
* Use multiple ssm documents to manage cloudwatch log agent
  * install agent
  * run agent
  * display status
* Create Cloudwatch dashboard to see EC2 mem usage (fed by Cloudwatch Agent), EC2 standard network metrics
* Test cloudwatch alarm
  * create an sns topic to be notified
  * create a cloudwatch alarm that triggers if there is a StatusCheckFailed_System
  * Force the state of cloudwatch alarm to test behavior
* Bonus Step
  * Create a canary lambda (it's lambda created with a blueprint, that checks some text is present in a url). URL and text are provided in an env variable
  * This lambda is triggered by EventBridge, once every minute
  * The objective is to create an alarm that trigger on lambda failure. Make lambda fail and check the results (a mail will be sent through SNS)

## Step Details

 
* for all command documents, targets are added manually

* Task 1 : install cloudwatch agent
  * Install SSM Agent Cmd : deselect S3 logging
  * Install CloudWatch Log Agent Cmd : deselect S3 logging
* Task 2 : Start CloudWatch Agent
  * Check that ssm is selected
  * Check that configure is selected
  * Check that Optional restart is selected
  * AgentConfigFile as name of ssm parameter
  * Unselect S3 Bucket
* Task 6.2
  * Careful about the command to trigger the alarm. Region and name must eventually be changed

* For Lambda Bonus question, it can take some time for the alarm to trigger.

# Lab 5 : Backup

## Lab description

* Create a backup plan that backup all EBS volumes with tag NAme as webAppVolume
* launch an on demand backup
* inspect lambda
  * when a backup complete, it triggers a backup restore test
  * when a restore job completes, it clean the restored resources

## Step Details

* Task 1 : subscribe to a SNS topic
  * don't forget to confirm the mail subscription
* Task 2 : create a backup plan a backup vault, and assign specific EBS resource to the plan
* task 3 : Replace placeholder region and sns topic ARN with the one provided by the LAB left menu.
  * Backup vault name should be changed too if the student didn't respect the name given by the lab
  * In the verification command, the name must match also backup plan name
* Task 4 : select the right Vault, right EBS volume and the correct IAM role
* Other tasks are about inspecting resources

# Lab 6 : Capstone

## Lab description

* EventBridge 
  * Create an Event Bridge rule that sends a message to an sns topic when an automation document completes with a success state.
  * Execute an automation document to check configuration has been properly set.
* CloudFormation
  * Create a drift detection in CloudFormation to see what resource has drifted
  * fix the resource by executing a managed SSM Automation Document
  * check drift has been fixed
* AWS Config
  * activate AWS Config with a rule that detect Bucket Versioning is enabled
  * add an automatic remediation action to the rule
  * Execute it to remediate the non-compliant resource

## Step Details

* Task 1
  * create SNS Topic
  * EventBridge rule triggered when an SSM document has status success
  * EventBridge triggers SNS
* Task 2
  *  the drift has to be applied on the stack that has description Lab 6 Capstone lab
  * The document to applied is named AWS-DisablePublicAccessForSecurityGroup and remove the SSH inbound rule that have been added manually
* Task 3
  * The SSM Document is named AWS-ConfigureS3BucketVersioning
  * pass the role arn to the remediation rule (provided in Lab menu)
  * pass Enabled to versioningState