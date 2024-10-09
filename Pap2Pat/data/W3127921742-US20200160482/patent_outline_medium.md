# DESCRIPTION

## FIELD OF THE DISCLOSURE

- define field of disclosure

## BACKGROUND

- introduce imaging and vision systems
- limitations of traditional vision systems

## SUMMARY

- motivate near-sensor architectures
- describe thermal implications of near-sensor processing
- propose thermal management control policies
- summarize embodiments of runtime controller

## DETAILED DESCRIPTION

- introduce embodiments of the disclosure
- define terms and concepts used in the disclosure
- describe the problem of energy-expensive off-chip data movements
- motivate near-sensor processing for energy efficiency
- characterize thermal implications of using 3D stacked image sensors with near-sensor VPUs
- reveal opportunities for regulating temperature based on dynamic visual task requirements
- propose and investigate two thermal management control policies
- present parameters that govern policy decisions
- explore trade-offs between system power and policy overhead
- evaluate novel dynamic thermal management strategies
- describe a runtime controller for controlling an operational mode of a vision or imaging system
- translate fidelity demands into effective thermal management
- apply application-specific requirements into policy parameters
- activate temperature reduction mechanisms
- continuously adapt policy parameters to situational settings
- characterize relationships between near-sensor processing power and sensor temperature
- reveal a consequential insight: removing near-sensor power results in an immediate and dramatic reduction in transient junction temperature
- describe imaging-specific control policies for thermal management
- evaluate the effectiveness of control policies for managing sensor temperature
- demonstrate the robustness of exemplary embodiments in smoothly handling dynamic fidelity needs
- introduce thermal management for 3D stacked vision sensor
- motivate thermal noise impact on image quality
- describe thermal characterization of sensor element
- illustrate noise sensitivity to temperature, exposure, and ISO
- discuss image fidelity needs for vision and imaging tasks
- summarize insights for near-sensor processing
- motivate need for novel dynamic thermal management strategies
- introduce control policies for thermal management
- describe principles for managing sensor temperature
- discuss situational temperature regulation
- discuss on-demand fidelity and system power minimization
- illustrate power consumption at various duty cycles
- describe stop-capture-go control policy for near-sensor processing
- discuss seasonal migration control policy for thermal management
- introduce stop-capture-go policy
- motivate temperature regulation
- describe policy parameters
- discuss limitations of stop-capture-go
- introduce seasonal migration policy
- describe policy parameters
- discuss thermal isolation
- derive duty cycle and frequency of migration
- discuss implementation considerations
- introduce Stagioni runtime controller
- describe API for application-specific fidelity needs
- discuss runtime controller operation
- illustrate process for thermally managing vision system
- describe simulation framework
- describe emulation framework
- evaluate control policies
- discuss vision tasks
- discuss metrics and policies
- discuss environment conditions
- illustrate power impact of control policies
- discuss policy execution overhead
- illustrate situational awareness features
- discuss power profile of VPU choices
- discuss future extensions
- conclude near-sensor processing benefits

