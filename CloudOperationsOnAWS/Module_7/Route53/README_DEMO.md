# Demo

## Steps

* use public hosted zone mcc-aws-demo.fr

* create two alias records on ALB
* domain name

```
hello.mcc-aws-demo.fr
```

* create Geolocation routing policy. 
  * UK IPs should be redirected to Ireland ALB
  * France IPs should be redirected to France ALB
* Try to connect with a different country (Romania, Germany for ex.) to act that application is not accessible.

## VPN available countries

* US
* Canada
* UK
* HK
* FR
* Germany
* Netherlands
* Switzerland
* Norway
* Romania