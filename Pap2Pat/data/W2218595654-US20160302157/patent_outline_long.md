# DESCRIPTION

## FIELD OF THE INVENTION

- introduce telecommunications field
- describe interference phenomenon
- motivate coordination mechanisms

## PRIOR ART

- define equivalent channel
- introduce channel gain
- describe IWFA algorithm
- explain power allocation
- define SINR
- provide SINR expression
- describe initialization stage
- allocate power vectors
- iterate on frame index
- iterate on transmitter index
- update power vector
- determine stop criterion
- describe IWFA limitations
- explain IWFA convergence
- discuss utility functions

## SUMMARY OF THE INVENTION

- introduce method of coordinating transmitters
- describe K transmitters and receivers communication
- explain channel gains and power levels
- detail exchange stage of method
- describe power level coding
- explain SINR estimation
- detail system of equations for power estimation
- describe maximum likelihood estimation
- explain global interference minimization
- compare with IWFA algorithm
- introduce acquisition stage
- describe training sequence transmission
- explain SINR estimation during acquisition
- detail system of equations for channel gain estimation
- describe solving system of equations
- introduce normalized SINR
- explain advantage of normalized SINR
- introduce pseudo-invertible matrix constraint
- describe determining power levels
- explain estimating channel gains
- introduce random draw for full rank matrix
- describe joint source-channel coding
- describe separate source-channel coding
- introduce estimating SINR before filtering
- describe transmitter for performing method
- describe telecommunications system
- describe computer program for performing method

## DETAILED DESCRIPTION OF AN EMBODIMENT

- assume channel gains are constant or piecewise constant
- define coherence time Tc
- introduce fast fading
- define number of consecutive carriers C
- express signals or observations yi,m(n)(k)
- define SINR associated with subband m for receiver i
- estimate SINR on basis of available observations
- define theoretical value of SINR
- consider estimation noise
- discuss effect of observation duration T0
- consider SINR after filtering
- define linear filter fii,m(q)
- express theoretical SINR
- define equivalent channels gii,m and gji,m
- consider special case NR=1 and Q=1
- express equivalent SINR estimated at receiver i
- estimate equivalent SINR based on knowledge of samples and transmitted symbols
- express estimate of equivalent SINR
- consider estimation before filtering
- estimate equivalent SINR from samples before filtering
- define associated theoretical SINR
- express equivalent SINR as function of equivalent channels and transmission powers
- describe wireless communications system
- introduce IEEE 802.11n standard
- explain channel selection problem
- propose power allocation method
- define quality of communications channel
- describe two examples of method application
- explain SINR structure
- represent system diagrammatically
- describe transmitter and receiver structure
- explain channel gain estimation methods
- describe acquisition stage Ph1
- explain SINR estimation
- solve system of equations
- obtain estimate of channel gains
- describe power level determination
- ensure pseudo-invertibility of matrix Si,m
- estimate channel gains using relationship
- describe exchange stage Ph2
- explain coding step
- explain estimation step
- explain decoding step
- describe power level coding
- explain joint spatial-temporal and source-channel coding
- describe separate source-channel coding
- define channel coding
- motivate channel coding rate
- introduce quantization cells
- describe channel coding implementation
- explain cell indexing
- associate power sequences with cells
- order power sequences
- receive SINR estimates
- estimate SINR
- calculate power levels
- define maximum likelihood estimate
- approximate SINR
- reduce model complexity
- describe example scenario
- set up linear system of equations
- solve for channel gains
- define mathematical notation
- derive system of equations for access point AP1
- derive system of equations for access point AP2
- describe power level coding
- describe estimation of channel gains
- describe power allocation stage
- define performance criterion
- describe simplified structure of transmitter
- describe memory module and processor unit
- describe execution of computer program
- describe transmission and reception of subframes
- describe implementation in Wi-Fi context
- describe channel selection by access points
- describe return channel for SINR estimation
- describe testing of channel selections
- define global performance criterion
- describe constraints for power allocation
- describe particular implementation with constraint C3
- present simulation results

