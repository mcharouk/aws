## SSM Setup

* [Link on SSM Cloudwatch setup](https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/install-cloudwatch-systems-manager.html)

## CloudWatch

* create a custom document

Document Name
  
```
CloudWatchApacheInstall
```

Document Type

```
/AWS::EC2::Instance
```

Document content

```
{
  "schemaVersion": "2.2",
  "description": "The AWS-InstallAndManageCloudWatch command document installs the Amazon CloudWatch agent and manages the configuration of the agent for Amazon EC2 instances.",
  "mainSteps": [
    {
      "inputs": {
        "documentParameters": {
          "name": "AmazonCloudWatchAgent",
          "action": "Install"
        },
        "documentType": "SSMDocument",
        "documentPath": "AWS-ConfigureAWSPackage"
      },
      "name": "installCWAgent",
      "action": "aws:runDocument"
    },
    {
      "inputs": {
        "documentParameters": {
          "mode": "ec2",
          "optionalRestart": "yes",
          "optionalConfigurationSource": "ssm",
          "optionalConfigurationLocation": "/cloudwatch/agent/config/apache",
          "action": "configure"
        },
        "documentType": "SSMDocument",
        "documentPath": "AmazonCloudWatch-ManageAgent"
      },
      "name": "manageCWAgent",
      "action": "aws:runDocument"
    }
  ]
}
```

* Run document on EC2
* check that cloudwatch log agent installed in 

```
/opt/aws/amazon-cloudwatch-agent/
```

config file is located in 

```
/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.d
```


* check logs in cloudwatch
