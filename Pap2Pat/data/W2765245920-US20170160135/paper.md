# INTRODUCTION

"Spectral imaging" (SI) refers to the acquisition of the threedimensional (3D) spectral cube of spatial and spectral data of a source object at a limited number of wavelengths in a given wavelength range. SI has a multitude of applications in many fields (Brady, 2009), including biology (Garini et al., 2006), medicine (Uhr et al., 2012), food inspection (Long et al., 2005), archaeology, art conservation (Lang, 2012), astronomy and remote sensing (Foster et al., 2006). SI with mosaic spectral filter arrays on the image sensor (Themelis et al., 2008) leads to substantial light gathering losses. In "staring" or "pushbroom" SI systems (Carlsohn, 2006), removable sets of narrow bandpass filters (Long et al., 2005) or time-sequential dynamic spectral filters (López-Álvarez et al., 2008) slow the SI process and cannot apply it to dynamic, fast changing objects. Modern trends in digital imaging (Brady, 2009) resort to a generic combination of optics with digital processing and to compressed sensing (CS) (Donoho, 2006, Candès et al., 2006) for various purposes and applications. CS-based algorithms already have many applications in astronomy, biology, medicine, radar and seismology (Stern et al., 2008, Willet et al., 2011). "Snapshot spectral imaging" (SSI) refers to the instantaneous acquisition of the spectral cube, a process suitable for fast changing objects. There are several known SSI devices/architectures that demonstrate the progress and high potential of SSI. In particular, the Coded Aperture Snapshot Spectral Imager (CASSI) (Wagadarikar et al., 2008) designs use an intermediate image plane and a coded aperture. The coded aperture can be a binary mask, a gray-scaled coded mask (Rueda-Chacon et al., 2013), or a spatial-light modulator (Yuan et al., 2015). These designs yield 2D coded measurements on the sensor array, from which the spectral cube is reconstructed using CS algorithms.

The need for intermediate image formation optics (in addition to regular components of a digital camera) in several of the referenced devices, increases the total track length, the weight and the production costs of such SSI devices. In order to convert a regular digital camera to an SSI camera for arbitrary objects, we resort here to (i) a diffusing and dispersing "phase-only" static optical element at the entrance pupil, and (ii) tailored CS methods for digital processing of the diffused and dispersed (DD) image recorded on the image sensor. The limited volume of data in the DD image acquired by a 2D image sensor in a single snapshot poses a problem for the reconstruction of a 3D spectral cube. To overcome this limitation and to enable SSI, we resort to compression of spatial data in multispectral images with the aid of CS-based reconstruction algorithms. The diffuser is designed to mix the spectral cube data spectrally and spatially and thus to enable convergence in its reconstruction by CSbased algorithms. We demonstrate the feasibility of reconstructing experimental SSI images with a relatively straightforward linear iterative process of "split Bregman iterations" (SBI) (Goldstein et al., 2009, Cai et al., 2009).

# SPECTRAL IMAGING WITH A DISPERSIVE DIFFUSER

## Continuous Model of the Optical System

A schematic layout of the spectral imaging system with monochromatic image sensor, a pupil-domain diffuser and compressed sensing is shown in Figure 1. The system (Golub et al., 2016) includes elements of a regular digital camera such as an imaging lens, a monochromatic image sensor, a bandpass spectral filter, the transparent diffuser at the entrance pupil, as well as a digital processor, which also enables conversion of the spectral cube to RGB color coordinates.

The International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences, Volume XLII-3/W3, 2017 Frontiers in Spectral imaging and 3D Technologies for Geospatial Solutions, 25-27 October 2017, Jyväskylä, Finland Figure 1. Optical scheme of a spectral and color imaging optical system based on a digital camera and a diffuser.

To succeed in image reconstruction, modern CS theory requires a highly randomized system response. Classical spectroscopic systems comprise a dispersive optical element like a prism or a diffraction grating. In order to minimize the required number of optical elements and to restrict our imager design to a modification of standard digital cameras, we decided to combine dispersive and diffusing properties required from the added optical element in a single diffuser. We assume that the entrance pupil is located in front of the imaging lens. The diffuser is positioned at the "pupil domain", i.e., entrance pupil or the system aperture of the imaging lens and works as a random dispersing element that provides the DD image at the monochromatic image sensor. A digital processor processes the DD image to reconstruct a plurality of monochromatic images (i.e., the spectral cube) of the source object through iterative CS-based algorithms.

While the diffuser was designed for wavelength des l , other wavelengths in the entire spectral range are incident on it. The diffuser (Golub et al., 2016)  for the diffuser's phase function was a randomly permutated, nonlinear saw-tooth phase. Figure 2 illustrates a portion of the diffuser's phase profile. The diffuser provides wavelengthdependent light diffusion and accordingly serves also as an inherent disperser. Therefore, it provides spectral multiplexing along with spatial multiplexing. We assumed that before introduction of the 1D diffuser, the imaging system was spatially shift invariant and its optical resolution was matched to the sensor pixel pitch. When installed into the SI optical system, the diffuser modifies the system pupil function of the entire SI optical system towards ( ) ( )

Accordingly, the coherent PSF can be calculated as an inverse Fourier transform

where ( )  wavelength range. A discrete version of the spectral cube in each spectral band can be expressed by the y N N L ´´ matrix:

where spectral cube voxels can be expressed as

The continuous 1D convolution in Equation ( 4) is converted into a discrete convolution applied separately to each of y N image rows. Discrete pixels of the DD image at the th l wavelength and at a given row j can be expressed as a discrete 1D aperiodic convolution

,

).

# I h x -x;l ¢

Note that in our model with a 1D diffuser, each ¢ = j j row of the DD image is in one-to-one correspondence with a respective th j row of the spectral cube. The contribution of polychromatic light to discrete pixels of the DD image is denoted as ( ) j i Y ¢ and can be expressed as a sum of the intensities of monochromatic DD images ( )

At each image pixel, the sum can be expressed as

where non-negative numbers l k characterize the overall relative spectral sensitivity of the image sensor and the optical transmission of the optical components of the system at wavelength l l , and where coefficients

describe the effect of the diffuser scaled with the relative spectral sensitivity of the optical system. For mathematical considerations, it is convenient to concatenate the spectral and vertical spatial dimensions of the spectral cube to a matrix X with dimensions

such that each spectral dimension is described by a sub-matrix l X of size y N N

´. We define an x

# N NL

´

which may be treated as a block rectangular matrix

´ each. Each sub-matrix l A corresponds to a single wavelength and features the randomization originating from the diffuser. The 2D DD image is represented as a matrix Y of size

X is a single column vector from the concatenated spectral cube to be reconstructed from the single column sensed vector ( )

X represents the spectral data to be reconstructed from DD image . Y Equation ( 8) can now be expressed in matrix form as the multiplication of a vector of length N L over a matrix of size x

# N NL

´. The multiplication results in a vector of a smaller length x N ( )

For efficient 2D data processing, Equation ( 13) can be expressed in matrix form as the multiplication of matrix X of size ´, A = X Y (14) as customary in CS theory.

## Sparse Representation and Reconstruction

Equation ( 14) provides the CS model for our spectral imaging system. It shows that the recorded DD image Y includes a linear mixture of spectral and spatial data of the entire spectral cube X , as described by the sensing matrix .

A The CS problem consists of the reconstruction of matrix X in such a way that Equation ( 14) with a given matrix Y becomes satisfied. The number x y

# N N

´ of equations for Y in Equation ( 14) is less than the number of unknown variables y N L N ín . X To obtain a sensible solution, we have to impose some constraints on the spectral cube to be reconstructed. The commonly chosen constraint in CS is sparsity. The latter originates from a well-established fact that typical 2D digital images have a sparse representation in wavelet and wavelet-frame domains. Consequently, spectral cubes, which are collections of monochromatic images, possess the same property, i.e. they can be represented by collections of sparse matrices that contain many zeros. Therefore, in accordance with the CS theory, we look for a solution of Equation ( 14) that is maximally sparse in a wavelet-frame domain. The mathematical relation between spectral cube matrix X and its sparse representation d (having only a relatively small number of non-zero elements) can be represented as a linear transform D = d X , with a "sparsifying" matrix . D Then, d is the transform coefficients array. The sparse representation may be implemented by resorting to the 2D frame transforms (Averbuch et al., 2014). Another option is the 3D wavelet transform, where the 2D transforms are applied to the monochromatic images and 1D transform is applied to the cube comprised of the 2D transform coefficients matrices along the spectral dimension. The spectral-dimension wavelet transform provides an additional sparseness of the representation because spectra in each pixel are changing smoothly from one band to another. For the wavelet transforms, the biorthogonal wavelets derived from the discrete splines of 12-th order were utilized (Averbuch et al., 2014). We denote by Y the matrix of the inverse 2D (3D) frame (wavelet) transform, such that spectral cube X can be restored from its sparse representation d by X d

Equation ( 14) can be expressed in the form

Where

The CS theory (Donoho, 2006, Candès et al, 2006) addresses the feasibility for reconstruction of sensible solution of Equation ( 16) for a special case of K-sparse matrices or vectors d that have only K non- zero elements. It is known that the K-sparse sensible solution d of Equation ( 16) (and consequently X of Equation ( 14)) exists and can be reconstructed for a class of matrices Q that satisfy a RIP condition of order K. The RIP condition of order K in CS (Candès et al, 2006) demands that any sub-matrix of Q formed by less than K columns must satisfy the inequality:

(1 ) (1 )

for any K-sparse vector d , where 0 K d > is some small number. In order to reconstruct the sparse representation d of the spectral cube X from the DD image Y, we resorted to split Bregman iterations (SBI) (Goldstein et al., 2009, Cai et al., 2009). Specifically, d was reconstructed as a solution of the following constrained minimization problem:

with conditions:

we mean the Frobenius norm, and the

The minimization problem is equivalent to minimization of a functional

where , µ c are Lagrange weight coefficients.. In particular, coefficient c weights the sparsity level of d, and coefficient µ weights the fit of AX to Y . Following (Shen, 2010), a closed loop of the iterative algorithm uses a feedback from the 1 l error and a shrinking operation that ensures a sparse reconstruction. In more detail, the minimization of the functional in Equation ( 20) is performed by an iterative process:

)

where k is the number of the iteration, k b and k c are intermediate vectors used to execute iterations,

is the function applied to each vector component. The iterations are terminated once the inequality

is achieved, or after a given number of iterations. The parameter s is determined by the noise level on the sensor array.

# EXPERIMENTAL OPTICAL ARRANGEMENT AND CALIBRATION

The concept of our CS-based SSI camera was proven for L =33 wavelength bands in an optical experiment that used a regular digital camera equipped with a monochromatic (without color filters array) image sensor, a diffuser, and specialized digital image processing capabilities, as shown in Figure 1 The actual diffuser design used in our experiments had a 3.2mm clear aperture that matched the entrance pupil and included d N = 400, u D =8µm wide stripes, as illustrated in Figure 2.

In order to obtain a more accurate model of our physical system, we performed direct calibration of the SSI camera by direct point-spread function (PSF) measurements that provided the sensing matrix. An object with single thin white vertical column displayed on the iPad screen was imaged in the dark at several spatial positions in each spectral band. Separated spectral bands for the calibration were achieved by resorting to a set of L =33 Thorlabs narrow-bandpass 10nm FWHM spectral filters that covered the 400-720nm wavelength range in equal gaps of 10nm and which were mechanically integrated in filter wheels. To have a firm reference for spectral cube reconstruction in our experiments, we conducted direct reference measurements of the spectral cube of size 256 256 33

for the object of interest. In addition, spectral calibration procedure was performed in order to correct non-ideal aspects, such as the white line's spectrum used for the PSF measurements and the non-uniform transmittance of the bandpass filters.

# OPTICAL EXPERIMENT FOR SPECTRAL IMAGING

An exemplary "Color Checker" test object was used, among others, for optical SSI experiments. This was created on the iPad screen mounted on the optical bench in the arrangement of Figure 1, at a fixed distance of 88cm in front of the imaging lens. The reference spectral cube measurements, the PSF measurements and the grayscale snapshots of the DD image were recorded on the image sensor in the dark, with the diffuser in place. The digital reconstruction of the spectral cube was performed using the SBI process with a measured sensing matrix A and optimized iteration parameters , µ c . Two reconstruction methods were considered: 1) 2D frame transforms of the monochromatic images, 2) 3D wavelet transforms of the spectral cubes. For this, the biorthogonal wavelet and tight and semi-tight frame transforms derived from polynomial and discrete splines were tested. The diverse libraries of such transforms were designed in (Averbuch et al., 2014). The experimental results demonstrated below are produced by using the 2D semi-tight frame transform derived from the quasiinterpolating polynomial splines and the biorthogonal 3D wavelet transform derived from the twelfth-order discrete splines.

Quality evaluation of the reconstructed spectral cube X was done by comparison to the reference spectral cube X , which was measured directly with the set of L=33 bandpass filters. We expressed the normalized root-mean-square errors (RMSE) of the full spectral cube as

where

X . Then, we calculated the peak signal-to-noise ratio (PSNR) as

Similarly, we have performed a quality evaluation of the monochromatic images per each wavelength, the spectra per each spatial coordinate and the RGB image, all derived from the reconstructed spectral cube. The RGB conversion was done in accordance with the CIE standard observer color matching functions implemented by Matlab function "RGB_from_Spectral_cube" (Foster, 2017).

Figure 3 shows images that correspond to the "Color Checker" object. Figure 3(a) shows the original object displayed on the iPad, Figure 3(b) shows the RGB image calculated from direct measurements with the 33 bandpass filters, and Figure 3(c) shows the DD image recorded at the monochromatic image sensor with 10.6ms integration time. Note that this time is substantially smaller than the 80.8 x 33=2666 ms needed for use of 33 bandpass filters, for a given peak signal of 90% of the sensor's saturation level. Such small integration time provides one major advantage of SSI over time-sequential acquisition methods. Figure 3(d) and 3(e) show the RGB images built from the reconstructed spectral cubes, obtained with the 2D framelet and 3D wavelet reconstruction methods, respectively. For the RGB images, the calculated PSNR RGB (RMSE RGB values in brackets) values of the obtained with the 2D framelet reconstruction method are 17.67 (0.049), and for the 3D wavelet reconstruction method are 15.92 (0.16). Figure 4 shows five out of 33 monochromatic images extracted from the spectral cubes at wavelengths 450 nm, 540 nm, 570 nm, 610 nm and 650 nm.  PSNR λ values as functions of wavelength for the monochromatic images that were CS reconstructed using the 2D framelet method (blue) and 3D wavelet method (dashed green).  Some shifts and missing peaks in the spectra and RGB values could be caused by a mismatch between the measured sensing matrix and the actual physical sensing matrix of the optical system with the diffuser, as well as due to the presence of actual noise in the experimental system. The PSNR i,j (RMSE i,j in brackets) values of the spectra at the marked points 1-8 for the 2D framelet transform are 10. 24 (0.31), 11.2 (0.28), 11.74 (0.26), 11.99 (0.25), 15.52 (0.17), 12.11 (0.25), 10.83 (0.29) and 10.48 (0.3), whereas for the 3D wavelet transform the values are 14.34 (0.19), 14.26 (0.19), 15.72 (0.16), 11.08 (0.27), 14.31 (0.19), 17.73 (0.13), 11.56 (0.26) and 10.21 (0.31). To conclude, the 3D wavelet method exhibits smaller error for the entire spectral cube compared to the 2D framelet method. In particular, it yields an improvement in the spectral reconstruction in certain spatial coordinates. It is, however, inferior in the reconstruction quality of some of the monochromatic wavelength images, as well as in the quality of the reconstructed RGB image. 

# SIMULATIONS WITH SPECTRAL CUBE OBTAINED WITH VTT SPECTRAL IMAGER

In order to expand the analysis of the suggested concept, we have performed computer simulations using a spectral cube obtained with a VTT spectral imager prototype. This spectral imager, provided by Jyväskylä University (JyU), is integrated with a piezo-driven Fabri-Perot Interferometer (FPI), which enables time sequential scanning of the spectral domain, in the range of 400-1000 nm. The spectral cube was acquired from the human skin tissue with a suspected Melanoma tumor. A method to delineate the skin area affected by a tumor using the VTT spectral imager was reported in (Zheludev et al., 2015). The spectral cube's original dimensions, which was imaged in the 460-850nm range, were 1200 1920 120 ´´. In order to incorporate the skin spectral data into the above computational scheme and, at the same time, to significantly reduce the noise inherent in the data, the following preprocessing operations were carried out: 1) The original cube was spatially cropped to the size 1024 1024 120 ´´and padded by zeros to a cube of size 1024 1024 132 ´´, denoted as . CRC 2) A two-level 3D biorthogonal wavelet transform was applied to the cube . CRC The wavelet transform coefficients filled a cube denoted by CΤC , of size 1024 1024 132, ´´where the sub-cube denoted by LLL of size 256 256 33, ´´comprised the coefficients produced by low-pass filtering in all three dimensions. 3) The sub-cube , LLL which presents a smoothed and down-sampled by factor of 4 copy of the cube , CRC was selected for further processing. Recall that the last three planes of the sub-cube LLL comprise all zeros.  The sensing matrix A was generated by performing theoretical PSF calculation in the wavelengths of interest, assuming that our system is equipped with a nominal phase profile diffuser.

The sensor image Y was calculated according to Equation ( 14) and multiplied with a matrix R consisting of randomly distributed plus-and minus-ones. Correspondingly, columns of the sensing matrix A were multiplied by the matrix R . Our assumption that the reduction of the sensing matrix coherency can improve the reconstruction results, was corroborated by the simulations. For the simulation, we used the 2D framelet reconstruction method. Figure 7(a) shows pseudo-color representation of the "Skin Tissue" reference spectral cube.  

# DISCUSSION AND CONCLUSIONS

We showed experimentally and by simulations the feasibility of snapshot spectral imaging with a regular digital camera complemented by a minor hardware addition in the form of a single phase-only static diffuser. Our phase-modulation architecture removes the need for intermediate image plane optics and/or spatial light modulators. This can lead to a real miniaturization of SSI cameras, thus providing significant advantages in applications where weight, volume and/or price are critical. The key element of our optical system is a diffuser designed to create a randomized sensing matrix built from calibration measurements of the PSF. The use of a monochromatic sensor, instead of a regular mosaic color sensor, increases the captured light amount and, therefore, the sensitivity of the camera. Successful acquisition of RGB images by a fully monochromatic image sensor is another important result.

Our method relies substantially on spatial and spectral mixing at the image sensor and subsequent reconstruction of the cube with CS-based algorithms. It demonstrated the ability to reconstruct both spectral and spatial data from spatial-only data acquired by a monochromatic image sensor. This is achieved by proper use of the sparsity property, naturally attributed to photographic images. We believe that one of the major advantages in our reported development is the resorting to specific wavelet and frame transforms designed in  (Averbuch et al., 2014), which provide the efficient conversion of the spectral cubes into their sparse representation.

Results of this work may have applications in miniaturized snapshot spectral imagers of dynamic objects in such fields as remote sensing and astronomy, biology, environmental studies, agriculture, food and drug inspection, automotive and vehicle sensors, medical diagnostics, photographic and video cameras, smartphones, wearable devices and augmented reality.

# ACKNOWLEDGEMENTS

This research was partially supported by the Israel Ministry of Science, Technology and Space no. 3-13601.

