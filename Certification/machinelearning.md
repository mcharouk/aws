# Sagemaker projects

* Offer a standardized structure and tooling to streamline the development, deployment, and maintenance of ML applications. Think of them as blueprints for your ML projects, promoting best practices and repeatability.
* Integrates with 
  * Github
  * CodePipeline
  * CodeBuild (for build step that are not ML specific)
  * SageMaker pipelines (for orchestration that is ML specific)
  * SageMaker Studio
  * S3

# Data Preparation

## Encoding techniques

* Label encoding : replace a label by a number
* One hot encoding
  * replace a multi class label by a table of boolean. 
  * Does not scale when there is a lot of class.
* Target encoding : replaces a feature's categories with some number derived from the target. 
  * For exemple, for a group of item replace a number by the mean of the group.

## Feature engineering

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
  * PCA : used for dimensionality reduction. It retain most of the original variations but reduce the number of features. PCA can be applied to a subset of feature.

## Sagemaker feature store

* regroup feature in feature groups
* can join data from multiple feature groups to create a final dataset.
* two data mandatory to create a feature store
  * Record Identifier: A unique identifier for each record in the feature group (e.g., customer ID, product ID). This is the primary key.
  * Event Time: A timestamp indicating when the feature value was recorded or updated. This is crucial for time-series data and point-in-time correctness.
* Can have an online feature (dynamodb) store or offline feature store (s3)
* Features can be 
  * online only
  * offline only
  * online and offline
* TTL configurable

## Data labeling

* Mechnical Turk
  *  delegate tasks to workers. This can be about ML but not necessarily.
  *  Quality must be monitored by the client.
*  Groundtruth
   *  specific to ML labelling tasks
   *  integrated with Sagemaker
   *  With groundTruth Plus : active learning / poor performers removal / label automatic refining / validation and monitoring of DQ 
   *  can delegate tasks to employees instead of mech turk workforce

## Dataset balancing

To remediate unbalanced dataset : 
  * Numeric data
    * Oversampling
      * Random sampling : consists duplicating minority dataset
      * **SMOTE** : interpolates new data from existing data
  * Text data
    * Resampling
    * Synthetic data generation (create new data from scratch)
  * Image data
    * Data augmentation : create synthetic data from real data with ML algo like GAN (Generative Adversarial Network)

## Dataset bias

* **DPL** (Difference of Proportions of Label) is a metric that you can use to detect **post-training** bias : DPL measures the difference in the proportion of positive outcomes (or a specific label) between different groups after the model has been trained
* Kullback Leibler Divergence (KL) : measures the difference between two probability distributions. measuring how far off your predictions are from true labels
* Total Variation Distance (TVD) : **Pre training bias**. Captures variances in sub group outcomes, reflecting unequal acceptance and rejection ratios
* Conditional Demographic Disparity (CDD) : **post training bias**, focus on whether disparities in outcomes exist across different demographic groups within specific subgroups defined by other features. For example, calculate loan approval rate by race, and split it by income differences. On low income and high income, you could see no disparity, but it could be the case for medium income for example.


# Training

## Dataset splitting

* Simple hold-out : selecting 80% for training, 10% for tests, 10%  for validation
* K-fold cross validation
  * split k times the dataset, to take each time a different sample for training and validating.
  * It provides an estimate of how well a modeling approach will generalize
    * using performance metrics (average accuracy)
    * using variance across the K folds. A high variance can indicate the model is sensitive to the specific training dataset. It can indicate overfitting.
  * You use this estimate to select the best approach (algorithm, hyperparameters).
  * You then train a single, final model on the entire dataset using the chosen approach. This is the model you deploy.

* A good practice is to shuffle the data before selecting it to ensure randomness on data selection.

## SageMaker Model Registry

* organize models in Model group
* Can create collections to discover models in different model groups, in a hierarchical way.

## Model tuning

* Loss function is the function used to evaluate the prediction qualities. It help adjust the hyper parameters of the model.
  * for regression : root mean square error
  * for classification : log-likelihood loss
* Optimization technique refers to the path it takes to reach for the global minimum, means the set of hyper parameters that gives the better results.
  * gradient descent : compute intensive but best technique to find the global minimum
  * stochastic gradient descent : only take one data point to find the global minimum. This can lead to inaccurate results but cheap
  * mini batch gradient descent : hybrid solution. Takes a subset of data points to determine the global minimum.
* batch size is a hyperparameter that determines the number of data points taken for each iteration. Larger batch size, are more prone to overfitting.

## Sagemaker

### Compute options

* use sagemaker prebuilt algorithm (use image provided with prebuild algorithm)
* use sagemaker framework containers
* extend sagemaker framework containers
* BYOC
* Market place

### Managed instances

* family good for deep learning training : p3 (GPU), p4d (GPU), dl1, tr1 (trainium)
* family good for deep learning inference : inf1 (inferentia), g5
* for other ml : take m, c family
* take GPU for massive datasets or for deep learning

### Model selection

* Reinforcement Learning : support MxNet and TensorFlow

### Model training

#### Script mode

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


#### Overfitting remediation

* Early stopping
* Pruning
  * remove features that doesn't contribute a lot to the output. It lower the noise
  * Regularization
    * Dropout
      * **Specific to neural networks**
      * Randomly drops out, or sets to zero, a number of neurons in each layer of the neural network during each epoch
      * forces the network to not overemphasize specific neurons and develop multiple methods of arriving at a result.
    * L1 : Reduces the number of features that impact the training of the model. Instead of removing the features themselves, you use L1 regularization to push the weights of less important features to zero
    * L2 : Results in smaller overall weight values and stabilizes the weights when there is high correlation between the input features
  * Data augmentation : generate new synthetic data to increase the diversity of the training data
  * Model architecture simplification : take a simpler model or change hyperparameters to simplify the model

#### Scaling model training

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
* Quantization : changes the representation of weights of a model. For example, from a 32-bit floating point, replace by a 8-bit integer. Primarly used to reduce memory footprint and speeds up computation of the model.
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
  * To maximize recall means to minimize the false negatives.
* F1 score : 2 * Precision * Recall / Precision + Recall
  * It's an indicator that mixes Precision and Recall.

* Receiver Operating characteristics
  * ROC curve is a graphical representation of the performance of a classification model at all classification thresholds. Basically is threshold is set to 0,5, that means all prediction > 0,5 will be classified as positive.
    * Lowering the threshold gives you more true positive and false positive as well
    * Raising the threshold gives you less true positive and less false positive.
* Area under the curve
  * used with ROC curve. 
  * it's a number between 0 and 1. 
  * 1 is perfect
  * 0,5 means the model performs likes a random guess
  * < 0,5 means worse than random
  
   


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


## SageMaker TensorBoard

* TensorBoard is a visualization toolkit for machine learning experimentation. It's part of the TensorFlow ecosystem but can be used with other frameworks like PyTorch. It helps you track and visualize metrics like loss and accuracy, visualize model graphs, examine weight distributions, and much more. It's crucial for understanding and debugging your training process
* This service bridges the gap between SageMaker and TensorBoard. Instead of having to manually set up and manage TensorBoard instances, SageMaker TensorBoard provides a managed environment

## SageMaker Experiments

there was a legacy custom feature of SageMaker to track experiments. Now it has been replaced by a managed service of MLFlow.

# SageMaker CI/CD

## SageMaker pipelines

### Steps
####  Processing
* processing
####  Training

* training
* tuning (hyperparameters)
* fine-tuning (tune a pre existing model)
* automl
#### Model
* model (create or register a Sagemaker AI model)
* create model (just create)
* register (just register)

#### Deploy, Inference & Monitoring

* Deploy
* Transform (batch inference)
* ClarifyCheck 
  * conduct baseline drift checks
  * generate and register baselines (used by Model Monitor)
* suggest baseline (can be used by Model Monitor)

#### Other services integration
* EMR
* Notebook
* Callback (to integrate with other external services)
* Lambda

# SageMaker Deployment options

## Deployment modes

* Multi model deployment
    * A/B testing
    * intelligently route requests to a specific model
    * Dynamic model loading to save costs
    * Multi tenant applications when each customer needs their own unique model
* Multi container deployment
  * there is a pipeline that includes pre processing and post processing between inference step.
  * complex workflows : container can be used to split the workflow in small parts.
* Shadow Variant
  * deploy a model with its container behind the same endpoint than the production model. The candidate model will receive some percentage of traffic and redirects the response in a S3 bucket.

## Infrastructure

### Containers 

* can use a Sagemaker managed container
  * no code to handle inbound and outbound requests
* can use own inference code
  * can extend Sagemaker managed container to inherit all the libraries and dependencies
  * can BYOC

### Instance types

* Training
  * CPU -> small to medium sized models
  * GPU -> good choice for **training** bigger models
  * Trainium
    * More cost effective than GPU
    * More limited availability
* Inferentia
  * Can be more cost-effective than GPU instances
  * not all models can work on them, limited framework support
  * for deep learning applications


# Catastrophic forgetting

* it can happen on incremental training.
* incremental training is the ability to fine tune an existing model to adapt it to new tasks
  * for example a model knows how to recognize cats
  * we want to train the model so that it can recognize cats and dogs without having to retrain the cat recognition capability.
  * the main risk is that the model changes its weights and forgets how to recognize cats
* Different techniques to avoid it
  * Regularization
    * **Elastic Weight Consolidation (EWC)**: assign different importance to the model parameters based on their relevance to the previous tasks, preventing the model from forgetting the important parameters
    * **Synaptic Intelligence** : tracks the importance of each parameter during training and uses this information to selectively update the parameters, reducing catastrophic forgetting 
  * Replay-based methods
    * **Experience Replay** : stores a small subset of the data from previous tasks and replays it during the training of the current task. This replaying helps the model maintain the knowledge acquired from the previous tasks.
    * **Generative Replay** : No actual data is stored. In this method, a generative model synthesizes data from the previous tasks and uses it for training the current task.
  * Architectural methods
    * **Progressive Neural Networks** : involves growing the model's capacity as new tasks are learned, supporting the model to retain the knowledge from previous tasks without overwriting it.
    * **Modular Networks** : the model is divided into different modules, where each module is responsible for a specific task. This way, the model can retain the knowledge from previous tasks by preserving the corresponding modules.
  * Rehearsal based methods
    * **Gradient Episodic Memory** : stores a small subset of the data from previous tasks and interleaves it with the data for the current task during training. This helps the model maintain the knowledge from the previous tasks.
    * **Exemplar Replay** stores a small set of representative examples from the previous tasks and uses them during the training of the current task.

# Monitoring
## Drift types

* Data quality drift : Production data differs than training data
* Model quality drift : predicted labels differ from actual ground truth
* Bias drift
  * Training data too small or not representative
  * Training data has societal assumptions
  * Some important feature have been neglected in training
  * Real world data has changed since last training
* Feature attribution drift : contribution of individual features on prediction differs from the baseline

## SageMaker Model Monitor

* Monitor continuously or at some frequency
* Monitors the model and the data
* Integrates with 
  * Cloudwatch (metrics & logs)
  * Eventbridge
  * Cloudtrail  
  * Sagemaker Clarify


* Monitor data drift
  * gets a baseline of data used to train the model
  * Calculates stats on the dataset, and monitor a drift with incoming new data
  * generates a report (on S3) 

  * The steps to use it
    * generate a data capture on endpoint, to capture predicted data in production
    * generate a baseline. It's a batch that runs on the training dataset. Two files will be provided as output
      * constraints.json
      * statistics.json
    * constraints can be adjusted depending on the use case
    * schedule data quality monitoring jobs
    * Configure integration with cloudwatch. Define the alarm thresholds to raise an alert on SNS.
    * Interpret results. A file named constraint_violations.json will be generated by the job

* Monitor model drifts
  * looks like data drift
  * Baseline job still here calculated from the prediction of a validation dataset. Baseline metrics differs with model type (binary, multiclass, regression)
  * One key difference is the integration of human in the loop process, to provide ground truth labels. Labels must be provided in SageMaker Ground Truth labels format. So it's possible to use another service than Groundtruth to provide the labels, if we transform the labels in this format.
  * Merge groundtruth labels with prediced labels. A merged file is produced
  * Violation are sent to S3 and can integrate with Cloudwatch metrics. 

* Feature attribution drift
  * looks like model drift
  * create a SHAP in the baseline job
  * Clarify is used to compute SHAP and compare with the baseline to detect a drift

* SageMaker Clarify can help to understand why a model has drifted by providing insights about the distribution of data, or features attribution of the model.
* on post training data, you can declare a facet, and compare drift on each facet.
* on pre training data, you can identify source of bias 


## SageMaker Model Dashboard

  * single pane of glass to monitor the model
    * Alerts
    * model card's risk rating (measures business impact of the model's predictions)
    * Endpoint performance (infrastructure)
    * most recent batch transform job
    * Model lineage graph (pipeline from data preparation to inference)
    * links to model details

## SageMaker Lineage Tracking

  * helps to track on which data has the model being trained, and on which endpoint it has been deployed.
  * can be used to quickly identify the bad dataset and the impacted endpoints.


# Finops

## SageMaker Inference Recommender

* Inference recommendations
  * It can launch a load test based on your data to recommend a type of infra (45 min. duration)
  * Inferentia, GPU/CPU, etc...
* Endpoint recommendations
  * Based on a custom load test. Specify custom traffic pattern, requirements for latency and throughput (2 hrs. duration)
  * Return the same result format that inference recommendation, but more customized on the business needs.
* Provide a list of recommended instances
* Can also use Compute Optimizer but does not work on SageMaker managed instances

## Capacity Blocks for ML

* Reserve highly sought-after GPU instances on a future date
* Instances are placed close together inside EC2 UltraClusters, for low-latency, petabit-scale, nonblocking networking
* pay only for the amount of time needed
* good for training jobs of experimentation


## ML Savings plan

* SageMaker Saving plans : SageMaker training jobs, hosted models, and batch transform jobs.
* Machine Learning Services Savings Plan : covers managed ML services (rekognition, transcribe, translate, etc..)

# Metrics glossary 

## Training

* Weighted Quantile Loss (wQL) : The wQL metric measures the accuracy of a model at a specified quantile
* Mean Absolute Scaled Error : MASE is calculated by dividing the average error by a scaling factor that is affected by seasonality
* The Gini impurity formula is used to measure the impurity or disorder of a set of data. In the context of decision trees, it's used to evaluate the quality of a split

## Algorithms

* DeepAR is an algorithm that is available in SageMaker to forecast based on historical time series data

## Data pre processing

* quantic binning transformation : The core idea is to take a continuous numerical feature and convert it into a categorical feature. This is done by dividing the range of the continuous feature into intervals (bins).

## Neural networks

* Sigmoid function : used in binary classification. Converts an input in 0 or 1
* tanh function : same than sigmoid but centered on 0, not 0.5 like Sigmoid
* Relu function : f(x) = max(0, x). Basically it replaces the negative values by 0


# Sagemaker built-in algorithms

* Regression : Linear Learner
* Classification or Regression : XGBoost
* Object Detection : SSD, Faster R-CNN, YOLO
* Image Classification : ResNet, Inception, VGG
* Semantic Segmentation : Fully Convolutional Networks (FCNs) or U-Net
* Dimensionality Reduction : Principal Component Analysis
* Unsupervised learning : K-Means
* Word embeddings and text classification : BlazingText
* Time series forecasting : DeepAR Forecasting
* Recommendation and user preferences : Factorization Machines
* Topics discovery in text data : Neural Topic Model
* Topic modeling algorithm : LDA
* Machine translation : Sequence-to-Sequence


