# Module 1

## Well Architected Tool

[Cox Automative](https://aws.amazon.com/solutions/case-studies/cox-automotive-case-study-aws-well-architected/?did=cr_card&trk=cr_card)

We needed a standard framework to collect data on the health of our architecture,” says Brian Lloyd-Newberry, Associate Vice President of Architecture for the Cox Automotive data portfolio. “Every team was doing something different, and we weren’t able to clearly communicate risk, investment posture, and architectural and operational health.

to help organizations learn best practices for designing and operating secure, reliable, efficient, and cost-effective workloads on AWS

use that data to drive investment and communicate application health (the tool KPIs)
"At this point, we started to have a truly data-driven architecture practice.”

Summary of the findings to the executive team / secure a significant investment into the company’s solutions for reducing risk and improving security and resilience

We have increased the satisfaction of architects, who see the impact of their work and feel more valuable

Ultimately, customers experience this reduction in risk and technical debt as more uptime, improved quality of our solutions, and greater responsiveness in the experiences that we deliver

Consolidated workloads and clarified best practices across 350 engineering teams

## Local Zones

[Netflix](https://aws.amazon.com/fr/solutions/case-studies/netflix-aws-local-zones-case-study/)

To recruit talent across the world, the company needed remote workstations that could provide similar performance to those available to employees in Netflix’s studio headquarters

Netflix is poised to become one of the world’s most prolific producers of **visual effects** and **original animated content**

These artists need **specialized hardware** and access to **petabytes of images** to create stunning visual effects and animations. Historically, artists had **specialized machines built for them at their desks**; now, we are working to move their workstations to AWS to take advantage of the cloud.

Netflix wanted to **reduce application latency** so that its artists could create content from their **home offices** or **animation hubs** without experiencing interruptions or lag

Netflix uses Local Zones to access select AWS services closer to its artists and to achieve **single-digit millisecond latency** from its studios to the Local Zones
Using the new **Amazon EC2 G5 Instances**, we can provision higher-end graphics workstations that offer **up to three times higher performance** compared to before

Customers using Local Zones can access the full suite of AWS services in the parent Region by using the redundant private network provided by AWS and **have the option of partitioning workloads between a Local Zone and a Region to increase availability**.


# Module 2 : Security


# Module 3 : Networking


# Module 4

## EC2

[Climate Data Factory](https://aws.amazon.com/fr/solutions/case-studies/the-climate-data-factory/?did=cr_card&trk=cr_card)

Mais le gain principal de cette migration est ailleurs : 

* simulations à la volée, alors qu’il nous fallait auparavant attendre plusieurs mois, et parfois même un an pour avoir nos résultats faute de disponibilité suffisante sur le cluster partagé. 
*  solution scalable pour allouer les ressources adaptées au périmètre de nos projets
*  nous pouvons répondre à des demandes client que nous ne pouvions pas honorer jusqu’alors faute de disponibilité.
*  Le tout sans complexifier notre IT, bien au contraire : je peux gérer seul l’ensemble de l’infrastructure de traitement"

coût final 10 fois plus faible que celui que nous avions estimé à l’origine


## Lambda

[Utopus](https://aws.amazon.com/solutions/case-studies/utopus-insights-case-study/?did=cr_card&trk=cr_card)

When migrating to AWS, Utopus opted for fully managed, serverless solutions when possible. “Using serverless solutions on AWS means that we don’t have to worry about scalability, manageability, installation, or configuration,” says Rida. For instance, the company adopted Amazon Kinesis Data Streams, which companies use to easily stream data at virtually any scale. On average, the company streams 7 TB of data through Scipher every day. 

After streaming its data, the company processes it using AWS Lambda, a serverless, event-driven compute service that companies use to run code for virtually any type of application or backend service without provisioning or managing servers. “AWS Lambda is highly scalable and very powerful,” says Rida. “We can manage latency, make our processing faster, and decide how much we want to spend.” Using AWS Lambda, the company processes over 200 billion signals from wind and solar sources every day, and in under 2 hours, it can process the same amount of data that would have taken 2 weeks to process on premises. By gaining deeper and timelier insights, its customers can improve the performance of their renewable energy assets and minimize their carbon footprints. 

# Module 5

## Storage Gateway

[TransferWise](https://aws.amazon.com/solutions/case-studies/transferwise-case-study/?did=cr_card&trk=cr_card)
AWS Storage Gateway helped us address the load and network constraints we had, which were preventing us from getting backups done

* TransferWise used the Tape Gateway mode of AWS Storage Gateway to replace tape backups 
* write database backups to a Volume Gateway. This in turn created Amazon Elastic Block Store (Amazon EBS) Snapshots that were managed by the AWS Backup service. 

-> As a result, TransferWise was able to close its recovery data center in the Netherlands.

## S3 lifecycle policies

[Illumina](https://aws.amazon.com/solutions/case-studies/illumina-carbon-emissions-case-study/?did=cr_card&trk=cr_card)

* As the company expanded its customer base and product line, the amount of genetic data that Illumina securely stored in the cloud grew exponentially—from 1 PB to 100 PB in 8 years.
* During 2021–2022 alone, Illumina added over 24 PB of data
* Illumina predicted that its stored data would continue to double every 2 years

 * Previously, Illumina’s teams would use Amazon S3 lifecycle policies to transition its data into different Amazon S3 storage classes to cut its data storage costs.
 * Illumina decided to adopt the S3 Intelligent-Tiering storage class. By using S3 Intelligent-Tiering, Illumina could allocate its cost savings toward expanding its service and software offering, enhancing the customer experience

 * a few minutes to setup
 * After just 3 months of using S3 Intelligent-Tiering, Illumina began to see significant monthly cost savings. For every 1 TB of data, the company saves 60 percent on storage costs

# Module 6 : RDS

[Freshworks](https://aws.amazon.com/solutions/case-studies/freshworks-case-study/?did=cr_card&trk=cr_card)
On its database side, which uses horizontal
scaling, Freshworks performs around four million queries per second for Freshdesk across 200 database shards

In 2020, the company received **1.69 billion** requests per week, compared with 359 million requests per week in 2016. Even for its large customers, for which the number of web requests skyrockets **during peak times**, Freshworks can provision **multiple read replicas** and distribute the API request load **in less than 30 minutes—regardless of size or region**.

Freshworks uses Amazon RDS **Multi-AZ** deployments—which provide enhanced availability and durability for Amazon RDS database instances. For example, using Amazon RDS for MySQL, Freshworks can automatically switch to a new Availability Zone if needed, and its workload takes **less than 10 seconds** to detect a point of failure

Simplified disaster recovery with cross region read replica

# Module 7 : Monitoring and scaling

# Module 8 : System Manager

[RackSpace](https://aws.amazon.com/solutions/case-studies/rackspace-case-study/?did=cr_card&trk=cr_card)

# Module 9 : Containers

## EKS

[Biz2Credit](https://aws.amazon.com/solutions/case-studies/biz2-credit/?did=cr_card&trk=cr_card)

helps small companies secure loans fast through a platform that banks can use to offer their own lending services.

They were cloud native from the start, and used to manage entirely their Kubernetes cluster.

They decided to move on to EKS to be able to scale faster.

Now, the company no longer needs to manually adjust master nodes behind Kubernetes clusters — a task that needed application downtime. 
Amazon EKS automatically scales our control plane, helping us increase uptime **from 99.9 to 99.999 percent**

Biz2Credit has reduced IT costs through management savings and the integration of Karpenter

With the cost savings achieved through migrating to Amazon EKS, Biz2Credit has been able to invest in improving its security posture.
The company now utilizes various AWS security services, such as AWS Config, Amazon GuardDuty, Container Insights, CloudWatch Logs Insights, Amazon Inspector, Amazon Detective, and Amazon Macie to ensure the security of applications and workloads.


Biz2Credit can offer a better customer experience, lowering the time it takes to onboard companies to its online marketplace or Biz2X. Setting up infrastructure for a new bank used to take us **3−4 days**, but with Amazon EKS, our delivery time is reduced to **5−6** hours

# Module 10 : Networking 2

## Transit gateway

[ZenDesk](https://aws.amazon.com/blogs/networking-and-content-delivery/zendesks-global-mesh-network-how-we-lowered-operational-overhead-and-cost-by-migrating-to-aws-transit-gateway/?trk=el_a134p000003yz30AAA&trkCampaign=CSI_Q3_2020_TGW_ZendeskBlog&sc_channel=el&sc_campaign=CSI_Q3_2020_TGW_ZendeskBlog&sc_outcome=Enterprise_Marketing&sc_geo=mult)



# Module 11 : Serverless

## SNS

[Armut](https://aws.amazon.com/solutions/case-studies/armut-case-study/?did=cr_card&trk=cr_card)

Digital application that link consumer and professionals on topics like moving, wellness, health...
 
company **grew by more than 1,000 percent** over the last 5 years, its **existing notification system no longer met its needs**, with **notifications often failing**. It also **didn’t scale well**, while its day-to-day maintenance requirements were becoming challenging and time-consuming for the IT team

The notifications sent to customers and professionals via email, SMS, or push notifications are central to the customer experience. They communicate the various steps needed for the work to be completed, such as confirming the job and setting up a time. They also notify customers if a professional arrives late, a job is cancelled, or payments are due.

Armut developed and implemented its new notification system in just **6 months** using **AWS Lambda**, a serverless, event-driven compute service that lets it run code without thinking about servers or clusters

Armut can now send many more notifications in a given time period than it could previously—in one trial, the system sent **1,000 emails per second**. It delivers more than **1.5 million emails a day** over Amazon Simple Email Service, a high-scale inbound and outbound cloud email service.

Around **20 million push notifications** and **3 million SMS notifications** are sent **a month**, with this expected to grow as more customers use the service. The ability to send more notifications also has a direct impact on income, as Armut charges professionals to provide quotes.

# Module 12 : WAF

[Outsystems](https://aws.amazon.com/solutions/case-studies/outsystems-case-study/?did=cr_card&trk=cr_card)

The company manages a large and growing number of application load balancers—over 4,000 as of 2022—and serves thousands of applications across all load balancers.

Using AWS services, we can manage the security posture of all customers from a central place by deploying rules that are specific to our technology and blocking malicious events,

“Previously, an analyst and an operator would have to create the local WAF and deploy the rules with the solution when reacting to an event,

Using AWS, we reduced 2 hours of work to less than 5 minutes

OutSystems reduced its costs by 88 percent per month by upgrading to Shield Advanced. The company gains these significant cost savings on an ongoing basis despite its scale because it no longer needs to pay for each WAF or rule

# Module 13 : Backup


