# DESCRIPTION

## STATEMENT CONCERNING FEDERALLY-FUNDED RESEARCH

- acknowledge government support

## FIELD OF THE INVENTION

- introduce true random number generation

## BACKGROUND

- motivate need for true random number generation
- describe limitations of pseudo-random number generators
- introduce physical unclonable functions (PUFs)
- describe use of PUFs for cryptographic key generation
- motivate improvement of PUF-based random number generation

## BRIEF SUMMARY

- introduce pre-formed ReRAM cells for random number generation
- describe ReRAM cell structure and operation
- explain pre-forming process and its effects
- describe unique resistance values of pre-formed ReRAM cells
- introduce method of random number generation using ReRAM cells
- describe generating address list for measurement
- explain measuring resistance of selected ReRAM cells
- describe determining random bitstream from resistance measurements
- introduce pairwise comparison of resistance values
- describe excluding unreliable cells from measurement
- mention further processing of random bitstream

## DETAILED DESCRIPTION

- introduce random number generation
- describe ReRAM arrays for random number generation
- motivate use of ReRAM arrays
- describe experimental data on ReRAM cells
- summarize stochasticity of ReRAM cells
- describe method of true random number generation
- outline steps of TRNG method
- describe address selection for TRNG
- describe probing ReRAM elements
- describe generating random bit stream
- introduce "median" scheme for TRNG
- describe "median" scheme protocol
- introduce "pairing" scheme for TRNG
- describe "pairing" scheme protocol
- quantify levels of randomness
- describe experimental results of TRNG
- introduce enhanced versions of TRNG
- describe general method protocol for enhanced TRNG
- describe post-processing techniques for enhanced TRNG

### Example 1

- describe example of enhancing randomness with XORing operations

### Example 2

- handle second stream of random numbers
- group random bits by chunk of 11 bits
- add each chunk modulo 2 to get one resulting bit
- enhance randomness with XORing
- pass twelve NIST tests with high score
- extend concepts to other physical arrays of devices
- generate random bit stream using measured voltage or calculated resistance
- select probe current value for cell measurements
- use multiple probe currents for different cells
- use multiple probe currents for the same cell
- generate address data stream using probe current values
- compute median cell resistance value using variable currents
- exhaustively characterize ReRAM cells in advance
- store resistance values in a database
- employ techniques on images of ReRAM arrays
- generate same pair of random numbers in parallel
- permit generation of cryptographic key pairs
- address shortcomings of conventional systems and methods
- use physical unclonable function generators (APGs) for secure authentication
- generate unique challenge-response pairs
- eliminate need to exchange keys over insecure communication channels
- use APGs for generation of keys or key pairs for cryptography
- characterize APG by applying probe currents to each cell
- record challenges and responses in a table
- use challenge-response pairs for cryptographic key generation
- authenticate client devices and generate encryption keys

