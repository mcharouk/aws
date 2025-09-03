# Module 1 : From LLM To Agents


# Module 2 : Exploring Agentic AI

# Module 3 : Understanding Agentic AI Workflows

## Worklow example

### Prompt chaining

Road Trip planning
* Step 1 : Take user preferences and suggest cities to visit
* Step 2 : Generate itinerary for each the cities
* Step 3 : Cost Estimation for each itinerary

### Parallelization

Based on user choice of cities, take these cities and execute in parallel planning for activities and accomodation

Example : 

Paris / Activities
Paris / Accomodations
Rome / Activities
Rome / Accomodations
etc...

Finally synthesize the results

### Routing

Some agents are specialized : 
- Flight Booking Agent
- Accomodation Agent
- Activity Agent
- Visa Information Agent

If the user asks "What are the best flights to Rome?", route to Flight Booking Agent.
If the user asks "Where should I stay in Paris?", route to Accommodation Agent.
If the user asks "What are some historical sites in Barcelona?", route to Activity Agent.
If the user asks "Do I need a visa to travel to Europe?", route to Visa Information Agent.

### Orchestration

A central manager agent orchestrate all the steps and adapt the steps to the user query

## Bedrock flows

Nodes can define 
* flow logic : iterator, condition, collector
* data handling
  * **prompts**
  * **agent**
  * **Knowledge base**
  * S3 Storage
  * S3 retrieval
  * **lambda**
  * **inline code** (python_3 only currently)
  * Lex 

# Module 4 : Introducing Autonomous Agents

## ReWOO

### Example of a ReWOO prompt

```
"You are a travel planning agent named "Wanderlust AI." Your goal is to create a detailed 3-day itinerary for a user who wants to visit Rome, Italy. The user has specified the following constraints:

Budget: $500 (USD) for all activities, food, and local transportation.
Interests: History, art, and food.
Accommodation: The user will handle their own accommodation separately.
Timeframe: 3 full days.

Use the ReWOO architecture to break down this complex task into smaller, manageable sub-tasks. For each sub-task, clearly state the Reasoning (R) behind the task, the Working Memory (W) you'll use (data structures, variables, external tools), the Output (O) you expect to generate, and how this output will be used in subsequent steps.

Specifically, demonstrate the following ReWOO steps:

Task Decomposition: Break down the overall goal into a series of smaller, sequential tasks.

Reasoning & Planning: For each task, explain why you're doing it and how it contributes to the overall goal.

Execution & Observation: Describe how you would execute each task (e.g., using a search engine, accessing a database, performing a calculation). Also, describe what you would observe from the execution (e.g., search results, database entries, calculation results).

Reflection & Adjustment: After each task, reflect on the results. Did the task achieve its intended purpose? If not, how will you adjust your strategy for the next task?

Iteration & Refinement: Show how the agent iterates through these steps, refining the itinerary based on the information gathered and the constraints provided.

Provide the final 3-day itinerary, including specific attractions, restaurants, and estimated costs. Also, summarize the ReWOO process you used and highlight any challenges you encountered and how you overcame them."
```

# Module 5 : Amazon Q and Agentic Development Tools

# Module 6 : Agentic AI with Amazon Bedrock

# Module 7 : Building DIY Solutions




