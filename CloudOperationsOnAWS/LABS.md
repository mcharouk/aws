# Lab 1

Systems manager

* Task 1 : Setup Inventory
  * Nothing really can fail
* Task 2 : Connect to Session manager
  * Nothing really can fail
* Task 3 : AWS Config
  * Select Continuous recording
  * Remove rule that blocks all resources
  * click on service linked role
  * choose rule ec2-instance-managed-by-systems-manager
* Task 4 : AWS Config IAM Rule
  * normally some resources should be not compliant
* Task 5 : Only exploration of inventory screens

# Lab 3

* Task 1 : create a cloudwatch log group
* Task 2 : create a command document
  * Task 2.2 : run the command
    * choose the right resource group
    * For logging, unselect S3 and select cloudwatch log group. The log group name is a free text, so careful the name that has been provided. IF the wrong log group has been provided, AWS will create a new one automatically with corresponding name.
  * Test EC2 has Apache installed on it. in URL specify http instead of https.
  * Other tasks : run an update command and retest EC2 url to see the change.
* Task 3 : create an automation document
  * The document
    * tests if instance type provided is different than the one given.
    * if so, it stop it, change instance size attribute, and restart it after a configurable wait time.
* Task 4
  * Check the logs in cloudwatch

# Lab 4

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