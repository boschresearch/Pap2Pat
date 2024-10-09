# DESCRIPTION

## BACKGROUND

- introduce Byzantine fault-tolerant distributed computing systems

## SUMMARY

- introduce LBTOB protocol
- execute multiple instances of LBTOB protocol
- assign disjoint partitions of client requests
- multiplex outputs in a single log
- map client requests to subdomains
- distribute buckets of client requests
- segment log into non-overlapping segments
- assign segments to instances
- prevent association of client requests with multiple sequence numbers
- use deterministic function with two operands
- re-assign buckets through segments
- rotate buckets to ensure segment assignment
- map client requests to subdomains using hash function
- execute instances according to distributed computing primitive
- design primitive to handle client requests as messages
- extend subdomain to include termination value
- deliver messages in extended subdomain
- ensure message delivery by correct nodes
- prevent message duplication
- ensure broadcast message delivery
- describe system embodiment
- describe computer program product embodiment

## DETAILED DESCRIPTION OF EMBODIMENTS OF THE INVENTION

- introduce Byzantine fault-tolerant distributed computing system

### 1. General Embodiments and High-Level Variants

- describe distributed computing system 1
- introduce nodes 11 and consensus protocol
- describe client requests and processing
- motivate concurrent execution of LBTOB protocol instances
- describe deterministic function for assigning client requests
- introduce multiplexing of outputs in totally ordered log 20
- compare with Mir-BFT approach
- describe advantages of present invention
- introduce buckets of client requests and epochs
- describe mapping of client requests to subdomains
- distribute buckets through executing instances of LBTOB protocol
- describe outputs of executing instances
- introduce segments of sequence numbers
- describe distribution of buckets through segments
- prevent malicious leaders from censoring requests
- describe leader nodes and proposing requests
- introduce broadcast and delivery operations
- describe partition of requests for liveness and preventing duplication
- segment log 20 into non-overlapping segments
- assign segments to instances of LBTOB protocol
- distribute buckets through segments at each epoch
- describe re-distribution of buckets at each new epoch
- prevent request duplication
- describe deterministic function for bucket distribution
- introduce nominal numbers of buckets and segments
- describe example of deterministic function
- rotate buckets through segments at each epoch
- ensure each segment is assigned a different bucket at each epoch
- describe hash function for mapping client requests to subdomains
- exploit collisions in hash function outputs
- describe background task of mapping client requests
- execute instances of LBTOB protocol on disjoint partitions of requests
- describe outputs of executing instances
- introduce primitive for handling client requests as messages
- describe properties of primitive (integrity, agreement, no duplication, eventual progress)
- ensure termination condition
- describe advantages of primitive
- introduce computer program product for executing LBTOB protocol
- describe computerized unit for executing program instructions

### 2. Particularly Preferred Embodiments

- introduce ISS construction
- describe ISS benefits
- explain SB primitive
- describe ISS multiplexing
- introduce log of client requests
- explain sequence number assignment
- describe segment subdivision
- explain bucket assignment
- describe epoch processing
- explain request duplication prevention
- describe implementation and deployment
- introduce system model
- define node processes
- describe communication channels
- assume eventually synchronous network
- introduce sequenced broadcast
- define SB properties
- explain SB implementation
- describe multiplexing instances of SB
- explain log structure
- describe epoch processing
- explain segment partitioning
- describe leader selection
- explain bucket partitioning
- describe bucket assignment
- explain epoch transition
- describe bucket rotation
- explain liveness guarantee
- describe leader selection policy

### 3. Technical Implementation Details

- describe computerized units and systems
- introduce non-interactive and automated methods
- implement methods in software, hardware, or combination
- execute program by digital processing devices
- illustrate computerized unit 101
- describe hardware architecture of unit 101
- include processor and memory in unit 101
- couple input/output devices to local input/output controller
- describe system bus and input/output controller
- execute software instructions by processor
- include volatile and nonvolatile memory elements
- provide external storage
- load instructions in memory
- include operating system in memory
- control execution of computer programs
- provide scheduling and input-output control
- manage files and data
- control memory and communication
- include keyboard and mouse as I/O devices
- include display controller and display
- provide network interface for data communication
- transmit and receive data between units
- implement network in wireless fashion
- use wireless protocols and technologies
- provide fast message passing between units
- implement IP-based network for communication
- administer network by service provider
- describe computer program products
- include computer readable storage medium
- provide computer readable program instructions
- execute instructions by processor
- include ISA instructions
- store instructions in computer readable storage medium
- download instructions from network
- receive instructions from network adapter card
- execute instructions in computing/processing devices
- illustrate flowchart and block diagrams
- implement functions/acts in flowchart and block diagrams
- provide computer readable program instructions
- execute instructions in computer or programmable apparatus
- implement functions/acts in flowchart and block diagrams
- describe cloud computing environment
- provide characteristics of cloud computing
- describe service models and deployment models

