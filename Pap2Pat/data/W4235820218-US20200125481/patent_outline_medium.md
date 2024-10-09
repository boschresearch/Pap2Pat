# DESCRIPTION

## FIELD OF TECHNOLOGY

- define screen recording preparation method

## BACKGROUND

- motivate screen recording
- describe limitations of current methods
- summarize prior art US2016378642A1
- summarize prior art WO2007056373A2, EP2713290A2, WO2017123203A1

## SUMMARY

- introduce screen recording preparation method
- describe method for evaluating software usability
- outline initial phase of method
- detect visual features within screenshots
- create metadata containing screenshot identifiers and features
- set threshold similarity value and local similarity threshold value
- outline cycling phase of method
- compare screenshots for similarity using metadata
- attribute similar screenshots to screenshot cluster
- save information defining screenshot cluster
- reinitialise cycling phase
- discuss advantages of separating method into initial and cycling phases
- describe input screen recording and its encoding
- explain screenshot clustering and user behaviour analysis
- calculate similarity value and discuss its threshold
- outline method's applications and advantages
- introduce fixed elements in web pages and software applications
- identify fixed regions by comparing screenshot features
- stitch screenshots to form extended screenshot
- determine scroll height using feature points
- combine moved areas to form extended screenshot
- analyze extended screenshots efficiently
- identify and remove fixed regions
- define fixed features as outliers
- update position information of additional data
- define first screenshot as extended screenshot
- create identification vector of screenshot clusters
- include identification vector in database
- analyze identification vectors efficiently
- compare identification vectors to aggregate similar screenshot clusters
- load and attribute additional data to screenshot clusters
- overlay screenshot with additional data

## DETAILED DESCRIPTION

- introduce setup for recording user session
- describe display device and screenshot components
- illustrate computing system and storage medium
- outline method steps for screenshot clustering
- detail cycling phase for similarity comparison
- describe steps for classifying and stitching screenshots
- illustrate screenshot clustering and stitching examples
- outline method variations and aggregation of screenshot clusters

