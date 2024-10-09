# DESCRIPTION

## FIELD OF THE INVENTION

The present invention relates generally to medical imaging. More particularly, the present invention relates to a method of tissue type estimation for use with computed tomography scanning.

## BACKGROUND OF THE INVENTION

Energy sensitive photon counting detector-based, x-ray computed tomography (PCD-CT) has been one of the hottest research topics lately, as it is expected to provide various clinical benefits such as enhanced tissue contrast, decreased image noise, decreased radiation dose to patient, quantitative mono-energetic CT images, and more accurate material decomposition. Tissue types such as bones, fat, muscle, and iodine-enhanced blood can then be identified, allowing software applications to, e.g., separate blood vessels from bones, quantify the fat mass, etc.

The typical approach to process PCD data consists of the following two steps. First, by applying material decomposition, density images of basis functions (discussed later), w, are reconstructed from spectral projections, i.e., counts in multi-energy bins. Second, images of linear attenuation coefficients and tissue types are estimated from w.

This sequential method decouples the two steps and makes it difficult to use a priori information on tissue types to accurately estimate linear attenuation coefficients and tissue types from photon counts. For example, tissue types may be able to effectively regularize linear attenuation coefficients than a simple edge-preserving prior. The values of neighboring pixels of linear attenuation coefficients (and w) are expected to vary smoothly and continuously if they belong to the same tissue types, while they may be discontinuous at organ boundaries. The typical values of the chemical composition and mass density of various human tissue types or organs are provided by the National Institute of Standards and Technology, from which w and linear attenuation coefficients can be calculated.

Accordingly, there is a need in the art for a method to jointly estimate images of the energy-dependent linear attenuation coefficients and tissue types from PCD data.

## SUMMARY OF THE INVENTION

The foregoing needs are met, to a great extent, by the present invention which provides a method for computed tomography imaging of a subject including obtaining photon counting detector-based x-ray computed tomography image information for the subject. The method includes performing material decomposition on the photon counting detector-based x-ray computed tomography image information for the subject. The method also includes assessing, simultaneously, an energy dependent linear attenuation coefficient and information about structures being imaged, and generating an image of the subject.

In accordance with an aspect of the present invention, the method includes reconstructing density images of basis functions, w. The method includes using latent Markov Random Field (MRF) calculations to describe geometrical information of the structures being imaged and w of the computed tomography image information for the subject. Additionally, the method includes determining a statistical relationship between a structure type and w. The method includes using Poisson noise models of PCD data and continuously executing a Bayesian estimation from a detected photon count. The method also includes programming a non-transitory computer readable medium to execute the method. The method includes w to represent a set of P-C coefficients on the image information, and using z to represent a set of latent variable labels. The method includes defining a prior distribution as a combination of the latent MRF and statistical distribution between w and z.

In accordance with another aspect of the present invention a non-transitory computer readable medium is configured for executing a method including obtaining photon counting detector-based x-ray computed tomography image information for the subject. The method includes performing material decomposition on the photon counting detector-based x-ray computed tomography image information for the subject. The method also includes assessing, simultaneously, an energy dependent linear attenuation coefficient and information about structures being imaged and generating an image of the subject.

## DETAILED DESCRIPTION

The presently disclosed subject matter now will be described more fully hereinafter with reference to the accompanying Drawings, in which some, but not all embodiments of the inventions are shown. Like numbers refer to like elements throughout. The presently disclosed subject matter may be embodied in many different forms and should not be construed as limited to the embodiments set forth herein; rather, these embodiments are provided so that this disclosure will satisfy applicable legal requirements. Indeed, many modifications and other embodiments of the presently disclosed subject matter set forth herein will come to mind to one skilled in the art to which the presently disclosed subject matter pertains having the benefit of the teachings presented in the foregoing descriptions and the associated Drawings. Therefore, it is to be understood that the presently disclosed subject matter is not to be limited to the specific embodiments disclosed and that modifications and other embodiments are intended to be included within the scope of the appended claims.

A method according to the present invention employs maximum a posteriori (MAP) Bayesian estimation based on pixel-based latent variables for tissue types: Poisson likelihood models PCD data; a Markov random field (MRF) represents the geometrical a priori information on tissue types and w; and the statistical a priori information relates tissue types and w. A computer simulation is performed to evaluate the effectiveness of the proposed method compared with the sequential, two-step method.

According to the present invention, a more accurate regularization can be performed with the knowledge of the tissue types and organ boundaries, and consequently, the image quality can be improved. The values of the linear attenuation coefficients for neighboring image pixels are expected to vary smoothly and continuously when they belong to the same tissue. In contrast, the values are usually discontinuous at the organ boundaries. Moreover, the typical values of the chemical composition and mass density of various human tissue types or organs are provided by the National Institute of Standards and Technology (NIST), from which expected values of linear attenuation coefficients can be calculated.

The present invention includes a novel image reconstruction method, denoted “Joint Estimation Maximum A Posteriori” (JE-MAP), which jointly estimates images of the energy-dependent linear attenuation coefficients and tissue types from PCD data using material decomposition. The method implements image reconstruction using prior information about tissue types as well as tissue type identification using information of the noise distribution during CT projection. The JE-MAP algorithm employs maximum a posteriori (MAP) estimation based on voxel-based latent variables for the tissue types. The geometrical and statistical information about human organs is incorporated as prior information using a voxel-based coupled Markov random field model and a Gaussian mixture model, respectively.

A. Problem Modeling

1) Characteristic Coefficients: The energy-dependent linear attenuation coefficients at photon energy E, x(E), can be described as a linear combination of the product of energy dependent basis functions, Φn(E) and their spatial distribution coefficients, wn:

\(\begin{matrix}
{{{x(E)} = {\sum\limits_{n = 1}^{N_{a}}{\omega_{n}{\Phi_{n}(E)}}}},} & (1) \\
{{{\Phi (E)} = \left( {\frac{E^{- 3}}{E_{0}^{- 3}};\frac{f_{KN}(\alpha)}{f_{KN}\left( \alpha_{0} \right)}} \right)^{T}},} & (2) \\
{{\omega = \left( {\omega_{pe},\omega_{cs}} \right)^{T}},} & (3)
\end{matrix}\)

where Na=2 is the number of basis functions, E−3 denotes the photoelectric effect, fKN(α) is the Klein-Nishina function for Compton scattering,

\(\begin{matrix}
{{{f_{KN}(\alpha)} = {{\frac{1 + \alpha}{\alpha^{2}}\left\{ {\frac{2\left( {1 + \alpha} \right)}{1 + {2\alpha}} - {\frac{1}{\alpha}{\ln \left( {1 + {2\alpha}} \right)}}} \right\}} + {\frac{1}{2\alpha}\ln \; 1} + {2\alpha} - \frac{\left( {1 + {3\alpha}} \right)}{\left( {1 + {2\alpha}} \right)^{2}}}},} & (4)
\end{matrix}\)

where α=E/510.975 keV; α0=E0=510.975 keV, and E0 is the reference energy. The coefficient vector w is denoted as the “characteristic coefficients”. Note that it is straightforward to add a third basis function and the corresponding characteristic coefficients to describe the discontinuity at the K-edge of a contrast agent. However, it is assumed herein that large attenuation in the low X-ray energy range where the detected photon counts in the low energy bins are so small that the ‘signal’ of the K-edge effect is negligible.

2) Tissue Type Labeling: A goal is to estimate the characteristic coefficients and the tissue type for each image voxel from measured PCD sinogram data. Latent variable z, is introduced to express the tissue type at each image voxel i, i=1, . . . , I, with I the total number of image voxels, using the Potts model represented by the 1-of-K scheme.

ziε{(0,1)K}, Σk=1Kzi(k)=1,  (5)

where zi(k) represents the kth element of zi (k=1, . . . , K). Thus, each image voxel is labeled by one of K tissue types with zi.

3) Image and Projection Set Definition: Let i=1, . . . , I be a voxel index of the tomographic image, and let W={wi|i=1, . . . , I} represent a set of the characteristic coefficients in the tomographic image, and let Z={zi|i=1, . . . , I} be a set of the latent variables.

Furthermore, let j=1, . . . , J be a sinogram pixel index, with J the total number of sinogram pixels, and let V={νi|i=1, . . . , I} be a set of line integrals of the characteristic coefficients in the sinogram, which can be calculated by forward projection of W as

νj=Σiεray(j)dijwi  (6)

where ray(j) is a set of image voxels through which a ray goes to sinogram pixel j in the forward projection process, and dij is an element of the forward projection matrix from image to sinogram. Let Y={yi|i=1, . . . , I} be a set of photon counts in the sinogram, where each pixel is given by yj=(y(j, 1), . . . , y(j,B)) which indicates the expected photon counts in B energy bins. The photon counts in each sonogram pixel yj can be calculated from νj as,

y(j,b)=hb(νj)=∫EEn(E)exp(−νjTΦ(E))dE,  (7)

where b=1 . . . B, n(E) denotes the x-ray spectrum emitted from the source described as a number of photon counts per keV, and the function hb: Na→ relates the line integral of the characteristic coefficients, ν, to the expected photon counts through Eq. (1) and Beer's law. The set of measured photon counts in the sinogram is described by Ŷ={ŷi|j=1, . . . , J}

B. Cost Function

The problem of image reconstruction, material decomposition, and tissue type identification can be formulated as a MAP estimation with W and Z as random variables whose estimates W*, Z* can be obtained by

\(\begin{matrix}
{{\left( {W^{*},Z^{*}} \right) = {\arg \; {\min\limits_{W,Z}\left\{ {{\ln \; {p\left( \hat{Y} \middle| W \right)}} - {\ln \; {p\left( {W,Z} \right)}}} \right\}}}},} & (8)
\end{matrix}\)

where p(Y|W) is the likelihood distribution of the measured data, and p(W, Z) is the likelihood of the prior distribution as explained in the following.

1) Likelihood: An ideal photon counting detector which is unaffected by pulse pileup effects or spectral response effects is assumed. Thus, the probability of photon counts in the bth energy bin at the jth pixel in the sinogram ŷ(j,b) follows a Poisson distribution as a result of the Poisson process of x-ray generation in the x-ray source and the binomial process of attenuation in the object. Therefore, the probability of PCD-CT measurements Ŷ given the object is calculated by taking the product of each Poisson distribution for all the energy bins and sinogram pixels:

\(\begin{matrix}
{{p\left( \hat{Y} \middle| W \right)} = {\prod\limits_{j = 1}^{J}\; {\prod\limits_{b = 1}^{B}\; {{Poisson}\left( {\hat{y}}_{({j,b})} \middle| y_{({j,b})} \right)}}}} & (9)
\end{matrix}\)

2) Prior Distribution: We define the likelihood of the prior distribution as a combination of a voxel-based coupled Markov random field (MRF) model and a statistical distribution between W and Z, as illustrated in FIG. 1. FIG. 1 illustrates a graphical view of a factor graph representing the voxel-based coupled MRF model and the Gaussian mixture model around voxel i.

ln p(W,Z):=ln pMRF(W,Z)+ln psta(W,Z)  (10)

The voxel-based coupled MRF model formulates the relation between the characteristic coefficients w and the latent variable z between neighboring voxels, while a multivariate Gaussian mixture model describes the relation between w and z in each voxels.

Voxel-based Coupled MRF Model: To express the geometrical continuity and discontinuity of human organs, the coupled MRF model is used. The coupled MRF model consists of two MRFs, one for observable variables and the other for latent variables which describe the state of the voxels. The variances of the two MRFs are coupled to each other via a probability function, e.g., a conditional probability. We adopt the coupled MRF model with voxel-based latent variables (or a voxel-based coupled MRF), regarding characteristic coefficients as observable variables and tissue types as latent variables.

Let ne(i) be a set of indexes of neighboring voxels around image voxel i. Considering the Potts model of tissue types, the voxel-based coupled MRF model is designed as follows,

\(\begin{matrix}
{{{- {\ln_{p_{MRF}}\left( {W,Z} \right)}} = {{ɛ\left( {W,Z} \right)} + \ln_{C_{MRF}}}},} & (11) \\
{{{ɛ\left( {W,Z} \right)} = {\frac{1}{2}{\sum\limits_{t = 1}^{I}{\sum\limits_{v \in {{ne}{(t)}}}\left\{ {{{\beta_{1}\left( {z_{i} \cdot z_{v}} \right)}\left( {w_{i} - w_{v}} \right)^{2}} + {\beta_{2}\left( {1 - {z_{i} \cdot z_{v}}} \right)}} \right\}}}}},} & (12)
\end{matrix}\)

where ε(W, Z) represents the energy function of the Gibbs distribution and CMRF is a normalization constant. If two tissue types zi and zi′ are the same, then the inner product becomes zi·zi′=1 and the first term of Eq. (12) encourages smoothness while the second term vanishes. When the tissue types are different then the first term vanishes and the second term adds a constant penalty. Two parameters, β1 and β2 control the effect of the two terms.

Gaussian Mixture Model: The statistical relationship between characteristic coefficients and tissue types are modeled. The expected values of w for various tissue types are obtained from the NIST database, and it is assumed that w follows a multivariate Gaussian distribution corresponded for each tissue type. The relationship between the w and all the tissue types is then modeled using a multivariate Gaussian mixture model, which is defined for each voxel.

For simplicity a tissue type is denoted expressed by the latent variable zi(k)=1 as the “kth tissue type”. In the Gaussian mixture model, the probability of zi can be described by using mixing coefficients πk as

psta(zi(k)=1)=πk,  (13)

0≦πk≦1,  (14)

Σk=1Kπk=1,  (15)

Because the Potts model is adopted, represented by the 1-of-K scheme for the latent variable z, Eq. (13) can be also written as

\(\begin{matrix}
{{{p_{sta}\left( z_{i} \right)} = {\prod\limits_{k = 1}^{K}\; \left( \pi_{k} \right)^{z_{i}^{(k)}}}},} & (16)
\end{matrix}\)

The mixing coefficient πk represents prior information about the presence of a tissue type in each image voxel. Thus, psta(zi) can be formulated as, for example, a function of the location, size, or shape of the voxels that belong to a particular tissues type. For simplicity, we assume a uniform probability for all tissues, i.e., psta(zi)=1/K for all k.

The conditional probability of wi given zi is described as a multivariate Gaussian distribution:

psta(wi|zi(k)=1)=N(wi|μk,Σk),  (17)

where μk and Σk are the expected value and the covariance matrix of the characteristic coefficients for the kth tissue type, respectively. Using the notation of the Potts model, Eq. (17) can also be written as

\(\begin{matrix}
{{{p_{sta}\left( w_{i} \middle| z_{i} \right)} = {\prod\limits_{k = 1}^{K}{N\left( {\left. w_{i} \middle| \mu_{k} \right.,\sum_{k}} \right)}^{z_{i}^{(k)}}}},} & (18)
\end{matrix}\)

Therefore, the multivariate Gaussian distribution of the statistical relation between W and Z can be obtained by summing the joint probabilities of Eq. (16) and Eq. (18) for all voxels:

−ln psta(W,Z)=−β3Σi=1I{ln psta(zi)+ln psta(wi|zi)}=β3Σi=1I{ln K+Σk=1Kzi(k){½(wi−μk)TΣk−1(wi−μk)+ln Ck}},  (19)

where Ck is the normalization constant of the multivariate Gaussian distribution for the kth tissue type, and β3 is a weighting parameter.

C. Optimization

The MAP estimation Eq. (8) is computationally intractable due to the nonlinearity of x-ray attenuation and the introduction of latent variables. Therefore, the likelihood in Eq. (9) is approximated by a Gaussian distribution, and an iterated conditional modes (ICM) algorithm is used, which realizes voxel-driven optimization with the discrete latent variables. The flowchart of the JE-MAP algorithm is summarized in the pseudo code in FIG. 11.

FIG. 11 shows a flow of JE-MAP. First, the likelihood approximation is performed followed by initializing the image set of characteristic coefficients and tissue types. Because latent variable for tissue types are introduced, the cost function tends to have more local minima than the method regarding only characteristic coefficients as variables. The ICM is terminated when the difference in the cost function from one iteration to the next becomes less than a certain value c.

1) Approximation of the Likelihood: For a given set of latent variables Z, both prior terms in Eqs. (11) and (19) are quadratic functions of w. The Poisson likelihood term, Eq. (9), however, is not quadratic and expensive to compute. Thus, the Poisson likelihood is approximated by a Gaussian distribution of the line integrals of the characteristic coefficients, V.

Using Eq. (6), the likelihood function of W given Ŷ to the likelihood function of V given Ŷ as,

p(Ŷ|W)=L(W|Ŷ)=L(V|Ŷ)=Πj=1JL(νj|ŷj).  (20)

The transformation between W and V satisfies the data sufficiency, i.e., the mapping q: W→V is bijective. The Poisson likelihood L can be written as follows using the function hb in Eq. (7).

\(\begin{matrix}
{{L\left( v_{i} \middle| {\hat{y}}_{j} \right)} = {\prod\limits_{b = 1}^{B}{\frac{{h_{b}\left( v_{j} \right)}^{{\hat{y}}_{({j,b})}}{\exp \left( {- {h_{b}\left( v_{j} \right)}} \right)}}{{\hat{y}}_{({j,b})}!}.}}} & (21)
\end{matrix}\)

This likelihood function is approximated with a multivariate Gaussian distribution,

L(νj|ŷj)≈N(νj|νj*,Pj*),  (22)

where νj*εN and Pj*εN×N are the mean vector and covariance matrix, respectively of the line integrals of the characteristic coefficients. The parameters are found by minimizing the Kullback-Leibler divergence of the multivariate Gaussian distribution with constant factor N from the likelihood L:

\(\begin{matrix}
{{\left( {v_{j}^{*},P_{j}^{*}} \right) = {\arg\limits_{v_{j},P_{j}}\; \min \; {D_{KL}\left( {L{}N} \right)}}},} & (23) \\
{{D_{KL}\left( {L{}N} \right)} = {\int{{\ln \left( \frac{L\left( v_{j} \middle| {\hat{y}}_{j} \right)}{N\left( {\left. v_{j} \middle| \upsilon_{j} \right.,P_{j}} \right)} \right)}{L\left( v_{j} \middle| {\hat{y}}_{j} \right)}{{v_{j}}.}}}} & (24)
\end{matrix}\)

As shown in Appendix A, the minimum is given by

\(\begin{matrix}
{{\upsilon_{j}^{*} = \frac{\int{{L\left( v_{j} \middle| {\hat{y}}_{j} \right)}v_{j}{v_{j}}}}{\int{{L\left( v_{j} \middle| \hat{y_{j}} \right)}{v_{j}}}}},} & (25) \\
{P_{j}^{*} = {\frac{\int{{L\left( v_{j} \middle| {\hat{y}}_{j} \right)}v_{j}{v_{j}}}}{\int{{L\left( v_{j} \middle| \hat{y_{j}} \right)}{v_{j}}}} - {\upsilon_{j}^{*}{\upsilon_{j}^{*T}.}}}} & (26)
\end{matrix}\)

By performing the minimization for sinogram pixels j=1, . . . , J independently, the Gaussian parameters for the entire sonogram are obtained. The Poisson likelihood of the image W given the measurement Ŷ is approximated by multivariate Gaussian distributions of νj given the parameters νj* and Pj*:

p(Ŷ|W)≈Πj=1JN(νj|υj*,Pj*).  (27)

2) Iterative Method: In order to handle all of the combinations of discrete variables z efficiently, an iterated conditional modes (ICM) algorithm was used, which updates the parameters of each image voxel successively. The flowchart of ICM as used in the JE-MAP algorithm is shown in FIG. 2. FIG. 2 illustrates a schematic diagram of a core scheme of the ith iteration of ICM. The ith iteration ends when the flow (a) to (c) is completed for all voxels.

During the update of the ith voxel in the tth iteration, the following sub-minimization of the quadratic cost function F(wi) is performed with zi fixed to one of the K tissue types:

\(\begin{matrix}
{\mspace{79mu} {\left. w_{i}^{new} \right|_{z_{i}^{(k)} = 1} = \left. {\arg\limits_{w_{i}}\min \; {F\left( w_{i} \right)}} \right|_{z_{i}^{(k)} = 1^{\prime}}}} & (28) \\
{{\left. {F\left( w_{i} \right)} \right|_{z_{i}^{(k)} = 1} = {{\sum\limits_{j \in {{ray}^{\prime}{(i)}}}{{g_{j}\left( w_{i} \right)}^{T}P_{j}^{- 1}{g_{j}\left( w_{i} \right)}}} + {\sum\limits_{v \in {{ne}{(i)}}}\left\{ {{{\beta_{i}\left( {z_{1} \cdot z_{2}} \right)}\left( {w_{i} - w_{v}} \right)^{2}} + {\beta_{2}\left( {1 - {z_{i} \cdot z_{d}}} \right)}} \right\}} + {\beta_{3}\left\{ {{\left( {w_{t} - \mu_{k}} \right)^{T}{\sum\limits_{k}\left( {w_{i} - \mu_{k}} \right)}} + C_{k}} \right\}}}},} & (29) \\
{\mspace{79mu} {{{g_{j}\left( w_{i} \right)} = {{d_{ij}\left( {w_{i} - w_{i}^{(t)}} \right)} - \left( {v_{j} - v_{j}^{(t)}} \right)}},}} & (30)
\end{matrix}\)

where ray′(i) denotes a set of sinogram pixels onto which the voxel i is projected, and the constant values wi(t) and νi(t) are characteristic coefficients of image voxel i and the line integral of characteristic coefficients in sinogram pixel j, respectively, both of which were estimated in the previous (t−1)th iteration.

Because the cost function F(wi) is convex and quadratic over wi in each sub-minimization as shown in Appendix B, its minimum can be analytically found with no iteration by completing the square. After performing the sub-minimization procedure for all K tissue types, the characteristic coefficients winew and tissue type zinew which give the minimum cost are selected and used in the next step.

### III. EXEMPLARY IMPLEMENTATIONS

Exemplary implementation of the present invention are described herein, in order to further illustrate the present invention. The exemplary implementation is included merely as an example and is not meant to be considered limiting. Any implementation of the present invention on any suitable subject known to or conceivable by one of skill in the art could also be used, and is considered within the scope of this application.

A. Phantom and Scan

A modified thorax image of the XCAT phantom was used with the nine tissue types shown in FIG. 3A. FIGS. 3A-3E illustrate images and graphical data related to a thorax of the modified XCAT phantom. FIG. 3A illustrates an image of nine tissue types including air indicated by different shading. FIG. 3B illustrates a monochromatic CT image at 70 keV, WW 600 HU and WL 0 HU. FIGS. 3C and 3D illustrate images of distributions of two character coefficients. FIG. 3E illustrates a graphical view of a scatter plot of characteristic coefficients in the phantom. The phantom image covered 40×40 cm2 by 512×512 pixels, and geometrical textures were added to make the image pixel values inside organs heterogeneous. Parallel beam projections were simulated with Poisson noise and the following parameters: tube voltage 140 kV, x-ray 105 counts per incident projection ray, 360 projections over 180°, 728 detectors with 0.78125 mm width, and 4 energy thresholds at 10, 40, 70, 100 keV. 100 noise realizations were performed.

B. Reconstruction and Tissue Type Classification

First, material decomposition was performed to obtain two sinograms of the characteristic coefficients from the PCD data through Eq. (20) to Eq. (26). Then, images of the characteristic coefficients were reconstructed using the following three methods: FBP, PML, and JE-MAP. A color table for tissue types in the phantom is included below. The FBP images were used as an initial estimate for PML and JE-MAP. For each image pixel, a tissue type is chosen which gives the minimum L2-norm distance from the statistically expected values to the image pixel value. FBP with a Shepp-Logan filter was performed on each of the three sinograms of the characteristic coefficients independently to obtain the corresponding image.

PML minimizes the Gaussian likelihood of the data (Eq. (22)) with a quadratic regularizer R(W) weighted by γ=5×104:

W*=argwmax{ln p(Ŷ|W)−ln R(W)}, R(W)=½Σi=1NΣνεne(i)γ(wi−wν)2.  (31)

JE-MAP was performed with β1=6.0×104, β2=1.5, and β3=1.0. The covariance matrix Σk was sampled from the phantom and scaled by β4=1.0×10−2.

Σk=β4Σsample,k.  (32)

For each image pixel of wi a tissue type is chosen which gives the minimum L2-norm distance from the statistically expected values to the image pixel value. Monochromatic CT images at 70 keV were synthesized from the characteristic coefficient images using Eq. (1).

C. Impact of Parameters

In order to better understand the role of the four terms in JEMAP, only one of the four parameters, β1, β2, β3, β4 was changed at a time and qualitatively evaluated the image quality.

D. Quantitative Evaluation

The standard deviation, a, of pixel values over 100 noise realizations was measured. The averaged value over adipose regions shown in FIG. 4A was used to measure the image noise.

The spatial resolution was quantified by fitting an error function to each horizontal edge profile in the region shown in FIG. 4B.

\(\begin{matrix}
{{{{Edge}(x)} = {{\frac{\lambda_{1}}{2}\left( {1 + {{erf}\left( \frac{x - \lambda_{2}}{\sqrt{2}\lambda_{3}} \right)}} \right)} + \lambda_{4}}},} & (33)
\end{matrix}\)

In Eq. (33), λ3 indicates the sharpness of the edge, from which the full-width-at-half-maximum (FWHM) was calculated as FWHM=2√{square root over (2 ln 2λ3)}. The FWHM was averaged over all profiles to obtain a measure for the spatial resolution. The trade-off between the image noise and spatial resolution was obtained by applying different Gaussian filters to the images and repeating the measurements.

The accuracy of the CT images was quantified by calculating the bias of the monochromatic CT images for each pixel, and the mean bias was calculated over the entire region inside the phantom. The accuracy of the tissue types was assessed in a binary fashion on a pixel basis. When the chosen tissue type for the image pixel was the correct tissue type, it was considered an accurate outcome; if it was not the correct tissue type, it was considered an inaccurate outcome. The ratio of the number of accurate outcomes to the number of image pixels is the accuracy of the tissue types.

FIGS. 4A and 4B illustrate images where the mean of the standard deviation is obtained in the inner region of adipose in FIG. 4A and illustrates an image where the FWHMs are calculated from horizontal edges inside the region indicated by the white box in FIG. 4B.

### IV. EVALUATION RESULTS

FIGS. 5A-5F illustrate the estimated tissue types and monochromatic CT images at 70 keV from one noise realization and FIG. 6 illustrates a graphical view of a horizontal profile take along the line shown in FIG. 5F for each reconstruction method through adipose, rib, lung, and a thin layer of adipose, and the liver. More particularly, FIGS. 5A-5C illustrate images of estimated tissue types and FIGS. 5D-5F illustrate monochromatic CT images at 70 keV (WW 600 HU, WL 0 HU). A strong salt and pepper noise can be seen in the FBP image (σ=46.8 HU in entire phantom) which resulted in a salt and pepper pattern in the tissue type image as well. PML provided CT images with less noise (σ=38.5 HU). However, it blurred the organ boundaries as shown in FIG. 6, which resulted in wrong tissue type identification near the organ boundaries. For example, it can be seen that there is adipose tissue identified at the boundaries between the heart muscle and the lung, or the heart muscle and the ventricles. JE-MAP reconstructed CT images with much less noise (σ=27.4 HU), while the boundaries of organs remained sharp (FIG. 6) resulting in more accurate tissue type identification at the boundaries. There are some regions in the tissue images of PML and JE-MAP where muscle and liver tissues were mislabeled because the characteristic coefficients of muscle and liver are too close to each other to be separated (see FIG. 3E).

FIGS. 7A-7F illustrate JE-MAP images when one of the four parameters was smaller than the default setting used in FIGS. 5A-5F. FIGS. 7A-7C illustrate images of estimated tissue types. FIGS. 7D-7F illustrate images of monochromatic CT images at 70 keV obtained by JE-MAP with smaller parameters than the optimal ones. (WW 600 HU, WL 0 HU). FIGS. 7A and 7D are taken with a smaller β1, FIGS. 7B and 7E taken with a smaller β2, and FIGS. 7B and 7E also taken with a smaller β4.

FIGS. 8A-8F illustrate images with larger parameters than optimal used in FIGS. 5A-5F. FIGS. 8A-8C illustrate images of the estimated tissue types, and FIGS. 8D-8F illustrate monochromatic CT images at 70 keV obtained by JE-MAP with larger parameters than the optimal ones. (WW 600 HU, WL 0 HU). FIGS. 8A and 8D are taken with a smaller β1, FIGS. 8B and 8E taken with a smaller β2, and FIGS. 8B and 8E also taken with a smaller β4. The use of a smaller β1 made the images heterogeneous but noisy (FIGS. 7A and 7D), while the use of a larger β1 resulted in a camouflage pattern caused by mislabeled tissue types (FIGS. 8A and 8D). Decreasing β2 resulted in salt and pepper noise (FIGS. 8B and 8E), while increasing β2 made the shape of the organs smoother (FIGS. 8B and 8E)). Both β3 and β4 had the same effect on the images, and decreasing either β3 or β4 weakened the relationship between the characteristic coefficients so that the pixels were identified as either tissue type. Increasing either β3 or β4 made the characteristic coefficients (thus, CT pixel values) to be closer to the statistically expected values, suppressing the geometrical heterogeneous textures inside the organs.

FIGS. 9A-9C illustrate image results of 100 noise realizations with bias. FIGS. 9D-F illustrate image results of 100 noise realizations with noise of CT images, and FIGS. 9G-9I illustrate image results of 100 noise realizations with the accuracy of tissue type identification. Display window width and level are: (9A-9C) 100 HU, 0 HU, (9D) 100 HU, 100 HU, (9E-9F) 30 HU, 60 HU, (9D) 100 HU, 100 HU, and (9G-9I) 50%, 100%.

FIGS. 9A-9I illustrate the bias and standard deviation of the CT images at 70 keV, and the accuracy of the tissue type identification. The mean values were measured for each organ excluding pixels near the boundaries of organs and are presented together with the mean values of the entire phantom in Tables III, IV, and V, below. It can be seen that JE-MAP provided the best values in most indexes. The bias was as small as −0.1 HU with JE-MAP. The image noise of the entire phantom (Table IV) was 46.8 HU for FBP, 38.5 HU for PML and 27.4 HU for JE-MAP. The accuracy of tissue types improved from 71.7% for FBP and 80.1% for PML to 86.9% for JE-MAP. The low accuracy of muscle with JE-MAP was attributed to the mislabeling as liver. The resolution-noise tradeoff curves were shown in FIG. 10, where the top-left end-point of the curves was obtained from the images reconstructed by the corresponding method. JE-MAP provided the best tradeoff performance. FIG. 10 illustrates a graphical view of noise-resolution tradeoff curves. The top-left point of each method is the values from the estimated images, and the curves are obtained by blurring each image with a Gaussian filter with various parameters.

### V. DISCUSSION AND CONCLUSION

The present invention is directed to a new framework, JE-MAP, to jointly perform image reconstruction, material decomposition, and tissue type identification for photon-counting x-ray CT. The results showed that JE-MAP provided superior noise-resolution tradeoff for the CT images (FIG. 10) than PML with quadratic penalty and FBP. This is because JE-MAP does not penalize differences between adjacent pixels at organ boundaries, while PML with quadratic penalty encourages smoothness even at edges. A PML with edge-preserving penalty could perform better than that with quadratic penalty, and a comparison with JE-MAP would be of interest. However, JE-MAP has a greater potential than PML, because an edge-preserving penalty such as the Huber penalty changes the strength of the penalty based on differences in pixel values, which are affected by image noise. Moreover, JE-MAP could use more prior information about tissues in the human body via additional latent variables such as the location, the size, and the number of pixel groups with the same tissue type.

The accuracy of the tissue type identification improved as well for JE-MAP compared to PML and FBP. While the tissue type images based on FBP and PML images showed an isolated salt-and-pepper noise pattern, JE-MAP provided pixels with the same tissue type grouped together to form ‘islands.’ This is because JE-MAP honors the statistical relation between the characteristic coefficients and the tissue types and those between neighboring pixels. Another advantage of JE-MAP is that the tissue-type identification is based on the projection likelihood rather than on information from image voxels. This means that JE-MAP can perform identification by placing more weight on the prior information if the reconstructed characteristic coefficients are not accurate due to large noise in the projection data.

A potential problem of JE-MAP with the current parameter setting is that it might suppress heterogeneous textures inside organs (FIG. 9C) or introduce a bias. This behavior can be attributed to suboptimal parameters such as β4. A larger β4 decreases the image noise as can be seen in FIG. 8F, but at the expense of heterogeneous texture and bias.

## APPENDIX

### A. Derivation of Equation (25), (26)

In this section the analytic solution for the minimization of the Kullback-Leibler divergence of a multivariate Gaussian distribution is presented. The minimization of the Kullback-Leibler divergence over the expected vector νj and covariance matrix Pj of the multivariate Gaussian distribution can be described by extracting the terms including νj and Pj as,

(υj*,Pj*)=argν,PminG(υj,Pj),  (34)

G(νj,Pj)=∫L(νj|ŷj){(νj−υj)TPj−1(νj−υj)−ln |Pj−1|}dνj.  (35)

The values νj*, Pj* that minimize the Kullback-Leibler divergence are those where partial derivatives equal zero.

\(\begin{matrix}
{\mspace{79mu} {\frac{\partial G}{\partial\upsilon_{j}} = \left. 0\Rightarrow{{Eq}.\mspace{14mu} 25} \right.}} & (36) \\
{\left. \frac{\partial G}{\partial P_{j}} \right|_{v_{j} = v_{j}^{*}} = {\left. \left. \Rightarrow\frac{\partial G}{\left. \partial \right)P_{j}^{- 1}} \right. \right|_{v_{j} = v_{j}^{*}} = {\left. 0\Rightarrow{{\int{{L\left( v_{j} \middle| {\hat{y}\; j} \right)}v_{j}v_{j}^{T}{v_{j}}}} - {2\upsilon_{j}^{*}{\int{{L\left( v_{j} \middle| {\hat{y}}_{j} \right)}v_{j}^{T}{v_{j}}}}} + {\upsilon_{j}\upsilon_{j}^{*}{\int{{L\left( v_{j} \middle| {\hat{y}}_{j} \right)}{v_{j}}}}} - {P_{j}{\int{{L\left( v_{j} \middle| {\hat{y}}_{j} \right)}{v_{j}}}}}} \right. = {\left. 0\Rightarrow{P_{j}{\int{{L\left( v_{j} \middle| {\hat{y}}_{j} \right)}{v_{j}}}}} \right. = \left. {{\int{{L\left( v_{j} \middle| {\hat{y}}_{j} \right)}v_{j}v_{j}^{T}{v_{j}}}} - {\upsilon_{j}\upsilon_{j}^{*}{\int{{L\left( v_{j} \middle| {\hat{y}}_{j} \right)}{v_{j}}}}}}\Rightarrow{{Eq}.\mspace{14mu} 26} \right.}}}} & (37)
\end{matrix}\)

### B. Convexity Proof for Equation (29)

In this section the convexity of the cost function in the ICM scheme F|zi(k)=1 by calculating the Hessian matrix. From Eq. (29), the Hessian matrix with respect to wi becomes

\(\begin{matrix}
{{{H\left( \left. F \right|_{z_{i}^{(k)} = 1} \right)} = {{\sum\limits_{j \in {{ray}^{\prime}{(i)}}}{d_{ij}P_{j}^{- 1}}} + {\sum\limits_{i^{\prime} \in {{ne}{(i)}}}{{\beta_{1}\left( {z_{i} \cdot z_{i^{\prime}}} \right)}I}} + {\beta_{3}\sum\limits_{k}}}},} & (38)
\end{matrix}\)

where I is the identity matrix. Because each term in Eq. (38) is a covariance matrix, H is positive-semidefinite, i.e., H0,

therefore F|zi(k)=1 is convex.

A computing device can be programmed to execute the steps of the method of the present invention. A computing device for use with the present invention can be loaded with a non-transitory computer readable medium configured to execute the steps of the method. Alternately, the computing device can be networked to a server or other computing device configured to execute the steps of the method. The computing device can also be networked to the computed tomography scanning machine either wired or wirelessly in order to obtain the information from the computed tomography scans for processing. The information from the computed tomography scan can also be input into the computing device manually or using magnetic, optical, or other computer readable medium. As used herein, a non-transitory computer readable medium can be any article of manufacture that contains data that can be read by a computer. Such computer readable media includes but is not limited to magnetic media, such as a floppy disk, a flexible disk, a hard disk, reel-to-reel tape, cartridge tape, cassette tape or cards; optical media such as CD-ROM and writeable compact disc; magneto-optical media in disc, tape or card form; and paper media, such as punched cards and paper tape. The computer readable medium contains code such that the method described herein can be executed.

The many features and advantages of the invention are apparent from the detailed specification, and thus, it is intended by the appended claims to cover all such features and advantages of the invention which fall within the true spirit and scope of the invention. Further, since numerous modifications and variations will readily occur to those skilled in the art, it is not desired to limit the invention to the exact construction and operation illustrated and described, and accordingly, all suitable modifications and equivalents may be resorted to, falling within the scope of the invention.

