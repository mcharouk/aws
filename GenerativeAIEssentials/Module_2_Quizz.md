# Module 2 : Exploring GenAI Use Cases

## Quizz

### Question 1: Real Estate Pricing

* **Scenario**: A company wants to develop a system that can predict the price of a house based on its characteristics (size, number of bedrooms, location, etc.). The goal is to obtain the most accurate estimate possible to assist real estate agents.

* **Correct Answer**: Bad use case for Generative AI

* **Explanation**: This scenario is a classic example of predictive Machine Learning. The objective is to predict a numerical value (price) based on existing input data. Regression algorithms, which are part of classic Machine Learning, are perfectly suited for this task. Generative AI, on the other hand, is designed to create new data, not to predict precise values from existing data.

* **Good Use Case for Generative AI**: Generating attractive and personalized real estate descriptions.

* **Explanation**: Instead of predicting a price, Generative AI can be used to create persuasive textual content. For a property listing, you could provide a generative model with the key features of a house (size, number of rooms, architectural style, neighborhood, highlights like a view or garden) and ask it to generate multiple versions of catchy marketing descriptions. These descriptions could be tailored to different potential buyer types (families, young professionals, investors) by adjusting the tone and emphasis. Generative AI here creates original and engaging text, rather than predicting a numerical value.


### Question 2: Advertising Image Creation

* **Scenario**: An advertising agency wants to quickly create multiple variations of an ad image to test different visual hooks and target various customer segments. They want to generate original images based on text descriptions.

* **Correct Answer**: Good use case for Generative AI

* **Explanation**: Generating original images from text descriptions (text-to-image) is a core capability of Generative AI. This allows for the creation of new and varied content, ideal for marketing campaigns where experimentation and visual personalization are key.

### Question 3: Fraud Detection

* **Scenario**: A bank wants to automate the process of detecting fraudulent credit card transactions. The system must analyze millions of daily transactions and identify those with a high risk of fraud, based on past behavioral patterns.

* **Correct Answer**: Bad use case for Generative AI

* **Explanation**: Fraud detection is a problem of classification and anomaly detection, which falls under classic Machine Learning. The goal is to identify specific patterns in existing data to distinguish legitimate transactions from fraudulent ones. Generative AI would not be the most appropriate tool for this precise classification task based on established rules.

* **Good Use Case for Generative AI**: Generating synthetic data for training fraud detection models.
* **Explanation**: Fraud detection models require a lot of data, including examples of fraudulent transactions, which are often scarce. Generative AI can be used to create realistic synthetic transaction data, including examples of fraud that resemble real-world fraud but are artificially generated. This synthetic data can then be used to augment the training datasets for classic Machine Learning fraud detection models, improving their ability to detect fraud, even novel types they haven't encountered before. Generative AI here creates artificial data to enhance another ML process, rather than performing the detection itself.

### Question 4: Game Dialogue Generation

* **Scenario**: A video game publisher wants to create realistic and varied dialogues for non-player characters (NPCs) in a new role-playing game. The goal is for each NPC to react uniquely to the player's actions and the environment, generating dynamic and contextual conversations.

* **Correct Answer**: Good use case for Generative AI

* **Explanation**: Generating creative and contextual text, such as game dialogues, is a flagship application of Generative AI (especially Large Language Models - LLMs). These models can understand context, tone, and generate coherent and original responses, making the gaming experience more immersive.

### Question 5: Delivery Route Optimization

* **Scenario**: A logistics company wants to optimize its delivery truck routes to minimize travel time and fuel consumption. The system must calculate the most efficient path, considering numerous variables (traffic, time constraints, vehicle capacity).

* **Correct Answer**: Bad use case for Generative AI

* **Explanation**: Route optimization is a classic operations research and algorithmic problem, often solved by Machine Learning techniques (like reinforcement learning for dynamic scenarios) or classic optimization algorithms (like the shortest path algorithm). Generative AI is not designed to solve deterministic optimization problems or those based on strict constraints of this nature.

* **Good Use Case for Generative AI** : Generating problem scenarios for logistics training or brainstorming.
* **Explanation**: In logistics, there are numerous complex and unforeseen issues. Generative AI could be used to create varied and realistic case studies or descriptions of logistical challenges. For example, it could generate scenarios describing situations like:
  * "A customer requests a last-minute delivery change due to an address modification."
  * "Several trucks are blocked in an area following an unforeseen event."
  * "New regulations impose traffic restrictions in certain zones at specific times." 
 
These descriptions could be used to train new employees, stimulate brainstorming sessions for innovative solutions, or test the responsiveness of operational teams. Generative AI here creates textual content describing complex situations, rather than directly solving the optimization problem.