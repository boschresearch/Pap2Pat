# DESCRIPTION

## STATEMENT OF FEDERALLY SPONSORED RESEARCH

- disclose government support

## BACKGROUND

- motivate ultrafast ultrasound imaging

## SUMMARY OF THE DISCLOSURE

- introduce hybrid solution
- describe system embodiment

## DETAILED DESCRIPTION

- introduce ultrafast ultrasound beamforming systems and methods
- motivate need for improved ultrasound imaging
- describe advantages of disclosed systems and methods
- summarize key features of disclosed systems and methods

### Example Ultrasound System

- introduce example ultrasound system
- describe transducer array and elements
- explain transmitter and receiver operation
- detail controller and computer system
- describe transmitter programming options
- describe receiver programming options
- explain FPGA-based beamformer operation
- describe processing unit and memory operation
- summarize display of beamformed data

### Example Process

- illustrate example process for ultrafast ultrasound beamforming
- introduce ultrasound system 100 and its components
- describe radio frequency (RF) ultrasound data acquisition
- specify subject types for ultrasound data acquisition
- introduce integrated circuit and memory components
- explain RF ultrasound data conversion from echo signal
- describe transmitter control of transducer for plane wave transmission
- introduce delay profile matrix and its storage in memory
- explain pre-calculation of delay profile matrix
- describe single delay value in delay profile matrix
- explain depth calculation from target depth and sampling rate
- illustrate conventional delay profile matrix usage
- introduce optimized delay profile matrix for reuse
- describe ultrasound system's reuse of delay profiles
- explain path delay calculation for unsteered plane wave
- illustrate unsteered path between beamformed point and transducer element
- explain path delay calculation for steered plane wave
- illustrate steered path between beamformed point and transducer element
- describe padding zeros to RF ultrasound data for steered plane wave
- explain revised receive delay calculation using relative lateral distance
- define example process
- calculate path delay
- calculate total delay
- create 2D delay profile matrix
- enable delay reuse
- achieve memory parallelization
- load delay profile to memory buffer
- read and load delay profile
- read RF ultrasound data based on delay value
- read multiple rows of RF ultrasound data
- generate multiple memory buffers
- read multiple rows in one clock cycle
- reduce memory buffer size
- read multiple rows in multiple clock cycles
- generate beamformed data
- stack multiple rows of RF ultrasound data
- sum diagonally to generate beamformed row
- generate beamformed data in alternative approach
- stack subset of multiple rows
- sum diagonally to generate partial beamformed row
- sum partial beamformed rows
- achieve DAS parallelization
- read all delay values at same depth
- read F rows of RF ultrasound data
- stack F rows of input RF data samples
- perform diagonal sum
- generate beamformed result
- align RF data samples as diagonal line
- beamform two adjacent targeting pixels
- reconstruct images with finer spatial pixel resolution
- generate image of subject based on beamformed data

### Example Implementation

- implement linear interpolation on raw RF data
- generate interpolated row by calculating mean of two rows
- reorder output of linear interpolator
- compensate transmit delay for each receive channel
- use W simple-two-port BRAM to buffer receive-channel data
- set depth of each BRAM to maximum transmit delay
- write interpolated RF data to buffer when N > Nnremove
- read from all buffers simultaneously when N > MTD
- demonstrate transmit delay compensation mechanism
- separate beamforming process into multiple clock cycles
- use Fsub RF buffers to reduce memory usage
- reshape buffering of receive channel
- use pointers to track writing address of each receive channel
- implement time interleaved FIFO on each BRAM
- reduce total memory space utilized by transmit delay compensation
- address challenge of receive delay compensation
- buffer only portion of RF data to internal buffer
- define dependent range and maximum dependent range
- reduce MDR and save internal memory resources
- implement cyclic buffers to reduce buffer depth

### Experiment and Results

- design realization using C++ and Xilinx Vitis HLS
- synthesize results to Verilog and implement using Xilinx Vivado
- use raw RF channel data from Verasonics Vantage system
- compare beamformed IQ data and resulting images
- scan tissue-mimicking phantom using Verasonics L11-5v probe
- evaluate lateral resolution and contrast
- scan mouse brain using Verasonics L35-16vX probe
- evaluate speed of beamformer
- import RF data and pre-calculated delay profile to Xilinx HLS
- get beamformed results using Xilinx HLS C/RTL co-simulation
- list latency and resources utilization results in Table II
- compare beamformed images from Verasonics and FPGA beamformer
- calculate contrast to noise ratio (CNR)
- create power Doppler and ULM images of mouse brain

### Further Examples

- integrate example beamforming parallelization method with hardware
- achieve ultrafast beamforming for ultrafast ultrasound imaging
- solve major obstacle of achieving higher beamforming frame rate
- enable delay profile reuse and parallel beamforming
- use HLS-based design flow for fast adaptation to different applications
- achieve sustainable average beamforming rate of 4.83 GSPS
- compare image quality of FPGA beamformer with Verasonics beamformer
- verify correctness and quality of example beamformer
- enable continuous unblocked ultrafast ultrasound imaging
- reduce bandwidth of data transferred to host PC
- improve functional ultrasound (FUS) with continuous real-time ultrafast ultrasound imaging
- scale up or down example beamformer design to fit different platforms
- compare example design with previous FPGA-based beamformers

## CONCLUSION

- summarize FPGA implementation benefits

