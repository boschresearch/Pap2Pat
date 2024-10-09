# DESCRIPTION

## TECHNICAL FIELD

- define technical field of resource reservation

## BACKGROUND

- motivate real-time resource allocation
- describe limitations of current bidding platforms
- identify need for improvement

## SUMMARY

- summarize service-level agreement monitoring
- describe method of operating demand side platform
- determine current state of DSP
- receive bid request
- determine uncertainty of predicted user response
- determine risk tendency value
- determine adjusted value of advertisement impressions
- determine bid price
- transmit bid price
- receive auction result
- update current state of DSP
- describe DSP embodiment
- describe non-transitory computer-readable medium

## DETAILED DESCRIPTION

- illustrate electronic device 100
- describe components of electronic device 100
- explain RF transceiver 110 functionality
- describe TX processing circuitry 115 functionality
- explain RX processing circuitry 125 functionality
- describe main processor 140 functionality
- explain memory 160 components
- illustrate server 200
- describe components of server 200
- explain processing device 210 functionality
- describe memory 230 and persistent storage 235
- explain communications unit 220 functionality
- describe I/O unit 225 functionality
- illustrate network context 300
- describe electronic devices 301 functionality
- explain supply side platforms (SSPs) 305a-305n functionality
- describe real-time-bidding (RTB) ad exchange 310 functionality
- explain demand side platforms (DSPs) 315a-315n functionality
- describe data management platform (DMP) 320 functionality
- explain processing platforms 325 functionality
- illustrate operations of process 400
- receive bid request from ad exchange
- perform initial prediction of user response metrics
- adjust predicted value to account for uncertainty
- determine risk tendency of DSP
- calculate bid price based on uncertainty and risk tendency
- submit calculated bid price
- illustrate process 500
- receive bid request from ad exchange
- calculate mean predicted click-through-rate (pCTR)
- calculate standard deviation of pCTR
- model risk tendency of rational DSP
- determine risk tendency based on remaining auctions and budget
- specify sign of risk tendency based on budget sufficiency
- determine monotonicity of risk function
- apply approximation for equivalent states
- describe rule-based approach for risk tendency
- describe machine-learning based approach for risk tendency
- explain benefits of bid optimization
- describe limitations of historical approaches
- explain importance of considering uncertainty
- describe benefits of optimizing KPI
- explain importance of reducing network traffic and latency
- describe benefits of bid shading
- explain importance of modeling risk tendency
- describe benefits of using reinforcement learning
- summarize benefits of bid optimization according to this disclosure
- define β equation
- derive β from equations 1-3
- introduce tanh function
- define Û equation
- calculate Û from historical data
- introduce θ equation
- calculate θ using β
- describe benefits of θ calculation
- introduce reinforcement learning method
- define g(δ) function
- define V(t, b) function
- approximate V(t, b) using equation 8
- perform reinforcement learning
- determine bid price using equation 9
- submit bid and receive auction result
- update DSP state
- introduce self-supervised risk tendency learning framework
- train MLP to implement risk tendency function
- describe Gaussian exploration stage
- describe batch sampler
- train MLP using experience buffer
- calculate episode-level rewards
- update experience buffer
- describe process for performing real-time bid optimization
- determine current DSP state
- receive bid request
- determine predicted user response and uncertainty
- determine risk tendency value
- determine adjusted value of ad impressions
- determine optimum bid price and submit bid

