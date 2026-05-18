# Module 1 : From LLM To Agents

## Composition Fallacy

### 1. The "Unit Test" vs. "System Reliability" Trap
*   **The Assumption:** "I tested this prompt for summarizing text, and it works 99% of the time. I tested this other prompt for sentiment analysis, and it works 99% of the time. Therefore, my system that summarizes text *and then* analyzes the sentiment will be 99% reliable."
*   **The Reality:** Errors compound. If you chain five steps together, each with 99% accuracy, the total system accuracy drops to roughly 95% ($0.99^5$). If the individual steps are only 90% accurate, a five-step chain drops to 59% accuracy. The whole is significantly less reliable than the individual parts.

### 2. Context Drift and Pollution
*   **The Assumption:** "The model understands the context in Step 1 perfectly. It will maintain that understanding through Step 10."
*   **The Reality:** As an LLM moves through a workflow (e.g., a RAG pipeline or an agentic loop), it accumulates "noise." Minor misunderstandings or irrelevant details generated in Step 1 can become the primary focus by Step 3. The individual components work fine in isolation, but when composed, the context degrades, leading to hallucinations or logic failures later in the chain.

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


### Orchestrator

**The "Full Service" Travel Concierge**
The Orchestrator handles complex, multi-step requests where the output of one step determines the input of the next (managing dependencies and context).

**Input:** *"I have a total budget of $5,000 for a 10-day trip to Japan in May. Please plan the whole thing, but check if I need a visa first."*

**The Process:**
1.  **Analysis & Planning:** The Orchestrator analyzes the request and creates a plan. It recognizes that Hotels cannot be booked until Flight dates are confirmed, and nothing should happen if a Visa is impossible.
2.  **Step 1 (Conditional Check):** Call **Visa Information Agent**.
    *   *Logic:* If Visa is denied or takes too long -> **Stop and warn user.**
    *   *Else:* Proceed to Step 2.
3.  **Step 2 (Contextual Execution):** Call **Flight Booking Agent**.
    *   *Output:* Flights found for May 1st-10th. Cost: $1,500.
4.  **Step 3 (Dynamic Adaptation):** The Orchestrator calculates the *remaining* budget ($5,000 - $1,500 = $3,500).
    *   It calls the **Accommodation Agent** passing the *specific dates* found in Step 2 (May 1-10) and the *adjusted budget* ($3,500).
5.  **Synthesis:** Combine Visa status, Flight details, and Hotel options into a single comprehensive itinerary.

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

* ReWOO creates a DAG that describes the actions to take, it does not necessarily execute all tasks in parallel. 
* But the idea is to create the plan before taking action

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
## React vs Rewoo

* most of frameworks uses react because of its adaptation capabilities
* Still some frameworks let the developer choose between both
  * LangChain/LangGraph
  * LlamaIndex

## Multi Agent Collaboration

* Role based
  * Provide a specific role to an agent. Mimic the way humans are organized. It's the role that keep agent focus. The task itself could have some complexity
* Swarm approach
  * Role agnostic, but the task itself has a narrow scope. So even if the agent has no role, it can fullfill the task and not get lost  

### Hierarchical Pattern: "The Annual Report Generator"
**Scenario:** A bank needs to generate a comprehensive "Personal Financial Health Report" for a high-net-worth client.

**The Setup:**
*   **Structure:** Strict Top-Down delegation.
*   **Goal:** Produce a single, polished PDF report.

**The Workflow:**

1.  **Top Level: The Relationship Manager (Root)**
    *   *Goal:* "Create Q3 Report for Client X."
    *   *Action:* It splits the job into three distinct sections and assigns them to middle managers: **Income Analysis**, **Portfolio Performance**, and **Tax Estimation**.

2.  **Middle Level: The Section Leads**
    *   **Lead A (Income):** Receives "Analyze Income."
        *   *Action:* Spawns a *Transaction Classifier* to sort raw bank logs into "Salary" vs "Dividends."
    *   **Lead B (Portfolio):** Receives "Analyze Investments."
        *   *Action:* Spawns a *Stock Analyzer* (for equities) and a *Bond Analyzer* (for fixed income).
    *   **Lead C (Tax):** Receives "Estimate Taxes."
        *   *Action:* Waits for Lead A and Lead B to finish (dependencies), then spawns a *Compliance Checker* to apply current tax laws to those numbers.

3.  **Bottom Level: The Workers**
    *   *Transaction Classifier:* Reads raw CSV rows. Outputs: `Salary: $50k`.
    *   *Stock Analyzer:* Checks current market value. Outputs: `Stocks up 4%`.
    *   *Compliance Checker:* Calculates capital gains tax based on the stock growth.

4.  **The Roll-Up (Synthesis):**
    *   The Workers report back to the Section Leads.
    *   The Section Leads summarize their specific areas into paragraphs.
    *   The Relationship Manager compiles the three summaries into the final "Dear Client..." letter.
    *   

### Blackboard Pattern : "Forensic Fraud Detection"

**The Goal:** Detect if a specific series of transactions in a corporate account is fraudulent. No single agent has enough context to know for sure; they must build a case together on the Blackboard.

**The Blackboard State:**
Initially contains: `Transaction_ID: #9921, Amount: $450,000, Vendor: "Acme Corp", Time: 2:00 AM`.

---

#### Step 1: The Initial Hypothesis
**Agent A (The Profiler)** looks at the board.
*   *Observation:* It sees the time `2:00 AM` and the amount `$450,000`.
*   *Action:* It writes a hypothesis to the board:
    > **Hypothesis 1:** "Suspicious timing. Flagged as potential anomaly."
    > **Confidence:** Low (20%)

#### Step 2: Adding Context (The Collaboration Begins)
**Agent B (The Vendor Analyst)** looks at the board.
*   *Observation:* It sees `Vendor: "Acme Corp"` and **Hypothesis 1**.
*   *Reasoning:* "The Profiler thinks this is weird because of the time, but let me check the vendor."
*   *Action:* It checks a database and updates the board:
    > **Fact Added:** "Acme Corp is a registered shell company in the Cayman Islands with no physical address."
    > **Refinement of Hypothesis 1:** "Elevating risk. This isn't just an anomaly; it looks like money laundering."
    > **Confidence:** Medium (50%)

#### Step 3: The Counter-Argument (Crucial Step)
**Agent C (The Historical Matcher)** looks at the board.
*   *Observation:* It reads the updated hypothesis about "Money Laundering" and the vendor name.
*   *Reasoning:* "Wait, I've seen this pattern before. Let me check past approved transactions."
*   *Action:* It finds a match and **modifies** the hypothesis on the board:
    > **Fact Added:** "We have a pre-approved contract with Acme Corp for 'Emergency Server Migration' dated last year."
    > **Refinement of Hypothesis 1:** "Downgrading risk. The 2:00 AM timing matches the 'Emergency' nature of the contract."
    > **Confidence:** Low (10% fraud probability).

#### Step 4: The Final Twist (Synthesis)
**Agent D (The Payroll Cross-Referencer)** looks at the board.
*   *Observation:* It sees the "Emergency Contract" defense from Agent C.
*   *Reasoning:* "Okay, the contract exists. But who authorized the payment?"
*   *Action:* It checks the authorization signature against the HR database.
    > **Fact Added:** "The payment was authorized by User: J_DOE. However, J_DOE was fired 3 days ago."
    > **Final Hypothesis:** "FRAUD CONFIRMED. Valid contract used as cover by terminated employee."
    > **Confidence:** High (99%)

# Module 5 : Amazon Q and Agentic Development Tools

# Module 6 : Agentic AI with Amazon Bedrock

# Module 7 : Building DIY Solutions




