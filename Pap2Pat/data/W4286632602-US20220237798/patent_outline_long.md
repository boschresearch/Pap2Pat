# DESCRIPTION

## FIELD

- relate to ultrasound imaging

## BACKGROUND

- introduce ultrasound imaging
- motivate HRI estimation
- limitations of manual HRI estimation

## BRIEF SUMMARY

- introduce automatic HRI estimation

## DETAILED DESCRIPTION

- introduce method and system for automatically estimating hepatorenal index (HRI) from ultrasound images
- motivate technical effects of automatically calculating HRI from ultrasound images
- summarize technical effects of automatically identifying liver and kidney anatomy
- describe technical effects of identifying valid samples in liver and kidney region
- motivate technical effects of identifying appropriate anatomical view for HRI calculation
- summarize technical effects of calculating HRI score and providing confidence score
- describe technical effects of automatically positioning liver region of interest and renal cortex region of interest
- motivate technical effects of automated HRI calculation
- introduce drawings and diagrams of functional blocks
- clarify division between hardware circuitry
- define element or step recited in singular
- introduce term "image" and its broad reference
- define processor or processing unit
- describe forming of images with or without beamforming
- introduce ultrasound system 100 and training system 200
- describe components of ultrasound system 100
- describe functionality of components of ultrasound system 100
- describe receive beamformer
- describe user input device
- describe signal processor
- describe image analysis processor
- analyze ultrasound image data
- direct signal processor to freeze view
- store view at archive
- provide quality metric
- describe segmentation processor
- segment flow image frames and B-mode frames
- identify liver and renal cortex
- store segmentation information at archive
- display segmentation information
- provide segmentation information to image analysis processor
- provide segmentation information to sample identification processor
- describe sample identification processor
- identify valid samples in liver and renal cortex
- exclude invalid samples
- apply artificial intelligence algorithms
- identify valid samples with visual indication
- display obtained ultrasound image view with valid samples
- provide obtained ultrasound image view to ROI positioning processor
- store obtained ultrasound image view at archive
- describe ROI positioning processor
- automatically position liver region of interest
- automatically position renal cortex region of interest
- apply algorithms to valid samples
- determine densest valid sample region
- provide visual indications of regions of interest
- display obtained ultrasound image view with regions of interest
- provide obtained ultrasound image view to HRI processor
- store obtained ultrasound image view at archive
- describe HRI processor
- calculate hepatorenal index
- display hepatorenal index
- store hepatorenal index at archive
- describe ultrasound system
- continuously acquire ultrasound scan data
- display acquired ultrasound scan data
- store acquired ultrasound scan data at image buffer
- describe image buffer
- describe FIG. 4
- introduce display 400
- describe segmented ultrasound image view 202
- introduce ROI positioning processor 170
- describe automatic positioning of liver and renal cortex regions of interest
- introduce HRI processor 180
- describe determination of HRI
- introduce display system 134
- describe display capabilities
- introduce archive 138
- describe storage capabilities
- introduce components of ultrasound system 100
- describe implementation of components
- introduce training system 200
- describe training engine 210
- describe training database 220
- introduce artificial intelligence model
- describe training of deep neural networks
- introduce FIG. 5
- describe flow chart 500
- introduce step 502
- describe acquisition of ultrasound data
- introduce step 504
- describe determination of desired ultrasound image view
- introduce step 506
- describe assignment of quality metric
- introduce step 508
- describe segmentation of liver and renal cortex
- introduce step 510
- describe identification of valid samples
- describe ultrasound system
- determine HRI and quality score
- display HRI and quality score
- acquire ultrasound image data
- segment liver and renal cortex
- identify valid samples
- automatically position regions of interest
- determine HRI
- display HRI
- assign quality metric
- display quality metric
- describe invalid samples in liver
- describe invalid samples in renal cortex
- describe criterion for positioning regions of interest
- describe densest valid sample region in liver
- describe densest valid sample region in renal cortex
- describe ultrasound system components
- describe processor configurations
- describe display system
- describe non-transitory computer readable medium
- describe computer program
- describe steps for automatically estimating HRI
- describe receiving ultrasound image data
- describe segmenting liver and renal cortex
- describe identifying valid samples
- describe automatically positioning regions of interest
- describe determining HRI
- describe displaying HRI
- describe assigning quality metric
- describe displaying quality metric
- describe invalid samples in liver
- describe invalid samples in renal cortex

