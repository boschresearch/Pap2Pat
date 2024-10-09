# DESCRIPTION

## BACKGROUND OF THE INVENTION

- introduce 5G mobile network
- describe eMBB, mMTC, and URLLC
- motivate flexible air interface
- describe limitations of OFDM
- introduce flexible waveform parametrization
- discuss channel conditions and use cases
- describe importance of numerology design
- discuss inter-numerology interference (INI)
- motivate need for improved system and method

## SUMMARY OF INVENTION

- introduce system and method for reducing INI
- describe adaptive guards and multi-window operation
- summarize method for improved OFDM signal transmission
- identify numerology of users
- identify power offset and required SIR
- optimize guard band and duration
- generate OFDM signal
- describe multi-window approach
- perform interference-based scheduling
- describe apparatus with integrated circuit devices
- describe non-transitory computer readable storage medium
- summarize benefits of present invention

## DETAILED DESCRIPTION OF THE INVENTION

- introduce OFDM-based system
- describe significance of adaptive guards
- motivate transmitter windowing operation
- describe windowing approach
- define key parameters for guard allocation
- jointly optimize guards in time and frequency domains
- provide interference-based scheduling algorithm
- describe multiuser pulse-shaped OFDM system
- define numerologies and user equipments (UEs)
- describe transmitter windowing operation
- formulate RC window function
- describe roll-off factor (α)
- illustrate transmitter windowing operation
- describe need for guard bands
- define threshold for allowed interference level (θ)
- describe adaptive guard concept
- illustrate asymmetric interference scenario
- describe multi-window operation
- illustrate block diagram of apparatus
- describe parallel to serial (P/S) conversion
- apply left and right window functions
- combine subcarriers to generate OFDM symbol
- list remaining parameters of W-OFDM system
- describe interference-based scheduling algorithm
- generate power level and SIR requirements randomly
- describe PSD of W-OFDM signal
- illustrate effect of Δf on PSD
- illustrate effect of α on PSD
- describe INI management procedure
- illustrate required GB and GD amounts for selected θ values
- describe joint optimization of GB and GD
- define spectral efficiency (η)
- calculate efficiencies in time and frequency domains
- define optimization problem
- illustrate spectral efficiencies for selected θ values
- summarize optimal GB-GD pairs
- describe adaptive guard design
- describe interference-based scheduling methodology
- sort numerologies regarding subcarrier spacing (Δf)
- calculate similarity metric (β)
- sort β for numerologies with same subcarrier spacing
- allocate numerology with higher SIR requirement to edge
- describe example scenario with eight numerologies
- implement random scheduling strategy
- implement interference-based scheduling strategy
- compare and demonstrate effect of adaptive guards
- present numerical evaluation results
- conclude adaptive guard utilization

