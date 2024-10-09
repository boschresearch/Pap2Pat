# DESCRIPTION

## CROSS REFERENCES

- claim priority

## TECHNICAL FIELD

- define technical field

## BACKGROUND

- motivate abstractive summarization
- limitations of prior approaches

## DETAILED DESCRIPTION

- define network and module
- introduce hallucination in abstractive summarization models
- describe types of hallucinations
- discuss impact of training data quality on hallucinations
- introduce Contrastive Parameter Ensembling (CaPE) framework
- describe base summarization model
- describe expert summarization model
- describe anti-expert summarization model
- describe ensembling parameters of three models
- discuss advantages of CaPE framework
- describe FIG. 1
- introduce factual metrics (entity overlap and DAE)
- describe scoring data samples based on factual metrics
- select noisy data samples
- select clean data samples
- describe ensembling final parameters
- introduce mixing coefficient
- describe alternative ensembling methods
- discuss final summarization model
- describe use of XSUM and CNN/DM datasets
- introduce computer and network environment
- describe computing device architecture
- describe Summarization module and its submodules
- describe networked system for implementing Summarization framework

### Computer and Network Environment

- introduce computing device
- describe processor and memory
- describe machine-readable media
- describe arrangement of processor and memory
- introduce data interface
- describe input and output data
- introduce Summarization module
- describe Base Training module
- describe Data Filtering module
- describe Fine-Tuning module
- describe Mixing Experts module
- describe executable code
- introduce networked system
- describe user device
- describe data vendor servers
- describe server
- describe network
- describe user interface application
- describe other applications
- describe database
- describe network interface component
- describe data vendor server
- describe database
- describe network interface component
- describe server
- describe Summarization module
- describe database
- describe network interface component

### Example Workflows

- illustrate algorithm for CaPE Summarization
- provide logic flow diagram for CaPE Summarization
- implement processes in executable code
- receive training dataset with documents and summaries
- train base summarization model using all samples
- select clean samples using factual metric
- select noisy samples using factual metric
- fine-tune base model using clean training dataset
- fine-tune base model using noisy training dataset
- combine parameters of base and expert models
- combine parameters of base and anti-expert models
- return final summarization model
- store final summarization model in database
- send final summarization model to user device
- illustrate performance of different summarization models
- train expert model for DAE error metric
- train anti-expert model for DAE error metric
- train expert model for entity token overlap precision
- train anti-expert model for entity token overlap precision
- evaluate four variants of CaPE
- define variables for performance metrics
- illustrate validation performance comparison of BART models
- illustrate performance comparison of CaPE and baseline models
- illustrate performance comparison of CaPEDP and base models
- illustrate performance comparison of individual expert and anti-expert models
- illustrate variations in performance with different mixing coefficients
- illustrate average summary lengths of training data
- illustrate variations in performance on CNN/DM data
- illustrate performance comparison of fine-tuning vs training BART model
- illustrate performance comparison of CaPE, expert, and anti-expert models

