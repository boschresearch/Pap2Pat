# DESCRIPTION

## BACKGROUND

- introduce personality trait recognition
- motivate bag-of-words approach
- limitations of bag-of-words approach
- introduce deep-learning based approaches
- motivate neural network approach
- limitations of neural network approach
- motivate compositional character-to-sequence model

## BRIEF DESCRIPTION

- describe trait prediction method
- describe system for trait prediction

## DETAILED DESCRIPTION

- introduce personality trait prediction system
- define character and word
- describe computer-implemented system for personality trait prediction
- illustrate functional block diagram of system
- describe software instructions
- introduce learning component
- describe text preprocessing component
- introduce character embedding component
- describe modeling component
- introduce prediction component
- describe output component
- illustrate method for trait prediction
- describe implementation of method

### Sequence Preprocessing (S104, S202)

- describe input text sequence
- describe tokenization and normalization of input sequence

### Character Embedding (S106)

- describe character embedding component

### Sequence Representation and Prediction

- introduce compositional model 50
- describe character sequence model 56
- explain word sequence model 58
- detail forward and backward RNNs
- describe hidden state generation
- illustrate word representation construction
- explain sentence representation construction
- describe prediction model 54
- detail GRU and LSTM equations
- explain word embeddings computation
- describe sentence embeddings computation
- illustrate multitask learning model
- explain joint training of multitask model

### Generating User Scores

- describe user-level personality trait scores computation

### Learning the Prediction Model (S102)

- describe learning process
- explain stochastic gradient descent

### Multitask Learning

- describe multitask learning model

### Examples

- introduce dataset
- describe data preprocessing
- explain experiment setup
- present results at user level
- compare with other models
- present results at tweet level
- compare with baseline models
- discuss multitask learning
- conclude effectiveness of model

### Principal Component Analysis of Features

- apply PCA to visualize learned representations
- analyze and interpret results

