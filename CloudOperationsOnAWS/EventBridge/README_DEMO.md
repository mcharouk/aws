Rule pattern

Type of event :

```
AWS Console Sign in Via CloudTrail
```

Custom Pattern

```
{
  "source": ["aws.signin"],
  "detail-type": ["AWS Console Sign In via CloudTrail"],
  "detail": {
    "userIdentity": {
      "type": ["Root"]
    }
  }
}
```

* Create SNS Topic / mail subscriber
* No need to create a role. SNS resource policy will be updated on rule creation
