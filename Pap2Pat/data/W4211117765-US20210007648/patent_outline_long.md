# DESCRIPTION

## BACKGROUND

- introduce hematologic diseases
- describe anemia
- describe sickle cell disease
- discuss limitations of current hemoglobin tests
- introduce non-invasive point-of-care tools
- motivate need for non-invasive hemoglobin measurement

## SUMMARY

- introduce non-invasive hemoglobin measurement method
- acquire time-based series of images
- divide images into blocks
- generate time series signal
- identify PPG cycles
- process PPG cycles to determine hemoglobin levels
- calculate ratio of PPG signals
- identify features in PPG cycles
- use features to determine hemoglobin level
- introduce system for non-invasive hemoglobin analysis
- describe camera and lighting devices
- describe predictive model and processing

## DETAILED DESCRIPTION

- introduce photoplethysmogram (PPG) technique
- describe PPG system components
- explain PPG signal components
- motivate use of near-infrared (NIR) light
- describe tissue optical window
- introduce hemoglobin response
- introduce blood plasma response
- describe video camera capture of transmitted light
- extract pulsation response from video data
- convert video data to PPG signal
- acquire image data for PPG signal
- describe illumination of finger with NIR light sources
- capture light beams exiting ventral pad side of finger
- extract PPG signals from video data
- normalize PPG signals by dividing AC by DC components
- define R850 and R1070 ratios
- calculate ratio of R850 and R1070
- generate relationship between ratio and laboratory-measured hemoglobin values
- extract additional features from PPG signal
- pre-process data and identify region of interest in images
- extract frames from video
- subdivide each frame into blocks
- generate time series signal for each block
- apply bandpass filter to remove noise
- sample using Nyquist frequency
- filter data to remove areas of fluctuation
- define filtered and cropped signal as PPG signal
- extract features from PPG signal
- construct hemoglobin prediction model using Support Vector Machine Regression (SVR)
- define MAPE
- derive MAPE equation
- explain MAPE usage
- define correlation coefficient R
- derive R equation
- explain R usage
- describe Bland-Altman plot
- explain Bland-Altman plot usage
- describe model development
- explain data filtering
- describe LED light application
- explain video capture
- describe PPG feature computation
- explain feature normalization
- describe ratio calculation
- explain SVR application
- describe optimal prediction model development
- illustrate regression line
- describe comparative model results
- describe hemoglobin estimation procedure
- illustrate device block diagram
- describe device operation
- explain image data processing
- describe remote computer system
- explain data transfer methods
- describe mobile application
- illustrate light source configuration
- describe LED device configuration
- explain light restrictive enclosure
- describe device coupling methods
- explain system flexibility and variations

