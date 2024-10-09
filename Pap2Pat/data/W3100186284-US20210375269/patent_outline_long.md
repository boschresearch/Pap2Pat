# DESCRIPTION

## TECHNICAL FIELD

- define technical field

## BACKGROUND

- motivate neural networks
- limitations of dialogue act tagging

## DETAILED DESCRIPTION

- motivate dialogue act tagging
- limitations of existing dialogue act taggers
- introduce embodiments for efficient dialogue act tagging
- define key terms

### Overview

- introduce dialogue act tagging
- describe multi-label classification problem
- illustrate example block diagram of using pre-trained language model
- describe limitations of pre-trained language model
- introduce mask augmentation for adapting pre-trained language model
- describe training with mask augmented data
- illustrate example data segment of labeled dialogue
- illustrate example data segment of dialogue in target domain
- describe cross-domain generalization challenge
- introduce computer environment
- describe computing device for implementing neural network
- describe processor and memory
- describe machine readable media
- describe dialogue act tagging module
- describe supervised tagging loss module
- describe masked tagging loss module
- describe masked language model loss module
- describe disagreement loss module
- describe language module
- describe training mechanisms
- illustrate training mechanisms
- describe dialogue act tagging task
- formalize dialogue act tagging as multi-label classification problem
- describe objective of dialogue act tagging
- describe labeled and unlabeled examples
- illustrate learning supervised objective
- describe supervised tagging loss
- illustrate learning semi-supervised objective
- describe masked tagging loss
- illustrate learning original objective
- describe masked language model loss
- illustrate learning teacher-student mechanism
- describe disagreement loss
- describe stochastic imputation-based teacher and student selection
- describe masking probabilities
- describe augmented sequences
- describe output distributions
- describe DAL loss
- illustrate mask augmentation under teacher-student mechanism
- describe flattened sequence representation
- describe randomly masked sequences
- describe output distributions
- describe binary cross-entropy
- illustrate method for training language model-based dialogue act tagging module
- describe receiving input of dialogue history
- describe generating dialogue history representation
- describe computing aggregated loss metric

### Example Performance

- provide example data charts
- introduce GSIM and SGD datasets
- describe dialogue acts and universal schema
- illustrate performance of adapting dialogue act tagger
- show effect of MTL and DAL objectives on language models
- compare performance of Transformer and BERT models
- highlight benefits of fine-tuning with STL objective
- demonstrate improvement with DAL and MTL objectives
- show performance of pre-BERT model
- illustrate effect of MLM loss on target domain
- demonstrate improvement with mask augmentation
- show performance under low-resource setting
- illustrate effect of domain-adaptive pre-training
- provide complete results for FIG. 9
- show micro-F1 scores for each dialog act
- analyze adaptation performance across dialog acts
- provide example data outputs of dialogue act tags
- describe computing devices and machine readable media
- discuss scope and limitations of the disclosure

