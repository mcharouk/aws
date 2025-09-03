# Model performance metrics

* Perplexity: how well the model predicts the next token
  * A lower perplexity indicates that the model is better at predicting the text and therefore has a better understanding of the language
* ROUGE : text summarization
  * ROUGE metrics measure the overlap between AI-generated text and human-created reference content
* BLEU : evaluates machine translation
* ROUGE and BLEU : Score from 0 to 1 where 1 is better.
* BERTSCORE : assessing the semantic similarity between two sentences. Uses word embedding to match similarity and has been created to overcome limitations of ROUGE and BLEU indicators.




* Used for classification
  * Accuracy : (TP + TN) / (TP+TN+FP+FN) -> total number of correct predictions 
  * Precision : TP / (TP + FP) -> to evaluate the number of false positives. 
    * How many of positive predictions were correct ? 
    * Evaluates how many non cats where classified as cats ? 
  * Recall : TP / (TP + FN) -> To evaluate the number of false negatives 
    * How many of positive predictions where identified by the model ?
    * Evaluates how many cats have been classified as non cats ? How many real cats have been missed ?
  * F1 score : evaluate classification or entity recognition. It calculates a good balance between Precision and Recall.
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

* These are techniques to try a set of hyper parameters to find the best combination

  * Random Search : try randomly in a range otf parameters
  * Grid Search : you define a grid (like a matrix) and all possible combinations will be tried. Very resource intensive and hard to make it scale when grid gets bigger.
  * Bayesian Optimization : Uses previous evaluations to optimize the hyper parameters. Requires fewer evaluations.

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

# Interpretability vs Explainability

Interpretability is to understand how the model works to be able to predict what it will output. It's something that can be used on simple models like decision trees. It's desirable but not always achievable.

Explainability is to understand why a prediction was made. We can understand how the input features can influence the outputs, without completely understand the algorithm of the model. It's something used for more complex models.

