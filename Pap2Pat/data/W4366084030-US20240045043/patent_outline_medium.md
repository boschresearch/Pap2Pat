# DESCRIPTION

## STATEMENT OF FEDERALLY SPONSORED RESEARCH

- disclose government support

## BACKGROUND

- motivate ultrafast ultrasound imaging

## SUMMARY OF THE DISCLOSURE

- introduce hybrid solution

## DETAILED DESCRIPTION

- introduce ultrafast ultrasound beamforming systems and methods
- motivate advantages over conventional ultrasound imaging

### Example Ultrasound System

- describe ultrasound system architecture
- detail transducer array and transmitter operation
- explain receiver and beamformer operation
- outline processing and display of beamformed data

### Example Process

- illustrate ultrafast ultrasound beamforming process
- acquire RF ultrasound data using plane wave imaging acquisition
- describe delay profile matrix and its calculation
- explain conventional delay profile matrix usage
- introduce optimized delay profile matrix for reuse
- describe unsteered plane wave imaging path delay calculation
- describe steered plane wave imaging path delay calculation
- explain padding zeros to RF ultrasound data for steered imaging
- reduce receive delay profile matrix dimensions
- express transmit delay and remove xn*sin θ term
- define delay calculation
- derive path delay equation
- explain 2D delay profile matrix
- describe delay reuse and memory parallelization
- load delay profile into memory buffer
- read RF ultrasound data based on delay values
- generate beamformed data by beamforming RF ultrasound data
- stack RF data samples and sum diagonally
- describe alternative beamforming approach
- generate partial beamformed rows and sum
- achieve DAS parallelization
- explain diagonal sum and beamformed result
- describe relationship between beamformed lines and input channels
- explain beamforming of adjacent pixels
- generate image of subject based on beamformed data

### Example Implementation

- implement linear interpolation on FPGA
- compensate transmit delay using BRAM
- read and write to BRAM simultaneously
- reduce BRAM usage by time interleaving
- implement receive delay compensation
- reduce memory usage by buffering only a portion of RF data
- use cyclic buffers to reduce buffer depth
- separate beamforming into multiple clock cycles
- implement beamforming with reduced subaperture size
- pipeline the beamforming process

### Experiment and Results

- design realization using Xilinx Vitis HLS
- synthesize and implement the design on FPGA
- test the design with tissue-mimicking phantom data
- test the design with mouse brain data
- measure latency and resource utilization
- compare beamformed images with Verasonics beamformer
- calculate contrast to noise ratio (CNR)

### Further Examples

- integrate beamformer with hardware for ultrafast ultrasound imaging
- achieve sustainable average beamforming rate of 4.83 GSPS
- compare image quality with Verasonics beamformer
- enable continuous unblocked ultrafast ultrasound imaging
- improve functional ultrasound (FUS) with continuous real-time imaging
- scale up or down the design for different platforms and applications

## CONCLUSION

- summarize FPGA implementation benefits

