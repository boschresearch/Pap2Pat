# INTRODUCTION

Computed tomography (CT) is one of the most important medical imaging tools, thanks to its high contrast resolution and short scan durations. Recent improvements in detector technology made it possible to develop energy-resolved photon counting detector (PCD)-based CT, which is expected to provide various clinical benefits such as enhanced tissue contrast, decreased image noise, decreased radiation dose to patient, quantitative monoenergetic CT images, and more accurate material decomposition. 1 PCD-CT counts the number of x-ray photons transmitted through an attenuator with two or more energy windows using an energy-resolved semiconductor detector such as CZT or CdTe and allows using multiple basis functions in material decomposition. 2 For example, a linear combination of three basis functions-e.g., photoelectric effect, Compton scattering, and the discontinuity at the K-edge of a contrast agent-can accurately model the energy-dependent linear attenuation coefficient of any material typically involved in clinical imaging routine, except for metallic implants. 3 The coefficients of basis functions, which we call characteristic coefficients in this paper, are functions of the chemical composition and the mass density of the attenuator. They are unique for typical biological compounds such as adipose, heart muscle, liver parenchyma, lung, rib, spine, and iodine-enhanced blood. 4 Therefore, energy-resolved PCD-CT has the potential to perform tissue-type identification more accurately using the characteristic coefficients and allowing software to separate blood vessels from bones, quantify the fat mass, etc.

A variety of methods have been proposed to reconstruct the projection data in energy-resolved CT. [5][6][7][8] As in the case of conventional x-ray CT, iterative reconstruction methods have improved the trade-off between the spatial resolution and the noise in the reconstructed images compared to analytic filtered backprojection (FBP) methods. Many iterative methods are a variation of the penalized maximum likelihood (PML) method. While the likelihood term of these methods is based on the statistical properties of the measured data, the regularization (or prior) term is empirical and is often not optimal. For example, the transition point for the Huber prior between the quadratic and the linear penalty term is defined without exact knowledge of the tissue type to which the pixel of interest belongs, 9 and the same parameters are applied to all pixels regardless of their true tissue type.

We hypothesize that a more accurate regularization can be performed with the knowledge of the tissue types and organ boundaries, and consequently, the image quality can be improved. The values of the linear attenuation coefficients for neighboring image pixels are expected to vary smoothly and continuously when they belong to the same tissue. In contrast, the values are usually discontinuous at the organ boundaries. Moreover, the typical values of the chemical composition and mass density of various human tissue types or organs are provided by the National Institute of Standards and Technology (NIST), from which expected values of linear attenuation coefficients can be calculated.

We propose a novel image reconstruction method, denoted "joint estimation maximum a posteriori" (JE-MAP), which jointly estimates images of the energy-dependent linear attenuation coefficients and tissue types from PCD data using material decomposition. The method implements image reconstruction using prior information about tissue types as well as tissue-type identification using information of the noise distribution during CT projection. The JE-MAP algorithm employs maximum a posteriori (MAP) estimation based on voxel-based latent variables for the tissue types. 10 The geometrical and statistical information about human organs is incorporated as prior information using a voxelbased coupled Markov random field (MRF) model and a Gaussian mixture model, respectively. 11,12 We performed computer simulations to systematically and quantitatively evaluate the effectiveness of the proposed method compared to FBP and PML methods with a quadratic penalty.

# METHODS

In this section we outline the following three aspects of the proposed algorithm: problem modeling in Sec. 

# 2.A.1. Characteristic coefficients

The energy-dependent linear attenuation coefficients at photon energy E, x(E), can be described as a linear combination of the product of energy-dependent basis functions, Φ n (E), and their spatial distribution coefficients, w n ,

where N a = 2 is the number of basis functions, E -3 denotes the energy dependence of the photoelectric effect, f KN (α) is the Klein-Nishina function for Compton scattering,

where α = E/510.975 keV, α 0 = E 0 /510.975 keV, and E 0 is the reference energy. The coefficient vector w is denoted as the "characteristic coefficients." Note that it is straightforward to add a third basis function and the corresponding characteristic coefficients to describe the discontinuity at the K-edge of a contrast agent. However, in this paper, we do not consider this case because we assume that due to large attenuation, the detected photon counts in the low energy bins are so small that the "signal" of the K-edge effect is negligible.

# 2.A.2. Tissue-type labeling

Our goal is to estimate the characteristic coefficients and the tissue type for each image voxel from measured PCD sinogram data.

We introduce latent variables z i to express the tissue type at each image voxel i, i = 1,...,I, with I the total number of image voxels, using the Potts model represented by the 1-of-K scheme, 13

where z (k) i represents the kth element of z i (k = 1,...,K). Thus, each image voxel is labeled by one of the K tissue types with z i .

# 2.A.3. Image and projection set definition

Let i = 1,...,I be a voxel index of the tomographic image, and let W = {w i |i = 1,...,I} represent a set of the characteristic coefficients in the tomographic image, and let Z = {z i |i = 1,...,I} be a set of the latent variables.

Furthermore, let j = 1,...,J be a sinogram pixel index, with J the total number of sinogram pixels, and let V = v j | j = 1,...,J be a set of line integrals of the characteristic coefficients in the sinogram, which can be calculated by forward projection of W as

where ray( j) is a set of image voxels through which a ray goes to sinogram pixel j in the forward projection process, and d i j is an element of the forward projection matrix from image to sinogram. Let Y = y j | j = 1,...,J be a set of photon counts in the sinogram, where each pixel is given by y j = ( y ( j,1) ,..., y ( j, B) ) which indicates the expected photon counts in B energy bins. The photon counts in each sinogram pixel y j can be calculated from v j as

where b = 1,...,B, n(E) denotes the x-ray spectrum emitted from the source described as a number of photon counts per keV, and the function h b : R N a → R relates the line integral of the characteristic coefficients, v, to the expected photon counts through Eq. ( 1) and Beer's law. We assume the use of antiscatter grids which limit the detection of the x-ray photons from unexpected directions, and thus ignore the effect of detection of x-ray scattered in the object. We describe the set of measured photon counts in the sinogram by Ŷ = ŷj | j = 1,...,J .

# 2.B. Cost function

The problem of image reconstruction, material decomposition, and tissue-type identification can be formulated as a MAP estimation with W and Z as random variables whose estimates W * and Z * can be obtained by

where L(W | Ŷ ) is the likelihood distribution of the object given the measured data, and p(W,Z) is the prior distribution as explained in the following.

# 2.B.1. Likelihood

We assume an ideal photon counting detector which is unaffected by pulse pileup effects 14 or spectral response effects. 15 Thus, the probability of photon counts in the bth energy bin at the jth pixel in the sinogram ŷ(j,b) follows a Poisson distribution as a result of the Poisson process of x-ray generation in the x-ray source and the binomial process of attenuation in the object. Therefore, the likelihood of probability of the object given PCD-CT measurements Ŷ is calculated by taking the product of each Poisson probability distribution for all the energy bins and sinogram pixels,

where Poisson(k|λ) denotes the Poisson probability distribution of k with expected value λ,

Note that Eq. ( 9) is a function of W where W appears by substituting Eqs. ( 6) and (7) for y ( j,b) (W ) in Eq. (9).

# 2.B.2. Prior distribution

We define the prior distribution as a combination of a voxel-based coupled MRF model and multiple sets of joint distributions of Gaussian mixture model (Fig. 1),

The voxel-based coupled MRF model formulates the relationship between the characteristic coefficients w and the latent variable z between neighboring voxels, while a joint distribution of Gaussian mixture model describes the statistical relationship between w and z in each voxel.

# 2.B.2.a. Voxel-based coupled MRF model.

To express the geometrical continuity and discontinuity of human organs, we use the coupled MRF model, which was proposed in the context of visual image processing. 11 The coupled MRF model consists of two MRFs, one for observable variables and the other for latent variables which describe the state of the voxels. The variances of the two MRFs are coupled to each other via a probability function, e.g., a conditional probability. We adopt the coupled MRF model with voxel-based latent variables (or a voxel-based coupled MRF), regarding characteristic coefficients as observable variables and tissue types as latent variables.

Let ne(i) be a set of indexes of neighboring voxels around image voxel i. Considering the Potts model of tissue types, we design the voxel-based coupled MRF model as follows:

where E(W,Z) represents the potential function of the Gibbs distribution and C CMRF is a normalization constant. If two tissue types z i and z i ′ are the same, then the inner product becomes z i • z i ′ = 1 and the first term of Eq. ( 13) encourages smoothness while the second term vanishes. When the tissue types are different, then the first term vanishes and the second term adds a constant penalty. Two parameters, β 1 and β 2 , control the effect of the two terms.

# 2.B.2.b. Statistical relationship modeling.

The NIST database 16 provides data on the chemical composition and density of various tissue types, as well as the energy-dependent mass attenuation coefficients of chemical elements. From these data, thus we can calculate the energy-dependent linear attenuation coefficients of each tissue type, from which its characteristic coefficients w are obtained by least square fitting of Eq. ( 1). We prepare characteristic coefficients of all tissue types which can appear in an object. We assume that w follows a multivariate Gaussian distribution corresponded for each tissue type. We then model the statistical distribution of w by a set of multivariate Gaussian distributions, i.e., the joint distribution of Gaussian mixture, which is defined for each voxel.

For simplicity, we denote a tissue type expressed by the latent variable z (k) i = 1 as the "kth tissue type." The probability of z i can be described by using mixing coefficients π k as

Since we adopt the Potts model represented by the 1-of-K scheme for the latent variable z, Eq. ( 14) can be also written as

The mixing coefficient π k represents prior information about the presence of a tissue type in each image voxel. Thus, we can formulate p sta (z i ) as, for example, a function of the location, size, or shape of the voxels that belong to a particular tissues' type. For simplicity, we assume a uniform probability for all tissues, i.e., p sta (z i ) = 1/K for all k. The conditional probability of w i given z i is described as a multivariate Gaussian distribution

where µ k and Σ k are the expected value and the covariance matrix of the characteristic coefficients for the kth tissue type, respectively. Using the notation of the Potts model, Eq. ( 18) can also be written as

Therefore, the statistical relationship between W and Z can be obtained by summing the joint probabilities of Eqs. ( 17) and ( 19) for all voxels,

where C k is the normalization constant of the multivariate Gaussian distribution for the kth tissue type, β 3 is a weighting parameter, and superscript T denotes a transpose.

# 2.C. Optimization

The MAP estimation Eq. ( 8) is computationally intractable due to the nonlinearity of x-ray attenuation and the introduction of latent variables. Therefore, we approximate the likelihood in Eq. ( 9) by a Gaussian distribution, and use an iterated conditional modes (ICM) algorithm, 17 which realizes voxel-driven optimization with the discrete latent variables. The flow chart of the JE-MAP algorithm is summarized in the pseudocode in the listing Algorithm I.

# 2.C.1. Approximation of the Likelihood

For a given set of latent variables Z, both prior terms in Eqs. ( 12) and ( 22) are quadratic functions of w. The Poisson likelihood term, Eq. ( 9), however, is not quadratic and expensive to compute. Thus, we approximate the Poisson A I. Pseudo code of JE-MAP. First, the likelihood approximation is performed followed by initializing the image set of characteristic coefficients and tissue types. Since we introduced latent variable for tissue types, the cost function tends to have more local minima than the method regarding only characteristic coefficients as variables. The ICM is terminated when the difference in the cost function from one iteration to the next, ∆ln p(W, Z | Ŷ ), becomes less than a certain value ϵ.

Estimate ν * j , P * j from Eq. ( 27) and Eq. (28) 3: end for 4: Initialize W 0 , Z 0 5: Number of iterations t = 0 {ICM start} 6: while ∆ln p(W, Z | Ŷ ) ≥ ϵ do 7:

for i = 1 to N do 8:

for k = 1 to K do 9:

Solve

10: end for 11:

Select (w

end for 13:

t ← t + 1 14: end while likelihood by a Gaussian distribution of the line integrals of the characteristic coefficients, V .

The Poisson likelihood L in Eq. ( 9) can be written as follows using the function h b in Eq. ( 7):

Similar to Refs. 18 and 19, we approximate this Poisson likelihood with a multivariate Gaussian distribution,

where ν * j ∈ R N a and P * j ∈ R N a ×N a are the mean vector and covariance matrix, respectively, of the line integrals of the characteristic coefficients. We find the parameters by minimizing the Kullback-Leibler divergence 20 of the multivariate Gaussian distribution with constant factor N from the likelihood L,

As shown in Appendix A, the minimum is given by

By performing the minimization for sinogram pixels j = 1, ...,J independently, we obtain the Gaussian parameters for the entire sinogram. The Poisson likelihood of the image W given the measurement Ŷ is approximated by multivariate Gaussian distributions of v j given the parameters ν * j and P * j ,

# 2.C.2. Iterative method

In order to handle all of the combinations of discrete variables z efficiently, we also have to propose a new algorithm for MAP optimization. For simplicity, we use ICM algorithm in this paper and update the variables of each image voxel sequentially.

During the update of the ith voxel in the tth iteration, the following subminimization of the quadratic cost function F(w i ) is performed with z i fixed to one of the K tissue types:

where ray ′ (i) denotes a set of sinogram pixels onto which the voxel i is projected, w (t) i and v (t) j are constant values both of which were estimated in the previous (t -1)th iteration.

Since the cost function F(w i ) is convex and quadratic over w i in each subminimization as shown in Appendix B, its minimum can be analytically found with no iteration by completing the square. After performing the subminimization procedure for all K tissue types, the characteristic coefficients w new i and tissue type z new i which give the minimum cost are selected and used in the next step.

# 3.A. Phantom and scan

Since PCD-CT has not been put to practical use, we performed a phantom simulation to evaluate our algorithm. We used a modified thorax image of the XCAT phantom 21 with the nine tissue types shown in Fig. 2. The phantom image covered 40 × 40 cm 2 by 512 × 512 pixels, and geometrical textures were added to make the image pixel values inside organs heterogeneous. For contrast agent, we assumed that a dualphase injector is used in clinics and set its concentration in heart blood as 0.4% and 0.8%, which provides enhancements similar to clinical images. Because there is no information about the value's distribution of characteristic coefficients of tissue types in human organ, the geometrical textures were added in the following way; we randomly generated high or low density pixels corresponding to the tissue type each pixel belongs to, followed by blurring the image by Gaussian filter inside each organ region.

We simulated parallel beam projections with Poisson noise and the following parameters: tube voltage 140 kV, x-ray 10 5 counts per incident projection ray, 360 projections over 180 • , 728 detectors with 0.781 25 mm width, same as the width of the phantom image pixel, and four energy thresholds at 10, 40, 70, and 100 keV. We performed 100 noise realizations.

# 3.B. Reconstruction and tissue-type classification

First, material decomposition was performed to obtain two sinograms of the characteristic coefficients from the PCD data through Eqs. ( 23)-(28). Then, images of the characteristic coefficients were reconstructed using the following three methods: FBP, PML, and JE-MAP. The FBP images were used as an initial estimate for PML and JE-MAP. For tissue-type identification for FBP and PML, we employed pixel-based identification, i.e., for each image pixel, a tissue type is chosen which gives the minimum L2-norm distance FBP with a Shepp-Logan filter was performed on each of the two sinograms of the characteristic coefficients independently to obtain the corresponding image.

PML minimizes the negative Gaussian likelihood of the data in Eq. ( 24) with a quadratic regularizer R(W ) weighted by γ = 5 × 10 4 ,

JE-MAP was performed with β 1 = 6.0 × 10 4 , β 2 = 1.5, and β 3 = 1.0. We preset the expected values and covariance matrices of characteristic coefficients used in JE-MAP with the number of tissue types K = 9 and each latent variable corresponds to tissue type shown in Table II. The covariance matrix Σ k was sampled from the phantom and scaled by

Monochromatic CT images at 70 keV were synthesized from the characteristic coefficient images using Eq. ( 1). The parameters in JE-MAP are empirically searched. For better understanding of the role of the four terms in JE-MAP, we made the images which we changed only one of the four parameters β 1 , β 2 , β 3 , and β 4 at a time and qualitatively evaluated the image quality.

# 3.C. Quantitative evaluation

The standard deviation (SD), σ, of pixel values over 100 noise realizations was measured. The averaged value over adipose regions shown in Fig. 3(a) was used to measure the image noise.

The spatial resolution was quantified by fitting an error function to each horizontal edge profile in the region shown in Fig. 3

In Eq. ( 35), δ 3 indicates the sharpness of the edge, from which the full-width-at-half-maximum (FWHM) was calculated as FWHM = 2 √ 2ln2δ 3 . The FWHM was averaged over all profiles to obtain a measure for the spatial resolution. The trade-off between the image noise and spatial resolution was obtained by applying different Gaussian filters to the images and repeating the measurements.

The accuracy of the CT images was quantified by calculating the bias of the monochromatic CT images for each pixel, and the mean bias was calculated over the entire region inside the phantom. The accuracy of the tissue types was assessed in a binary fashion on a pixel basis. When the chosen tissue type for the image pixel was the correct tissue type, it was considered an accurate outcome; if it was not the correct tissue type, it was considered an inaccurate outcome. The ratio of the number of accurate outcomes to the number of image pixels is the accuracy of the tissue types.

# EVALUATION RESULTS

Figure 4 presents the estimated tissue types and monochromatic CT images at 70 keV from one noise realization and Fig. 5 shows profiles along the line shown in Fig. 4(f) for each reconstruction method. A strong salt and pepper noise can be seen in the FBP image [σ = 46.8 Hounsfield unit (HU) in entire phantom] which resulted in a salt and pepper pattern in the tissue type image as well. PML provided CT images with less noise (σ = 38.5 HU). However, it blurred the organ boundaries as shown in Fig. 5, which resulted in wrong tissue-type identification near the organ boundaries. For example, it can be seen that there is an adipose tissue identified at the boundaries between the heart muscle and the lung, or the heart muscle and the ventricles. JE-MAP reconstructed CT images with much less noise (σ = 27.4 HU), while the boundaries of organs remained sharp (Fig. 5) resulting in more accurate tissue-type identification at the boundaries. There are some regions in the tissue images of PML and JE-MAP where muscle and liver tissues were mislabeled because the characteristic coefficients of muscle and liver are too close to each other to be separated [see Fig. 2(e)].

The calculation of JE-MAP took 942.59 s for 33 iterations, while PML took 867.35 s for 33 iterations, using single Intel ® Xeon ® CPU E5-2643 v3 @ 3.40 GHz. Note that the present program codes have not been optimized in any way in the simulation.

Figure 6 presents JE-MAP images when one of the four parameters was smaller than the default setting used in Fig. 4, and Fig. 7 shows the images with larger parameters. The use of a smaller β 1 made the images heterogeneous but noisy [Figs. 6(a Figure 8 shows the bias and standard deviation of the CT images at 70 keV, and the accuracy of the tissue-type identification. The mean values were measured for each organ excluding pixels near the boundaries of organs and are presented together with the mean values of the entire phantom in Tables III-V. It can be seen that JE-MAP provided the best values in most indexes. The bias was as small as -0.1 HU with JE-MAP. The image noise of the entire phantom (Table IV) was 46.8 HU for FBP, 38.5 HU for PML, and 27.4 HU for JE-MAP. The accuracy of tissue types improved from 71.7% for FBP and 80.1% for PML to 86.9% for JE-MAP. The low accuracy of muscle with JE-MAP was attributed to the mislabeling as liver. The resolution-noise trade-off curves were shown in Fig. 9, where the top-left end-point of the curves was obtained from the images reconstructed by the corresponding method. JE-MAP provided the best trade-off performance.

# DISCUSSION AND CONCLUSION

We proposed a new framework, JE-MAP, to jointly perform image reconstruction, material decomposition, and tissuetype identification for photon counting x-ray CT. The results from 100 noise realizations showed that JE-MAP provided superior bias, standard deviation in homogeneous tissue regions (Tables III-V) to PML with quadratic penalty and FBP. However, JE-MAP showed larger standard deviation on the boundaries of tissues [Fig. 8(f)] which is usually observed in the PML method with edge-preserving penalty as well. The results from Fig. 9 showed that JE-MAP provided superior noise-resolution trade-off for the CT images to PML with quadratic penalty and FBP. This is because JE-MAP does not penalize differences between adjacent pixels at organ boundaries, while PML with quadratic penalty encourages smoothness even at edges. These results also indicate that the large standard deviation on the boundaries is caused not because JE-MAP blurs the boundaries but because the location of tissue boundaries varies for each noise realization while the edge is indeed maintained sharp as reported in Ref. 22.

A PML with edge-preserving penalty could perform better than that with quadratic penalty, and a comparison with JE-MAP would be of interest. We shall leave this for future study. However, we believe that JE-MAP has a greater potential than PML, because an edge-preserving penalty such as the Huber penalty 9 changes the strength of the penalty based on differences in pixel values, which are affected by image noise. It is a challenge to robustly suppress noise effectively while maintaining the true differences in adjacent pixel values. In contrast, JE-MAP obtains the information if the adjacent pixels are located at an organ boundary or inside an organ, and will change the strength of the penalty [see Eq. ( 13)]. We believe that this is a conceptual difference in the algorithm design. Moreover, JE-MAP could use more prior information about tissues in the human body via additional latent variables such as the location, the size, and the number of pixel groups with the same tissue type.

The accuracy of the tissue-type identification improved as well for JE-MAP compared to PML and FBP. While the tissue-type images based on FBP and PML images showed an isolated salt-and-pepper noise pattern, JE-MAP provided pixels with the same tissue type grouped together to form "islands." This is because JE-MAP honors the statistical relationship between the characteristic coefficients and the tissue types and those between neighboring pixels. Another advantage of JE-MAP is that the tissue-type identification is based on the projection likelihood rather than on information from image voxels. This means that JE-MAP can perform identification by placing more weight on the prior information if the reconstructed characteristic coefficients are not accurate due to large noise in the projection data. However, the current prior in JE-MAP cannot differentiate the tissue types whose characteristic coefficients are too close to each other or even overlapped. To differentiate them correctly, we will need to use prior information about the presence of tissue types such as the statistical atlas, which models the probability map of tissue types in human body. In the future work, the use of the evaluation metric that can be accounted for the similarities of the tissue types would be desirable.

A potential problem of JE-MAP with the current parameter setting is that it might suppress heterogeneous textures inside organs [Fig. 8(c)] or introduce a bias. We think this behavior can be attributed to suboptimal parameters such as β larger β 4 decreases the image noise as can be seen in Fig. 7(f), but at the expense of heterogeneous texture and bias. This discussion leads to another point: How to optimize several parameters of JE-MAP?

In this paper, we focused on finding a reasonable parameter to study the effect of the parameter values on the image quality. The question how to optimize the parameters remains a challenge, just like for other algorithms with multiple parameters. We envision that it would require both repeating the same procedures for various cases and using information theory to automatically weigh and balance the effect of each term and parameter. We shall leave this for future work as well.

The limitation of the current JE-MAP method is that it assumes that there exists only one tissue type in each voxel.  Two cases that would violate this assumption are the partial volume at organ boundaries and contrast-enhanced soft tissues. In the future work, we plan to address the issue while maintaining the framework of JE-MAP method. The partial volume problem at organ boundaries will be solved or mitigated by using finer voxels at boundaries. The contrast agent could be modeled by using a third basis function in material decomposition, which describes the attenuation coefficient of the contrast agent, although it could be challenging when the attenuation is large. In Ref. 23, the authors proposed a method similar to JE-MAP for dual-energy CT, which could potentially solve the partial volume problem. They assumed that each voxel contained at most three out of several possible tissue types and estimated the three tissue types and their volume fractions for each voxel using volume conservation as a constraint. A penalized-likelihood method with edge-preserving penalty for each material was used. The strength of this method is that by design, the tissue-mixture is modeled at any voxels. The weakness of the method is that the linear attenuation coefficient of each tissue type is deterministic and deviations from the expected value are modeled only by mixing other tissue types. In addition, similar to the problem with the conventional edge-preserving penalty discussed above, the penalty changes its strength based on differences in the volume fractions of each tissue type between adjacent voxels. Unlike JE-MAP, the change of (or the lack thereof) tissue types is not used to change the penalty strength.

As the number of tissue types in the object increases, the optimization of the cost function becomes more difficult in terms of calculation cost and increase of local minima. To deal with these optimization problems, we plan to perform a graded tissue-type identification, namely, we perform the identification along a preliminary defined tree structure where tissue type are categorized depending on their components' similarity. We may also need to perform image reconstruction and tissue-type identification alternatively in order to utilize more sophisticated image segmentation algorithm such as Graph Cut. 24 These improvements in optimization algorithm enable JE-MAP to find minima closer to global minimum with less calculation time, thus more reliably enhanced CT images and tissue-type distribution can be obtained.

In terms of the experimental setup, we need to further perform studies with different dose levels and different phantoms. For comparison, we need to perform reconstructions with other PML algorithms such as the Huber penalty as well as tissue-type identification with other MRF-based image segmentation algorithms, and evaluate them with other criteria such as the noise power spectrum or noise correlation in the image domain. We also need to change geometries from simple parallel beam to fan beam or cone beam. F. 9. Noise-resolution trade-off curves. The top-left point of each method is the values from the estimated images, and the curves are obtained by blurring each image with a Gaussian filter with various parameters.

We used the NIST database to calculate the expected value of human tissue types. However, these are just literature values and they may be quite different from the actual values in a particular patient. We will need to revisit our statistical relationship prior model parameters once we have better understanding and data of the distribution of each tissue's characteristic coefficients. After the implementation of PCD-CT in clinics, we plan to perform evaluations using real images, and collect distributions of characteristic coefficients for various tissue types. We will need to change our statistical relationship prior model depending on the shape of distribution of each tissue's characteristic coefficients.

At the present stage, we need to set all the tissue types which can possibly appear in the slices. However, we assume the number of tissue types does not become drastically large, if an appropriate tissue type database to be used can be chosen based on the location and protocol of scan. Moreover, using too many candidate tissue types with similar characteristic coefficients may introduce errors in tissue identifications as seen in our simulation result. Theoretically, such an error will lead to a wrong choice of priors, resulting in unexpected artifact, although it was not observed in our simulation. Thus, we will need to keep the number of tissue-type classes small and manageable by putting similar tissue types into one class if necessary, for example, in the simulation, putting muscle and liver tissue types into a class called "soft tissue."

The approach of JE-MAP method-estimating characteristic coefficients and tissue types jointly-can be applied to dual-energy CT by adjusting the data likelihood model. Furthermore, it can be applied to current single-energy CT by changing the variables from the characteristic coefficients to x-ray attenuation coefficients. We plan to develop JE-MAP methods for dual-energy CT and singleenergy CT and evaluate the performances using actual patient data.

Other future challenges of this study are as follows. First, as discussed above, we plan to improve a prior for tissue type and characteristic coefficients including the shape and size of organs, similar to statistical atlas, in order to identify tissue types more correctly. Second, we need to allow for multiple tissue types at a voxel to deal with partial volume effect at organ boundaries and iodine perfusion to tissues such as liver and kidney. Third, we need to include PCD degradation factors to the algorithm. This can be done in a straightforward fashion as long as the likelihood can be approximated as a multivariate Gaussian distribution.

where I is the identity matrix. Since each term in Eq. (B1) is a covariance matrix, H is positive-semidefinite, i.e., H ≽ 0; therefore, F| z (k ) i =1 is convex.

# ACKNOWLEDGMENTS

The authors thank Dr. Jeffrey A. Fessler for introducing us a paper, "Multi-Material Decomposition Using Statistical Image Reconstruction for Spectral CT," 23 and giving comments on how to express the mixture of materials. The authors appreciate editorial help by Dr. Jochen Cammin.

# APPENDIX A: DERIVATION OF EQS. (27) AND (28)

In this section, we derive the analytic solution for the minimization of the Kullback-Leibler divergence of a multivariate Gaussian distribution. The minimization of the Kullback-Leibler divergence over the expected vector ν j and covariance matrix P j of the multivariate Gaussian distribution can be described by extracting the terms including ν j and P j as

The values ν * j and P * j that minimize the Kullback-Leibler divergence are those where partial derivatives equal zero, ∂G ∂ν j = 0 ⇒ Eq. ( 27), (A3)

# APPENDIX B: CONVEXITY PROOF FOR EQ. (31)

In this section, we prove the convexity of the cost function in the ICM scheme F| z (k ) i =1 by calculating the Hessian matrix. We thank Fessler, for drawing our attention to Ref. 23, on which this part of the work is based. From Eq. (31), the Hessian matrix with respect to w i becomes

Medical Physics, Vol. 42, No. 9, September 2015

