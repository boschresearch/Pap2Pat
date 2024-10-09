# DESCRIPTION

## CROSS REFERENCE(S)

- claim priority

## TECHNICAL FIELD

- define technical field

## BACKGROUND

- motivate cross-lingual sentence alignment
- limitations of training data

## DETAILED DESCRIPTION

- define network
- define module
- define rich-source and low-resource
- motivate cross-lingual sentence alignment
- describe limitations of existing systems
- introduce proposed framework
- describe use of pre-trained multi-lingual language model
- describe supervised version of BERT-score
- describe normalization layer
- describe training on rich-resource language pairs
- describe scaling up with top-k rich-resource language pairs
- describe training without English as an anchor language
- illustrate training framework for alignment model
- describe input sentences
- describe alignment model
- describe embedding model
- describe BERT score computation module
- describe normalization layer
- illustrate BERT score computation
- describe recall score computation
- describe precision score computation
- describe BERT score computation
- describe normalization step
- describe inference stage
- describe contrastive learning approach
- describe in-batch negatives
- describe pairwise semantic similarity computation
- describe contrastive loss computation
- illustrate method of training aligner model
- receive training dataset
- form positive and negative input pairs
- compute pairwise token-level similarity
- compute loss objective
- update pre-trained multi-lingual model
- perform alignment task
- describe computing device for implementing cross-lingual sentence alignment
- describe processor and memory
- describe paraphrase generation module
- describe data interface and output

### Example Performance

- describe aligner model training
- introduce OPUS-100 and Tatoeba Challenge datasets
- explain data removal from OPUS-100
- show performance results in FIGS. 5-13
- introduce cross-lingual sentence retrieval tasks
- describe Tatoeba dataset from XTREME benchmark
- introduce v2021-08-07 Tatoeba Challenge dataset
- explain language pair selection for evaluation
- describe BUCC 2018 dataset
- introduce baseline models for comparison
- describe VECO and ERNIE-M models
- show basic stats of each model in FIG. 6
- compare aligner model with baseline models
- show Tatoeba-36 performance in FIG. 5
- show data efficiency of aligner model
- show consistent performance across language pairs in FIG. 7
- analyze performance against data availability in FIG. 8
- show performance on non-English-centered language pairs in FIG. 9
- explore X-centered language pairs in FIG. 10
- discuss limitations and scope of the disclosure

