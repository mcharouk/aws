# Table of Contents

- [Pfizer - Health care](#pfizer)
- [ABP Network - Media](#abp-network)  
- [Crypto.com - Finance](#cryptocom)
- [Amazon's New AI-Powered Children's Story Feature](#amazons-new-ai-powered-childrens-story-feature)


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

# Crypto.com

[Crypto.com](https://aws.amazon.com/solutions/case-studies/case-study-crypto/)

## Context

*   Crypto.com is a large cryptocurrency exchange and trading platform serving 100 million users across 90 countries.
*   The company is focused on driving user adoption of cryptocurrency through partnerships and a comprehensive service offering.
*   They leverage AI to improve customer experience, including sentiment analysis for market insights.

## Issue

*   Crypto.com needed to provide timely and accurate market intelligence to its users, particularly sentiment analysis of crypto news.
*   Existing open-source machine learning (ML) models had limitations in accuracy, especially with multilingual data.
*   Self-hosting large language models (LLMs) was proving to be expensive and computationally intensive.
*   They needed a solution to effectively integrate and synthesize outputs from multiple ML models (both pre-trained and custom) for reliable market insights.

## Solution

### Solution Description

Crypto.com implemented a multi-agent consensus-seeking solution for sentiment analysis on AWS, leveraging both pre-trained and fine-tuned models. This allowed them to efficiently deliver accurate, comprehensive, and localized crypto market insights to their global user base.

### Technology Used

*   Anthropic Claude 3 LLMs on Amazon Bedrock for sentiment analysis and application development.
*   Amazon SageMaker for fine-tuning custom models.
*   Amazon EC2 for fine-tuning open-source models like Mistral AI and Meta Llama.

### Key Performance Indicators
*   **Speed:** Sentiment analysis results delivered in less than 1 second.
*   **Accuracy:** Improved accuracy in sentiment analysis, especially for multilingual news and new coins.
*   **Scalability:** Highly scalable models on Amazon Bedrock, capable of processing vast amounts of data in real-time.
*   **Cost Reduction:** Eliminated the manual effort, extra cost, and computational constraints of self-hosting LLMs.
*   **Customer Satisfaction:** Positive feedback from users regarding the improved market insights.





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


