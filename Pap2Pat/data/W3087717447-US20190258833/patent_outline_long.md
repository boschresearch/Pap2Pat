# DESCRIPTION

## BACKGROUND

### Technical Field

- introduce RF energy harvesting

### Description of the Related Art

- describe RFID technology
- limitations of RFID tags
- antenna design trade-offs

## BRIEF SUMMARY

- motivate improved RFID solutions
- introduce self-tuning system
- extend communication range
- increase energy collection
- enable autonomous smart sensors
- provide energy-efficient solution
- develop smart RFID devices
- describe auto-tuning arrangement
- summarize benefits of embodiments

## DETAILED DESCRIPTION

- introduce embodiments of energy harvesting
- motivate low-power consumption
- describe RFID devices and IoT devices
- explain energy harvesting from environment
- describe RF harvesters and DC-DC converters
- discuss energy storage and low-power circuits
- motivate auto-tuning capability in energy-harvesting antenna
- describe scanning radio-frequency spectrum
- explain maximum power point tracking operation
- discuss antenna tuning capability and high Q
- describe RF harvester circuit and low-power consumption
- motivate tuning antenna/rectifier arrangement
- describe prior art auto-tuning circuit
- discuss limitations of prior art
- describe alternative arrangements using bank of capacitors
- discuss power spectrum available in urban environment
- describe block diagram of RF energy harvester arrangement
- explain DC-DC converter and storage element
- describe control circuit and procedure
- provide circuit-level representation of arrangement
- explain relationships between power levels and voltages
- describe impedance of antenna and rectifier
- discuss voltage and current signals
- explain converter efficiency and threshold loss
- describe operation of DC-DC converter in discontinuous mode
- describe converter operation
- describe DC-DC control
- motivate embodiment recognition
- describe input impedance dependence
- describe power dependence
- describe impedance matching
- describe quality factor role
- describe detuning effect
- describe rectifier operation
- describe tuning benefits
- describe antenna tuning
- describe converter off state
- describe input impedance dependence
- describe effective tuning
- describe auto-tuning operation
- describe global maximum search
- describe tuning capacitor control
- describe peak-power-based tuning
- describe tuning capacitor implementation
- describe load current control
- describe power estimation
- describe frequency selection
- describe scanning process
- describe alternative comparator implementation
- describe current line circuit
- describe level shifter operation
- describe power estimation method
- introduce resistive load
- explain threshold value calculation
- describe voltage and current relationships
- introduce analog-to-digital converter
- explain power calculation
- describe step-wise load reduction
- explain power evaluation
- describe power consumption assumption
- explain threshold voltage calculation
- describe power estimation steps
- explain power evaluation results
- describe power index calculation
- explain frequency band identification
- describe harvester circuit operation
- introduce flowcharts for tuning procedure
- describe sweep load and sweep frequency approaches
- describe negative outcome of check in act 104
- store value of highest available power for each frequency band
- vary tuning frequency according to frequency scanning plan
- skip certain frequencies/tones for various reasons
- check if frequency scanning schedule has been completed
- return to act 102 if further frequency bands/tones remain to be scanned
- identify highest power level available and best frequency band/tone
- process ends after a number of iterations
- adopt practically any desired preset frequency default value
- facilitate non-linear scanning of load values and frequency values
- perform same actions as acts 100 and 102 in FIG. 7
- check if VHARV is higher than VTHR
- store power value and vary frequency
- check if planned scanning of frequencies has been completed
- return to act 202 if frequency scan loop still has to be completed
- exclude frequency values NFREQ for which VHARV was found to be lower than VTHR
- increase value for NPHARV
- check if harvester load loop has been completed
- return to act 202 if load loop still has to be completed
- identify highest power level available and best frequency band/tone
- process ends after a number of iterations
- facilitate dual-step start-up solution
- provide circuit that identifies available power level at output of RF rectifier
- tune antenna to best sub-frequency band or tone with highest available energy
- detect total available power and activate converter and/or separate charge storage circuitry
- improve reliability by avoiding undesired discharging of battery or tank capacitor
- obtain RF power measurements by means of simple low-power circuit
- include string of switchable resistors that load RF rectifier output
- provide information about available input power
- identify frequency providing highest RF energy
- stabilize signal POK by avoiding ringing phenomena
- decide how to proceed using state machine
- keep DC-DC converter in off state during calibration phase
- switch off frequency scan circuitry and activate converter
- apply to wide variety of devices for use in logistics, asset tracking, life sciences, and monitoring applications

