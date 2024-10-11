## SNS

* don't forget to confirm mail subscription

## EventBridge

rule name (name not mandatory)

```
rootuser-connection
```

In Sample event, we can try with 

```
AWS Console Sign in Via CloudTrail
```

Rule pattern

Type of event :

```
AWS Console Sign in
```

Event Type

```
Sign-in Events
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

* connect with root user of sandbox.admin account in a private window
* look at mail to confirm a notification has been received. It might take 2-3 mins to receive it