# DESCRIPTION

## TECHNICAL FIELD

- relate to identifying codemixed text

## BACKGROUND

- describe limitations of sentence level- and document level language identifiers

## SUMMARY

- receive codemixed text
- segment codemixed text into tokens
- extract features from each token
- predict probability distribution over possible languages for each token
- assign language to each token using greedy search
- extract features from adjacent tokens
- use character features, script features, or lexicon features
- implement language identifier model using feed-forward neural network
- receive assignment constraint for language assignment
- execute lexicon feature dropout strategy during training

## DETAILED DESCRIPTION

- introduce codemixed text problem
- motivate need for language identification
- describe limitations of existing services
- introduce two-stage process for language identification
- describe first stage: predicting probability distribution
- describe feature extraction for tokens
- describe feed-forward neural network for language prediction
- describe second stage: assigning language labels
- describe decoder and greedy decoding strategy
- describe global constraints for language assignment
- describe advantages of two-stage process
- introduce system architecture
- describe language identifier and its components
- describe example applications of language identification
- describe variations of codemixed text
- define character n-gram features
- calculate frequency of character n-gram features
- use feature hashing to control vocabulary size
- extract character script features
- store character script library
- extract lexicon features
- store lexicon library
- extract features from adjacent tokens
- describe neural network model architecture
- define embedding layer
- describe hidden layer and output layer
- illustrate example probability distributions over possible languages
- describe greedy decoding strategy
- apply assignment constraint
- execute greedy decoding strategy
- calculate score associated with assignment constraint
- compare language predictions under different assignment constraints
- assign language labels to tokens
- describe applications using per-token language labels
- discuss limitations of feed-forward neural network model
- describe grouped feature dropout strategy
- train feed-forward neural network model
- evaluate accuracy of model on different datasets
- compare accuracy of model with benchmark models
- describe method of per-token language identification
- receive codemixed text
- segment codemixed text into tokens
- describe codemixed text processing method
- extract features from tokens
- predict language probability distribution using neural network
- assign language to tokens using greedy search
- define software application
- describe computing device architecture
- detail memory and storage components
- explain high-speed and low-speed controllers
- illustrate various computing device implementations
- discuss digital electronic and optical circuitry
- describe machine-readable medium and computer program
- summarize computer processing and interaction

