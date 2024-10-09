# DESCRIPTION

## CROSS REFERENCE(S)

- claim priority

## TECHNICAL FIELD

- define technical field

## BACKGROUND

- motivate NLP evaluation

## DETAILED DESCRIPTION

- define network and module
- describe evaluation mechanism for NLG-NND
- introduce method of generating evaluation dataset
- describe method of using evaluation dataset to evaluate NLP models
- illustrate system for evaluation of model for natural language generation
- describe components of system 100
- explain evaluation of model 104 based on unit test
- describe generation of sequence likelihoods
- explain formula for likelihood calculation
- describe normalization of likelihood
- explain unit test computation
- describe determination of pass/fail result
- explain generation of evaluation result
- describe overall pass rate and breakdown of pass-rates
- explain use of overall pass percentage and pass rates
- describe annotation of dataset 120 with labels or notations
- explain organization of candidates into partially ordered set
- describe evaluation of model 104 for different NLG tasks
- explain generation of unit tests for any NLG task
- illustrate system for generating dataset
- describe generation of sequence of tokens
- explain determination of intermediate probability associated with candidates
- describe generation of dataset 120
- explain selection of candidate pairs for unit tests
- describe inclusion of likelihood of candidates in dataset 120
- explain generation of plurality of unit tests
- describe evaluation of models based on likelihood of reproducing mistakes
- explain generation of dataset 120 for question generation task
- describe generation of unit tests for evaluating question generation task
- explain generation of dataset 120 for question answering task
- describe generation of unit tests for evaluating question answering task
- explain generation of dataset 120 for summarization task
- describe generation of unit tests for evaluating summarization task
- explain normalization of quality notations
- describe generation of dataset 120 for summarization task with hierarchical error categorization
- explain use of quality notations with hierarchical error categorization
- describe generation of unit tests for evaluating summarization task with hierarchical error categorization

### Example Workflows

- illustrate example process of model evaluation framework
- receive evaluation dataset with unit tests
- determine first likelihood of generating first candidate
- determine second likelihood of generating second candidate
- compare first and second likelihoods
- determine if model passed unit test
- perform steps with respect to plurality of unit tests
- increment test pass count
- determine aggregate pass rate
- illustrate example process of dataset generation
- determine likelihood of generating candidates
- receive first quality notation associated with first candidate
- receive second quality notation associated with second candidate
- determine near negative distinction
- generate unit test with input context and candidates
- associate candidates with quality notations
- enable evaluation of model

### Computing Environment

- introduce computing device
- describe processor and memory
- explain operation of computing device
- detail memory types
- describe model evaluation module
- explain data interface
- describe model dataset generation module
- discuss implementation of modules

### Example Performance

- introduce system evaluation
- describe evaluation metrics
- explain model comparison
- discuss verification experiments
- detail question generation evaluation
- describe QA evaluation
- explain summarization evaluation
- discuss correlation results
- compare NND and reference-based metrics
- explain near negatives
- discuss model evaluation framework
- introduce practical applications
- describe extrapolating model performance
- explain fine-grained model comparison
- discuss model scaling effects
- evaluate model training
- introduce quiz design study
- discuss unseen model evaluation
- summarize NND pass rates
- determine model performance
- discuss BART-Large and PEGASUS models
- explain summarization evaluation results
- discuss model size effects
- determine performance trends

