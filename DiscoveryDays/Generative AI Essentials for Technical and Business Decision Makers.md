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