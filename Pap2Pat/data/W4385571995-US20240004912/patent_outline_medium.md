# DESCRIPTION

## TECHNICAL FIELD

- define topic models

## BACKGROUND

- limitations of flat topic models

## SUMMARY

- generate hierarchical topic model
- application of HTM to custom content generation

## DETAILED DESCRIPTION

- motivate hierarchical topic models
- limitations of existing HTMs
- introduce interpretable HTMs
- describe topic modeling system
- determine first-level topics
- identify second-level topics
- recursively define additional levels
- assign documents to topics
- generate custom content
- describe content customization system
- introduce topic modeling system components
- describe document analysis subsystem
- describe clustering subsystem
- describe hierarchy finder subsystem
- describe topic definition subsystem
- illustrate HTM generation process
- describe process for generating HTM
- compute document-topic matrix and topic-word matrix
- define first-level topics
- assign documents to first-level topics
- select first-level topic for consideration
- cluster words of first-level topic into clusters
- generate semantic relations matrix for first-level topic
- generate statistical relations matrix for first-level topic
- compute document-topic matrix and topic-word matrix for first-level topic
- define second-level topics
- assign documents to second-level topics
- determine whether anymore first-level topics remain
- iterate over first-level topics to generate additional levels of topics
- access words of a topic
- identify top words in the topic
- determine respective embedding for each top word
- apply clustering technique to word embeddings
- describe process for computing document-topic matrix and topic-word matrix
- initialize topic-word matrix based on clusters
- compute similarity between each pair of words
- compute hierarchical relations matrix
- multiply statistical relations matrix by semantic relations matrix
- multiply product by hierarchical relations matrix
- perform matrix factorization to produce document-topic matrix and topic-word matrix
- describe example of content generation system
- receive indication of access to document
- determine where document falls within HTM
- identify other documents having topics in common with document
- generate custom content for user
- transmit custom content to client
- describe example of computing system for implementing embodiments
- execute program code on processor
- access models, datasets, or functions of topic modeling system
- store models, datasets, and functions on memory device
- provide access to necessary models, datasets, and functions
- establish data connection to one or more data networks
- communicate with other computing devices via data network
- discuss general considerations for claimed subject matter
- provide disclaimer for patent application

