# Woowa Brothers - Wavelength

[Woowa Brothers](https://aws.amazon.com/solutions/case-studies/woowa-brothers/?did=cr_card&trk=cr_card)

## Context

* Woowa Brothers is a South Korean company specializing in food delivery software and mobile applications.
* They aim to become a comprehensive food technology company and are expanding internationally and into new business verticals.
* They are investing in cutting-edge technologies like AI, IoT, and robotics, including their self-driving delivery robot, Dilly Drive.

## Issue

* Woowa Brothers needed to overcome the technical challenges of operating autonomous delivery robots in outdoor environments.
* Factors like weather, road conditions, and unexpected obstacles required real-time responses for safe and efficient operation.
* Existing network infrastructure, like 4G LTE, could not meet the low latency requirements for real-time robot control.

## Solution

### Solution Description

* Woowa Brothers partnered with SK Telecom and AWS to implement a remote management system for Dilly Drive using 5G mobile edge computing.
* This system allows for real-time monitoring and control of the robots, enabling them to navigate complex outdoor environments safely.
* Operators can remotely adjust robot speed, react to obstacles, and monitor surrounding conditions to ensure safe delivery.

### Technology Used

* AWS Wavelength: Enables ultra-low latency communication between the robots and the control center by integrating AWS services with SK Telecom's 5G network.
* SK Telecom's 5G Network: Provides the high bandwidth and low latency required for real-time data transmission and robot control.
* Video Surveillance System: Integrated with the robot control system to provide operators with real-time visual feedback of the robot's surroundings.

### Key Performance Indicators

* Reduced Latency: AWS Wavelength and 5G enabled near real-time robot control, significantly reducing latency compared to 4G LTE.
* Improved Safety: Real-time monitoring and control allowed operators to react to obstacles and adjust robot behavior for increased safety.
* Increased Operational Efficiency: Remote management capabilities enabled efficient monitoring and control of multiple robots simultaneously.
* Successful Pilot Programs: Dilly Drive completed over 3,000 orders and logged 1,250 kilometers during pilot testing, demonstrating the solution's effectiveness.
* Expansion to Public Trials: The solution's success in pilot programs led to public trials in residential areas, showcasing its real-world applicability.

# Atlassian - Global Accelerator

[Atlassian](https://aws.amazon.com/solutions/case-studies/atlassian-aws-global-accelerator/?did=cr_card&trk=cr_card)

## Context

* Atlassian, an Australian software company, aimed to enhance the performance of its code-management service, Bitbucket.
* Bitbucket had a global user base, with over 50% of users located outside the US, while its data center resided in the US East (Northern Virginia) Region.

## Issue

* Bitbucket users, especially those outside the US, experienced significant latency due to the distance their traffic had to travel across the public internet.
* Users reported issues such as internet outages, blocked IP addresses, and slow service, impacting their code collaboration workflows.
* Bitbucket's reliance on single-homed Network Load Balancers with a limited number of static IPs further exacerbated these issues, particularly for customers using IP allow lists.
* The complex network paths involving multiple ISPs between users and the Bitbucket data center contributed to performance degradation and were outside Atlassian's direct control.

## Solution

### Solution Description

* To address these challenges, Atlassian implemented AWS Global Accelerator to optimize Bitbucket's network performance.
AWS Global Accelerator routes user traffic through AWS's global network infrastructure, bringing Bitbucket's edge closer to users worldwide.
* This approach minimizes the impact of unreliable ISPs and reduces latency by leveraging AWS's extensive network of points of presence.
* The solution also maintained support for static anycast IP addresses and preserved customer source IP addresses, crucial for Bitbucket's security features and IP-based access controls.

### Technology Used

* AWS Global Accelerator: Core service for routing traffic and improving performance.
* Amazon Route 53: Facilitated the migration of traffic from Network Load Balancers to AWS Global Accelerator in a controlled manner.

### Key Performance Indicators

* Global response time improvement: 8-45% reduction.
* Response time improvement in US West Coast, UK, and Ireland: 20% reduction.
* Average user experience improvement: 500 ms reduction in latency.
* Improvement for users with slower response times: 800 ms reduction in latency.
* Download speed improvement for some customers: 100% or more increase.
* Engineering effort reduction: Achieved significant performance gains with less engineering effort compared to alternative solutions.