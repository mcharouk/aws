* create the following policy
  * the policy deny to create ec2 instances that are not of the specified type
  * for example, it can be used to prevent creating large instances in a sandbox env.

* Policy name

```
DenyLargeInstancePolicy
```

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "RequireMicroInstanceType",
      "Effect": "Deny",
      "Action": "ec2:RunInstances",
      "Resource": [
        "arn:aws:ec2:*:*:instance/*"
      ],
      "Condition": {
        "StringNotEquals": {
          "ec2:InstanceType": "t2.micro"
        }
      }
    }
  ]
}
```

* Attach policy to OU Sandbox
* try to create an EC2 instance of any type except t2.micro, it should fail.