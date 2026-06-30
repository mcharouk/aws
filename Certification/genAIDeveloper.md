# Model training

- Lora (Low rank adaptation) is a lightweight method to fine tune a model
  - Freeze the Base Model: The billions of original parameters of the pre-trained base model are locked and kept completely untouched.
  - Inject Low-Rank Matrices: LoRA inserts a very small set of new, trainable adapter layers (mathematically structured as two smaller, low-rank matrices) alongside the original layers.
  - Train Only the Small Layers: During fine-tuning, only these tiny adapter layers learn from your custom data.
  - at inference time, the base layers and small layers are combined layer by layer to produce the final tuned output.

# RAG

## Chunking strategies

- Data granularity : not too small (loose context), not too large (create noise)
- Standard chunking: This method divides the document into equal-sized chunks, regardless of content. It’s simple and fast but may split sentences or concepts awkwardly:  Fixed size + overlap. Honor sentence boundaries.
- No chunking : it's good to specify when a custom split is done before ingestion. No chunking means one doc -> one chunk.
- Hierarchical chunking: Nested Parent/child. Initial chunks hits the child, but can get the parent to get more context.
  - small child chunks (high precision)
  - comprehensiveness from parents.
  - Parent chunk size : child chunk size, overlap
- Semantic chunking: Ensure each chunk contains semantically independent information. More expensive as must used an LLM for that.
  - Buffer size. The buffer the llm will get to do the analysis.
  - Breakpoint percentile threshold : how semantically similar a chunk must be 
- Recursive Chunking :  
  - Page level
  - Element levetl(chunk by sections, paragraphs...). Chunks split based on separator.
  - Word level

## Optimize embeddings

- embedding size means impact on the number of dimensions per vector.
- not too big, because more expensive. Too small, loose meaning.
- high dimension number is justified with the semantic complexity of the documents.
- cosine similarity : it's the math to calculate similarity between 2 vectors.

## Metadata
- You can add metadata to the embeddings, can help to filter, to rank, access control, data lineage, etc...

## Bedrock RAG Evaluation
* Criterias 
  - Correctness
  - Completeness
  - Helpfulness
  - Logical coherence
  - Faithfulness (how well responses aligns with the original text)
  - Citation precision and coverage
  - Harmfulness
  - Refusal (is it evasive when answering questions ?)
- Most provide a groundtruth set of answers, and prompt associated.
  - can provide also reference contexts.
- LLM as a judge

## Multi modal embedding

- in the vector DB, not only text, but also images, audio, video, etc...
- image must be encoded in base64 before providing it to the embedding model. This operation is not managed by Bedrock, so you need to do in a pre processing step.

## Bedrock Kownledge base specifics

- can have a vector store
- can connect to external systems (confluence, sharepoint, salesforce, S3, webcrawler, etc...)
- cross account access: Opensearch & Bedrock in different accounts: setup a remote inference connector, iam roles

## Bedrock Reranker models

* improve relevance of retrieved results to the original query
* order results accordingly
* Rerank operation in Bedrock API
* You can specify a reranker when hitting knowledge base
* Amason models or Cohere available in limited regions

# Token level redaction
- Redact sensitive information in the input text before sending it to the model, or before sending response to the end user.
- Launch lambda functions that filter based on regex or Named Entity Recognition (using AWS Comprehend for example).

# Json structured out of a prompt

* you can call a tool with the converse API

# Bedrock

## Bedrock Data Automation

- Extracts structured data from unstructured data : Documents, audio, video, images
- can be used for vector stores, just intelligent document processing, etc...
- Have to define a **blueprint** to specify the output. Managed blueprints exists
  - Basic fields
  - Transformed fields
  - Table fields
  - custom types (address type )
  - Can define blueprint from prompt
- pdf
  - split a pdf, to assign one blueprint by pdf page. allow multipage document processing
- output formats
  - For documents : json, json and additional files, csv, markdown, html
  - for images : generates summary, logos, text in image, content moderation... in JSON
  - for videos, same as images.
  - for audio, transcript, speaker and channel labelling,breakup in topics..in JSON
  
## Guardrails

* Bedrock guardrails can be integrated with any model, including sagemaker AI by calling its dedicated endpoint ApplyGuardrail
* [More info](https://aws.amazon.com/blogs/security/implementing-safety-guardrails-for-applications-using-amazon-sagemaker/)

# AWS ML Services

  * [Transcribe](./machinelearning.md#transcribe)
  * [Comprehend](./machinelearning.md#comprehend)

# Opensearch

## Index management

* Index state mgt policy
  * to move data from different tiers (Hot, UltraWarm, Cold storage)
  * to delete old data
  * move indices in readonly state
  * Reduce replica count over time
  * automate index snapshots
  * can run every 30-50 min. 
  * Can send notifications
* Index rollups
  * For timeseries. 
    * Summarize the data (for example, one second metrics to one hour metrics). 
    * Can remove fields
  * Periodic trigger  
* Index transforms
  * reshape the index into a new schema. Not tied to time series.
  * can aggregate logs for example to user centric rows.
  * create a different view of an index (aggregations for ex)
* Cross cluster replication for high availability. Basically looks like Aurora global databases or DynamoDB global tables, but it's active/passive.
* Remote reindex : just copy an index from a cluster to another on demand 

## Serverless

* no domains, only collections
* can be type search or time series
* OCU. Don't scale to 0. min 2 for indexing and 2 for searching

## Vector store
 
* Hybrid search : store keywords as metadata for keyword search
* top level engines
   * FAISS
   * NMSLib
   * Apache Lucene

### Search methods

* Exact Nearest neighbor : slow
* Approximate Nearest neighbor : good enough
  * HNSW : fast but use a lot of RAM. Not scale for huge datasets
  * IVF for huge datasets but will have more recall. Use less RAM
  * HNSW tuning available
     * M : (how many edges per node)
     * ef_construction : higher means more accurate but slower indexing
     * ef_search : higher means higher recall but slower search performance

### Performance

* Vector compression
  * Dense embeddings add up fast
  * Binary vectors (Faiss/Lucene)
  * Byte / 7-bit called **SQ** (Lucene)
  * FP16 (Faiss)
  * Vector compression consumes less RAM, accelerate queries, but the trade off are higher recall 
    * much higher operational complexity if using Product (PQ) -> Faiss

* Sharding strategies
  * semantic search : 30-50 GB per shard
  * smaller for hybrid : 10-30 GB per shard

* multi index approaches
  * tune each index on its own
  * different embedding models for different indices

* Hierarchical indices
  * top level index as a general / summary layer
  * routes to an index with more details
  * it's not an opensearch feature, has to do it by yourself.


### Operational convenience

* Neural plugin
   *  Don't have to send to it an embedding, it will manage it by itself. Just send text to it.

# Amazon S3 vectors

* 90% cheaper than opensearch
* Specify dimensions and distance metric
* Strongly consistent
* auto optimized over time (price/performance)
* actual performance : 100ms-1s
* infrequent queries
* integrate with opensearch to copy data from S3 to opensearch and back and forth.
* Possible to use opensearch and S3 vector as a backend.
* best practices
  * insert or delete in batches
  * use concurrent requests when not in batches.
  * have a retry mechanism because there is a throughput limit
  * can mark a metadata as non filterable

# RDS

* one pattern is to use RDS as RAG for metadata. RDS returns path that points to S3 buckets.

## Aurora

* pgvector extension to use Aurora as a vectorstore.

# DynamoDB

* mostly use to store long term memory of agents.

# Elasticache

* Valkey supports vector searches, as well as Redis
* MemoryDB -> Redis and Valkey
*


# Neptune

* As a vector database

# Amazon Kendra

* fully managed hybrid search (vector + keyword)
* means also less customizations that opensearch for example (no choice on embedding model, distance, algorithm to measure distance)


# Bedrock agents
  * use an alias to deploy it
  * On demand throughput or provisioned throughput (can increase throughput comparing to on-demand which is bound to account quotas)
  * Every agent has a default pre-processing prompt that you can enable. This is a lightweight prompt that uses a foundation model to determine if user input is safe to be processed.


## Bedrock agent tracing

* agent shows its reasoning process
* what tools did he executes, and the responses
* error details
* logs at multiple steps : preprocessing, orchestration, guardrails, errors, Post processing, rountingClassifier, etc...

 
# Strands

* AWS-specific integrations
  * include boto3 sdk
  * integration with bedrock (knowledge database)
  * Speak with Amazon Polly
* agnostic capabilities
  * run python code
  * shell scripts
  * read/write files
  * http call
  * ...custom tools

# AWS Agent squad

* It's a router agent
* it has a memory that keep trace of the conversation with the agents it calls
* Python and Typescript
* Integrates with Bedrock agents
* Can extend bedrock flows

# AWS AgentCore

* Observability that ties everything

## Agent runtime

* Serverless
* No ECS, EKS to manage but agentcore uses ECS behind the scene.
* Can customize with own docker images
* can deploy your agent on ECR.
* Can integrate with Bedrock agents
  * It consists of converting bedrock agents into strands code and deploy it on agent core.

## Identity

* with Cognito
* it's about the agent identity, and how they access external tools and aws services
* centralized repository, like user pool
* credential storage
* Oauth 2.0 support

## Memory

* Memory capability (short term and long term). Managed database
* Short term
  * Session objects that contain events
* Long term
  * extracted insights
  * Summaries of past sessions
  * Preferences, 
  * Facts you gave it in the past
  * you can define the strategies to specify what to store in long term memory

## Gateway
* Access between agent and external tools. Convert to MCP. 
  * OpenAPI
  * Smithy models (AWS specific)
  * lambda functions.

## Tools
* Browser tool
* Code interpreter tool

## Policy

* more control on what it can do or cannot do
* For example define 
  * how a tool can be called (with a specific role, specific OAuth 2 claims, specific tool arguments, etc...)
  * under what conditions (amount > 200 or whatever). Deterministic safeguards.
  * It's bind to the Gateway, so it works only if tool is accessible through it.
  * Deny by default, can explicitly deny
  * Mode to only log, and mode to enforce policies

## Evaluations

* how well agent perform tasks, handle edge cases
* Results in Cloudwatch
* can raise Alarms
* use cross region inference, so pay attention to compliance requirements.
* Evaluation criteria
  * correctness
  * conciseness
  * helpfulness
  * instruction following
  * faithfulness
  * etc...
  * can create custom evaluator
* can sample how much calls to assess
* It's a LLM that evaluates based on its prompt which is bind to the evaluation criteria. no labeled examples to compare with

# Amazon Q Business

* Data connectors for readonly data
* Plugins to connect to Jira, Servicenow, Zendesk, etc... 
  * Not only read actions, write too
* Can crawl ACL during ingestion too only select documents with appropriate permissions. Can also check permissions in real time to complete the selection at ingestion phase, but does not work on all sources.
* Q Apps
  * create an app with natural language
  * looks like PartyRock, but connected to enterprise data, can use Q business plugins...
  * can upload file, provide text inputs
  * can generate multiple outputs  

# Optimizations

## Token efficiency

* Bedrock has a countTokens API to measure
  * Count without actually run it
* Cloudwatch to monitor metrics
  * Token usage
  * Count, latency
  * Time to First Token
  * Errors

## Model selection

* route to a different model depending on query complexity
* Bedrock has a intelligent prompt routing feature
* Amazon Bedrock evaluations
  * measure foundation models performance agains your dataset
  * Human evaluation
    * uses Cognito User Pool to manage human task force
    * can use a work group from GroundTruth as well, but don't need to create a job in this service, just select the work group

## Resource utilization

* We canb batch embeddings or inference, instead of real time
* Provisioned throughput / Quota increase to overcome default quotas.

### Cache

* Cache requests
  * we cache an embedding vector
  * ask for requests similarity
  * upper to a threshold we return the cached response
  * can use Valkey, MemoryDB, Opensearch
  * **Prompt caching exists in Bedrock**
* In Bedrock we can cache **static information** by using checkpoints to not always embedding it
* You have to hit cache enough to have a good ROI, because writes are usually mpre expensive
* Edge Caching : Can use CloudFront too, but no GenAI, so it can work if queries are exactly the same.
* Deterministic Request Hashing : requests with minor variations, such as formatting differences, whitespace changes, altered parameter ordering, or punctuation shifts, still resolve to the same cache entry.
* Result Fingerprinting : generates a unique fingerprint of a model’s output, allowing the system to detect when future inference attempts would produce the same or nearly identical result

### Latency

* Bedrock Feature : Latency Optimized inference. Optimizes
  * Time to first token
  * output tokens per second
  * End to end latency
  * There is a more agressive quota for that feature. Fallback to Standard automatically.
  * no trade off regarding accuracy
  * Only available for a few models
  * Still beta in June 2026

### EC2 Ultraservers

* if not using Bedrock by hosting on EC2
* Tight interconnection (EFA at petabyte scale), high bandwidth, low latency
* Supported instances : Trn2 (Trainium), P6e-GB200 (Nvidia)

### Cross region inference

* more resiliency
* overcome capacity limits (quotas or peak usage in specific regions)
* doesn't work with provisioned throughput
* can select which regions to use or just make it global


# Sagemaker

## Import in Bedrock

* Use Custom Model Import and your model becomes serverless
* Inference Infrastructure
  * Deep Learning Containers using DJL (Deep Java Library)

## Adapter inference components

* LoRA can be used to fine tune a model
* adapter inference component
  * specify the base inference component : the FM that needs adaptation
  * LoRA adapter location in S3
* At invoke time, Sagemaker combines the adapter with the base model

## Model monitor

* possible to provide a custom ECR image to analyze monitoring drifts
  * helps to support other types of formats than tabular datasets (image, audio files, text data, ...)
  * can define custom criterias
* Makes it usable in generative ai model evaluation

## Training

* SageMaker training metrics can be used to push to cloudwatch (F1 Score for example...)
  * Sagemaker has a number of metrics available in SDK
  * by default, basic infra metrics are sent and basic training metrics
    * Training error
    * Prediction accuracy
    * Mean absolute error (MAE)
    * Algorithm-specific metrics
  * can define own metrics with sdk by specifying a regular expression that will be used to parse the logs.
  * use Sagemaker Debugger for enhanced monitoring.
* Can use Sagemaker serverless training instances to fine tune some FMs with common techniques : supervised learning, reinforcement learning


# Amazon Lex

* recognize intent, can trigger lambda function on that.
* is powered with genAI to recognize intent, but it's not a real AI agent. Not able to reason by itself, it's more determinisic. It follows some sort of state machine
* Lex could call Bedrock agent though with a Lambda.
* You define a bot with an intent (a specific goal to achieve)
  * sample utterances are sentences examples that match with the intent
  * Slots are the parameters of the function behind the intent.
    * Lex can ask for slots to user if they are missing. 
    * You can have custom slot types or built in slot types (date or city)
    * custom slot types can have synonyms, so called slot type values
  * Fullfillement describes the action it takes (call a lambda)
* runtime hints used to improve speech recognition for audio inputs.

# Glue

* it's possible to redact PII information with Glue but 
  * it should be used for structured and semi-structured data.
  * For unstructured data, use AWS Comprehend

# Model parameters

## Length control

* Response length
* stop sequences
* Penalties
  * Types
    * length
    * repeated tokens
    * frequency of tokens
    * type of tokens
  * For example, for length : As the response gets longer, the model reduces the probability of generating continuation tokens
  * it's not hard limit, it's something that influences softly the output
  * But this is available mostly on A21 labs models (Jurassic)