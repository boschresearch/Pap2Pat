# DESCRIPTION

## FIELD

- relate to computerized systems and methods for optimizing data transmission paths

## BACKGROUND

- introduce large communication networks
- describe control planes
- discuss limitations of control plane technology
- motivate need for flexible deployment of distributed control planes
- highlight importance of performance guarantees in networked systems

## SUMMARY OF THE INVENTION

- introduce electronic data transmission scheduling system
- describe electronic reliability checker
- describe electronic bandwidth checker
- describe electronic resource planner
- introduce electronic flow delay checker
- describe method for electronic data transmission scheduling
- describe automatic monitoring and decision-making method
- describe power utilization determination

## DETAILED DESCRIPTION OF AN EMBODIMENT OF THE INVENTION

- introduce computerized network management system
- describe deployment strategy for network control operations
- motivate black-box optimization framework
- compare with prior art
- formalize distributed control plane optimization problem
- describe computerized system for identifying network topology
- outline automated deployment of processing entities and aggregators

### Relevant Terminology and Definitions

- define computerized processing entity
- define electronic aggregator
- define data transmission node
- define data transmission link
- define network link propagation delay
- define network topology
- define bandwidth
- define electronic bandwidth checker
- define network flow
- define flow delay
- define electronic flow delay checker
- define reliability
- define electronic reliability checker
- define computer-implementable deployment strategy
- define electronic resource planner
- define limitations in the prior art
- define network components
- describe control plane architecture
- explain data transmission nodes
- introduce electronic reliability checker
- describe electronic bandwidth checker
- introduce electronic resource planner
- describe electronic flow delay checker
- explain electronic network monitor
- describe electronic change detector
- introduce electronic power utilization manager
- represent network topology as graph
- calculate delay bound
- describe network calculus
- formulate guaranteed performance service discipline
- describe formal problem solved by embodiments
- calculate network mapping reliability score
- calculate bandwidth allocations
- define electronic bandwidth checker
- motivate processing components and workflow
- describe computerized workflow
- outline electronic resource planner steps
- explain electronic bandwidth checker steps
- detail electronic flow delay checker steps
- discuss condition step and deployment strategy
- mention practical considerations and optimization
- contrast with prior art
- define prior art limitations
- motivate invention
- summarize prior art differences
- introduce advantages and applications
- describe application examples
- explain delay guarantees
- highlight workflow features
- introduce computerized workflow example
- describe control plane deployment challenges
- outline workflow steps for control plane deployment
- detail mapping step
- explain cost function calculation
- describe association step
- define traffic estimation
- estimate bandwidth demands
- introduce simple traffic estimation model
- estimate flow demand
- estimate burstiness of a flow
- introduce bandwidth verification
- formulate maximum concurrent flow problem
- solve maximum concurrent flow problem
- introduce dual of maximum concurrent flow problem
- solve dual problem using FPTAS
- introduce faster variant of FAS
- accelerate bandwidth verification
- introduce delay and backlog bound verification
- calculate routability indicator χ
- use genetic algorithm or column generation heuristic
- illustrate optimization time with different implementations
- introduce exemplary use cases
- provide analytic tool

### Example #2: Deployment of VMs for a Cloud Computing Task

- deploy computational task in distributed big data framework
- map deployment of distributed computational infrastructure

### Application Example #3: Deployment of a VNF Service Chain

- deploy service chains comprising connected VNF instances
- deploy computerized processing entities without associating electronic aggregator nodes
- simplify placement of VNFs on network topology
- set reliability R(G, j, C)=1 and assume N∈Ø
- execute steps from Workflow 100
- introduce network calculus
- define arrival curve and service curve
- calculate flow delay and backlog bounds
- compute output bound of flow after traversing system
- discuss concatenation property of network calculus
- apply network calculus for calculating delay bound of deployment plan
- assume guaranteed performance service discipline
- derive equivalent service curve of entire path
- split and route flow on list of selected paths
- calculate delay bound and backlog bound for sub-flow
- formulate delay and backlog verification problem as MILP
- introduce column generation heuristic algorithm
- solve master problem and subproblem iteratively
- restrict δ(K) variable back to binary values

