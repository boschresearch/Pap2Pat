# DESCRIPTION

## FIELD OF THE INVENTION

- relate to space-time encoded spread spectrum communication systems

## BACKGROUND

- introduce MIMO systems
- describe BLAST system
- explain V-BLAST
- discuss receiver design for MIMO systems
- describe LMMSE algorithm
- describe Kalman filter algorithm
- discuss characterization of MIMO link
- explain link-to-system mapping
- classify MIMO transmission schemes
- discuss SNR vs. FER mapping issue
- describe prior art solutions for SISO systems
- describe prior art solutions for MIMO systems with separate encoding
- identify need for CQI in JE MIMO systems

## SUMMARY OF THE INVENTION

- introduce method for detecting jointly encoded signal
- describe receiving and sampling signal
- explain filtering using CQI
- describe downconverting to bits and symbols
- introduce method for detecting symbols of jointly encoded signal
- describe receiving and sampling signal
- explain estimating multi-path channel
- describe filtering to restore orthogonality
- introduce method for adapting transmissions
- describe jointly encoding and modulating signal
- explain determining CQI and detecting symbols
- describe adapting transmission based on feedback

## BRIEF DESCRIPTION OF THE DRAWINGS

- describe drawings

## DETAILED DESCRIPTION

- introduce CQI for space-time jointly encoded MIMO CDMA systems
- describe limitations of RAKE receiver
- motivate linear filters to restore orthogonality of Walsh codes
- define constrained mutual information as CQI measure
- describe MIMO communication system 20
- illustrate transmitter 22 and receiver 26
- explain coding and modulation block 34
- describe spreading and scrambling blocks 36
- illustrate signal model at transmitter 22
- define signal model at mth transmit antenna 24
- describe signal model at receiver 26
- stack up received samples across all receive antennas
- define linear filters at receiver
- describe LMMSE equalizing filter
- define notation for block of received vectors
- rewrite signal model using new notation
- define covariance matrix of received signal
- define related matrix
- conclude signal model description
- introduce Vector Viterbi Algorithm (VVA)
- limitations of VVA
- motivate per Walsh code joint detection structure
- describe receiver structure
- define linear filter bank
- equalize multi-path MIMO channel
- perform chip-to-symbol down-conversion
- describe composite block
- generate soft bits for decoder
- detect bits from symbol vectors
- output soft decision bits
- describe log-likelihood ratios (LLR)
- motivate per-Walsh code joint detection approach
- describe complexity reduction
- optimize front-end linear filter
- use mutual information as measure of optimality
- describe LMMSE or MVDR solutions
- provide Channel Quality Indicators (CQI)
- assume Gaussian transmitted chip vectors
- maximize conditional mutual information
- prove theorem
- describe Data Processing Lemma
- provide upper bound on mutual information
- show achievability of bound
- describe signal model
- derive mutual information expression
- conclude optimality of filter
- define constrained mutual information
- motivate LMMSE and MVDR filters
- derive LMMSE filter solution
- derive MVDR filter solution
- prove mutual information maximization
- describe transmitter architecture
- explain feedback mechanism
- detail CQI calculation
- describe MIMO link mapping methods
- introduce Generalized SNR (GSNR)
- derive GSNR equation
- introduce constrained mutual information as CQI
- derive symbol-level mutual information equation
- discuss chip vs. symbol mutual information
- describe simulation setup
- present simulation results
- compare coded VBLAST and PARC schemes
- discuss link adaptation
- describe simulation parameters
- present throughput comparison
- discuss link-to-system mapping
- introduce FER(CQI) curves
- describe simulation setup for link-to-system mapping
- present FER(GSNR) curve
- present FER(constrained mutual information) curve
- compare GSNR and constrained mutual information
- summarize disclosure
- discuss advantages of constrained mutual information
- discuss applications of disclosure
- provide background information
- discuss prior art
- describe scope of invention
- provide concluding remarks

