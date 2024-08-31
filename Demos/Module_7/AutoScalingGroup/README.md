## Launch Template

* Create a launch template

 ```
 ASGDemoTemplate
 ```

* Provide infos
    * AMI
    * Instance Type
    * Security Group (default one)

## ASG

* Create an ASG

 ```
ASGDemo
 ```

* Configuration
  * Select default VPC and all subnets
  * No load balancer
  * No group metrics collection
  * Desired 1, Min 1, Max 2
  * No scaling policies
* Try to kill the created instance to show it's automatically restarted. Might take a few minutes to detect instance has been terminated

## Cloudwatch

Alarm Name
```
ASGScaleOutDemoAlarm
```

* create an alarm on metric EC2 / By AutoscalingGroup / ASGDemo / CPUUtilization
* Statistic : Average
* Period : 5 mins
* >= 70% (any number will work)
* No notification
* No autoscaling action (will configure that later)

## ASG update

* Go to **Automatic Scaling** tab
* Add a dynamic scaling policy of type simple scaling
* Provide some name (anything will be ok)
* Provide alarm
* Add One instance

## Alarm Breach

```
aws cloudwatch set-alarm-state --alarm-name ASGScaleOutDemoAlarm --state-value ALARM --state-reason test
```

* Note : must add a new cloudwatch alarm for scale in purpose
