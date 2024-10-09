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
- explain characterization of memory arrays for PUFs
- describe use of PUFs for authentication
- motivate use of random numbers in PUF-based systems
- describe prior art for generating random numbers with PUFs
- introduce limitations of prior art
- describe advantages of using ReRAM cells for random number generation
- motivate embodiments of the invention

## BRIEF SUMMARY

- introduce embodiments of the invention
- describe use of pre-formed ReRAM cells for random number generation
- explain formation of conductive paths in ReRAM cells
- describe characteristics of pre-formed ReRAM cells
- introduce concept of digital "fingerprint" of ReRAM arrays
- describe method of random number generation
- generate address list for random number generation
- measure resistances of selected ReRAM cells
- determine bit stream from resistance measurements
- compare resistances to median value
- generate random bit stream by pairwise comparison
- exclude unreliable cells from measurement
- further process random bit stream
- generate address data stream
- receive request for random number generation
- generate pseudorandom number
- segment pseudorandom number into addresses
- discard defective cells
- measure cells with same low-level injection current
- exclude cells with median resistance
- compare cells to median value or another cell
- further randomize bit stream

## DETAILED DESCRIPTION

- introduce random number generation
- describe limitations of traditional TRNGs
- motivate use of ReRAM arrays for TRNGs
- describe experimental data on ReRAM cell resistance
- explain stochasticity of ReRAM cell resistance
- describe method of true random number generation using ReRAM array
- introduce protocol for TRNG
- describe input request for RNG
- select addresses of ReRAM array
- generate random bits from ReRAM array
- describe "median" scheme for TRNG
- calculate median value of resistance distribution
- compare resistance values to median value
- generate random bits based on comparison
- describe "pairing" scheme for TRNG
- compare resistance values of paired cells
- generate random bits based on comparison
- handle defective cells in TRNG
- eliminate cells with outlier resistance values
- quantify levels of randomness using NIST tests
- describe results of NIST tests
- improve levels of randomness using additional processing
- filter address data stream to reject identical resistance values
- revise address data stream to reflect new pairs
- describe design of enhanced versions of TRNGs
- select stream of addresses in ReRAM array
- filter set of addresses to keep only desirable addresses
- generate random bits using "median" or "pairing" scheme
- enhance randomness using additional schemes
- describe post-processing techniques to enhance randomness
- describe example of enhancing randomness using XORing
- group streams of random bits by chunk
- add bits of each chunk modulo 2 to get resulting bit
- describe results of XORing operation
- discuss trade-off between latency and randomness
- describe optimized scheme for XORing
- discuss applicability of TRNGs to various computing devices
- conclude description of TRNGs based on ReRAM arrays

### Example 1

- describe example of enhancing randomness using XORing
- show results of XORing operation

### Example 2

- handle second stream of random numbers
- group stream of random bits by chunk of 11 bits
- add each chunk modulo 2 to get one resulting bit
- enhance randomness with XORing
- pass twelve NIST tests with average score of 99/100
- extend concepts to other physical arrays of devices
- apply probe current to measure voltage drop
- calculate resistance of ReRAM element
- generate random bit stream on basis of measured voltage or calculated resistance
- select constant probe current value
- use multiple probe currents for different cells
- use multiple probe currents for same cell
- segment address data stream into words
- specify cell address and cell probe current
- compute median cell resistance value
- exhaustively characterize ReRAM cells in advance
- store resistance values in database
- associate resistance measurements with cell addresses
- employ techniques on images of ReRAM arrays
- permit generation of cryptographic key pairs
- send handshaking message to initiate generation of random number
- include user input in handshaking message
- use handshaking message as seed input to PRNG process
- generate address data stream
- use PRNG process at both client and server devices
- generate parallel address data streams
- measure ReRAM devices corresponding to addresses
- generate pair of random bit streams
- use random bit streams to generate matching encryption keys
- ensure secure communications between devices
- send one random bit stream from one device to another
- receive and compare to native copy to authenticate sending device
- combine with other encryption schemes
- rely on arrays of pre-formed ReRAM cells
- generate unique, difficult to intercept challenge-response pairs
- eliminate need to exchange keys over insecure communication channels
- improve security
- use physical unclonable function generators (APGs)
- generate keys or key pairs for cryptography
- enable secure authentication and identification of client devices
- include addressable ReRAM in pristine state
- apply predetermined range of probe currents to each cell
- record challenges and responses in table
- use table to authenticate future communications
- treat challenge as public key and PUF response as private key
- generate cryptographic key pairs using PUF responses
- enroll client devices in secure environment
- select ReRAM addresses and apply probe current
- measure resulting resistance of selecting ReRAM cells
- store addresses, probe current, and resistance in server database
- authenticate client devices using challenges and responses
- use PUFs for secure cryptographic communication

