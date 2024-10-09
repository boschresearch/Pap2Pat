# DESCRIPTION

## FIELD OF INVENTION

- define field of invention

## BACKGROUND OF THE INVENTION

- introduce digital watermarks
- motivate copyright protection
- describe watermarking systems
- summarize forensic marking
- describe copy-control watermarking
- limitations of conventional marking systems
- motivate efficient forensic marking
- describe compressed domain challenges
- summarize importance of forensic marks
- describe forensic marking applications

## SUMMARY OF THE INVENTION

- introduce forensic marking method
- describe metadata processing
- generate code
- select tributary segments
- assemble forensically marked content
- describe database storage
- describe preprocessing module
- describe tributary versions
- describe compression units
- describe watermark symbol intervals
- describe device and computer program product

## DETAILED DESCRIPTION OF CERTAIN EMBODIMENTS

- introduce forensic marks in compressed domain
- describe detection and recovery of forensic marks
- motivate resiliency against collusion attacks and differential analysis
- describe limitations of prior art
- introduce technique of U.S. Pat. No. 6,430,301
- describe limitations of U.S. Pat. No. 6,430,301
- introduce present invention's technique
- describe advantages of present invention's technique
- illustrate block diagram of forensic marking system
- describe preprocessing module
- describe marking module
- describe database
- describe embedder modules
- describe symbol interval
- describe compression of marked host content
- describe storage unit
- describe tributaries
- describe marking module's operation
- describe code generator
- describe transaction metadata
- describe database's role
- describe MUX's operation
- describe MUX's components
- illustrate example embodiment of MUX's operation
- describe compression units
- describe cut-and-splice procedure
- describe assembly of marked content
- describe advantages of present invention's technique
- describe applications of present invention
- describe variations of present invention
- describe benefits of present invention
- conclude description of present invention
- describe compression unit
- define watermark symbol interval
- illustrate example embodiment of FIG. 2
- generalize procedure to M-ary codes
- describe cut-and-splice technique
- illustrate marking operations in FIG. 4
- generate unique code
- store code and transaction metadata
- select tributary segments
- generate marked content
- adapt cut-and-splice procedure to different compression technologies
- select watermarking parameters
- extract embedded forensic marks
- describe example of watermarking parameters for AAC compression
- illustrate example string of overlapping windows
- describe embedding watermark bits
- describe transition from one tributary to another
- avoid perceptible artifacts
- illustrate window shapes in AAC compression
- describe long and short windows
- describe long-start and long-stop windows
- smooth transition points
- detect audio attacks
- select different window types
- create audible artifacts
- inhibit switching to new tributary
- assert switch abandon action
- determine switch abandon assertion
- permit switching to new tributary
- correct bit errors
- save bit error locations
- assert abandon switch in multi-channel content
- configure perceptual compressors
- apply procedures to other compression techniques
- describe MPEG-1, 2, and 4 audio compression
- describe speech codecs
- describe image and video compression techniques
- apply forensic marking to JPEG2000 and video compression

### Differential Analysis Obstruction

- thwart differential analysis attacks
- introduce signal distortions in preprocessing stage
- distortions must be different in each tributary
- distortions must be perceptually insignificant
- introduce non-linear amplitude modification
- apply non-linear amplitude modification to input samples
- produce different distortions in each tributary
- introduce random phase offsets into host content
- apply random phase offsets independently to each version
- create large difference between versions of host content
- use two or more distinct watermarking technologies
- embed same symbol in same compression unit(s)
- introduce host signal variations at marking stage
- manipulate parameters of compressed domain stream
- introduce small, random amplitude modifications
- use AAC Fill elements to introduce modifications
- change Dynamic Range Control (DRC) in Fill element
- effect masking of watermark symbols
- vary value of Δ associated with each tributary
- change and/or insert bits into DRC portion of bitstream
- add DRC bits to compressed bitstream
- implement embodiments in devices with hardware/software modules
- execute steps of methods using computer-executable instructions

