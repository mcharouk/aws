# Lab 1

* It's a very simple lab playing with bedrock playground simple prompt and chat feature. It should be quite straightforward

* For Task 2.1, make sure Nova Lite with On demand inference is selected. If not, there will be an error : 
 
> User ... is not authorized to perform: bedrock:InvokeModelWithResponseStream on resource: ...:**inference-profile**/.. because no identity-based policy allows the bedrock:InvokeModelWithResponseStream action

* If closing paragraph is missing, or more generally, if there's a missing part in the generated document, change **Maximum Output Tokens** value

# Lab 2

* it's a lab on guardrails. It tests
  * toxicity
  * denied topics
  * PII redacting
  * contextual grounding

* Be careful of always save and exit, when editing the draft version of guardrail

## Toxicity

* On toxicity, it should block the response, not the request. The reason is **violence**.
* note that the success of blocking action depends on the response returned by the LLM. It happened that it does not block

## GroundChecking

* the reference field didn't appear at start, i had to check and uncheck **Use ApplyGuardrail API** to make it appear
* in case groundchecking is not working, improve the grounding score threshold

