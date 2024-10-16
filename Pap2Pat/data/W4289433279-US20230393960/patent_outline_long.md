# DESCRIPTION

## BACKGROUND

- motivate machine learning

## SUMMARY

- introduce fairness deviation constraint
- application of decision matrix
- enforce fairness deviation constraint
- flexibility of fairness constraint

## DETAILED DESCRIPTION

- introduce bias correction system
- limitations of conventional systems
- type-1 and type-2 errors in conventional systems
- illustrate conventional system limitations
- equalized odds or equalized opportunity in conventional systems
- limitations of equalized odds or equalized opportunity
- conventional systems are inefficient
- multiple sanitations in conventional systems
- undermine privacy, security, flexibility, and fidelity in conventional systems
- introduce fairness deviation constraint
- relaxed equality condition for false positive rates and true positive rates
- determine mean performance rate
- determine standard deviation of performance
- impose fairness deviation constraint
- learn decision matrix
- decision matrix includes decision thresholds
- iteratively analyze performance rates
- modify decision thresholds
- apply decision matrix to machine learning model
- reduce bias in machine learning model predictions
- extract features/values from sample
- generate classification probability
- control for bias by applying decision threshold
- analyze multiple values of multiple data attributes
- determine decision matrix for sub-populations
- utilize multiple approaches to determine decision thresholds
- reduce computational complexity
- provide options for defining fairness deviation constraints
- improve accuracy relative to conventional systems
- improve flexibility relative to conventional systems
- expand compatible values and data attributes
- improve efficiency relative to conventional systems
- reduce time and computing resources
- improve privacy, security, flexibility, and fidelity
- apply decision thresholds in a differentially private manner
- do not undermine model fidelity
- process model outputs
- apply to various machine learning model architectures
- introduce system environment
- describe client device
- describe server
- describe database
- describe network
- describe client application
- describe machine learning system
- describe bias correction system
- train machine learning models
- generate sanitized predictions
- introduce bias correction system
- operate with various predictions or classifications
- generate decision thresholds for each class or prediction type
- operate across different values and attributes
- determine new set of values for attributes
- utilize machine learning model to generate new classification probabilities
- determine new decision threshold particular to new set of values
- generate new sanitized classification
- operate in relation to samples that do not correspond to client devices or users
- operate with regard to various digital inputs
- iteratively modify decision thresholds to generate decision matrix
- initialize decision matrix
- utilize various approaches to generate initial decision threshold values
- select randomized values for initial decision thresholds
- determine classifications for samples utilizing machine learning model and decision matrix
- generate classification probabilities
- utilize decision matrix to generate classifications
- compare classification probabilities with decision thresholds
- generate classifications
- determine machine learning model performance with decision matrix
- compare classifications with ground truth classifications
- determine performance rates/metrics
- determine mean and/or deviation of performance metric
- determine performance rates for individual values within data attribute
- prune decision thresholds utilizing fairness deviation constraint
- determine fairness deviation constraint
- apply fairness deviation constraint to prune certain decision thresholds
- select new decision thresholds
- utilize accuracy model to select new decision thresholds
- apply accuracy model to generate accuracy scores
- select new decision threshold based on accuracy score
- iteratively perform acts until generating decision matrix
- determine new classifications utilizing new decision matrix
- determine new performance rates for machine learning model performance with new decision matrix
- prune decision thresholds
- select new thresholds until determining that all values satisfy fairness deviation constraint
- provide user interface for flexible selection of parameters for fairness deviation constraints
- apply different fairness deviation constraint selectable elements
- utilize different fairness models
- apply fairness deviation constraint and accuracy model based on selection
- introduce bias correction system
- describe system flexibility
- illustrate fairness deviation constraints
- describe decision threshold generation
- introduce pruning data attributes
- describe dependency metric
- illustrate modifying design thresholds
- describe combining decision thresholds
- illustrate multi-dimensional decision thresholds
- describe pruning data attributes for multi-dimensional populations
- describe determining sub-populations
- illustrate pruning attributes based on sub-population numbers
- describe determining initial decision thresholds
- describe modifying decision thresholds for sub-populations
- illustrate utilizing decision thresholds for future samples
- describe sample manager
- describe fairness deviation constraint manager
- describe machine learning model manager
- describe performance metric manager
- describe decision matrix manager
- describe storage manager
- describe communication between components
- describe software and hardware components
- describe implementing components as part of an application
- describe implementing components as a cloud-computing model
- illustrate generating enhanced digital images
- describe flowchart for generating a decision matrix
- describe act of generating predicted classification probabilities
- describe act of determining fairness deviation constraint
- describe determining fairness deviation constraint by performance mean and deviation
- describe determining fairness deviation constraint by window of performance rates
- illustrate generating decision matrix for machine learning model
- describe act of generating decision matrix
- describe act of pruning data attributes
- describe act of determining sub-populations
- describe act of pruning attributes based on sub-population numbers
- describe act of determining initial decision thresholds
- describe act of modifying decision thresholds for sub-populations
- describe act of utilizing decision thresholds for future samples
- describe act of generating predicted classification probabilities
- describe act of determining fairness deviation constraint
- describe act of modifying decision thresholds
- describe act of combining decision thresholds
- describe act of utilizing decision thresholds for multi-dimensional populations
- describe act of generating sanitized predictions
- describe detailed description
- introduce act 904
- generate predicted classifications
- determine performance rate
- determine fairness deviation constraint
- determine true positive rate or false positive rate
- identify user selection of fairness deviation constraint
- generate decision matrix
- select modified decision threshold
- apply modified decision matrix
- determine accuracy score
- select modified decision threshold based on accuracy score
- provide selectable options for fairness deviation constraint
- determine fairness deviation constraint based on user interaction
- generate modified decision matrix for additional value
- determine dependency between data attributes
- prune decision thresholds
- determine sub-population
- generate modified decision matrix for sub-population
- determine number of samples for sub-population
- prune decision thresholds for sub-population
- illustrate flowchart of example sequence of acts
- describe acts of FIG. 10
- generate predicted classification probability
- determine decision threshold
- generate classification for sample
- determine first decision threshold
- determine second decision threshold
- combine decision thresholds
- describe computer-readable media
- describe non-transitory computer-readable storage media
- describe transmission media
- describe network
- describe computer-executable instructions
- describe computer system components
- describe cloud computing environments
- describe service models
- describe deployment models
- illustrate computing device
- describe processor
- describe memory
- describe storage device

