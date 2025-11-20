# Access point

This setup shows how access policy works : 

* a bucket policy that delegates permissions to access point policies
* 2 access points
  * **AccessPointFinanceDemoRole** has r/w access on finance through access-point-finance, but not through access-point-human-resources
  * **AccessPointHumanResourcesDemoRole** has r/w access on human-resources through access-point-human-resources, but not through access-point-finance

