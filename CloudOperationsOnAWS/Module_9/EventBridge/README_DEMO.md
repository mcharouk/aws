## SNS

* don't forget to confirm mail subscription

## EventBridge

rule name (name not mandatory)

```
rootuser-connection
```

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

* look at mail to confirm a notification has been received