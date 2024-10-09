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
- explain latency requirements for URLLC applications
- discuss limitations of moving gNB-CU and gNB-DU to network edge
- describe connection-oriented 3GPP transport architecture
- introduce ring architecture background
- describe token ring and buffer insertion ring technologies
- discuss Resilient Packet Ring (RPR) network
- introduce handover techniques and multi-connectivity
- highlight unmet needs in HO with low latency

## § 2. SUMMARY OF THE INVENTION

- introduce FIBR architecture
- describe ring network for wireless communication
- explain primary serving DUBS selection
- detail control path and data transmission path maintenance
- describe downlink packet transmission and acknowledgement
- explain ring network operation with multiple DUBSs
- describe method for UE to select available DUBSs
- detail UE's search procedure to find available DUBSs
- explain UE's request for DUBSs to serve as access points
- describe AFD database and UE ID addition
- detail channel state information reception
- explain primary serving DUBS selection and control path maintenance
- describe downlink packet transmission and acknowledgement
- explain FIBR implementation benefits for eMBB services and URLLC applications
- motivate need for connection-less transport network

## § 4. DETAILED DESCRIPTION

- introduce invention scope
- provide general description guidelines

### § 4.0 ACRONYMS

- list acronyms used

### § 4.1 3Gpp and FIBR Architectures for 5G Cellular Systems

- introduce 3GPP transport network architecture
- describe functional split between PDCP and RLC
- illustrate 3GPP proposed functional split and 5G transport network
- introduce FIBR transport network architecture
- describe FIBR as bidirectional buffer-insertion ring architecture
- illustrate example FIBR architecture
- describe UE association with TA-GW
- describe connectionless connectivity between UE and gNB-DUs
- illustrate example UE method
- describe gNB-DU method
- describe packet processing and handover processing
- describe single connectivity schemes
- describe downlink packet processing
- describe uplink packet processing
- describe multi-connectivity schemes
- illustrate first example method for packet and handover processing
- illustrate second example method for packet and handover processing
- describe packet processing schemes in FIBR
- describe downlink packet processing
- describe uplink packet processing
- describe ring protection schemes in FIBR
- describe complexity of FIBR transport architecture

### § 4.2 Handover (Ho) Procedures in 3Gpp and FIBR

- introduce 3GPP HO procedures
- describe limitations of multi-RAT DC
- motivate intra-gNB-CU HO procedures
- describe single connectivity HO procedures
- calculate control plane latency
- discuss RLF and its impact on data plane latency
- describe multi-RAT DC HO procedures
- introduce FIBR HO procedures
- describe single connectivity HO procedures in FIBR
- motivate multi-connectivity in FIBR
- describe multi-connectivity and HO procedures in FIBR
- illustrate HO procedure for FIBR in multi-connectivity case
- discuss RLF recovery process in FIBR

### § 4.3 Numerical Results

- simulate FIBR transport architecture
- compare with 3GPP transport architecture
- consider blockage and RLF probabilities
- consider throughput
- consider data plane latency
- describe simulation setup
- plot blockage and RLF probabilities
- analyze blockage probability results
- analyze RLF probability results
- analyze throughput results
- analyze data plane latency results
- discuss trade-offs between reliability and resources

### § 4.4 Example Apparatus

- describe example system 1600
- describe components of system 1600
- describe machine-readable medium

### § 4.5 Refinements, Extensions, and/or Alternatives

- discuss applicability to other networks

### § 4.6 Conclusions

- summarize FIBR transport architecture
- summarize benefits of FIBR transport architecture

## APPENDIX I

### A. Blockage Probability

- define blockage probability
- derive blockage probability for dynamic blockers
- compute blockage probability for K-connectivity scenario
- obtain upper-bound on LOS blockage probability
- obtain lower-bound on LOS blockage probability
- compute probability of having at least K gNB-DUs in UE coverage area
- show probability of having at least K gNB-DUs in UE coverage area for different gNB-DU density values

### B. RLF Probability

- derive RLF probability

## APPENDIX II

### C. Queueing Analysis of FIBR

- model uplink and downlink queueing delay in FIBR
- analyze queueing delay for ring priority
- analyze queueing delay for gNB-DU priority
- compute waiting time in insertion buffer and gNB-DU uplink buffer
- compute downlink delay and uplink delay

### D. Uplink Traffic

- compute total queueing delay for uplink packet
- discuss uplink scheduling delay for URLLC applications
- analyze performance of FIBR considering protection mechanism and QoS agreement

