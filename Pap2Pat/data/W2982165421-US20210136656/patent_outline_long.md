# DESCRIPTION

## § 0. RELATED APPLICATION(S)

- claim benefit of provisional patent application

## § 1. BACKGROUND

### § 1.1 Field of the Invention

- introduce mobile communications

### § 1.2 Background Information

- introduce 5G and 3GPP background
- describe 5G service requirements
- discuss mmWave frequency use
- explain mmWave limitations
- describe blockage effects on mmWave signals
- discuss need for dense BS deployment
- introduce frequent handovers in mmWave networks
- describe 3GPP transport architecture
- discuss gNB-CU and gNB-DU functionality
- explain Xn interface and F1 logical interface
- discuss optimal placement of functional blocks
- argue against moving gNB-CU and gNB-DU to network edge
- describe connection-oriented 3GPP transport architecture
- discuss challenges of frequent HOs in mmWave networks
- introduce ring architecture background
- describe token ring architecture
- discuss fairness and node failure issues
- introduce buffer insertion rings
- describe Resilient Packet Ring (RPR) network
- discuss RPR reliability and fairness
- introduce HO techniques and multi-connectivity
- describe break-before-make HO technique
- discuss Make-Before-Break (MBB) and RACH-less techniques
- explain synchronized RACH-less technique
- discuss HO failure due to blockages and UE mobility
- introduce multi-connectivity to ameliorate intermittent connectivity
- describe two multi-connectivity ideas
- discuss dynamic multi-connectivity performance
- introduce dual connectivity framework
- describe fast switching between BSs
- discuss limitations of dual connectivity framework
- introduce offloading traffic to WiFi networks
- discuss limitations of WiFi networks
- discuss unmet needs in HO with low latency

## § 2. SUMMARY OF THE INVENTION

- introduce FIBR architecture
- alleviate performance degradation due to HOs
- describe ring-based transport network architecture
- group BSs in close proximity to form bidirectional buffer insertion ring network
- fast control signaling among gNB-DUs
- fast signaling among BSs and re-selection of gNB-DUs in case of blockages
- associate UE with Target Area Gateway (TA-GW)
- consider ultra-fast capability to accommodate UEs with changing point of attachment
- ensure connections are not interrupted or delayed
- meet QoS requirements of URLLC applications
- host gNB-CU, Layer 2/Layer 3 switching, and edge cloud at TA-GW
- connect user to core network without regard to serving BS
- provide framework for fast signaling among gNB entities
- overcome blockages and frequent HOs
- provide reliability with low degree of connectivity
- describe example ring network for wirelessly communicating with UE
- include centralized part of base station (CUBS) and distributed parts (DUBSs)
- maintain control path for connectivity and wireless data transmission path
- store downlink packets in buffer until acknowledged
- select new primary service DUBS and transmit stored packets
- describe method for forming ring network and serving UE
- group DUBSs in target area to form ring network
- conduct search procedure to find available DUBSs
- discover and select available DUBSs
- submit request for selected DUBSs to serve as access point
- accept request and add UE ID to address filter database
- receive or determine channel state information
- select primary serving DUBS and maintain control and data transmission paths
- receive and process downlink packets
- describe benefits of FIBR architecture

## § 4. DETAILED DESCRIPTION

- introduce invention scope
- provide context and disclaimer
- outline document structure
- motivate FIBR architecture

### § 4.0 ACRONYMS

- define acronyms

### § 4.1 3Gpp and FIBR Architectures for 5G Cellular Systems

- introduce 3GPP transport network architecture
- describe functional split of gNB
- illustrate 3GPP proposed functional split and 5G transport network
- describe gNB-CU and gNB-DU separation
- explain limitations of 3GPP transport architecture
- introduce FIBR transport network architecture
- illustrate FIBR architecture
- describe FIBR ring network
- explain UE association with TA-GW
- describe UE cell search procedure
- illustrate UE selection of gNB-DUs
- explain gNB-DU request and acceptance
- describe RACH procedure
- explain coordinated scheduling and beamforming
- describe packet processing and handover processing
- illustrate gNB-DU processing
- describe single connectivity schemes
- explain downlink packet processing
- describe gNB-DU downlink buffer
- explain uplink packet processing
- describe gNB-DU uplink buffer
- illustrate ring protection schemes
- describe 1+1 ring protection
- explain ring node failure
- describe fiber cut failure
- explain wrap on adjacent nodes
- describe gNB-DU node functionality
- explain packet inspection unit
- describe insertion buffer
- explain insertion decision unit
- describe queueing analysis
- explain downlink and uplink packet latency
- describe complexity of FIBR transport architecture
- explain TA-GW complexity
- describe gNB-CU complexity
- explain hardware processing capability
- describe ring architecture complexity
- explain FIBR advantages
- describe fast HO
- explain air interface utilization
- describe reliability improvement
- explain QoS satisfaction
- describe flexibility and controllability
- summarize FIBR benefits

### § 4.2 Handover (Ho) Procedures in 3Gpp and FIBR

- introduce 3GPP HO procedures
- describe limitations of multi-RAT DC
- motivate intra-gNB-CU HO procedures
- describe single connectivity HO procedures
- explain control plane latency calculation
- discuss data plane latency in legacy HO procedures
- describe RLF recovery procedures
- motivate multi-RAT DC HO procedures
- describe multi-RAT DC HO procedures
- explain control plane functions in dual connectivity
- introduce FIBR HO procedures
- describe single connectivity HO procedures in FIBR
- explain user-centric networking in FIBR
- describe switch request procedure in FIBR
- explain switch response procedure in FIBR
- describe switch acknowledgement procedure in FIBR
- explain AFD update procedure in FIBR
- motivate multi-connectivity in FIBR
- describe multi-connectivity HO procedures in FIBR
- explain heartbeat signal procedure in FIBR
- describe secondary gNB-DU blockage procedure in FIBR
- explain RLF recovery process in FIBR
- discuss purpose of multi-connectivity in FIBR
- explain framework for removing connection setup/teardown
- describe alternative data path transmission in FIBR
- discuss RLF probability in FIBR

### § 4.3 Numerical Results

- introduce simulation setup
- describe UE and blocker mobility models
- define simulation area and blocker distribution
- specify simulation parameters
- introduce blockage and RLF probabilities
- plot blockage and RLF probabilities with different degrees of connectivity
- compare blockage probabilities with theoretical bounds
- analyze effect of degree of connectivity on blockage probability
- discuss impact of number of gNB-DUs on blockage probability
- compare FIBR and 3GPP transport architectures
- introduce RLF probability
- plot RLF probabilities with different degrees of connectivity
- analyze effect of degree of connectivity on RLF probability
- discuss impact of number of gNB-DUs on RLF probability
- introduce heartbeat signal periodicity
- analyze effect of heartbeat signal periodicity on RLF probability
- discuss trade-off between reliability and resources
- introduce throughput computation
- describe ON-OFF process for throughput computation
- compare throughput of FIBR and 3GPP transport architectures
- discuss impact of degree of connectivity on throughput
- introduce data plane latency
- analyze data plane latency with different degrees of connectivity
- compare data plane latency of FIBR and 3GPP transport architectures
- discuss impact of RLF probability on data plane latency

### § 4.4 Example Apparatus

- introduce example system
- describe processors
- describe input/output interface units
- describe storage devices
- describe system buses and networks
- describe input and output devices
- describe machine-executable instructions

### § 4.5 Refinements, Extensions, and/or Alternatives

- discuss applicability to other mmWave and Terahertz cellular networks

### § 4.6 Conclusions

- summarize QoS requirements of 5G mmWave cellular networks
- introduce FIBR transport architecture
- summarize benefits of FIBR transport architecture
- conclude on FIBR transport architecture

## APPENDIX I

### A. Blockage Probability

- define blockage probability
- derive expression for blockage probability
- introduce dynamic blockers
- compute dynamic blockage rate
- derive upper and lower bounds on blockage probability
- assume independence of dynamic blockage and self-blockage
- compute blockage probability in K-connectivity setting
- simplify blockage probability expression
- derive upper-bound on LOS blockage probability
- derive lower-bound on LOS blockage probability
- compute probability of having at least K gNB-DUs in UE coverage area
- plot probability of having at least K gNB-DUs in UE coverage area
- discuss impact of gNB-DU density on multi-connectivity
- conclude blockage probability analysis

### B. RLF Probability

- define RLF probability
- derive RLF probability expression

## APPENDIX II

### C. Queueing Analysis of FIBR

- introduce queueing analysis of FIBR
- model system as prioritized non-preemptive head-of-the-line queue
- define packet arrival rates and service times
- compute utilization factors of gNB-DU uplink and insertion buffer
- consider two priority options: ring priority and gNB-DU priority
- derive waiting time in insertion buffer for ring and gNB-DU priorities
- derive waiting time in gNB-DU uplink buffer for ring and gNB-DU priorities
- model downlink traffic as M/M/1/N queue
- compute downlink delay for a packet destined to a UE
- compute uplink delay for an uplink packet in the ring node

### D. Uplink Traffic

- compute total queueing delay for an uplink packet
- discuss uplink scheduling delay for URLLC applications
- consider ring capacity and service rate at gNB-DUs
- assume uplink traffic to be one fourth of downlink traffic
- compute average uplink load at every gNB-DU
- evaluate maximum number of gNB-DUs that can be supported in FIBR
- discuss impact of priority on uplink and downlink delay

