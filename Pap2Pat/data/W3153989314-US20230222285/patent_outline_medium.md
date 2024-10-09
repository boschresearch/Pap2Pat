# DESCRIPTION

## FIELD

- relate to document processing

## BACKGROUND

- motivate limitations of existing document representation models

## SUMMARY

- introduce layout-aware document representation model
- describe method for generating layout-aware document representations
- partition document into blocks based on layout data
- process blocks with machine-learned block-level encoder model
- generate block-level representations
- process block-level representations with machine-learned document-level encoder model
- generate document-level representation
- provide document-level representation as output
- describe applications of document-level representation
- introduce computing system for generating layout-aware document representations
- describe operations performed by computing system
- introduce pretraining method for machine-learned block-level encoding model

## DETAILED DESCRIPTION

### Overview

- introduce document understanding systems and methods
- describe hierarchical encoder model
- motivate layout-aware document representations
- summarize document processing steps
- describe block-level encoder model
- explain document-level encoder model
- motivate multimodal transformer
- describe block tokenizer
- explain block sorting and serialization
- describe intra-block processing
- describe inter-block processing
- motivate training objectives
- describe block-ordering prediction
- describe block masked learning
- describe image suggestion prediction
- describe document-level attention mask
- describe pre-training techniques
- describe model variants and baselines
- summarize technical benefits

### Example Devices and Systems

- introduce computing system 100
- describe user computing device 102
- detail user computing device components
- introduce document processing models 120
- describe neural networks
- explain model training methods
- introduce server computing system 130
- describe server computing system components
- introduce document processing models 140
- describe user input component 122
- introduce training computing system 150
- describe training computing system components
- introduce model trainer 160
- explain backwards propagation of errors
- describe generalization techniques
- introduce training data 162
- describe model personalization
- introduce network 180

### Example Model Arrangements

- utilize layout to understand document
- obtain layout by in-house document parsing tool
- tokenize web page-document into content blocks
- define block position with 2D real valued coordinates
- normalize XY coordinates to ∈[0,1]
- define block type with semantic type of content
- define block attributes for blocks with textual contents
- generate attributes with font-size and binary values
- include multimedia contents in blocks
- prepare input representation to models by sorting blocks
- serialize blocks in zigzag fashion
- model hierarchical formulation of document layouts
- exploit structure alongside contents to generate representation
- include two cascaded transformers for different levels of inputs
- take raw parsed contents as inputs for block-level model
- prepend CLSi special token for indicating boundary of block contents
- prepend global-CLS token at beginning of inputs
- take block-level representations as inputs for document-level model
- tokenize textual input contents with WordPiece tokenizer
- attach block-segment-id to each block
- map and round font-size to integer scalar ∈[0, 10]
- represent boldness, underline, and italic as binary values
- supplement binary embedding indicating modality
- define overall input representation for each token position

### Example Methods

- introduce document processing method
- obtain document
- partition document into blocks
- process blocks to generate block-level representations
- process block-level representations to generate document-level representation
- provide document-level representation as output
- introduce pretraining method
- obtain media training blocks
- evaluate pre-training loss function

### Example Experimental Data

- introduce experimental questions
- design document completion tasks
- describe text block filling task
- describe image suggestion task
- fine-tune on downstream tasks
- compare to single-level layout language model
- compare to CNN-Grid model
- analyze model performances on downstream tasks

## Additional Disclosure

- clarify flexibility of computer-based systems

