# Model performance metrics

* Perplexity: how well the model predicts the next token
* ROUGE : text summarization
* BLEU : evaluates machine translation
* BERTSCORE : assessing the semantic similarity between two sentences
* F1 score : evaluate classification or entity recognition



* Used for classification
  * Accuracy : (TP + TN) / (TP+TN+FP+FN) -> total number of correct predictions 
  * Precision : TP / (TP + FP) -> to evaluate the number of false positives
  * Recall : TP / (TP + FN) -> To evaluate the number of false negatives 
* Used for regression
  * Mean Absolute Error : difference between the current and predicted
  * Mean Absolute Percentage Error : difference between the current and predicted in percentage


# Model compression techniques

* Pruning : Removing redundant or less important parameters
* Quantization : Reduce the precision of model's weights, representing them with fewer bits -> smaller footprint and faster inference
* Distillation : train a smaller model that mimic a larger model

# Text processing

* n-gram
  * for example 3-gram takes all combinations of 3 words, 2 words and 1 word.

# Common hyperparameters

* Random Search
* Grid Search²
* Bayesian Optimization

# Bedrock

* To build a custom model (for example by fine tuning an existing model), purchasing provisioned throughput is mandatory to test and deploy the new model


# Model Explainability

| Shapley                                                             | Partial Dependence Plots                                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Quantify the contribution of each feature to a specific prediction  | Show the marginal effect of a feature on the predicted outcome across its entire range of values |
| explain individual predictions                                      | explain global model behavior                                                                    |
| often presented as bar charts but can be visualized in various ways | inherently visual                                                                                |


# Model types

* GAN (Generative Adversarial Network) : Image generation and manipulation, generate synthetic data
* CNN (Convolutional) : classify, recognize images
* RNN (Recurrent Neural Networks): Natural language processing



# Embeddings

* BERT is designed to capture the contextual meaning of words by looking at both the words that come before and after them (bidirectional context). 
* it creates dynamic word embeddings that change depending on the surrounding text, allowing it to understand the different meanings of the same word in various contexts. 