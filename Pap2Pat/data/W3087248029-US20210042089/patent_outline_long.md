# DESCRIPTION

## DESCRIPTION

### BACKGROUND OF THE INVENTION

- introduce field of invention
- motivate neural networks
- summarize history of neural networks
- describe limitations of GPU solutions
- describe development of dedicated ASIC solutions
- describe common theme of ASIC neural processing engines
- highlight optimization of data flow

### SUMMARY OF THE INVENTION

- introduce TCD-MAC concept
- describe TCD-MAC operation
- describe TCD-NPE architecture
- describe NESTA architecture
- highlight benefits of invention

### DETAILED DESCRIPTION THE INVENTION

- introduce temporal carry and TCD-MAC unit
- illustrate dot product computation using MAC unit
- describe MAC architecture with multiplier and adder
- detail Data Reshape Unit (DRU) and Hamming Weight Compressors (HWC)
- introduce TCD-MAC architecture with GEN and CPAU
- describe GEN unit and its output signals
- explain temporal carry injection and propagation
- illustrate TCD-MAC cycle-by-cycle execution
- describe signed input support using two's complement
- reformulate multiplication for signed inputs
- introduce NESTA architecture and its components
- describe application of TCD-MAC in NESTA
- reformulate computation using Hamming Weight compressors
- illustrate HW compression Adder (HWC-Adder) structure
- describe Compression and Expansion Layers (CEL)
- detail Hamming Weight Compressors (HWC) function
- introduce Carry Propagation Adder Unit (CPAU) and GEN
- describe Carry Buffer Unit (CBU) and its function
- illustrate NESTA architecture with six units
- describe Data Reshaping Unit (DRU) in detail
- detail Sign Extension Unit (SEU) and its function
- describe sign extension for signed inputs
- reformulate multiplication for signed inputs
- introduce Compressions and Expansion Layers (CEL) in detail
- describe input to CEL in each cycle
- detail Hamming Weight Compressors (HWC) in CEL
- describe Carry Propagation Adder Unit (CPAU) in detail
- detail GEN unit and its output signals
- describe Carry Buffer Unit (CBU) in detail
- illustrate NESTA operation in each cycle
- describe approximate partial sum and carry computation
- detail correct partial sum computation in last cycle
- illustrate NESTA application in convolutional neural networks
- describe TCD-MAC operation in NESTA
- detail energy and performance benefits of NESTA
- describe NESTA architecture for 3×3 kernel window
- illustrate NESTA operation for 11×11 convolution
- summarize NESTA architecture and its components
- describe Output Register Unit (ORU)
- introduce NESTA operation modes
- explain Carry Deferring Mode (CDM)
- explain Carry Propagation Mode (CPM)
- describe TCD-MAC architecture
- introduce design aspects of TCD-MAC
- describe DRU and CEL unit operations
- explain SEU and GEN unit operations
- describe PCPA unit operations
- explain clock period reduction
- describe CDM latency
- compare CDM latency scenarios
- analyze total latency
- analyze energy consumption
- introduce TCD-NPE architecture
- describe PE-array and LDN
- describe global buffers and Mapper-and-controller unit
- explain PE-array operation modes
- describe quantization and activation unit
- explain MLP computation
- describe PE-array configuration
- analyze NPE utilization
- introduce mapping unit
- describe Algorithm 1 for unrolling MLP problem
- explain CreateTree procedure
- describe execution tree extraction
- explain BFS search for optimal execution schedule
- illustrate example of executing MLP layer
- describe controller as finite state machine
- describe npe global memory division
- describe feature-map memory access
- describe filter weight memory access
- describe data arrangement in fm-mem and w-mem
- illustrate data arrangement in fig 14a
- describe data reshaping solution
- illustrate execution cycles of tcd-npe in fig 14b
- describe local distribution networks interface
- illustrate ldns in an npe constructed using 6x3 array of tcd-macs
- evaluate power, performance, and area gain of using tcd-mac
- describe ppa metrics extraction
- compare tcd-mac with conventional macs
- illustrate ppa comparison in table 1
- describe limitation of tcd-mac
- illustrate throughput and energy improvement in table ii
- describe tcd-npe implementation
- summarize characteristics of tcd-npe in table iii
- report overall ppa of implemented tcd-npe in table iv
- compare tcd-npe with similar npe composed of conventional macs
- illustrate four possible data flows in fig 11
- compare efficiency of each data flow on popular mlp benchmarks
- illustrate execution time and energy consumption in fig 16
- introduce tcd-mac and nesta

