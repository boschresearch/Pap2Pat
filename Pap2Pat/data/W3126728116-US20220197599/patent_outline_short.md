# DESCRIPTION

## STATEMENT CONCERNING FEDERALLY-FUNDED RESEARCH

- acknowledge government support

## FIELD OF THE INVENTION

- introduce true random number generation

## BACKGROUND

- motivate need for true random number generation
- describe limitations of pseudo-random number generators

## BRIEF SUMMARY

- introduce ReRAM arrays for random number generation
- describe pre-forming process of ReRAM cells
- explain unique resistance values of pre-formed ReRAM cells
- outline method of random number generation using ReRAM cells
- highlight advantages of inventive embodiments

## DETAILED DESCRIPTION

- introduce ReRAM arrays for random number generation
- motivate stochasticity of ReRAM arrays
- describe experimental data on ReRAM arrays
- outline method of true random number generation using ReRAM arrays
- describe "median" scheme for TRNG
- describe "pairing" scheme for TRNG
- quantify levels of randomness using NIST tests
- describe enhanced versions of TRNGs
- provide example of post-processing to enhance randomness

### Example 1

- demonstrate post-processing to enhance randomness

### Example 2

- handle second stream of random numbers
- group random bits by chunk of 11 bits
- add each chunk modulo 2 to get one resulting bit
- extend concepts to other physical arrays of devices
- generate random bit stream using measured voltage or calculated resistance
- use multiple probe currents for different cells
- combine with other encryption schemes, including keyless schemes
- address shortcomings of conventional systems and methods
- use physical unclonable function generators to generate unique challenge-response pairs
- eliminate need to exchange keys over insecure communication channels
- generate cryptographic key pairs using PUFs
- describe PUF-enabled authentication/communication protocol
- illustrate example embodiment of clients having APGs interacting with a server

