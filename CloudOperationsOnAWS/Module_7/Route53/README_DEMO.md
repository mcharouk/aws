# Demo

* create private hosted zone

```
route53.demo.com
```

* create two alias records on ALB
* create Geolocation routing policy. 
  * Resources in Ireland VPC should be redirected to Paris ALB
  * Resources in Paris VPC should be redirected to Ireland ALB
* change Parameter store in both regions. Replace ALB DNS name by private hosted zone root domain name
