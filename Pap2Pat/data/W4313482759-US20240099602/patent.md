# DESCRIPTION

## FIELD

The present disclosure generally relates to diagnosis and treatment of epilepsy including imaging techniques and computer-implemented evaluation; and more particularly, to systems and methods for an automated seizure onset zone locator from resting state functional MRI for drug resistant epilepsy.

## BACKGROUND

Epilepsy is devastating, affecting 50 million worldwide (WHO). One in 150 children, 30% have drug resistant epilepsy (DRE) and causes significant morbidity and mortality. A consensus proposal by the ad hoc Task Force of the International League Against Epilepsy (ILAE) proposed the following definition for DRE: “a failure of adequate trials of two tolerated, appropriately chosen and used antiepileptic drug schedules (whether as monotherapies or in combination) to achieve sustained seizure freedom (considered as freedom from all seizures, including auras) for at least 12 months.”

Early diagnosis and treatment of DRE can potentially avoid complications such as evolution into status epilepticus, and Sudden Unexplained Death in Epilepsy (SUDEP), wherein the individual dies due to cardio-respiratory failure from presumed nocturnal seizure activity. Moreover, in children, timely diagnosis, intensive management and treatment are pivotal in minimizing neurological damage. Further, the earliest onset of severe epilepsy in the neonatal population can lead to nearly constant life-threatening seizures requiring urgent need for surgical evaluation early in life.

It is with these observations in mind, among others, that various aspects of the present disclosure were conceived and developed.

Corresponding reference characters indicate corresponding elements among the view of the drawings. The headings used in the figures do not limit the scope of the claims.

## DETAILED DESCRIPTION

The present disclosure relates to systems and methods for accurate localization of seizure onset zone (SOZ) from independent components (IC) of resting state functional magnetic resonance imaging (rs-fMRI) to improve surgical outcomes in children with Drug Resistant Epilepsy (DRE). Automated IC sorting has limited success in identifying SOZ localizing ICs in adult normal rs-fMRI or uncategorized epilepsy. Children provide unique challenges due to the developing brain and associated surgical risks. The present concept proposes a novel SOZ localization algorithm (EPIK) for children with DRE.

Methods: EPIK is developed in a phased approach, where fMRI noise-related biomarkers are used through high fidelity image processing techniques to eliminate noise ICs. Then SOZ markers are used through a maximum likelihood-based classifier to determine SOZ localizing ICs. The performance of EPIK was evaluated on a unique pediatric DRE dataset (n=52). 24 children underwent surgical resection or ablation of rs-fMRI identified SOZ, concurrently evaluated with EEG and anatomical MRI. Two state-of-art techniques are used for comparison: a) least squares support vector machine, and b) Convolutional Neural Networks. The performance was benchmarked against expert IC sorting and Engel outcomes for surgical SOZ resection or ablation. Analysis is stratified across age and sex.

Results: EPIK outperforms state-of-art techniques for SOZ localizing IC identification with mean accuracy of 84.7% (4% higher), precision 74.1% (22% higher), specificity 81.9% (3.2% higher) and sensitivity 88.6% (16.5% higher). EPIK provides consistent performance across age and sex with best performance in <5-year age. It achieves a -5-fold reduction in the number of ICs to be potentially analyzed during pre-surgical screening.

Significance: Automated SOZ localization from rs-fMRI, validated against surgical outcomes, indicates potential for clinical feasibility. It eliminates the need for expert sorting, outperforms prior automated methods and is consistent across age, and sex.

### Introduction and Technical Problems

As indicated above, epilepsy, and DRE in particular, is life-altering for most affected. Various conventional approaches for dealing with these afflictions shall now be described.

Surgery for DRE: The most effective treatment for DRE is surgery. Early surgery is key: “minimally invasive surgical treatment can be a life-changing option for DRE patients: hence management of SOZ requiring disconnecting techniques, or deep sited lesions requiring excision should be considered earlier rather than later”. Notably, recent findings show that ultra-early (before 3 months old) surgical intervention in children evaluated to be DRE after trials of an average of 4 anti-seizure drugs, although seldom performed, has excellent epilepsy outcomes and leads to decrease in usage of anti-seizure drugs, without any increased risk of surgery related permanent morbidity.

Brain Imaging for Pre-surgical screening: Surgical intervention in DRE requires accurate localization of the seizure onset zone (SOZ) for success. Here we make a distinction between epileptic network (EN) and SOZ. EN denotes regions where seizure propagates and may be more extensive than the SOZ. As such it may be difficult as well as unnecessary to surgically eliminate EN since they can incorporate sensitive areas of the brain. Several brain imaging techniques has been explored to identify ictal seizure onset zone (SOZ), propagation zone (i.e., EN), and interictal activity (Table 1, below). This can be done with nuclear medicine-based imaging techniques such as positron emission tomography (PET) or ictal single-photon emission computerized tomography (SPECT). Recent works suggest some SOZ identification capability for PET and SPECT in both adults and children, however, accuracy heavily depends on the timing of the scan. Delay in drug infusion can result in detection of EN instead of SOZ. Invasive modalities such as intracranial EEG (iEEG) is considered as gold standard for SOZ identification and has shown excellent accuracy for both adults and pediatric DRE. Stereo-electroencephalography (SEEG) is minimally invasive which uses a three-dimensional configuration of depth electrodes to localize epileptiform activity and has shown some SOZ identification capability recently.

However, traditional analysis of PET, SPECT, or SEEG is relatively temporally and spatially restricted, whereas functional interpolation of brain activity might allow for noninvasive three-dimensional representation of epileptiform activity and avoid pitfalls inherent of other modalities (Table 1). Recently, magnetoencephalography (MEG) and functional magnetic resonance imaging (fMRI) based noninvasive techniques have been analyzed for DRE in both adults and children and show descent SOZ identification capability. A combination of MEG and fMRI imaging is also proposed for accurate SOZ identification. However, a major drawback of such brain imaging based SOZ identification techniques is the heavy reliance on manual sorting of images and their components, which not only increases cost but also reduces accessibility and repeatability.

Unfortunately, less than 1% of DRE patients are evaluated for surgery and only 25% of those undergo surgery, part due to the diagnostic and surgical treatment high expensive (>$200,000/patient) and risk of debilitating impairment. Of the 1% evaluated, surgical failure rates are 30-70% despite the use of noninvasive SOZ-localization biomarkers such as anatomical MRI, scalp EEG, simultaneous EEG-fMRI, and magnetoencephalography which are then often confirmed by invasive iEEG. Hence, for surgery to be safe and efficient for wide acceptance, accessible, minimally invasive and accurate SOZ localization is essential.

One of the newer methods showing promise, to this end, is resting state functional MRI (rs-fMRI). Rs-fMRI has shown accurate SOZ-localization capacity by various analysis approaches, but only independent component analysis (ICA) has provided Level 1 evidence and has led to improvement in surgical outcomes and candidacy in DRE. However, expert interpretation of independent components (IC) into sources of noise, normal resting state networks (RSN), and SOZs, limits reproducibility and availability. An automated whole-brain data-driven SOZ-localizing IC identification technique that is rigorously validated against surgical destruction outcomes, reproducible, equally effective across age and sex and epilepsy subtype may greatly improve epilepsy care feasibility, morbidity, and mortality.

### Proposed Solution to Technical Problems

fMRI based screening: Referring to flow diagram 100 of FIG. 1, functional MRI (fMRI) is a popular imaging technique originally used to identify brain activity in terms of blood oxygenation level change in different parts of the brain for a given mental task. However, for SOZ detection, it is required to identify blood oxygenation changes due to onset of seizure. Hence, an important step is to remove other sources of brain activity such as mental tasks, fMRI noise, and head motion. Rs-fMRI requires the subject to be in resting state, which is achieved in majority of children through sedation. Even if any mental task is eliminated there are still resting state brain activity in a subject, which are manifested as RSN brain activity. Head motion is a significant source of noise. Although head motion is limited to less than 1 mm it still can pose significant amount of noise in the rs-fMRI measurement. Automated image registration is used to reduce head motion artifacts in rs-fMRI (FIG. 1 middle panel). The resulting rs-fMRI captures brain activity due to several sources including, a) noise (fMRI machine noise and head motion), b) RSN (resting state activity of the brain), and c) SOZ (change in blood oxygenation due to seizure onset). To decouple the effects of noise, RSN and SOZ in rs-fMRI signals, ICA is used to recover mutually independent fMRI signal components (ICs) that potentially only captures brain activity from one of the three sources.

Rs-fMRI ICA results in approximately 100 ICs. Each IC is a spatial-temporal distribution of regions of synchronous activity. In ICA of those with DRE, there are three IC categories: 1) RSNs which are well described and validated in the literature; 2) SOZ, currently, highly dependent on expert sorting; and 3) noise, which is also well understood, resulting from cardiovascular, cerebral-spinal-fluid-pulsation, or scanner artifacts (as described in Boerwinkle et al. 2017 for details and examples). In standard rs-fMRI based pre-surgical screening for DRE children, the entire set of ICs is analyzed by a neurosurgeon or neurologist to determine which ICs capture blood oxygenation changes due to seizure onset. Such an IC is referred to as a “SOZ localizing IC”. The neurosurgeon then determines the location of seizure onset in the brain using the SOZ localizing IC and a recommendation for surgical procedure such as resection or ablation or neurostimulation is made.

Given that ICA results in >100 ICs and only <10% are SOZ localizing ICs, manual sorting of rs-fMRI ICs to search for SOZ localizing IC is a significant time commitment by the neurosurgeon resulting in increased cost, reduces availability, and higher chance of false positives (FIG. 1). In some examples, the present inventive concept disclosed herein focuses on automating the task of IC sorting and reducing the number of ICs to be analyzed by the neurosurgeon for pre-surgical evaluation for children with DRE.

Automation of fMRI-based screening: Recent works have considered two automation objectives with rs-fMRI (Table 2): a) classification of subjects with or without epilepsy by identifying epilepsy networks using rs-fMRI BOLD signal z score latency maps, and b) localization of seizure onset zone using rs-fMRI ICs. Epilepsy networks indicate the areas of the brain that are affected by the propagation of seizure. As such they may not indicate the origin of the seizure, which is encapsulated by SOZ. Our work in this paper, tackles the second automation objective of SOZ localization.

Automated classification of rs-fMRI ICs as SOZ or RSN has been explored using supervised shallow machine learning (ML), and using deep learning (DL) in healthy adults to identify the typical RSNs, and is yet to be tested in epilepsy (Table 2 below). Supervised ML indicates that the DRE population has to be divided into two parts: a) training set, which is used to configure the ML, and b) testing set, which is used to test the performance of the ML. Some supervised ML can also choose to utilize a validation set. The performance of the ML technique on the validation set is used to update the training process and improve the performance in the validation set. Hence, the performance on the validation set is excluded from the analysis in Table 2 and only the test set performance is reported. Recent automated methods to classify adult rs-fMRI into RSN, SOZ and noise ICs are of three types: 1) Voxel-based network measures quantifying the number of connections to each voxel in an IC, called voxel degree connectivity (VDC), as indicators for SOZ. Such approaches have small sample size (n≈20) and show maximum reported sensitivity of 77% and specificity of 57% (Table 2); 2) ML based classification, with a sensitivity of 40% and specificity of 77%; and 3) DL approaches for only identifying RSN and noise, but not SOZs, for normal and non-DRE epileptic patients (accuracy 92% in Table 2).

To date, automated approaches have not been successful in classification of RSN, noise, and SOZ, in rs-fMRI for pediatric DRE patients due to challenges including: 1) Lack of normalized pathological rs-fMRI RSN data for children; 2) Databases with balanced instances of RSN, SOZ and noise, large enough for DL techniques to effectively recognize the three IC categories are not available; 3) Potentially inadequate performance of SOZ identification in children with DRE can indicate high risk of developmental disorders post-surgery. Given that each patient only has 5% ICs as SOZ, a 40% sensitivity means only two out of five SOZ ICs are correctly identified, while 14 are wrongly identified as SOZ; and 4) fMRI-based pre-surgical mapping is more complicated for children with DRE due to developmental changes during cognitive maturation, the impairment experienced due to DRE and the normal representation of memory function during development, which may differ from adults. Hence, the efficacy of fMRI classification techniques on adults needs to be reexamined for children with DRE.

Most current studies (Table 2) focus on adult epilepsy with unknown effect of the degree of hypothesized network disruption effect on localization. Currently available automated IC sorting techniques either only identify SOZ or RSN localizing ICs. Hunyadi et al., the first major work to attempt SOZ localizing ICs identification, used supervised ML but could only achieve a specificity of 77% and sensitivity of 40% on a subset of adult patient population. A more recent technique by Nozais et al. used DL to identify only RSN in healthy adults and reports an accuracy of 92%. The major drawback of DL techniques is the requirement for labelled data on all three IC categories. Table 2 shows that such labelled data is rarely available, even if we combine datasets from different authors, IC data labelled as RSN and SOZ is only available from 212 DRE children. For DL to successfully recognize SOZ it will need at least a balanced distribution of RSN and SOZ. The DL works in this domain utilize RSN data from 2000 healthy subjects for appropriate training (Table 2 Nozais et al and Luckett et al). Hence to achieve balanced data, we would need SOZ from at least 2000 subjects which is not available currently.

There has been one prior unsupervised approach by Zhang et al., however, it was applied to DRE adults and achieved a sensitivity of 78% and specificity of 57%. We cannot replicate that study for this paper, because specific information about parameter settings were not discussed in Zhang et al.

Difference between EPIK and supervised ML: Referring to FIG. 2, a prior machine learning (ML) approach 201 is illustrated, along with a novel, unsupervised technique (EPIK) 202 is described to identify SOZ localizing ICs that requires no prior dataset for training and classifies ICs by encoding expert knowledge. The unsupervised nature of the associated algorithm of the present novel disclosure implies that the entire dataset is used as a test set and no training dataset is required. The algorithm is tested on the largest number of DRE children among the recent studies on automated SOZ identification mechanisms with rs-fMRI listed in Table 2. FIG. 2 illustrates differences from other techniques. Prior ML techniques and approaches (FIG. 2) utilize examples of SOZ and RSN ICs to learn a model in the training phase, which is subsequently used for identification of SOZ on previously unseen rs-fMRI signals. Such techniques have not been successful, possibly for the following reasons: 1) SOZ biomarkers are not precise and exhibit significant individual variance, and 2) patients have low number of SOZ localizing ICs as compared to noise and RSN, leading to imbalance in data and potential overfitting of ML models. Compared to prior ML techniques and approaches, EPIK first purges ICs with noise markers by employing rules compiled from experts. The ICs that pass the initial purge, are then classified into RSN and SOZ based on maximum likelihood-based clustering mechanism. The italicized text marks the innovation in this work.

In other words, EPIK (ExPert Knowledge based IC categorization) (FIG. 2) takes an alternative approach. Instead of directly learning SOZ related features from training data, EPIK first uses expert rules in a waterfall technique to purge noise ICs. Noise markers used by EPIK such as clusters outside brain boundaries or overlapping white matter or arteries, are well established, evidenced by consistency across several publications. It then uses SOZ specific spatial and temporal markers in a maximum likelihood-based clustering to further classify the ICs into RSN and SOZ. Clustering is unsupervised and does not implement training with prior data to tune its parameters.

To illustrate differences compared to prior ML approaches, we replicate shallow (Borbala Hunyadi, 2014) and implement a Convolution Neural Network (CNN) based DL technique for identification of SOZ localizing ICs from rs-fMRI thereby providing a preliminary comparative study of all three approaches on the same dataset of children with DRE using the standard metrics of accuracy, precision, specificity, and sensitivity. It is hypothesized that EPIK will perform at least equally well as prior methods and consistently across age and sex, due to being informed by developmental and sex informed expert sorting in the pediatric DRE population.

### Materials and Methods

**Inclusion Criteria:**

Patients who were determined to be DRE by a treating epileptologist and received surgery evaluation. Most of the patients had focal epilepsy, however, rapid generalization of epileptiform activity from an epileptogenic focus may appear to be generalized epilepsy when evaluated using surface EEG. Hence generalized epilepsy was not an exclusion criterion.

Data Collection method: Referring to the flow diagram 300 of FIG. 3, the rs-fMRI data from 52 children with DRE, age 3 months-18 years old, were selected in descending alphabetical order from the PCH clinical database, who were under the care of a treating epileptologist at PCH. The diagnosis of DRE was according to the treating epileptologist's documented medical record notes. The children received rs-fMRI, video EEG, and anatomical MRI as part of standard clinical MRI SOZ localization for epilepsy surgery evaluation (FIG. 3). For rs-fMRI, patients who were determined to require conscious sedation received a propofol infusion, as a part of standard care determined by the institution's policies. In the 52 children, 39 required conscious sedation. The dataset included patients who had less than 1 mm head motion in any direction during scanning. For children who received sedation, propofol administered at levels to produce conscious sedation (80-110 micrograms/kilogram/minute), avoiding higher dosages typical of general anesthesia, was utilized. Propofol at levels producing conscious sedation reduces the BOLD signal strength by ˜10%, still allowing for complete network detection. General anesthesia causes gross loss of ability to detect the large-scale cortical networks and, was, therefore avoided.

As part of standard of care the children also received inpatient video EEG and anatomical MRI. This data also aided the manual identification of SOZ localizing ICs in rs-fMRI (FIG. 3). The MRI images were acquired using a 3 T MRI unit, Ingenuity Philips Medical systems. It has 32 channel headcoil. The resting state fMRI parameters were set at TR 2000 ms, TE 30 ms, matrix size 80×80, flip angle 80°, number of slices 46, slice thickness 3.4 mm with no gap, in-plane resolution 3×3 mm, interleaved acquisition, and number of total volumes 600, in two 10 -min runs, with total time of 20 mins.

rs-fMRI pre-processing: Oxford Centre FMRIB (Functional MRI of the Brain) Software Library tool MELODIC, was used to analyze the rs-fMRI and extract ICs as detailed in. Pre-processing included deletion of the first 5 volumes to remove T1 saturation effects, passing through a high-pass filter at 100 seconds, slice time correction, spatial smoothing of 1-mm full-width at half maximum, and motion corrected by MCFLIRT, with nonbrain structures removed.

Linear registration was performed between the individual functional scans and patient's high-resolution anatomical scan which was further optimized using boundary-based registration. Individual rs-fMRI data sets then underwent independent component analysis (ICA) as previously reported.

Expert RS-fMRI evaluation methodology: The SOZ were evaluated by the expert epilepsy surgery conference team and deemed to be consistent with the other acquired data (video EEG and anatomical MRI) with high enough evidence to surgically target the SOZ. Further, the confirmation that the SOZ was deemed true by the treatment team as evidenced by the Engel I and II scores 1 year post-operatively.

The ICA results were viewed by two blinded reviewers (1 neurologist and 1 neurosurgeon) and sorted the ICs into 3 categories—noise, resting-state network, and rs-fMRI SOZ—by the criteria below. In case of disagreement between the first two reviewers, the opinion of a third reviewer (a neurologist) was used to make the final determination.

Rs-fMRI was categorized into noise, resting state network (RSN) and SOZ using the following criteria:


- - Noise category: Consistent noise markers in rs-fMRI are reported in
    various literature references. The noise markers reported in
    different manuscripts are summarized in Table 4.
  - RSN category: These are activations in the MRI images that are
    spatially located in established anatomical regions. Such regions
    are highlighted in literature references and include bilateral face
    area, bilateral leg area, and unilateral right- and left-hand
    regions, language networks, parietal networks, temporal networks,
    visual networks, default mode networks and the deep gray networks.
  - SOZ category: SOZ characteristics consist of two types of
    features: a) spatial features and b) temporal features.

Spatial features: The activation should, and in some examples must be located within the gray matter, while not overlapping with the RSN spatial patterns. It must have a bullseye pattern, where two or more overlapping abnormal neuronal IC can be identified. May have alternating activation and deactivation pattern that does not overlap noise zones shown in Table 4. May extend to ventricles through white matter. May have irregular borders.

Temporal features: The SOZ BOLD signal power spectra must contain dominant frequencies greater than 0.073 Hz, the rs-fMRI SOZ must have power spectra at higher frequencies than RSN, the BOLD time series may have irregular patterns.

The rs-fMRI IC were expert sorted and reported to the clinical epilepsy surgery evaluation team. The data includes ICs extracted using the MELODIC module in FSL. Table 3 shows the age and sex distribution and surgical outcome statistics.

**(Example) EPIK Method**

Referring to the sample method 400 of FIG. 4 illustrating the EPIK approach described herein, EPIK considers noise markers for ICs in an rs-fMRI as documented in several studies including Griffanti et al. The method 400 applies rules in a waterfall technique to classify an IC as noise (FIG. 4). If an IC is not noise, then it classifies the IC as either an RSN or a SOZ. In detail, examples can include six expert-derived rules for IC noise markers, combined from Boerwinkle and Hunyadi's works (Table 4), and other examples can include other expert-derived rules configurations/implementations. Automated application of such rules, necessitate the development of the following key components.


- - a) Voxel cluster detection algorithm (**402**): A density-based
    scanning approach is undertaken to derive voxel clusters (upper
    panel of FIG. **4**). The algorithm **402** takes two configurable
    inputs: neighborhood, which includes a distance metric and a value
    ϵ, and minimum number of nearby voxels ν_(min). If a voxel has more
    than ν_(min) voxels in the ϵ neighborhood, then it is marked as a
    core point of a cluster. If a voxel is not a core point but is in ϵ
    neighborhood of a core point, then it is identified as border point.
    All other points are ignored from clusters. Core points, that are in
    ϵ neighborhood of each other, are combined into one cluster, and
    border points are assigned to the cluster of the nearest core point.
    The output of this step is the set of clusters in each IC slice
    (from slice extraction **401**).
  - b) Brain boundary/periphery detection (**406**): Contours in the
    brain are derived using a Sobel filter-based edge detection
    technique (**404** in FIG. **4**). The lowest intensity contour is
    most likely the outer contour of the brain. However, the
    cerebrospinal fluid and blood vessels also present as low intensity
    contours. The method searches for the contour that encompasses all
    other contours, which gives us the brain periphery.
  - c) White matter detection (**408**): The white matter manifests as
    the brightest contour in the brain. The blood vessels and
    cerebrospinal fluid in the white matter contour are discarded.
  - d) Blood vessel detection (**410***s*): The major basal-region blood
    vessels present themselves as low intensity contours encompassed in
    the brain periphery contour.
  - e) Noise IC classification: Utilizing the a,b,c, and d steps, an IC
    can be classified as noise (FIG. **5**). From each slice of an IC,
    the clusters and the contours are extracted. An overlapping cluster
    can cause the contour detection algorithm to fail in extracting the
    peripheral, the white matter and the blood vessel contours. In the
    initial pass though the ICs, EPIK obtains a version of each slice
    devoid of clusters, which is subsequently used to identify contours.
    The algorithm then reruns through each slice of an IC and performs
    cluster detection. It then evaluates the overlap of the largest
    cluster with the brain boundary (first row of images **500** in FIG.
    **5**), intersection of the largest cluster with the white matter,
    and blood vessels (third row in FIG. **5**). The output of the first
    stage classifier (upper panel in FIG. **4**) is a statistic for each
    slice on the cluster size, the percentage (%) overlap with the brain
    boundary, blood vessels, and white matter for each cluster in a
    slice (slice statistics **412** in FIG. **4**).

Each IC has multiple slices (around 55 for PCH dataset). The second stage classifier sorts the slices in decreasing order of cluster size (lower panel of FIG. 2). It selects the top 10 slices and checks the % overlap to determine noise slices. If the majority of the top 10 slices are noise, the IC is classified as a noise IC. If the IC passes through the majority evaluation, it is passed to the second level classifier which determines if it is a normal RSN or an SOZ (FIG. 4). The SOZ classification is based on expert guidance on the SOZ markers in ICs as documented in Hunyadi et al (Table 4).

- - f) BOLD signal feature extraction: The BOLD signal was first divided
    into windows of length 256 samples. Four levels of activelet
    transformation coefficients using the ‘a trois’ algorithm with
    exponential-spline wavelets were extracted from each window.
    Sparsity in the activelet coefficients were evaluated using the Gini
    Index metric. A Gini Index of greater than 0.75 is sparse. If an IC
    is classified as white matter noise, then it can be classified as an
    SOZ if the Gini Index in the BOLD signal is greater than 0.75. In
    addition, sparsity in matching pursuit using sine dictionary limited
    to frequencies between 0.01 Hz to 0.1 Hz was also evaluated using
    the Gini index. If an IC was classified as white noise, then it can
    be classified as SOZ if the BOLD signal Gini Index in the sine
    dictionary matching pursuit is greater than 1.72.

**Likelihood-Based Classification for SOZ ICs**

The main aim of the likelihood-based classification step is a standard technique in ML. We want to obtain a 1×4 weight vector ω, such that exi19 ω=ρi corresponds to the likelihood that the largest cluster in IC i is the SOZ. To obtain such a weight vector we solve the following optimization problem:


- - Given: A set Ex of expert knowledge-based representations
    (g_i={KNumC, KThruV, KDomF, KSparseF}) of a sample of RSN and SOZ
    ICs and a set y_(i)∈C of one hot encodings of two classes, such that
    y_(i)=−1 if i∈Ex is RSN and y_(i)=1 if i∈Ex is SOZ.\\
  - Find: A 4×1 weight vector ω that
  - Minimizes: P Σ_(i=1)^(\|Ex\|)(1−y_(i)ex·ω)²
  - Such that: Σ₁⁴ω_(k)=1,
  - where P is a penalty factor. The constraint in the problem
    formulation ensures that the confidence score is solely and
    exclusively based on the expert knowledge, and ω_(k) ex_(k) is the
    contribution of the k-th knowledge component. This contribution
    factor ω_(k) ex_(k) is later used for generating explanations.

It should be understood that the above weight configurations are merely exemplary, and the inventive concept can include other weight amounts; i.e., other classifier configurations are contemplated. In addition, the classifier as described can be one of one or more machine learning approaches implemented as part of an artificial intelligence mode (AI model). As such, other AI approaches including different machine learning models may be implemented for identification of SOZ ICs.

**DL Strategy for SOZ Localization**

Nozais et al. recently proposed a DL based technique where a multi-layer perceptron (MLP) is trained on 12690 RSNs from 282 participants. As such, it does not incorporate any expert knowledge but instead attempts to build its own hypothesis from examples. The technique has not been used to classify SOZ and can currently only identify RSNs. We have implemented CNN based DL for SOZ localization.

For the CNN technique, hyperparameter tuning is one of the most important steps. A Keras-Tuner was implemented to get the optimal values of the hyperparameters. We used hyperband algorithm with the objective of least validation loss to select the best model of CNN by optimizing the following hyperparameters:


- - Number of layers: \[3; 4; 5\]
  - Number of units/filters per layer: min_value=32, max_value=512,
    default=128.
  - Learning rate: \[10⁻², 10⁻³; 10⁻⁴\]
  - Dropout rate: \[0; 0.2; 0.33; 0.4; 0.5; 0.66\].

4212 ICs were used for training and 1404 ICs were used for validation in the hyperparameter tuning process. The input shape of the IC image was down sampled from 1006×709×3 to 270×400×3 during preprocessing. Binary cross-entropy was used as a loss function and Adam was used as an optimizer. To avoid the overfitting problem, “dropout” and “early_stopping” strategies were implemented. “ReLU” being more computationally efficient was used as an activation function for the input and hidden layers, and “Sigmoid” activation function was used for the output layer. For CNN, weights were initialized using “He uniform” initializer.

**Shallow Learning Strategy**

The technique proposed in Hunyadi et al. was replicated. rs-fMRI image and BOLD signal features were extracted from the IC images. 60% of the data from the entire pool of ICs was randomly sampled to be used as training data. The remaining 40% was used for testing. The features extracted from the rs-fMRI image and BOLD signal was used to train a Least Squares Support Vector Machine (LS-SVM) as described in Hunyadi et al.

**Metrics and Statistical Analysis Method**

We evaluated performance of each approach for two objectives: a) noise IC removal, and b) SOZ localizing IC identification. For the first objective, we define true positives (TP) as ICs that are classified as RSN or SOZ by both expert and the automated approach, true negatives (TN) as ICs that are classified as noise by both expert and the automated approach, false positives (FP) as ICs classified as noise by expert but RSN or SOZ by automated approach, and false negatives (FN) as ICs classified as RSN or SOZ by expert but noise by automated approach. For the second objective we define TP as ICs classified by both expert and automated approach as SOZ, TN as ICs classified by both expert and automated approach as not SOZ, FP as ICs classified as non-SOZ by expert but SOZ by automated approach, and FN as ICs classified as SOZ by expert but non SOZ by automated approach. From these we derived accuracy, precision, sensitivity, and specificity.

We evaluated the statistical significance of a difference in performance metrics between two approaches by utilizing a one-sided paired t test. The alternate hypothesis was that there is a positive non-zero difference between EPIK and any other approach (LS-SVM or CNN). The alternate hypothesis was rejected if the p-value for the paired t test was less than 0.05.

We also evaluated the effect of age and gender on each approach using a mixed effects model with each parameter as the observation variable and age or gender as the predictor variable. A random effect on the patient ID was also introduced. For each algorithm, a separate mixed effects model was generated for each metric and for each predictor variable age/gender.

### Overall Identification Results

We compared performance of EPIK with two competing ML based approaches: shallow learning (LS-SVM) and deep learning (CNN). For the ML based approach, training data was used from every subject. This is also known as user-dependent supervised classification approach and gave us the best performance metrics. For EPIK no such training set is needed. The results in Table 5 show that EPIK outperforms both LS-SVM and CNN approaches for SOZ localizing IC identification task. The CNN approach is more accurate in noise removal, however, performs poorly in the SOZ identification task.

EPIK has high sensitivity in the SOZ identification task with low number of FNs. This implies that EPIK rarely misses any SOZ localizing IC. The LS-SVM approach is poor in noise removal, but its performance improves for the SOZ identification task. The confidence interval is specified as [a,b] for metrics with p<0.5.

### Performance Variation with Age and Gender

Table 6 shows the variation of the performance metrics for EPIK, LS-SVM and CNN with respect to age and gender. The accuracy, precision, and sensitivity of EPIK for noise removal does not have a statistically stable dependence on age or gender. The specificity of EPIK for noise removal decreases with age resulting in more FPs, where noise is categorized as RSN or SOZ. For the SOZ identification task, there is a statistically significant trend for sensitivity to increase and specificity to decrease with age. This implies that as age progresses EPIK tends to classify more RSN or noise as SOZ, however, less SOZs are ignored as noise. Consequently, EPIK is observed to have accuracy greater than 85% at ages below 5, which is higher than those previously reported.

The LS-SVM approach had consistently better performance for SOZ identification task than noise removal. It also had the same pattern of increasing sensitivity and decreasing specificity with age. The LS-SVM approach had higher variance in performance across subjects. This indicates that the hand-crafted features chosen in Hunyadi et al. may be less applicable to specific scenarios of DRE in children.

CNN approach outperformed EPIK and LS-SVM for all age groups for noise removal. However, it had lower performance for SOZ identification. In the training data there were only 318 SOZ localizing ICs as opposed to 2427 RSN IC. This may have led to underfitting of CNN technique for SOZ identification. For CNN technique in noise removal, both sensitivity and specificity increased with age. This potentially indicates that CNN technique is finding novel hidden features from the ICs that are characteristic of RSN but not SOZ.

Overall, EPIK provided consistent performance across the three age categories considered in this study compared to prior reported methods. Whereas the ML techniques of Hunyadi and CNN have significantly higher variance, possibly indicating inconsistent performance.

### Performance on Subjects Undergoing Surgery

Out of the 52 subjects considered in this study 24 underwent surgery. The surgical outcomes were varied with 16 becoming seizure free (Engel I) after surgically destroying expert identified SOZ using rs-fMRI and 7 having reduced post operative seizure frequency (Engel II) (Table 7). We focused on EPIK and LS-SVM for the SOZ identification task on the 24 subjects that underwent surgery, because CNN had significantly poorer performance than the other two.

Table 7 shows that, for subjects whose post operative outcomes are either seizure free or significantly reduced frequency, the agreement between EPIK and expert hand classification is significantly high (88.9% sensitivity and 79% specificity). Although LS-SVM approach has nearly similar accuracy as EPIK, Sensitivity is far lower in LS-SVM, with significant individual variance. To better understand the difference between EPIK and LS-SVM approach, the graph 600 of FIG. 6 shows the receiver operating characteristics (ROC) curve for both EPIK and LS-SVM. EPIK exhibits higher sensitivity and specificity than LS-SVM, which appears to possibly sacrifice one for the other. More specifically, FIG. 6 shows an ROC curve for EPIK and LS-SVM approach for patients undergoing surgery. A curve close to the top left-hand corner of the graph is favorable and shows a balance between sensitivity and specificity.

For patients undergoing ablation surgery the specificity for EPIK was 82.9% while the sensitivity was 88%. This is preliminarily encouraging result given that ablation is minimally invasive and thus largely accepted as less risky than resection. The specificity and sensitivity in EPIK for patients undergoing resection reduces to 79.5% and 86.6% respectively. Ten out of 15 subjects with ablation procedure were seizure free (Engel 1 outcome), which is slightly better than recently reported statistics (66% in this study, versus. 60.4% reported in other studies).

### Reduction in IC Sorting Effort for the Neurosurgeon/Neurologist

The ICs marked as SOZ by the EPIK method can be supplied to the Neurosurgeon or neurologist for localization of SOZs in the brain. The number of SOZ classifications in EPIK per subject is 22 (±4). Out of which 16 are true positive SOZ ICs, 2 are noise ICs, and 4 are RSN ICs. These ICs are then evaluated by the neurosurgeon or neurologist for determining SOZ in the brain. This implies that there is ˜5 times reduction in the number of ICs to be analyzed by the neurosurgeon or neurologist. This can significantly aide in pre surgical screening by reducing the cognitive burden of the neurosurgeon or neurologist and improve accuracy of the SOZ identification.

### Discussion

A strength of EPIK, that may increase its utility, is that it does not require any prior training data and hence it is a plug-n-play IC sorting method. EPIK combines spatial and temporal markers specific for RSN and SOZ which results in possibly equivalent or better performance than prior methods. The waterfall technique removes the number of noise ICs using well established expert rules, hence may reduce false positives and increase true positives of SOZ localizing ICs.

For subjects with good post operative outcomes, there was excellent agreement between expert hand sorting and EPIK based SOZ localizing IC identification. Also, EPIK appeared to performance well in those less than 5 years of age, in whom surgery yields improved developmental outcomes.

The LS-SVM approach did not performs as well for the noise identification task, but drastically improves for SOZ identification task. This was expected because the hand selected features proposed by Hunyadi et al. are specifically geared towards the SOZ identification task. However, LS-SVM exhibits significant valiance in performance across subjects resulting in inconsistent accuracy in this study. EPIK had higher and consistent balance in identification of all three categories of IC compared to LS-SVM herein.

The CNN approach had the lower performance for SOZ identification. However, there was a significant improvement in the performance for the noise identification task. This can be explained by the difference in data availability for the two tasks. This gives confidence that CNN can perform better if given adequate number of training-SOZ-localizing ICs, an avenue for future research.

### Additional Directions

Subtypes of epilepsy-acquired, congenital/genetic, and surgical approaches success metrics should be statistically evaluated with acceptable power. Lastly, repeat studies in same individuals over time would increase knowledge of validity and reproducibility of the tool.

The majority of the subjects in this study received propofol infusion for sedation as part of standard of clinical care for epilepsy surgery evaluation. Head motion maximum was less than 1 mm framewise displacement in any direction. Although propofol use has minimal effect on the overall rs-fMRI BOLD signal, it puts small but additional risks on the child. Several research works have proposed alternate methods of reducing head motion, through engaging the child with videos and post processing by measuring and accounting for head movements through computational methods. An area of future study is to evaluate the effect of sedation on the EPIK SOZ identification accuracy and integration of live motion monitoring and reduction-based approaches towards elimination of head movement artifacts.

**General Non-Limiting Conclusions**

- - 1. EPIK identified seizure onset zone (SOZ) localizing resting state
    fMRI independent components in children with drug resistant epilepsy
    with accuracy of 84.7% in this preliminary study.
  - 2. EPIK can reduce the number of potential ICs to be analyzed by the
    neurosurgeon by ˜5-fold, hence significantly reducing the time
    commitment for pre-surgical evaluation.
  - 3. EPIK is unsupervised and does not need any prior example of SOZ
    and works by codifying expert knowledge about fMRI noise and SOZ
    markers.
  - 4. EPIK had consistent performance across age groups, gender, and
    has been validated with surgical outcomes.
  - 5. EPIK appeared to performance best for those under 5 years of age,
    and thus may enable successful surgeries early in their life,
    potentially improving long-term post operative outcomes.
  - 6. EPIK preliminary performed as well or better than shallow and
    deep learning systems for identification of SOZ localizing ICs in
    resting state fMRI.

Referring to FIG. 7, a computing device 1200 is illustrated which may be configured, via one or more of an application 1211 or computer-executable instructions, to execute functionality described herein associated with localization of seizure onset zone from independent components of resting state functional magnetic resonance. More particularly, in some embodiments, aspects of the predictive methods herein may be translated to software or machine-level code, which may be installed to and/or executed by the computing device 1200 such that the computing device 1200 is configured to such execute functionality as described herein. It is contemplated that the computing device 1200 may include any number of devices, such as personal computers, server computers, hand-held or laptop devices, tablet devices, multiprocessor systems, microprocessor-based systems, set top boxes, programmable consumer electronic devices, network PCs, minicomputers, mainframe computers, digital signal processors, state machines, logic circuitries, distributed computing environments, and the like.

The computing device 1200 may include various hardware components, such as a processor 1202, a main memory 1204 (e.g., a system memory), and a system bus 1201 that couples various components of the computing device 1200 to the processor 1202. The system bus 1201 may be any of several types of bus structures including a memory bus or memory controller, a peripheral bus, and a local bus using any of a variety of bus architectures. For example, such architectures may include Industry Standard Architecture (ISA) bus, Micro Channel Architecture (MCA) bus, Enhanced ISA (EISA) bus, Video Electronics Standards Association (VESA) local bus, and Peripheral Component Interconnect (PCI) bus also known as Mezzanine bus.

The computing device 1200 may further include a variety of memory devices and computer-readable media 1207 that includes removable/non-removable media and volatile/nonvolatile media and/or tangible media, but excludes transitory propagated signals. Computer-readable media 1207 may also include computer storage media and communication media. Computer storage media includes removable/non-removable media and volatile/nonvolatile media implemented in any method or technology for storage of information, such as computer-readable instructions, data structures, program modules or other data, such as RAM, ROM, EEPROM, flash memory or other memory technology, CD-ROM, digital versatile disks (DVD) or other optical disk storage, magnetic cassettes, magnetic tape, magnetic disk storage or other magnetic storage devices, or any other medium that may be used to store the desired information/data and which may be accessed by the computing device 1200. Communication media includes computer-readable instructions, data structures, program modules, or other data in a modulated data signal such as a carrier wave or other transport mechanism and includes any information delivery media. The term “modulated data signal” means a signal that has one or more of its characteristics set or changed in such a manner as to encode information in the signal. For example, communication media may include wired media such as a wired network or direct-wired connection and wireless media such as acoustic, RF, infrared, and/or other wireless media, or some combination thereof. Computer-readable media may be embodied as a computer program product, such as software stored on computer storage media.

The main memory 1204 includes computer storage media in the form of volatile/nonvolatile memory such as read only memory (ROM) and random access memory (RAM). A basic input/output system (BIOS), containing the basic routines that help to transfer information between elements within the computing device 1200 (e.g., during start-up) is typically stored in ROM. RAM typically contains data and/or program modules that are immediately accessible to and/or presently being operated on by processor 1202. Further, data storage 1206 in the form of Read-Only Memory (ROM) or otherwise may store an operating system, application programs, and other program modules and program data.

The data storage 1206 may also include other removable/non-removable, volatile/nonvolatile computer storage media. For example, the data storage 1206 may be: a hard disk drive that reads from or writes to non-removable, nonvolatile magnetic media; a magnetic disk drive that reads from or writes to a removable, nonvolatile magnetic disk; a solid state drive; and/or an optical disk drive that reads from or writes to a removable, nonvolatile optical disk such as a CD-ROM or other optical media. Other removable/non-removable, volatile/nonvolatile computer storage media may include magnetic tape cassettes, flash memory cards, digital versatile disks, digital video tape, solid state RAM, solid state ROM, and the like. The drives and their associated computer storage media provide storage of computer-readable instructions, data structures, program modules, and other data for the computing device 1200.

A user may enter commands and information through a user interface 1240 (displayed via a monitor 1260) by engaging input devices 1245 such as a tablet, electronic digitizer, a microphone, keyboard, and/or pointing device, commonly referred to as mouse, trackball or touch pad. Other input devices 1245 may include a joystick, game pad, satellite dish, scanner, or the like. Additionally, voice inputs, gesture inputs (e.g., via hands or fingers), or other natural user input methods may also be used with the appropriate input devices, such as a microphone, camera, tablet, touch pad, glove, or other sensor. These and other input devices 1245 are in operative connection to the processor 1202 and may be coupled to the system bus 1201, but may be connected by other interface and bus structures, such as a parallel port, game port or a universal serial bus (USB). The monitor 1260 or other type of display device may also be connected to the system bus 1201. The monitor 1260 may also be integrated with a touch-screen panel or the like.

The computing device 1200 may be implemented in a networked or cloud-computing environment using logical connections of a network interface 1203 to one or more remote devices, such as a remote computer. The remote computer may be a personal computer, a server, a router, a network PC, a peer device or other common network node, and typically includes many or all of the elements described above relative to the computing device 1200. The logical connection may include one or more local area networks (LAN) and one or more wide area networks (WAN) but may also include other networks. Such networking environments are commonplace in offices, enterprise-wide computer networks, intranets and the Internet.

When used in a networked or cloud-computing environment, the computing device 1200 may be connected to a public and/or private network through the network interface 1203. In such embodiments, a modem or other means for establishing communications over the network is connected to the system bus 1201 via the network interface 1203 or other appropriate mechanism. A wireless networking component including an interface and antenna may be coupled through a suitable device such as an access point or peer computer to a network. In a networked environment, program modules depicted relative to the computing device 1200, or portions thereof, may be stored in the remote memory storage device.

Certain embodiments are described herein as including one or more modules. Such modules are hardware-implemented, and thus include at least one tangible unit capable of performing certain operations and may be configured or arranged in a certain manner. For example, a hardware-implemented module may comprise dedicated circuitry that is permanently configured (e.g., as a special-purpose processor, such as a field-programmable gate array (FPGA) or an application-specific integrated circuit (ASIC)) to perform certain operations. A hardware-implemented module may also comprise programmable circuitry (e.g., as encompassed within a general-purpose processor or other programmable processor) that is temporarily configured by software or firmware to perform certain operations. In some example embodiments, one or more computer systems (e.g., a standalone system, a client and/or server computer system, or a peer-to-peer computer system) or one or more processors may be configured by software (e.g., an application or application portion) as a hardware-implemented module that operates to perform certain operations as described herein.

Accordingly, the term “hardware-implemented module” encompasses a tangible entity, be that an entity that is physically constructed, permanently configured (e.g., hardwired), or temporarily configured (e.g., programmed) to operate in a certain manner and/or to perform certain operations described herein. Considering embodiments in which hardware-implemented modules are temporarily configured (e.g., programmed), each of the hardware-implemented modules need not be configured or instantiated at any one instance in time. For example, where the hardware-implemented modules comprise a general-purpose processor configured using software, the general-purpose processor may be configured as respective different hardware-implemented modules at different times. Software may accordingly configure the processor 1202, for example, to constitute a particular hardware-implemented module at one instance of time and to constitute a different hardware-implemented module at a different instance of time.

Hardware-implemented modules may provide information to, and/or receive information from, other hardware-implemented modules. Accordingly, the described hardware-implemented modules may be regarded as being communicatively coupled. Where multiple of such hardware-implemented modules exist contemporaneously, communications may be achieved through signal transmission (e.g., over appropriate circuits and buses) that connect the hardware-implemented modules. In embodiments in which multiple hardware-implemented modules are configured or instantiated at different times, communications between such hardware-implemented modules may be achieved, for example, through the storage and retrieval of information in memory structures to which the multiple hardware-implemented modules have access. For example, one hardware-implemented module may perform an operation, and may store the output of that operation in a memory device to which it is communicatively coupled. A further hardware-implemented module may then, at a later time, access the memory device to retrieve and process the stored output. Hardware-implemented modules may also initiate communications with input or output devices.

Computing systems or devices referenced herein may include desktop computers, laptops, tablets e-readers, personal digital assistants, smartphones, gaming devices, servers, and the like. The computing devices may access computer-readable media that include computer-readable storage media and data transmission media. In some embodiments, the computer-readable storage media are tangible storage devices that do not include a transitory propagating signal. Examples include memory such as primary memory, cache memory, and secondary memory (e.g., DVD) and other storage devices. The computer-readable storage media may have instructions recorded on them or may be encoded with computer-executable instructions or logic that implements aspects of the functionality described herein. The data transmission media may be used for transmitting data via transitory, propagating signals or carrier waves (e.g., electromagnetism) via a wired or wireless connection.

It should be understood from the foregoing that, while particular embodiments have been illustrated and described, various modifications can be made thereto without departing from the spirit and scope of the invention as will be apparent to those skilled in the art. Such changes and modifications are within the scope and teachings of this invention as defined in the claims appended hereto.

