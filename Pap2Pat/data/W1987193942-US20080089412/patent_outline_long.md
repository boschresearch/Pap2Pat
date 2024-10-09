# DESCRIPTION

## FIELD OF THE INVENTION

- relate to multi-view video coding and decoding

## BACKGROUND OF THE INVENTION

- introduce 3D video communication and entertainment services
- describe 3D display characteristics
- explain head motion-parallax feature
- introduce Multi-View Video Coding (MVC) standard
- describe inter-view dependencies in MVC
- explain complexity problems and parallelism issues
- illustrate decoding issues in 3D-TV systems
- motivate need for parallel decoding of separate views

## SUMMARY OF THE INVENTION

- introduce parallel decoder implementation for different views
- describe encoding constraints for parallel decoding
- explain macroblock delay signaling
- summarize advantages of the invention

## BRIEF DESCRIPTION OF THE DRAWINGS

- describe FIG. 1 conventional sample prediction chain
- describe FIG. 2 system overview diagram
- describe remaining figures

## DETAILED DESCRIPTION OF VARIOUS EMBODIMENTS

- introduce parallel decoder implementation
- describe multimedia communications system
- illustrate data source and encoder
- explain encoding process
- describe storage and sender
- illustrate communication protocol stack
- describe sender and gateway
- explain receiver and decoder
- describe renderer
- motivate scalability
- list transmission technologies
- list communication devices
- illustrate representation of frames
- describe parallel decoding of views
- explain decoding process for two views
- illustrate decoding process
- describe WAIT state
- explain decoding operation
- describe notification process
- explain parallel implementation
- describe delay and synchronization overhead
- motivate signaling macroblock delay
- define syntax elements
- explain available reference area
- describe pds_block_size and pds_initial_delay
- illustrate sample decoding process
- describe pds_parameters_present_flag
- explain fixed_pds_for_all_sequence_flag
- describe parallelly_decodable_slice_flag
- explain available_reference_area equation
- discuss adaptive deblocking and sub-pixel interpolation
- describe sliding deblocking approach
- illustrate decoding process for first and second views
- detail filtering of macroblock boundaries
- describe modified deblocking operation
- discuss sub-pixel interpolation
- illustrate effect of sub-pixel interpolation
- describe padding approach for addressing unavailable pixels
- describe limiting reference area approach
- discuss degradation of coding efficiency
- describe arranging view dependencies
- describe modifying original picture
- describe utilizing slice groups
- describe modified raster scan
- describe signaling through SEI message syntax
- detail NAL unit and bytestream format
- describe SEI NAL unit and SEI messages
- discuss user data SEI messages
- describe signaling of parallelly decodable slice parameters
- discuss taking advantage of PDS arrangement
- describe entropy coding arrangements
- detail CAVLC and CABAC implementations
- describe motion vector coding
- illustrate ranges for horizontal and vertical components of motion vectors
- describe single codeword arrangement
- describe separate coding of horizontal and vertical components
- illustrate adapting variable length codes
- describe electronic device implementation
- detail components of electronic device
- describe program product implementation
- discuss computer-readable medium
- describe software and web implementations
- discuss rule-based logic and other logic
- describe database searching steps
- describe correlation steps
- describe comparison steps
- describe decision steps
- discuss modifications and variations
- describe combining features of embodiments

