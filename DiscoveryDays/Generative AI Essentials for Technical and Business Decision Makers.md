# Table of contents

- [Table of contents](#table-of-contents)
- [Business insights](#business-insights)
- [Technical Foundations](#technical-foundations)
  - [Model](#model)
  - [Transformers](#transformers)
  - [Context](#context)
  - [Inference parameters](#inference-parameters)
  - [Tuning a Model](#tuning-a-model)
- [Risks and Mitigations](#risks-and-mitigations)
  - [Fairness](#fairness)
    - [Mitigations](#mitigations)
  - [Privacy](#privacy)
    - [Mitigations](#mitigations-1)
  - [Toxicity](#toxicity)
    - [Mitigation](#mitigation)
  - [Hallucinations](#hallucinations)
    - [Real case study](#real-case-study)
      - [Description](#description)
      - [Conclusion](#conclusion)
    - [Mitigations](#mitigations-2)
  - [Intellectual property](#intellectual-property)
    - [Mitigation](#mitigation-1)
  - [Plagiarism and cheating](#plagiarism-and-cheating)
  - [Disruption of the nature of work](#disruption-of-the-nature-of-work)
  - [Guardrails details](#guardrails-details)
- [GenAI Organization Overview](#genai-organization-overview)
  - [Start with leaders](#start-with-leaders)
    - [Drive](#drive)
    - [Discover](#discover)
    - [Understand](#understand)
  - [Prepare your employees](#prepare-your-employees)
    - [Feedback loop](#feedback-loop)
  - [GenAI \& Cloud Operating Model](#genai--cloud-operating-model)
    - [Envision](#envision)
    - [Discover](#discover-1)
    - [Build](#build)
    - [Deliver](#deliver)
  - [Team Success](#team-success)
    - [People enablement](#people-enablement)
      - [Expertise](#expertise)
      - [Data strategy](#data-strategy)
      - [Cloud infrastructure](#cloud-infrastructure)
      - [Security](#security)
      - [Continuously Evaluate and improve](#continuously-evaluate-and-improve)
    - [Governance](#governance)
      - [Transparency](#transparency)
      - [Ethical principles](#ethical-principles)
    - [Data privacy and security](#data-privacy-and-security)
- [GenAI Services](#genai-services)
  - [Q for Business](#q-for-business)
  - [Q for developers](#q-for-developers)
  - [Q integration with other services](#q-integration-with-other-services)
- [Governance Framework](#governance-framework)


# Business insights

* [McKinsey Report - business value](https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/the-economic-potential-of-generative-ai-the-next-productivity-frontier#business-value)


* [McKinsey Report - industry impacts](https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/the-economic-potential-of-generative-ai-the-next-productivity-frontier#industry-impacts)
# Technical Foundations

## Model

* Model store deeper and larger content that other ML models that are more specialized
* 2 constraints
  * Have sufficient quality training data
  * Have sufficient power calculation
* Examples of Foundation models
  * Amazon Titan (AWS)
  * Jurassic (AI21 Labs)
  * GPT (OpenAI)
  * Cohere Command (Cohere)
  * Claude (Anthropic)
  * Mistral (Mistral AI)
  * Stable Diffusion (text to image) (Stability.AI)
  * BLOOM (Hugging Face)
* Model types
  * Large Language Models (LLMs) : Text to text
  * Multimodal Models
    * unstructured data to text, text to unstructured data
    * unstructured data : (text, images, audio, video)
  * Speech and Audio Models
    * Applications: Speech recognition, text-to-speech, music generation
  * Code models
  * Domain specific models
  * Embedding models

## Transformers

* Easy to parallelize, because it processes a sentence as a whole, not word by word, like former models (RNN -> Recurent Neural Network)
  * **Position encoders** encode words position. Learns the importance of word order
  * Self attention
    * know which word it's attending to based on previous words. Learned from data. Like this, it can learn all the grammatical rules. 
    * remember the context around a word. Captures importance of each word in a sentence and relationship between words.
    * can understand the underlying concept behind a sentence. Much more powerful than previous methods for translation.
  
* Transformers are made of encoders and decoders. Encoders capture the meaning, decoder can restitue the result, according tho the meaning.
* Words are transformed in tokens. Tokens are encoded in multidimensional vectors

* bank : homonyme anglais de **banque** et **rive**

## Context

* Context Window is the number of tokens the model can take as input when generating responses. Typically a few thousands words, depends on the model

## Inference parameters

* Max New Tokens : max number of tokens a LLM can produce
* Top K : the model returns a dict with probabilities attached to each word. When using Top K, we select the next word from the top K words with the highest probabilities
* Repetition Penalty : discourage the repetition of tokens in generated text
* Temperature : adjusts the level of randomness when selecting the next token. A higher temperature value indicates a broader and more evenly distributed probability range, promoting greater diversity in token selection, that is creativity. On the other hand, a lower temperature value results in a more focused and peaked probability distribution, leading to less variation and potentially more conservative choices.
* Do Sample : determines whether the model selects the next token based on their probabilities or simply chooses the token with the highest probability. False means get only highest probability


## Tuning a Model

use cases : 

* Domain-specific language generation : learn the specific terminology, style, and conventions of a domain
* Code generation for specific programming languages or frameworks
* Task-specific performance improvement: For tasks like sentiment analysis, named entity recognition, or text classification in specific contexts, fine-tuning can significantly improve the model's accuracy compared to prompt-based approaches

# Risks and Mitigations

## Fairness

* if training data contains biases : nurses are women and doctors are men.
* For example, if you ask to generate a script for advertising, AI will reproduce these stereotypes
* AI will be perceived as unfair

### Mitigations

* We can influence results with prompts, but that means it's a proactive strategy.
* We can change the training data by tuning the model and feed him with data that balance these stereotypes

## Privacy

* Using a public version of a model
  *  You're private data can be used for training and so could be reused in answers
  * For example AI could reuse code to answer developers with some light modifications like changing variable names
* If LLM is working on private data, it could inadvertendly expose private informations in the prompt. *Based on (private fact), my analysis is (...)*
* pay attention to the logs. Sensitive data could appear here too
  * Bedrock is integrated in with cloudwatch, with a feature that can mask 10s of sensitive data types in the logs.

### Mitigations

* use private models
* Bedrock Guardrails to filter sensitive data
* Cloudwatch [Data Protection Policy](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/cloudwatch-logs-data-protection-policies.html) 


## Toxicity

* hate speech, biased statements, and any language that targets individuals or groups based on sensitive characteristics like race, gender, religion, or sexual orientation.
* it's not easy for an LLM sometimes to differentiate between unappropriate content and opinions.
* LLM can be manipulated with prompts or have biased that comes from the training data

### Mitigation

* Guardrails
* Prompt Engineering

## Hallucinations

### Real case study

[Canada Lawyer fake cases](https://www.theguardian.com/world/2024/feb/29/canada-lawyer-chatgpt-fake-cases-ai)

#### Description

* A Canadian lawyer, Chong Ke, is under investigation after using ChatGPT for legal research in a child custody case (garde d'enfants), highlighting significant risks of using generative AI in legal settings.

* Key Issues with AI Use:
  * ChatGPT generated completely fictitious legal cases that Ke submitted to the British Columbia supreme court
  * The opposing counsel could not locate these non-existent cases despite multiple attempts
  * This incident demonstrates the danger of AI "hallucinations" - fabricated information presented as factual
  * The court described citing fake cases as "an abuse of process" that could potentially "lead to a miscarriage of justice"

#### Conclusion

While the judge accepted Ke's apology and did not find intent to deceive, the Law Society of British Columbia **has launched an investigation** into her conduct. This case serves as a stark warning about the risks of relying on untested AI technologies in professional legal work without proper verification.

### Mitigations

* Data Quality
* RAG
* Quote the sources
* Make explicit the limitation of AI

## Intellectual property

* Legal ambiguities on copyrights :
  * Generate paintings in the style of someone
  * Get the voice of some singer and use it in some song.

### Mitigation

* Prompt engineering : limit the scope of what AI can do

## Plagiarism and cheating

* the issue is how it can be used by LLM users. For example, for education assignments, students can just copy/paste the content. Hard to detect that it came from an IA
* there are some [detectors](https://www.zerogpt.com/) that can evaluate if some content has been written by a genAI or not.

## Disruption of the nature of work

* IA could change the way we work. Could make disappear some jobs and create some other jobs.

## Guardrails details

* Bedrock guardrails can filter content provided by user or by LLM
  * can filter harmful content (hate, insults, sexual, violence, misconduct, prompt attack)
  * can provide topics that are denied. For example the LLM will not be able to reply to questions about security, finance, etc...
  * Sensitive information filtering (PII) (  [list of blocked or masked attributes](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-filters.html)  )
  * Word filters : provide a list of words or sentences that are denied
  * Grounding : Check response accuracy based on your entreprise data (RAG)

# GenAI Organization Overview

* People first approach : investment in technology + change of culture
  * Provide people the training and the resources to effectively use GenAI technology
  * Implements processes and governance (to ensure responsible and ethical use of the technology)
  * Requires full implication of C-level executives, director and senior leaders

## Start with leaders

* As a leader, get insights to know where the organization needs to support generative AI initiatives. 

### Drive

* shared vision of GenAI
* how to deal with organizational changes
* Discuss use cases with business leaders. 
* Explain expected benefits

### Discover  

* Evaluate how initiatives perform across multiple key business areas
  * *Discover* : through informal discussions, surveys, understand if the support you provide is relevant or not
* it can facilitate decision-making regarding 
  * talent acquisition, 
  * the required level of training for current employees, 
  * acceleration of recruiting and skill-building needed.
  
### Understand

* consider the impact genAI will have on employees. This will determine the level and effort needed

## Prepare your employees

* Educate your employees. The natural reaction in front of something that we don't understand is fear.
* **Think scale, not replace**. 
  * Scale on market : GenAI can give ideas that the company never had before, so it drives innovation.
    * improve marketing campaign
    * create new products and services
  * Scale on number of tasks : GenAI can be seen as an assistant to be more efficient (for example developers will not disappear because of IA)
    * increase efficiency
    * reduce costs
    * improve customer service
  * Scale on new roles

### Feedback loop

* Encourage staff to share thoughts and worrying
* Put IA in place that it is practical and useful for employees
* Create a feedback loop to improve the product. Might ask the users to rate the response, provide multiple FM models to see which one people prefer

* Make analogy with computer, smartphones, etc... It's an opportunity to learn new tech, new ways of doing, but without losing every knowledge they have already acquired.

## GenAI & Cloud Operating Model

Cloud Operating Model categories

* Operations leadership
* Cloud operations
* Platform enablement
* Service management
* Cost and governance


Impacts on [Cloud Operating Model](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/foundational-capabilities.html): 

* Enhanced Automation: Automate routine tasks, allowing your team to focus on strategic initiatives.
* Innovation Acceleration: Develop and deploy new AI-driven services quickly.
* Efficient Resource Management: Optimize cloud resources and reduce operational costs.
* Improved Decision Making: Leverage AI for data-driven insights and predictive analytics.

A Robust Cloud Operating Model supports : 

* Smooth Integration: **Seamlessly incorporate AI** into your cloud strategy.
  * Focus on DQ and data availability
* Skill Development: **Upskill your workforce** to handle AI-powered tools and platforms.
  * Collaborate with experts in the field
* Scalability: **Ensure your cloud infrastructure can scale** with AI demands.
  * Invest in Cloud Infrastructure
* Governance: **Maintain strong oversight and compliance** as AI capabilities grow.
  * Prioritize Security And Privacy
  * Transparency and accountability
  * Ethical principles and guidelines

### Envision

* It's about having a vision of how GenAI will impact the business 
  * who are the stakeholders involved ? 
  * What are desired outcomes ?
  * What are the use cases ?
    * customer success stories, news
    * search for pain points for your employees and search when GenAI can help (Working Backwards)
  * what KPIs
    * Cost Reduction
    * utilization de l'IA / Satisfaction
    * Metriques sur l'efficacité
  * create a clear vision and roadmap for leveraging Gen AI to achieve their business objectives ?
  * Discover the challenges, security concerns, ethical issues.


### Discover

* Evaluate the your current cloud capabilities, prior to generative AI, to benchmark maturity. 
* Consult with operational leaders to identify any team constraints and upskilling opportunities.

### Build

* Define clear guidelines and processes for integrating Gen AI into your cloud environment. Ensure alignment with existing governance and compliance frameworks.
* Investing in Skills and Training
* Adapt Cloud Infrastructure to prepare for GenAI

### Deliver

* Develop a road-map for implementation steps of a specific use case
* Measure your improvements against original desired outcomes. 
* Test and refine the model as your organization continues developing your generative AI capabilities.
  * regularly check model performance
  * define what to do on a foundation model upgrade

## Team Success

### People enablement

#### Expertise
Experts : [Generative AI Innovation Center](https://aws.amazon.com/ai/generative-ai/innovation-center/)

#### Data strategy

* note that a focus should be done a quality, availability and governance of all **unstructured data**


#### Cloud infrastructure

* Cloud infrastructure

  *  Availability of performant infrastructure
  *  With Serverless pattern, earlier positive ROI

#### Security

* Use cases oriented
  * Define Specific application use Cases (easier to control)
  * Guardrails on PII
  * Human in the loop process to check outputs (once every week for ex.)    
    * Scan the code (prompt attacks)
    * Prompt attacks challenge
      * [Prompt attack challenge](https://prompting.ai.immersivelabs.com/)
      * [Solution](https://denizsivas.medium.com/prompt-injection-challenge-how-far-can-you-go-9d78c18df51d)  
    * Popular SAST
      * Snyk Code
      * Checkmarx
      * SonarQube
      * Note that CodeGuru Reviewer currently does not have these kind of checks.

* Prompt attacks types
  * **Prompt injection** : Inserting instructions that override the AI's original guidelines
  * **JailBreaking** : Using creative workarounds or roleplaying scenarios to trick the AI into responding to prohibited content
  * **Prompt leaking** : Attempting to extract the AI's underlying instructions or system prompts

#### Continuously Evaluate and improve

* data refresh
* process to integrate new model upgrades
* testing, validation


### Governance

#### Transparency
* Regarding users
  * Tell when AI is being used, how it works, risks associated (Service Cards)
  * [Service Card Structure](https://aws.amazon.com/blogs/machine-learning/introducing-aws-ai-service-cards-a-new-resource-to-enhance-transparency-and-advance-responsible-ai/)
    * Basic concepts to help customers better understand the service or service features
    * Intended use cases and limitations
    * Responsible AI design considerations
    * Guidance on deployment and performance optimization  
  * Ask for GenAI to display its sources  
* Regarding compliance
  * AWS AI services are all integrated with CloudTrail (Bedrock, Q for Developer, ...). 
  * Logs all intermediate steps when using Bedrock agents.

#### Ethical principles
  * identify issues at high risk and find mitigations

### Data privacy and security

* Tag/Identify confidential data
* Encryption at rest and in transit. Data and model
* Data access (IAM), LakeFormation. Minimize access
  * blur/anonymize data used for training
  * Data lifecycle rules (removing personal data, refreshing model with new data)
* Audit/log the data that comes in and out

# GenAI Services

## Q for Business

* [Q Business Workflow](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/how-it-works.html#app-flow)
    * Managed chat application
    * Managed ingestion pipeline
    * Many connectors
    * Implement Guardrails
    * Implement responses fallback on plugins, or on LLM answers 
* Q Apps on top of Q for Business

## Q for developers

* live code generation or on a specific answer
* troubleshooting
* code explanation
* security scans
* code migration (Java 11 -> Java 17)

## Q integration with other services

* Glue (build pipelines)
* Quicksight
* Amazon Connect (customer service assistant)
* EC2 (helps to choose an EC2 instance type)
* Reachability Analyzer (troobleshoot network issues)
* Redshift (generate SQL Queries)
* ChatBot (integrated with chat groups). Chatbot can integrate with Teams, Slack and Chime

# Governance Framework

[GenAI Security Scoping Matrix](https://aws.amazon.com/blogs/security/securing-generative-ai-an-introduction-to-the-generative-ai-security-scoping-matrix/)


* Dimensions
  * Governance and compliance : The policies, procedures, and reporting needed to empower the business while minimizing risk.
  * Legal and privacy : The specific regulatory, legal, and privacy requirements for using or creating generative AI solutions.
  * Risk management : Identification of potential threats to generative AI solutions and recommended mitigations.
  * Controls : The implementation of security controls that are used to mitigate risk.
  * Resilience : How to architect generative AI solutions to maintain availability and meet business SLAs.
