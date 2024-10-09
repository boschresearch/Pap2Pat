# DESCRIPTION

## BACKGROUND

- introduce antibodies and affinity levels

## SUMMARY

- introduce method for identifying antibody amino acid sequence
- receive initial amino acid sequence
- query machine learning engine
- receive proposed amino acid sequence
- identify proposed amino acid sequence
- query machine learning engine successively
- train machine learning engine
- predict affinity level
- compare predicted affinity level
- train machine learning engine based on comparison
- identify region of initial amino acid sequence
- introduce method for identifying series of discrete attributes
- introduce method for identifying amino acid sequence for protein interaction

## DETAILED DESCRIPTION

- introduce antibody affinity identification techniques
- describe machine learning engine for affinity prediction
- train machine learning engine using affinity information
- query machine learning engine with known amino acid sequence
- output proposed amino acid sequence with higher predicted affinity
- describe limitations of conventional antibody development techniques
- introduce targeted antibody synthesis using machine learning engine
- describe advantages of targeted antibody synthesis
- identify amino acid sequence for antibody with predicted affinity
- synthesize and screen antibody with predicted affinity
- update machine learning engine with new affinity information
- describe iterative process for discretization of optimized values
- convert continuous representation to discrete representation
- input discrete representation into machine learning engine
- describe optimization process for machine learning engine
- select highest-value amino acid for each residue
- describe application to other protein-protein interactions
- train machine learning engine for different protein interactions
- query machine learning engine for proposed amino acid sequence
- receive output series of discrete attributes
- identify discrete version of output series
- describe iterative process for identifying proposed amino acid sequence
- stop iterative process when output series matches prior output series
- describe identifying proposed amino acid sequence with multiple quality metrics
- train machine learning engine with data associated with multiple characteristics
- generate model with parameters representing relationships between quality metrics
- estimate values for parameters using scores assigned during training
- describe application to different embodiments
- illustrate amino acid identification system with machine learning engine
- describe training facility, optimization facility, and identification facility
- define denoising of training data
- motivate replicates of assay
- describe quality metric information
- introduce machine learning engine
- describe training facility
- motivate proposed amino acid sequences
- describe identification facility
- introduce continuous representation
- describe discretization process
- motivate selection of amino acids
- describe iterative process
- introduce subsequent training
- describe protein interaction data
- motivate affinity data
- describe process 200
- receive amino acid sequences and quality metrics
- train machine learning engine
- receive initial amino acid sequences
- query machine learning engine
- receive proposed amino acid sequences
- describe process 300
- query machine learning engine
- receive values associated with amino acids
- select amino acids
- describe process 400
- train machine learning engine using proposed amino acid sequence

### Illustrative Embodiments

- introduce high-throughput methodology for designing antibodies
- motivate computational methods for antibody design
- describe iterative framework for identifying effective antibodies
- summarize application of machine learning models for antibody design
- propose using phage display for high-throughput affinity testing
- describe training machine learning models from observed affinity data
- outline iterative loop of antibody testing, model training, and design
- discuss using oligonucleotide synthesis for creating and testing antibodies
- describe using machine learning models to predict antibody affinity and specificity
- outline framework for developing computational models for antibody design
- describe using deep learning methods for antibody engineering
- motivate using convolutional neural networks for antibody sequence analysis
- describe optimizing antibody sequences using gradient-based methods
- outline method for recognizing and segmenting antibody VHH sequences

## EXAMPLES

- introduce phage display affinity experiments
- describe antibody library derivation
- sequence antibody repertoire
- parse DNA sequencing reads
- analyze frequency of observed complete CDR sequences
- train CNN using non-binders and mid-binders
- examine performance of CNN architectures
- analyze performance of K-nearest neighbors algorithm
- apply CNN-based models to published dataset
- predict binding affinity to influenza hemagglutinin
- propose novel antibody sequences with higher affinity
- verify novel sequences with higher predicted affinity
- produce novel sequences with high affinity for first target and low affinity for second target
- validate potential of method to propose novel antibody sequences

### Example Computer-Implemented Embodiments

- introduce computing device
- describe components of computing device
- explain network adapter
- describe computer-readable storage media
- explain processor
- describe data and instructions
- illustrate computing device 1900
- describe components of computing device 1900
- explain network adapter 1904
- describe computer-readable storage media 1906
- explain processor 1902
- describe data and instructions stored on computer-readable storage media 1906
- describe facilities stored on computer-readable storage media 1906
- explain input and output devices
- describe implementation of embodiments
- explain hardware and software implementation
- describe controller implementation
- explain network implementation
- describe computer-readable storage medium

