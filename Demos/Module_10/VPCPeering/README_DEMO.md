# VPC Peering

* try to ping VPC A from VPC B (or the other way around, does not matter). Ping should fail.
* create a peering connection
  * give any name
* Confirm pending request
* add routes in both route table of VPC A and VPC B
* test again ping that didn't work at first step