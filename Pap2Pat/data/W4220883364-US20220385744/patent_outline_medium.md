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
- re-assign buckets through segments
- rotate buckets to ensure fairness
- execute instances with distributed computing primitive

## DETAILED DESCRIPTION OF EMBODIMENTS OF THE INVENTION

- introduce Byzantine fault-tolerant distributed computing system

### 1. General Embodiments and High-Level Variants

- describe distributed computing system
- define nodes and network
- explain Byzantine fault tolerance
- introduce leader-based total order broadcast protocol
- describe concurrent execution of multiple instances
- explain deterministic function for assigning partitions
- describe multiplexing outputs in a single log
- introduce buckets of client requests
- explain assignment of buckets to leaders
- describe distribution of buckets through segments
- explain segmentation of log
- describe assignment of segments to instances
- introduce rotating buckets through segments
- explain ensuring fairness and preventing censoring
- describe mapping client requests to subdomains
- explain using hash function for mapping
- introduce primitive for handling client requests
- describe properties of primitive
- explain termination condition

### 2. Particularly Preferred Embodiments

- introduce ISS construction
- motivate ISS for scalability
- describe ISS architecture
- explain SB primitive
- describe ISS multiplexing
- introduce system model
- define sequenced broadcast
- describe SB properties
- explain multiplexing instances of SB
- describe epoch processing
- explain segment assignment
- describe bucket assignment
- explain epoch transition
- summarize ISS principles

### 3. Technical Implementation Details

- describe computerized units and systems
- introduce non-interactive and automated methods
- implement methods in software, hardware, or combination
- illustrate computerized unit 101
- describe hardware architecture of unit 101
- detail processor and memory components
- describe input/output devices and peripherals
- explain local input/output controller and system bus
- describe software in memory 110
- introduce operating system (OS) and its functions
- describe display controller and display
- introduce network interface or transceiver
- describe network and data communication
- detail network types and technologies
- introduce computer program products
- describe computer readable storage medium
- detail computer readable program instructions
- explain downloading instructions from network
- describe flowchart and block diagram illustrations
- introduce cloud computing environment
- describe characteristics of cloud computing
- detail service models and deployment models

