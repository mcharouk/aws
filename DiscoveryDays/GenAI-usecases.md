# Table of Contents

- [SBI Life Insurance - Insurance](#sbi-life-insurance)  
- [Pfizer - Health care](#pfizer)
- [ABP Network - Media](#abp-network)  
- [Tymex - Code Generation](#tymex)
- [Amazon Pharmacy](#amazon-pharmacy)
- [Amazon Ads](#amazon-ads)
- [Amazon's New AI-Powered Children's Story Feature](#amazons-new-ai-powered-childrens-story-feature)
- [Bravante - Oil Industry](#bravante)

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

# Pfizer

* Used RAG

[Pfizer](https://aws.amazon.com/solutions/case-studies/pfizer-PACT-case-study/?did=cr_card&trk=cr_card)

* The development of one drug can result in approximately **20,000 documents**, and scientists often must look for data **manually** using a variety of tools to find historical data
* Pfizer uses Amazon Kendra to index documents
* PACT teams now use generative AI, accessing Anthropic’s Claude 2.1 through Amazon Bedrock, to summarize results and to provide orders in natural language
* give order by chat or by voice
* Pfizer estimates that, annually, scientists could save up to **16,000 hours** of searching and extracting data
* minimize the time spent in data discovery up to **80** percent for **1 500** PSSM scientists
  
# ABP Network

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
* image turnaround time is now **5x** faster, with image acquisition costing **50 %** less
* **10 % boost** in audience engagement and click-through rates
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


[Tymex Use Case](https://aws.amazon.com/solutions/case-studies/tymex/)

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
* An internal AI chatbot was developed to streamline internal communication
  * AI to select good CV of engineering and development roles
  * AI to summarize complex documents about compliant software design and compliance documentation

### Technology Used

* Amazon Q Developer
* Amazon Bedrock

### Key Performance Indicators (KPIs)

* Developer Productivity: Developers experienced a **40%** increase in productivity due to automation and AI assistance.
* Code Coverage: Unit testing efficiency increased significantly, achieving **89%** code coverage in **30 minutes** compared to the previous **5 hours** (a **90%** improvement).
* Time to Market: Development cycles were accelerated, with the second digital bank built in 18 months compared to the first in 3 years, and the third expected in just 9 months.
* Employee Satisfaction: Developers gained more time for innovation, skill development, and learning new technologies.
* Chatbot Adoption: The internal AI chatbot "Tymee" received a 77% positive feedback score from internal users.
* Document Processing: AI-powered chat-to-document feature summarizes 100-page documents in under 10 seconds, improving efficiency in understanding complex information. Documents about compliant software design and compliance documentation to launch financial institutions internationnally.

# Amazon Pharmacy

* Used RAG with SageMaker (no Bedrock)

* [Amazon Pharmacy](https://aws.amazon.com/blogs/machine-learning/learn-how-amazon-pharmacy-created-their-llm-based-chat-bot-using-amazon-sagemaker/)

# Amazon Ads


* Used SageMaker Jumpstart
* Tried multiple text-to-image foundational model, and refined them with custom data. Reviewed the image with a human-in-the-loop process using Amazon Groundtruth
* Finally selected the best model

* [Amazon Ads](https://aws.amazon.com/blogs/machine-learning/learn-how-amazon-ads-created-a-generative-ai-powered-image-generation-capability-using-amazon-sagemaker/)


# Amazon's New AI-Powered Children's Story Feature

## Personalized Stories

* Users can choose themes (e.g., "underwater," "enchanted forest"), protagonists (e.g., pirate, mermaid), colors, and adjectives (e.g., "silly," "mysterious") to guide story generation.
* AI generates a unique five-scene story with illustrations, background music, and sound effects based on the chosen prompts.

## Hybrid Approach

* Combines AI generation with curated elements for a balance of creativity and control.
* Uses a library of artist-rendered and AI-generated backgrounds and objects.
* AI determines object arrangement and animation.
* Music generation blends composer-created patterns with AI-generated melodies.


## Story Generation Process

* Planner Model: Takes user prompts and creates a detailed keyword plan for each scene.
* Text Generator Model: Uses the plan to generate the story text.
* Trained on human-written stories, including those created by Amazon writers.
* Coherence ranker ensures plot consistency and overall quality.

## Scene Generation

* Uses a pipeline of models due to limited training data.
* NLP Modules:
  * Coreference resolution clarifies pronoun references.
  * Dependency parsing maps relationships between objects.
* Scene Generation Model:
  * Selects a background based on theme and NLP output.
  * Chooses and positions objects from the library.

## Music Generation

* Library of artist-created musical elements (chord progressions, harmonies, rhythms).
* AI melody generator expands the library with new melodies.
* Text-to-speech and paralinguistic analysis inform music duration and mood.

## Safety Measures:

* Curated training data to exclude offensive content
* Pre-curated input prompts
* Automated filtering of inappropriate outputs
* Requires parental consent through the Alexa app

# Bravante

[Bravante Use Case](https://aws.amazon.com/solutions/case-studies/bravante-generative-ai/?nc1=h_ls&did=cr_card&trk=cr_card)

## Context
* RRC Tecnologia, the robotics and technology arm of Grupo Bravante, specializes in marine engineering, particularly in the decommissioning of oil equipment and pipeline removal.
* Brazilian law mandates the restoration of the seabed after oil exploration, requiring accurate location and removal of submerged equipment.
* Traditional methods rely on analyzing scattered and diverse documents, leading to inaccuracies and high costs due to the expensive daily rates of certification vessels.

## Issue

* Locating and removing submerged oil pipelines is a complex and costly process due to reliance on outdated and fragmented documentation.
* Inaccurate location data leads to wasted time and resources, with certification vessels costing $250,000 per day.
* Manual analysis of thousands of documents is time-consuming and prone to errors, hindering efficient decommissioning efforts.
* Considering the more than **800 km** of pipelines to be decommissioned, the data repository has over **10 thousand documents**

## Solution

### Solution Description

* RRC Tecnologia partnered with AWS and Flexa Cloud to develop a Generative AI-powered solution to automate document analysis and improve the accuracy of pipeline location data.
* The solution creates a centralized, reliable data source for pipeline information, streamlining the decommissioning process.
* It leverages advanced AI models to interpret and classify data from various document formats, providing valuable insights for naval engineers.

### Technology Used

* Amazon S3: Stores the vast repository of pipeline documents, providing secure and scalable storage.
* Amazon Textract: Extracts text and data from various document formats (images, spreadsheets, PDFs) using OCR.
* Amazon Bedrock: Offers access to pre-trained foundational models like Anthropic's Claude-2 via APIs, facilitating development and experimentation.
* Amazon Aurora: Stores the processed data in a structured database, enabling efficient querying and analysis.

### Key Performance Indicators (KPIs)

* Reduction in operational load on surveying engineers: Automating document analysis frees up engineers for other tasks.
* Man-hours savings: Automation significantly reduces the time spent on manual document review.
* Increased mapping accuracy: AI-powered analysis improves the precision of pipeline location data.
* Reduction in the number of daily vessels required for field certification: Expected reduction of up to 40%, resulting in significant cost savings.
* Cost savings: Projected to save millions of dollars by minimizing the use of expensive certification vessels (daily rate of $250,000).

# Smokeball AI Case Study Summary for Students

[Smokeball](https://aws.amazon.com/solutions/case-studies/smokeball/?did=cr_card&trk=cr_card)

## Context

* Smokeball provides practice management software for over 6,000 law firms globally (Australia, UK, US).
* Law firms struggle with time-consuming administrative tasks, reducing billable hours and impacting client service.
* Smokeball aimed to leverage AI to improve efficiency and client service for its users.

## Issue

* Manual administrative tasks (document processing, client intake, time tracking) consume significant time and resources.
* Initial exploration of third-party AI solutions faced limitations with APIs and support.
* Need for a scalable, secure cloud infrastructure with advanced AI/ML capabilities to handle sensitive legal data.

## Solution

### Solution Description

* Smokeball developed Smokeball AI, a suite of generative AI tools built on AWS to automate key legal tasks.
* Three main tools:
    * **Archie:** AI assistant for document processing (summarization, analysis, Q&A, drafting).
    * **Intake:** Automates client intake and onboarding by processing and generating customized forms.
    * **AutoTime:** Automates time tracking and billing.

### Technology Used

* **Amazon Bedrock (Claude V3):** Powers Archie's natural language processing capabilities.
* **Amazon SageMaker:** Used for developing and training the machine learning models behind Intake and AutoTime.
* **AWS Lambda:** Serverless compute for handling AI-powered responses.
* **Amazon SQS:** Manages data flow and task management across the platform.
* **Amazon EKS:** Enables scalable deployment and orchestration of the application infrastructure.

### Key Performance Indicators (KPIs)

* **Archie:** Saves up to 3 hours per day on administrative tasks.
* **Intake:** Reduces form creation and population time from 1 hour to 5 minutes.
* **AutoTime:** Reduces timesheet creation time from hours to minutes and increases billable hours capture by up to 30%.
* **Overall:** Smokeball launched the public beta of its AI tools within six months using AWS.
