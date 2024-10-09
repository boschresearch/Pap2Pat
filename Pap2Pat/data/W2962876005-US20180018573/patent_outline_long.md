# DESCRIPTION

## BACKGROUND

- introduce vector-space representations of semantics
- motivate distributional models of semantics
- describe limitations of similarity measures
- summarize previous work on modeling entailment
- introduce Conditional Bag-of-Words and Skip-Gram models
- describe applications of word embeddings
- motivate entailment as a more powerful semantic relation
- summarize previous work on unsupervised models of lexical entailment
- describe supervised and semi-supervised methods for hyponymy detection
- introduce the present system and method

## BRIEF DESCRIPTION

- introduce method for making entailment inference
- describe computing entailment inference with asymmetric vector space operator
- introduce entailment system with representation generation component
- describe inference component and output component
- introduce method for making entailment inference with selected asymmetric vector space operator

## DETAILED DESCRIPTION

- define logical entailment
- introduce distributional semantics
- describe vector-space model for entailment
- motivate mean-field approximation
- describe entailment operators
- illustrate entailment with examples
- describe factorized entailment operator
- parameterize forward-inference entailment operator
- parameterize backward-inference entailment operator
- compute entailment scores
- illustrate entailment prediction
- describe application to Word2Vec model
- describe extension to entailment graphs
- describe clustering text objects
- illustrate system architecture
- describe computer system components
- describe memory and storage
- describe processor and execution
- describe input/output devices
- describe software instructions
- describe learning component
- describe representation generation component
- describe inference component
- describe clustering component
- describe output component
- illustrate method of inferring entailment relations
- receive training data
- learn semantic model
- generate semantic representations
- make entailment inferences
- cluster semantic representations
- output information
- describe vector operators
- describe generating feature vectors

### Vector Operators

- describe asymmetric vector space operators
- predict hyponymy using operator functions
- learn semi-supervised model of hyponymy

### Generating Feature Vectors

- learn model from raw text and hyponymy data
- describe alternative methods for generating feature vectors

### Modeling Entailment in a Vector Space

- formalize entailment as logical relation
- define entailment in vector space
- generalize discrete function to continuous values
- define entailment relation with binary formula
- write exact joint probability and marginal probabilities
- introduce mean-field approximation
- describe posterior distribution P(x|... )
- define factorized distribution Q(x,y)
- minimize KL-divergence with true distribution
- derive equation for mean-field approximation
- bound prior terms by assuming exponential family
- introduce approximations for forward and backward inference
- apply Jensen's inequality to log function
- optimize for Q(xk=1) and Q(yk=1)
- define vector-space operators and
- approximate log-probability of entailment
- define forward-inference entailment operator
- define backward-inference entailment operator
- parameterize backward-inference entailment operator
- define vector-space operator
- derive inference equations
- explain constraint vectors
- describe correlation matrix
- outline optimization process
- introduce log-odds entailment operators
- motivate inference in entailment graphs
- assume prior information
- express joint probability
- define entailment relations
- define negated entailment relations
- formulate joint probability equation
- define entailment relations
- introduce graphical model
- derive factorized distribution Q
- approximate L for inference of xik
- simplify L using mean-field approximation
- define θik(xīk) for prior information
- infer optimal Xik
- simplify Xik using log-odds terms
- derive update rule for Xik
- interpret update rule
- discuss backward inference term
- discuss forward inference term
- discuss negative entailment terms
- discuss treatment of negative entailment cases
- summarize mean-field approximation
- discuss optimization of Xixj
- discuss incorporation of negative entailment relations
- discuss incorporation of complex priors
- conclude mean-field approximation
- finalize inference in entailment graphs

### Applications

- introduce applications of inferred vector Y
- example of entailment inference
- describe distributional semantics
- motivate Word2Hyp model
- define Word2Hyp model
- explain inference of hidden vector Zi
- explain log-probability of entailments
- apply sigmoid function to score
- interpret Word2Vec vectors
- re-interpret Word2Vec model
- apply entailment operators to Word2Vec
- calculate log-probability of entailment
- provide alternative interpretation of Word2Vec
- describe Word2Vec's Skip-Gram model
- interpret Word2Vec vectors as log-odds
- calculate inferred hidden vector Y
- describe third alternative interpretation
- introduce algorithms for abstraction clustering
- describe K-abstractions algorithm
- apply forward inference method
- assign vectors to clusters
- find best labeling for clusters
- address imbalanced clusters
- normalize cluster vectors
- describe other applications
- generalize to compositional vector-space model
- model composition of multi-word expressions
- describe textual entailment
- apply to summarization and question answering
- describe opinion summarization
- summarize abstract representation of clusters
- conclude with exemplary vector operators for entailment

## EXAMPLES

- demonstrate entailment detection in semantic vector spaces
- describe experiments on hyponymy relations using Word2Vec distributional semantic vectors
- compare operators to dot product and arithmetic differences
- describe clustering method based on operators
- present initial results on distributional semantics models
- replicate experimental setup of Weeds 2014
- evaluate on hyponymy classification using publicly available word embeddings
- describe semi-supervised experiments with ten-fold cross validation
- present hyponymy classification results in Table 2
- describe direction accuracy measure
- evaluate unsupervised hypernym detection and direction classification
- compare operators to dot product, vector differences, and weighted cosine
- evaluate semi-supervised hypernym detection and direction classification
- train linear vector-space mapping into new vector space
- apply operators in new vector space to predict hyponymy
- discuss results on hyponymy detection with Word2Vec vectors
- evaluate unsupervised models on hyponymy data from Baroni et al.
- summarize results and advantages of entailment operators

### Semi-Supervised Hypernym Detection and Direction Classification

- describe semi-supervised setting
- train linear mappings for operator and vector differences
- present semi-supervised results in Table 2
- compare mapped operator to probabilistic entailment operator and Weeds 2014
- evaluate direction accuracy of mapped operator
- discuss performance of dif operator in mapped setting
- describe evaluation of Word2Hyp distributional semantic model
- train CBOW model of Word2Vec software
- present results on hypernym detection for Word2Hyp vectors in Table 3
- compare Word2Hyp vectors to Word2Vec vectors
- evaluate semi-supervised experiments with Word2Hyp vectors
- compare training gradients of Word2Vec and interpretations
- discuss implications of results for hyponymy detection and textual entailment

