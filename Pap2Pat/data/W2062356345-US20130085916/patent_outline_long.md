# DESCRIPTION

## FIELD OF THE INVENTION

- relate data system

## BACKGROUND OF THE INVENTION

- motivate financial crisis
- limitations of regulatory oversight
- introduce problem of confidential data

## OBJECTS AND SUMMARY OF THE PRESENT INVENTION

- provide secure mechanism
- provide data processing system
- provide computer platform
- provide process of managing data
- summarize illustrative data processing system

## DESCRIPTION OF THE INVENTION AND ILLUSTRATIVE EMBODIMENTS THEREOF

- introduce financial industry problem
- describe solution: aggregate metrics for assessing industry-wide attributes
- describe process: confidential information used to develop aggregate metrics
- describe system architecture: multiple server environment with system managing software
- describe hardware: speed and capacity of system defined by size and complexity of data sets
- describe inter-firm communication: dedicated link or Internet protocols on public access network
- describe operative software: database management and access tools
- describe system operation: computes aggregate risk exposures of financial institutions
- describe hardware arrangement: block diagram form in FIG. 1
- describe system functionality: enables cooperation among financial institutions
- describe application: financial audit
- describe application: monitoring private investments
- describe application: index-based securities
- describe other applications: system-wide aggregate quantities, monitoring system liquidity risk
- describe Herfindahl index calculation
- describe multi-party computations: information-theoretic algorithms and encryption techniques
- describe process flow: FIG. 2
- describe fraud detection feature
- describe system repetition: for computing additional information

### Information Theoretic Approach

- introduce information-theoretic approach
- describe two protocols: securely compute summations and inner products
- describe protocol 1: Information Theoretic Secure Sum Algorithm
- describe common inputs: quantization level and number of parties
- describe party inputs: quantized values
- describe common output: summation of quantized values
- describe step 1: parties provide random numbers to other parties
- describe step 2: parties compute and publicly reveal numbers
- describe step 3: each party computes summation
- describe extensions: fewer random numbers, polynomial or linear subspaces
- describe example: three banks computing average risk exposure
- describe example: each bank assigns numbers to other banks
- describe example: each bank completes its row
- describe example: each bank calculates sum of numbers
- describe example: final calculation of average risk exposure
- describe protocol 2: Information Theoretic Secure Inner Product Algorithm
- describe definition: sample correlation of two time series
- describe algorithm: secure protocol to compute correlations

### Cryptographic Security Approach

- introduce RSA encryption technique
- describe public and private keys
- explain encryption and decryption process
- introduce Oblivious Transfer (OT) protocol
- define OT protocol functionality
- motivate GMW approach for Boolean functionalities
- describe circuit decomposition using XOR and AND gates
- explain secure computation of shares for gates
- introduce cryptographically secured algorithms
- discuss extensions to malicious or active adversaries
- introduce cryptographic sum-protocols
- describe homomorphic thresholding approach
- introduce cryptographic inner-product-protocols
- describe arithmetic OT approach for secure inner product
- introduce homomorphic approach for calculating inner product
- describe fully homomorphic encryption approach
- introduce cryptographic security approach
- describe circuit-based approach for calculating inner product
- outline protocol for computing inner product
- illustrate circuits for inner product computation
- optimize circuit for minimizing AND gates or communication rounds
- introduce cryptographic quantile protocol
- describe secure protocol for computing k-th ranked element
- propose circuit-based approach for k-th ranked element computation
- optimize circuit for k-th ranked element function
- run Yao, BMR, or GMW protocol for secure computation
- apply techniques for amortizing OT protocols
- use BMR protocol for fixed number of communication rounds
- describe application of secured sum algorithm
- calculate system-wide aggregate quantities
- calculate concentration index
- calculate true average or asset-weighted average of NAV
- describe application of secured sum and quintile algorithms
- aggregate risk metrics across financial industry
- monitor systemic liquidity risk of exchange
- calculate total liquidity demand or supply
- aggregate privately calculated metrics
- monitor market vulnerability metrics
- describe application of secure correlation algorithm
- monitor risks taken by outside managers
- describe application of secure correlation algorithm
- measure or manage counterparty risk
- describe application of secured sum and quintile algorithms
- assist financial auditors in comparing valuations
- describe application of secured computation techniques
- perform due diligence on private investments
- create new trading indices
- calculate index based on internally assigned values
- describe application of secured computation techniques
- aggregate individual data from social network systems
- track aggregate performance parameters in healthcare
- describe application of secured computation techniques
- operate in general-purpose or special-purpose computing system environments
- describe components of inventive computer system

