# SBI Life Insurance

[Use case](https://aws.amazon.com/solutions/case-studies/sbi-life-case-study/?did=cr_card&trk=cr_card)

* Used RAG

## Context

* SBI Life Insurance, a company of SBI Insurance Group, provides various life insurance products and policies.
The Information Systems Department of SBI Life Insurance is responsible for development, maintenance, operation, and security response.
* The team continually builds systems in-house and decided to migrate their applications to a new technology platform using AWS.

## Issue

* SBI Life Insurance aimed to enhance customer service at its call centers and shorten the training period for operators.
* Operators faced difficulties in quickly answering inquiries about discontinued life insurance products due to the enormous variety and volume of related documents.


## Solution Description

* SBI Life Insurance built a document search solution using Amazon Kendra, an intelligent enterprise search service, to let call center workers easily search for documentation on insurance products and policies.
* The solution includes a selfbot function that summarizes and displays Amazon Kendra search results using generative AI.

## Technology Used

* Amazon Kendra
* Amazon Bedrock

## Key Performance Indicators:

* Shortened development period: Released to a production environment in July 2023, **three months** after development started in April 2023.
* Improved call center operations: Significantly improved call center operations and reduced stress on operators.
* Shorter training periods: Reduced training periods by about **30 %**
* Increased applicant interest: Attracted applicants who want to be involved in the intelligent operations projects.

# Health care

* Used RAG

[Pfizer](https://aws.amazon.com/solutions/case-studies/pfizer-PACT-case-study/?did=cr_card&trk=cr_card)

* The development of one drug can result in approximately **20,000 documents**, and scientists often must look for data **manually** using a variety of tools to find historical data
* Pfizer uses Amazon Kendra to index documents
* PACT teams now use generative AI, accessing Anthropic’s Claude 2.1 through Amazon Bedrock, to summarize results and to provide orders in natural language
* give order by chat or by voice
* Pfizer estimates that, annually, scientists could save up to **16,000 hours** of searching and extracting data
  
# Media

* Used prompting
* [ABP News](https://aws.amazon.com/solutions/case-studies/abp-network/?did=cr_card&trk=cr_card)

## Context

* ABP Network, a media company, uses AWS and generative AI to enhance media content creation and procurement.
* The network publishes millions of stories, videos, social media posts, and multimedia content across eight languages annually on ABP LIVE.
* Traditionally, securing images was time-consuming and costly. The editorial workflow for images took **three to four hours** per day.

## Issue

* ABP Network needed to streamline image procurement and video localization workflows, reducing associated time and costs without compromising quality and relevance.

## Solution

* ABP Network deployed Amazon Bedrock and generative AI on AWS for greater efficiency, innovation, and cost savings.
* The solution included an image-generating application, which empowers the editorial team to generate multiple image variations quickly, and a video production application for transcribing, translating, and dubbing videos into multiple languages.
* The image-generating application creates up to 170 image variations in under 10 seconds using simple text prompts, streamlining the image procurement process.
* The video production application transcribes, translates, and dubs a single 300 to 600-second video into four languages within four to six minutes, reducing video localization time by 88%.

## Technology Used

Amazon Bedrock

## Key Performance Indicators:

* 170 image variations generated in under 10 seconds
* 5-fold faster image turnaround time
* 88% reduction in time taken for video localization.
* 50% reduction in image acquisition cost (eliminating the need to purchase costly stock images)
* 10% boost in audience engagement and click-through rates


# Tymex

## Context

* TymeX is a digital banking platform focused on providing services to underserved and underbanked populations.
* They prioritize an agile development culture and employee satisfaction to drive innovation and deliver high-quality products.
* Recognizing the potential of AI, TymeX embarked on a journey to integrate generative AI into their operations, focusing on security and compliance within the banking industry.

## Issue

* TymeX developers faced challenges with time-consuming tasks in the software development lifecycle, hindering their ability to focus on innovation and feature development.
* There was a need to improve efficiency in understanding complex documentation and streamline internal processes.
* Maintaining a high level of security and compliance in AI implementation was crucial for the banking sector.

## Solution

### Solution Description

* TymeX partnered with AWS to implement and develop generative AI solutions to address their challenges.
* They adopted a two-phased approach: initially leveraging existing AWS AI services and subsequently building custom AI applications.
* The solution focused on automating recurring development tasks, enhancing code quality, and providing AI-powered assistance to developers.
* An internal AI chatbot was developed to streamline internal communication and support various tasks, including HR processes.

### Technology Used

* Amazon Q Developer
* Amazon Bedrock

### Key Performance Indicators (KPIs)

* Developer Productivity: Developers experienced a 40% increase in productivity due to automation and AI assistance.
* Code Coverage: Unit testing efficiency increased significantly, achieving 89% code coverage in 30 minutes compared to the previous 5 hours (a 90% improvement).
* Time to Market: Development cycles were accelerated, with the second digital bank built in 18 months compared to the first in 3 years, and the third expected in just 9 months.
* Employee Satisfaction: Developers gained more time for innovation, skill development, and learning new technologies.
* Chatbot Adoption: The internal AI chatbot "Tymee" received a 77% positive feedback score from internal users.
* Document Processing: AI-powered chat-to-document feature summarizes 100-page documents in under 10 seconds, improving efficiency in understanding complex information.


# Amazon Pharmacy

* Used RAG with SageMaker (no Bedrock)

* [Amazon Pharmacy](https://aws.amazon.com/blogs/machine-learning/learn-how-amazon-pharmacy-created-their-llm-based-chat-bot-using-amazon-sagemaker/)

# Amazon Ads


* Used SageMaker Jumpstart
* Tried multiple text-to-image foundational model, and refined them with custom data. Reviewed the image with a human-in-the-loop process using Amazon Groundtruth
* Finally selected the best model

* [Amazon Ads](https://aws.amazon.com/blogs/machine-learning/learn-how-amazon-ads-created-a-generative-ai-powered-image-generation-capability-using-amazon-sagemaker/)
