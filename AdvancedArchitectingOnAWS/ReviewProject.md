# Project 1 : TGW

## Question 5

* All VPCs can talk to each other
* For Outbound a new route table should be created
* Private VPC should be associated with a TGW route table 
  * 0.0.0.0/0 -> OutboundVPC
  * CIDR VPC 1 -> VPC 1
  * CIDR VPC 2 -> VPC 2
  * etc...
* Outbound VPC should be associated with a TGW route table that looks like the default route table to redirect the response...

# Project 2 : Hybrid Connections

## Question 2

* Possible to attach a [site-to-site VPN to a TGW](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-transit-gateway-vpn.html)
* It could be possible to create 2 VPN connections, but initial pre requisities is that current VPN to AWS connection alone is untenable, so that's probably why the right answer is direct connect + VPN as fallback

## Question 3

* There are 2 answers for Private VIF. When two are inverted, it appears as a wrong answer, i think it's more a bug

## Question 5

* Right answer si the pattern Direct Connect -> Public VIF -> VPN to TGW
* It could be possible to use Direct Connect -> DXGW -> Transit VIF -> VPN to TGW. 
* There's no mention of DXGW in the answers, maybe that's why it's false. Or maybe, because the question has been written before this feature was available.

# Project 3 : Migration

## Question 1

* the key sentence is detailed time-series performance data
* Only AWS Discovery Agent collects these kind of data
* To find the data
  * For Agent
    * Data are available on Migration Hub
    * Option to export the data collected to S3 (CSV File)
  * For Agentless
    * Data are only available on Migration Hub

## Question 5

* to have an estimation of [migration time](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-data-migration-services/time-and-performance.html)
