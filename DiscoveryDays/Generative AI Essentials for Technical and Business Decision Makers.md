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





# GenAI Services

## Q for Business

* [Q Business Workflow](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/how-it-works.html#app-flow)
    * Managed chat application
    * Managed ingestion pipeline
    * Many connectors
    * Implement Guardrails
    * Implement responses fallback on plugins, or on LLM answers 

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