# Encoding techniques

* Label encoding
* One hot encoding
* Target encoding : replaces a feature's categories with some number derived from the target. 
  * For exemple , for a group of item replace a number by the mean of the group.

# Feature engineering

* Numeric
  * Normalization : rescale the values to a range between 0 and 1. 0 corresponds to the min value,and 1 to the max
  * Standardization : rescale feature so that mean is 0 and standard deviation (ecart type) is 1
  * Binning : regroup some categories in macro categories to lower the noise. For example numeric values can be classified in ranges
  * Log transformation : apply the logarithmic function to the values. It scales down the large outlier values
* Text features
  * bag of words : count occurences of each word. Can be used for sentiment analysis but lack of precision because if we count the word great for example, we don't know to what it refers
  * n-gram : take all combinations of n words that follow each other.
  * temporal data : create new features for example to know if it is a week end, take the day of week, of the hour, etc..
* Feature selection
  * split features
  * combine features
  * PCA : used for dimensionality reduction. It retain most of the original variations but reduce the number of features. PCA can be applied to a set of feature.

# Data labeling

* Mechnical Turk
  *  delegate tasks to workers. This can be about ML but not necessarily.
  *  Quality must be monitored by the client.
*  Groundtruth
   *  specific to ML labelling tasks
   *  integrated with Sagemaker
   *  With groundTruth Plus : active learning / poor performers removal / label automatic refining / validation and monitoring of DQ 
   *  can delegate tasks to employees instead of mech turk workforce

# Dataset balancing

To remediate unbalanced dataset : 
    * Numeric data
      * Oversampling
        * Random sampling : consists duplicating minority dataset
        * SMOTE : interpolates new data from existing data
    * Text data
      * Resampling
      * Synthetic data generation (create new data from scratch)
    * Image data
      * Data augmentation : create synthetic data from real data with ML algo like GAN (Generative Adversarial Network)

# Dataset splitting

* Simple hold-out : selecting 80% for training, 10/% for tests, 10%  for validation
* K-fold cross validation
  * split k times the dataset, to take each time a different sample for training and validating.
  * It provides an estimate of how well a modeling approach will generalize
    * using performance metrics (average accuracy)
    * using variance across the K folds. A high variance can indicate the model is sensitive to the specific training dataset. It can indicate overfitting.
  * You use this estimate to select the best approach (algorithm, hyperparameters).
  * You then train a single, final model on the entire dataset using the chosen approach. This is the model you deploy.

* A good practice is to shuffle the data before selecting it to ensure randomness on data selection.

# Model tuning

* Loss function is the function used to evaluate the prediction qualities. It help adjust the hyper parameters of the model.
  * for regression : root mean square error
  * for classification : log-likelihood loss
* Optimization technique refers to the path it takes to reach for the global minimum, means the set of hyper parameters that gives the better results.
  * gradient descent : compute intensive but best technique to find the global minimum
  * stochastic gradient descent : only take one data point to find the global minimum. This can lead to inaccurate results but cheap
  * mini batch gradient descent : hybrid solution. Takes a subset of data points to determine the global minimum.


# Sagemaker

## Compute options

* use sagemaker prebuilt algorithm (use image provided with prebuild algorithm)
* use sagemaker framework containers
* extend sagemaker framework containers
* BYOC
* Market place


## Managed instances

* family good for deep learning inference : inf1 (inferentia), g5
* family good for deep learning training : p3, p4d, dl1, tr1 (trainium)
* for other ml : take m, c or m family
* take GPU for massive datasets or for deep learning

## Model selection

* Reinforcement Learning : support MxNet and TensorFlow

## Model training

### script mode

* provide a train.py file with 3 functions
  * input_fn : preprocessing
  * model_fn : model definition
  * train_fn : 
    * implement the training loop, which iterates over the training data
    * computes the loss
    * updates the model parameters
    * evaluates the model on the validation data

* create an estimator object
  * provide training script, instance type, hyperparameters
  * call fit method with the training and validation data

* Sagemaker will get the image, deploy it on a managed infrastructure, upload the script on the instance, execute the script, donwload the files (pipe mode, file mode, etc...)


### Overfitting remediation

* Early stopping
* Pruning
  * remove features that doesn't contribute a lot to the output. It lower the noise
  * Regularization
    * dropout
      * specific to neural networks. 
      * Randomly drops out, or sets to zero, a number of neurons in each layer of the neural network during each epoch
      * forces the network to not overemphasize specific neurons and develop multiple methods of arriving at a result.
    * L1 : Reduces the number of features that impact the training of the model. Instead of removing the features themselves, you use L1 regularization to push the weights of less important features to zero
    * L2 : results in smaller overall weight values and stabilizes the weights when there is high correlation between the input features
  * Data augmentation : generate new synthetic data to increase the diversity of the training data
  * Model architecture simplification : take a simpler model or change hyperparameters to simplify the model


### Scaling model training

* Early stopping
  * after each epoch of the training job, specify an objective metric
  * calculate the median of the objective metric among all the epochs
  * stop the job if objective metric is lower than the the median
* Distributed training
  * Data parallelism
    * each node gets a copy of the model
    * the weights of the model are update with each training data in a distributed way
    * at the end, resulting gradients are aggregated across devices before updating the model weights
* Model parallelism
  * split the model on multiple instances if the model does not fit on a single instance.
  * each part of the model is trained in a distributed way. It's possible also that this sub part is trained in a distributed way by using data parallelism
  * at the end all the weights are aggegated in a single model
  * Overhead on communication, load balancing (workload well distributed on all the nodes, complex model architecture...)


# Model Tuning

## Model Combination

* Boosting
  * Train a first model and assign a weight to it. The weight will determine how much this model will be considered for the final output
  * After the first training, the data is weighted so that the data that had bad predictions are favoured on the second model.
  * The second model is trained.. and so on until...
  * a max number of model is reached or a threshold of number of errors is reached.
  * Example : XGBoost, AdaBoost
* Bagging
  * train multiple models, each on a different part of the dataset. The final result is a result of the majority of votes for example ,or the average of the different model responses
  * Example : Random forests
* Stacking
  * different model **types** are trained on the dataset.
  * all the predictions are used to create a new training dataset
  * a meta model is trained on this dataset that will provide the final output

## Hyperparameter Tuning

### Methods

* Manual selection (based on experience)
* Grid search : a grid containing all possible values combinations within a specified range
* Random search : take random values
* Bayesian Optimization : calculate the next set of parameters based on the previous sets and associated results
  * main drawback : sequential training (does not scale well)
* Hyperband
  * takes a set of hyper parameters and use them in multiple epochs
  * at the end of this number of epochs, drop half the hyper parameters set that less perform
  * Continue with the next ones, and train on more epochs
  * go on until, there is only one set remaining

## Model compression

* Pruning : removing least important parameters of the dataset
* Quantization : changes the representation of weights of a model. For example, from a 32-bit floating point, replace by a 8-bit integer
* Knowledge distillation : a student model (simpler) is trained by taking the training data set of the teacher. Also it uses the teacher soft labels (probability distribution of outputs) to adjust its weight.

## Model evaluation

* Accuracy : TP + TN / TP + FP + TN + FN
  * Basically it measures the ratio of correct predictions.
  * it might not be a good indicator if the dataset is imbalanced. For example if there are a lot of TN regarding TP.
* Precision
  * TP / TP + FP
  * measures the ratio of correct predictions when the label to predict should be positive.
  * Precision measures the proportion of **predicted** positive cases that are actually positive
  * For example, when detecting a spam, what is important is to be sure that a non spam email should not be classified as spam. It has more bad consquences than don't filter a real spam.
* Recall
  * TP / TP + FN
  * it's a good metric when cost of false negatives is high. 
  * Recall measures the proportion of **actual** positive cases that the model correctly identifies.
  * For example, a model that should detect an illness. If the model identify a patient free of disease wrongly, it can be very annoying. For example, if the model predicts a disease to a patient that does not have anything, it's less important, because probably, other studies will show there's no disease.
* F1 score : 2 * Precision * Recall / Precision + Recall
  * It's an indicator that mixes Precision and Recall.

## Model convergence issues

* SageMaker Automatic Model Tuning (AMT)
  *  can automatically tune the hyperparameters to find the best configuration.
  *  can help overcome convergence issues by exploring different combinations of hyperparameters to find the optimal settings that lead to better convergence and model performance. 
  *  These hyperparameters include learning rates, batch sizes, and regularization techniques.
* SageMaker Training Compiler 
  *  Reduce training time on GPU instances. 
  *  The compiler optimizes DL models to accelerate training by more efficiently using SageMaker machine learning GPU instances. 
  *  Automatically applies graph and tensor optimization, enabling the efficient utilization of hardware resources and reducing training time
*  Sagemaker debugger
   *  helps identify convergence issues
   *  it outputs metrics from the training phase, and helps diagnose issues. It can be used with Model Monitor or Clarify to understand why there are issues, or to anticipate what feature to monitor specifically (in case of Model Monitor). Note that debugger does not integrate directly with clarify and model monitor, but it can be used with those features to understand more deeply what is happening.
   *  it integrates directly with services like Lambda, Cloudwatch Events or SNS to react when these metrics trigger a threshold (send notification, stop a job, etc...)
   *  Built-in rules and custom rules can be defined to output the metrics
*  SageMaker Clarify
    * metrics on feature explanations with SHAP or Partial Dependency Plots (PDP). 
      * PDP is used to visualize the marginal effect of one or two features on the model's predictions
      * SHAP calculates the contribution of each feature to the model's prediction, providing a local explanation for individual predictions
    * metrics on dataset bias (data quality)
    * metrics on model bias on some specific groups (race, gender, etc...)
