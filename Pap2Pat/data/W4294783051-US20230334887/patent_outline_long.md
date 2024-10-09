# DESCRIPTION

## BACKGROUND

- motivate technical challenges

## BRIEF SUMMARY

- introduce method
- generate unmasked label probability scores
- segment document data objects
- perform classification routine iterations
- mask text blocks
- generate per-masked document classification
- generate per-iteration masked label probability scores
- generate per-label text block importance scores
- generate predictive data output
- perform prediction-based actions
- introduce apparatus
- configure apparatus
- introduce computer program product

## DETAILED DESCRIPTION

- introduce predictive data analysis computing entity

### I. OVERVIEW AND TECHNICAL IMPROVEMENTS

- motivate technical contributions
- describe tradeoff between predictive accuracy and training speed
- introduce techniques to improve predictive accuracy and training speed
- describe document classification using machine learning
- introduce sparse attention mechanisms
- describe limitations of existing natural language processing techniques
- introduce masking of text blocks to improve efficiency and speed
- describe benefits of improved efficiency and speed

### II. DEFINITIONS

- define document data object
- define classifier
- define classification
- define document classification machine learning model
- define multi-label classification machine learning model
- define text block
- define label probability score
- define unmasked document data object
- define masked document data object
- define unmasked label probability score
- define per-label masked label probability score
- define predictive data output
- define classification routine iterations
- define required number of classification routine iterations
- define expected text block masking count
- define text block masking probability
- define predictive system
- define token
- define natural language processing output
- define per-iteration masked label probability scores
- define per-label text block importance score
- define masking
- define non-label-specific text block importance score
- describe non-label-specific text block importance score
- define per-masked document classification
- define per-label pairwise text block importance score
- describe per-label pairwise text block importance score
- define document data object components
- define classification label groups
- define multi-label classification
- define sequence of classifiers
- define classification label prediction
- define document classification machine learning model components
- define long document models
- define Bidirectional Encoder Representation from Transformers (BERT)
- define Big Bird
- define medical data records
- define medical decision aid system

### III. COMPUTER PROGRAM PRODUCTS, METHODS, AND COMPUTING ENTITIES

- define computer program products
- describe software components
- specify programming languages
- explain conversion of programming languages
- describe storage of software components
- define non-transitory computer-readable storage medium
- list examples of non-volatile computer-readable storage media
- list examples of volatile computer-readable storage media
- describe implementation as methods, apparatus, systems, computing devices, computing entities
- explain execution of instructions on computer-readable storage medium
- describe embodiments as hardware, computer program products, or combination
- introduce block diagrams and flowchart illustrations
- explain implementation of blocks as computer program products, hardware, or combination
- describe sequential and parallel execution of instructions

### IV. EXEMPLARY SYSTEM ARCHITECTURE

- introduce predictive data analysis system
- describe system architecture
- define predictive data analysis requests
- describe processing of predictive data analysis requests
- introduce prediction-based actions
- describe generating prediction output user interface
- motivate existing natural language processing techniques
- describe limitations of existing techniques
- introduce masking multiple text blocks
- describe generating predictive data output
- introduce expected number of times a given text block is masked
- describe impact of each text block on each label prediction
- describe reducing computational operations needed
- describe reducing training data entries needed
- introduce communication networks
- describe predictive data analysis system communication
- introduce predictive data analysis computing entity
- describe predictive data analysis computing entity functions
- introduce storage subsystem
- describe storage subsystem functions
- introduce data assets
- describe data about computed properties
- introduce non-volatile storage or memory media
- describe non-volatile storage or memory media types
- introduce predictive data analysis computing entity architecture
- describe processing element functions
- introduce non-volatile media
- describe non-volatile media types
- introduce volatile media
- describe volatile media types
- introduce communications interfaces
- describe communication protocols
- introduce input elements
- describe input elements types
- introduce output elements
- describe output elements types
- introduce client computing entity
- describe client computing entity functions
- introduce antenna
- describe transmitter functions
- introduce receiver
- describe processing element functions
- introduce network interface
- describe client computing entity communication protocols

### V. EXEMPLARY SYSTEM OPERATIONS

- introduce predictive analysis with respect to text-based machine learning model
- describe process for performing predictive analysis
- receive classification labels associated with document data objects
- receive document data objects from client computing entity or predictive data analysis computing entity
- describe document data objects
- describe document classification machine learning model
- fine-tune language machine learning model
- train language classification machine learning model on training document data objects
- generate unmasked label probability score for each classification label
- perform classification for document data object using document classification machine learning model
- segment document data object into text blocks
- describe text block size measures
- select text block size measure
- segment document data object into text blocks of text block size K
- describe text block size configurations
- generate per-iteration masked label probability scores for document data object
- perform classification routine iterations
- describe classification routine iteration
- mask one or more text blocks of document data object
- generate per-masked classification of document data object
- generate per-iteration masked label probability scores
- describe required number of classification routine iterations
- determine required number of classification routine iterations based on expected text block masking count J and text block masking probability P
- describe text block masking probability P
- describe expected text block masking count J
- perform required number of classification routine iterations
- mask each text block at least J times
- describe optimization techniques for determining optimal masking probability
- describe process for performing classification routine iteration
- selectively mask one or more text blocks of document data object
- generate per-masked classification of document data object
- generate per-iteration masked label probability scores
- describe per-masked classification of document data object
- perform prediction inference operations on masked document data object
- generate classification prediction for each classification label
- describe classification prediction for each classification label
- perform classification routine iteration with respect to classification label
- perform classification routine iteration with respect to plurality of classification labels
- generate classification prediction for each of plurality of classification labels
- describe advantages of techniques described herein
- improve predictive accuracy without harming training speed
- improve efficiency and speed of training predictive machine learning models
- reduce number of computational operations needed
- reduce amount of training data entries needed
- improve at least one of computational efficiency, storage-wise efficiency, and speed of training predictive machine learning models
- describe tradeoff between predictive accuracy and training speed
- describe importance of improving training speed without sacrificing predictive accuracy
- conclude exemplary system operations
- introduce predictive data analysis computing entity
- generate per-label text block importance scores
- generate per-label masked label probability scores
- compare per-label masked label probability scores with unmasked label probability scores
- generate per-label text block importance scores based on comparison
- generate non-label-specific text block importance scores
- generate predictive data output based on text block importance scores
- compare per-label text block importance scores and non-label-specific text block importance scores
- rank text blocks based on importance scores
- generate predictive data output based on ranked text blocks
- perform prediction-based actions based on predictive data output
- determine relative importance of group of text blocks
- generate per-label pairwise text block importance scores
- identify per-iteration masked label probability scores for pair of text blocks
- generate per-label pairwise masked label probability scores
- compare per-label pairwise masked label probability scores with unmasked label probability scores
- generate per-label pairwise text block importance scores based on comparison
- generate non-label-specific pairwise text block importance scores
- determine distance between pair of text blocks
- measure association between text block distance and importance measure
- improve predictive accuracy of document classification machine learning model
- improve computational efficiency of training predictive machine learning models
- improve speed of training predictive machine learning models
- reduce number of computational operations needed to train predictive machine learning models
- reduce amount of training data entries needed to train predictive machine learning models
- generate per-label text block importance scores for multiple classification labels
- generate non-label-specific text block importance scores for multiple classification labels
- compare per-label text block importance scores for multiple classification labels
- rank text blocks based on importance scores for multiple classification labels
- generate predictive data output based on ranked text blocks for multiple classification labels
- perform prediction-based actions based on predictive data output for multiple classification labels
- determine relative importance of group of text blocks for multiple classification labels
- generate per-label pairwise text block importance scores for multiple classification labels
- identify per-iteration masked label probability scores for pair of text blocks for multiple classification labels
- generate per-label pairwise masked label probability scores for multiple classification labels
- compare per-label pairwise masked label probability scores with unmasked label probability scores for multiple classification labels
- generate per-label pairwise text block importance scores based on comparison for multiple classification labels
- generate non-label-specific pairwise text block importance scores for multiple classification labels
- determine distance between pair of text blocks for multiple classification labels
- measure association between text block distance and importance measure for multiple classification labels
- improve predictive accuracy of document classification machine learning model for multiple classification labels
- improve computational efficiency of training predictive machine learning models for multiple classification labels
- improve speed of training predictive machine learning models for multiple classification labels
- reduce number of computational operations needed to train predictive machine learning models for multiple classification labels
- reduce amount of training data entries needed to train predictive machine learning models for multiple classification labels
- generate p-value for text block importance scores
- determine relative importance of text blocks within a document data object

## VI. CONCLUSION

- summarize scope of disclosure

