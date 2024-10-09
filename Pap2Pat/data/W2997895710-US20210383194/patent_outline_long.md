# DESCRIPTION

## STATEMENT REGARDING PRIOR DISCLOSURES BY THE INVENTOR OR A JOINT INVENTOR

- disclose prior publication

## BACKGROUND

- motivate event stream data

## SUMMARY

- introduce MCN-GEM method
- describe MCN-GEM system
- describe MCN-GEM storage medium
- note different subject-matters
- describe combination of features
- preview detailed description
- explain drawing notation

## DETAILED DESCRIPTION

- introduce event datasets
- define event datasets
- describe streaming algorithms
- motivate use of negative evidence
- introduce multi-channel neural graphical event model (MCN-GEM)
- describe components of MCN-GEM
- define graphical event model (GEM)
- write log-likelihood (LL) of event data
- describe deep neural network for λtk|i
- introduce sequence modeling approach
- describe recurrent neural networks and long short term memory (LSTM) cells
- model continuous time
- compute hidden state hik
- describe attention models
- compute net hidden states
- feed net hidden states into feed-forward layers
- describe λ-networks
- write LL function
- describe FIG. 2
- illustrate event dataset
- describe event types
- describe FIG. 3
- illustrate conditional intensity function
- motivate use of negative evidence
- introduce fake labels
- describe inter-event interval
- write LL function with fake labels
- describe FIG. 4
- illustrate event dataset with fake labels
- describe fake epochs
- describe FIG. 5
- illustrate basic model for history dependent conditional intensity
- describe recurrent cells
- describe λ-network
- motivate modeling continuous time history with negative evidence
- introduce fake epochs to reinforce negative evidence
- describe internal states in basic model
- describe internal states with fake epochs
- describe FIG. 6
- illustrate spatio-temporal attention
- describe spatial attention
- describe temporal attention
- describe training phase
- write regularized objective for training
- introduce event data analysis
- describe neural graphical model
- explain conditional instantaneous intensity estimation
- detail multi-channel recurrent neural network
- illustrate system for handling streaming algorithms
- describe hardware configuration of computing system
- introduce cloud computing environment
- explain service models of cloud computing
- detail deployment models of cloud computing
- illustrate abstraction model layers
- describe management layer functions
- detail workloads layer functions
- apply open loop integration scheme in IoT systems
- incorporate MCN-GEM with negative evidence in IoT devices
- describe IoT sensors for data collection
- illustrate position/presence/proximity sensors
- detail motion/velocity sensors
- explain displacement sensors
- describe temperature sensors
- detail humidity/moisture sensors
- illustrate flow sensors
- explain acoustic/sound/vibration sensors
- describe chemical/gas sensors
- detail force/load/torque/strain/pressure sensors
- illustrate electric/magnetic sensors
- receive time-stamped event epochs
- generate fake epochs for negative evidence
- feed event epochs and fake epochs into LSTM cells
- compute hidden states for event epochs and fake epochs
- feed hidden states into spatial and temporal attention models
- employ average attention for causal graph generation
- describe computer readable storage medium
- detail computer readable program instructions
- explain network for transmitting computer readable program instructions
- describe computer readable program instructions for carrying out operations
- detail flowchart illustrations and block diagrams
- explain computer implemented process
- describe article of manufacture
- detail computer readable storage medium having instructions
- explain functions/acts specified in flowchart and block diagram
- describe one embodiment of the present principles
- detail variations of the present principles
- explain use of "one embodiment" and "an embodiment"
- describe use of "and/or" and "at least one of"
- detail modifications and variations of the invention
- explain scope of the invention
- describe claims of the invention
- detail patent laws
- explain changes in particular embodiments
- describe what is claimed and desired protected by Letters Patent
- detail appended claims
- explain aspects of the invention
- describe functionality and operation of systems
- detail methods and computer program products
- explain architecture of possible implementations
- describe special purpose hardware-based systems
- detail variations of the present principles

