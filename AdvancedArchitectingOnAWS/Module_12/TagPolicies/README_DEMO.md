# Create a SCP

* make tag mandatory for sns topics
* Policy name

```
EnforceTagOnSNS
```

* policy content

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "RequireTeamTagForSNSTopic",
            "Effect": "Deny",
            "Action": [
                "sns:CreateTopic"
            ],
            "Resource": [
                "arn:aws:sns:*:*:*"
            ],
            "Condition": {
                "Null": {
                    "aws:RequestTag/examplecorp:team-name": "true"
                }
            }
        },
        {
            "Sid": "PreventTagRemoval",
            "Effect": "Deny",
            "Action": [
                "sns:UntagResource",                
            ],
            "Resource": [
                "arn:aws:sns:*:*:*"
            ],
            "Condition": {
                "Null": {
                    "aws:RequestTag/examplecorp:team-name": "true"
                }
            }
        }
    ]
}
```

* Attach Policy to sandbox OU

# Create a Tag Policy

* Tag Policy Name

```
TeamNamePolicy
```

* Tag Key

```
examplecorp:team-name
```

* Tag Values

```
team1
team2
```

* Prevent noncompliant operations for this tag : add s3 bucket
* Preventing has no effect on unspecified tags
* Attach Policy to Sandbox OU

# Test policies

* Go to cloudshell
* try to create an s3 bucket without any tag. It's possible because no SCP prevent it. 
* Anyway, it's not possible to create a bucket and give tags directly. So there is some mechanism to build to detect buckets without this tag key (aws config for example)

## S3

```
aws s3api create-bucket --bucket aws-training-marccharouk-tagpolicies --region eu-west-3 --create-bucket-configuration LocationConstraint=eu-west-3 
```


* Add tag key examplecorp:team-name with value team3 (not allowed)
```
aws s3api put-bucket-tagging --bucket aws-training-marccharouk-tagpolicies --tagging 'TagSet=[{Key=examplecorp:team-name,Value=team3}]'
```

* Add tag key examplecorp:Team-Name (bad capitalization) with value team2 (allowed). This command should fail

```
aws s3api put-bucket-tagging --bucket aws-training-marccharouk-tagpolicies --tagging 'TagSet=[{Key=examplecorp:Team-Name,Value=team2}]'
```

* Add tag key examplecorp:team-name with value team1 (allowed)
```
aws s3api put-bucket-tagging --bucket aws-training-marccharouk-tagpolicies --tagging 'TagSet=[{Key=examplecorp:team-name,Value=team1}]'
```

## SNS

* try to create sns topic without any tag

```
aws sns create-topic --name sns-tagpolicy-demo
```

* try to create a sns topic with team3 as team name (allowed because not enforced)
  
```
aws sns create-topic --name sns-tagpolicy-demo --tags Key=examplecorp:team-name,Value=team3
```

* get non compliant resources

```
aws resourcegroupstaggingapi get-resources  --region eu-west-3 --include-compliance-details --exclude-compliant-resources
```