# DESCRIPTION

## BACKGROUND OF THE INVENTION

- introduce compressive sensing and video compressive sensing

### 1.2.1 Compressive Sensing

- define compressive sensing
- describe signal y and measurement matrix Φ
- explain restricted isometry property (RIP)
- introduce convex problem for signal recovery
- discuss compressible signals
- mention various algorithms for signal recovery

### 1.2.2 Video Compressive Sensing

- introduce video compressive sensing
- describe existing methods for video CS
- explain snapshot imager and single pixel camera
- discuss various video CS algorithms
- mention limitations of existing methods
- relate video CS to background subtraction problem

### 1.2.3 Dynamic Textures and Linear Dynamical Systems

- introduce linear dynamical systems (LDS)
- describe LDS model for dynamic textures
- mention applications of LDS models

## SUMMARY OF THE INVENTION

- motivate video compressive sensing
- introduce predictive/generative signal models
- describe linear dynamical system (LDS) model
- explain advantages of LDS model
- introduce method for capturing video sequence
- describe common measurements
- describe innovation measurements
- estimate state sequence using SVD
- estimate observation matrix
- recover video sequence
- mention other embodiments
- describe method for efficient acquisition of correlated data sequences
- describe method for estimating parameters of interest

## DETAILED DESCRIPTION OF THE PREFERRED EMBODIMENTS

- introduce notation
- define LDS and its properties
- motivate LDS for video modeling
- describe CS-LDS framework
- outline measurement process
- define common and innovations measurements
- estimate state sequence using SVD
- recover observation matrix using CoSAMP
- describe CS camera implementation
- outline recovery of state sequence and observation matrix
- discuss low-dimensional projections of LDS data
- describe SVD-based estimation of state sequence
- discuss accuracy of state sequence estimation
- introduce structured sparsity and modified CoSAMP
- describe recovery of observation matrix using modified CoSAMP
- discuss performance and measurement rate
- describe extensions to CS-LDS framework
- outline mean+LDS model
- describe residual correction
- present experimental results
- discuss performance with measurement noise
- discuss application to non-LDS data

### 4.5.1 Mean+LDS

- modify algorithm for mean+LDS model

### 4.5.2 Residual Correction

- perform residual recovery on each frame
- define residual recovery problem
- describe l1 recovery of residue
- update estimate of frame
- discuss conditions for residual correction
- describe measurement rate requirement
- outline benefits of residual correction
- discuss limitations of residual correction
- describe experimental setup
- present experimental results
- discuss performance of residual correction
- compare with frame-to-frame CS
- discuss applicability to high-speed imaging

