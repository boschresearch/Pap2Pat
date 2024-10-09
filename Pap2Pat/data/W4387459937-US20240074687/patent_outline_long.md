# DESCRIPTION

## FIELD OF THE DISCLOSURE

- define field

## BACKGROUND OF THE DISCLOSURE

- motivate neural oscillations
- limitations of traditional approach
- limitations of existing methods
- importance of three criteria

## SUMMARY OF THE DISCLOSURE

- introduce oscillation detection method
- summarize three criteria
- application of method
- describe method's features

## DETAILED DESCRIPTION

- introduce neurophysiological signals
- define neurophysiological signal or neural signal
- motivate oscillation detection
- define oscillation
- illustrate challenges of detecting non-sinusoidal oscillations
- describe limitations of existing methods
- introduce disclosed oscillation detection method
- receive neurophysiological signal data
- identify oscillations based on three criteria
- transform raw time series into time-frequency space
- remove 1/f pink noise from EM data
- identify potential periodic signals
- enclose contiguous regions with spectral power above threshold
- evaluate candidate oscillations
- perform autocorrelation for data within bounding boxes
- identify center frequency within each selected bounding box
- retain oscillations with same frequency as autocorrelation
- yield onset time, offset time, center frequency, frequency range, number of cycles, and degree of asymmetry
- identify multiple oscillations from EM electrode readings
- group oscillations by frequency range
- produce normalized power map
- compare disclosed method with existing methods
- illustrate topographic patterns of oscillation detection
- simulate wave time histories
- evaluate performance of disclosed method and existing methods
- illustrate advantages of disclosed method
- describe computing systems and devices for implementing disclosed method
- illustrate block diagram of computing device
- describe components of computing device
- describe processor 605
- describe communication interface 615
- describe storage device 625
- describe storage interface 620
- describe memory areas 510 and 610
- discuss computer systems and methods
- introduce machine learning
- describe machine learning module
- discuss data inputs
- discuss machine learning methods and algorithms
- describe supervised learning
- describe unsupervised learning
- describe reinforcement learning
- discuss implementation of machine learning
- discuss computer programming and engineering techniques
- describe computer-readable media
- discuss machine instructions and data
- define processor
- define software and firmware
- discuss system execution environments
- discuss system components and distribution
- discuss definitions and methods
- discuss numerical parameters and values
- discuss use of terms such as "a" and "an"
- discuss open-ended linking verbs
- discuss method steps and order
- discuss use of examples and exemplary language
- discuss groupings of alternative elements
- discuss incorporation of references
- discuss modifications and variations
- discuss equivalent embodiments
- conclude description of present disclosure

### EXAMPLES

- introduce examples of present disclosure
- motivate novel oscillation detection method
- describe limitations of traditional methods
- outline novel method's three principle criteria
- evaluate method's performance on simulated signals
- test method on electrocorticographic and electroencephalographic signals
- introduce targeted neurofeedback application
- describe high specificity requirements for neurofeedback
- outline phase-locked electrical stimulation application

