# DESCRIPTION

## BACKGROUND

- introduce Byzantine fault-tolerant distributed computing systems

## SUMMARY

- motivate leader-based total order broadcast protocols
- describe method of executing LBTOB protocol
- outline advantages of the invention
- describe system and computer program product embodiments
- summarize benefits of the invention

## DETAILED DESCRIPTION OF EMBODIMENTS OF THE INVENTION

- introduce Byzantine fault-tolerant distributed computing system

### 1. General Embodiments and High-Level Variants

- describe distributed computing system architecture
- motivate concurrent execution of multiple LBTOB protocol instances
- describe deterministic function for assigning client requests to instances
- multiplex outputs of instances in a single log
- eliminate primary node and single-primary bottlenecks
- accommodate involvement of several BFT protocols
- assign buckets of client requests to different leaders throughout epochs
- distribute buckets through executing instances using deterministic function
- segment log into non-overlapping segments for distributing buckets

### 2. Particularly Preferred Embodiments

- introduce ISS construction for scalable leaderless protocols
- describe sequenced broadcast (SB) primitive
- multiplex instances of SB for parallelism
- define system model and assumptions
- detail sequenced broadcast properties
- explain multiplexing and bucket assignment
- describe bucket rotation and leader selection

### 3. Technical Implementation Details

- describe computerized units and systems
- illustrate computerized unit architecture
- detail hardware components
- explain software in memory
- describe network interface and transceiver
- introduce computer program products
- explain computer readable storage medium
- describe computer readable program instructions
- illustrate flowchart and block diagrams
- explain cloud computing environment
- describe functional abstraction layers

