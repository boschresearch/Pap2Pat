# DESCRIPTION

## BACKGROUND

- motivate technical challenges

## BRIEF SUMMARY

- introduce method
- generate unmasked label probability scores
- segment document data objects
- perform classification routine iterations
- generate predictive data output
- perform prediction-based actions

## DETAILED DESCRIPTION

- introduce predictive data analysis computing entity

### I. OVERVIEW AND TECHNICAL IMPROVEMENTS

- motivate technical contributions
- describe tradeoff between predictive accuracy and training speed
- introduce techniques for improving predictive accuracy and training speed
- summarize benefits of techniques

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

### III. COMPUTER PROGRAM PRODUCTS, METHODS, AND COMPUTING ENTITIES

- define computer program products
- describe software components
- list programming languages
- explain storage of software components
- describe non-transitory computer-readable storage media
- describe volatile computer-readable storage media
- summarize embodiments as methods, apparatus, systems, computing devices, computing entities

### IV. EXEMPLARY SYSTEM ARCHITECTURE

- introduce predictive data analysis system
- describe system architecture
- define predictive data analysis requests
- describe processing of predictive data analysis requests
- introduce prediction-based actions
- motivate masking multiple text blocks
- describe limitations of existing natural language processing techniques
- introduce expected number of times a given text block is masked
- describe impact of each text block on each label prediction
- summarize benefits of disclosed techniques
- introduce predictive data analysis computing entity
- describe communication with client computing entities
- introduce storage subsystem
- describe storage of input data and model definition data
- introduce predictive data analysis computing entity architecture
- describe processing element
- introduce non-volatile media
- describe storage of databases and applications
- introduce volatile media
- describe storage of databases and applications
- introduce communications interfaces
- describe communication with various computing entities

### V. EXEMPLARY SYSTEM OPERATIONS

- motivate predictive accuracy and computational efficiency
- describe tradeoff between predictive accuracy and training speed
- introduce document classification machine learning model
- describe process for performing predictive analysis
- receive classification labels and document data objects
- describe document data objects and classification labels
- fine-tune language machine learning model
- generate unmasked label probability scores
- segment document data objects into text blocks
- describe text block size and order
- generate per-iteration masked label probability scores
- describe classification routine iterations
- mask one or more text blocks
- generate per-masked document classification
- generate per-iteration masked label probability scores
- describe required number of classification routine iterations
- determine required number of iterations based on expected text block masking count and text block masking probability
- perform required number of classification routine iterations
- selectively mask one or more text blocks
- generate per-masked classification of document data object
- generate one or more per-iteration masked label probability scores
- perform prediction inference operations on masked document data object
- generate classification prediction for each classification label
- conclude predictive analysis
- introduce predictive data analysis computing entity
- generate per-label text block importance scores
- generate per-label masked label probability scores
- compare per-label masked label probability scores with unmasked label probability scores
- generate per-label text block importance scores based on comparison
- generate non-label-specific text block importance scores
- generate predictive data output based on text block importance scores
- compare per-label text block importance scores and/or non-label-specific text block importance scores
- rank text blocks based on importance scores
- generate predictive data output based on ranked text blocks
- generate z-scores for text block importance scores
- compare text block importance scores to average importance scores
- generate predictive data output based on compared importance scores
- determine relative importance of text blocks
- generate per-label pairwise text block importance scores
- generate per-label pairwise masked label probability scores
- compare per-label pairwise masked label probability scores with unmasked label probability scores
- generate per-label pairwise text block importance scores based on comparison
- generate non-label-specific pairwise text block importance scores
- determine distance between text blocks
- measure association between text block distance and importance measure
- perform prediction-based actions based on predictive data output
- improve predictive accuracy, computational efficiency, and speed of machine learning language models

## VI. CONCLUSION

- scope of disclosure

