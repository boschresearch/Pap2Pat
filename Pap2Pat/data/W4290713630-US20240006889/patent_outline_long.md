# DESCRIPTION

## FIELD

- define field

## BACKGROUND

- motivate PMSGs
- describe AC-DC converters
- limitations of diode bridge rectifier
- describe dc-dc converters
- limitations of two-level six-switch converter
- describe neutral-point-clamped converters
- describe flying-capacitor-based converters
- limitations of multilevel rectifiers
- describe reduced-switch multilevel rectifiers
- limitations of prior approaches
- describe MVDC collection grid
- describe sub-station-less architecture
- limitations of prior designs
- motivate integrated generator-rectifier systems
- describe prior integrated generator-rectifier systems
- limitations of prior integrated generator-rectifier systems
- motivate current invention

## SUMMARY OF THE INVENTION

- describe generator-rectifier system
- describe grid interface

## DETAILED DESCRIPTION OF THE PREFERRED EMBODIMENTS

- introduce integrated generator-rectifier topology/system
- describe connection of turbine to multi-port PMSG
- explain connection of each port to passive or active rectifier
- describe dc outputs of rectifiers connected in series
- highlight reduction in active rectification and elimination of bulky filter capacitors
- describe improvement in overall system efficiency, power density, and reliability
- introduce dc-grid interface circuit between integrated generator-rectifier and MVDC or HVDC grid
- describe isolated dc-dc converter at integrated generator-rectifier output
- mention preferred embodiment generator-rectifier systems and grid interfaces
- describe integrated multi-port generator-rectifier device
- explain grid-interface architecture with isolated dc-dc converter
- highlight reduction in switch VA rating requirement
- describe design to minimize VA rating requirement
- mention reduction in overall loss
- introduce maximum power point tracking control method
- describe active rectifier dc link voltage controller design
- mention implementation with full-bridge topology
- describe other isolated dc-dc converters (DAB, SAB, SRC)
- highlight shortcomings of DAB, SAB, and SRC topologies
- describe advantages of FB converter topology
- introduce integrated generator-converter architecture
- describe reduction in number of active switches and capacitors
- highlight optimization of total switch VA rating requirement
- describe integrated generator-rectifier architecture for harvesting energy
- mention majority of power processed by reliable, efficient, and inexpensive diodes
- introduce dc grid interface circuit and control strategy for maximum power point tracking
- describe experimental results validating converter architecture and control strategy
- highlight opportunities for integrating dc-collection networks with offshore wind farms
- introduce FIG. 1A showing preferred generator-rectifier system and grid interface
- describe components of FIG. 1A (wind turbine, multi-port PMSG, active rectifier, passive rectifiers, isolated dc-dc converters
- mention objective to minimize sum of VA rating of all active switches
- introduce equation for normalized active rectifier input current
- illustrate variation of Iac,pu with co for different numbers of ac ports k
- define total normalized switch VA rating
- derive VAConvI,pu
- derive VAConvII,pu
- derive VAact,pu
- formulate optimization problem
- solve optimization problem
- compute n1 and n2,opt
- illustrate variations of n1 and n2,opt
- illustrate minimum switch VA rating requirement
- highlight design points A, B, and C
- discuss reduction in total switch VA rating
- illustrate allowable duty ratio d for Converter II
- illustrate active rectifier output voltage
- describe 10-MW wind-turbine-driven multiport PMSG example
- calculate n1 and n2,opt for the example
- select semiconductor devices
- compare switch VA rating with conventional architecture
- discuss losses within individual converters
- compare conversion loss with conventional architecture
- describe control strategy
- model passive rectifiers and Converter I
- model active rectifier and Converter II
- derive equation for active rectifier input current
- describe Converter II control strategy
- discuss simulation results

