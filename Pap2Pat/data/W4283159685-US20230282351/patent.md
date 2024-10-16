# DESCRIPTION

## FIELD OF INVENTION

The present invention relates to methods and apparatus, and more particularly to computer implemented methods and computer apparatus, still more particularly, the invention relates to image processing for images of the human brain such as magnetic resonance images, and to methods and computer apparatus which use image processing for predicting and/or identifying cognitive impairment in the subject of such images.

## BACKGROUND

A variety of medical imaging techniques exist, and the spatial resolution achievable in these methods is increasingly accurate. Millimetre and even sub-millimetre resolution can often be achieved. The ability of these methods to distinguish between different types of tissue, and to identify structure within tissue, is also increasing, e.g. based on image contrast mechanisms of different types.

Accurate structural imaging can be performed by radiographic and tomographic techniques such as projection radiography and fluoroscopy, and X-ray computed tomography (CT), ultrasound techniques such as elastography, and magnetic resonance imaging (MRI). Other types of medical imaging are possible. For example, functional imaging techniques aim to provide contrast mechanisms which show underlying function. Techniques such as functional magnetic resonance imaging have been used for this purpose. Intuitively it would seem that the best way to investigate cognitive function is by use of functional neuroimaging techniques.

Another factor which militates against the use of structural images to predict cognitive changes or function is that whilst human anatomy might have some perceived norms there is a wide degree of variability between individuals which arise from both hereditary and environmental factors.

For example, the problem of how to map images of the brain of an individual subject onto a normalised anatomical model of the brain to facilitate comparisons between subjects and across populations is itself a non-trivial issue. In the context of such inherent variability, making predictions as to cognitive function based on structural data is fraught with potential error and difficulty.

A variety of cognitive disorders exist. Mild cognitive impairment (MCI) is a condition in which someone has minor problems with cognition—their mental abilities such as memory or thinking. In MCI these difficulties are worse than would normally be expected for a healthy person of their age. A person with MCI is more likely to go on to develop dementia.

Dementia is the name for a set of symptoms that includes memory loss and difficulties with thinking, problem-solving or language. Dementia develops when the brain is damaged by diseases, such as Alzheimer's disease. In Alzheimer's disease, among the areas often damaged first are the hippocampus. The amygdala and cortex are generally affected later than the hippocampus. The disease is however progressive, and may ultimately affect many regions of the brain. Damage to the hippocampus and amygdala may become measurable only after the symptoms of dementia are manifest.

Early diagnosis of MCI is a significant issue because once diagnosed steps can be taken to lessen the likelihood that a patient with MCI will go on to develop dementia.

## SUMMARY

Aspects and examples of the present disclosure aim to address technical problems related to those discussed above. In particular they may aim to provide a method of predicting or diagnosing cognitive impairment in a human subject based on images of the subject's brain.

An aspect of the disclosure provides a computer implemented method of predicting or diagnosing cognitive impairment in a human subject based on images of the subject's brain, the method comprising: identifying in the images, image regions corresponding to at least two of: the left cerebral cortex; the right cerebral cortex; the left hippocampus; and the left amygdala; and, determining for each of the identified image regions at least one image metric, wherein the or each at least one image metric of each image region provides a quantitative indication of structure in that image region; and determining an indicator based on the image metrics according to a predetermined method; obtaining reference data configured to indicate a cognitive impairment state using indicators determined according to the predetermined method; and predicting or diagnosing cognitive impairment in the subject based on comparing the indicator with the reference data.

Alternatively, different image regions may be used in this method instead. In one aspect, in place of the image regions listed above, the image regions may comprise the left choroid plexus; the right hippocampus; right cerebellar cortex; and the right inferior lateral ventricle.

In another aspect in place of the image regions listed above, the image regions may comprise the right middle temporal gyrus; the right rostral middle frontal; the right supramarginal; and the right temporal pole.

In an aspect there is provided a computer implemented method of distinguishing between human subjects the method comprising: determining, based on processing by the computer of digital image data obtained from the images, first image metrics providing a quantitative indication of structure in the left choroid plexus; the right hippocampus; right cerebellar cortex; and the right inferior lateral ventricle, determining a first indicator based on the first image metrics according to a first predetermined method; and distinguishing between Alzheimer's disease and non-Alzheimer's disease subjects based on the first indicator. Having identified subjects not having Alzheimer's disease in this way, the method may further comprise distinguishing between subjects having Alzheimer's disease and prodromal Alzheimer's disease determining, based on processing by the computer of digital image data obtained from the images, second image metrics providing a quantitative indication of structure in the right middle temporal gyrus; the right rostral middle frontal; the right supramarginal; and the right temporal pole determining a second indicator based on the second image metrics according to a second predetermined method thereby to distinguish between subjects having Alzheimer's disease and subjects having prodromal Alzheimer's disease.

In an aspect there is provided a method of distinguishing between Alzheimer's disease and non-Alzheimer's disease subjects. The method comprises a computer implemented method of predicting or diagnosing cognitive impairment in a human subject based on images of the subject's brain, the method comprising: determining, based on processing by the computer of digital image data obtained from the images, image metrics comprising at least one of: a complexity metric of an image region corresponding to the right middle temporal gyrus; an image texture metric of a image region corresponding to the right rostral middle frontal; an image texture metric in the image region corresponding to the right supramarginal; and an image intensity metric in the image region corresponding to the right temporal pole; the method further comprising: determining an indicator based on said image metrics according to a predetermined method; and predicting or diagnosing cognitive impairment state in the subject based on the indicator.

In an aspect there is provided a method of distinguishing between Alzheimer's disease and mild cognitive impairment (MCI) such as prodromal Alzheimer's disease. The method comprises a computer implemented method of predicting or diagnosing cognitive impairment in a human subject based on images of the subject's brain, the method comprising: determining, based on processing by the computer of digital image data obtained from the images, image metrics comprising at least one of an intensity measure of an image region corresponding to the left choroid plexus a morphological measure of the image region corresponding to the right hippocampus; an image texture in the image region corresponding to the right cerebellar cortex; and an image texture in the image region corresponding to the right inferior lateral ventricle; the method further comprising: determining an indicator based on said image metrics according to a predetermined method; and predicting or diagnosing cognitive impairment state in the subject based on the indicator.

The predetermined method of determining the indicator may comprise applying a weighting to each of the image metrics and combining the weighted image metrics, for example using a weighted sum. The combination may be linear. The first predetermined method may comprise a first set of weights, and a corresponding first set of image metrics such as any one of those described and claimed with reference to FIG. 13 and Table 13, below. The second predetermined method may comprise a second set of weights, and a corresponding second set of image metrics such as any one of those described and claimed with reference to FIG. 14 and Table 14, below.

One of the at least two image regions may be the left amygdala, and the at least one image metrics for the left amygdala may comprise a texture feature such as a non-uniformity measure. For example non-uniformity of a grey level size zone matrix, GLSZM.

At least one image metrics for the left amygdala may comprise a measure of correlation of the grey level co-occurrence matrix GLCM, such as an informational measure of correlation of the GLCM.

The image data upon which the image metrics described herein are based may be filtered in order to determine those image metrics, for example it may be high pass filtered, for example using a wavelet based filter, for example using a 3D high pass filter.

One of the at least two image regions may comprise the left hippocampus, and a run length non-uniformity, RLN, measure of a grey level run length matrix GLRLM may provide one of the image metrics of the image metrics of the left hippocampus.

One of the at least two image regions may comprise the left cerebral cortex, and the surface area to volume ratio may provide one of the image metrics of the left cerebral cortex. A measure of the degree to which the left cerebral cortex is spherical, for example its sphericity, may also provide one of the image metrics of the left cerebral cortex.

One of the at least one image metrics for the left cerebral cortex may be a fractal dimension maximum value, for example wherein the image region is high pass filtered in the first and third dimension and low pass filtered in the second dimension (HLH), for example using a wavelet based filter, for example using a 3D wavelet filter.

One of the at least two image regions may comprise the right hippocampus.

One of the at least one image metrics for the right hippocampus may comprise compactness, for example based on

\({F_{{{morph}.{comp}}\text{.1}} = \frac{V}{\pi^{1/2}A^{3/2}}},\)

wherein V is the volume of the right hippocampus image region and A is the surface area of the right hippocampus image region.

One of the at least two image regions may comprise the right cerebral cortex. One of the at least one image metrics for the right cerebral cortex may comprise the minimum value of the right cerebral cortex image region, for example filtered with a low pass filter, for example using a wavelet based filter, for example using a 3D low pass filter. One of the at least one image metrics for the right cerebral cortex may comprise a fractal dimension maximum value, for example wherein the image region is high pass filtered in the first and third dimension and low pass filtered in the second dimension (HLH), for example using a wavelet based filter, for example using a 3D wavelet filter.

One of the at least two image regions may comprise the left inferior lateral ventricle. One of the at least one image metrics for the left inferior lateral ventricle may comprise a measure of correlation of the grey level co-occurrence matrix GLCM, such as an informational measure of correlation of the GLCM. The image data upon which the GLCM is based may be low pass filtered in the first and third dimension and high pass filtered in the second dimension (LHL), for example using a wavelet based filter, for example using a 3D wavelet filter.

An aspect of the disclosure provides a computer implemented method of predicting or diagnosing cognitive impairment in a human subject based on images of the subject's brain, the method comprising: identifying in the images, image regions corresponding to the left amygdala, the left inferior lateral ventricle, the left hippocampus, and the right hippocampus; determining for each of the identified image regions at least one image metric, wherein the or each at least one image metric of each image region provides a quantitative indication of structure in that image region; and determining an indicator based on the image metrics according to a predetermined method; obtaining reference data configured to indicate a cognitive impairment state using indicators determined according to the predetermined method; and predicting or diagnosing cognitive impairment in the subject based on comparing the indicator with the reference data.

The image metric for the left inferior lateral ventricle may comprise a correlation measure of the grey level co-occurrence matrix, GLCM, (such as information based correlation). The image region may be filtered, for example using an LHL wavelet filter.

The image metric for the left hippocampus may comprise a run length non-uniformity measure of the grey level run length matrix, GLRLM.

The image metric for the left amygdala may comprise a grey level non-uniformity measure of the grey level size zone matrix, GLSZM.

The image metric for the right hippocampus may comprise compactness.

An aspect of the disclosure provides a computer implemented method of predicting or diagnosing cognitive impairment in a human subject based on images of the subject's brain, the method comprising: identifying, in the images, image regions corresponding to sub-regions of the cortex comprising: the banks of the superior temporal sulcus; the lateral occipital lobe; the entorhinal cortex; and the pars orbitalis; determining for each of the identified image regions a corresponding at least one image metric, wherein the at least one image metric comprises at least one of: (i) a measure of image texture; (ii) a measure of image intensity in the image region, such as its central tendency; and (iii) a morphological measure of the image region determining an indicator based on the image metrics according to a predetermined method; obtaining reference data configured to indicate a cognitive impairment state using indicators determined according to the predetermined method; and predicting or diagnosing cognitive impairment in the subject based on comparing the indicator with the reference data.

The sub-region of the cortex in the banks of the superior temporal sulcus may comprise the right banks of the superior temporal sulcus. The sub-region of the cortex in the lateral occipital lobe may comprise the left lateral occipital lobe. The sub-region of the cortex in the entorhinal cortex may comprise the left entorhinal cortex. The sub-region of the cortex in the pars orbitalis may comprise the left pars orbitalis.

The at least one image metric of the entorhinal cortex, such as the left entorhinal cortex, may comprise the measure of image intensity such as at least one of: (a) a measure of its central tendency, for example the mean; and (b) a measure of its spread such as its maximum and/or minimum.

The at least one image metric of the left entorhinal cortex may comprise the measure of image texture, such as a metric of correlation in the grey level co-occurrence matrix which may be used in combination with a small zone emphasis of the grey level size zone matrix.

The at least one image metric of the left lateral occipital lobe may comprise the metric of image texture, such as a neighbourhood grey tone based feature—for example a measure of complexity in the neighbourhood grey tone difference matrix, NGTDM.

The at least one image metric of the banks of the right superior temporal sulcus may comprise at least one of: (a) the measure of image intensity, for example the measure of central tendency; and (b) the measure of image texture such as a measure based on the grey level co-occurrence matrix such as the sum variance, e.g.

\(F_{{cm}.{sum}.{var}} = {\sum\limits_{k = 2}^{2N_{g}}{\left( {k - µ} \right)^{2}p_{{i + j},k}}}\)

An aspect provides a computer implemented method of predicting or diagnosing cognitive impairment in a human subject based on images of the subject's brain, the method comprising: identifying, in the images, image regions corresponding to sub-regions of the cortex comprising: the left inferior temporal lobe, the left entorhinal cortex the left superior parietal lobe, the left middle temporal lobe, and the right superior parietal lobe, determining for each of the identified image regions a corresponding at least one image metric, wherein the at least one image metric comprises at least one of: (i) a measure of image texture; (ii) a measure of image intensity in the image region, such as its central tendency; and (iii) a morphological measure of the image region determining an indicator based on the image metrics according to a predetermined method; obtaining reference data configured to indicate a cognitive impairment state using indicators determined according to the predetermined method; and predicting or diagnosing cognitive impairment in the subject based on comparing the indicator with the reference data.

An aspect of the disclosure provides a computer implemented method of predicting or diagnosing cognitive impairment in a human subject based on images of the subject's brain, the method comprising: identifying in the images, image regions corresponding to the left amygdala and at least one of: the left cerebral cortex; the right cerebral cortex; and the left hippocampus; and, determining for each of the identified image regions at least one image metric, wherein the or each at least one image metric of each image region provides a quantitative indication of structure in that image region; and determining an indicator based on the image metrics according to a predetermined method;

obtaining reference data configured to indicate a cognitive impairment state using indicators determined according to the predetermined method; and predicting or diagnosing cognitive impairment in the subject based on comparing the indicator with the reference data.

One of the at least one image metrics for the left amygdala may comprise compactness. One of the at least one image metrics for the left amygdala may comprise a run length non-uniformity measure. For example it may be based on a grey level run length matrix, GLRLM, for example wherein it comprises at least one of GLRLM run length non uniformity and GLRLM grey level non-uniformity.

One of the at least one image regions may be the left hippocampus and one of the at least one image metrics for the left hippocampus may be based on compactness and/or a texture strength, for example texture strength based on neighbourhood grey tone difference.

The image regions used in the methods described herein may comprise subcortical regions such as: Entorhinal cortex, Fusiform gyrus, Banks of the superior temporal sulcus, Inferior parietal lobe, isthmus cingulate, Medial orbitofrontal, Middle temporal, Parahippocampal, Rostral middlefrontal, Superior parietal and so forth.

One such aspect of the disclosure comprises a computer Implemented method of predicting or diagnosing cognitive impairment in a human subject based on images of the subject's brain, the method comprising: identifying in the images, an image region corresponding to the fusiform gyrus, determining for the identified image region at least one image metric, wherein the at least one image metric comprises at least one of: (i) a texture feature indicating the prevalence of small zones having low grey level; (ii) a measure of central tendency, such as the mode; and (iii) a texture feature indicating the prevalence of short run lengths having low grey level thereby to provide a quantitative indication of structure in that image region; determining an indicator based on the image metrics according to a predetermined method; obtaining reference data configured to indicate a cognitive impairment state using indicators determined according to the predetermined method; and predicting or diagnosing cognitive impairment in the subject based on comparing the indicator with the reference data.

This method has been tested on a test population comprising control subjects and subjects having mild cognitive disfunction, and has been found to be able to distinguish between the two. It may also be able to distinguish AD subjects from control subjects.

One such aspect of the disclosure provides a computer Implemented method of predicting or diagnosing cognitive impairment in a human subject based on images of the subject's brain, the method comprising: identifying in the images, an image region corresponding to the entorhinal cortex, determining for the identified image region at least one image metric, wherein the at least one image metric comprises at least one of: (i) a morphological feature indicating the extent to which the region is spherical, for example spherical disproportion; (ii) a texture feature indicating the prevalence of small zones having high grey level; (iii) the minimum fractal dimension; and (iv) a measure of texture strength, such as a the texture strength of the neighbourhood grey tone difference matrix (NGTDM); thereby to provide a quantitative indication of structure in that image region; and determining an indicator based on the image metrics according to a predetermined method; obtaining reference data configured to indicate a cognitive impairment state using indicators determined according to the predetermined method; and predicting or diagnosing cognitive impairment in the subject based on comparing the indicator with the reference data.

This method has been tested on a test population comprising control subjects and subjects having Alzheimer's Disease, and has been found to be able to distinguish between the two. It may also be able to distinguish MCI subjects from control subjects. This method may be further refined by identifying in the images, an image region corresponding to the fusiform gyrus, determining for the image region corresponding to the fusiform gyrus at least one of the following image metrics: (i) a texture feature indicating the prevalence of small zones having low grey level; (ii) a measure of central tendency, such as the mode; and

(iii) a texture feature indicating the prevalence of short run lengths having low grey level thereby to provide the quantitative indication of structure in the image region corresponding to the fusiform gyrus.

The texture feature indicating the prevalence of small zones having low grey level may comprise the grey level size zone (GLSZM) small zone low grey level emphasis.

\(F_{{szm}.{szlge}} = {\frac{1}{N_{s}}{\sum\limits_{i = 1}^{N_{g}}{\sum\limits_{j = 1}^{N_{z}}\frac{s_{ij}}{i^{2}j^{2}}}}}\)

The texture feature indicating the prevalence of short run lengths having low grey level comprises the GLRLM Short Run Low Gray Level Emphasis (SRLGLE)

\(F_{{rlm}.{srlge}} = {\frac{1}{N_{s}}{\sum\limits_{i = 1}^{N_{g}}{\sum\limits_{j = 1}^{N_{r}}\frac{r_{ij}}{i^{2}j^{2}}}}}\)

Embodiments of the disclosure provide computer program products configured to program a programmable processor to perform any of the methods described and/or claimed herein. Embodiments also provide tangible non transitory computer readable media storing such computer program products, for example in the form of computer readable instructions.

Embodiments of the disclosure also provide computer apparatus configured to perform any of the methods described and/or claimed herein.

Embodiments of the disclosure provide methods of diagnosing cognitive impairment, for example MCI or dementia, for example Alzheimer's disease. These and other embodiments may enable early treatment to be provided, e.g. before the impairment can be detected by traditional diagnostic techniques.

Embodiments of the present disclosure may provide methods of selecting subjects for participation in clinical trials. For example, such embodiments may comprise selecting patients based on the indicators defined herein.

Embodiments also provide methods of classifying subjects and/or identifying cohorts of patients in such trials, for example to permit intra-cohort and inter-cohort comparison amongst or between cohorts of patients identified based on the indicators defined herein.

Some embodiments provide methods of treating cognitive impairment, the methods comprising determining an indicator of cognitive impairment according to any one or more of the methods described and/or claimed herein, and selecting a therapy, such as a medicament, dosage regimen, or course of treatment based on said indicator.

The images may comprise images having contrast able to distinguish between tissue types in the human brain, and may have sufficient resolution to permit them to resolve structures in the human brain such as cortex, gyri and sulci of the grey matter, white matter structures such as cortico-cortical fibres, bundles of such fibres and so forth. The image contrast mechanism and/or the resolution may also be sufficient to enable aggregates of grey matter within cerebral white matter to be resolved. For example, the images may be capable of resolving sub-structures which make up one or more of the following anatomical features of the brain:


- - Left Cerebral White Matter
  - Left Inferior Lateral Ventricle
  - Left Cerebral Cortex
  - Right Cerebral Cortex
  - Left Hippocampus
  - Left Amygdala
  - Left choroid plexus
  - Brain Stem
  - White matter (WM) hypointensities, which may comprise white matter
    lesions
  - Left Pallidum
  - Corpus Callosum Posterior
  - Left Inferior Lateral Ventricle
  - Right Hippocampus.

Any imaging technique capable of resolving such sub-structures may be used. For example, imaging methods able to distinguish water, water protein mixtures, and fat may be used. The images may have a resolution of at least 3 mm resolution or finer, for example at least 2 mm resolution, for example at least 1 mm. The images may have a resolution of better than 1 mm, for example 0.6 mm. The resolution may be isotropic. The images may be converted to 1 mm resolution by pre-processing steps such as those performed by FreeSurfer to enable image segmentation (e.g. they may be downsampled, and or smoothed e.g. with antialiasing filters, and so forth).

In an aspect there is provided a computer implemented method of predicting or diagnosing cognitive impairment in a human subject based on images of the subject's brain, the method comprising: identifying, in the images, image regions corresponding to sub-regions of the cortex comprising: the fusiform gyrus, the entorhinal cortex the temporal pole, the transverse temporal cortex, and the insula, determining for each of the identified image regions a corresponding at least one image metric, wherein the at least one image metric comprises at least one of: (i) a measure of image texture (i) a measure of image intensity in the image region, such as its central tendency; and (iii) a morphological measure of the image region determining an indicator based on the image metrics according to a predetermined method; obtaining reference data configured to indicate a cognitive impairment state using indicators determined according to the predetermined method; and predicting or diagnosing cognitive impairment in the subject based on comparing the indicator with the reference data.

The at least one image metric of the entorhinal cortex may comprise a measure of its central tendency, for example the mean and/or the morphological measure. The image region corresponding to the entorhinal cortex may correspond primarily to the left entorhinal cortex or primarily to the right entorhinal cortex, and different image metrics may be used in the left entorhinal cortex as compared to those used in the right entorhinal cortex. The morphological measure in the entorhinal cortex may comprise an indication of shape, such as sphericity for example spherical distortion.

The at least one image metric in the entorhinal cortex may comprise the measure of image texture, such as a measure indicating the degree of heterogeneity in grey level. The measure of image texture may comprise a texture feature based on grey level zone size, such as a feature indicating the prevalence of small zone size. The measure of image texture may comprise a texture feature based on the grey level run length, such as a feature indicating the prevalence of short runs.

The image region corresponding to the fusiform gyrus may correspond primarily to the left fusiform gyrus e.g. in preference to the right (e.g. only to the left). In this region the metric of the left fusiform gyrus may comprise: (a) a first order statistic indicating grey level intensity, such as a measure of central tendency or minimum, and/or (b) the measure of image texture, such as a measure indicating the degree of heterogeneity in grey level. This measure of image texture may comprise a texture feature based on the grey level run length, such as a feature indicating the prevalence of short runs, for example those having low grey level.

The image region corresponding to the temporal pole may correspond primarily to the right temporal pole, for example in preference to the left (e.g. only to the right). In this context image metric of the temporal pole may comprise a first order statistic indicating grey level intensity, such as a measure of central tendency.

The image region corresponding to the transverse temporal cortex may correspond primarily to the right transverse temporal cortex, for example in preference to the left (e.g. only to the right). In this context, the image metric of the transverse temporal cortex comprises a first order statistic indicating grey level intensity, such as a measure or central tendency or distribution

The image region corresponding to the insula may correspond primarily to the right insula, for example in preference to the left (e.g. only to the right). In this context, the image metric of the insula may comprise the measure of image texture, such as a measure indicating the degree of heterogeneity in grey level. The measure of image texture may comprise a texture feature based on the grey level run length, such as a feature indicating the prevalence of short runs.

The image region corresponding to the entorhinal cortex may correspond primarily to the right entorhinal cortex, for example in preference to the left (e.g. only to the right). In this context, the at least one image metric of the entorhinal cortex may comprise a measure of image intensity such as a measure of its spread such as its maximum and/or minimum. The at least one image metric of the entorhinal cortex may comprise the measure of image texture, such as a metric of correlation in the grey level co-occurrence matrix this metric may be used in combination with a metric of the grey level size zone matrix, such as a metric indicating the prevalence of small zones.

The image regions may comprise a sub region of the cortex corresponding to the lateral occipital lobe, which may correspond primarily to the left lateral occipital lobe, for example in preference to the right (e.g. only to the left). The at least one image metric of the left lateral occipital lobe may comprise the metric of image texture, such as a neighbourhood grey tone based feature—for example a measure of complexity in the neighbourhood grey tone difference matrix, NGTDM.

The image regions may comprise a region which corresponds to the banks of the superior temporal sulcus, and may correspond primarily to the right banks of the superior temporal sulcus, for example in preference to the left (e.g. only to the right). The at least one image metric of the right banks of the superior temporal sulcus comprises at least one of: (a) the measure of image intensity, for example the measure of central tendency; and (b) the measure of image texture such as a measure based on the grey level co-occurrence matrix.

The image regions may comprise a sub region of the cortex corresponding to the caudal middle frontal cortex which may correspond primarily to the left caudal middle frontal cortex, for example in preference to the right (e.g. only to the left). In this context, the at least one image metric of the right caudal middle frontal cortex may comprise the metric of image texture, such as a neighbourhood grey tone based feature—for example a measure of complexity in the neighbourhood grey tone difference matrix, NGTDM.

The image regions may comprise a sub region of the cortex corresponding to the isthmus cingulate, which may correspond primarily to the left isthmus cingulate, for example in preference to the right (e.g. only to the left). The at least one image metric of the left isthmus cingulate may comprise a measure of image intensity, such as a measure of central tendency—e.g. the mean.

The image regions may comprise a sub region of the cortex corresponding to the rostral middle frontal cortex, which may correspond primarily to the right rostral middle frontal cortex, for example in preference to the left (e.g. only to the right). The at least one image metric of the right rostral middle frontal may comprise the measure of image intensity.

The methods described with reference to the above described aspect and the embodiments of that aspect may comprise age normalising the images prior to identifying the image regions and determining said image metrics.

The image region corresponding to the entorhinal cortex may correspond primarily to the left entorhinal cortex. The at least one image metric of the left entorhinal cortex may comprise at least one of: (a) a metric of the grey level size zone matrix; and (b) a metric of the neighbourhood grey tone difference matrix.

The image regions may comprise a sub region of the cortex corresponding primarily to the left inferior parietal lobe, and the image metric of the left inferior parietal lobe may comprise a metric of image texture such as a metric of the grey level run length matrix.

The image regions may comprise a sub region of the cortex corresponding to the lateral occipital lobe and the image metric comprises a measure of image texture such as a measure of the fractal dimension for example a standard deviation of the fractal dimension.

The image regions may comprise a sub region of the cortex corresponding to the pars triangularis. For example, corresponding primarily to the left (e.g. in age normalised images) and alternatively to the right in non-age normalised data. The image metric of the pars triangularis may comprise a measure of image intensity such as a measure of central tendency.

The image regions may comprise a sub region of the cortex corresponding to the rostral middle frontal cortex, for example primarily to the left rostral middle frontal cortex. The at least one image metric of the rostral middle frontal cortex may comprise the measure of image texture, such as a measure based on the grey level size zone matrix, such as a metric indicating the variance of the zone sizes.

The image regions may comprise a sub region of the cortex corresponding to the superior temporal lobe (e.g. primarily to the left superior temporal lobe) and the image metrics of the left superior temporal lobe may comprise the measure of image texture, for example a metric based on at least one of: (a) the grey level size zone matrix; and (b) the grey level co-occurrence matrix.

The image regions may comprise a sub region of the cortex corresponding to the supramarginal cortex (e.g. primarily to the left supramarginal cortex) and the image metric of the left supramarginal cortex may comprise the measure of image texture, for example a measure based on the grey level size zone matrix.

The image metric of the temporal pole (e.g. primarily to the left temporal pole) may comprise a measure of image texture based on fractal dimension such as a minimum fractal dimension.

The image region corresponding to the insula may correspond primarily to the right insula in which case the image metric in the right insula may comprise a measure of image intensity such as a measure of central tendency, for example the mode.

A further aspect of the disclosure may provide a computer Implemented method of predicting or diagnosing cognitive impairment in a human subject based on images of the subject's brain. This aspect may find particular application in differentiating between subjects having Alzheimer's disease and control subjects. The method comprises: identifying, in the images, image regions corresponding to sub-regions of the cortex comprising: the inferior temporal lobe, the entorhinal cortex the superior parietal lobe, the middle temporal lobe, and the superior parietal lobe, determining for each of the identified image regions a corresponding at least one image metric, wherein the at least one image metric comprises at least one of: (i) a measure of image texture; (ii) a measure of image intensity in the image region, such as its central tendency; and (iii) a morphological measure of the image region determining an indicator based on the image metrics according to a predetermined method; obtaining reference data configured to indicate a cognitive impairment state using indicators determined according to the predetermined method; and predicting or diagnosing cognitive impairment in the subject based on comparing the indicator with the reference data.

In this aspect, the image metric in the inferior temporal lobe may correspond primarily to the left inferior temporal lobe in preference to the right (e.g. only to the left) and may comprise a measure of image intensity, such as a measure of central tendency. The at least one image metric in the entorhinal cortex may correspond primarily to the left entorhinal cortex and may comprise a measure of image texture such as a metric of the neighbourhood grey tone difference matrix, for example a contrast metric of the NGTDM.

The at least one image metric in the superior parietal lobe may correspond primarily to the left superior parietal lobe and may comprise a measure of image texture, such as a metric of the grey level co-occurrence matrix, such as autocorrelation of the grey level co-occurrence matrix.

The at least one image metric in the superior parietal lobe may correspond primarily to the right superior parietal lobe and may comprise a measure of image intensity such as the minimum.

The at least one image metric in the middle temporal lobe correspond primarily to the left middle temporal lobe and may comprises a measure of image intensity such as the maximum.

Embodiments of the present disclosure provide a computer implemented method of differentiating between human subjects having at least mild cognitive impairment, MCI, and control subjects, the method comprising obtaining images of each subject's brain, and performing any one or more of the methods described or claimed herein to differentiate between the subjects.

Embodiments of the present disclosure also provide a method of differentiating between human subjects having Alzheimer's Disease, AD, and control subjects, the method comprising obtaining images of each subject's brain, and performing any one or more of the methods described or claimed herein to differentiate between the subjects.

The methods described herein may comprise age normalising the image data prior to determining said at least one image metric. Normalising may comprise: (a) obtaining, for each voxel, j, a vector of intensity values wherein each intensity value comprises the intensity of the voxel, j, voxel in one of a corresponding plurality of images each obtained from a control subject (CN). The vector of intensity values at the voxel j may be denoted as xjCN (b) obtaining a vector of age values, each age value identifying the age of a corresponding one of the control subjects aCN so that each element of the vector of age values corresponds to an element of the vector of intensity values; (c) determining parameters of age related effects in the voxel, j, based on the vector of age values and the vector of intensity values and a model of said effects; and (d) using said model and said parameters to normalise intensity values in the voxel j in images of test subjects based on the age of said test subject.

The model of age related effects may comprise a linear model, such as a straight line or other linear model. Determining the parameters may comprise fitting said model to the vector of intensity values. For example, fitting may comprise least squares fitting of the model

xjNC=αjaNC+αj0.

to determine the parameters αj and αj0.

The model, and these parameters, can then be applies to images of test subjects (e.g. the MCI and AD groups) to remove the age effects of each voxel separately. For example, by estimating the age related effect in each voxel j for each subject based on the model and the parameters, and subtracting these effects from the corresponding intensity in said voxel, j.

For example, for the MCI group:

xjMCIar=xjMCII−αjaMCI+αj0.

Embodiments of the present disclosure also provide method of classifying subjects for a clinical study, the method comprising obtaining images of each subject's brain, and performing any one or more of the methods described or claimed herein to differentiate between the subjects.

Embodiments of the disclosure provide a computer program product, such as a tangible non-transitory computer readable medium storing program instructions configured to program a processor to perform the method of any preceding claim.

It will be appreciated in the context of the present disclosure that the images described herein, whether relating to control subjects or to test subjects may be coregistered with each other and/or with a reference image of the human brain. Such reference images may comprise an anatomical standard.

Magnetic resonance images having T1 contrast, such as T1 weighted MRI, may be particularly useful in the methods described herein. Other imaging methods having contrast mechanisms able to distinguish between different types of human brain tissue may also be used to provide the images upon which the methods described herein operate.

## DETAILED DESCRIPTION

A computer implemented method of predicting or diagnosing cognitive impairment in a human subject will now be described with reference to the apparatus shown in FIG. 1.

In overview, this apparatus segments the images to identify in those images, image regions corresponding to selected anatomical features in the brain. It then determines an image metric or metrics for each anatomical features (segmented image region). Each of these image metrics provides a quantitative indication of structure in that image region, which are combined according to a predetermined method to determine an indicator. The apparatus then obtains reference data against which the indicator is compared to predict or diagnose cognitive impairment in the subject.

The apparatus illustrated in FIG. 1 comprises a subject image data obtainer 20, a reference data store 26, and a controller 10. It may also be coupled to a source of image data 28.

The subject image data obtainer 20 may comprise a data interface 22 for communicating data with the controller 10 and/or with the source of image data 28. It may also comprise volatile and/or non-volatile data storage 24, such as a cache, connected to the data interface 22. The subject image data obtainer 20 may be connected (e.g. via the interface 22) to communicate with one or both of:


- - an imaging system such as a CT scanner, or an MRI scanner or other
    imaging system capable of acquiring appropriate images of the human
    brain; or
  - a store of appropriate images of the human brain.

Other sources of image data (such as network connections to local and/or wide area networks may also be used). Images of subjects can thus be provided to the controller 10 from a variety of sources.

The controller 10 may comprise a general purpose processor or similar processing logic, which is configured to segment images of the human brain according to a brain atlas model such as that defined in the freesurfer utilities which are available from https://surfer.nmr.mgh.harvard.edu/fswiki/CorticalParcellation. It will be appreciated in the context of the present disclosure that such utilities may assign neuroanatomical labels to each location on a cortical surface model based on probabilistic information estimated from a manually labelled training set (e.g. that which is made using FreeSurfer). Such procedures may incorporate both geometric information derived from the cortical model, and neuroanatomical convention, as found in the training set. The atlases used may comprise:


- - gyral based atlases such as the ‘Desikan-Killiany’ cortical atlas
    described in “*An automated labeling system for subdividing the
    human cerebral cortex on MRI scans into gyral based regions of
    interest*” Neuroimage 31 (2006) 968-980, by RS Desikan et al.
  - atlases based on parcellation schemes that divide the cortex into
    gyral and sulcal regions such as the ‘Destrieux’ cortical atlas
    described in “*Automatic parcellation of human cortical gyri and
    sulci using standard anatomical nomenclature*” NeuroImage 53, Issue
    1, 15 Oct. 2010, Pages 1-15, Destrieux et al.
  - the DKT40 atlas https://mindboggle.info/data.html or other similar
    atlases. Whatever atlas is used, the controller may be configured to
    identify, in image data having appropriate contrast and resolution,
    some or all of the following structures:
  - Left Cerebral White Matter
  - Left Inferior Lateral Ventricle
  - Left Cerebral Cortex
  - Right Cerebral Cortex
  - Left Hippocampus
  - Left Amygdala
  - Left choroid plexus
  - Brain Stem
  - White matter (WM) hypointensities, which may comprise white matter
    lesions
  - Left Pallidum
  - Corpus Callosum Posterior
  - Left Inferior Lateral Ventricle
  - Right Hippocampus

The controller may also be configured to segment, from the images regions of interest (ROI) corresponding to the structures which it identifies. This too may be done using approaches such as those defined in the FreeSurfer package or other equivalent packages.

The controller also comprises image processing functionality arranged to determine some or all of the features defined below. For example, the controller may be configured to determine for a given ROI:


- - First order statistics such as measures of central tendency,
    measures of spread, skewness and kurtosis;
  - Morphological features;
  - Grey Level Size Zone Matrix features;
  - Grey Level Co-occurrence Matrix (GLCM) features;
  - Neighbourhood grey tone difference based features;
  - Grey Level Run Length Matrix (GLRLM) features; and
  - Fractal dimension features.

Examples of such features and the way in which they may be determined by the controller are explained below. It will be appreciated in the context of the present disclosure that other equivalent and/or comparable image features may be used. In addition, the formulae given for the features listed are intended only to serve as an illustrative description of the way in which they can be provided. Typically, such metrics operate on digital data which may be encoded as a discrete grey level in each voxel of an ROI. It will be appreciated in the context of the present disclosure that the notations set out below, using indices and summations are intended to be implemented by the controller stepping through the intensity values (e.g. digital grey level data) stored in the pixels of the images (or ROI's of those images). The indices mentioned in the mathematical formulae below may thus connote the indices of stepwise computational methods, such as may be implemented using a counter incremented to step through the relevant set of digital data. Other methods, such as vector methods, may also be used.

### Morphological Features

Morphological features, such as the surface area, A, and volume, V, of a region identified in an image may be determined based on voxel representations of that volume. Mesh based representations of the outer surface of such a volume may also be used to determine the surface area and volume of the region, for example a marching cubes algorithm may be used.

One morphological feature which may be used is the degree to which a region is spherical. One measure of this feature is sphericity, which may be defined by Fmorph.sphericity

\(F_{{morph}.{sphericity}} = \frac{\left( {36\pi V^{2}} \right)^{1/3}}{A}\)

wherein V is the volume of the image region concerned, and A is its surface area. Other measures include:


- - compactness, which may be based on

\(F_{{{morph}.{comp}}\text{.1}} = \frac{V}{\pi^{1/2}A^{3/2}}\)

(so called compactness 1), or

\(F_{{{morph}.{comp}}\text{.2}} = {36\pi\frac{V^{2}}{A^{3}}}\)

(so called compactness 2)


- - asphericity, which may be based on the ratio A³/V² and spherical
    disproportion, which may be based on the ratio A/V^(2/3).

### Grey Level Size Zone Matrix Features

The grey level size zone matrix (GLSZM) counts the number of groups (or zones) of linked voxels. Voxels are linked if the neighbouring voxel has an identical discretised grey level. Whether a voxel classifies as a neighbour depends on its connectedness. In a 3D approach to texture analysis all of the 26 neighbouring voxels in a 3D rectilinear grid are considered. In the 2D the neighbouring 8 voxels in the same 2D image are considered.

Let  be the Ng×Nz grey level size zone matrix, where Ng is the number of discretised grey levels present in the ROI intensity mask and Nz the maximum zone size of any group of linked voxels. Element sij of M is then the number of zones with discretised grey level i and size j. Furthermore, let Nv be the number of voxels in the intensity mask and

Ns=Σi=1NNj=1Nsij

be the total number of zones. Marginal sums can likewise be defined. The number of zones with discretised grey level i, regardless of size is si.

si.=Σj=1Nsij

Likewise, the number of zones with size j, regardless of grey level is s·j

s.j=Σi=1Nsij

A grey level non-uniformity measure can then be defined which assesses the distribution of zone counts over the grey values. The feature value is low when zone counts are equally distributed along grey levels. One example of a grey level size zone matrix based grey level non-uniformity measure, denoted Fszm.glnu, comprises:

\(F_{{szm}.{glnu}} = {\frac{1}{N_{s}}{\sum\limits_{i = 1}^{N_{g}}s_{i.}^{j}}}\)

The controller may be configured to determine an image metric which gives emphasis to the prevalence of large zones. One example of such a measure, which may be based on the grey level size zone matrix and indicate the presence of large zones, is the large zone emphasis of the grey level size zone matrix. This may be denoted Fszm.lze and comprises:

\(F_{{szm}.{lze}} = {\frac{1}{N_{s}}{\sum\limits_{j = 1}^{N_{z}}{j^{2}s_{.j}}}}\)

The controller may be configured to determine an image metric indicating the variance in zone counts over the different zone sizes (the GLSZM variance)

\(F_{{szm}.{zs}.{var}} = {\sum\limits_{i = 1}^{N_{g}}{\sum\limits_{j = 1}^{N_{z}}{\left( {j - \mu} \right)^{2}p_{ij}}}}\)

In which pij=sij/Ns and μ=Σi=1NΣj=1Njpij

### Grey Level Co-Occurrence Matrix (GLCM) Features

The grey level co-occurrence matrix (GLCM) is a matrix that expresses how combinations of discretised intensities (grey levels) of neighbouring pixels, or voxels in a 3D volume, are distributed along one of the image directions. Generally, the neighbourhood for GLCM is a 26-connected neighbourhood in 3D and a 8-connected neighbourhood in 2D. Thus, in 3D there are 13 unique direction vectors within the neighbourhood for Chebyshev distance δ=1, i.e. (0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 1, 1), (0, 1, −1), (1, 0, 1), (1, 0, −1), (1, 1, 0), (1, −1, 0), (1, 1, 1), (1, 1, −1), (1, −1, 1) and (1, −1, −1), whereas in 2D the direction vectors are (1, 0, 0), (1, 1, 0), (0, 1, 0) and (−1, 1, 0).

A GLCM is calculated for each direction vector, as follows. m is the Ng×Ng grey level co-occurrence matrix, with Ng the number of discretised grey levels present in the region of interest (ROI) intensity mask, and m the particular direction vector.

Element (i, j) of the GLCM contains the frequency at which combinations of discretised grey levels i and j occur in neighbouring voxels along direction m+=m and along direction m−=−m. Then, m=m++m−=m++Tm+. As a consequence the GLCM matrix Mm is symmetric.

A probability distribution for grey level co-occurrences, m, is obtainable by normalising m by the sum of its elements. Each element pij of m is then the joint probability of grey levels i and j occurring in neighbouring voxels along direction m.

The row marginal probability pi is

pi.=Σj=1Npij

and the column marginal probability is

p.j=Σi=1Npij

as m is by definition symmetric, pi.=p.j.

Measures of correlation of the grey level co-occurrence matrix GLCM can be defined such as

\(F_{{cm}.{corr}} = {\frac{1}{\sigma_{i.}\sigma_{.j}}\left( {{{- \mu_{i.}}\mu_{.j}} + {\sum\limits_{i = 1}^{N_{g}}{\sum\limits_{j = 1}^{N_{s}}{ijp}_{ij}}}} \right)}\)

in which μi. and σi. are the mean and standard deviation of row marginal probability pi., respectively. Likewise, μ.j and σ.j are the mean and standard deviation of the column marginal probability p.j, respectively. An informational measure of correlation of the grey level co-occurrence matrix GLCM, Fcm.info.corr.2:

\(F_{{{cm}.{info}.{corr}}\text{.2}} = \sqrt{1 - {\exp\left( {{- 2}\left( {{HXY}_{2} - {HXY}} \right)} \right)}}\)
\({wherein},\)
\({{HXY} = {- {\sum_{i = 1}^{N_{g}}{\sum_{j = 1}^{N_{g}}{p_{ij}\log_{2}p_{ij}}}}}},\)
\({HXY}_{2} = {- {\sum\limits_{i = 1}^{N_{g}}{\sum\limits_{i = 1}^{N_{s}}{p_{i.}p_{.j}{\log_{2}\left( {p_{i.}p_{.j}} \right)}}}}}\)

pij is the joint probability of grey levels i and j occurring in neighbouring voxels along a direction in which the GLCM is defined;

pi. is the row marginal probability of the GLCM, and

p.j is the column marginal probability of the GLCM.

Other measures of correlation of the GLCM may be used.

The controller may be configured to determine the above and other measures of correlation. In addition, the controller may be configured to determine an auto correlation of the GLCM based on:

\(F_{{cm}.{auto}.{corr}} = {\sum\limits_{i = 1}^{N_{g}}{\sum\limits_{j = 1}^{N_{g}}{ijp}_{ij}}}\)

The GLCM difference variance may be computed as the difference variance for the diagonal probabilities thus:

\(F_{{cm}.{diff}.{var}} = {\sum\limits_{k = 0}^{N_{g} - 1}{\left( {k - \mu} \right)^{2}p_{i - {j.k}}}}\)

The sum average for the GLCM is:

\(F_{{cm}.{sum}.{avg}} = {\sum\limits_{k = 2}^{2N_{g}}{kp}_{i + {j.k}}}\)

The sum variance for the GLCM is defined as:

\(F_{{cm}.{sum}.{var}} = {\sum\limits_{k = 2}^{2N_{g}}{\left( {k - \mu} \right)^{2}p_{i + {j.k}}}}\)

Where μ is equal to the value of the sum average for the GLCM.

The controller may be configured to determine an entropy measure of the GLCM, such as a sum entropy:

\(F_{{cm}.{sum}.{entr}} = {- {\sum\limits_{k = 2}^{2N_{g}}{{p_{i}}_{+ {j.k}}\log_{2}p_{i + {j.k}}}}}\)

It can thus be seen that a variety of metrics of image texture may be obtained from the GLCM. Another example is the inverse variance:

\(F_{{cm}.{inv}.{var}} = {2{\sum\limits_{i = 1}^{N_{g}}{\sum\limits_{j > 1}^{N_{g}}\frac{p_{ij}}{\left( {i - j} \right)^{2}}}}}\)

The controller may also be configured to determine other measures derived from the GLCM—such as cluster based measures of texture. One such measure is the cluster tendency

\(F_{{cm}.{clust}.{tend}} = {\sum\limits_{i = 1}^{N_{g}}{\sum\limits_{j = 1}^{N_{g}}{\left( {i + j - \mu_{i.} - {\mu._{j}}} \right)^{2}p_{ij}}}}\)

in which μi is the mean row marginal probability, and μ.j is the mean column marginal probability. As noted above, these parameters may be computed as

μi.=Σi=1Ni pi. and μ.j=Σj=1Nj p.j

Another such cluster based measure is the so called GLCM cluster shade, which may be computed as

\(F_{{cm}.{clust}.{shade}} = {\sum\limits_{i = 1}^{N_{g}}{\sum\limits_{j = 1}^{N_{g}}{\left( {i + j - \mu_{i.} - \mu_{.j}} \right)^{3}p_{ij}}}}\)

Another such cluster based measure is the so called GLCM cluster prominence, which may be computed as

\(F_{{cm}.{clust}.{prom}} = {\sum\limits_{i = 1}^{N_{g}}{\sum\limits_{j = 1}^{N_{g}}{\left( {i + j - \mu_{i.} - \mu_{.j}} \right)^{4}p_{ij}}}}\)

### Neighbourhood Grey Tone Difference Based Features

The controller may also be configured to determine neighbourhood grey tone difference matrix (NGTDM). This contains the sum of grey level differences of pixels/voxels with discretised grey level i and the average discretised grey level of neighbouring pixels/voxels within a Chebyshev distance δ.

The average grey level within a neighbourhood centred at (kx, ky, kz), but excluding (kx, ky, kz) itself is:

\({\overset{\_}{X}}_{k} = {\frac{1}{W}{\sum\limits_{{m_{x}m} - \delta}^{\delta}{\sum\limits_{{m_{y}m} - \delta}^{\delta}{\sum\limits_{{m_{x}m} - \delta}^{\delta}{X_{d}\left( {{k_{x} + m_{x}},{k_{y} + m_{y}},{k_{z} + m_{z}}} \right)}}}}}\)
\(\left( {m_{x},m_{y},m_{z}} \right) \neq \left( {0,0,0} \right)\)

where Xd,k is the discretised grey level of a voxel at position kx, ky, kz), for a 3D neighbourhood W=(2δ+1)3−1 is the size of the neighbourhood. For a 2D neighbourhood W=(2δ+1)2−1, and averages are not calculated between different slices.

Neighbourhood grey tone difference si for discretised grey level i is:

\(s_{i} = {\sum\limits_{i = 1}^{N_{v}}{{❘{i - {\overset{\_}{X}}_{k}}❘}\left\lbrack {{X_{d}(k)} = {{i{and}W_{k}} \neq 0}} \right\rbrack}}\)

where, Wk is neighbourhood size for the voxel (kx, ky, kz) and Nv is equal to the number of voxels in the neighbourhood that are part of the ROI mask

\(W_{k} = {\sum\limits_{m,{m - \delta}}^{\delta}{\sum\limits_{{m_{8}m} - \delta}^{\delta}{\sum\limits_{m,{m - \delta}}^{\delta}\left\lceil {m \neq {{0{and}k} + {m{in}{ROI}}}} \right\rceil}}}\)

where [ . . . ] is an Iverson bracket, which is 1 if the conditions within it are true and zero otherwise.

In NGTDM grey level probabilities pi are defined, thus pi=ni/Nv,c. Nv,c is total number of voxels that have at least one neighbour. If all voxels have at least one neighbour Nv,c=Nv

The controller may be configured to determine a texture strength based on the NGTDM. One example of such a texture strength comprises:

\({F_{{ngi} \cdot {strength}} = \frac{{\sum}_{i_{1} = 1}^{N_{g}}{\sum}_{i_{2} = 1}^{N_{g}}\left( {p_{i_{1}} + p_{i_{2}}} \right)\left( {i_{1} - i_{2}} \right)^{2}}{{\sum}_{i = 1}^{N_{g}}s_{i}}},\)
\(p_{i_{1}} \neq {0{and}p_{i_{2}}} \neq 0\)

Where Ng is the number of discretised grey levels in the ROI intensity mask.

The controller may be configured to determine a contrast based on the NGTDM, which may be based on depends on the dynamic range of the grey levels and the spatial frequency of intensity changes in said grey levels. One example of such a contrast comprises:

\(F_{{ngt} \cdot {contrast}} = \left( {\frac{1}{N_{g,p}\left( {N_{g,p} - 1} \right)}{\sum\limits_{i_{1} = 1}^{N_{g}}{\sum\limits_{i_{2} = 1}^{N_{g}}{p_{i_{1}}{p_{i_{2}}\left( {i_{1} - i_{2}} \right)}^{2}}}}} \right)\)
\(\left( {\frac{1}{N_{v,c}}{\sum\limits_{i = 1}^{N_{g}}s_{i}}} \right)\)

Grey level probabilities pi1 and pi2 are copies of pi with different iterators, i.e. pi1=pi2 for i1=i2. The first term considers the grey level dynamic range, whereas the second term is a measure for intensity changes within the volume. If Ng,p=1, Fngt.contrast=0.

The controller may also be configured to determine a measure of busyness, for example based on the prevalence of large changes in grey levels between neighbouring voxels. One such metric may be defined

\({F_{{ngt} \cdot {busyness}} = \frac{{\sum}_{i = 1}^{N_{g}}p_{i}s_{i}}{{\sum}_{i_{1} = 1}^{N_{g}}{\sum}_{i_{2} = 1}^{N_{g}}{❘{{i_{1}p_{i_{1}}} - {i_{2}p_{i_{2}}}}❘}}},\)
\(p_{i_{1}} \neq {0{and}p_{i_{2}}} \neq 0\)

The controller may also be configured to determine a measure of complexity such as an image metric indicating the prevalence of complex textures in which rapid changes in grey levels are common. One example of such a metric is texture complexity, or NGTDM complexity, which may be defined:

\({F_{{ntg} \cdot {complexity}} = {\frac{1}{N_{v,c}}{\sum\limits_{i_{1} = 1}^{N_{g}}{\sum\limits_{i_{2} = 1}^{N_{g}}{{❘{i_{1} - i_{2}}❘}\frac{{p_{i_{1}}s_{i_{1}}} + {p_{i_{2}}s_{i_{2}}}}{p_{i_{1}} + p_{i_{2}}}}}}}},\)
\(p_{i_{1}} \neq {0{and}p_{i_{2}}} \neq 0\)

The controller may be configured to provide a metric of coarseness based on the fact that grey level differences in coarse textures are generally small due to large-scale patterns. Such measures may be determined by summing differences to give an indication of the level of the spatial rate of change in intensity (coarseness). One measure of NGTDM coarseness may be defined as:

\(F_{{ngt} \cdot {coarseness}} = \frac{1}{\sum_{i = 1}^{N_{g}}{p_{i}s_{i}}}\)

Where Ng, si and pi are defined as above.

### Grey Level Run Length Matrix (GLRLM) Features

Another way to define texture features is to use the grey level run length matrix (GLRLM). A run length is defined as the length of a consecutive sequence of pixels or voxels with the same grey level along direction m. The GLRLM then contains the occurrences of runs with length j for a discretised grey level i.

m is an Ng×Nr grey level run length matrix, where Ng is the number of discretised grey levels present in the ROI intensity mask and Nr is the maximum possible run length along direction m. Matrix element rij of the GLRLM is the occurrence of grey level i with run length j. If Nv is the total number of voxels in the ROI, and Ns is the sum over all elements in m

In the context of GLRLM measures, ri. is the marginal sum of the runs over run lengths j for grey value i.

ri.=Σj=1Nrij.

Similarly, in GLRLM measures r.j is the marginal sum of the runs over the grey values i for run length j.

r.j=Σi=1Nrij.

The controller may be configured to determine grey level non-uniformity, e.g. based on ri. the marginal sum of the runs over run lengths j for grey value i, viz.

\(F_{{rlm} \cdot {glnu}} = {\frac{1}{N_{s}}{\sum\limits_{i = 1}^{N_{g}}r_{i}^{2}}}\)

where Ns is the sum over all elements in m in the GLRLM.

The controller may also be configured to determine run length non-uniformity based on r.j the marginal sum of the runs over the grey values i for run length j. For example, this may comprise an image metric whose value is low when runs are equally distributed along run lengths, e.g.

\(F_{{rlm} \cdot {rlnu}} = {\frac{1}{N_{s}}{\sum\limits_{j = 1}^{N_{g}}r_{j}^{2}}}\)

The controller may also be configured to determine measures of run percentage such as the fraction of the number of realised runs and the maximum number of potential runs. Strongly linear or highly uniform ROI volumes may produce low run percentages. One example of run percentage may be defined:

\(F_{{rlm} \cdot r \cdot {perc}} = {\frac{N_{s}}{N_{v}}.}\)

Any feature of any one of the examples disclosed herein may be combined with any selected features of any of the other examples described herein. For example, features of methods may be implemented in suitably configured hardware, and the configuration of the specific hardware described herein may be employed in methods implemented using other hardware.

### Fractal Dimension Features

A fractal dimension of a region may be based on a statistical index of complexity comparing how detail in a pattern, such as the boundary of an image region changes with the scale at which it is measured. It may also be based on the space-filling capacity of such a pattern. Fractal dimensions considers the space filling properties of the images, and may be defined based on methods such as those defined in “A multifractal approach to space-filling recovery for PET quantification.” Med Phys. 2014 November; 41(11):112505. doi: 10.1118/1.4898122. Willaime J M, Aboagye E O, Tsoumpas C, Turkheimer F E.

### Spatial Filtering

In addition to the image metrics defined above, the controller may also be configured to apply filters such as high pass and/or low pass filters to the image data (e.g. prior to calculation of the image metrics). These filters may be wavelet based. It will be appreciated in the context of the present disclosure that three-dimensional wavelets can be constructed as separable products of 1-D wavelets by successively applying a 1-D analyzing wavelet in three spatial directions (x, y, z). The volume F (x, y, z) is firstly filtered along the x-dimension, resulting in a low-pass image L(x, y, z) and a high-pass image H(x, y, z). Both L and H are then filtered along the y-dimension, resulting in four decomposed sub-volumes: LL, LH, HL and HH. Then each of these four subvolumes are filtered along the z-dimension, resulting in eight sub-volumes: LLL, LLH, LHL, LHH, HLL, HLH, HHL and HHH.

In 1D dimension, the continuous wavelet transform is defined as the convolution of x(t) with a wavelet function, W(t), shifted in time by a translation parameter b and a dilation parameter a:

\({X_{W}\left( {a,b} \right)} = {\frac{1}{\sqrt{a}}{\int\limits_{- \infty}^{+ \infty}{W\frac{t - b}{a}{x(t)}{dt}}}}\)

The discrete form of the wavelet transform is based upon the discretization of parameters (a, b) on the time-scale plane corresponding to a discrete set of continuous basis functions. This can be achieved defining:

\({W_{j,k}(t)} = {\frac{1}{\sqrt{a_{j}}}W\frac{\left( {t - b_{k}} \right)}{a_{j}}}\)

For aj=a0j and bk=kb0 a0j where j, k∈Z, a0>1, b0≠0 where j controls the dilation and k controls the translation. Two popular choices for the discrete wavelet parameters a0 and b0 are 2 and 1 respectively, a configuration that is known as the dyadic grid arrangement resulting in:

\({W_{j,k}(t)} = {{a_{0}^{- \frac{j}{2}}{W\left( {{a_{0}^{- j}t} - {kb_{0}}} \right)}} = {2^{- \frac{j}{2}}{W\left( {{2^{- j}t} - k} \right)}}}\)

Wavelet analysis is simply the process of decomposing a signal into shifted and scaled versions of a mother (initial) wavelet. An important property of wavelet analysis is perfect reconstruction, which is the process of reassembling a decomposed signal or image into its original form without loss of information. For decomposition and reconstruction the scaling function Φjk(t) and the wavelet Wjk(t) are used in the form:

\({\Phi_{jk}(t)} = {2^{- \frac{j}{2}}{\Phi_{0}\left( {{2^{- j}t} - k} \right)}}\)
\({W_{jk}(t)} = {2^{- \frac{j}{2}}{\Psi_{0}\left( {{2^{- j}t} - k} \right)}}\)

where m stands for dilation or compression and k is the translation index. Every basis function W is orthogonal to every basis function Φ.

The one-dimensional wavelet transform of a discrete-time signal x(n) (n=0, 1, . . . , N) is performed by convolving signal x(n) with both a half-band low-pass filter L and high-pass filter H and downsampling by two.

\({c(n)} = {\sum\limits_{n - 0}^{L - 1}{{h_{0}(k)}{x\left( {n - k} \right)}}}\)
\({d(n)} = {\sum\limits_{n - 0}^{L - 1}{{h_{1}(k)}{x\left( {n - k} \right)}}}\)

where c(n) represent the approximation coefficients forn=0, 1, 2 . . . ,N−1 and d(n) are the detail coefficients, h0 and h1, are coefficients of the discrete-time filters L and H respectively where c(n) represent the approximation coefficients for n=0, 1, 2 . . . , N−1 and d(n) are the detail coefficients, h0 and h1, are coefficients of the discrete-time filters L and H respectively.

{h0(n)}n−0L−1=(h0(0),h0(1), . . . ,h0(L−1))

{h1(n)}n−0L−1=(h1(0),h1(1), . . . ,h1(L−1))

resulting in the separable, sub-band process.

It will be appreciated in the context of the present disclosure that whilst wavelet based filters may have particular advantages, other types of spatial filters may be used.

## IMPLEMENTATION

By applying the image processing steps outlined above, the controller is configured first to segment the image data for the subject to identify regions of the image data (anatomical neuroanatomical regions of interest, ROIs). It will be appreciated in the context of a 3D image (such as one made up of a set of slices) that an ROI may comprise a 3D volume, e.g. a cluster of voxels spanning more than one slice of a volumetric image.

For each ROI, the controller determines a selected one or more of the features mentioned above, e.g.


- - First order statistics such as measures of central tendency,
    measures of spread, skewness and kurtosis;
  - Morphological features;
  - Grey Level Size Zone Matrix features;
  - Grey Level Co-occurrence Matrix (GLCM) features;
  - Neighbourhood grey tone difference based features;
  - Grey Level Run Length Matrix (GLRLM) features; and
  - Fractal dimension features.

The controller may store a list of weightings which define the weighting to be given to that feature (image metric) in combining the feature score from each region to provide an indicator. Two examples of such lists of weights have been defined for predicting or diagnosing cognitive impairment in human subjects. The first of these is defined in Table 1, below. The second is defined in Table 2. These two lists have been found to have excellent prediction accuracy, but prediction accuracy which is sufficient to make reliable diagnosis may be provided by other embodiments such as those described and claimed elsewhere herein.

It may be advantageous to age normalise image data before applying the feature analysis defined in Table 1.

The controller may apply either (a) the combination of weightings listed in Table 1, or (b) the combination of weightings listed in Table 2 to scale each feature's value in the corresponding ROI before combining the scaled feature values (e.g. by summing them) to provide the indicator. The controller then compares this indicator value with reference data thereby to determine a cognitive impairment diagnosis for the indicator.

The reference data may be predetermined using the same set of regions, features, and weights as is used to determine the indicator, but based on image data from subjects having a known cognitive impairment diagnosis. The reference data may thus comprise reference value (or range of values) associated with each population on image data from subjects having a known cognitive impairment diagnosis (e.g. control (no impairment), MCI, AD, etc.). The reference data may also be correlated with cognitive testing scores, which may enable a cognitive testing score to be estimated or predicted based on the image data.

The indicators defined by the combinations of regions, features and weights defined in Table 1 are listed in Table 3. The rows shown in Table 3 indicate the outcome of an ROC analysis.

In Table 3 the first of the two columns under the heading APV1 (CNvsAD) indicates the application to a trial population of Alzheimer's disease (AD) subjects and control subjects (CN), and the accuracy of the method defined in table 1 in discriminating AD from CN. The second of the two columns under the heading APV1 (CNvsMCI) indicates the application to a trial population of mild cognitive impairment (MCI) subjects and control subjects (CN), and the accuracy of the method defined in Table 1 in discriminating MCI from CN. The columns under the heading Vol Hippocampus indicate the accuracy of discrimination based on the so-called “gold standard” measure provided using the volume of the hippocampus. Compared to the gold standard, our method shows higher AUC, specificity, sensitivity, accuracy, negative and positive predictive values, likelihood ratios and diagnostic odds ratios in both the discriminations between CN/MCI and CN/AD. Table 4 provides the same ROC analysis for indicators defined by the combinations of regions, features and weights defined in Table 2.

Table 5 shows the same ROC analysis for indicators defined by the combinations of regions, features and weights defined in Table 1 to a different cohort. Table 6 shows the same ROC analysis for indicators defined by the combinations of regions, features and weights defined in Table 2 to a different cohort. The data used to establish tables 5 and 6 provided by OASIS, namely OASIS-3: Principal Investigators: T. Benzinger, D. Marcus, J. Morris; NIH P50AG00561, P30NS09857781, P01AG026276, P01AG003991, R01AG043434, UL1TR000448, R01EB009352. Any AV-45 doses were provided by Avid Radiopharmaceuticals, a wholly owned subsidiary of Eli Lilly.

It will be appreciated in the context of the present disclosure that the weights listed herein need not be given the accuracy quoted here. It is believed that weightings which provide comparable relative contributions of at least two of the more heavily weighted contributions may provide reliable prediction/diagnosis.

It can be seen that in all cases, and in both cohorts of subjects, the ability of the method described herein to distinguish control subjects from those with MCI or AD matches or exceeds measurements based on the volume of the hippocampus.

### The Use of Reduced Feature Sets

It is believed that the weightings having the highest absolute values may contribute most strongly to the predictive power of the indicators defined by the lists of tuples defined in Table 1 and Table 2. Therefore not all of the features and regions need be used in order to predict cognitive impairment. Particularly advantageous combinations of features and regions include those described and claimed elsewhere herein.

To determine the extent to which reduced feature sets may be useful in predicting cognitive impairment two comparative studies were conducted. In the first comparative study the predictive power of the full feature sets listed above in Table 1 was compared with the predictive power of incomplete versions of that same set. In summary—it was determined that the proposal set out in the preceding paragraph is correct, and that methods of predicting or diagnosing cognitive impairment based only on the more strongly weighted image metrics and image regions provide effective predictive power.

In Tables 7 and 8 listed below the tuples of feature and region listed in Tables 1 and 2 are referred to using row labels. This labelling relates to the image regions and image metrics identified in those rows of Table 1 and Table 2 being used to determine an indicator for comparison with reference data, thereby to predict or diagnose cognitive impairment in the subject in the manner described and claimed herein.

In the first study, the indicated combinations of features from the rows listed in Table 1 were selected, and tested using an ROC analysis. The complete ROC data is shown in FIG. 4, but summarised below using the AUC (area under curve) obtained from the ROC analysis of each feature set.

The performance achieved using only four of the heavily weighted feature-region tuples (Ftest4) is closely comparable with that achieved by using the entire feature set listed in Table 1. Where only three features are used, effective performance is still achieved and the best performance is given by permutation 4 (P4), which involves he Left Hippocampus, Left Amygdala and Right Cerebral Cortex—see rows f, g and j of Table 1.

Where only two of the feature-region tuples were used, the best performance was provided by the permutation labelled P6, which involves Left Cerebral Cortex and Left Amygdala—see rows c and g of Table 1. The worst performance was given by the combination of Left and Right Cerebral Cortex alone, labelled P7. Even this however provided a reasonable degree of class separation, so a measurable predictive effect is present even in this less preferred embodiment.

It can thus be seen that whilst there are some particularly advantageous combinations, selection of any two of the four heavily weighted feature-region tuples listed above provides effective prediction or diagnosis of cognitive impairment. The full table with complete ROC data is set out in FIG. 4.

In the second study, combinations of features from the rows listed in Table 2 were selected and tested using an ROC analysis. The complete ROC data is shown in FIG. 5, but is summarised below using the AUC (area under curve) obtained from the ROC analysis of each feature set.

As with the reduced feature sets explained with reference to Table 7, Table 8 also shows that the performance achieved using only four of the heavily weighted feature-region tuples from Table 2 (Ftest4) is closely comparable with that achieved by using the entire feature set of Table 2.

Where only three features are used, effective performance is still achieved and the best performance is given by permutation 4 (P4), which involves the Left Hippocampus, Left Amygdala and Right Hippocampus—see rows I, J and O of Table 2.

Where only two of the feature-region tuples were used, the best performance was provided by the permutation labelled P9, which involves Left Hippocampus and Right Hippocampus—see rows I and O of Table 2. The performance of all of the reduced sets using only two feature-region tuples of Table 2 provided AUC performance of well above 0.9

It can thus be seen that whilst there are some particularly advantageous combinations, selection of any two of the four heavily weighted feature-region tuples listed above provides very effective prediction or diagnosis of cognitive impairment. The full table with complete ROC data is set out in FIG. 5.

### The Use of Sub-Regions of the Cortex

In addition, or as an alternative to, the use of the image regions outlined above embodiments of the present disclosure comprise methods which identify regions of interest ROIs comprising sub-regions of the cortex (which may be referred to as sub cortical regions). Such methods of predicting or diagnosing cognitive impairment may find particular application in providing a visual guide to the stage of cognitive impairment and/or the progress of disease states such as Alzheimer's disease (AD).

The apparatus which performs these methods may be identical to that outlined above, other than in that it may comprise a display means for providing an overlay of the results of the methods disclosed herein on an image of a subject's brain and/or on a standard brain such as an anatomical atlas.

FIG. 6, FIG. 7 and FIG. 8 illustrate the type of visual output which may be obtained from such methods FIG. 7 relates to the data obtained from mild cognitive impairment (MCI) and alzheimer's patients (AD) in age normalised image data. FIG. 8 relates to the data obtained from mild cognitive impairment (MCI) and alzheimer's patients (AD) in non-age normalised image data. Such visual indications may be determined by calculating the feature/region tuples defined in any one of Tables 9 to 13 below, and displaying the results as an overlay on an anatomical/structural image of the human brain to assist a clinician in diagnosing/stratifying patients.

The controller may also be configured to identify, in image data having appropriate contrast and resolution, certain sub-regions of the cortex. The sub-regions of the cortex may comprise:


- - Banks of the Superior Temporal Sulcus
  - Caudal Middlefrontal
  - Entorhinal
  - Frontal pole
  - Fusiform
  - Inferior parietal
  - Inferior temporal
  - Insula
  - Isthmus cingulate
  - Lateral Occipital
  - Lateral Orbitofrontal
  - lingual
  - Middle temporal
  - Parahippocampal
  - Pars Orbitalis
  - Pars Triangularis
  - Pericalcarine
  - Precentral
  - Precuneus
  - Rostral anterior cingulate
  - Rostral middlefrontal
  - Superior parietal
  - Superior temporal
  - Supramarginal
  - Temporal pole
  - Transverse Temporal

In the embodiments in which these sub regions of the cortex are used, the controller is able to identify both the left and right brain locations of these regions. The image metrics employed in each of these regions may comprise any one or more of those outlined above. The image data may be age normalised as described above.

In particular embodiments, the controller is configured to identify: the left entorhinal, left fusiform and the right temporal pole, and the transverse temporal pole. In each of these regions the controller then determines one or more of the following image metrics:


- - a metric of image texture;
  - a metric of image intensity; and
  - a morphological metric of the image region.

Different implementations can be used—and some of the metrics which have been found to be of particularly strong predictive power are outlined in Table 9, Table 10, Table 11, and Table 12, below. It can be seen from these different tables of data that, in addition to the consistent usefulness of these four regions, the insula was also found to play a significant part in some approaches.

Table 9, below, sets out one set of tuples of sub-cortical regions, and the image metrics for each region. These have been applied to age normalised data and found to have a particularly strong predictive effect. The weightings listed can be used to combine the image metrics from the identified regions, for example in a linear sum. Other predetermined methods may also be used. The resultant indicator may be used in the prediction and/or diagnosis of cognitive impairment as described above.

In addition to the quantitative predictive/diagnostic effectiveness of these methods, it has also been found that overlays of the relevant image metrics on images of the human brain provide a useful marker of the extent of cognitive impairment. Examples of such overlays are illustrated in FIG. 6. The display of visual indicators of the metrics of sub-regions of the cortex as defined herein may therefore provide a useful diagnostic aide, to assist clinicians in making an assessment of cognitive impairment in a subject.

An extract of the ROC analysis of using this approach to distinguish between age normalised images of control subjects and subjects having mild cognitive impairment (MCI) is illustrated in FIG. 9.

It is strongly indicated by the data set out above in Table 7 and Table 8, that when combining image metrics from different regions in this way, the predictive power of the method may remain even when using reduced feature sets. This hypothesis was tested by making comparative assessments of the predictive power of the method defined in Table 9, above. In this comparative test, the predictive power of the full feature set listed in Table 9 was compared against the power of a reduced feature set in which only 5 tuples were selected. The tuples chosen for the comparative test were:


- - 1. a morphological feature of the left entorhinal (e.g. spherical
    distortion)
  - 2. a texture feature of the left fusiform (e.g. GLRLM short run low
    grey level emphasis)
  - 3. an image intensity of the right temporal pole (median intensity)
  - 4. an image intensity of the right transverse temporal cortex—(e.g.
    mean absolute deviation, which may comprise the mean distance of all
    intensity values from the Mean Value of the image array

\({{{Mean}{Abs}{Dev}} = {\frac{1}{N_{P}}{\sum}_{i = 1}^{Np}{❘{{X(i)} - \overset{¯}{X}}❘}}};{and}\)


- - 5. a texture feature of the right insula (e.g. GLRLM short run
    emphasis)

It can be seen from FIG. 9 that the performance of the reduced feature set (labelled F5 in FIG. 9) which uses just five (5) of the 17 tuples listed in Table 9 provides a predictive/diagnostic effect nearly equivalent to that provided by the full feature set. This is consistent with the observations set out above—namely that a reduced feature set using the more strongly weighted feature/region tuples provides effective performance.

It can be seen from an inspection of Table 9, above, that whilst certain texture, intensity, and morphology features have been selected in each of these regions other such features also provide significant contributions to the predictive power of the approach. It is therefore believed that the combination of the particular image regions, and texture/morphology/intensity based image metrics derived from those regions provides the predictive/diagnostic effect of the present disclosure. The precise detail of the metrics themselves is a lesser consideration than the underlying anatomical/physiological effect which they reveal. Other image metrics of texture, morphology and so forth may be used.

A further predictor was derived using control patients and patients with Alzheimer's Disease. The data used to establish this model was age normalised in the manner described above. The feature/region tuples used in this predictor are set out below in Table 10

Significantly, it can be seen that a morphological feature of the entorhinal cortex is again very heavily weighted in this data. In this instance the parameter is the surface to volume ratio, but it will be appreciated in the context of the present disclosure that such parameters are not unrelated to the sphericity of a region, or indeed the spherical disproportion. Embodiments of the present disclosure may thus comprise methods of predicting or diagnosing cognitive impairment based on morphological features of the entorhinal cortex.

Other features which are heavily weighted in Table 10 are also heavily weighted in Table 9. For example the insula, the fusiform, and the temporal pole amongst other regions are heavily weighted in both Table 9 and Table 10.

To test the hypothesis that the most strongly weighted feature/region tuples can provide an effective predictor without use of the full feature set, a set of comparative tests were performed. In these comparative tests, the full 80 tuple feature set defined in Table 10 was compared against the reduced feature sets shown in FIG. 10.

In FIG. 10, Ftot indicates the full 80 tuple feature set. The following feature sets are also defined:


- - F35: 35 features correspondent to the 35 highest weighted features
    per region
  - F18: the 18 highest weighted among the 35
  - F10: the 10 highest weighted among the 18

An ROC analysis was performed to compare the predictive/diagnostic power of the full feature set against the reduced sets. It can be seen that even the 10 tuple feature set, F10, provides an effective predictor with an AUC of 0.73. Again, the entorhinal, temporal pole, and insula provide a significant contribution to the effectiveness of this predictor.

Table 11, below shows the feature/region tuples developed for a non-age normalised data set comprising control patients and patients with mild cognitive impairment (MCI)

It can be seen that this analysis gives rise to 41 feature/region tuples in 17 regions of the brain. A comparative test was performed in which the performance of a predictor based on 17 tuples (the highest weighted feature for each region) was tested against the full feature set and a further reduced feature set was also used in which only the 8 highest weighted tuples from amongst that 17 were used. These are labelled Ftot, F17, and F8 respectively in FIG. 11. It can be seen from the ROC analysis presented in FIG. 11 that both reduced feature sets provide effective predictive/diagnostic power.

It can also be seen from a comparison of the performance of the predictive models defined in Tables 9 and 11 that although age normalisation may have some advantages it is by no means essential. An effective prediction can be made without it. In addition the morphology of the entorhinal cortex again plays a significant role—in this instance the compactness.

Table 12 below shows the feature/region tuples for a predictor developed from a data set comprising control patients and patients with Alzheimer's Disease. The image data was not age normalised.

Table 12 comprises 78 tuples in 34 different sub-regions of the cortex. As with the data listed in Table 11 in the comparative test, the highest weighted tuple in each region was selected an used to provide a reduced feature set, labelled F34 in FIG. 12. A further reduced feature set was also constructed by using the most heavily weighted 14 tuples from amongst these 34, labelled F14 in FIG. 12. Again, it can be seen that the reduced feature sets both provide effective diagnostic/predictive power. Again the entorhinal cortex plays a significant role, although in this predictor the NGTDM contrast, a texture feature of the entorhinal is significant.

The consistent finding of the predictors investigated herein is that it is possible to define texture and morphology based models of certain brain regions which can be used to predict the presence of cognitive impairment and/or Alzheimer's disease. A wide variety of models/predictors are possible. Without wishing to be bound by theory, it is believed that those which take account of at least the texture and/or morphology of the entorhinal cortex, the fusiform gyrus, the temporal pole, and the transverse temporal cortex may be the most effective predictors. The insula may also make a significant contribution.

In further investigation to establish the robustness of the methods described and claimed herein a further dataset was investigated in which the control subjects comprised both healthy controls and subjects with Parkinson's and frontotemporal disease. The other subjects, referred to herein as group ADrp, had prodromal Alzheimer's disease and Alzheimer's disease. Predictors were developed that, in a first stage classification were able to distinguish group ADrp from the control subjects. A further predictor was also developed that is able to distinguish within group ADrp. These two predictors differ from those described above, not only in that the control subjects comprise subjects with Parkinson's and frontotemporal disease, but also in that the predictor uses both cortical regions and sub-regions of the cortex.

FIG. 13, and Table 13 below set out a predictor to distinguish between (a) control subjects comprising both healthy controls and subjects with Parkinson's and frontotemporal disease, and (b) a group ADrp having both prodromal Alzheimer's disease and Alzheimer's disease.

This predictor based on the above features and weights set out in Table 13 was found to provide an AUC of 0.986 in an ROC analysis, and a specificity of 0.9831. It is thus shown to have very reliable predictive power and specificity—even where the control group comprise subjects having other cognitive impairments. A comparative test was performed to demonstrate the possibility to employ reduced feature sets and to demonstrate that the predictive power is preserved when selected ones of the image regions and image metrics are used in the predictor and other are disregarded. As illustrated in FIG. 13, a reduced feature set was constructed using at least two regions selected from the following four:


- - Right Middle Temporal
  - Right Rostral Middle Frontal
  - Right Supramarginal
  - Right Temporal Pole

It was found that all of the predictors generated using these regions reliably distinguished the group ARDP subjects from the control group—even where the control subjects comprised both healthy controls and subjects with Parkinson's and frontotemporal disease. The use of spatial filters such as those indicated in column 13 of table 13 is optional.

It can be seen that when reduced to three image region-feature tuples, the best performance was given by the predictor labelled permutation 2 (Ftest3-p2) in FIG. 13. This involves Right Middle Temporal, Right Rostral Middle Frontal and Right Temporal Pole. When reduced to 2 Features, best performance given by permutation 7 (Ftest2-p7), which involves Right Middle Temporal and Right Temporal Pole.

In the Right Middle Temporal, this embodiment may employ a measure of complexity such as fractal dimension (e.g. minimum fractal dimension). In the right temporal pole a measure of central tendency of pixel intensity may be used, such as the mean intensity.

FIG. 14, and Table 14 below set out the results obtained from this approach when the predictor is developed to distinguish between patients having prodromal Alzheimer's disease and those having Alzheimer's disease

This predictor based on the above features and weights set out in Table 14 was found to provide an AUC of 0.8121 in an ROC analysis, and a specificity of 0.65. It is thus shown to have reasonable predictive power and specificity—even where distinguishing between different Alzheimer's disease states. A comparative test was performed to demonstrate the possibility to employ reduced feature sets and to demonstrate that the predictive power is preserved when selected ones of the image regions and image metrics are used in the predictor and other are disregarded. As illustrated in FIG. 14, a reduced feature set was constructed using at least two regions selected from the following four:


- - Left choroid Plexus
  - Right Inferior Lateral Ventricle
  - Right Cerebellar cortex
  - Right Hippocampus

Surprisingly in this predictor higher accuracy may be achieved by the reduced feature sets. When reduced to these 4 regions & features, the accuracy of the classification goes to 0.72 (compared to 0.68 given by the complete set of features & regions). When reduced to 3 Features, best performance is given by permutation 4 (labelled Ftest3-p4 in FIG. 14), which involves Left choroid Plexus, Right Cerebellar cortex and the Right Hippocampus.

When reduced to 2 Features, the higher accuracy is obtained with permutation 7 (Ftest2-p7), which involves Left choroid Plexus and Right Hippocampus. The feature used in the left choroid plexus may comprise a measure of intensity such as the minimum intensity. The feature used in the right hippocampus may comprise a morphological measure, such as the shape to volume ratio. This permutation gives the highest accuracy.

Embodiments of the disclosure may employ these methods sequentially—in a first classification step, a predictor such as any one of those described above with reference to FIG. 13 and/or Table 13 may be used to diagnose or to predict a cognitive impairment state corresponding to Alzheimer's disease. Then, in the event that this first method step does indicate a cognitive impairment state corresponding to Alzheimer's disease, a predictor such as any one of those described above with reference to FIG. 14 and/or Table 14 may be applied to diagnose or to distinguish between Alzheimer's disease and prodromal Alzheimer's disease in the patient. It will be appreciated in the context of the present disclosure that the prodromal stage of Alzheimer's disease may also referred to as mild cognitive impairment (MCI) due to Alzheimer's disease, and this is the stage where there are obvious symptoms of brain dysfunction. Accordingly, in the present disclosure MCI may comprise the prodromal stage of Alzheimer's disease.

These and other methods of the disclosure may be used to stratify patients for clinical trials and/or to assess the effectiveness of treatments or therapies applied to said patients. It will be appreciated in the context of the present disclosure that whilst particular metrics of image structure in the image regions identified herein have been found to have particular differentiating power, other metrics—e.g. such as metrics of structure, shape, complexity and texture may also be used.

The reference data store used to store data against which test values are compared may comprise volatile and/or non-volatile data storage for storing the above described reference data. The reference data may comprise data calculated by applying the image metrics described herein to a set of reference images of the human brain (a training data set). This training data set may comprise a large number of images of different subjects for which the cognitive impairment diagnosis of each subject is known—e.g. having been verified by other means.

It will be appreciated from the discussion above that the embodiments shown in the Figures are merely exemplary, and include features which may be generalised, removed or replaced as described herein and as set out in the claims. With reference to the drawings in general, it will be appreciated that schematic functional block diagrams are used to indicate functionality of systems and apparatus described herein. It will be appreciated however that the functionality need not be divided in this way, and should not be taken to imply any particular structure of hardware other than that described and claimed below. The function of one or more of the elements shown in the drawings may be further subdivided, and/or distributed throughout apparatus of the disclosure. In some embodiments the function of one or more elements shown in the drawings may be integrated into a single functional unit.

In some examples the functionality of the controller may be provided by a general purpose processor, which may be configured to perform a method according to any one of those described herein. In some examples the controller may comprise digital logic, such as field programmable gate arrays, FPGA, application specific integrated circuits, ASIC, a digital signal processor, DSP, or by any other appropriate hardware. In some examples, one or more memory elements can store data and/or program instructions used to implement the operations described herein. Embodiments of the disclosure provide tangible, non-transitory storage media comprising program instructions operable to program a processor to perform any one or more of the methods described and/or claimed herein and/or to provide data processing apparatus as described and/or claimed herein. The controller may comprise an analogue control circuit which provides at least a part of this control functionality. An embodiment provides an analogue control circuit configured to perform any one or more of the methods described herein.

The embodiments described herein need not perform any diagnosis in order to provide a technical advantage. In particular, there is no need for any comparison with standard data because patients can simply be stratified according to the indicators obtained from the combinations of features (image metrics), image regions, and weights described herein. Such indicators may be used to stratify subjects, for example to identify cohorts for clinical trials Accordingly, methods of the present disclosure comprise computer implemented methods of processing images, such as T1 weighted MRI images to determine any one or more of the indicators based on image regions and image metrics described herein. Such methods may further comprise conducting clinical trials and/or processing clinical measurement data obtained from the subjects to investigate the efficacy of therapies, such as drug treatments. It will thus be appreciated that the methods and apparatus described herein offer a new method of physiological measurement.

The above embodiments are to be understood as illustrative examples. Further embodiments are envisaged. It is to be understood that any feature described in relation to any one embodiment may be used alone, or in combination with other features described, and may also be used in combination with one or more features of any other of the embodiments, or any combination of any other of the embodiments. Furthermore, equivalents and modifications not described above may also be employed without departing from the scope of the invention, which is defined in the accompanying claims.

