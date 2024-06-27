# Module 3 : System Discovery

## Experian

[Experian](https://aws.amazon.com/solutions/case-studies/experian-case-study/?did=cr_card&trk=cr_card)

* Global Technology company in data and analytics
* needed a solution to help manage security alerts arising from its cloud environments.
* standardize and automate security protocols to address the root cause of the security alerts.
* "How can we best give our clients the tools that provide them flexibility in their environments functionality without compromising security?"

* Used AWS Config + AWS Lambda for alerting and automatic remediation 
* Experian has applied standardized security controls to over 400 of its accounts, and the number is continually growing
* By using AWS Config, Experian enjoys visibility and can correct misconfiguration in 2–5 minutes, compared to 24 hours using third-party tools.
* Experian decreased the number of security alerts in its Amazon S3 buckets (as they work on data use cases, s3 is a central service in their workload) by 80 percent from June to August 2021

# Module 12 : Mountable Storage

## PLANA

[PLANA, Pioneers the Future of Advanced Aviation on AWS](https://aws.amazon.com/solutions/case-studies/plana-case-study/?did=cr_card&trk=cr_card)

* design hybrid eVTOL aircraft for urban and regional environments
* objective : production ready by 2028
* encountered inefficiencies within their traditional workstation setup, resulting in time-consuming simulations
* faced high costs because it relied on engineering software that is charged on an hourly basis
* Migrated on AWS HPC Stack
  * ParallelCluster
  * EC2 on EFA (Elastic Fabric Adapter)
  * FSx for Lustre

### Results

* 70 percent reduction in HPC simulation costs by using
  * combination of On-Demand and Spot-Instance
  * C5n HPC instances
  * Amazon FSx for Lustre 
  * AWS ParallelCluster for configuring HPC resources for each simulation quickly and flexibly.
* The airflow simulations can now be completed in 5−8 hours instead of 10 days
