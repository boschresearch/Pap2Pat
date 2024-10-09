# DESCRIPTION

## TECHNOLOGICAL FIELD

- introduce high-density crossbar memory arrays

## BACKGROUND

- motivate need for new technologies
- describe memristor based resistive RAM
- limitations of redox memristive array
- summarize sneak-paths problem

## BRIEF SUMMARY

- introduce single stage readout technique
- describe locality property of memory systems
- summarize sneak-paths correlation
- describe power efficient accessing mode
- introduce minimal control and sensing circuitry
- describe method for reading target memory cell
- calculate actual value of target memory cell
- estimate component of read value caused by sneak path current
- read value of initial memory cell
- calculate component of read value caused by sneak path current
- store known value in dummy memory cell
- read value of dummy memory cell
- calculate component of read value caused by sneak path current
- identify row and column of high-density gateless array
- connect remaining rows to first common node
- connect remaining columns to second common node
- bias rows and columns to predefined voltages
- describe apparatus for reading target memory cell
- execute computer-executable instructions
- calculate component of read value caused by sneak path current
- describe computer program product
- execute computer-executable instructions
- provide apparatus with means for reading and calculating

## DETAILED DESCRIPTION

- describe patent application structure

### Sneak Paths Analysis

- motivate sneak-paths problem
- describe crossbar accessing modes
- introduce equivalent circuit for sneak-paths
- discuss limitations of floating terminals mode

### Sneak-Paths Correlation

- derive sneak-paths resistance equations
- discuss row and column resistance components
- analyze relative change in row resistance
- plot maximum relative change versus array size
- discuss effect of number of ones on sneak-paths resistance

### Adaptive-Threshold Readout

- motivate adaptive threshold readout
- describe connected terminals circuit model
- simplify circuit model for VB terminal bias
- define sense current and sneak-current components
- discuss role of sneak-paths correlation in readout

### Multi-Read for Initial Bits

- motivate multi-read approach
- categorize bits into initial and regular bits
- describe readout procedure for initial bits
- calculate threshold from initial bit readout
- discuss readout sequence for array

### Predefined Dummy Bits

- motivate predefined dummy bits approach
- describe organization of dummy bits
- estimate adaptive threshold from dummy bit
- discuss readout sequence for array
- compare overhead of initial and dummy bits methods
- plot average number of readouts per memory bit
- discuss convergence of average readouts to one
- show negligible overhead of dummy bits
- discuss simulation platform for crossbar readout

### Crossbar Power Consumption

- discuss undesirable sneak-paths power consumption
- show power savings of connected terminals technique

### Figure-of-Merit

- define figure-of-merit for readout techniques

### Operations Performed by a Computing Device to Efficiently Perform Readout Operations

- illustrate flowchart of operations
- introduce apparatus performing operations
- calculate sneak path current component
- estimate initial memory cell value
- read initial memory cell value
- calculate sneak path current component (alternative)
- store known value in dummy memory cell
- read dummy memory cell value
- read target memory cell value
- identify row and column of target memory cell
- connect rows and columns to common nodes
- bias rows and columns to predefined voltages
- calculate actual target memory cell value
- repeat operations for multiple memory cells
- summarize advantages of readout technique

