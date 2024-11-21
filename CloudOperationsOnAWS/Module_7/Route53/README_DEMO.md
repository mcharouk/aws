# Demo

## Steps

* in a web explorer, input dns names of the 2 ALBS (available in CF outputs)
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