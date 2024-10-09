# DESCRIPTION

## TECHNICAL FIELD

The present invention relates generally to image intensity standardization. More specifically, the invention relates to methods and apparatuses for pre-processing and isolating specific components of a medical image for more efficient intensity standardization.

## BACKGROUND

Magnetic resonance images (MRI) acquired with similar protocols but on different scanners will show dissimilar intensity contrasts for the same tissue types. These variations are machine-dependant, and go beyond random or systematic errors that can be corrected with image de-noising that are known in the art or bias field heterogeneity estimation. This situation is particularly acute in large, multi-centric settings such as the Alzheimer's Disease Neuroimaging Initiative (ADNI), in which data was acquired from 56 different centers in the United States and Canada. The ADNI was launched in 2003 by the National Institute on Aging, the National Institute of Biomedical Imaging and Bioengineering, the Food and Drug Administration, private pharmaceutical companies and non-profit organizations, as a $60-million, 5-year public-private partnership. It collected data on more than 800 subjects for Alzheimer's neuroimaging research.

Automated image-processing pipelines must be robust to these variations, if they are to provide reliable and reproducible measurements that have clinical meaning. Thus, intensity standardization must be performed so that similar intensities will have similar tissue meaning in the standardized images, regardless of scanner origin, location, type or operator. Techniques exist to perform standardization, but they are essentially aimed at matching the image histogram (i.e. from the image to be standardized) onto a standard or reference image histogram In particular, the technique of Nyul et al. [Nyul, L. G., J. K. Udupa, and X. Zhang, New variants of a method of MRI scale standardization. IEEE Trans Med Imaging, 2000. 19(2): p. 143-50.] matches percentile histogram landmarks (PCT), linearly interpolating intensities between them. Applicant's experience dictated that histogram matching should not be considered the unique objective, as it may artificially distort image contrasts and therefore result in a loss of biological meaning, quite exactly the opposite effect sought after. In some cases, two different tissue types can have a similar intensity profiles and therefore provide inefficient intensity adjustment and/or intensity adjustments that are not adapted to the specific tissue type. Indeed, intensity values alone do not inherently carry information about the tissue being observed. Rather, standardization should be aimed at matching spatially corresponding tissue intensities to remove, as much as possible, scanner effects. FIG. 1 shows a flowchart of a prior art methods for standardization.

One of the drawbacks of the prior art methods is that, in some cases, two different tissue types can have a similar intensity profiles (for example CSF and background), and therefore provide inefficient intensity adjustment and/or intensity adjustments that are not adapted to the specific tissue type.

## SUMMARY

Applicants have discovered that intensity standardization is best achieved by matching spatially corresponding tissue intensities. Applicants present herein a novel automatic technique, called STI, which shares the simplicity and robustness of histogram-matching techniques, but also incorporates tissue spatial intensity information. Applicants compared STI to two histogram-matching techniques qualitatively, by visual inspection, and quantitatively, with four measures, on two multi-centric datasets, namely ADNI and a similar initiative called the European ADNI (E-ADNI). Qualitatively, STI showed better performance. This was reflected quantitatively by only one measure, the diagonal sum of the standard-vs.-input joint-histogram, suggesting that histogram-matching measures and techniques cannot be considered entirely appropriate.

It is therefore an object of the present invention to provide a new method of standardizing the intensity of a medical image to a standard image comprising pre-processing the medical image, registering the medical image to the standard image, applying one or more mask to the test and the standard images for isolating image components, determining the most common intensity data pair between the medical image and the standard image for each isolated image component, calculating a formula that joins the most common intensity data pair of each image component and interpolating an intensity data adjustment using the formula and applying it to the medical image data to generate a standardized version of the medical image.

In some embodiments of the present invention, a minimal and maximal data pair is added to provide a more precise intensity data interpolation in the lower and upper intensity values.

In yet other embodiments, a pre-processing step can comprise scaling, filtering, intensity heterogeneity correction, de-noising, re-sampling, smoothing and an intensity adjustment formula can comprise any one or combination of a linear, polynomial, basis-function (Gaussian, Bessel, Sine, Cosine, etc.) formula.

It is another object of the present invention to provide an apparatus for standardizing a medical image to a standard image comprising a medical image source and a standard image source, an image pre-processor for pre-processing the medical image, an image registrator for registering the medical image to the standard image, a component isolator for isolating specific image components, a data pair frequency selector for selecting the highest frequency intensity data pair, an intensity adjustment calculator for calculating a formula using intensity values of the data pairs and an intensity adjuster for adjusting the intensity data of the medical image

In some embodiments of the apparatus, a visual display is utilized for presenting standardized images and in others, a transmitter is utilized for transmitting the standardized image data to another location or computer.

It is yet another object of the present invention to provide a method of determining a disease risk factor or of performing classification of an image comprising receiving an unstandardized image, standardizing said image according to the present invention and determining a disease risk factor or performing classification using said standardized image.

It is still another object of the present invention to provide a system for automatically calculating a disease risk factor or medical classification based on a medical image comprising a standardization apparatus according to the present invention and a calculator configured to process said standardized image to generate said disease risk factor or medical classification.

## DETAILED DESCRIPTION

Applicant's objective was to design an automated technique that would be simple and robust, while incorporating tissue-specific intensity information. Applicants herein report the development of a novel automated technique for STandardization of Intensities (STI), which makes use of spatial correspondences and available tissue masks from the standard image to adjust the intensity of the input image. STI was compared to one variant of Nyul et al., referred as PCT-10, and its modified form, referred as PCT-1, on two different multi-centric MRI datasets.

FIG. 2 is a flowchart illustrating a method of image intensity standardization according to the present invention. The method comprises receiving a test MRI image, pre-processing image (e.g. filter, scale, de-noise), registering image to standard image, applying tissue-specific masks (e.g. BG, WM, GM, CSF), generating joint-histogram for each tissue type, finding intensity correspondence with standard (joint-histogram maximum) for each tissue type, determining intensity adjustments by interpolating intensity correspondence between tissue types and applying adjustments to input image.

In order to test out the new method on a real dataset, the European ADNI project (E-ADNI) dataset was obtained with permission. It consisted in data from three healthy volunteers, herein referred as Subjects 1 to 3, that acted as human quality control phantoms and that were scanned three times (scan; repeat scan, same session; rescan) within the span of few weeks at seven different European centers, herein referred as Sites 1 to 7, using the ADNI 3D T1-weighted MP-RAGE protocol taught by Jack et al. [Jack, C. R., Jr., et al., The Alzheimer's Disease Neuroimaging Initiative (ADNI): MRI methods. J Magn Reson Imaging, 2008. 27(4): p. 685-91]. In this study applicants used only the rescan data since scan and repeat scan were missing for one subject at one site. FIGS. 8 and 9 show the results obtained for Subject 1 at sites 1 and 2, respectively.

This dataset allowed the applicants to evaluate the performance of standardization techniques by avoiding inter-subject intensity variations and focusing only on inter-scanner differences. Making the reasonable hypothesis that subject tissue properties did not change between sites within the short study timeframe, a well-performing standardization technique should output the same tissue intensities independently of the scanning site.

The second dataset was obtained via ADNI. It consisted in 735 baseline MRIs from controls, mild cognitive impairment and probable Alzheimer's disease subjects, acquired on 56 different 1.5T scanners (GE Medical Systems; Siemens Healthcare; Philips Healthcare) using the aforementioned protocol of Jack et al. Data used in the preparation of this article were obtained from the ADNI database (www.loni.ucla.edu/ADNI). For up-to-date information see www.adni-info.org.

### Pre-Processing

All MRI volumes were pre-processed in a similar fashion using the MINC image processing toolbox2: a) raw scanner intensity inhomogeneity correction; b) noise removal; c) linear scaling of grey level intensities to match the mean level of a target image; d) global registration (12 degrees of freedom) to the standard image space as taught by Collins et al. [Collins, D. L., et al., Automatic 3D Intersubject Registration of MR Volumetric Data in Standardized Talairach Space. Journal of Computer Assisted Tomography, 1994. 18: p. 192-205.], maximizing the mutual information between the two volumes; and e) resampling to a 1-mm3 isotropic grid. The standard image throughout this study was taken from BrainWeb [Aubert-Broche, B., A. C. Evans, and L. Collins, A new improved version of the realistic digital brain phantom. Neuroimage, 2006. 32(1): p. 138-45.] (normal brain, T1 image, 1-mm resolution, 0% noise, 0% non-uniformity). Global non-linear registration to the standard image was also performed [D. L. Collins and A. C. Evans, “ANIMAL: Validation and Applications of Nonlinear Registration Based Segmentation,” International Journal of Pattern Recognition and Artificial Intelligence, vol. 11, pp. 1271-1294, 1997 1997.] Hereafter, the pre-processed images will be referred to as the input images for the standardization techniques.). Intensity clamping can also be used in the pre-processing pipeline and involves setting to zero all intensity values below the percentile value 0.01, setting to 100 all intensity values above the percentile value 99.99, and linearly interpolating intensities between those limits. This step removes outliers of low and high intensities and rescales the image intensity between 0 and 100.

### Intensity Standardization

Global registration established spatial correspondence between standard and input images, allowing applicants to compute a joint intensity histogram of the frequency distribution of intensity correspondences. From the most frequent tissue-specific correspondences, STI computed an intensity mapping function that mapped the input image onto the standard.

Since tissue intensities overlap, it was difficult to estimate tissue-specific correspondences from the global joint histogram. To refine its estimates, STI thus used available BrainWeb tissue masks for the background, white matter and grey matter. For each tissue, STI performed the following steps:


- - 1. Mask both input and standard images, i.e. keep only the voxels
    contained in the tissue mask.
  - 2. From the masked voxels, compute and smooth (with a Gaussian
    low-pass filter for example), the standard-vs.-input joint intensity
    histogram.
  - 3. Find the two-dimensional (2D) position of the maximum in the
    joint histogram. The maximum corresponds to the most frequent
    intensity correspondence (intensity data pair) between the input and
    standard images for the current tissue. The 2D coordinates
    correspond to the intensity values of the input and standard images.
    Applicants supposed that this point corresponds to the
    input-to-standard intensity mapping for the current tissue.

The 2D intensity points obtained for each tissue were used as control points in the mapping function. To this set, STI added two extra points: the first (0,0) mapped both minimum intensities in the input and standard images, and the second (100,100), the maximum values. STI finally completed the mapping function by linearly interpolating intensities between the 2D points.

Applicants compared STI to the histogram-matching technique described in Nyul et al. as L4, which uses percentile landmarks spaced by 10%. Herein, the technique is referred as PCT-10. Applicants also compared STI to a modified version using landmarks spaced by 1% for better histogram matching. This technique is herein referred as PCT-1.

### Comparison Measures

Applicants first visually inspected all standardized images and qualitatively compared the standardization techniques. The problem was then to define a measure that applicants could use to perform a quantitative comparison. Since applicants think that standardization should aim at matching corresponding tissue intensities, applicants needed measures that would evaluate both histogram matching and spatial intensity correspondence. Applicants thus performed a comparison based on the following four measures:


- - 1. Kullback-Leibler divergence (KLD) with respect to standard.
    Applicants used KLD to evaluate histogram matching. It measures the
    difference between the histograms of the standardized and the
    standard images. KLD does not depend on spatial correspondence.
  - 2. Mean absolute error (MAE), with respect to standard, i.e. mean
    absolute intensity difference between the standardized and the
    standard images over the entire image volume. MAE depends on spatial
    correspondence between the standard and the input images.
  - 3. Normalized mutual information with respect to input (NMI) as
    shown in Studholme et al. \[Studholme, C., D. L. G. Hill, and D. J.
    Hawkes, An overlap invariant entropy measure of 3D medical image
    alignment. Pattern Recognition, 1999. 32(1): p. 71-86\]. Although
    NMI does not assess standardization performance, applicants used
    that measure to evaluate how the standardization affects the input
    image. As NMI decreases, information is lost in the standardization
    process.
  - 4. Joint-histogram diagonal sum with respect to standard (JHDS),
    i.e. the sum of the diagonal bins of the joint histogram of standard
    vs. standardized images. Applicants note that the bin size
    corresponded to a 1% intensity variation. The rationale behind this
    proposed measure is that the joint histogram of the standard vs.
    input images should present higher frequencies on its diagonal after
    standardization. Ideally, if the standardization was perfect, the
    joint histogram would be concentrated on the diagonal only, mapping
    each intensity value of the input image to the same value for the
    standard image. JHDS depends on spatial correspondence between the
    standard and the input images.

By visual inspection of the E-ADNI dataset, STI gave overall the best results, followed by PCT-1 and PCT10, on the E-ADNI dataset (a complete set of drawings is publicly available at the following permanent web link: http://medics.crulrg.ulaval.ca/

FIG. 8 shows the standardized images for Subject 1 at site 1 and FIG. 9 shows the standardized images for Subject 1 at site 2 using the three techniques. For the most challenging cases, Sites 6 and 7, STI showed the best performance, while PCT-10 and PCT-1 underestimated the white matter intensity for Site 6 and overestimated it for Site 7. Applicants obtained similar results for Subjects 2 and 3. It will be appreciated that interpretation of these images is facilitated by viewing on a single page and on a color scale. However, for the purposes of this application, all images where transformed to grey scale. The spatial coordinates for all images of FIGS. 8 and 9 are (x,y,z; 0,−18,18).

Table 1 presents the quantitative results of the four measures obtained for the standardizations of FIG. 8. Unsurprisingly, PCT-1 gave the lowest KLD values in all cases, showing that it is the best histogram-matching technique. However, STI gave overall the best results for MAE and JHDS. As for NMI, PCT-1 gave the poorest values.

Qualitatively, STI gave again better results overall for the ADNI dataset, followed by PCT-1 and PCT-10. Applicants provide three image examples for qualitative evaluation at http://medics.crulrg.ulaval.ca/. Focusing on PCT-10 and PCT-1, the white matter intensity was underestimated in (A), while it was overestimated in (B) and (C). Applicants also note that the cerebrospinal fluid (CSF) intensity was overestimated for all three images, especially in (B) and (C). For the three cases, STI gave the best results. In particular, applicants note that the CSF intensity was kept similar to the original image and background of the standard.

Quantitative results obtained for the three examples above followed the same trend as for the whole ADNI dataset. In Table 2, applicants show the mean and standard deviation of KLD, MAE, NMI and JHDS for the whole dataset. PCT-1 gave the best results for KLD and MAE, followed by PCT-10. STI showed better NMI and JHDS, matching applicant's visual, qualitative evaluation. Applicants also performed two-sample t-tests between standardization methods for each measure. Distributions were all significantly different (p-value <0.001), except for one case: between PCT-10 and PCT-1, JHDS distributions were not, with a p-value of 0.439.

According to the KLD measure, PCT-1 was better than STI, showing superior histogram matching. However, as shown qualitatively in FIG. 8, STI showed better spatially-distributed intensity matching. For MAE, STI showed the best scores overall with the E-ADNI dataset, but the worst with the ADNI dataset. Those results suggest that KLD and MAE measures, along with histogram-matching techniques, cannot be considered entirely appropriate.

In fact, one of applicants' main challenges was to determine which measure to use to assess standardization technique performances. One objective in finding such a measure would be to use an optimization method to find a better intensity mapping function.

While NMI suggested that more information from the input image was kept for STI than for PCT-1 or PCT-10 with the ADNI dataset, this measure cannot be used for that purpose since it compares the standardized image with the input image, not with the standard.

JHDS seemed to follow best applicants' qualitative evaluation by visual inspection. Those results lead the applicants to believe that it is a first step toward an appropriate performance measure.

Although a limitation of STI is that global linear registration is necessary, visual inspection showed that STI performed better than PCT-10 and PCT-1. With this new technique, applicants were able to successfully standardize intensities in two multi-centric datasets.

It will be understood that a “mask” of an image component allow to isolate specific areas of the image which can correspond to specific tissue types such as grey matter, white matter, CSF and background. It will be appreciated in FIG. 3 that the image components being masked are those in white. Any pixel/voxel not appearing in the mask is discarded and any pixel/voxel from the test image and standard image corresponding to the location of a pixel/voxel in the mask will be retained for further analysis such as generating joint histograms. In this case, applicants used brain masks obtained from the McGill Brain Imaging Center.

Registration is the process of identifying the transformations (rotation, translation, scaling, etc) that maximize the cross-correlation between characteristics from the standard and test images, estimated at each pixel/voxel position.

FIG. 4 schematically illustrates intensity adjustment of a medical image according to the present invention. A dot plot joint-histogram of medical image intensity (x axis) and standard image intensity (y axis) for each pixel/voxel is presented. Sample dot clouds for grey matter and white matter are provided. If two identical images were compared with this method, a line with a slope (m) of 1 and a y-intercept (b) of 0 would be obtained. In this example,


- - if X is less than intensity 35, y=m1x+b1,
  - if X is between 35 and 50, y=m2x+b2
  - if X is greater than 50, y=m3x+b3  
    where b is the y-intercept and m is the slope of the line (formula).

A specific linear formula of the type y=mx+b is used. The “adjusted” intensity (y value) for any medical image intensity (x value) depends on the value of X and its proximity to a tissue component. For example, if the intensity value of the pixel/voxel of the medical image to be standardized is 30, then the formula used will be y=m1x+b1. However, if the intensity value of the pixel/voxel of the medical image to be standardized is 60, then the formula used will be y=m3x+b3, and so on. It will be appreciated that the more image components in a medical image, the more formulas will be used to “adjust” the medical image intensity value. It will be understood by those skilled in the art the formula need not be a linear formula it could also be, for example, a polynomial formula. As discussed above, minimum and maximum data points were added. In this example, the presence of two image components would allow to generate only one linear formula that would not be efficient for low or high intensity values. By adding the minimum and maximum points, the “adjustment” to low and high values generates a more useful standardized image.

In cases where only 1 image component is used (i.e. one mask isolates one tissue type and all other tissues are discarded from the image), having the minimum and maximum allows to calculate 2 linear formulas. Without these added points, it would not be possible to provide an intensity adjustment factor.

FIG. 5 shows an example of an intensity histogram after standardization by the various methods indicated (PCT-10, PCT-1, STI) as well as one of the statistical measures (JHDS) used to determine standardization method effectiveness.

FIG. 6 is a block diagram illustrating various components of an apparatus for image intensity standardization. In such an apparatus, a source of medical images and a source of standard images are required. An image pre-processor pre-processes the medical image to facilitate its registration by the registrator. Masking specific tissues with the component isolator is an essential part of the present invention. Once tissues are isolated, the highest frequency data pair is retained for each tissue and used in the intensity adjustment calculator which generates an “adjustment factor” to be applied to all pixels/voxels of the medical image as a function of their proximity to the high frequency data pair. Once adjusted or standardize, the image can be presented on a viewer or image data can be transmitted to another location/computer. It will be appreciated that most aspects of this diagram can be performed by a computer using software programmed to carry out the described method.

FIG. 7 is a block diagram illustrating one possible physical setup of the present invention. In this setup, a subject is placed inside an MRI machine for generating an image of his brain. In this case the imaging is performed by radio frequency emitters/sensors that are placed inside the MRI machine. The RF sensors can send data to an image capture device for generating a viewable image of the brain. The image thereby generated must be pre-processed. After pre-processing, the image is ready to be registered with a standard image representing the same “brain volume” obtained from an image database. After registration of the image to the standard image, masks are applied in order to isolate specific tissue types. These masks can also be obtained from a mask database. A processor/calculator determines the adjustment to be performed as a function of intensity and prepares a standardized image that can be viewed on an image viewer or transmitter with a data transmitter.

FIG. 8 shows images for one subject at a specific MRI imaging site in the E-ADNI study where a standard image (a), an original image (b) and an original image standardized according to PCT-1 (c), PCT-10 (d), and STI (e) methods are presented. This is to provide an example and highlight the effectiveness of the STI approach for intra-subject variability on different imaging devices (in this case MRI machine).

FIG. 9 shows images for the same subject as that of FIG. 6 at another specific MRI imaging site in the E-ADNI study where a standard image (a), an original image (b) and an original image standardized according to PCT-1 (c), PCT-10 (d), and STI (e) methods are presented. This is to provide an example and highlight the effectiveness of the STI approach for intra-subject variability on different imaging devices (in this case MRI machine).

It will be appreciated that not all images corresponding to the statistical results of table 1 are shown herein. Selected examples for two of the seven sites tested are shown in FIGS. 8 and 9 and these images correspond to sites 1 and 2. A complete set of drawings, including those corresponding to table 2 are publicly available at the following web link:

http://medics.crulrg.ulaval.ca/

FIGS. 10 and 11 present ADNI images sorted according to MAE percentiles 100 (A), 90 (B), 75 (C), 50 (D), 25 (E), 10 (F) and 0 (G) for the foreground voxel set. Images (A) and (G) thus give the highest (worst) and lowest (best) MAE, respectively, for L4 (FIG. 10) and STI (FIG. 11). From top to bottom: input images, standard image, and images standardized with L4 and STI, respectively.

Qualitatively, although foreground MAE decreases from (A) to (G), a corresponding improvement in WM is not necessarily observed. This is also shown in Table 3, where foreground, WM and GM MAE values are given for each image of FIGS. 10 and 11. MAE values for GM do not necessarily follow the trend for the foreground either.

Interestingly, as shown in Table 3, L4 and STI can both result in higher (worse) MAE than with no standardization (see FIG. 11 (A) and (C) for WM). In other words, the WM intensity of the non-standardized image, in these cases, is closer to the standard than the WM intensity given by L4 and STI.

Finally, for the images presented in FIGS. 10 and 11, Table 3 reveals that STI gave the lowest MAE values in 26 cases (foreground: 7, WM: 10, GM: 9) vs. 16 for L4 (foreground: 7, WM: 4, GM: 5). It must be noted that this sample is not representative of the whole ADNI dataset, as we artificially selected images to display at each MAE percentiles for each standardization technique.

In some embodiments, fuzzy logic can be exploited to generate tissue-specific masks using classification algorithms. In other embodiments fuzzy logic classification [M. Ozkan, B. M. Dawant, and R. J. Maciunas, “Neural-networkbased segmentation of multi-modal medical images: A comparative and prospective study,” IEEE Trans. Med. Imag., vol. 12, pp. 534-544, September; and Zijdenbos, A P, Dawant B M, Margolin R A, Palmer A C “Morphometric Analysis of White Matter Lesions in MR images: Methods and Validation”, IEEE Trans. Med. Imag., Vol. 13, NO. 4, December 1994], can be used at the end of the processing pipeline whereby, after being processed, each image is fed to a fuzzy classification algorithm. The resultant classification gives a probability map for each tissue (e.g. CSF, GM and WM), with each voxel value ranging from 0 to 1. Examples are presented in FIG. 12 for GM (a), WM (b) and CSF (c), respectively. This procedure yields to a standardization of intensities for each tissue, intensity values being on a same common scale (0 to 1), and, in addition to providing a useful unit of measure, provides images with better overall intensity standardization.

In some embodiments of the present invention, “Background” is included as a tissue type for the purpose of this application. It will be understood that background is not really a tissue type but rather the absence of any other tissue.

STI uses spatial correspondence and joint intensity histograms between the input and standard images to find modes and use them as landmarks in the intensity mapping function. As demonstrated in this study, using spatial correspondence improves the standardization quality.

While the invention has been described in connection with specific embodiments thereof, it will be understood that it is capable of further modifications and this application is intended to cover any variations, uses, or adaptations of the invention following, in general, the principles of the invention and including such departures from the present disclosures as come within known or customary practice within the art to which the invention pertains and as may be applied to the essential features herein before set forth, and as follows in the scope of the appended claims.

