# Module 1

## Well Architected Tool

[Cox Automative](https://aws.amazon.com/solutions/case-studies/cox-automotive-case-study-aws-well-architected/?did=cr_card&trk=cr_card)

Facilite l'Achat et vente de véhicules (le produit est une application de gestion)

### Problem
* We needed a **standard framework** to collect data on the health of our architecture,
* **Every team was doing something different**, and we weren’t able to clearly **communicate risk, investment posture, and architectural and operational health**.

### Solution
* Have used Well Architected Tool to **collect data** to **drive investment and communicate application health** (the tool KPIs)
* At this point, we started to have a truly **data-driven** architecture practice

### Results

* Summary of the findings to the executive team / secure a **significant investment** into the company’s solutions for **reducing risk and improving security and resilience**
* We have increased the **satisfaction of architects**, who see the impact of their work and **feel more valuable**
* Ultimately, **customers experience this reduction in risk and technical debt** as **more uptime, improved quality of our solutions, and greater responsiveness in the experiences that we deliver**
* **Consolidated workloads and clarified best practices across 350 engineering teams**

## Local Zones

[Netflix](https://aws.amazon.com/fr/solutions/case-studies/netflix-aws-local-zones-case-study/)

* Netflix is poised to become one of the world’s most prolific producers of **visual effects** and **original animated content**

* These artists need **specialized hardware** and access to **petabytes of images** to create stunning visual effects and animations. * Historically, artists had **specialized machines built for them at their desks**; now, we are working to move their workstations to AWS to take advantage of the cloud.

### Problem

* To recruit talent **across the world**, the company **needed remote workstations** that could provide **similar performance** to those available to employees in Netflix’s studio headquarters

* Netflix wanted to **reduce application latency** so that its artists could create content from their **home offices** or **animation hubs** without experiencing interruptions or lag

### Solution

* Netflix uses Local Zones to access select **AWS services closer to its artists** and to achieve **single-digit millisecond latency** from its studios to the Local Zones
* Using the new **Amazon EC2 G5 Instances**, we can provision higher-end graphics workstations that offer **up to three times higher performance** compared to before
* Customers using Local Zones can access the full suite of AWS services in the parent Region by using the redundant private network provided by AWS and **have the option of partitioning workloads between a Local Zone and a Region to increase availability**.

# Module 2 : Security

## AWS Organization / SCP

[Warner Bros](https://aws.amazon.com/solutions/case-studies/warnerbros-discovery-case-study/?did=cr_card&trk=cr_card)

### Activity

Medias / Divertissement

Merge of Warner bros and Discovery Channel

### Problem

* Goal is to be able to integrate **new acquired company without impacting the day-to-day operations of either business**

### Solution

* GuardDuty / CloudTrail / FirewallManager
* When account creation is centralized, we have the ability to view and control cloud spend in a single pane of glass
* Before 2019, creating a new account could take up to **2 months**. Now that the centralized process is used, with defined features and a controlled process, an account can be configured immediately, and the entire delivery is finished **within 2 days**.
* When merging Discovery Channel, The company went from 270 accounts to thousands of accounts.

# Module 3 : Networking


# Module 4

## EC2

[Climate Data Factory](https://aws.amazon.com/fr/solutions/case-studies/the-climate-data-factory/?did=cr_card&trk=cr_card)

### Activity

* Agrège, traite et rend accessibles les données de simulations climatiques mondiales grâce à une infrastructure HPC hébergée dans le cloud AWS.
* Les données sont notamment mises à disposition des décideurs mondiaux

### Situation

* les calculs de base nécessitent plusieurs To de RAM et des centaines CPU
* Au départ, un HPC du CNRS était utilisé
* **Pb de disponibilité du cluster** surtout face à des calculs de plus en plus exigeants : pour passer d’une échelle de 25 km à 10 km sur nos données, il faut déployer **6 fois** plus de ressources
* Le cluster étant partagé il faut attendre son tour...

### Solution

Après migration sur AWS : 
* Disponibilité immédiate (à la volée) alors qu'avant il fallait attendre plusieurs mois avant d'utiliser le cluster
* Capacité à répondre à des demandes clients qu'ils ne pouvaient pas honorer jusque là
* Simplification de l'IT : une seule personne allouée à la gestion du cluster
* Coût 10 fois plus faible que celui estimé au départ

## Lambda

[Utopus](https://aws.amazon.com/solutions/case-studies/utopus-insights-case-study/?did=cr_card&trk=cr_card)

### Activity

* Renewable energy analytics provider
* Process IoT data coming from wind and solar energy
* Businesses can proactively monitor their assets worldwide and **predict maintenance needs or part failures**, helping to **increase the longevity and performance** of their renewable energy assets
* Petabytes of data to process in real time

### Problem

On premise, infrstructure was overwhelmed by the amount of data

### Solution

* Go serverless to not worry about **scalability, manageability, installation, or configuration**
* With Kinesis Data Streams, streams **7 TB of data every day** through Scipher (their platform)
* Process data with **Lambda**
* Lambda processes over **200 billion (milliards) signals every day**. In **2 hours**, it processed what the legacy infra was able to process in **2 weeks**
* Its customers can **improve the performance** of their renewable energy assets and minimize their carbon footprints



# Module 5

## Storage Gateway

[TransferWise](https://aws.amazon.com/solutions/case-studies/transferwise-case-study/?did=cr_card&trk=cr_card)

### Activity
Global financial technology company working to develop better ways to move money around the world

### Problem
TransferWise hosted its application environments in **on-premises data centers** that made it **difficult to scale** and **ensure the 
constant availability** customers expect. 

We wanted to **grow globally** and didn’t want to have to build out data center partnerships with multiple vendors all over the place.

### Solution

* TransferWise began its cloud migration by using a hybrid cloud storage architecture to **move its data backup environment to AWS**.
* AWS Storage Gateway helped us address the **load and network constraints** we had, which were preventing us from getting backups done
* TransferWise used the Tape Gateway mode of AWS Storage Gateway to replace tape backups. 
* write database backups to a Volume Gateway. This in turn created Amazon Elastic Block Store (Amazon EBS) Snapshots that were managed by the AWS Backup service. 
* As a result, TransferWise was able to **close its recovery data center** in the Netherlands.
* Then they used the EBS backup to migrate the databases
* The organization migrated **90 percent** of its German data center using this approach
* Moved hundreds of MySql and Postgresql instances and EC2 instances. 

## S3 lifecycle policies

[Illumina](https://aws.amazon.com/solutions/case-studies/illumina-carbon-emissions-case-study/?did=cr_card&trk=cr_card)

### Activity

* is a leading developer, manufacturer, and marketer of **life science tools** and systems for large-scale **genetics analysis**

###  Problem

* As the company expanded its customer base and product line, the **amount of genetic data** that Illumina securely stored in the cloud **grew exponentially—from 1 PB to 100 PB in 8 years**.
* During 2021–2022 alone, Illumina added over **24 PB of data**
* Illumina predicted that its stored data would continue to **double every 2 years**
 * Previously, Illumina’s teams would use **Amazon S3 lifecycle policies** to transition its data into different Amazon S3 storage classes to cut its data storage costs.


### Solution

 * Illumina **decided to adopt the S3 Intelligent-Tiering** storage class.
 * a few minutes to setup
 * After **just 3 months** of using S3 Intelligent-Tiering, Illumina began to see **significant monthly cost** savings. **For every 1 TB of data**, the company saves **60 percent** on storage costs
 * I think it’s the **biggest return on investment** that we’ve ever seen
 * By using S3 Intelligent-Tiering, Illumina could **allocate its cost savings toward expanding its service and software offering**, enhancing the customer experience

 

# Module 6

## RDS
[Freshworks](https://aws.amazon.com/solutions/case-studies/freshworks-case-study/?did=cr_card&trk=cr_card)

### Activity

it's a SaaS : CRM, customer service

### Problem

Our founding team consisted of application developers. We are architects, and **we write code**; we **don’t want to deal with infrastructure**. We wanted a solution that was **predictable and reliable**

* They had a previous solution on another cloud vendor. They wanted to use MySQL and the other provider didn't have at the time MySQL in its offer.

### Solution

* They migrated on AWS on RDS in 2013.

* Using Amazon RDS for MySQL, Freshworks can handle **500,000 web requests per minute** for Freshdesk, and for all its software products combined, it can handle around **one million requests per minute**
* On its database side, which uses **horizontal scaling**, Freshworks performs around **four million queries per second** for Freshdesk across **200 database shards**
* In 2020, the company received **1.69 billion requests per week**, compared with **359 million requests per week in 2016**. Even for its large customers, for which the number of web requests skyrockets **during peak times**, Freshworks can provision **multiple read replicas** and distribute the API request load **in less than 30 minutes—regardless of size or region**.
* Freshworks uses Amazon RDS **Multi-AZ** deployments—which provide **enhanced availability and durability** for Amazon RDS database instances. For example, using Amazon RDS for MySQL, Freshworks can automatically switch to a new Availability Zone if needed, and its workload takes **less than 10 seconds** to detect a point of failure
* **Simplified disaster recovery** with cross region read replica

## DynamoDB

[Careem](https://aws.amazon.com/solutions/case-studies/careem-dynamodb-case-study/?did=cr_card&trk=cr_card)


# Module 7 : Monitoring and scaling

## Logs

[Zs](https://aws.amazon.com/solutions/case-studies/zs-associates-security-case-study/?did=cr_card&trk=cr_card)

!!! Montrer l'architecture sur la page!!!

### Activity

Société de services qui a construit bcp de solutions sur AWS pour ses clients et qui a besoin d'un framework pour gérer la sécurité et notamment la compliance exigeante de leurs multiples clients (**250 comptes**)

### Problem
Seek to
* **automate time-consuming manual security procedures** 
* **eases the rollout of cloud architecture for clients**

### Solution

* **Collect logs (To fo data)** from spoke accounts into a centralized account. 
* ZS built a robust security landscape centered around the cybersecurity framework from the National Institute of Standards and Technology (NIST). NIST is supported by governments and industries worldwide as a **recommended baseline** for use by any organization, regardless of its sector or size
* SecurityHub to check against compliances : SOC 2, ISO/IEC 27001, and HITRUST. Has helped to extend to other regions because each region has its specific compliance frameworks (GDPR)
* **GuardDuty**  has given us **great insights that could have been security incidents** if our incident response team hadn’t been made aware quickly
* **Cloudtrail** which monitors and records account activity across AWS infrastructure. This greater visibility simplifies auditing procedures.
* ZS estimates that this automated solution saves about **1,000 hours of labor every month**
* ZS is onboarding new clients **three times faster** using stackable security

# Module 8

## System Manager (Cloudwatch agent a little bit)

[RackSpace](https://aws.amazon.com/solutions/case-studies/rackspace-case-study/?did=cr_card&trk=cr_card)

### Activity
The have a solution called **VM Management** to manage EC2 infrastructure for their clients on their behalf.
The solution is **multi cloud**

### Problem

Managing **multicloud** environments **at scale reliably and cost-effectively was a challenge** because organizations had to manually perform activities across a fleet of **hundreds of thousands** of different compute instances.

If the Rackspace team detected a **security vulnerability** on a customer’s system or a customer requested a **patching activity**, a Rackspace employee had to **log in** to the customer’s infrastructure, investigate and troubleshoot the issue, and perform **manual patching**

The solution extended to on premises instances also.
* Historically, organizations have each needed a **large IT team** to complete time-consuming tasks such as **patching, agent distribution, server diagnostics, and issue remediation**


### Solution

* mass patching at scale, covering **more than 62,000 VMs** across all its managed services
* **reduced overhead** and **improved support efficiency** by using **a single solution**
* **eliminate the cost and complexity** of patching their own infrastructure. The automation also **improves security** by **avoiding errors** associated with manual tasks
* handled more than 38,000 incidents  in just **2 months** between August and September 2021
* Used AWS Systems Manager to send **10,660 automated responses**, which not only **saved 1,480 labor hours** and reduced costs but also drove **faster response times** for customers. 
* Overall, Rackspace automated **70 percent of manual remediation**. Rackspace also uses AWS Systems Manager to **automatically resolve** some of those issues
* The Amazon **CloudWatch agent** on the VMs performs monitoring and alerting based on the events happening in customers’ infrastructure. **During the same 2-month span** in 2021, Rackspace used Amazon CloudWatch to ingest **14,670 alarm events** across all its products that use the AWS service
* automate **more than 150 runbooks**
* reduces complexity for customers by providing a **single-pane view** of their environments, **even hybrid and multicloud ones**.

# Module 9 : Containers

## EKS

[Biz2Credit](https://aws.amazon.com/solutions/case-studies/biz2-credit/?did=cr_card&trk=cr_card)

### Activity

helps small companies secure loans fast through a platform that banks can use to offer their own lending services.

### Problem
They were cloud native from the start, and used to manage entirely their Kubernetes cluster.

Our goal was to **optimize operations**, **reduce costs**, **expedite infrastructure set ups for our customers**, and **enhance our Biz2x platform’s reliability**

They decided to move on to EKS to be able to scale faster.

### Solution

* Now, the company **no longer needs to manually adjust master nodes** behind Kubernetes clusters — a task that needed **application downtime**. Amazon EKS **automatically scales** our control plane, helping us increase uptime **from 99.9 to 99.999 percent**
* Biz2Credit has **reduced IT costs** through management savings and the integration of Karpenter. **Karpenter manages auto scaling** and select the **optimal EC2 instances** for each K8s node. we’ve lowered our Kubernetes costs by **25−30 percent**.
* **With the cost savings** achieved through migrating to Amazon EKS, Biz2Credit has been able to **invest in improving its security posture**. The company now utilizes various AWS security services, such as **AWS Config, Amazon GuardDuty, Container Insights, CloudWatch Logs Insights, Amazon Inspector, Amazon Detective, and Amazon Macie** to ensure the security of applications and workloads.
* Biz2Credit can offer a **better customer experience**, **lowering the time** it takes **to onboard companies** to its online marketplace or Biz2X. Setting up infrastructure for a new bank used to take us **3−4 days**, but with Amazon EKS, our delivery time is reduced to **5−6** hours

# Module 10 : Networking 2

## Transit gateway

[ZenDesk](https://aws.amazon.com/blogs/networking-and-content-delivery/zendesks-global-mesh-network-how-we-lowered-operational-overhead-and-cost-by-migrating-to-aws-transit-gateway/?trk=el_a134p000003yz30AAA&trkCampaign=CSI_Q3_2020_TGW_ZendeskBlog&sc_channel=el&sc_campaign=CSI_Q3_2020_TGW_ZendeskBlog&sc_outcome=Enterprise_Marketing&sc_geo=mult)

!!! Show the architecture on the blog !!!

### Activity

* Global CRM Company. 160 countries and territories. 
* Builded a in-house network technology for interconnecting many VPCs across multiple regions and our on-premises. 
* Due to the large number of **dynamic VPN tunnels** this setup created, the project was aptly named **Medusa**

### Problem

* This architecture allowed for **flexible connectivity** between VPCs, as well as our on-premises networks for about three years. It could **scale up or out** to a certain point, **self-heal**, and **the deployment of new infrastructure was effortless** compared to previous days, as it was heavily automated.

That said, there were some drawbacks. 
* **Managing all the EC2 Medusa Routers turned out to be a bit more daunting than expected**. 
* Stay on top of **software vulnerabilities**
* **rotate the fleet** of immutable routers frequently. 
* It also required us to set up **different monitoring profiles depending on the EC2 instance type used as a router**, as each has unique network capacity, limits, and quirks.

### Solution

* The migration from our in-house networking solution to AWS Transit Gateway **removed a lot of moving parts** in the Zendesk network architecture. 
* It also translated to **less overhead and cognitive load** on our Network team. 
* Each transit gateway attachment can achieve throughput up to **50 Gbps**, more than enough for our current cross-Region traffic demand. 
* Replacing our EC2 infrastructure with this managed service also helped **reduce our overall AWS cross-Region network spend by close to 50%**
* **The amount of toil** that was eliminated by the migration **released cycles back to our team**, enabling us to deep dive into other challenges up in the network stack. This helps keep us ahead of demand as the global Zendesk customer base continues to grow rapidly
* Note that they needed to use a **Lambda to manage Dynamic propagation** through their Transit Gateway peering. Now AWS released **CloudWAN** to overcome this limitation

# Module 11 : Serverless

## SNS

[Armut](https://aws.amazon.com/solutions/case-studies/armut-case-study/?did=cr_card&trk=cr_card)

### Activity

Digital application that link consumer and professionals on topics like moving, wellness, health...

* The **notifications** sent to customers and professionals via email, SMS, or push notifications are **central to the customer experience**. 
  * They communicate the **various steps needed for the work to be completed**, such as confirming the job and setting up a time. 
  * They also notify customers if a professional arrives late, a job is cancelled, or payments are due.

### Problem

* company **grew by more than 1,000 percent** over the last 5 years,
* its **existing notification system no longer met its needs**, with **notifications often failing**. 
* It also **didn’t scale well**, while its day-to-day maintenance requirements were becoming **challenging and time-consuming** for the IT team

### Solution

* Armut developed and implemented its new notification system in just **6 months** using **AWS Lambda**
* Armut can now send **many more notifications** in a given time period than it could previously—in one trial, the system sent **1,000 emails per second**.
* Today, it delivers more than **1.5 million emails a day** over Amazon **Simple Email Service**, a high-scale inbound and outbound cloud email service.
* Around **20 million push notifications** and **3 million SMS notifications** are sent **a month**, with this expected to grow as more customers use the service. The ability to send more notifications also has a **direct impact on income**, as Armut charges professionals to provide quotes.

# Module 12

## Firewall Manager and Shield Advanced

[Outsystems](https://aws.amazon.com/solutions/case-studies/outsystems-case-study/?did=cr_card&trk=cr_card)

### Activity

it's a low code platform (ETL like)

The company manages a **large and growing number of application load balancers** — **over 4,000 as of 2022** — and serves **thousands of applications** across all load balancers.

### Problem

* Its customers’ applications have **different usages and traffic patterns depending on the use case**, making it **challenging for OutSystems to manage the wide range of behaviors and security postures**. 
* Prior to using AWS services for a security solution, OutSystems supported two customers with their own custom security protection solution. 
  * However, this solution required a **significant amount of manual effort** from the company and **didn’t offer protection at scale**

* They migrated to AWS with WAF, Firewall Manager and Shield

But still : 
* Previously, an analyst and an operator would have to create the **local WAF** and **deploy the rules** with the solution **when reacting to an event**

### Solution

* Can manage the security posture of **all customers from a central place** by deploying rules that are specific to our technology and blocking malicious events
* can **define rules** while **leaving room for local configuration options based on a country’s regulations or a company’s policies**
* Using AWS, we reduced 2 hours of work to less than 5 minutes
* OutSystems **reduced its costs by 88 percent per month** by upgrading to **Shield Advanced**. The company gains these significant cost savings on an ongoing basis despite its scale because **it no longer needs to pay for each WAF or rule**

## Cloudfront

[Zalando](https://aws.amazon.com/fr/solutions/case-studies/zalando-case-study/)

### Activity

il s'agit d'un site qui fait le lien entre des consommateurs et des vendeurs, axé sur la mode. Besoin de diffuser des photos sur son site.

### Problem

ils avaient un ancien CDN non satisfaisant
* manque de visibilité opérationnelle (log...). 
* Flexibilité limitée dans la configuration

### Solution

* La migration a duré **4 mois**.
* Migration de **20 sites web**
  * total de **26,93 Po** de données
  * Le pic de trafic a régulièrement dépassé les **100 000 requêtes par seconde**
* Utilisation de Lambda@Edge et Cloudfront functions pour 
  * normaliser la largeur des images
  * réécrire les URL en fonction du type d'appareil de l'utilisateur
* Raux de succès de cache (Cache hit ratio) de **99,5%**
* **5 milliards** d'images par jour
* Projet pour mettre de la vidéo

# Module 13

## Backup

Can use eventually the story with Storage Gateway
