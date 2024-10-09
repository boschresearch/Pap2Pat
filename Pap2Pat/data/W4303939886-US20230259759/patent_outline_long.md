# DESCRIPTION

## FIELD

- relate to machine-learning

## BACKGROUND

- introduce sequence-to-sequence models

## SUMMARY

- motivate improved quality translation
- introduce computer-implemented method
- describe neural utility metric model
- outline computing system operations
- mention other aspects of disclosure
- reference appended claims

## DETAILED DESCRIPTION

- introduce sequence-to-sequence modeling with neural quality metrics
- motivate neural sequence-to-sequence models for machine translation
- describe limitations of existing approaches using beam search
- explain problem of less-frequently used words scoring lower
- describe decreased quality of translations produced by beam search
- introduce example aspects of the present disclosure
- motivate use of neural utility metrics for evaluating candidate translations
- describe advantages of neural utility metrics over existing metrics
- introduce BLEURT and COMET as examples of neural utility metrics
- describe how neural utility metrics can select translations that better reflect human translations
- introduce computer-implemented method for translating a source sequence with improved quality
- describe obtaining a plurality of candidate outputs based on a source sequence
- explain sampling from a machine translation model to obtain candidate outputs
- describe determining a plurality of reference utilities for each candidate output
- introduce neural utility metric model for determining reference utilities
- describe how neural utility metric model can be configured to determine utility of a candidate translation
- explain how neural utility metric model can output a utility score associated with a candidate translation
- describe examples of neural utility metric models, including BLEURT and COMET
- introduce so-called “first generation” and “second generation” neural utility metric models
- describe how BLEURT metric can be used to score how appropriate a hypothesis translation is
- explain how COMET metric can calculate a sentence embedding for a hypothesis translation
- describe determining an average utility of each candidate output
- explain how average utility can be determined by averaging reference utilities for each candidate output
- describe determining an output sequence based on average utility of each candidate output
- explain how output sequence can be selected based on highest average utility
- describe technical effects and benefits of systems and methods according to example aspects of the present disclosure
- introduce improvements to computing technology
- describe how systems and methods can provide for improved quality of machine translations
- explain how systems and methods can produce translations that are less likely by conventional approaches
- describe how neural utility metric models can provide improved performance over existing metrics
- introduce example embodiments of the present disclosure with reference to the Figures
- describe block diagram of an example computing system that performs sequence-to-sequence modeling with neural quality metrics
- introduce user computing device and its components
- describe one or more processors and memory of the user computing device
- explain how user computing device can store or include one or more machine-learned models
- describe how machine-learned models can be received from a server computing system
- introduce server computing system and its components
- describe one or more processors and memory of the server computing system
- explain how server computing system can store or include one or more machine-learned models
- describe training computing system and its components
- introduce model trainer that trains machine-learned models
- explain how model trainer can use various training or learning techniques
- describe how model trainer can perform generalization techniques
- explain how model trainer can personalize the model using user-specific data
- define model trainer
- describe hardware implementation
- describe software implementation
- describe network communication
- describe machine-learned model applications
- describe text input processing
- describe speech input processing
- describe latent encoding input processing
- describe statistical data input processing
- describe sensor data input processing
- describe encoding task
- describe decoding task
- describe embedding task
- illustrate computing system
- describe user computing device
- describe model trainer
- describe training dataset
- illustrate computing device
- describe applications
- describe machine learning library
- describe machine-learned model
- describe API communication
- describe sensor communication
- describe context manager
- describe device state component
- illustrate computing device
- describe central intelligence layer
- describe machine-learned models
- describe API communication
- describe central device data layer
- describe sensor communication
- describe context manager
- describe device state component
- illustrate sequence-to-sequence model
- describe source segment input
- describe machine-learned translation model
- describe candidate translations
- describe neural utility metric model
- describe utility scores
- describe average utility calculation
- describe output segment selection
- illustrate method for translating source sequence
- describe obtaining candidate outputs
- describe determining reference utilities
- describe determining output sequence

