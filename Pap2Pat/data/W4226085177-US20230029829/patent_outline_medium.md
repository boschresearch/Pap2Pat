# DESCRIPTION

## BACKGROUND

- introduce conversational search
- limitations of current approaches

## SUMMARY

- describe computer-implemented method
- describe system embodiment
- describe computer program product
- rank candidate clarification questions
- retrieve text passages
- retrieve candidate clarification questions
- train deep learning models

## DETAILED DESCRIPTION

- introduce computer-implemented method for automatic selection of clarification question
- describe use of deep learning models to rank candidate clarification questions
- introduce first model for ranking clarification questions based on search conversation
- introduce second model for ranking clarification questions based on search conversation and text passage
- describe training system for training models
- describe components of training system
- describe conversational search system
- describe clarification-question selection module
- describe method for training one or two models for ranking of clarification questions
- obtain H2H conversations for training
- obtain text passages relevant to H2H conversations
- retrieve candidate clarification questions for each text passage
- create training sets for first and second models
- train first model based on first training set
- train second model based on second training set
- describe method for selecting suitable clarification question during search conversation
- receive search conversation
- retrieve text passages relevant to search conversation
- retrieve candidate clarification questions for each text passage
- rank candidate clarification questions using one or both trained models
- fuse scores from both models (optional)
- select top-ranking candidate clarification question
- provide top-ranking candidate clarification question to user
- describe optional presentation of multiple top-ranking candidate clarification questions
- conclude description of patent application

### Experimental Results

- introduce datasets
- describe dataset differences
- explain experimental setup
- detail document representation
- describe text passage retrieval
- specify hyperparameters
- outline BERT model implementation
- report development set results
- compare BERT models
- show official Clariq results
- describe optional embodiments
- define computer program product
- explain computer readable storage medium

