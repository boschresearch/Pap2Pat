# DESCRIPTION

## BACKGROUND

- motivate speech processing models

## SUMMARY

- introduce wav2seq method
- compute feature vectors
- determine pseudo tokens
- train first neural network
- train second neural network
- deploy second neural network
- describe variations of method

## DETAILED DESCRIPTION

- introduce speech processing models
- motivate self-supervised learning
- describe pseudo tokens
- outline method for training speech processing model using pseudo tokens
- determine set of pseudo tokens using unlabeled training data
- train first speech processing model using pseudo tokens and unlabeled training data
- train second speech processing model using labeled training data
- fine-tune second speech processing model
- deploy second speech processing model
- describe system for determining set of pseudo tokens
- compute feature vectors from audio data
- perform clustering on feature vectors
- generate cluster tokens
- perform deduplication on cluster tokens
- perform token compression
- describe system for determining sequences of pseudo tokens
- reuse clusters to generate cluster tokens
- replace cluster tokens with pseudo tokens
- describe system for training encoder-decoder neural network using pseudo tokens
- describe system for fine-tuning encoder-decoder neural network using labeled training data
- describe transformer encoder
- describe transformer decoder
- describe output token layers
- describe output token embedding component
- describe audio encoding component
- describe output token prediction component
- describe joint network
- describe output token layers component
- introduce training method
- obtain first training corpus
- compute feature vectors
- determine pseudo tokens
- determine pseudo-token sequences
- train first neural network
- obtain second training corpus
- train second neural network
- deploy second neural network
- describe method for determining pseudo tokens
- obtain first training corpus
- compute feature vectors
- cluster feature vectors
- determine cluster-token sequences
- perform token compression
- describe computing device components
- describe feature vector computation component
- describe clustering component
- describe cluster tokenization component
- describe token compression component
- describe token replacement component

