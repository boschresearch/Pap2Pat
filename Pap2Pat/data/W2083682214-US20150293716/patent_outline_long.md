# DESCRIPTION

## STATEMENT REGARDING GOVERNMENT SPONSORED RESEARCH AND DEVELOPMENT

- disclose government support

## TECHNICAL FIELD

- define technical field

## BACKGROUND

- introduce coding for rewriting
- motivate coding for rewriting
- summarize prior art on coding for rewriting
- describe WOM model
- discuss techniques for designing WOM codes
- summarize recent works on WOM codes
- discuss capacity achieving WOM codes
- introduce error correction in WOM codes
- summarize prior art on error-correcting WOM codes
- motivate need for joint rewriting and error correction

## SUMMARY

- introduce joint rewriting and error correction
- describe code construction using polar coding
- summarize analytical technique
- discuss lower bounds to sum-rate
- describe extension to MLC and general noise models
- introduce method of rewriting a memory
- introduce method of reading a memory
- introduce memory system

## DETAILED DESCRIPTION

- introduce detailed description
- explain purpose of drawings
- describe illustrative embodiments
- outline scope of disclosure
- introduce joint rewriting and error correction
- motivate rewriting and error correction
- present coding scheme
- analyze code for binary symmetric channel
- extend results to multi-level cells and general noise models
- introduce code construction for error-correcting WOM codes
- describe cell programming method
- outline constraints for cell programming
- introduce example write process
- describe polar encoder and WOM channel devices
- illustrate write process with block diagram
- outline operations of encoding method
- determine current cell levels
- generate next cell levels
- write next cell levels into memory
- describe rewriting operation
- outline error correction method
- define rewriting method
- minimize cell level changes
- introduce 1st probabilistic model
- compute new cell levels
- introduce 2nd probabilistic model
- compute new cell levels
- specify matrix AN×N
- generate dither
- compute new cell levels
- define vector y
- compute u_FWOM−FC
- compute u_FC
- compute W_N^(i)
- define base cases for W_N^(i)
- compute L_N^(i)
- define WOM cell levels
- describe error correction method
- introduce polar code generating matrix
- determine FWOM
- compute FER values
- describe error correction decoding
- introduce binary vector properties
- describe data value generation
- introduce binary matrix AN×N
- describe subsets FWOM and FC
- describe error distribution
- describe binary vector properties
- introduce polar code decoding algorithm
- recover data values
- describe list-decoding algorithm
- compute ui values
- describe list management
- choose most likely element
- describe stored data error-correcting code
- introduce list size parameter
- compute ui values with list
- choose most likely element
- specify matrix AN×N
- recover value action
- compute WNi values
- determine ui values
- recover data bits
- specify list-decoding algorithm
- compute WNi values (again)
- update list of value assignments
- choose most likely element
- recover data bits (again)
- specify error-correcting code
- compute WNi values (again)
- update list of value assignments (again)
- choose most likely element (again)
- recover data bits (again)
- specify error-correcting code (again)
- recover data bits (again)
- define WOM cells and operations
- describe rewriting method
- explain error correction method
- introduce FC and FWOM
- describe embodiment of encoding method
- describe embodiment of decoding method
- introduce Nadditional cells
- describe modified encoding method
- describe modified decoding method
- introduce q-level cells
- describe level-by-level approach
- provide example of encoder and decoder
- outline organization of description
- introduce basic model and notations
- describe embodiment of code construction
- describe embodiment of code
- describe embodiment of code extensions
- analyze actual sum-rates achieved by code embodiment
- provide further example embodiments
- include concluding remarks
- define model for rewriting
- introduce polar codes
- define polar code properties
- describe encoder transformation
- explain decoding process
- introduce concept of upgrading and degrading channels
- define channel degradation
- describe code construction with nested structure
- introduce WOM channel parameters
- explain encoding function
- describe decoding operation
- discuss time complexity of encoding and decoding
- extend code to t-write error correcting WOM code
- describe application of encoder and decoder for t writes
- note on computing α values for BSC(p)
- introduce code construction
- revise encoder and decoder
- derive sum-rate equation
- analyze correctness of code
- discuss nested structure of code
- prove Lemma 1
- prove Lemma 2
- prove Lemma 3
- prove Lemma 4
- analyze lower bound to sum-rate
- derive equation for number of bits written
- derive sum-rate equation
- prove lemma 5
- state theorem 6
- prove theorem 6
- show numerical results
- introduce erasure channel
- describe handling erasures
- extend to multi-level cells
- discuss achievable rates
- find BSCs satisfying condition
- show achievable sum-rates for nested code
- show achievable sum-rates for general code
- discuss lower bound to sum-rate
- conclude with remarks on code performance

### VII. Additional Example Embodiments

- illustrate data device constructed/configured to perform methods and operations
- show memory accessed by memory controller
- describe memory controller operating under control of microcontroller
- manage communications with memory via write device
- manage communications with host device via host interface
- supervise data transfers from host to memory
- supervise data transfers from memory to host
- include data buffer for temporarily storing data values
- include Error Correcting code (ECC) block for maintaining ECC data
- perform error correction operations for encoding and decoding scheme
- describe operations for operating data storage device
- describe operations for reading data from device
- describe operations for programming data storage device
- describe encoding and decoding operations
- implement processing components in software or hardware
- implement processing components as control logic
- execute software program instructions from program memory
- describe host device as computer apparatus
- illustrate example computing device
- describe basic configuration of computing device
- include processor and system memory
- describe memory bus for communicating between processor and system memory
- describe processor as microprocessor, microcontroller, or digital signal processor
- include levels of caching, processor core, and registers
- describe memory controller as part of processor or separate component
- describe system memory as volatile or non-volatile memory
- include operating system, applications, and program data
- describe applications as encoding and decoding algorithms
- operate with program data on operating system
- include WOM that is written to and read from using various features
- describe applications as including algorithms with computer-readable instructions
- execute algorithms by one or more processors
- describe program data as including various data
- include bus/interface controller for facilitating communications
- describe data storage devices as removable or non-removable
- include examples of computer storage media
- describe system memory, removable storage, and non-removable storage
- include interface bus for facilitating communication from interface devices
- describe output devices as graphics processing unit and audio processing unit
- describe peripheral interfaces as serial interface controller or parallel interface controller
- describe communication device as network controller
- facilitate communications with other computing devices over network
- describe computing device as portion of small-form factor portable electronic device
- describe computing device as personal computer

