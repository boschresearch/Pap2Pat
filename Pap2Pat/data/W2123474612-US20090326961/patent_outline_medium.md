# DESCRIPTION

## FIELD OF INVENTION

- define field of invention

## BACKGROUND OF THE INVENTION

- motivate digital watermarking
- describe objectives of watermarking systems
- describe forensic marking applications
- describe limitations of conventional marking systems
- motivate efficient forensic marking

## SUMMARY OF THE INVENTION

- introduce forensic marking in compressed domain
- describe method for embedding forensic marks
- describe example embodiments of metadata
- describe example embodiments of tributaries
- describe example embodiments of assembling

## DETAILED DESCRIPTION OF CERTAIN EMBODIMENTS

- introduce forensic marks in compressed domain
- describe detection and recovery of forensic marks
- motivate resiliency against collusion attacks and differential analysis
- summarize limitations of prior art (U.S. Pat. No. 6,430,301)
- introduce advantages of present invention over prior art
- describe block diagram for embedding forensic marks (FIG. 1)
- explain preprocessing module and embedder modules
- describe compression of marked host content
- define symbol interval and its application
- explain marking module and its operation
- describe flow diagram of preprocessing operations (FIG. 3)
- introduce code generator and transaction metadata
- explain operation of multiplexer (MUX) and selection of content segments
- illustrate example embodiment of MUX operation (FIG. 2)
- describe cut-and-splice procedure for forming marked content
- summarize advantages of present invention
- describe compression unit structure
- explain watermark symbol interval
- illustrate example embodiment of FIG. 2
- describe cut-and-splice technique for partial marking
- illustrate marking operations in FIG. 4
- describe adaptation to different compression technologies
- explain watermark extraction process
- provide detailed example of watermarking parameters for AAC compression
- illustrate example string of overlapping windows in FIG. 5
- describe MUX operation in FIG. 1
- explain avoidance of perceptible artifacts
- illustrate window shapes in AAC compression in FIG. 6
- describe transition window design criterion
- explain avoidance of audible artifacts in AAC compression
- illustrate determination of switch abandon assertion in FIG. 7
- describe error correction and bit error location saving
- explain abandon switch assertion in multi-channel content
- describe applicability to other compression techniques
- provide examples of image and video compression techniques

### Differential Analysis Obstruction

- thwart differential analysis attacks
- introduce signal distortions in preprocessing stage
- apply non-linear amplitude modification to host content
- illustrate non-linear amplitude modification using FIG. 8(A) and FIG. 8(B)
- introduce random phase offsets into host content
- use distinct watermarking technologies for embedding same symbol
- introduce host signal variations at marking stage
- implement differential analysis obstruction using AAC compressor
- change Dynamic Range Control in Fill element of compressed AAC bitstream
- describe implementation of various embodiments in devices and modules
- discuss computer program product and computer-readable medium

