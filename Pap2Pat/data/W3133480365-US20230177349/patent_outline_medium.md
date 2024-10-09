# DESCRIPTION

## BACKGROUND

- define edge computing
- applications and use-cases of edge computing

## DETAILED DESCRIPTION

- introduce edge computing concept

### A. Overviews of Edge Computing

- define edge computing
- describe edge cloud architecture
- illustrate operational layers among endpoints, edge cloud, and cloud computing environments
- describe latency constraints in network communication
- categorize network layers as “close edge”, “local edge”, “near edge”, “middle edge”, or “far edge”
- describe use cases for edge computing
- discuss service-flow and transaction concept
- describe edge computing advantages
- discuss caveats of edge computing
- describe edge computing system deployments
- define client computing node
- describe edge cloud formation
- describe network components of edge cloud
- describe appliance computing device
- describe server rack and sled
- describe sensors and mechanical connectivity
- describe output devices
- describe edge devices
- describe appliance computing device management
- describe virtual computing environment

### B. Usage of Containers in Edge Computing

- illustrate deployment and orchestration for virtualized and container-based edge configurations
- describe coordination of edge nodes and tenants
- introduce virtual edge instances and edge compute capabilities
- explain distributed trusted computing base
- describe container migration and key management
- introduce multi-tenant orchestrator and security functions
- describe use of containers, pods, and functions in edge computing
- illustrate system arrangements for containerized pods and functions
- describe security enforcement points and tenant isolation
- introduce software-defined silicon and configurable hardware
- describe integration of applications, functions, and services with edge computing system

### C. Mobility and Multi-Access Edge Computing (MEC) in Edge COMPUTING SETTINGS

- illustrate vehicle compute and communication use case
- describe edge gateway nodes and edge resource nodes
- introduce stateful applications and geographic distributed database
- describe container migration and hardware abstraction layer
- introduce FaaS computing capabilities and executable applications
- describe function code execution and containerization
- introduce edge provisioning node and software distribution
- describe payment and licensing of software instructions
- illustrate mobile edge system reference architecture
- describe MEC hosts and virtualization infrastructure manager
- introduce MEC platform manager and MEC orchestrator
- describe operations support system and user app proxy
- illustrate MEC services and filtering rules control component
- describe DNS handling component and service registry
- introduce MEC app lifecycle management component

### D. Computing Architectures and Systems

- introduce edge computing nodes
- describe components of edge computing node
- detail processor and system memory
- specify interconnect and interconnect interface
- describe storage options
- detail memory devices and standards
- introduce transceiver and antennas
- describe wireless communication protocols
- detail local and wide area network protocols
- introduce network interface controller
- describe wired communication options
- introduce acceleration circuitry
- detail artificial intelligence accelerators
- describe sensor hub and external interface
- introduce input/output devices
- describe battery and power management
- detail battery monitor and charger
- introduce power block and wireless power receiver
- describe instructions and machine-readable medium

### E. Machine Readable Medium and Distributed Software Instructions

- define machine-readable medium
- describe storage devices
- explain transmission of instructions
- discuss derivation of instructions
- illustrate assembly and compilation
- describe edge computing system
- depict layers of distributed compute
- explain fog computing
- describe core data center
- illustrate global network cloud

### F. Use Case: Satellite Edge Connectivity

- illustrate network connectivity in satellite and terrestrial settings

### G. Software Distribution:

- illustrate software distribution platform
- describe storage of computer readable instructions
- explain transmission of software
- discuss updates to software

### H. Machine Learning in Edge Computing Networks

- define machine learning
- introduce linear regression
- describe gradient descent algorithm
- discuss distributed computing for GD
- introduce federated learning
- describe federated learning protocol
- define model updates
- explain central server role
- describe client role
- decompose Equation (A1) into partial sums
- compute partial gradients locally
- aggregate partial gradients centrally
- update global model
- discuss structural embodiments of central server
- discuss structural embodiments of client device
- describe communication between nodes
- introduce distributed meta-learning
- describe modified objective for federated learning
- discuss challenges of federated learning
- introduce meta-learning approach
- describe problem in Equation (B2)
- illustrate example process for federated meta-learning
- introduce federated meta-learning
- describe approach 1: federated meta averaging
- illustrate process 1400 for approach 1
- describe gradient computation
- describe local weight updates
- describe Hessian computation
- describe local meta update
- describe global model update
- describe approach 2: federated meta stochastic gradient descent
- illustrate process 1500 for approach 2
- describe meta-learning over client data distributions
- describe clustering approaches
- illustrate process 1600 for clustering
- describe client reporting
- describe central server clustering
- describe client selection
- describe experimental results
- summarize performance of different approaches

### J. Compute-Aware Batch Size Selection for Federated Learning

- introduce federated learning limitations
- motivate compute-aware batch size selection
- describe straggler problem in federated learning
- introduce client-based approach
- introduce server-based approach
- describe compute time estimation
- determine minimum acceptable batch size
- describe client-based batch size selection
- describe server-based batch size selection
- illustrate server-based process flow diagram
- describe compute model definition
- determine minimum batch size
- select batch sizes for clients
- communicate batch sizes to clients
- describe client operations
- illustrate client-based process flow diagram
- determine nominal compute time
- select clients for participation
- compute gradients over selected batch
- update weights and combine
- introduce automated ML approaches for federated learning
- motivate reinforcement learning for client selection
- describe deep reinforcement learning background
- illustrate reinforcement learning model
- define state representation
- introduce statistics of parameter updates
- motivate cosine similarity of local parameter updates
- describe training and validation loss
- introduce current lr and number of local epochs
- describe number of training examples at the federated node
- introduce average rate supported over the wireless link
- describe energy budget
- introduce time to compute gradient per data point
- describe memory access time
- introduce action representation
- describe reward signals
- outline example training algorithm
- describe extensions and edge computing implementations

## EXAMPLES

- introduce edge computing node apparatus
- process initial set of weights for global ML model
- compute gradient for set of weights based on first dataset
- generate updated set of weights based on computed gradient
- compute Hessian based on computed gradient
- evaluate gradient expression for ML model based on updated set of weights and second dataset
- generate meta-updated set of weights based on initial set of weights, Hessian, and evaluated gradient expression
- select client compute nodes randomly from larger set of client compute nodes
- cluster larger set of client compute nodes based on data distributions
- select client compute nodes based on clustering
- determine data batch size for each client compute node
- perform reinforcement learning to determine hyper-parameters for federated ML training
- obtain state information from clients of edge computing network
- select set of action vectors corresponding to hyper-parameters
- perform rounds of federated ML training within edge computing network
- determine measure of accuracy of updated global ML model
- perform reinforcement learning across multiple hyper-parameter scenarios
- define mathematical formula for weight update
- introduce Hessian computation
- describe Example 47
- describe Example 48
- describe Example 49
- describe Example 50
- describe Example 51
- describe Example 52
- describe Example 53
- describe Example 54
- describe Example 55
- describe Example 56
- describe Example 57
- describe Example 58
- describe Example 59
- describe Example 60
- describe Example 61
- describe Example 62
- describe Example 63
- describe Example 64
- describe Example 65
- describe Example 66
- describe Example P1 to P12
- describe Example PP1 to PP23

## ADDITIONAL EXAMPLES

- define apparatus with means to perform method
- define non-transitory computer-readable media with instructions
- define machine-readable storage with machine-readable instructions
- define apparatus with processors and computer-readable media
- define apparatus with transceiver and antennas
- define apparatus with system memory and processor
- define apparatus with logic, modules, or circuitry
- define method, technique, or process
- define apparatus with processors and computer-readable media
- define signal as described in examples
- define datagram, packet, frame, segment, protocol data unit (PDU), or message
- define signal encoded with data
- define signal encoded with datagram, packet, frame, segment, protocol data unit (PDU), or message
- define electromagnetic signal carrying computer-readable instructions
- define computer program with instructions

