# DESCRIPTION

## FIELD

- define DNA data storage

## BACKGROUND

- motivate DNA data storage

## SUMMARY

- introduce method embodiment
- introduce system embodiment
- introduce computer-readable media embodiment

## DETAILED DESCRIPTION

### Example 1—Overview

- introduce flexible decoding technologies for DNA storage
- describe error profile of DNA data storage
- discuss existing DNA coding schemes
- motivate need for new approaches to redundancy

### Example 2—Example Terminology

- define polynucleotides and their use in DNA data storage
- describe DNA strands and their composition
- explain hybridization and complementarity
- define primer and its role in nucleic acid synthesis
- describe amplification reaction mixture and PCR
- discuss PCR techniques and their applications
- explain melting temperature and its significance
- describe PCR amplification prior to sequencing

### Example 3—Example System Implementing Flexible Decoding in DNA Data Storage

- introduce system for encoding and decoding digital files using DNA
- describe encoder and its role in generating nucleotide symbol strings
- explain nucleotide synthesizer and sequencer
- describe decoder and its role in generating reconstructed digital file

### Example 4—Example Method Implementing Flexible Decoding in DNA Data Storage

- describe encoding and synthesizing digital file into nucleotide strands
- explain sequencing and decoding nucleotide strands to recover digital file

### Example 5—Example DNA Data Storage Scenarios

- describe DNA data storage scenarios and error correction challenges

### Example 6—Example Digital File

- describe digital file and its conversion to nucleotide symbol string

### Example 7—Example Nucleotide Symbol Strings

- describe nucleotide symbol strings and their use in DNA data storage

### Example 8—Example Encodings

- describe transformational encodings and constrained encodings
- explain application of constrained encodings in DNA data storage

### Example 9—Example Redundancy

- introduce redundancy information
- define inner redundancy
- define outer redundancy
- describe error correction using inner redundancy
- describe error correction using outer redundancy
- motivate use of redundancy in DNA data storage
- describe Reed Solomon code
- describe LT code
- describe LDPC code
- describe Hamming code
- describe cyclical redundancy check (CRC)
- describe checksum
- describe file integrity digests
- describe correction of substitution errors
- describe correction of insertion/deletion errors
- motivate use of redundancy in nanopore sequencing
- describe flexible decoding system
- describe block diagram of decoder system
- describe noisy reads
- describe solitary-strand-based selection
- describe cluster-based trace reconstruction
- describe conflict resolution processing
- describe additional decoding processing
- motivate flexible decoding
- illustrate cluster-based approach limitations
- demonstrate flexible-based approach advantages
- define trace reconstruction problem
- model noise in sequencing technologies
- describe synthetic test data creation
- illustrate architecture for trace reconstruction system
- describe DNA synthesis and storage
- explain DNA sequencing and error correction
- describe polynucleotide sequencer operation
- summarize sequencing technologies
- list examples of sequencing technologies
- introduce sequencing technologies
- describe error profiles
- introduce quality information
- describe polynucleotide sequencer output
- introduce trace reconstruction system
- describe system implementation options
- illustrate system operation
- describe noisy reads
- introduce consensus output sequence
- describe converter operation
- illustrate system flexibility
- introduce alignment anchor
- describe position of comparison
- introduce look-ahead window
- describe plurality consensus base
- identify variant reads
- describe look-ahead window consensus
- classify substitution errors
- classify deletion and insertion errors
- describe indeterminant errors
- introduce handling of indeterminant errors
- discard reads with indeterminant errors
- use bias or tiebreaker to force classification
- use quality information to classify ambiguous errors
- illustrate skipping over inactive trace portion
- generate consensus output sequence
- identify last good position in inactive trace
- introduce delay in inactive trace evaluation
- evaluate inactive trace to identify matching sequence
- create consensus look ahead sequence
- seek candidate position in inactive trace
- use search window to evaluate multiple possible locations
- compare subsequences of inactive trace to comparison sequence
- determine if candidate position represents a match
- restart trace reconstruction from candidate position
- introduce alignment anchors
- motivate use of alignment anchors
- describe function of alignment anchors
- illustrate placement of alignment anchors
- describe arrangement of multiple alignment anchors
- illustrate use of alignment anchors in consensus sequence generation
- describe generation of partial consensus sequences
- describe combination of partial consensus sequences
- illustrate joined consensus sequence
- describe removal of alignment anchor from consensus sequence
- introduce trace reconstruction system
- describe hardware components of trace reconstruction system
- describe software components of trace reconstruction system
- describe input/output devices of trace reconstruction system
- describe memory of trace reconstruction system
- describe sequence data interface of trace reconstruction system
- describe modules of trace reconstruction system
- introduce read alignment module
- align reads at position of comparison
- advance position of comparison based on error types
- generate reverse alignment
- combine forward and reverse alignments
- introduce alignment anchor module
- identify alignment anchor sequences
- divide reads into sub-reads
- align sub-reads
- reduce effects of accumulated mistakes
- identify variant reads
- classify error types
- generate consensus output sequence
- apply additional error correction techniques
- convert consensus output sequence to binary data
- introduce trace reconstruction process
- correct insertion, deletion, and substitution errors
- determine consensus base call
- compare base call to consensus
- identify variant read
- compare consensus string to variant read
- determine error type
- advance position of comparison
- determine reliability of variant read
- omit or use variant read
- determine if end of reads reached
- determine consensus output sequence
- introduce process for identifying errors in reads
- align reads at position of comparison
- determine consensus base call
- identify variant read
- determine error type for variant read
- move position of comparison for variant strand
- determine error type for variant read (continued)
- move position of comparison for variant strand (continued)
- determine error type for variant read (continued)
- move position of comparison for variant strand (continued)
- generate consensus output sequence
- convert consensus output sequence to binary data
- identify portion of read with bursty error
- omit portion of read with bursty error
- generate consensus output sequence with remaining portions
- identify indeterminate error in read
- define search window for matching sequence
- calculate edit distances for sub-sequences
- determine if match is found
- select matching sub-sequence
- select candidate position within matching sub-sequence
- set position of comparison past candidate position
- determine consensus output sequence at position of comparison
- synthesize DNA molecules from digital information
- describe SMRT technology
- describe Helicos True Single Molecule Sequencing (tSMS) technique
- describe SOLiD technology
- describe chemFET array sequencing
- describe electron microscope sequencing
- discuss error rates of sequencing technologies
- describe quality information in sequencing output
- describe trace reconstruction system
- describe computing system for trace reconstruction
- describe storage and input/output devices
- describe communication connections
- describe software implementation
- describe computer-readable media
- describe cloud computing environment
- describe example implementations
- describe method for cluster-based trace reconstruction
- describe error correction and integrity verification
- describe forming clusters and postponing processing
- describe outputting ordered list of nucleotide symbol strings
- describe system for cluster-based trace reconstruction
- describe string position map and operations
- describe correcting substitution and insertion/deletion errors
- describe inner redundancy information
- describe removing clusters and incorporating solitary strands
- describe computer-readable media and example alternatives

