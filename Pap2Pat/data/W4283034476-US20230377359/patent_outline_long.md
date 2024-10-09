# DESCRIPTION

## BACKGROUND

- introduce domain shift problem
- describe real-world VDU applications

## SUMMARY

- introduce disclosed technology
- train machine learning model
- determine distribution shift
- apply masked visual language modeling
- generate pseudo-labels
- adapt machine learning model
- process target domain data
- describe variations of disclosed technology

## DETAILED DESCRIPTION

- introduce test-time adaptation technique for VDU tasks
- describe masked visual language modeling
- explain pseudo-labeling with uncertainty-aware selection mechanism
- introduce benchmarks for VDU tasks
- describe implementation as methodology, method, or process
- explain document test-time adaptation
- discuss unsupervised domain adaptation methods
- introduce test-time adaptation methods
- highlight limitations of existing TTA approaches
- describe process 200
- receive input document or second data set
- feed input document to model trained on first data set
- detect domain or distribution shift event
- adapt model to account for shift
- define framework for DocTTA methodology and system
- describe source and target domains
- explain goal of TTA
- illustrate process flow 300 of DocTTA
- describe OCR parser
- tokenize words and divide document image into patches
- apply MVLM algorithm
- generate pseudo-labels using model's predictions
- maximize diversity of predictions
- construct input X
- describe MVLM objective function
- explain self-training with pseudo-labels
- describe uncertainty-aware selection mechanism
- combine objective functions for DocTTA
- formulate DocTTA procedure as algorithm
- compute entropy of predictions
- discard untrustworthy pseudo-labels
- adapt input document with correct pseudo-labels
- feed back correct pseudo-labels to train document model
- process target streams with unlabeled data
- introduce new benchmarks for VDU
- construct entity recognition benchmark
- split source and target documents based on sparsity
- describe FUNSD dataset
- describe SROIE dataset
- describe DocVQA dataset
- create adaptation benchmark for document VQA
- describe computing device for carrying out disclosed technology
- describe memory and processing element of computing device
- describe instructions and data stored in memory
- describe processing element as processor or ASIC
- describe memory as non-transitory computer-readable medium
- describe instructions as set of executable steps
- describe data as retrieved, stored, or modified by processor
- describe modules as software components
- describe input/output ports of computing device
- describe system in distributed computing environment
- describe computing devices in system
- describe storage in system
- describe network in system
- describe cloud computing systems in system
- describe computing device as standalone computer or server
- describe display and input system of computing device
- describe communication interface of computing device
- describe network protocols and configurations
- describe cloud computing systems as data centers
- describe infrastructure, storage, and computer system of cloud computing system
- describe computer system as supervisor or managing agent
- describe scope of invention

