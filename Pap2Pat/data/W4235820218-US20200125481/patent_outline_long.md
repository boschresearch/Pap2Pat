# DESCRIPTION

## FIELD OF TECHNOLOGY

- define screen recording preparation method

## BACKGROUND

- motivate user session recording
- describe screen recording process
- limitations of manual evaluation
- summarize US2016378642A1
- limitations of US2016378642A1
- summarize WO2007056373A2
- limitations of WO2007056373A2
- summarize EP2713290A2 and WO2017123203A1

## SUMMARY

- introduce screen recording preparation method
- describe method for evaluating software usability
- outline initial phase of method
- load screen recording from storage medium
- detect visual features within screenshots
- create set of metadata containing screenshot identifiers and features
- set threshold similarity value and local similarity threshold value
- outline cycling phase of method
- compare consecutive screenshots for similarity
- attribute similar screenshots to screenshot cluster
- save information defining screenshot cluster
- reinitialise cycling phase
- explain importance of separating method into initial and cycling phases
- describe advantages of using metadata
- outline possibility of real-time preparation of screen recording
- describe independence of initial and cycling phases
- outline further analysis on metadata
- describe input of screen recording from user session
- explain loading of screen recording from storage medium
- define screenshot clusters
- explain analysis of user behaviour
- describe calculation of similarity value
- outline advantages of method
- describe suitability for usability analysis of software applications
- outline use for analysing smartphone applications
- describe reliability of clustering based on visual features
- outline detection of visual features
- describe algorithms for feature detection
- outline classification of common features
- describe identification of fixed regions
- outline stitching of screenshots
- describe updating of position information
- introduce fixed elements in web pages and software applications
- identify fixed regions by comparing screenshot features
- save extended screenshot with identifying information
- calculate shift vector for stitching screenshots
- determine scroll height using feature points
- combine individual frames to form extended screenshot
- analyze extended screenshot for efficiency
- remove fixed regions to prevent falsified representation
- identify fixed regions using convex contour
- correct fixed region shape and position
- define fixed features as outliers
- update position information of additional data
- assign screenshot cluster to extended screenshot
- compress data for efficient analysis
- create identification vector for screenshot cluster
- include identification vector in database
- analyze identification vectors for user data evaluation
- remove identification vectors from memory
- analyze identification vectors using index search algorithms
- create identification vector using TF-IDF concept
- compare identification vectors for similar screenshot clusters
- measure similarity using cosine similarity measurement
- cluster screenshots using identification vectors
- compare screenshots using identification vectors
- recognize similar screenshots
- aggregate user data for analysis
- set fixed screen width for comparing data
- load additional data for user session
- attribute additional data to screenshot cluster
- overlay screenshot with additional data
- display resulting image using web-based application
- visualize additional user data

## DETAILED DESCRIPTION

- introduce setup for recording user session
- describe display device and screenshot components
- illustrate sequence of screenshots
- show computing system architecture
- describe processor function
- illustrate method steps
- load screen recording
- detect visual features
- create metadata
- set threshold similarity value
- compare screenshots for similarity
- attribute similar screenshots to cluster
- save cluster information
- classify features as fixed or scrolled
- identify fixed regions and stitch screenshots
- create identification vector for cluster
- attribute additional data to cluster

