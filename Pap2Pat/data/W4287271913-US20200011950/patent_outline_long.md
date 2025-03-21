# DESCRIPTION

## FEDERAL FUNDING NOTICE

- disclose government funding

## BACKGROUND

- motivate tumor heterogeneity

## DETAILED DESCRIPTION

- introduce cancer and tumor field effect
- describe limitations of existing approaches to predicting overall survival in Glioblastoma
- motivate radiomic features for capturing intra-tumoral heterogeneity
- describe radiomic features extracted from peritumoral regions
- introduce tumor field effect in GBM
- describe embodiments mining prognostic information from subtle deformations
- introduce integrated descriptor (r-DepTH) of radiographic deformation and textural heterogeneity
- describe embodiments employing r-DepTH descriptor to predict patient survival
- illustrate radiomic features associated with a GBM tumor for two different patients
- describe textural differences within tumoral regions
- illustrate deformation magnitudes in the surrounding normal parenchyma
- describe embodiments extracting radiomic features predictive of long-term GBM survival
- introduce machine learning classifier for distinguishing LTS from STS
- describe techniques for distinguishing LTS from STS via radiological imagery
- introduce algorithmic descriptions and symbolic representations of operations
- describe physical manipulations of physical quantities
- introduce example methods and operations
- illustrate flow diagram of an example method or set of operations
- describe accessing a radiological image associated with a patient
- segment tumoral region represented in the image
- define peritumoral region represented in the image
- illustrate example tumoral region
- describe defining peritumoral region based on morphological transformation
- introduce distance measurements for peritumoral region
- describe embodiments employing techniques for distinguishing LTS from STS
- conclude embodiments facilitating improved treatment management in solid tumors
- illustrate peritumoral region
- morphologically dilate tumoral boundary
- define annular rings
- generate peritumoral boundary
- define parenchymal region
- compute deformation heterogeneity feature descriptor
- access healthy brain atlas
- register parenchymal region to atlas
- compute deformation heterogeneity feature descriptor
- compute tumoral 3D gradient-based texture descriptor
- generate CoLIAGe feature
- compute tumoral 3D gradient-based texture descriptor
- compute peritumoral 3D gradient-based textural descriptor
- generate CoLIAGe feature
- compute peritumoral 3D gradient-based textural descriptor
- generate r-DepTH descriptor
- provide r-DepTH descriptor to machine learning classifier
- receive probability from machine learning classifier
- generate classification of patient
- display classification
- display image and descriptors
- train machine learning classifier
- illustrate set of operations
- train machine learning classifier
- facilitate training of machine learning classifier
- acquire radiographic image
- generate r-DepTH descriptor
- provide r-DepTH descriptor to machine learning classifier
- receive probability from machine learning classifier
- generate classification of patient
- introduce radiological image analysis
- access training dataset of radiological images
- determine values for distinguishing features
- generate r-DepTH descriptor
- train machine learning classifier
- test machine learning classifier
- determine optimal combination of parameters
- generate receiver operating characteristic curve
- calculate area under the curve
- train machine learning classifier until threshold level
- generate personalized GBM treatment plan
- display personalized GBM treatment plan
- introduce radiographic-deformation and textural heterogeneity descriptor
- extract deformation heterogeneity descriptors
- extract 3D gradient-based descriptors
- compute first order statistics
- compute higher order statistics
- obtain descriptor IF depth
- obtain feature vector depth
- introduce example use case
- define image scene
- extract deformation heterogeneity descriptors
- extract 3D gradient-based descriptors
- compute first order statistics
- compute higher order statistics
- obtain descriptor IF depth
- obtain feature vector depth
- introduce independent dataset
- employ sequential forward feature selection
- construct linear discriminant analysis classifier
- evaluate classifier on test cases
- perform Kaplan-Meier survival analysis
- compare survival times between groups
- illustrate Kaplan-Meier curves
- list features computed from T1w MRI scans
- facilitate improved distinguishing of LTS from STS
- analyze deformation magnitude across LTS and STS
- illustrate box plots of deformation skewness
- show results of example embodiment
- provide technical improvement in predicting OS
- introduce GBM OS prediction system
- describe apparatus for distinguishing LTS from STS in GBM
- detail processor and memory components
- outline I/O interface and set of circuits
- describe image acquisition circuit
- detail region definition circuit
- describe r-DepTH descriptor circuit
- outline GBM OS prediction circuit
- describe display circuit
- introduce apparatus with additional elements
- describe GBM personalized treatment plan circuit
- outline training and testing circuit
- describe personalized medicine device
- introduce example computer
- detail processor and memory components
- outline I/O ports and bus
- describe disk and operating system
- outline input/output devices
- describe network devices
- introduce non-transitory computer-readable storage device
- describe accessing radiological image
- detail segmenting tumoral region
- describe defining peritumoral region
- outline defining parenchymal region
- describe computing deformation heterogeneity feature descriptor
- detail computing tumoral 3D gradient-based texture descriptor
- describe computing peritumoral 3D gradient-based textural descriptor
- outline generating r-DepTH descriptor
- describe providing r-DepTH descriptor to machine learning classifier
- detail receiving probability from machine learning classifier
- describe generating classification
- outline displaying classification
- introduce MRI image
- describe CT image
- outline digital whole slide scanner
- describe CADx system
- detail personalized medicine system
- outline network environment
- describe remote computers
- define detailed description
- introduce example 3
- specify radiological image
- introduce example 4
- compute deformation heterogeneity feature descriptor
- introduce example 5
- register parenchymal region to healthy brain atlas
- introduce example 6
- define parenchymal region
- introduce example 7
- specify annular sub-regions
- introduce example 8
- compute deformation heterogeneity feature descriptor
- introduce example 9
- specify tumoral 3D gradient-based texture descriptor
- introduce example 10
- specify tumoral 3D gradient-based texture descriptor
- introduce example 11
- specify peritumoral 3D gradient-based textural descriptor
- introduce example 12
- specify peritumoral 3D gradient-based textural descriptor
- introduce example 13
- specify machine learning classifier
- introduce example 14
- train and test machine learning classifier
- introduce example 15
- generate personalized GBM treatment plan

