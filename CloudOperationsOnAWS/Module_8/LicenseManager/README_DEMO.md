## Description

* this demo runs on Ireland region because associating a license with a launch template is not a feature available in Paris region at the time of writing

* This demo creates
  * a license configuration (self managed license)
  * a launch template associated with license configuration

## Action
* Creates 2 ec2 instances from launch template (Process without key pair must be selected on creation)
* notice that second ec2 instance cannot be created because of licensing.