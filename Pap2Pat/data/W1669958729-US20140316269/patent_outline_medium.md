# DESCRIPTION

## RELATED APPLICATION DATA

- claim priority to provisional applications

## FIELD

- define field of invention

## BACKGROUND

- motivate ultrasound treatments

## SUMMARY

- introduce focused ultrasound systems
- describe system configurations
- explain ultrasound imaging and/or signal beacon tracking
- outline variations of methods, devices, and systems
- describe ultrasound delivery system with transducer array
- detail detector and actuator components
- explain computing unit and ultrasound transceiver module
- describe ultrasound transducer array configurations
- outline therapeutic ultrasound system with applicator
- detail first and second orientation sensors
- describe water conditioner and detector components
- outline method of delivering focused ultrasound
- describe determining treatment plan and moving ultrasound array
- explain verifying orientation changes
- detail method of delivery of focused ultrasound field
- describe generating phase and power tables
- outline tracking target position
- describe method for delivery of focused ultrasound to treatment site
- detail pulse-width modulating electrical energy
- explain adjusting pulse width modulation
- describe ultrasound therapeutic system with output drive circuitry
- outline computing unit adjustments
- describe ultrasound device with housing and interface
- detail treatment transducer array and actuators
- outline therapeutic ultrasound system with ultrasound transducer unit
- describe tracking beacon position
- explain acoustic time of flight calculation
- introduce therapeutic ultrasound transducer
- describe transducer elements and substrate
- detail three-dimensional printing process
- outline processor configuration and functionality
- describe imaging probe and fiducials
- explain processor input and output
- detail calibration procedure
- describe algorithm for tracking region of interest
- outline modulation techniques for output pulse
- describe electromechanical mover and therapeutic ultrasound transducer
- detail system configuration and components
- describe detector and actuator functionality
- outline ultrasound transceiver module and detector connection
- describe mover and applicator configuration
- detail system components and functionality
- conclude system description

## DETAILED DESCRIPTION

- introduce patent application structure
- explain scope and limitations of invention

### I. System Layout

- introduce therapeutic ultrasound system
- describe system configuration
- detail generator components
- explain generator functions
- describe water conditioner components
- explain water conditioner functions
- introduce treatment transducer array
- describe treatment transducer array movements
- detail applicator and acoustic coupling interface
- describe treatment module components
- explain treatment module functions
- introduce patient platform and treatment module interaction
- describe treatment process with beacon tracking
- describe treatment process with imaging tracking

### II. System Functionality

- describe GUI functionality
- introduce secondary GUI
- describe image detector functionality
- summarize camera monitor functionality
- illustrate system configuration
- describe generator functionality
- introduce ultrasound transceiver module
- describe treatment transducer array functionality
- summarize water conditioner functionality
- outline treatment process
- describe targeting catheter functionality
- summarize applicator positioning process
- describe therapeutic system functionality
- introduce computing unit functionality
- describe electronic interface board functionality
- summarize treatment module functionality
- describe generator components
- illustrate system block diagram
- describe ATOF amplification chain
- describe system functionality
- monitor electric current drawn by generator
- detect position and/or orientation of treatment array
- determine treatment plan with predefined treatment pattern
- deliver focused ultrasound energy to treatment region
- verify changes in orientation of treatment array
- calculate required movement of treatment array
- monitor orientation of applicator
- detect movement of applicator
- integrate therapeutic array and system
- generate control parameters for system
- modify control parameters during calibration
- locate target region to be treated
- track target tissue and maintain focus
- calculate dosage of focused ultrasound
- adjust position of applicator for target depth minimization
- conduct post-treatment evaluation
- generate phase table for focal positions
- generate power table for power requirements
- combine phase and power tables
- determine element geometric center
- determine beam steering area and focal positions
- calculate phase angle for focusing control
- calculate phase angle using time delay method
- calculate phase angle using phase shift method
- generate gain setting values or voltage control parameters
- extract electrical impedances and phases of treatment transducer array
- implement pulse-width modulation for uniform power intensity
- describe pulse width modulation waveform
- determine pulse width modulation duty cycle
- adjust pulse width modulation for varying transducer element sizes
- determine electrical power distribution of array elements based on element impedance

### III. Treatment Transducer Array

- describe treatment transducer array designs
- configure array geometry for specific ultrasound field patterns
- deliver specific ultrasound energy to focal point
- turn off selective transducers to adjust ultrasound field pattern
- describe transducer unit components
- illustrate transducer array unit components
- describe fan-shaped treatment transducer array
- illustrate concentric pattern of transducer array elements
- describe AFTOF receiver transducer array elements
- illustrate AFTOF receiver transducer array elements
- describe ATOF subsystem components
- illustrate ATOF detection algorithm process
- configure ATOF subsystem parameters
- introduce treatment transducer array
- describe actuator and control system
- illustrate fan shaped configurations of transducer array designs
- describe array with six sub-lobes
- describe array with diced configuration
- describe array with concaved surface profile
- illustrate delivery of focused ultrasound energy
- describe fan shaped transducer array design with curved elements
- describe concaved profile transducer array integrated in treatment module
- describe imaging transducer array
- describe concaved base support with honeycomb structure
- describe three-dimensional fabrication process
- describe random set of piezoelectric elements on spherical bowl
- describe single element transducer
- describe therapeutic array with phase control
- illustrate simulations of focal spot of array
- describe ability to move focus with phasing alone
- describe flat, two-dimensional array
- describe angled individual transducer elements
- describe multi-element therapeutic ultrasound transducer
- describe associated ultrasound imaging probe
- describe fiducials on imaging transducer
- describe functionality of arrays
- describe three-dimensional processing and manufacturing
- describe calibration process

### IV. Tracking Beacon

- introduce tracking beacon concept
- describe beacon function in ultrasound treatment
- detail catheter configuration for beacon placement
- describe targeting catheter features
- illustrate catheter construction
- detail ultrasound emitter configuration
- describe transducer liner and flare
- illustrate electronic tuning module
- detail tuning module components
- describe coax cable and handle configuration
- illustrate distal portion of catheter
- detail PZT transducer dimensions
- describe guide tubing and safety wire
- illustrate primary sheath tubing and lumens
- detail epoxy and adhesive use
- illustrate shrink-wrap tubing and excess removal
- describe targeting catheter placement in renal artery
- detail guide-wire insertion and catheter advancement
- describe beacon energization and signal transmission
- introduce variations with multiple beacons
- describe temperature sensing and detection
- outline process for placement of targeting catheter
- introduce tracking beacon
- evaluate stability of targeting catheter beacon
- determine location of targeting catheter beacon
- describe shaped targeting catheter
- describe ultrasound energy detection
- describe complex patterns on catheter
- launch treatment procedure software
- configure treatment transducer array
- detect ultrasound signals from beacon
- calculate position of beacon
- adjust position of treatment transducer array
- select transducer array for treatment
- verify transducer array installation
- display position applicator screen
- adjust targeting catheter parameters
- optimize ATOF signals
- specify therapy plan
- calculate therapy plan
- initiate therapy delivery
- assess targeting quality
- perform pre-treatment angiogram
- describe imaging transducer array
- track target tissue with imaging transducer array

### VII. Control

- illustrate steps to perform focus ultrasound therapy
- introduce software configuration for therapeutic system
- describe treatment planning and delivery
- outline GUI and UI components
- explain hardware abstraction layer
- detail application layer functions
- describe cross-cutting layer services
- illustrate dynamic view of software system
- outline therapy system controller threads
- describe top-level states of therapeutic system
- illustrate patient session states
- explain condition handling process
- describe power-on self-test (POST)
- outline patient setup process
- describe therapy delivery process
- list hardware sub-systems supported by system software
- describe monitoring of system operational parameters
- outline condition handling facility
- describe applicator positioning assistance
- outline targeting and dosing capabilities

### VIII. System Conditioning and Boundary Conditions

- define condition
- categorize conditions
- describe workflow errors
- describe normal system corrections
- outline steps to address a condition
- define condition components
- prioritize conditions
- define recovery states
- describe detected states
- describe pause therapy states
- illustrate conditioning handling process
- describe error handler software
- describe error resolution state sequence

### IX. Treatment Module

- describe treatment module
- introduce treatment applicator
- detail mover A components
- explain mover A functionality
- describe treatment transducer array mover
- introduce membrane for coupling to patient's body
- detail handles and switches on treatment applicator
- explain Z-motion extend and release switch
- describe inflate and deflate switch for membrane
- introduce base lock and release switch
- detail tubing for coupling fluid and air channels
- describe momentary-rocker switches on hand grips
- introduce exploded view of applicator
- detail nosecone and treatment array unit
- describe actuation unit and base plate
- introduce ball joint and piston
- detail stepper motors and push rods
- describe mechanical joint with two degrees of freedom
- introduce treatment transducer unit
- detail ATOF receivers and treatment transducer array
- describe rotatable joint and push rods
- introduce joy stick control for treatment transducer unit
- detail internal modules of treatment transducer unit
- describe treatment array positioner subsystem

### X. Interface Cooling and Monitoring

- describe nosecone structure
- illustrate nosecone components
- explain fluid flow through nosecone
- describe image detector functionality
- illustrate image detector positioning
- explain image detector capabilities
- describe bubble detection process
- illustrate bubble detection flowchart
- describe image detector placement variations
- illustrate image detector placement on treatment array unit
- describe image detector usage for transducer array orientation detection
- describe image detector usage for membrane inflation detection
- describe image detector usage for patient movement detection
- describe image detector usage for treatment module placement
- describe image detector usage for beam imaging
- describe image processing for bubble detection
- describe bubble removing device

### XI. Water Conditioner

- introduce water conditioner
- describe components
- detail water conditioning components
- detail air pressure and vacuum components
- detail electrical components
- describe power supply
- describe communication ports
- describe control of coupling fluid pressure
- describe pressure sensors
- describe air flow and suction control
- describe air flow sensors
- illustrate water conditioner sub-system
- describe dry box assembly
- describe wet box assembly
- describe membrane contactors
- describe vacuum and pressure chamber
- describe water reservoir and chiller
- describe power entry enclosure
- introduce water conditioner
- describe operator control over treatment planning and control subsystem
- detail therapeutic focal spot alignment
- describe DC power monitoring
- introduce lesion pattern generation
- describe pattern construction
- detail overlapping lesion pattern
- calculate acoustic output power level
- describe power calculation parameters
- detail intra-lesion cycle
- describe tracking and targeting quality
- introduce safeguards against excessive dose administration
- detail sequence of operations for setting and delivering a specific dose
- describe additional safeguards and monitoring
- introduce phase aberration correction
- describe phase aberration correction process
- detail phase aberration correction RF signal acquisition
- describe phase aberration correction signal processing
- detail performance improvements in water tank
- describe processor functionality
- conclude with variations and scope of invention

