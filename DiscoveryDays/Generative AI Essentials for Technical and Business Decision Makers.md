# Technical Foundations

## Model

* Model store deeper and larger content that other ML models that are more specialized
* 2 constraints
  * Have sufficient quality training data
  * Have sufficient power calculation
* Examples of Foundation models
  * Amazon Titan
  * Jurassic
  * GPT
  * Cohere
  * Claude (Anthropic)
  * Stable Diffusion (text to image)
  * BLOOM

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
* We can influence results with prompts, but that means it's a proactive strategy.
* We can change the training data by tuning the model and feed him with data that balance these stereotypes

## Privacy

* careful about using public AI models. You're private data can be used for training and so could be reused in answers
* For example AI could reuse code to answer developers with some light modifications like changing variable names
* Legal ambiguities on copyrights :
  * Generate paintings in the style of someone
  * Get the voice of some singer and use it in some song.
* If LLM is working on private data, it could inadvertendly expose private informations in the prompt. *Based on (private fact), my analysis is (...)*
* Bedrock is integrated in with cloudwatch, with a feature that can mask 10s of sensitive data types in the logs.


## Toxicity

* hate speech, biased statements, and any language that targets individuals or groups based on sensitive characteristics like race, gender, religion, or sexual orientation.
* it's not easy for an LLM sometimes to differentiate between unappropriate content and opinions.
* LLM can be manipulated with prompts or have biased that comes from the training data

## Hallucinations

* User input: "When did Leonardo da Vinci paint the Mona Lisa?"
AI-generated response: "Leonardo da Vinci painted the Mona Lisa in 1815."
This is a hallucination because the Mona Lisa was actually painted in 1503-1506. The AI model has made a mistake because it is not trained on enough data about the Mona Lisa

* When filing a response, lawyers for the plaintiff (demandeur) cited at least six other cases to show precedent, but the court found that the cases didn’t exist and had “bogus judicial decisions with bogus quotes and bogus internal citations,” leading a federal judge to consider sanctions. A member of the law team then revealed he had used a generative AI model to conduct legal research for the court filing that referenced the cases and that the artificial intelligence tool assured him the cases were real.

## Plagiarism and cheating

* the issue is how it can be used by LLM users. For example, for education assignments, students can just copy/paste the content. Hard to detect that it came from an IA
* there are some [detectors](https://www.zerogpt.com/) that can evaluate if some content has been written by a genAI or not.

## Disruption of the nature of work

* IA could change the way we work. Could make disappear some jobs and create some other jobs.

## Mitigations

* Bedrock guardrails can filter content provided by user or by LLM
  * can filter harmful content (hate, insults, sexual, violence, misconduct, prompt attack)
  * can provide topics that are denied. For example the LLM will not be able to reply to questions about security, finance, etc...
  * Sensitive information filtering (PII) (  [list of blocked or masked attributes](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-filters.html)  )
  * Word filters : provide a list of words or sentences that are denied
  * Grounding : Check response accuracy based on your entreprise data (RAG)

* Try to test multiple model to consider the best one
* Keep a human in the loop / Generative AI-assisted reviews
* Prompting / RAG (RAG against hallucinations) / Model parameters

# GenAI Organization Overview

* People first approach : investment in technology + change of culture
  * Provide people the training and the resources to effectively use GenAI technology
  * Implements processes and governance (to ensure responsible and ethical use of the technology)
  * Requires full implication of C-level executives, director and senior leaders

## Start with leaders

* drive first alignment among leaders
  * shared vision of GenAI
  * how to deal with organizational changes

* As a leader, get insights to know where the organization needs to support generative AI initiatives. 
  * *Drive* : Discuss use cases with business leaders. Explain expected benefits
* Evaluate how initiatives perform across multiple key business areas
  * *Discover* : through informal discussions, surveys, understand if the support you provide is relevant or not
* it can facilitate decision-making regarding 
  * talent acquisition, 
  * the required level of training for current employees, 
  * acceleration of recruiting and skill-building needed.
* *Understand* : consider the impact genAI will have on employees. This will determine the level and effort needed


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


Impacts on [Cloud Operating Model](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-cloud-operating-model/introduction.html#key-concepts): 

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
  * what KPIs
    * Cost Reduction
    * utilization de l'IA / Satisfaction
    * Metriques sur l'efficacité
  * create a clear vision and roadmap for leveraging Gen AI to achieve their business objectives ?
  * Discover the challenges, security concerns, ethical issues.

* how to find use cases
  * customer success stories, news
  * search for pain points for your employees and search when GenAI can help (Working Backwards)

* To know if GenAI is the good techno for a use case
  * can i add sufficient guardrails ?
  * can i break the problem in the sub tasks ?
  * Can i reuse or extend existing capabilities ?
  * What skill sets does my team have ?

### Discover

* Evaluate the your current cloud capabilities, prior to generative AI, to benchmark maturity. 
* Consult with operational leaders to identify any team constraints and upskilling opportunities.

### Build

* Define clear guidelines and processes for integrating Gen AI into your cloud environment. Ensure alignment with existing governance and compliance frameworks.
* Investing in Skills and Training
* Adapt Cloud Infrastructure to prepare for GenAI

### Deliver

* Develop a road-map for implementation steps of the new model.
* Measure your improvements against original desired outcomes. 
* Test and refine the model as your organization continues developing your generative AI capabilities.
  * regularly check model performance
  * define what to do on a foundation model upgrade

## Team Success

### People enablement

* Experts : [Generative AI Innovation Center](https://aws.amazon.com/ai/generative-ai/innovation-center/)à
* Data strategy
* Cloud infrastructure
* Security
  * Use cases oriented
    * Define Specific application use Cases (easier to control)
    * Guardrails on PPI
    * Human in the loop process to check outputs (once every week for ex.)
    * Tag/Identify confidential data
    * Scan the code (prompt attacks)
  * Infra oriented
    * Encryption at rest and in transit. Data and model
    * Data access (IAM), LakeFormation. Minimize access
      * blur/anonymize data used for training
    * Data lifecycle rules      
    * Audit/log the data that comes in and out
* Continuously evaluate and improve
  * data refresh
  * upgrades
  * testing, validation

### Governance

* Transparency
  * Tell when AI is being used, how it works, risks associated (Service Cards)
  * Transparency is also in audit trails. 
    * AWS AI services are all integrated with CloudTrail (Bedrock, Q for Developer, ...). 
    * Logs all intermediate steps when using Bedrock agents.
  * Ask for GenAI to display its sources
  * When building with SageMaker, use Clarify to explain the model. Use explainable algorithms
  * have a mechanism for humans to challenge decision made by AI
* Ethical principles
  * look for bias in model

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

