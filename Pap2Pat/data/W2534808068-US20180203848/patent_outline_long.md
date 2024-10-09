# DESCRIPTION

## BACKGROUND

- introduce personality trait recognition
- motivate word use and psychometric traits
- summarize linguistic inquiry and word count tool
- describe bag-of-words approach
- limitations of bag-of-linguistic-features approach
- motivate classification of short sequences of text
- describe early work on computational personality recognition
- summarize SVM-based approaches
- motivate deep-learning based approaches
- describe neural network based approach
- describe recurrent neural network based system
- motivate word lookup tables
- describe compositional character models
- limitations of word vectors
- motivate compositional character-to-sequence model

## BRIEF DESCRIPTION

- introduce trait prediction method
- generate character embeddings
- generate word representations
- generate sequence representation
- generate trait prediction

## DETAILED DESCRIPTION

- introduce system and method for personality trait prediction
- define character and word
- describe text sequence
- illustrate functional block diagram of computer-implemented system
- describe memory and processor
- describe input/output devices
- describe computing devices
- describe memory types
- describe network interface
- describe digital processor device
- define software
- describe software instructions
- describe learning component
- describe text preprocessing component
- describe character embedding component
- describe modeling component
- describe sequence representation component
- describe prediction component
- describe output component
- describe learning process
- describe model learning
- describe text preprocessing
- describe character embedding
- describe sequence representation
- describe prediction
- describe output
- describe method implementation

### Sequence Preprocessing (S104, S202)

- describe input text sequence
- describe tokenization
- describe normalization
- describe word decomposition

### Character Embedding (S106)

- describe character embedding component
- describe one-hot vector representation
- describe embedding transformation

### Sequence Representation and Prediction

- introduce compositional model
- describe character sequence model
- explain word sequence model
- detail recurrent neural networks (RNN) architecture
- describe forward and backward RNNs
- explain hidden state generation
- introduce gated recurrent unit (GRU) network
- detail GRU cell architecture
- explain forward pass equations
- explain backward pass equations
- describe word representation construction
- introduce word-level RNN
- detail word-level RNN architecture
- explain sentence representation construction
- introduce feedforward neural network (FNN)
- detail FNN architecture
- explain prediction output
- describe character-level word representation learning
- introduce long short-term memory (LSTM) network
- detail LSTM architecture
- explain LSTM equations
- describe precomputed word embeddings
- explain word-level RNN processing
- detail sentence embedding construction
- introduce multitask learning
- describe multitask learning model architecture

### Generating User Scores

- describe user-level personality trait scoring

### Learning the Prediction Model (S102)

- introduce learning process
- describe training sample preparation
- explain stochastic gradient descent
- detail Adam optimization method
- introduce mean square error objective function

### Multitask Learning

- introduce multitask learning concept
- describe multitask learning model architecture
- explain multitask learning loss function

### Examples

- introduce dataset
- describe dataset characteristics
- explain gold standard personality labels
- motivate Big 5 test
- describe tokenization process
- explain normalization process
- introduce experiment settings
- describe performance metrics
- present results at user level
- compare with other models
- describe multitask learning
- present results at tweet level
- compare with baseline models
- discuss benefits of multitask learning
- introduce principal component analysis
- visualize learned representations
- analyze example tweets
- discuss language independence
- conclude with potential applications

### Principal Component Analysis of Features

- introduce PCA
- describe visualization process
- analyze clusters of Extraversion
- highlight example tweets
- discuss implications of results

