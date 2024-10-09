# DESCRIPTION

## BACKGROUND OF INVENTION

- introduce cardio-vascular disease
- describe limitations of EBCT
- motivate multi-slice/cone-beam CT
- describe limitations of gating based cardiac CT
- introduce cardiac micro-CT
- describe current small animal micro-CT work
- emphasize need for controlled cardiac CT

## BRIEF SUMMARY OF THE INVENTION

- introduce controlled cardiac CT
- describe synergy between CT and control
- outline goals of invention

## BRIEF DESCRIPTION OF DRAWINGS

- introduce drawings
- describe FIG. 1
- describe FIG. 2
- describe FIGs. 3-11
- conclude drawings description

## DETAILED DESCRIPTION OF THE INVENTION

- define terms and conventions
- describe FIG. 1: controlled cardiac CT/micro-CT system
- describe FIG. 2: source rotation control strategy
- outline adaptive control for cardiac motion
- describe periodic cardiac motion control
- describe quasi-periodic cardiac motion control
- describe non-exact matching to desirable projection angular positions

### A. Adaptive Control

- motivate cardiac motion control
- focus on periodic motion based control
- define heart volume and periodicity
- formulate problem: find source angle profile
- illustrate problem with numerical example
- show that constant source velocity may not exist
- modify problem to allow constant velocity with angle offsets
- solve modified problem with constant source rotation velocity
- implement solution using variable velocity X-ray source rotation
- describe polynomial solution
- illustrate solution with FIG. 4
- describe quasi-periodic cardiac motion
- formulate problem for quasi-periodic motion
- estimate periods from ECG signal
- design control scheme based on period estimates
- monitor and adjust source rotation velocity/acceleration
- illustrate method with example
- show computer simulation results in FIG. 6
- describe manual, semi-automatic, automatic, or mixed mode control
- illustrate control with graphical display
- describe heuristic rule for steering source
- automate rules using interpolation-based control strategy
- describe approximate matching to desirable projection angular positions
- define error bound and corresponding times
- define neighborhood of volume level
- define permissible time interval
- formulate non-exact match problem
- describe control algorithms using numerical search technique

### B. Image Reconstruction

- introduce Feldkamp-type reconstruction
- define Feldkamp algorithm
- provide mathematical formula for Feldkamp algorithm
- explain approximate reconstruction procedure
- describe step 1 of reconstruction procedure
- describe step 2 of reconstruction procedure
- describe step 3 of reconstruction procedure
- discuss limitations of Feldkamp algorithm
- introduce Grangeat-type reconstruction
- define Grangeat-type algorithm
- provide mathematical formula for Grangeat-type algorithm
- explain half-scan Grangeat-type reconstruction
- discuss data interpolation for Grangeat-type reconstruction
- introduce Radon space information
- explain data filling in shadow zone
- discuss artifact suppression
- introduce controlled cardiac CT
- explain synchronization of x-ray source rotation and data acquisition
- describe numerical tests using cardiac phantoms
- present simulation results for thorax phantom
- present simulation results for motion phantom
- summarize advantages of variable velocity method

