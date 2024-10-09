# DESCRIPTION

## BACKGROUND

- motivate deep neural networks
- limitations of operator fusion approaches
- importance of optimizing DNN execution
- challenges of existing fusion techniques

## SUMMARY

- summarize DNNFusion method

## DETAILED DESCRIPTION OF THE INVENTION

- introduce DNNFusion framework
- motivate operator view of DNN computations
- summarize contributions of DNNFusion
- propose mathematical-property-based graph rewriting
- present integrated fusion plan generation
- implement optimized fusion code generation
- evaluate DNNFusion on 15 DNN models
- motivate study on executing deep neural networks efficiently
- correlate execution efficiency with computation and layer count
- classify DNN operators and analyze fusion opportunities
- define five high-level abstract operator types
- analyze fusion opportunities based on operator types
- elaborate on representative fusion combinations
- introduce Extended Computational Graph (ECG) representation
- overview DNNFusion's design
- describe mathematical-property-based graph rewriting
- present lightweight profile-driven fusion plan exploration
- generate fusion code and apply advanced fusion-based optimizations
- elaborate on graph rewriting rules and examples
- introduce light-weight profile-driven fusion plan exploration
- describe fusion plan generation algorithm
- motivate fusion seed operator selection
- explain propagated exploration along seed's successors
- explain propagated exploration along seed's predecessors
- describe fusion code generation
- explain data-flow tree traversal
- describe code generation rules
- motivate intra-fusion-block optimizations
- explain inter-fusion-block optimizations
- introduce evaluation objectives
- describe evaluation setup
- characterize models and datasets
- outline comparison with state-of-the-art frameworks
- introduce evaluation environment
- describe mobile inference evaluation
- present fusion rate results
- present execution latency results
- compare with TASO
- study fusion optimizations
- present optimization breakdown
- discuss memory and cache performance
- discuss CPU/GPU utilization
- discuss compilation time
- demonstrate portability
- discuss related work on operator fusion
- discuss related work on polyhedral-based loop fusion
- discuss other related work on machine learning optimization
- conclude related work

