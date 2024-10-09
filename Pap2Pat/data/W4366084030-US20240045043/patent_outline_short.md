# DESCRIPTION

## STATEMENT OF FEDERALLY SPONSORED RESEARCH

- acknowledge government support

## BACKGROUND

- motivate ultrafast ultrasound imaging

## SUMMARY OF THE DISCLOSURE

- introduce hybrid solution

## DETAILED DESCRIPTION

- describe ultrafast ultrasound beamforming systems and methods

### Example Ultrasound System

- illustrate example ultrasound system architecture
- describe system components and their interactions

### Example Process

- illustrate ultrafast ultrasound beamforming process
- acquire RF ultrasound data using plane wave imaging acquisition
- calculate delay profile matrix for beamforming
- reuse delay profiles in unsteered and steered plane wave imaging
- optimize delay profile matrix for reuse
- derive delay calculation formula
- explain delay profile matrix calculation
- describe memory parallelization
- explain beamforming process
- describe alternative beamforming approach
- discuss parallelization benefits
- outline image generation process

### Example Implementation

- implement linear interpolation on FPGA
- compensate transmit delay using BRAM
- reduce BRAM usage by time interleaving
- implement receive delay compensation using cyclic buffers
- reduce memory usage by buffering only a portion of RF data

### Experiment and Results

- design realization using Xilinx Vitis HLS
- test beamformer with tissue-mimicking phantom and mouse brain data
- evaluate beamformer performance and compare with Verasonics beamformer

### Further Examples

- integrate beamformer with hardware for ultrafast ultrasound imaging
- achieve sustainable average beamforming rate of 4.83 GSPS
- enable continuous unblocked ultrafast ultrasound imaging

## CONCLUSION

- summarize FPGA implementation benefits

