# Transit Gateway

## Route Analyzer

* In Network Manager
  * go to Transit gateway network, in global network created by CF
  * go to tab Route Analyzer
  * fill in
    * two attachments (mapping attachment vs VPC id is in CF output)
    * IP address (it does not necessarily have to exist)

  | VPC Name | IP Range    | IP Address Example |
  | -------- | ----------- | ------------------ |
  | VPC A    | 10.0.0.0/24 | 10.0.0.8           |
  | VPC B    | 10.1.0.0/24 | 10.1.0.12          |
  | VPC C    | 10.2.0.0/24 | 10.2.0.15          |

  * test connection A with B (should be OK)
  * test connection A with C (should be OK)
  * test connection B with C (should be OK)


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