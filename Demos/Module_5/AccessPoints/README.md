# Access point

This setup shows how access policy works : 

* a bucket policy that delegates permissions to access point policies
* 2 access points
  * **AccessPointDemoRole** has r/w access on folder 1 through access-point-folder1, but not through access-point-folder2
  * **AccessPointDemoRole** has no access on folder 2 on both access-points

