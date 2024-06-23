# Access point

This setup shows how access policy works : 

* a bucket policy that delegates permissions to access point policies
* 2 access points
  * **AccessPointDemoRole** has r/w access on finance through access-point-finance, but not through access-point-human-resources
  * **AccessPointDemoRole** has no access on human-resources on both access-points

