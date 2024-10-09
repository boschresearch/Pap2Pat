# DESCRIPTION

## FIELD OF THE INVENTION

- introduce hypotensive episode prediction

## BACKGROUND OF THE INVENTION

- describe acute hypotensive episodes
- discuss causes of acute hypotensive episodes
- highlight importance of predicting acute hypotensive episodes

## SUMMARY OF THE INVENTION

- introduce method of predicting acute hypotensive episodes
- describe generation of acute hypotension prediction classifier
- explain calculation of mathematical index
- mention alarm signal generation

## DETAILED DESCRIPTION OF THE INVENTION

- introduce ECG biomarkers processing subsystem
- describe ECG signal processing
- calculate RR', JT', and QRS' intervals
- normalize JT and QRS data
- form matrix An for every cardio cycle
- calculate dsk(JTn,QRSn) for every cardio cycle
- calculate biomarkers J and V
- process J and V data series
- form data array A{ti, 1...N}
- update data periodically
- form J and V data points distribution field array
- calculate density of J and V data points
- segment limited area
- calculate 2D array of data points distribution density
- calculate contour plot
- calculate contour area
- calculate centroids coordinates
- calculate maximum value of density function
- accumulate data within set time interval
- store reference set of data
- track and visualize centroids
- calculate cross-correlation function
- calculate correlation coefficient
- determine peak coordinates
- calculate 2D auto-correlation function
- determine reference peak coordinates
- calculate Euclidean distances ΔE1
- calculate Euclidean distances ΔE2
- calculate Euclidean distances ΔE3
- calculate root mean square (RMS)
- compare monitored factors with critical threshold values
- form alarm signal
- describe integrated alarm
- discuss clinical validation of the invention

