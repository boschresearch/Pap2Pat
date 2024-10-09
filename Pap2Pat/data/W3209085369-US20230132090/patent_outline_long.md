# DESCRIPTION

## FIELD

- define NLP and WSD

## BACKGROUND

- motivate WSD
- limitations of supervised models

## SUMMARY

- motivate gloss alignment algorithm
- propose gloss alignment algorithm
- application of gloss alignment algorithm
- embodiment of method
- generate aligned inventories
- obtain word in context sentence
- determine semantic equivalence scores
- predict correct sense of word
- generate positive and negative gloss pairs
- determine sentence textual similarity score
- train gloss classifier

## DETAILED DESCRIPTION

- introduce word sense predicting model
- describe gloss alignment of word sense inventories
- generate pairs of glosses
- label positive and negative pairs of glosses
- generate pairs of glosses using glosses within each word sense inventory
- obtain context sentence
- train model using training data
- use pre-trained transformers
- generate probability to predict correct sense of word
- evaluate word sense predicting model using WSD Datasets
- generate positive and negative pairs of glosses from built-in training data
- generate aligned inventories using dictionaries
- train transformers using augmented training data
- train general model using aligned inventories
- fine-tune general model on built-in training data
- compare expert model with previous best model
- demonstrate benefits of leveraging multiple word sense inventories
- evaluate word sense predicting model on FEWS dataset
- augment FEWS train set with multiple word sense inventories
- adopt transfer learning strategy on FEWS dataset
- describe aligned word sense inventory
- use dictionaries as word sense inventories
- align parallel glosses from multiple word sense inventories
- determine best matching function using optimization setup
- use Maximum Weighted Bipartite matching
- configure matching function to maximize sentence textual similarity
- describe example setup of Maximum Weighted Bipartite Matching optimization
- use secondary pre-trained model to measure sentence textual similarity
- describe semantic equivalence recognizer model
- train transformers using gloss examples from aligned inventories
- train transformers using augmented training data
- produce output probabilities for glosses semantically equivalent to word in context sentence
- describe word sense predicting model
- introduce process 400
- generate aligned inventories
- obtain word in context sentence
- determine semantic equivalence scores
- predict correct sense of word
- introduce process 500
- collect glosses from first word sense inventory
- collect glosses from second word sense inventory
- determine best match between inventories
- determine sentence textual similarity score
- determine matching function
- generate positive gloss pairs
- generate negative gloss pairs
- introduce process 600
- input context sentence into semantic equivalence recognizer model
- input pairs of glosses into semantic equivalence recognizer model
- identify glosses associated with word in context sentence
- apply trained gloss classifier
- generate probability score for each gloss
- introduce process 700
- input context sentence into semantic equivalence recognizer model
- input pairs of glosses into semantic equivalence recognizer model
- identify glosses associated with word in context sentence
- apply trained gloss classifier

