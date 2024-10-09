# DESCRIPTION

## BACKGROUND OF THE INVENTION

- introduce compressive sensing and video compressive sensing

### 1.2.1 Compressive Sensing

- define compressive sensing
- describe signal recovery
- mention algorithms for signal recovery

### 1.2.2 Video Compressive Sensing

- introduce video compressive sensing
- describe existing methods
- mention limitations of existing methods

### 1.2.3 Dynamic Textures and Linear Dynamical Systems

- introduce linear dynamical systems

## SUMMARY OF THE INVENTION

- motivate video compressive sensing
- introduce predictive modeling
- describe linear dynamical system model
- outline method for capturing video sequence
- mention other embodiments
- highlight advantages

## DETAILED DESCRIPTION OF THE PREFERRED EMBODIMENTS

- introduce notation
- motivate LDS models
- describe CS-LDS framework
- outline measurement process
- estimate state sequence using SVD
- recover observation matrix using CoSAMP
- discuss structured sparsity and recovery
- analyze performance and measurement rate
- describe extensions to mean+LDS and residual correction
- present experimental results
- discuss applications to non-LDS data

### 4.5.1 Mean+LDS

- modify algorithm for mean+LDS model

### 4.5.2 Residual Correction

- perform residual recovery on each frame
- estimate frame using observation matrix and state sequence
- perform l1 recovery on residue
- obtain new estimate of frame
- require large number of measurements
- estimate beyond support of C

