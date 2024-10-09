# DESCRIPTION

## BACKGROUND

### Technical Field

- introduce RF energy harvesting

### Description of the Related Art

- summarize RFID technology

## BRIEF SUMMARY

- motivate improved RFID solutions
- introduce self-tuning system
- describe energy-efficient antenna tuning
- outline benefits of embodiments

## DETAILED DESCRIPTION

- introduce embodiments of energy harvesting
- motivate low-power consumption
- describe RF harvesters and energy storage
- discuss limitations of prior art auto-tuning circuits
- introduce auto-tuning capability in energy-harvesting antenna
- describe scanning radio-frequency spectrum for maximum power point tracking
- discuss antenna tuning capability and RF rectifier arrangement
- describe prior art analog auto-tuning circuit with linear loop
- discuss limitations of prior art auto-tuning circuit
- introduce block diagram of RF energy harvester arrangement
- describe circuit-level representation of RF energy harvester arrangement
- discuss operation of DC-DC converter in discontinuous mode
- describe converter operation
- explain DC-DC control
- motivate impedance matching
- discuss input impedance dependence
- explain quality factor impact
- describe rectifier operation
- motivate antenna tuning
- explain tuning capacitor control
- describe peak-power-based tuning
- explain capacitor bank implementation
- describe load current control
- explain power estimation
- describe alternative comparator implementation
- describe power estimation method
- introduce resistive load arrangement
- explain voltage threshold calculation
- detail iterative power estimation steps
- illustrate power consumption calculation
- describe power evaluation based on resistor configuration
- outline peak-power based tuning procedure
- summarize flowcharts for sweep load and sweep frequency approaches
- describe negative outcome of check in act 104
- store value of highest available power for each frequency band
- vary tuning frequency according to frequency scanning plan
- check if frequency scanning schedule has been completed
- identify highest power level available and best frequency band/tone
- process to END after number of iterations
- adopt preset frequency default value and non-linear laws for load and frequency variation
- perform frequency scan loop
- check if VHARV is higher than VTHR
- store power value and vary frequency
- check if planned scanning of frequencies has been completed
- exclude frequency values NFREQ for which VHARV was found to be lower than VTHR
- increase NPHARV and check if harvester load loop has been completed
- identify highest power level available and best frequency band/tone
- provide dual-step start-up solution
- facilitate providing circuit that identifies available power level at output of RF rectifier
- describe method of operating radiofrequency harvester circuit

