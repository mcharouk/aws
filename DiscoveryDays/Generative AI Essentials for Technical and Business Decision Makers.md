# Technical Foundations

## Model

* Model store deeper and larger content that other ML models that are more specialized
* 2 constraints
  * Have sufficient quality training data
  * Have sufficient power calculation

## Transformers

* Easy to parallelize
* retain location of words, can bind a word to its context. Captures importance of each word in a sentence and relationship between words.
* **Position encoders** encode words position and can differentiate the meaning of a word based on its position in a sentence.

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

## Toxicity

* hate speech, biased statements, and any language that targets individuals or groups based on sensitive characteristics like race, gender, religion, or sexual orientation.
* it's not easy for an LLM sometimes to differentiate between unappropriate content and opinions.
* LLM can be manipulated with prompts or have biased that comes from the training data


## Hallucinations

User input: "When did Leonardo da Vinci paint the Mona Lisa?"
AI-generated response: "Leonardo da Vinci painted the Mona Lisa in 1815."
This is a hallucination because the Mona Lisa was actually painted in 1503-1506. The AI model has made a mistake because it is not trained on enough data about the Mona Lisa


## Plagiarism and cheating

* the issue is how it can be used by LLM users. For example, for education assignments, students can just copy/paste the content. Hard to detect that it came from an IA

## Disruption of the nature of work

* IA could change the way we work. Could make disappear some jobs and create some other jobs.

## Mitigations

* Bedrock guardrails can filter content provided by user or by LLM
  * can filter harmful content (hate, insults, sexual, violence, misconduct, prompt attack)
  * can provide topics that are denied. For example the LLM will not be able to reply to questions about security, finance, etc...
  * Sensitive information filtering (PII)
  * Word filters : provide a list of words or sentences that are denied
  * Grounding : Check response accuracy based on your entreprise data (RAG)

# GenAI Organization Overview

* People first approach : investment in technology + change of culture
  * Provide people the training and the resources to effectively use GenAI technology
  * Implements processes and governance
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
* Create a feedback loop to improve the product

* Make analogy with computer, smartphones, etc... It's an opprtunity to learn new tech, new ways of doing, but without losing every knowledge they have already acquired.


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