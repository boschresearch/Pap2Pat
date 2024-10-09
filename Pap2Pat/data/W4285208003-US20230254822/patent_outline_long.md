# DESCRIPTION

## TECHNICAL FIELD

- relate to wireless communications

## BACKGROUND

- describe D2D communication modes
- explain limitations of scheduled resource allocation
- explain limitations of autonomous resource selection
- describe out-of-coverage situations
- explain limitations of 3GPP standard LTE-A Release 14
- identify need for improved D2D communication

## SUMMARY

- introduce improved D2D communication devices and methods
- describe user equipment for wireless communication network
- describe network entity for allocating radio resources
- describe corresponding methods
- explain exploiting radio resource management control
- describe Extended Mode 3 operation
- describe interaction with Mode 4 operation
- improve OOC Mode 4 resource allocation
- provide information about OOC events
- increase reliability and efficiency of D2D communication
- describe user equipment with communication interface
- describe processing unit for operating UE
- describe switching between modes
- describe first and second conditions
- describe OOC event
- describe scheduled resource allocation mode
- describe autonomous resource selection mode
- describe memory for storing operation profiles
- describe operation profiles
- describe unexpected OOC event
- describe expected OOC event
- describe using active SPS configurations
- describe using allocated resources
- describe selecting resources for expected OOC event
- describe using one-shot schedule
- describe operating first mode in parallel with second mode
- describe sensing load of resources
- describe replacing transmission on resources
- describe meeting second condition
- describe sensing load of resources and recording information
- describe providing information to network entity
- describe using downlink resources

## DETAILED DESCRIPTION OF EMBODIMENTS

- introduce D2D or V2V communication network
- describe user entity (UE) and network entity (base station)
- explain D2D/V2V communication types (periodic/aperiodic messages)
- describe centralized network infrastructure entity (base station)
- explain modes of operation and resource pools for in-coverage/OOC communications
- describe configuration information broadcast via system information messages
- determine if user is out of coverage (received powers, RRC signaling, map information)
- store information centrally or in a cooperating manner
- allocate resources via scheduled mode of operation (Mode 3)
- describe dynamic or semi-persistent schedule (SPS) for periodic V2V traffic
- report V2V traffic pattern information to network entity
- collect location information and channel busy ratio (CBR) measurement reports
- adapt transmissions based on CBR measurements
- show schematic diagram of communication network (FIG. 1)
- describe UE implementation (mobile phone, vehicle, communication module)
- describe network entity implementation (base station)
- explain communication interface and processing unit of UE
- describe operation modes (scheduled resource allocation, autonomous resource selection)
- explain switching between modes based on conditions (OOC event, time elapsed, distance travelled)
- describe network entity providing operation profiles associated with expected OOC event
- store operation profiles in UE memory
- operate UE in first mode according to default operation profile
- determine size of resource pools based on information from another UE
- map resource pools to moving zones (e.g., timer, START/STOP times)
- allocate downlink resources for first mode and/or second mode
- operate UE in first mode according to another default operation profile (unexpected OOC event)
- operate UE in first mode using active SPS configurations and allocated resources
- operate UE in first mode according to operation profile associated with expected OOC event
- operate UE in first mode using active SPS configurations and allocated resources (expected OOC event)
- operate UE in parallel with second mode (autonomous resource selection)
- sense load of resources for second mode and replace transmission on resources allocated for first mode
- sense load of resources allocated for first mode and meet second condition
- record information about times and/or locations and provide to network entity
- use downlink resources in second mode (autonomous resource selection)
- transmit information about number of next transmissions of same type
- transmit information about number of upcoming transmissions
- show schematic diagram of communication network (FIG. 2)
- describe out-of-coverage (OOC) events and radio resource management control
- describe steps for managing radio resources in response to OOC event
- show schematic diagram of communication network (FIG. 3)
- describe Type I OOC event (unexpected or unknown by network entity)
- describe Type II OOC event (expected or known by network entity)
- show schematic diagram of communication network (FIG. 5)
- describe resource allocation and utilization for providing semi-persistent-schedule (SPS) and one-shot schedule
- describe embodiments of network entity 131
- improve OOC resource pools configuration
- map moving zones to OOC resources
- configure OOC resource pools with timer
- include downlink spectrum in resource pool
- allocate resource pools from downlink spectrum
- configure OOC pools to avoid interference
- signal OOC pool configuration to UEs
- improve autonomous resource selection procedure
- reserve and announce actual number of transmissions
- provide information about OOC event to network entity
- perform additional measurements out of coverage
- collect and report data regarding OOC events
- exchange information regarding OOC events
- describe procedure for V2V communication
- measure UE power and collect RRC signaling
- signal information about OOC events to base station
- configure OOC pools with extra information
- switch to extended mode 3
- operate mode 4 in parallel with extended mode 3
- perform sensing on extended mode 3 resources
- reserve exact number of transmissions
- check for collisions on extended mode 3 transmissions
- release pre-scheduled extended mode 3
- check for collisions or congestions on mode 4 transmissions
- preempt or skip extended mode 3 transmission
- describe procedure for V2V communication with multiple base stations
- configure SPS with timer for OOC event
- illustrate resource allocation and utilization based on SPS configuration

