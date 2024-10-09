# DESCRIPTION

## FIELD

- relate to document processing

## BACKGROUND

- introduce document representations
- limitations of existing models
- importance of layout and images

## SUMMARY

- introduce layout-aware document representations
- obtain document with text and images
- associate layout data with document
- partition document into blocks
- process blocks with block-level encoder model
- generate block-level representations
- process block-level representations with document-level encoder model
- generate document-level representation
- provide document-level representation as output
- include style, font, or color data in layout data
- include spatial layout data in layout data
- partition document based on HTML tags
- process blocks with both textual and image content
- process images with convolutional neural network and embedding model
- include multi-headed self-attention model in encoder models
- partition document using tokenizer
- process document-level representation for classification
- process document-level representation with search engine
- generate document summary
- encode layout data in attention maps
- include position data in layout data
- train block-level encoder model with block-level pretraining objectives
- train document-level encoder model with document-level pretraining objectives
- store document-level representation in database
- evaluate loss function and modify encoder model parameters

## DETAILED DESCRIPTION

### Overview

- introduce document understanding
- describe hierarchical encoder model
- explain layout information
- motivate layout-aware document representations
- describe obtaining a document
- explain partitioning document into blocks
- describe block-level encoder model
- explain processing block-level representations
- describe document-level representation
- motivate downstream tasks
- describe training techniques
- explain pre-training objectives
- describe block-level transformer
- explain document-level transformer
- describe block-level pre-training objectives
- explain block-order predictions
- describe masked-block predictions
- explain image fitting predictions
- describe partitioning document into blocks
- explain using HTML cues
- describe using spatial layout
- explain hierarchical model
- describe block-level encoding
- explain document-level encoding
- describe using document-level representation
- explain training techniques
- describe pre-training tasks
- explain self-supervisions
- describe using tokenizer
- explain block tokenizer
- describe processing text blocks and image blocks
- explain using visual-linguistic transformer
- describe training objectives
- explain block-level training objectives
- describe document-level training objectives
- explain block sorting step
- describe processing inputs
- explain using attention masks
- describe using multimodal alignment prediction model

### Example Devices and Systems

- introduce computing system 100
- describe user computing device 102
- detail user computing device components
- introduce document processing models 120
- describe types of document processing models
- explain model training methods
- introduce server computing system 130
- describe server computing system components
- introduce document processing models 140
- describe types of document processing models
- introduce user input component 122
- describe user input component
- introduce training computing system 150
- describe training computing system components
- introduce model trainer 160
- describe model trainer functionality
- introduce training data 162
- describe training data
- explain personalizing models
- introduce network 180
- describe network components
- introduce machine-learned model applications
- describe text or natural language data processing
- describe latent encoding data processing
- describe statistical data processing
- introduce encoding input data
- describe computer vision tasks
- describe image processing tasks
- introduce FIG. 1A
- describe alternative computing system implementations
- introduce FIG. 1B
- describe computing device 10 components
- describe application communication
- introduce FIG. 1C
- describe computing device 50 components
- describe central intelligence layer functionality

### Example Model Arrangements

- utilize layout to understand document
- obtain layout by in-house document parsing tool
- tokenize web-page document into content blocks
- define block position with 2D real-valued coordinates
- normalize XY coordinates to ∈[0,1]
- define block type with semantic type of content
- define 14 different block types
- define block attributes for blocks with textual contents
- generate attributes with visual presentations of text
- include multimedia contents in blocks
- define layout as structural presentation of tokenized content blocks
- prepare input representation to models by sorting blocks
- serialize blocks in zigzag fashion
- aim to model hierarchical formulation of document layouts
- exploit structure alongside contents to learn document representation
- have two levels for layout hierarchical formulation
- define lower-level as block-level, referring to block contents
- define higher-level as document-level, referring to block structure
- include two cascaded transformers taking different levels of inputs
- take raw parsed contents as inputs for block-level model
- prepend CLS special token for indicating boundary of block contents
- prepend global-CLS token at beginning of inputs
- take block-level representations as inputs for document-level model
- tokenize textual input contents by WordPiece tokenizer
- attach block-segment-id to each block
- map and round font-size to integer scalar ∈[0, 10]
- represent boldness, underline, and italic as binary values
- supplement binary embedding indicating modality
- define overall input representation for each token position
- leave design choice to truncate block contents with maximally allowed token length
- feed image contents to convolutional neural network (CNN)
- transform visual embedding to same size of textual token embedding
- pad inputs with zero-image tensors for documents without images
- adjust attention mask in block-level model not to attend to padded inputs
- aim to capture finer-grained linguistics, visual information, and multimodal inputs
- apply masked language modeling (MLM) objective
- adapt image-text matching (ITM) prediction
- sample candidate images from other documents during training
- swap images with certain probabilities
- prompt model to predict whether textual contents match resulting image sequences
- include block-ordering predictions (B-ORD) objective
- include block-MLM (B-MLM) objective
- include image fitting (IMG-FIT) objective
- jointly train with low and high-level objectives
- define linear combination of losses
- depict block diagram of example document processing model
- process document with one or more text blocks and one or more image blocks
- generate document-level representation for downstream tasks

### Example Methods

- introduce document processing method
- obtain document
- partition document into blocks
- process blocks to generate block-level representations
- process block-level representations to generate document-level representation
- provide document-level representation as output
- introduce pretraining method
- obtain media training blocks
- mask images in media training blocks
- process media training blocks to obtain media block representations
- evaluate pre-training loss function
- adjust model parameters based on pre-training loss function
- introduce document processing training method
- obtain document
- partition document into blocks
- process blocks to generate block-level representations
- process block-level representations to generate document-level representation
- evaluate loss function based on prediction
- modify model parameters based on loss function

### Example Experimental Data

- introduce experimental questions
- design document completion tasks
- describe text block filling task
- describe image suggestion task
- introduce fine-tuning on downstream tasks
- describe document-level representation
- introduce contrastive loss function
- compare to single-level layout language model
- describe CNN-Grid model
- describe unimodality (text-only) experiment
- introduce model initialization
- describe image encoding
- describe pretraining objectives
- introduce Wikipage dataset
- describe dataset preprocessing
- introduce evaluation metrics
- summarize model performances

## Additional Disclosure

- discuss system flexibility
- clarify non-limiting examples
- allow for variations

