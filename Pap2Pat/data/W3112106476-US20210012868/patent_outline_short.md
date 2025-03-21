# DESCRIPTION

## BACKGROUND

### Technical Field

- relate to systems and methods for analysis of videos of surgical procedures

### Background Information

- motivate need for unconventional approaches to analyze surgical videos

## SUMMARY

- introduce systems and methods for analysis of surgical videos
- describe reviewing surgical video
- describe video indexing
- describe generating surgical summary footage
- describe surgical preparation
- describe analyzing complexity of surgical footage
- describe enabling adjustments of an operating room schedule
- describe analyzing surgical images to determine insurance reimbursement
- describe populating a post-operative report of a surgical procedure

## DETAILED DESCRIPTION

- define terms used in patent application
- describe operations performed by computer
- explain phraseology and terminology used
- describe data structures and their uses
- introduce machine learning algorithms and models
- describe training and using machine learning algorithms
- explain artificial neural networks and their configurations
- describe analyzing image data and preprocessing methods
- introduce rules, functions, and procedures for analyzing image data
- describe analyzing pixels, voxels, point cloud, and range data
- introduce operating room setup and camera configurations
- describe camera control application and its functions
- introduce camera control application
- describe camera zoom adjustment
- explain triangulation for distance measurement
- list various sensors in operating room
- describe surgical instrument with sensors and light sources
- explain data transmission and processing
- introduce need for surgical video summary
- describe method for reviewing surgical video
- explain accessing and outputting video for display
- describe overlaying surgical timeline on video
- define playback and marker
- describe marker representation
- explain marker selection
- detail automatic marker generation
- describe marker coding
- discuss marker visual properties
- define decision making junction
- detect decision making junction using computer analysis
- identify alternative video clips for decision making junction
- display alternative video clips and possible decisions
- estimate outcomes of alternative possible decisions
- select similar past decision making junctions based on patient characteristics
- select similar past decision making junctions based on medical professional characteristics
- display distribution of past decisions made in similar past decision making junctions
- introduce surgical video indexing
- describe displayed distribution of decision making junctions
- analyze videos of past surgical procedures
- identify similar decision making junctions
- determine outcome of alternative decisions
- use computer vision algorithm for analysis
- identify intraoperative surgical event markers
- display alternative video clips for intraoperative events
- compile footage from multiple surgical procedures
- review surgical videos using timeline interface
- enable selection of markers on surgical timeline
- describe method for indexing surgical video footage
- define surgical phases
- describe user input for video footage location
- explain computer analysis for video footage location
- detail neural network model for video footage location
- describe generating phase tags
- associate phase tags with video footage location
- analyze video footage for intraoperative surgical events
- associate event tags with event locations
- define event characteristic
- determine event characteristic
- associate event characteristic with video footage
- store event characteristic in data structure
- illustrate data structure
- enable user to access data structure
- select phase tag, event tag, and event characteristic
- perform lookup in data structure
- identify matching subset of stored video footage
- display matching subset of stored video footage
- describe surgical footage filtering
- motivate event characteristic storage
- summarize adverse outcome identification
- explain surgical technique filtering
- describe surgeon identity filtering
- motivate time-based event filtering
- summarize patient characteristic filtering
- explain physiological response filtering
- present statistical information
- illustrate video indexing process
- describe processor and memory
- analyze video footage to identify surgical phase
- generate and associate phase and event tags
- store event characteristic and associate with video footage
- enable user to access and view filtered video footage
- describe method for generating surgical summary footage
- access historical data
- distinguish surgical activity from non-surgical activity
- use indicators to distinguish surgical activity
- detect tools and anatomical features
- analyze video footage to detect interaction
- distinguish first group of frames from second group
- analyze surgical footage to detect medical instrument
- analyze surgical footage to detect anatomical structure
- present aggregate of first group of frames
- define presenting aggregate
- describe user and request
- motivate exporting first group of frames
- generate index of intraoperative surgical events
- generate cause-effect summary
- illustrate processes for generating cause-effect summary and surgical summary footage
- introduce surgical preparation
- motivate need for efficient video review
- describe method for compiling surgical video footage
- define repository of surgical video footage
- describe case-specific information input
- compare case-specific information with data associated with surgical video footage
- identify group of intraoperative events likely to be encountered
- identify specific frames in specific sets of surgical video footage
- omit portions of identified specific frames to avoid redundancy
- determine common characteristic of intraoperative events
- use machine learning model to identify common characteristic
- omit second set from compilation and include first set
- describe compilation of footage associated with intraoperative events
- summarize method for surgical preparation using compiled footage
- describe presentation of surgical procedures
- enable surgeon to view presentation
- display common surgical timeline
- sequentially display discrete sets of video footage
- train machine learning model to generate index
- illustrate process for surgical preparation
- access repository of surgical video footage
- enable surgeon to input case-specific information
- compare case-specific information with data
- analyze complexity of surgical footage
- introduce surgical complexity level
- define complexity level
- analyze frames using historical data
- identify anatomical structure
- determine surgical complexity level
- analyze second set of frames
- identify medical tool, anatomical structure, and interaction
- access second historical data
- analyze second historical data
- determine second surgical complexity level
- use machine learning model to determine complexity level
- consider physiological response
- consider condition of anatomical structure and patient characteristic
- motivate surgical complexity level analysis
- determine skill level of healthcare provider
- analyze electronic medical record
- identify medical tool in frames
- determine complexity level based on event
- analyze time elapsed between frames
- compare complexity levels to threshold
- tag frames with complexity levels
- generate data structure with complexity levels
- analyze frames to identify anatomical structure
- access historical data for complexity level analysis
- adjust operating room schedule based on complexity level analysis
- describe camera system for tracking surgical instruments
- detail camera features and control application
- explain zoom lens and camera positioning
- outline rule-based control of camera position and zoom
- describe system for capturing and analyzing visual data
- detail computer system components and database
- explain input module and software instructions
- describe audio sensors, light emitting devices, and schedule
- outline schedule display and interface
- describe form for entering surgical procedure information
- define data structure for surgical procedure
- describe data tables and fields
- explain accessing data structure
- analyze visual data to determine estimated completion time
- describe machine learning model for estimating completion time
- explain using historical data to determine estimated completion time
- describe adjusting operating room schedule
- calculate variance from scheduled time
- output notification upon variance detection
- determine extent of variance from scheduled time
- determine likelihood of delay from scheduled time
- output notification upon delay detection
- introduce surgical procedure analysis
- describe visual data collection
- analyze visual data and historical surgical data
- determine estimated time of completion
- access operating room schedule
- calculate variance from scheduled time
- output notification
- detect characteristic events
- assess information based on historical surgical data
- train machine learning model
- adjust operating room schedule
- motivate insurance reimbursement
- describe method for analyzing surgical images
- define interactions between medical instruments and anatomical structures
- describe database of reimbursement codes
- illustrate data structure for reimbursement codes
- describe code-generating machine-learning method
- compare identified interactions with reimbursement codes
- output reimbursement codes for insurance reimbursement
- discuss multiple reimbursement codes for a surgical procedure
- introduce reimbursement code determination
- analyze post-operative surgical report
- capture video frames of surgical footage
- update database with reimbursement codes
- generate correlations between reimbursement codes and medical instruments/anatomical structures
- train machine-learning method for generating correlations
- use machine-learning method to detect medical instruments/anatomical structures
- analyze video frames to determine condition of anatomical structure
- determine reimbursement code based on condition of anatomical structure
- analyze video frames to determine change in condition of anatomical structure
- determine reimbursement code based on change in condition of anatomical structure
- analyze video frames to determine usage of medical device
- determine reimbursement code based on usage of medical device
- introduce post-operative report
- describe structure of post-operative report
- motivate image-based information
- describe process for populating post-operative report
- introduce surgical footage
- describe analysis of surgical footage
- derive image-based information
- populate post-operative report with image-based information
- describe phases of surgical procedure
- analyze surgical footage to identify phases
- use computer analysis to identify phases
- associate phase name with surgical procedure phase
- identify phase property from surgical footage
- determine beginning of surgical phase
- associate time marker with surgical phase
- detect surgical event using action detection algorithms
- analyze surgical footage to identify recommendation for post-operative treatment
- provide identified recommendation for post-operative treatment
- enable healthcare provider to alter derived image-based information
- track updates to post-operative report using version tracking system
- analyze surgical footage to identify surgical event and property of event
- describe electronic medical record update
- motivate user input for derived image-based information
- separate image-based information into parts
- structure post-operative report
- analyze preliminary post-operative report
- insert derived image-based information into report
- select frames of surgical footage for report
- identify inconsistencies between report and footage
- analyze surgical footage to identify phases of procedure
- transmit data to healthcare provider
- define surgical procedures
- describe deviations from recommended sequences
- describe operating room environment
- access video frames of surgical procedure
- describe surgical events and phases
- describe recommended sequences of events
- illustrate critical view of safety
- describe recommended sequence of events
- access stored data identifying recommended sequence
- select recommended sequence of events
- illustrate example recommended sequence
- compare accessed video frames with recommended sequence
- identify events within video frames
- quantify difference between events
- determine deviation between sequences
- identify deviation between surgical procedure and recommended sequence of events
- compare actual sequence of events with recommended sequence
- use machine learning model to identify deviations
- synchronize video frames with reference frames
- identify elapsed time associated with surgical procedure
- provide notification of deviation
- train machine learning model using training examples
- adjust model parameters to correctly predict deviation
- receive indication of particular action about to occur
- provide notification of deviation before action is performed
- introduce surgical procedure monitoring system
- describe input methods for healthcare professionals
- explain machine-learning algorithm for recognizing surgical events
- detail data structure for storing recommended sequence of events
- describe detecting presence of surgical tool in anatomical region
- identify indication of deviation between surgical procedure and recommended sequence
- illustrate process for determining and notifying omitted event in surgical procedure
- discuss decision support for surgical procedures using video footage analysis
- outline method for providing real-time recommendations to surgeons
- define operating room
- introduce data structure for image-related data
- describe image-related data characterizing surgical procedures
- analyze video footage to determine surgical decision making junction
- determine presence of decision making junction based on physiological response
- access correlation between outcome and specific action
- describe specific actions during surgical procedure
- output recommendation to undertake or avoid specific action
- output additional recommendation based on medical test result
- provide description of current surgical situation and guidance
- define recommendation
- motivate surgical decision making junction
- describe factors influencing decision
- summarize decision making junction examples
- outline machine learning model for recommendation
- describe information used for machine learning model
- illustrate process for decision support
- receive video footage of surgical procedure
- access image-related data for analysis
- analyze video footage for decision making junction
- access correlation between outcome and action
- output recommendation to user
- define contact force
- describe estimation of contact force through image analysis
- introduce method for estimating contact force on anatomical structure
- analyze image data to determine identity of anatomical structure
- analyze image data to determine condition of anatomical structure
- select contact force threshold associated with anatomical structure
- implement model to select contact force threshold
- receive indication of actual contact force on anatomical structure
- estimate indication of actual contact force based on image analysis
- compare indication of actual contact force with selected contact force threshold
- output notification based on determination that indication of actual contact force exceeds selected contact force threshold
- describe notification system for surgical procedures
- motivate fight mode determination
- outline method for estimating contact force
- illustrate process for estimating contact force
- describe updating predicted surgical outcomes
- motivate real-time decision support systems
- outline systems and methods for updating predicted outcomes
- describe determining predicted outcomes based on image data
- motivate determining predicted outcome
- describe determining predicted outcome based on surgeon's skill level
- describe determining predicted outcome based on anatomical structure's condition
- describe determining predicted outcome based on estimated contact force
- describe determining predicted outcome using machine learning model
- describe receiving image data associated with second event
- describe determining change in predicted outcome
- describe correlating variables to positive or negative outcomes
- describe determining change in predicted outcome based on elapsed time
- describe accessing data structure of image-related data
- describe identifying and outputting recommended remedial action
- describe surgical procedure
- analyze image data for fluid leakage
- determine source of fluid leakage
- identify properties of fluid leakage
- analyze frames of intracavitary video
- identify ruptured anatomical structure
- identify blood splash and properties
- identify spray of blood and properties
- determine remedial action
- institute remedial action
- define fluid leakage situation
- analyze frames of intracavitary video
- determine abnormal fluid leakage situation
- institute remedial action
- analyze surgical footage to identify events
- predict post discharge risk
- access frames of video captured during surgical procedure
- analyze frames using machine-learning method
- access stored historical data identifying intraoperative events
- associate intraoperative events with outcomes
- define intraoperative events and associated outcomes
- describe database structure for storing historical data
- introduce machine-learning model for identifying intraoperative events
- describe training process for machine-learning model
- identify intraoperative events using machine-learning model
- detect surgical tools and anatomical structures in video frames
- analyze frames to identify interactions between surgical tools and anatomical structures
- detect abnormal fluid leakage situations in video frames
- analyze accessed frames to identify specific intraoperative events
- determine predicted outcome associated with surgical procedure
- use statistical analysis to determine predicted outcome
- introduce surgical procedure prediction
- describe patient characteristics
- discuss electronic medical record
- explain postoperative surgical report
- introduce event-based machine learning model
- describe training machine learning model
- predict surgical outcome
- identify patient characteristic
- update machine learning model
- output predicted outcome
- define deviation-based model
- motivate machine learning for identifying deviations
- describe identifying deviations from recommended sequences
- determine actions to improve predicted outcomes
- outline predictive modeling process
- introduce predictive system
- define surgical video analysis system
- describe video indexing and tagging
- outline video search and display functionality
- detail event characteristic analysis and filtering
- describe computer image analysis and neural network model
- outline historical data analysis and surgical outcome detection
- summarize cause-effect analysis and presentation
- describe surgical footage analysis
- distinguish surgical activity frames
- generate compilation of frames
- access repository of surgical video footage
- compare case-specific information with data
- determine surgical complexity levels
- estimate completion time of ongoing surgical procedure
- analyze video frames to detect medical tools and anatomical structures
- access database of reimbursement codes correlated to medical instruments and anatomical structures
- compare identified interactions with database to determine reimbursement codes
- output reimbursement codes for insurance reimbursement
- update database with new correlations and reimbursement codes
- analyze video frames to determine condition of anatomical structure and usage of medical devices
- generate post-operative report and provide recommendations for post-operative treatment
- describe surgical decision making junction
- analyze image data to determine anatomical structure condition
- select contact force threshold based on anatomical structure condition
- output notification based on contact force threshold
- determine predicted outcome based on image data
- identify remedial action based on predicted outcome
- analyze intracavitary video to determine abnormal fluid leakage situation
- disclaim limitations

