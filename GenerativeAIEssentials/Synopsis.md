# Module 1 : Introducing Generative AI

## AWS Models

* Titan : usually solid for business case, but not as performant as mainstream models (ChatGPT, Gemini, Anthropic). It's in Tier 2 models
* Nova : Strong on multimodal, comparable to mainstream models
* AWS models usually have very good cost-to-performance ratio
* Also some features can be restricted to some models 
  * fine-tuning and continued pre-training (Titan, Anthropic, Llama, Nova)
  * Embeddings on KDB (Amazon Titan & Cohere only)
* Usually AWS models are better supp# Module 2 : Use cases


# Module 2 : Exploring Generative AI use cases

## Use cases 

* New Content (more about creating standard formats, not really innovation)
  * Writing product descriptions for e-commerce
  * Generating social media posts
  * Creating email marketing campaigns
* Innovation
  * Using GenAI to propose new research hypotheses or experimental approaches
  * Generating novel product concepts or design variations that haven't been tried before
* Efficiency
  * synthesize case law, regulations, and precedents to help lawyers prepare more efficiently for cases
  * analyze production line data, equipment performance, and quality metrics to optimize machine maintenance schedules and reduce downtime (task about planning and scheduling)
  * review loan documentation for completeness and consistency before human underwriters review them, reducing processing time and errors

## Amazon Pharmacy

* [Amazon Pharmacy](https://www.aboutamazon.com/news/retail/how-amazon-pharmacy-uses-generative-ai)
* Convert prescription (handwritten or digital) to structured data
  * Help pharamcist to validate the prescription. 
  * Processing speed increased by 90%
   
# Module 3 : Essentials of Prompt Engineering

## Tool use vs action-oriented prompting

### Tool-use

* Use GenAI to call a tool. 
* It's not agent because genAI is still not goal oriented. Agent make a plan, can analyse the results, can make multiple iteration before the final results. Calling a tool is much more straightforward.
* [Example on Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html)
  * During Bedrock response, it reply to backend specifying the tool to use with input parameters. 
  * The back end call the tool
  * Bedrock includes the tool response and generate the final repsonse to the user

### Action-oriented

* provide an actionable insights
  * some python code
  * some plan to execute manually

## Complete Prompt example

As a **senior marketing consultant** <span style="color:red">[ROLE]</span> specializing in **cloud technology adoption** <span style="color:red">[TOPIC</span>], create a **strategic recommendation report** <span style="color:red">[OUTPUT]</span> for **C-suite executives** <span style="color:red">[AUDIENCE]</span> analyzing our company's potential migration to AWS cloud services. Base your analysis on the **attached quarterly IT infrastructure assessment document** <span style="color:red">[DOCUMENT]</span>.

Structure your response with **an executive summary, current state analysis, AWS migration benefits, implementation roadmap, and risk assessment** <span style="color:red">[STRUCTURE]</span>. Limit your report to exactly **800 words** <span style="color:red">[LENGTH]</span> and format it as a **formal business document with numbered sections and bullet points** <span style="color:red">[FORMAT]</span>.

**Do not include specific pricing details, technical implementation steps, or competitor comparisons** <span style="color:red">[EXCLUSIONS]</span>. **Focus your recommendations within the scope of Infrastructure-as-a-Service solutions only, avoiding Platform-as-a-Service or Software-as-a-Service discussions** <span style="color:red">[BOUNDARIES]</span>.

For reference, here's the type of insight I'm looking for: **'AWS EC2 instances could reduce our current server costs by 30% while improving scalability for peak shopping seasons'** <span style="color:red">[EXAMPLES]</span>

## CoT & ToT

* two methods that can be implemented in a single prompt or in multiple prompt. 
* usually more effective on multiple prompts on complex problems

### Example

```
Our e-commerce company has a 25% customer churn rate. I need to systematically explore 
different business strategies to reduce this to 15% within 6 months. Let me think through 
this using multiple strategic approaches.

* THOUGHT TREE LEVEL 1: Primary Strategic Directions
* Branch A: Improve Customer Experience
* Branch B: Enhance Product/Service Value
* Branch C: Implement Retention Programs
* Branch D: Optimize Pricing Strategy

For each branch, I'll evaluate:
1. Implementation timeline (must fit 6-month window)
2. Expected impact on churn reduction
3. Required investment
4. Risk level
5. Measurability

Let me explore each branch systematically...
```

## Output refinement techniques

* Ask AI to filter some part of this reponse based on : 
  * some parts or section that could be excluded 
  * Similarity with predefined subject
  * Ask AI to rate the response in terms of quality, confidence and ask AI to filter response below a threshold.

* Filtering
```
Filter these recommendations and keep only those that:
    1. Directly address the stated requirements
    2. Are feasible for the user's context
    3. Have clear business value
    
    Remove any generic or irrelevant suggestions.
    Return only the filtered list with brief justification for each
```

* Threshold

```
 Analyze these AWS cost optimization opportunities and rate each by:
    - Confidence level (1-10)
    - Potential savings (1-10) 
    - Implementation difficulty (1-10)
    
    Only include recommendations with:
    - Confidence ≥ 7
    - Potential savings ≥ 6
    - Implementation difficulty ≤ 7
```

* Similarity

```
Remove duplicate or overly similar recommendations from this list:
    
    1. Use Amazon RDS for managed database
    2. Consider Aurora for managed database  
    3. Implement RDS for database management
    4. Use Lambda for serverless computing
    5. Consider Step Functions for workflow orchestration
    6. Use EC2 for virtual machines
    
    Keep the most comprehensive and specific recommendation from each group.
```

* Ranking 

```

Business Context: {business_context}
    
    Rank these AWS migration strategies from best to worst fit:
    
    A) Lift-and-shift to EC2 instances
    B) Refactor to serverless (Lambda + DynamoDB)
    C) Containerize with EKS
    D) Hybrid cloud with AWS Outposts
    E) Full modernization with microservices
    
    Provide ranking with detailed justification for each position.

```

* Summarization :
  * Extractive : provide sentences as is in the original document
  * Abstractive : reformulate sentences by keeping the essence of original input

* Post-processing
  * GenAI as a censor
    * Fact-Checking
    * Content-moderation


## Prompt engineering model differences

* Here are some [links](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-engineering-guidelines.html) on prompt guidelines provided by each FM provider
* Note that there can be model specificities to provide elements
  * For Anthropic, use XML tags

```
Your task is to fix the product description to be compliant with the product guidance.
Original product description: <originalProductDescription>{Product Description}</originalProductDescription>
Product Guidance: <productGuidance>{Product Guidance}</productGuidance>
Your product description: <productDescription>{Product Description}</productDescription>
```

  * For AI21 Labs it's more like that

```
Your task is to fix the product description to be compliant with the product guidance.
Original product description: {Original Product Description} – End of Description –
Product Guidance: {Product Guidance} – End of Description –
Your product description:
{Product Description}
 – End of Description –
```

## Model parameters

* Temperature
  * a high temperature flatten the distribution
  * a low temperature add some constrasts to the probabilities

![Temperature Example](/GenerativeAIEssentials/TemperatureIllustration.png "Temperature Example")

* A model typically don't always take the highest probability. 
* Top P : take all next tokens until some of probability reaches P.
* Top K : take K next tokens with decreasing prob
* Even when Top P = 0 and Temp = 0.
  *  if prob are equals, it can take different outputs.
  *  sometime model when temp = 0, they set temp to a very low temp but avoid zero for division (for example, they will take 0.0001)


# Module 4 : Reponsible AI principles and considerations

## Solutions for transparent and explainable models

### Explainability frameworks

* SHAP : supported by Clarify. 
  * Can sample the input tokens to get only the most relevant. Can sample more important paragraphs, or more important sentences in a paragraph.
  * for outputs, focus on only on specific sentences, if the output is too long (must select it manually)

* Attention maps show which input tokens the model "looked at" when generating each output token. Think of it as the model's "focus pattern."
  * more scalable
  * available on open source models, that are self-managed. Not available on models as a service.
  * Frameworks
    * Transformers + BertViz (HuggingFace)
    * Captum (Facebook)

### Transparent Documentation

* [Rekognition Example Model card](https://docs.aws.amazon.com/ai/responsible-ai/rekognition-face-matching/overview.html#design)

* Model card content
  * Intended use cases and limitations
  * Explain how it works
  * Performance expectations
  * Test Methodology
  * What has been done on fairness and bias, Robustness, Privacy and security 

* With Sagemaker model cards, Can create and access model cards in json and export it in PDF 

### Monitoring and Auditing

* Audit and keep trace of all interactions
* Monitor drift

### Human Oversight and Involvement

* If an human review and validates, it adds explainability to the system for high stake decisions
* AI flags potentially harmful content for review
* AI suggests but humans validate at the end
* Send a sample of live data for human review

### Counterfactual Explanations

* it consists of AI providing explanation of results. 
* Basically, it will say in which scenario the result could have been different.
* some frameworks : 
  * [Dice](https://www.microsoft.com/en-us/research/project/dice/)
  * [Alibi Explain](https://github.com/SeldonIO/alibi)

### User Interface Explanations

* For example, quote the sources it used to generate the response
* Chain of Thought prompting
* confidence score

## Bias

### Algorithm bias

* Scenario : A company uses AI to analyze profile photos for "professionalism" scoring. The training data is perfectly balanced - equal photos of successful employees across all demographics, all labeled as "professional."

* The algorithm's **mathematical structure** itself creates bias:
  * The CNN's **pooling layers** systematically reduce image resolution
  * This affects darker skin tones differently than lighter ones due to **pixel intensity calculations**
  * The algorithm's **ReLU activation functions** respond differently to various lighting conditions
  * **Gradient descent optimization** converges on patterns that favor certain facial structures

* Result
  * The **loss function mathematics** may inadvertently optimize for features that correlate with certain demographics

### Interaction Bias

* Scenario: An e-commerce company deploys an Amazon Lex chatbot for customer support.

* The Problem:

During initial deployment, primarily tech-savvy early adopters interact with the bot
These users ask more complex questions and provide feedback in technical language
The bot learns to respond better to technical queries but poorly to simple, everyday language

* Real Impact: Elderly customers or those less comfortable with technology receive inadequate support, creating a digital divide.

### Bias Amplification

* Scenario: A streaming service uses Amazon Personalize for content recommendations.

* The Problem:
  
Historical viewing data shows gender stereotypes (men watch action, women watch romance)
The recommendation engine amplifies these patterns
Creates a feedback loop where users are only shown stereotype-confirming content

* Real Impact:
  * Women interested in sci-fi never see those recommendations
  * Men interested in cooking shows don't get those suggestions
  * Reinforces and strengthens societal stereotypes

## Transparency and explainability

* LLM are in general not transparent because of their complexity    
* But be careful to who you are transparent. It can divulgate sensitive data, model internal behaviour (subject to disclosure), could show some of its vulnerabilities
* Might not be 100% explainable. Does not explain why genAI has generated this text instead of  another one. 

* Some ideas to alleviate
  * explain the results by anonymizing, or giving amounts in a range for ex.
  * have tiered explanations that depends on the user habilitations.
  * use model-agnostic explanations like SHAP
  * combine transparent models with complex ones

### Transparency trade offs

* Accuracy : More complex models are more accurate and less transparent
* Privacy : transparency could reveal confidential data.
* Safety : guardrails typically block responses. As the user didn't receive the response, he cannot understand why the response have been blocked
* Security : reveal the internals of the model

## AWS Services

* Sagemaker
  * Clarify
  * Monitor
  * Sagemaker Model cards
  * Sagemaker Lineage Tracking
* Bedrock
  * Guardrails
  * Model evaluation
    * LLM as a Judge
    * Automatic : classical indicators
    * Human review


### Sagemaker Clarify Evaluation Framework

* used for 
    * safety : toxicity, bias
    * fairness
    * robustness and veracity

* Model evaluation
   * [fmeval](https://github.com/aws/fmeval) is open source and is used by SageMaker Clarify under the hood
   * can work with any model
   * Evaluated Tasks
     * Open Ended generation
     * Summarization
     * Question-Answering
     * Classification
   * Evaluation dimensions
     * Factual knowledge
     * Robustness
     * Prompt stereotyping (biases / fairness)
     * Toxicity
     * Accuracy (for summarization, classification and question answering)
* Clarify has features to evaluate dataset fairness 


# Module 5 : Security and Compliance

## OWASP Top 10

### 1 - Prompt injection

* Mitigation
  * Provide specific instructions about the model’s role, capabilities, and limitations within the system prompt. 
  * Enforce strict context adherence, limit responses to specific tasks or topics, and instruct the model to ignore attempts to modify core instructions
  * Can use Bedrock guardarails

### 2-Improper Output Handling

* no sanitization or validation of LLM output
* can result in XSS and CSRF in web browsers
* Example
  * LLM output is entered directly into a system shell or similar function such as exec or eval, resulting in remote code execution
  * JavaScript or Markdown is generated by the LLM and returned to a user. The code is then interpreted by the browser, resulting in XSS

### 3-Data and model poisoning

* at different stages : pretraining, fine tuning or embeddings
* compromise model security, performance or ethical behavior
* Mitigation
  * Input sanitization
  * Access controls

### 4-Model denial of service

* Mitigation
  * Implement input validation and sanitization to ensure user input adheres to defined limits and filters out any malicious content
  * Enforce API rate limits to restrict the number of requests an individual user or IP address can make within a specific timeframe
  * Limit the number of queued actions and the number of total actions in a system reacting to LLM responses

### 5-Supply Chain 

* consists or exposing a poisoned LLM or LLM vendor has its LLM on a poisoned infrastructure. 
* Example
  * Pypi had a security breach on Pytorch library that led to poisoned model
  * exposing a poisoned model bypassing Hugging Face safety features 
  * An attacker finetunes a popular open access model to remove key safety features and perform high in a specific domain (insurance)
* Mitigation
  * careful about the LLM vendor
  * Apply comprehensive AI Red Teaming and Evaluations when selecting a third party model
  * SBOM if you host the model

### 6-Sensitive Information Disclosure

* LLM outputs reveals PII or other confidential data
* Mitigation
  * Output sanitization
  * Input validation on training data
  * Enforce access controls on downstream services

### 7-Insecure plugin design

* plugins are likely to implement free-text inputs from the model with no validation or type checking. This allows a potential attacker to construct a malicious request to the plugin.
* Example
  * A plugin accepts a base URL and instructs the LLM to combine the URL with a query to obtain weather forecasts which are included in handling the user request. A malicious user can craft a request such that the URL points to a domain they control, which allows them to inject their own content into the LLM system via their domain
  * A plugin accepts SQL WHERE clauses as advanced filters, which are then appended to the filtering SQL. This allows an attacker to stage a SQL attack
* Mitigation
  * should enforce strict parameterized input wherever possible and include type and range checks on inputs

### 8-Excessive Agency

  * Vulnerability that enables damaging actions to be performed in response to unexpected, ambiguous or manipulated outputs from an LLM 
    * excessive functionality
    * excessive permissions
    * excessive autonomy
  * Mitigation
    * Minimize functionality, permissions and autonomy
    * avoid open ended extensions
    * execute extensions in user context
  
### 9-Overreliance

*  LLM produces erroneous information and provides it in an authoritative manner
*  Example
   *  A news organization heavily uses an LLM to generate news articles. A malicious actor exploits this over-reliance, feeding the LLM misleading information, and causing the spread of disinformation.
   * The AI unintentionally plagiarizes content, leading to copyright issues and decreased trust in the organization
 * Mitigation
   * Regularly monitor and review the LLM outputs
   * Cross-check the LLM output with trusted external sources (ground checking)
   * Enhance the model with fine-tuning or embeddings to improve output quality
   * Break down complex tasks into manageable subtasks and assign them to different agents. This not only helps in managing complexity, but it also reduces the chances of hallucinations as each agent can be held accountable for a smaller task

### 10-Model theft

* proprietary LLM models (being valuable intellectual property), are compromised, physically stolen, copied or weights and parameters are extracted to create a functional equivalent
* Example
 * an attacker gained access on a central repository
 * An attacker queries the API with carefully selected inputs and collects sufficient number of outputs to create a shadow model
* Mitigation
 * Centralized repository to simplify access controls
 * least privilege access
 * Quota on LLM calls

## Prompt attacks

* Prompt injection
  * try to overwrite original instructions
  * attack vector : Technical instruction manipulation
  * Primary Weakness Exploited : Input validation gaps
  * risk level : Data breach, system compromise
* Jailbreaking
  * try to bypass ethical constraints
  * attack vector : Creative prompt crafting
  * Primary Weakness Exploited : Safety boundary limitations
  * risk level : Policy violations, harmful content
* Social Engineering
  * Manipulate through deception (manipuler par la tromperie)
  * attack vector : Psychological manipulation tactics
  * Primary Weakness Exploited : AI's tendency to be helpful and human-like
  * risk level : Information disclosure, fraud enablement

## AWS Services

### IAM

* for data access
* for model access
* for model training
* eventually on tools used by genAI
* genAI applications can access only specific models
  
### KMS

* mainly for model and data encryption
* can be used to encrypt data before sending it (client side encryption)


### Cloudwatch

* prebuilt dashboards for Model Invocation (not exhaustive)
  * invocation count
  * invocation latency
  * Token Counts by Model
  * Invocation Throttles
  * invocation error count
* prebuilt dashboards for agents as well (Agentcore)

### Audit manager

* provides long term evidence
* historical proof of compliance
* audit documentation

* It collects proof of remediation with cloudtrail
* It collects config snapshots that prove long term compliance
* It collects config that confirm ongoing monitoring (SecurityHub config)

* There is a framework called [AWS Generative AI Best Practices](https://docs.aws.amazon.com/audit-manager/latest/userguide/aws-generative-ai-best-practices.html)
* Supports a lot of standard frameworks : HIPAA, NIST, CPI, GDPR

### Security Hub

* Security-oriented
* Meant not for Real-time alerts, Security Remediation, Current Compliance
* Support some official frameworks.


# Module 6 : Implementing Generative AI projects

## Use case

* Use [this problem statement](Module_6_ProblemStatement_Example.md)

## Models

* Finance
  * [FinGPT](https://github.com/AI4Finance-Foundation/FinGPT)
  * [BloombergGPT](https://www.bloomberg.com/company/press/bloomberggpt-50-billion-parameter-llm-tuned-finance/)
  * [Financial-BERT](https://wandb.ai/ahmedrachid/FinancialBERT-Language-Model/reports/Financial-BERT--VmlldzoxMzQwMTgy)
* HealthCare
  * [Med-Gemini](https://research.google/blog/advancing-medical-ai-with-med-gemini/)
  * [Bio-GPT](https://github.com/microsoft/BioGPT)
  * [PMC-Llama](https://github.com/chaoyi-wu/PMC-LLaMA)
* Note that AWS has some services dedicated to health care like HealthScribe and Comprehend Medical, but does not offer specialized FMs, though it's possible to build them on Bedrock or Sagemaker.
* HealthScribe is a GenAI powered model
  * It listens to a patient-clinician conversation, transcribes it, identifies medical terms, and then summarizes the dialogue into clinical notes

## Benchmark

* SQUAD : evaluate question answers
* GLUE : evaluate language comprehension
  * sentiment analysis
  * text classification
  * Named Entity Recognition
  * Text Similarity
  * Question Answering
* SuperGlue : evaluate complex reasoning

## Model evaluation metrics

Let's say you want to rekognize a cat in an image : 

* Precision : take account of image misclassified as a cat (False positive)
* Recall : take account of a cat image not classified as a cat
* Accuracy : take account of both precision and recall
* F1 score : take account of both precision and recall but privilege models that balance both.

* These metrics could be used for genAI classification tasks and question/answers (for example classified as 1 if the answer is correct)

## Measurements standards

| Metric    | Focus            | Strength               | Limitation                   |
| --------- | ---------------- | ---------------------- | ---------------------------- |
| ROUGE     | Recall           | Good for summarization | Misses paraphrasing          |
| BLEU      | Precision        | Good for translation   | Penalizes valid alternatives |
| BERTScore | Semantic meaning | Captures paraphrasing  | Computationally expensive    |


## Drift

* note there is no easy way to detect drift with generative AI on AWS
  * activate logging on conversations
  * Track customer satisfaction, escalation rates
  * with Comprehend
    * calculate sentiment analysis with Comprehend
    * check that answer is related to the same topic than the question 
  * manual review of some conversations
* Model monitor is good to monitor drift on structured metric. So it might be useful if genAI is used as a classification task or it's possible to convert the response into some metric.
* There are third party tools that can do these kind of drifts 
  * Arize AI
  * Superwise AI
  * Fiddler AI Observability
  

### Data drift example

* Training Data (2023)
  * 70% purchases were physical products (electronics, books, clothing)
  * 20% digital products (software, e-books)
  * 10% services (warranties, subscriptions)
  * Average customer age: 35-45
  * Peak shopping: weekends and evenings

* Production Data (2024) - Data Drift Occurs
  * 40% purchases are now physical products
  * 35% digital products (AI tools, streaming services)
  * 25% services (cloud storage, AI subscriptions)
  * Average customer age: 25-35 (younger demographic)
  * Peak shopping: mobile during lunch breaks and commutes

* this can be a sign of recommendations becomes less pertinent, customer satisfaction decreases

# Bedrock pricing

* Different Tiers for serverless
  * Priority Tier
    * mission-critical applications
    * preferential compute allocation
    * 25% up output tokens per second latency compared to Standard
  * Standard Tier
    * consistent performance at regular rates for everyday AI tasks
  * Flex Tier
    * non-urgent AI workloads
  * Don't forget batch
* Provisioned throughput
  * allows you to reserve a certain amount of processing power for your application to avoid throttling and ensure consistent performance
  * not all models are eligible
  * you pay for an amount of MU (Model Units) that refers to a portion of compute
  * portion of compute associated to MU depends on the model, contact TAM to know about them
  * billed hourly, can take a commitment 1 yr or 3 yr (optional)