# DESCRIPTION

## FIELD

- relate machine-learned models

## BACKGROUND

- introduce templatic documents
- limitations of current techniques

## SUMMARY

- outline computer-implemented method
- describe other aspects of disclosure

## DETAILED DESCRIPTION

- introduce system for extracting information from form-like documents
- describe end-to-end trainable system using machine learning models
- explain robustness to native digital documents and scanned images
- describe machine learning model for learning dense representation
- explain generation of score for each candidate relative to field type
- describe assignment of candidates to field types based on scores
- motivate workflows for business processes with form-like documents
- describe document analysis system for identifying document types
- explain association of document types with target schemas
- describe extraction of text portions from document images
- explain determination of field types and candidate text portions
- describe generation of score for each candidate text portion
- explain selection of candidate text portion based on score
- describe transmission of selected values to central server
- outline three general principles for document analysis system
- describe pipeline stages for document ingestion and text recognition
- explain candidate generation and score generation stages
- define scorer system
- describe scorer system features
- motivate neighborhood zone
- describe neighbor text portions
- encode neighbor text portions
- calculate relative position
- embed information
- generate initial neighbor embeddings
- compute attention weight vector
- form single encoding
- describe document analysis system
- illustrate example embodiment
- describe candidate generation system
- determine target schema
- extract candidate text portions
- analyze content of text portions
- generate score for each candidate text portion
- use machine-learned model to generate score
- generate embeddings for input data
- compare embeddings to generate scores
- select candidate text portion based on scores
- assign selected text portion to field type
- store assigned values for later use
- describe text extraction system
- identify text portions
- determine content of text portions
- determine position of text portions
- determine relative position of text portions
- describe candidate selection system
- generate score values for candidate text portions
- define score model architecture
- describe initial neighbor embeddings transformation
- explain attention weight vector calculation
- detail self-attending neighbor layers encoding
- describe score model projection and normalization
- illustrate neighborhood encoding formation
- explain candidate encoding generation
- describe score calculation using cosine similarity
- illustrate document analysis system operation
- describe neighbor text portions identification
- detail multi-step document analysis model
- explain text extraction and candidate selection models
- describe method for extracting text from a form-like document
- summarize method steps and variations

