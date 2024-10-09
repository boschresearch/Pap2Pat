# DESCRIPTION

## BACKGROUND

- introduce conversational search
- limitations of traditional search
- describe conversational search paradigm
- summarize related art limitations

## SUMMARY

- introduce computer-implemented method
- receive search conversation
- retrieve relevant text passages
- retrieve candidate clarification questions
- rank candidate clarification questions
- provide highest-ranking candidate question
- introduce system embodiment
- describe system components
- introduce computer program product
- describe program code execution
- fuse scores from deep learning models
- retrieve solution documents
- extract candidate text passages
- retrieve candidate clarification questions
- train deep learning models

## DETAILED DESCRIPTION

- introduce computer-implemented method for automatic selection of clarification question
- describe system and computer program product embodiments
- explain use of deep learning models to rank candidate clarification questions
- describe first model outputting score denoting strength of association between candidate clarification question and search conversation
- describe second model outputting score denoting strength of association between candidate clarification question, search conversation, and text passage
- discuss fusion of scores from both models
- describe retrieval of candidate clarification questions
- introduce block diagram of exemplary configuration for training deep learning models
- describe training system components
- describe conversational search system components
- describe clarification-question selection module
- discuss training system operation
- describe conversational search system operation
- introduce flowchart of method for training one or two models
- obtain H2H conversations
- obtain text passages relevant to each H2H conversation
- label clarification questions and answers in H2H conversations
- discuss scoring solution documents based on relevancy to H2H conversation
- discuss utterance-biased extension for enhanced word-weighting
- retrieve top-r text passages for each H2H conversation
- retrieve candidate clarification questions for each text passage
- discuss creating training sets for first and second models
- train first model based on first training set
- train second model based on second training set
- discuss training first model using triplet network
- discuss training second model using triplet network
- introduce method for selecting suitable clarification question during search conversation
- receive search conversation
- retrieve text passages relevant to search conversation
- retrieve top-m solution documents
- extract candidate text passages from solution documents
- assign initial score to each candidate text passage
- calculate final text passage score
- select top-r text passages
- retrieve candidate clarification questions for each text passage
- rank candidate clarification questions using one or both trained models
- discuss ranking by first trained model
- discuss ranking by second trained model
- fuse scores from both models
- select top-ranking candidate clarification question
- provide top-ranking candidate clarification question to user
- discuss optional presentation of multiple top-ranking candidate clarification questions
- describe conversational search system operation
- describe clarification-question selection module operation
- discuss training system implementation
- discuss conversational search system implementation
- discuss clarification-question selection module implementation
- discuss hardware and software components
- discuss operating system and software components
- discuss additional components and modules
- conclude description of patent application

### Experimental Results

- evaluate method 200 and method 300
- introduce ClariQ dataset
- introduce Support dataset
- describe differences between datasets
- describe experimental setup
- represent documents using two fields
- use sliding window for text passage retrieval
- set hyperparameters
- use PyTorch Hugging Face implementation of BERT
- fine-tune BERT models
- retrieve initial candidate clarifications
- report results of development sets
- compare BERT rankers to IR-Base
- observe similar results from BERT models
- fuse scores for further improvement
- report official ClariQ results on test set
- describe optional embodiments of the invention
- define system, method, and computer program product
- describe computer readable storage medium
- list examples of computer readable storage medium
- describe computer readable program instructions
- download instructions from network
- execute instructions on computing device
- describe flowchart and block diagram illustrations
- implement functions using computer readable program instructions
- describe scope of numerical values
- clarify terminology and inconsistencies

