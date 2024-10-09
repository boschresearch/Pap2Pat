# DESCRIPTION

## FIELD OF THE INVENTION

- relate to artificial intelligence

## BACKGROUND

- introduce summarization systems
- limitations of conventional systems
- motivate affective summarization

## SUMMARY

- introduce affective summarization system
- describe system components

## DETAILED DESCRIPTION

- introduce affective text summarization
- limitations of conventional summarization systems
- benefits of affective text summarization
- define affective text summarization
- describe affective summarization system
- introduce neural networks in summarization
- describe affect predictor subnetwork
- describe embeddings generator
- describe summarization subnetwork
- define affect
- describe affective preferences
- define neural network
- define embeddings
- describe text document
- introduce computing system
- describe affective summarization system components
- describe training data
- describe affect predictor neural network
- describe summarization neural network
- describe interactions between subnetworks
- describe output of affective summarization system
- introduce user device
- describe user interface
- describe selected affect
- describe affective summarization system training
- describe training neural networks individually
- describe training neural networks together
- describe modified training dataset
- introduce FIG. 1
- describe computing system components
- describe affective summarization system components
- describe user device components
- introduce FIG. 2
- describe process for generating affective text summary
- receive text document
- receive affect level
- extract embeddings sequence
- determine encoding of words
- generate affective text summary
- output affective text summary
- introduce FIG. 3
- describe untrained subnetworks
- describe training datasets
- train affect predictor subnetwork
- train summarizer subnetwork
- describe modified training dataset
- train embeddings generator
- train encoder and decoder
- introduce FIG. 4
- describe trained subnetworks
- describe interactions between subnetworks
- generate predicted affect level
- generate embeddings sequence
- generate affective text summary

### Training a Predictor Neural Network

- introduce predictor neural network training
- describe unmodified predictor training dataset
- define affect score
- explain Equation 1
- normalize affect scores
- determine discrete affect levels
- generate modified predictor training dataset
- explain Equation 2
- train predictor neural network
- describe function MA(x)
- explain Equation 3
- train function MA(x) on modified dataset
- introduce process 500 for training predictor neural network
- receive predictor training dataset
- generate discrete affect levels and modify dataset

### Training a Summarization Neural Network

- introduce summarization neural network training
- describe unmodified summarization training dataset
- define article word sequences and summary word sequences
- explain affective properties in unmodified training set
- provide example of unmodified training set equation
- describe article sequences and summary sequences in dataset
- explain additional data in article sequences and summary sequences
- generate information about affects of summary word sequences
- describe embeddings sequence generation
- define modified summarization training dataset
- explain embeddings function generation
- describe training embeddings function
- explain affect level prediction
- describe embeddings generator training
- explain modified dataset generation
- describe summarization neural network training
- explain affective summary generation
- describe feedback reception for generated affective summary
- introduce process for training summarization neural network
- receive summarization training dataset
- receive discrete affect levels
- train embeddings function
- generate embeddings sequences
- modify summarization training dataset
- train summarization neural network
- describe repeated operations for process
- introduce affective summarization system
- describe computing system components
- explain memory device storage
- describe network interface and remote system connection

## GENERAL CONSIDERATIONS

- set forth specific details
- omit obvious details
- define computing terms
- describe computing devices
- discuss method variations
- claim scope disclaimer

