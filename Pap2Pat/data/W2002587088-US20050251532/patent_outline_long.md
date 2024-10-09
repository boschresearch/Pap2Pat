# DESCRIPTION

## FIELD OF THE INVENTION

- define field of invention

## BACKGROUND OF THE INVENTION

- motivate multimedia event detection
- summarize prior art for news videos
- summarize prior art for situation comedies
- summarize prior art for sports video summarization
- summarize prior art for movie content
- summarize prior art for surveillance content
- list prior patents and applications
- highlight limitations of prior art
- identify need for generalized event detection
- outline desired requirements for multimedia summarization

## SUMMARY OF THE INVENTION

- introduce content-adaptive event detection
- outline unified learning framework

## BRIEF DESCRIPTION OF THE DRAWINGS

- describe figures

## DETAILED DESCRIPTION OF THE PREFERRED EMBODIMENT

- motivate unusual event detection
- introduce background and foreground events
- define usual and unusual events
- formulate problem of detecting unusual events
- describe segmentation using eigenvector analysis
- introduce affinity matrix
- define partitioning criterion for graph
- minimize Ncut
- describe Shi et al.'s method
- solve generalized eigenvalue system
- transform system into standard eigenvalue system
- obtain second generalized eigenvector
- estimate true density using kernel function
- describe mean squared error
- tradeoff between bias and variance
- use data-driven bandwidth selection process
- describe unusual event detection method
- extract features from multimedia
- label features using discrete labels
- treat features as time series
- sample time series using sliding window
- construct context model for each sample
- determine affinity matrix using context models
- determine second generalized eigenvector
- cluster distances related to events
- rank unusual events
- summarize content of multimedia
- describe affinity matrix for golf video
- consider issues in method
- choose statistical models for context
- determine confidence measure for detected unusual events
- quantify confidence measure for binomial and multinomial PDF models
- verify analysis using simulation
- describe clustering technique for gaining domain knowledge
- extract features from audio portion of sports video
- obtain distinguishable clusters for selected features
- identify consistent patterns in features for unusual events
- build supervised statistical learning models based on identified features
- demonstrate better results with selected class of features
- show example of framework for selection of classes of features
- analyze interaction between different clusters of features
- select relevant features for detecting unusual events
- describe theory behind minimum description length Gaussian mixture models (MDL-GMMs)
- derive objective function for obtaining optimal number of mixture components and model parameters
- estimate parameters K and θ
- describe confidence measure for GMM and HMM models
- model PDF of process using GMM or HMM
- define commutative distance metric to compare two context models
- use bootstrapping to obtain observations of distance metric
- use kernel density estimation to obtain PDF of distance metric
- rank outliers using confidence measures
- determine confidence metric for outlier context model
- identify useful features for detecting unusual events
- perform hierarchical clustering using normalized cut on affinity matrix
- partition affinity matrix into individual clusters
- construct affinity matrices for identified clusters
- apply spectral clustering to resulting affinity graphs
- reveal features using hierarchical clustering
- identify significant features of unusual events
- train GMM to model distribution of low-level cepstral features
- classify sports video into highlight and non-highlight segments
- rank every second of input sports video
- set highlights selection threshold
- get interesting time segments
- compare precision-recall performance of two ranking schemes
- interpret meaning of MDL-GMM of highlight class
- assign every audio frame to a mixture component
- infer semantic meaning of every component
- apply method to sports video
- detect unusual events in sports video
- apply method to surveillance video

### Overview of Invention

- extract and process features
- train model and construct summary

