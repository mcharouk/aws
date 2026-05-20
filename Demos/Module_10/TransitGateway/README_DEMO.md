# Transit Gateway

## Route Analyzer

* In Network Manager
  * go to reachability analyzer to test connectivity. Paths have been created by CF.  

## Transit Gateway update

* default route table
  * detach VPC B and VPC A from default route table
* create a new route table

```
VPCC-Only
```
* new route table
  * attach VPC A and VPC B
  * add a propagation for VPC C
  * can add static routes to add a blackhole for VPC A and VPC B cidr ranges (not mandatory, good to show to make an explicit deny)
* tests
  * test connection A with B (should be **NOK**)
  * test connection A with C (should be OK)
  * test connection B with C (should be OK)