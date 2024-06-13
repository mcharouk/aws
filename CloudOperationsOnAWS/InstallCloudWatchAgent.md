* First, have created a new version of document AWSQuickSetup-CreateAndAttachIAMToInstance-pp69w with CloudWatchAgentServerPolicy as an additional policy to attach
* Have created a SSMAutomationRole to give to the document and be able to perform actions
* Execute document AWSQuickSetup-CreateAndAttachIAMToInstance-pp69w. It will associate a role to the instance with correct permissions. Parameters are 
  * AutomationRole : SSMAutomationRole 
  * instanceId
  * true for attaching policy

* Demonstrate Automation
* Demonstrate State manager that will execute the automation document on startup
* Demonstrate Command Documents (Cloudwatch installation) and apply them with Run Command
* Demonstrate also Cloudwatch agent log to Cloudwatch