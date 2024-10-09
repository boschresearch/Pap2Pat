# DESCRIPTION

## CROSS REFERENCE(S)

- claim priority

## TECHNICAL FIELD

- define technical field

## BACKGROUND

- motivate paraphrase generation
- limitations of existing systems

## DETAILED DESCRIPTION

- introduce dynamic blocking for paraphrase generation
- describe architecture of language model with encoder and decoder
- explain dynamic blocking mechanism with block dictionary and sampling
- discuss advantages of dynamic blocking over static blocking

### Overview

- introduce FIG. 1 and architecture of language model
- describe encoder and decoder components
- explain input source sequence and vector representation
- describe generation of paraphrased sentence
- discuss problem of generating identical tokens
- introduce dynamic blocking mechanism
- explain block dictionary and sampling
- describe generation of paraphrased sequence with dynamic blocking
- discuss example of paraphrasing with dynamic blocking
- explain beam search for generating multiple candidates
- discuss diversity of generated paraphrases
- introduce FIG. 2 and training mechanism
- describe task-adaptive training and self-supervised training
- explain pseudo-labeling and self-supervision
- discuss benefits of self-supervision
- describe reversed data for generating shorter paraphrases

### Computer Environment

- introduce FIG. 3 and computing device
- describe processor and memory components
- explain operation of computing device
- discuss memory storage and software execution
- introduce paraphrase generation module
- describe input and output of paraphrase generation module
- explain sub-modules of paraphrase generation module

### Work Flows

- introduce FIG. 4 and method for generating paraphrase text
- describe receiving input sequence of tokens
- explain generating active dictionaries and output tokens
- discuss blocking output tokens with dynamic blocking
- introduce FIG. 5 and pseudo-code algorithm for dynamic blocking

### Example Performance

- introduce BertBLEU metric
- define BertBLEU formula
- explain semantic similarity measurement
- describe IDF-reweighing
- explain surface-form dissimilarity measurement
- introduce blocking strategies
- describe addition of block surface-form variations
- describe addition of block closed-class words
- introduce example training datasets
- describe Quora Question Pair dataset
- describe ParaNMT dataset
- explain task-adaptation
- describe self-supervision data generation
- introduce supervised Transformer model
- describe CorruptLM model
- explain evaluation metrics
- describe iBLEU metric
- describe BLEU metric
- describe ROUGE metric
- report human evaluation results
- describe head-to-head binary comparison
- describe Likert-scale scoring
- explain annotator selection criteria
- describe human evaluation results on QQP
- describe human evaluation results on ParaNMT
- calculate Cohen's Kappa
- investigate correlation of automatic metrics with human evaluation
- present automatic evaluation results on QQP
- present automatic evaluation results on ParaNMT
- conduct ablation studies on finetuning phases
- demonstrate generalization to other languages
- describe computing devices and machine-readable media

