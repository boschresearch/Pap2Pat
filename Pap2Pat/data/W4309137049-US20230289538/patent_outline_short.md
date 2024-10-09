# DESCRIPTION

## BACKGROUND

- describe code-switching problem

## BRIEF SUMMARY

- introduce technology for generating synthetic code-switched data
- train first language model to translate single-language utterances
- generate synthetic code-switched data using first language model
- train semantic parser using synthetic data
- leverage accrued knowledge to generate large amounts of training data
- improve language model performance with less human-annotated data

## DETAILED DESCRIPTION

- describe processing system architecture

### Example Systems

- illustrate system diagram
- describe system components
- explain system communication

### Example Methods

- introduce flow diagram for generating trained language model
- describe set of first training examples
- generate training seed set using human annotators
- train first language model using training seed set
- generate synthetically generated code-switched utterances and parsing data
- associate labels with synthetically generated code-switched utterances and parsing data
- collect synthetically generated code-switched utterances and parsing data to form set of second training examples
- train semantic parser using set of second training examples
- describe method for generating code-switched semantic parsing training data
- select given first training example and perform steps for that example
- translate first text sequence into code-switched text sequence
- generate second parsing data associating identifiers with spans of text
- generate second training example based on second text sequence and second parsing data
- generate third parsing data
- include third parsing data in second training example
- generate training set from second training examples
- train second semantic parser based on training set
- filter training set based on span count
- filter training set based on identifier lists
- train second semantic parser based on filtered training set

