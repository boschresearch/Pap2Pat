# DESCRIPTION

## BACKGROUND

- introduce vector-space representations of semantics
- motivate distributional semantics
- limitations of similarity measures
- summarize previous work on entailment modeling
- describe hyponymy detection methods

## BRIEF DESCRIPTION

- describe method for making entailment inference
- describe entailment system and its components

## DETAILED DESCRIPTION

- define logical entailment
- introduce distributional semantics
- describe vector-space model for entailment
- motivate mean-field approximation
- derive entailment operators
- describe forward-inference entailment operator
- describe backward-inference entailment operator
- describe factorized entailment operator
- illustrate example of entailment prediction
- describe application to Word2Vec word embeddings
- describe extension to entailment graphs
- describe clustering text objects
- illustrate computer-implemented system for predicting entailment relations
- describe learning component
- describe representation generation component
- describe inference component
- describe output component

### Vector Operators

- describe asymmetric vector space operators

### Generating Feature Vectors

- describe generating feature vectors from raw text

### Modeling Entailment in a Vector Space

- formalize entailment as logical relation
- define entailment in vector space
- generalize discrete function to continuous values
- define entailment relation with binary formula
- write exact joint probability and marginal probabilities
- motivate mean-field approximation
- derive mean-field approximation
- apply mean-field approximation for inference
- define vector-space operators for entailment
- define vector-space operator
- derive inference equations
- explain constraint vectors
- describe optimization process
- introduce log-odds entailment operators
- generalize to inference in entailment graphs
- define entailment relations
- introduce mean-field approximation
- derive loss function
- approximate loss function
- define optimal Xik
- simplify terms
- infer optimal Xik
- explain inference process
- discuss negative entailment cases
- summarize mean-field approximation

### Applications

- introduce applications of inferred vector Y
- motivate entailment-based distributional semantics
- describe Word2Hyp model for distributional semantics
- derive Word2Hyp model equations
- interpret Word2Vec vectors in entailment framework
- apply Word2Vec to hyponymy detection
- introduce alternative interpretations of Word2Vec
- describe algorithms for abstraction clustering
- derive K-abstractions algorithm equations
- address imbalanced clusters in K-abstractions
- motivate other applications of entailment models
- describe compositional vector-space model
- apply entailment models to summarization
- apply entailment models to question answering
- describe opinion summarization application
- summarize exemplary vector operators for entailment

## EXAMPLES

- demonstrate entailment detection in semantic vector spaces
- describe experiments on hyponymy relations using Word2Vec distributional semantic vectors
- compare performance of operators to dot product and arithmetic differences
- describe clustering method based on operators applied to words
- present initial results on distributional semantics models
- replicate experimental setup of Weeds 2014 for hyponymy classification
- evaluate unsupervised hypernym detection and direction classification
- evaluate semi-supervised hypernym detection and direction classification
- discuss results on hyponymy detection with Word2Vec vectors

### Semi-Supervised Hypernym Detection and Direction Classification

- describe semi-supervised setting for hypernym detection
- train linear mappings from Word2Vec word vectors to new word vectors
- apply entailment operators in new vector space to predict hyponymy
- compare performance of operators in semi-supervised setting
- discuss results on semi-supervised hypernym detection and direction classification
- evaluate performance of Word2Hyp model

