# DESCRIPTION

## § 0. RELATED APPLICATION(S)

- claim benefit of provisional patent application

## § 1. BACKGROUND

### § 1.1 Field of the Invention

- introduce mobile communications

### § 1.2 Background Information

- motivate 5G networks
- describe 5G network requirements
- discuss limitations of sub-6 GHz band
- introduce millimeter wave frequencies
- discuss blockages and shadowing in mmWave systems
- describe 3GPP transport architecture
- discuss challenges of frequent handovers
- motivate need for improved handover mechanism

## § 2. SUMMARY OF THE INVENTION

- introduce FIBR architecture
- describe ring network for wireless communication
- outline method for UE to select primary serving DUBS
- explain data transmission and control path maintenance
- describe handling of downlink packets and acknowledgements
- motivate need for connection-less transport network
- summarize benefits of FIBR implementation

## § 4. DETAILED DESCRIPTION

- provide context for invention

### § 4.0 ACRONYMS

- define acronyms

### § 4.1 3Gpp and FIBR Architectures for 5G Cellular Systems

- describe 3GPP transport network architecture
- motivate functional split between PDCP and RLC
- illustrate 3GPP proposed functional split and 5G transport network
- introduce FIBR transport network architecture and methods
- describe FIBR architecture and methods
- illustrate example FIBR architecture and methods
- describe single connectivity schemes in FIBR
- describe multi-connectivity schemes in FIBR
- describe packet processing schemes in FIBR
- describe ring protection schemes in FIBR
- discuss complexity of FIBR transport architecture

### § 4.2 Handover (Ho) Procedures in 3Gpp and FIBR

- present 3GPP HO procedures
- describe limitations of 3GPP HO procedures
- introduce FIBR HO procedures
- describe single connectivity HO procedures in FIBR
- describe multi-connectivity and HO procedures in FIBR
- summarize benefits of FIBR HO procedures

### § 4.3 Numerical Results

- simulate FIBR transport architecture
- compare blockage and RLF probabilities
- analyze effect of heartbeat signal periodicity
- compute throughput using ON-OFF process
- evaluate data plane latency
- discuss trade-offs between reliability and resources

### § 4.4 Example Apparatus

- describe example system architecture

### § 4.5 Refinements, Extensions, and/or Alternatives

- discuss applicability to other networks

### § 4.6 Conclusions

- summarize benefits of FIBR transport architecture

## APPENDIX I

### A. Blockage Probability

- derive blockage probability expressions
- compute upper and lower bounds on LOS blockage probability
- relate blockage probability to RLF probability

### B. RLF Probability

- derive RLF probability expression

## APPENDIX II

### C. Queueing Analysis of FIBR

- model uplink and downlink queueing delay in FIBR
- analyze queueing delay for ring and gNB-DU priorities

### D. Uplink Traffic

- compute total queueing delay for uplink packets

