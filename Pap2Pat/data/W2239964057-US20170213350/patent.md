# DESCRIPTION

## BACKGROUND

The design of an information processing system can be approached on multiple levels. FIG. 1 illustrates two levels of abstraction, namely, the algorithm level and the physical circuit level. On the algorithmic level, one studies procedurally how the information is processed independently of the physical realization. The circuit level concerns the actual realization of the algorithm in physical hardware, for example, a biological neural circuit or silicon circuits in a digital signal processor.

Visual motion detection is important to the survival of animals. Many biological visual systems have evolved efficient/effective neural circuits to detect visual motion. Motion detection is performed in parallel with other visual coding circuits and starts already in the early stages of visual processing. In the retina of vertebrates, at least three types of Direction-Selective Ganglion Cells (DSGC) are responsible for signaling visual motion at this early stage. In flies, direction-selective neurons are found in the optic lobe, 3 synapses away from the photoreceptors.

The small number of synapses between photoreceptors and direction-selective neurons suggests that the processing involved in motion detection is not highly complex but still very effective. In addition, the biological motion detection circuits can be organized in a highly parallel way to enable fast, concurrent computation of motion. It is also interesting to note that the early stages of motion detection are carried out largely in the absence of spiking neurons, indicating that initial stages of motion detection are preferably performed in the “analog” domain. Taking advantage of continuous time processing can be important for quickly processing motion since motion intrinsically elicits fast and large changes in the intensity levels, that is, large amounts of data under stringent time constraints.

Certain computer-based motion detection algorithms employ optic flow techniques to estimate spatial changes in consecutive image frames. Although, often time, optic flow estimation algorithms produce accurate results, the computational demand to perform many of these algorithms can be too high for real-time implementation.

Several models for biological motion detection are known. For example, the Reichardt motion detector for motion detection in insects uses a correlation method to extract motion induced by spatiotemporal information patterns of light intensity. Therefore, it uses a correlation/multiplication operation. The motion energy detector uses spatiotemporal separable filters and a squaring nonlinearity to compute motion energy and it was shown to be equivalent to the Reichardt motion detector. Work in the rabbit retina was used for the Barlow-Levick model of motion detection, which uses inhibition to compensate motion in the null direction. However, there exists a need for an improved motion detection technique.

## SUMMARY

According to aspects of the present disclosure, methods for motion detection are provided. An example method includes receiving data representing a time sequence of frames of a multi-dimensional signal and constructing a multi-dimensional Gaussian window. The method can further include dividing each frame of the received data into a plurality of blocks. The method can further include, for each block in the plurality of blocks, multiplying each pixel in the block with a corresponding pixel of the Gaussian window to obtain a windowed signal block, and computing the multidimensional FFT of the windowed signal block to obtain an amplitude and phase thereof. The method can further include detecting the occurrence of motion in the block based on the computed phase of the windowed signal block.

According to other aspects of the present disclosure, a system including a processor and memory is provided, in which the processor is programmed to carry out the above method. Further, a computer readable medium is provided, where the computer readable stores instructions that, when executed by a processor, cause the processor to carry out the above method.

## DETAILED DESCRIPTION

Images can be represented by their global phase alone. Provided herein are techniques for reconstructing visual scenes by only using local phase information, thereby demonstrating the spectrum of the representational capability of phase information.

The Fourier shift property suggests the relationship between the global shift of an image and the global phase shift in the frequency domain. This relationship is elevated by computing the change of local phase to indicate motion that appears locally in the visual scene. The local phases can be computed using window functions that tile the visual field with overlapping segments, making it amenable for a highly parallel implementation. In addition, a Radon transform-based motion detection index on the change of local phases is provided for the readout of the relation between local phases and motion.

Phase information has been largely ignored in the field of linear signal processing. Phase-based processing is intrinsically non-linear. However, phase information can be employed in speech processing and visual processing. For example, spatial phase in an image is indicative of local features such as edges when considering phase congruency.

As demonstrated herein, local phase information can be used to represent visual information in the absence of amplitude information. Accordingly, one or more embodiments of a local phase based algorithm to detect motion in visual scenes are provided. Examples and applications of the motion detection algorithm disclosed in relation to motion segmentation.

Complex valued transforms can be used for both representing and processing images. When represented in polar coordinates, the output of a complex valued transform of a signal can be split into amplitude and phase. In this embodiment, two types of phases of an image are defined: a global phase and a local phase. Both types of phases can faithfully represent an image. Accordingly, an example of a reconstruction algorithm that recovers the image from local phase information is provided. This indicates that phase information alone can largely represent an image or video signal. As disclosed herein, the use of phase for representing image and video information leads to efficient ways to implement certain types of image/video processing algorithms, for example, motion detection algorithms.

### Global Phase of Images.

The Fourier transform of a real valued image u=u(x,y), (x,y)ε2, is given by

{circumflex over (U)}(ωw,ωy)=u(x,y)e−j(ωx+ωy)dxdy

with {circumflex over (U)}(ωw,ωy)ε and (ωw,ωy)ε2.  (1)

In polar coordinates, the Fourier transform of u can be expressed as

{circumflex over (U)}(ωx,ωy)={circumflex over (A)}(ωx,ωy)ej{circumflex over (φ)}(ω,ω),  (2)

where A(ωx,ωy)εR is the amplitude and φ(ωx,ωy) is the phase of the Fourier transform of u.

The amplitude of the Fourier transform of an image u=u(x,y), (x,y)ε2, is called the global amplitude of u. The phase of the Fourier transform of an image u=u(x,y), (x,y)ε2, is called the global phase of u.

The global phase of an image plays a role in the representation of natural images. One example is to take two images and to exchange their global phases before their reconstruction using the inverse Fourier transform. The resulting images can be smeared but largely reflect the information contained in the global phase.

### Local Phase of Images

The global phase indicates the offset of sinusoids of different frequencies contained in the entire image. However, it is not intuitive to relate the global phase to local image features such as edges and their position in an image. To understand these local features, the Fourier transform can be modified such that it reflects properties of a restricted region of an image. The Short-Time (-Space) Fourier Transform (STFT) can be considered:

U(ωx,ωy,x0,y0)=u(x,y)w(x−x0,y−y0)·e−j(ω(x-x)+ω(y-y))dxdy,  (3)

where w=w(x,y), (x,y)ε2 is a real valued window function centered at (x0,y0) Certain choices of window functions include the Hann window and the Gaussian window. The (effectively) finite support of the window restricts the Fourier transform to local image analysis.

Similar to the Fourier transform, the STFT can be expressed in polar coordinates as

U(ωx,ωy,x0,y0)=A(ωx,ωy,x0,y0)ejφ(ω,ω,x,y),  (4)

where A(ωx,ωy,x0,y0)ε is the amplitude and φ(ωx,ωy,x0,y0) is the phase of the STFT.

The amplitude of the STFT of an image u=u(x,y), (x,y)ε2, is called the local amplitude of u. The phase of the STFT of an image u=u(x,y), (x,y)ε2, is called the local phase of u.

It should be noted that when w is a Gaussian window, the STFT of u evaluated at (ωx,ωy,x0,y0) can be equivalently viewed as the response of a complex-valued Gabor receptive field

h(x,y)=e−((x-x)+(y-y))/2σe−j(ω(x-x)+ω(y-y))  (5)

to u.

In this case, the window of the STFT is given by

w(x,y)=e−(x+y)/2σ.  (6)

Therefore, the STFT can be realized by an ensemble of Gabor receptive fields that are common in modeling simple and complex cells (neurons) in the primary visual cortex.

Reconstruction of Images from Local Phase

Amplitude and phase can be interpreted as measurements/projections of images that are indicative of their information content. When both the global amplitude and phase are known, the image can be reconstructed. The reconstruction calls for computing the inverse Fourier transform given the global amplitude and phase. Similarly, when using local amplitude and phase, if the sampling functions form a basis or frame in a space of images, the reconstruction is provided by the formalism of wavelet theory, for example, using Gabor wavelets.

Amplitude or phase represents partial information extracted from visual scenes. They can be obtained via nonlinear sampling, that is, a nonlinear operation for extracting the amplitude and phase information from images. The nonlinear operation can make reconstruction from either amplitude or phase alone difficult. However, certain images can be reconstructed from global or local amplitude information.

While computing the amplitude can require a second order (quadratic) nonlinearity, computing the phase calls for higher order nonlinear operators (Volterra kernels). However, one can reconstruct up to a constant scale an image from its global phase information alone without explicitly using the amplitude information.

Similarly, up to a constant scale, a bandlimited signal u=u(x,y), (x,y)ε2, can be reconstructed from its local phase alone. First the encoding of an image u is formulated by local phase, using the Gabor receptive fields as a special case. The problem can then be formulated with local phase computed from other types of STFTs.

Formally, an image, u=u(x,y), on the domain 2, is an element of a space of trigonometric polynomials  of the form

\(\begin{matrix}
{{{u\left( {x,y} \right)} = {\sum\limits_{l_{x} = {- L_{x}}}^{L_{x}}\; {\sum\limits_{l_{y} = {- L_{y}}}^{L_{y}}\; {c_{l_{x\;}l_{y}}{e_{l_{x}l_{y}}\left( {x,y} \right)}}}}},{where}} & (7) \\
{{e_{l_{x}l_{y}} = {{\exp \left( {{jl}_{x}\frac{\Omega_{x}}{L_{x}}x} \right)}{\exp \left( {{jl}_{y}\frac{\Omega_{y}}{L_{y}}y} \right)}}},{l_{x} = {- L_{x}}},\ldots \mspace{14mu},L_{x},{l_{y} = {- L_{y}}},\ldots \mspace{14mu},L_{y}} & (8)
\end{matrix}\)

are the set of basis functions of , Ωx, and Lx are the bandwidth and the order, respectively, of the space in the x dimension, and Ωy and Ly are the bandwidth and the order, respectively, of the space in the y dimension.

is a Reproducing Kernel Hilbert Space with inner product

u1,u2=∫[0,T]×[0,T]u1(x,y)dxdy,  (9)

where Tx=2πLx/Ωx, Ty=2πLy/Ωy are the period of the space in the x and y dimensions, respectively.

A bank of N Gabor receptive fields can be represented as

{ h kl , mn  ( x , y ) = kl  ( w  ( x , y )  e - j  ( ω x m  x + ω
y n  y ) ) , ( 10 ) }

where Tkl is the translation operator with Tklu=u(x−kb0,y−lb0), k, lεZ, b0>0, 0≦kb0≦Tx, and 0≦lb0≦Ty, and ωxm=mω0, ωyn=nω0, m, nε, ω0>0, −Ωx≦mω0≦Ωx, and −Ωy≦nω 0≦Ωy. The responses of the Gabor receptive fields to the input u(x,y) are given by

\(\begin{matrix}
{{{{\cdot {w\left( {{x - {kb}_{0}},{y - {lb}_{0}}} \right)}}e^{- {j{({{\omega_{x_{m}}{({x - {kb}_{0}})}} + {\omega_{y_{n}}{({y - {lb}_{0}})}}})}}}{dxdy}} = {A_{{kl},{mn}}e^{j\; \varphi_{{kl},{mn}}}}},} & (11)
\end{matrix}\)

where Akl,mn≧0, Akl,mnε, is the local amplitude and φkl,mnε[0,2π) is the local phase.

Dividing both sides of (11) by ejφresults in

\(\begin{matrix}
{{{u\left( {x,y} \right)}{{w\left( {{x - {kb}_{0}},{y - {lb}_{0}}} \right)} \cdot e^{- {j{({{\omega_{x_{m}}{({x - {kb}_{0}})}} + {\omega_{y_{n}}{({y - {lb}_{0}})}} + \varphi_{{kl},{mn}}})}}}}{dxdy}} = {A_{{kl},{mn}}.}} & (12)
\end{matrix}\)

Since Akl,mnε, we have

u(x,y)w(x−kb0,y−lb0)·cos(ωx(x−kb0)+ωy(y−lb0)+φkl,mn)dxdy=Akl,mn,  (13)

u(x,y)w(x−kb0,y−lb0)·sin(ωx(x−kb0)+ωy(y−lb0)+φkl,mn)dxdy=0.  (14)

It should be noted that w(x−kb0,y−lb0)sin(ωxm(x−kb0)+ωyn(y−lb0)+φkl,mn) is a real-valued Gabor receptive field with a preferred phase at φkl,mn+π/2−ωxmkb0−ωynlb0.

Assuming that the local phase information φkl,mn is obtained via measurements, that is, filtering the image u with pairs of Gabor receptive fields (10), the set of linear equations (14) can be interpreted as follows: the image u is orthogonal to the space spanned by the functions

w(x−kb0,y−lb0)·sin(ωx(x−kb0)+ωy(y−lb0)+φkl,mn),  (15)

where (k,l,m,n)ε with ={(k,l,m,n)ε4|0≦kb0≦Tx, 0≦lb0≦Ty, −Ωx≦mω0≦Ωx, −Ωy≦nω0≦Ωy}.

An embodiments of a reconstruction algorithm of the image from phase φkl,mn, (k,l,m,n)ε is provided herein. First, it should be noted that u can be reconstructed from φkl,nm, (k,l,m,n)ε as

\(\begin{matrix}
{{{u\left( {x,y} \right)} = {\sum\limits_{l_{x} = {- L_{x}}}^{L_{x}}\; {\sum\limits_{l_{y} = {- L_{y}}}^{L_{y}}\; {c_{l_{x\;}l_{y}}e_{l_{x}l_{y}}\left( {x,y} \right)}}}},{with}} & (16) \\
{{{\Phi \; c} = 0},} & (17)
\end{matrix}\)

where Φ is a matrix whose pth row and qth column entry are

[Φ]pq=w(x−kb0,y−lb0)·sin(ωx(x−kb0)+ωy(y−lb0)+φkl,mn)·ell(x,y)dxdy.  (18)

Here p traverses the set , and q=(2Ly+1)(lx+Lx)+(ly+Ly+1). c is a vector of the form

c=[c−L,−l,c−L,−L+1, . . . ,c−L,L,c−L+1,−L,c−L+1,−L+1, . . . ,c−L+1,L, . . . ,cL,−L,cL,−L+1, . . . ,cL,L]T  (19)

that belongs to the null space of Φ. A necessary condition for perfect reconstruction of u, up to a constant scale, is that N≧(2Lx+1)(2Ly+1)−1, where N is the number of phase measurements.

In FIG. 2, an example of reconstruction of an image is shown using only local phase information. The reconstructed signal is scaled to match the original signal. The SNR of the reconstruction is 44.48 dB. An alternative way to obtain a unique reconstruction is to include an additional measurement, for example, the mean value of the signal u(x,y)dxdy to the system of linear equations (14).

### The Global Phase Equation for Translational Motion

Let u=u(x,y,t), (x,y)ε2, tε, be a visual stimulus. If the visual stimulus is a pure translation of the signal at u(x,y,0), that is,

u(x,y,t)=u(x−sx(t),y−sy(t),0),  (22)

where

sx(t)=∫0tvx(s)ds,

sy(t)=∫0tvy(s)ds  (23)

are the total length of translation at time t in each dimension and vx(t) and vy(t) are the corresponding instantaneous velocity components, then the only difference between u(x,y,t) and u(x,y,0) in the Fourier domain is captured by their global phase.

Further, the change (derivative) of the global phase is given by

\(\begin{matrix}
\begin{matrix}
{\frac{d{\hat{\varphi}\left( {\omega_{x},\omega_{y},t} \right)}}{dt} = {{{- \omega_{x}}{v_{x}(t)}} - {\omega_{y}{v_{y}(t)}}}} \\
{{= {- {\left\lbrack {\omega_{x},\omega_{y}} \right\rbrack \left\lbrack {{v_{x}(t)},{v_{y}(t)}} \right\rbrack}^{T}}},}
\end{matrix} & (24)
\end{matrix}\)

where {circumflex over (φ)}(ωx,ωy,t) denotes the global phase of u(x,y,t){circumflex over (φ)}(ωx,ωy,0) is the initial condition.

### The Local Phase Equation for Translational Motion

The previous analysis applies to global motion. This type of motion occurs, e.g., when the imaging device, either an eye or a camera, moves. Visual motion in the natural environment, however, can be more diverse across the screen since it is, often time, produced by multiple moving objects. The objects can be small and the motion more localized in the visual field.

Taking the global phase of u does not easily reveal where motion of independent objects takes place or their direction/velocity of motion. The interpretation of motion by using the Fourier transform, however, can be applied for detecting local motion. This can be achieved by restricting the domain of the visual field where the Fourier transform is applied.

To be able to detect local motion, the local phase of u(x,y,t) is obtained by taking the STFT with window function w(x,y). It should be noted that the STFT and its ubiquitous implementation in DSP chips can be used in any dimension. For simplicity and without loss of generality, the window can be centered at (0,0). The STFT is given by

u(x,y,t)w(x,y)e−j(ωx+ωy)dxdy=A00(ωx,ωy,t)ejφ(ω,ω,t),  (27)

where A00(ωx,ωy,t) is the amplitude and φ00(ωx,ωy,t) the local phase.

The relation between the change in local phase and visual motion taking place across the window support can be explained as follows. First, if the stimulus can undergo a uniform change of intensity or it changes proportionally over time due to lighting conditions, for example, the local phase does not change since the phase is invariant with respect to intensity scaling. Therefore, the local phase does not change for such non-motion stimuli. Second, a rigid edge moving across the window support will induce a phase change.

For a strictly translational signal within the window support (footprint), for example,

u(x,y,t)=u(x−sx(t),y−sy(t),0), for (x,y)εsupp(w(x,y)),  (28)

where sx(t) and sy(t) are as defined in (23).

Further:

\(\begin{matrix}
{{{\frac{d\; \varphi_{00}}{dt}\left( {\omega_{x},\omega_{y},t} \right)} = {{\frac{{ds}_{x}(t)}{dt}\omega_{x}} - {\frac{{ds}_{y}(t)}{dt}\omega_{y}} + {b_{00}\left( {\omega_{x},\omega_{y},t} \right)}}},} & (29)
\end{matrix}\)

where, by abuse of notation, φ00(ωx,ωy,t) is the local phase of u(x,y,t) and φ00(ωx,ωy,0) is the initial condition.

It should be noted that the derivative of the local phase has similar structure to that of the global phase, but for the added term υ00. The first two terms in (29) can dominate over the last term for an ON or OFF moving edge. For example, FIG. 3 shows the derivative of the local phase given in (29) for an ON edge moving with velocity (40, 0) pixels/sec.

It should be noted that φ00(ωx,ωy,t) is not necessarily differentiable even if u(x,y,t) is differentiable, particularly when A00(ωx,ωy,t)=0. For example, the spatial phase can jump from a positive value to zero when A00(ωx,ωy,t) diminishes. This also suggests that the instantaneous local spatial phase is less informative about a region of a visual scene whenever A00(ωx,ωy,t) is close to zero. Nevertheless, the time derivative of the local phase can be approximated by applying a high-pass filter to φ00(ωx,ωy,t).

### The Block Structure for Computing the Local Phase

First, Gaussian windows along the x, y dimensions are constructed. The Gaussian windows are defined as

(klw)(x,y)=e−((x-x)+(x-y)/2σ,  (30)

where xk=kb0, yl=lb0, in which b0ε+ is the distance between two neighboring windows and 1≦kb0≦Px, 1≦lb0≦Py, where Px, Pyε+ are the number of pixels of the screen in the x and y directions, respectively.

The 2D Fourier transform of the windowed video signal u(x,y,t)(klw)(x,y) is taken and written in polar form

u(x,y,t)(klw)(x,y)e−k(ω(x-x)+ω(y-y))dxdy=Akl(ωx,ωy,t)ejφ(ω,ω,t).  (31)

The above integral can be evaluated using the 2D FFT in a discrete domain defined on M×M blocks approximating the footprint of the Gaussian windows. For example, the standard deviation of the Gaussian windows disclosed in the examples herein is 4 pixels. A block of 32×32 pixels (M=32) is sufficient to cover the effective support (or footprint) of the Gaussian window. At the same time, the size of the block is a power of 2, which can be suitable for FFT-based computation. The processing of each block (k,l) is independent of all other blocks; thus, parallelism is achieved.

It should be noted that the size of the window is informed by the size of the objects to be located. Measurements of the local phase using smaller window functions are less robust to noise. Larger windows can enhance object motion detection if the object size is comparable to the window size. However, there can be an increased likelihood of independent movement of multiple objects within the same window, which is not necessarily robustly detected.

Therefore, for each block (k,l), M2 measurements of the phase φkl(ωxm,ωym,t) are obtained at every time instant t, with (ωxm,ωym)ε2, where

2={(ωx=mω0,ωy=nω0),m,n=−M/2,−M/2+1, . . . ,M/2−1},  (32)

with ω0=2π/M. The temporal derivative of the phase is then computed, that is, (dφkl/dt)(ωx,ωy,t) for (ωx,ωy)ε2.

An example of the block structure is illustrated in FIG. 4. FIG. 4(a) shows an example of an image of 64×64 pixels. Four Gaussian windows are shown each with a standard deviation of 4 pixels. The distance between the centers of two neighboring Gaussian windows is 6 pixels. The solid square shows a 32×32-pixel block with k=3, l=3, which encloses effective support of the Gaussian window on top-left (k=0, l=0 is the block with Gaussian window centered at pixel (1,1)). The dashed square shows another 32×32-pixel block with k=3, l=7. The two Gaussian windows on the right are associated with the blocks k=7, l=3 and k=7, l=7, respectively. Cross section of all Gaussian windows with k=7, lε[0,10], are shown in FIG. 4(b).

The curves in FIG. 4(b) correspond to the two Gaussian windows shown in FIG. 4(a). FIG. 4(b) also suggests that some of the Gaussian windows are cut off on the boundaries. This is, however, equivalent to assuming that the pixel values outside the boundary are always zero, and should not affect motion detection based on the change of local phase.

Since the phase, and thereby the phase change, is noisier when the local amplitude is low, de-noising can be employed to discount the measurements of (dφk/dt)(ωx,ωy,t) for low amplitude values Akl(ωx,ωy,t). The de-noising is given by

\(\begin{matrix}
{{\frac{d\; \varphi_{kl}}{dt}{\left( {\omega_{x},\omega_{y},t} \right) \cdot \frac{A_{kl}\left( {\omega_{x},\omega_{y},t} \right)}{{\left( {1/M^{2}} \right){\sum_{{({\omega_{x},\omega_{y}})} \in ^{2}}{A_{kl}\left( {\omega_{x},\omega_{y},t} \right)}}} + \varepsilon}}},} & (33)
\end{matrix}\)

where ε>0 is a constant, and (ωx,ωy)ε2.

### The Phase-Based Detector

An embodiment of a block FFT based algorithm to detect motion using phase information is provided. This can be suitable for an in silico implementation.

### Radon Transform on the Change of Phases

The approximately linear structure of the phase derivative for blocks exhibiting motion is exploited by computing the Radon transform of (dφkl/dt)(ωx,ωy,t) over a circular bounded domain C={(ωx,ωy)|(ωx,ωy)ε2, ω2x+ω2y<π2}.

The Radon transform of the change of phase in the domain C is given by

\(\begin{matrix}
{{{\left( {\frac{d\; \varphi_{kl}}{dt}} \right)\left( {\rho,\theta,t} \right)} = {\int_{\mathbb{R}}{\frac{d\; \varphi_{kl}}{dt}\left( {{{{\rho \cdot \cos}\; \theta} - {s \cdot \; \theta}},{{{\rho \cdot \sin}\; \theta} + {{s \cdot \cos}\; \theta}},t} \right)1_{C}\left( {{{{\rho \cdot \cos}\; \theta} - {{s \cdot \sin}\; \theta}},{{{\rho \cdot \sin}\; \theta} + {{s \cdot \cos}\; \theta}}} \right){ds}}}},\mspace{20mu} {where}} & (34) \\
{\mspace{79mu} {{1_{C}\left( {\omega_{x},\omega_{y}} \right)} = \left\{ \begin{matrix}
1 & {{if}\mspace{14mu} \left( {\omega_{x},\omega_{y}} \right)C} \\
0 & {otherwise}
\end{matrix} \right.}} & \left( {3\; 5} \right)
\end{matrix}\)

The Radon transform ((dφkl/dt))(ρ,θ,t) evaluated at a particular point (ρ0,θ0,t0) is essentially an integral of (dφkl/dt)(ωx,ωy,t0) along a line oriented at angle π/2+θ0 with the ωx axis and at distance |ρ0| along the (cos(θ0), sin(θ0)) direction from (0,0).

If, for a particular k and l, (dθkl/dt)(ωx,ωy,t)=−vx(t)ωx−vy(t)ωy, then

\(\begin{matrix}
{{\frac{\left( {\left( {d\; {\varphi_{kl}/{dt}}} \right)} \right)\left( {\rho,\theta,t} \right)}{c\left( {\rho,\theta} \right)} = {\rho \left\lbrack {{{- {v_{x}(t)}}\cos \; \theta} - {{v_{y}(t)}\sin \; \theta}} \right\rbrack}},{where}} & (36) \\
{{c\left( {\rho,\theta} \right)} = {\int_{\mathbb{R}}{1_{C}\left( {{{{\rho \cdot \cos}\; \theta} - {{s \cdot \sin}\; \theta}},{{{\rho \cdot \sin}\; \theta} + {{s \cdot \cos}\; \theta}}} \right){{ds}.}}}} & (37)
\end{matrix}\)

c(ρ,θ) is a correction term due to the different length of line integrals for different values of (ρ,θ) in the bounded domain C.

After computing the Radon transform of (dφkl/dt)(ωx,ωy,t) for every block (k,l) at time t0, the Phase Motion Indicator (PMI) is computed. The PMI is defined as

\(\begin{matrix}
{{PMI}_{kl} = {\max\limits_{\theta \in {({0,\pi})}}{\sum\limits_{\rho}\; {{\frac{\left( {\left( {d\; {\varphi_{kl}/{dt}}} \right)} \right)\left( {\rho,\theta,t_{0}} \right)}{c\left( {\rho,\theta} \right)}}.}}}} & (38)
\end{matrix}\)

If the PMIkl is larger than a chosen threshold, motion is deemed to occur in block (k,l) at time t0.

Using the Radon transform enables separation of rigid motion from noise. Since the phase is sensitive to noise, particularly when the amplitude is very small, the change of phase under noise can have comparable magnitude to that due to motion. The change of phase under noise, however, does not possess the structure suggested by (29) in the (ωx,ωy) domain. Instead, the change is more randomly distributed. Consequently, the PMI value is comparatively small for these blocks.

Moreover, the direction of motion, for block (k,l) where motion is detected, can be computed as

\(\begin{matrix}
{{{\hat{\theta}}_{kl} = {{\pi\left( \frac{{{sign}\left( {\sum_{\rho > 0}{\left( {\left( {d\; {\varphi_{kl}/{dt}}} \right)} \right){\left( {\rho ,_{kl},t_{0}} \right)/{c\left( {\rho,\alpha_{kl}} \right)}}}} \right)} + 1}{2} \right)} + \alpha_{kl}}},\mspace{20mu} {where}} & (39) \\
{\mspace{79mu} {\alpha_{kl} = {\underset{\theta \in {({0,\pi})}}{argmax}{\sum\limits_{\rho}\; {{\frac{\left( {\left( {d\; {\varphi_{kl}/{dt}}} \right)} \right)\left( {\rho,\theta,t_{0}} \right)}{c\left( {\rho,\theta} \right)}}.}}}}} & (40)
\end{matrix}\)

FIG. 5 depicts an example phase-motion detection algorithm in accordance with one or more embodiments. The algorithm depicted can be implemented on a general purpose computer, such as a desktop, laptop, or notebook computer. Further, the algorithm can be implemented as a parallel algorithm, and is capable of exploiting parallel computing capabilities of high-speed servers. FIG. 6 depicts a schematic diagram of the operation of the phase-based motion detection algorithm. Each of the planes depicted in the figure corresponds to a step of the algorithm, and presents an in-progress view of a video frame on which the algorithm operates.

The algorithm shown in FIG. 5 can be subdivided into two parts. The first part computes local phase changes and the second part is the phase-based motion detector.

In the first part, a screen is divided into overlapping blocks. For example, the red, green, and blue blocks in the plane “divide into overlapping blocks” correspond to the squares of the same color covering the video stream. A Gaussian window is then applied on each block, followed by a 2D FFT operation that is used to extract the local phase. A temporal high-pass filter is then employed to extract phase changes.

In the second part of the algorithm, the PMI is evaluated for each block based on the Radon transform of the local phase changes in each block. Motion is detected for blocks with a PMI larger than a preset threshold, and the direction of motion is computed as in (39). The algorithm of FIG. 5 can be parallelized.

The algorithm depicted in FIG. 5 is based on the FFT. The algorithm can be modified by extending the FFT to higher dimensions. For example, this technique is applicable to 3D motion detection and segmentation.

According to one or more embodiments, an N-dimensional signal u(x1, . . . ,xn,t) is received and the N-dimensional STFT is applied. Window functions defined as

\(w_{k_{1}},\ldots \mspace{14mu},{{k_{n}\left( {x_{1},\ldots \mspace{14mu},x_{n}} \right)} = {ce}^{- \frac{{({x_{1} - x_{k_{1}}})}^{2} + \ldots + {({x_{n} - x_{k_{n}}})}^{2}}{2\sigma^{2}}}}\)

are constructed, where xki=kib0, kiε and b0>0. The scaling constant c guarantees that the windows approximately form a partition of unity. The N-dimensional FFT can then be applied on the windowed signal u(x1, . . . ,xn)wk1, . . . ,kn(x1, . . . ,xn). Motion in the higher N-dimensional space can then be extracted from local phase information.

In FIG. 7, an illustrative example depicting how motion is detected using the algorithm of FIG. 5 is provided. FIG. 7(a) depicts a still from a “highway video” evaluated at a particular time t0. In accordance with the algorithm, the screen in FIG. 7(a) is divided into 26×19 overlapping blocks and the window functions are applied to each block. Local phases can then be extracted from the 2D FFT of each windowed block, and the local phase changes are obtained by temporal high-pass filtering. The phase change is shown in FIG. 7(b) for all blocks, with block (12, 11) enlarged in FIG. 7(c) and block (23, 6) enlarged in FIG. 7(d). It should be noted that, at the time of the video frame, block (12, 11) covers a part of the vehicle in motion in the front, and block (23, 6) corresponds to an area of the highway pavement where no motion occurs.

FIG. 7(f) depicts, for each block (k,l), the maximum phase change over all (ωx,ωy)ε2. That is,

\(\begin{matrix}
{\max\limits_{{({\omega_{x},\omega_{y}})} \in ^{2}}{{{\frac{d\; \varphi_{kl}}{dt}\left( {\omega_{x},\omega_{y},t_{0}} \right)}}.}} & (41)
\end{matrix}\)

As shown in the figure, for regions with low amplitude, such as the region depicting the road, when the normalization constant is absent, the derivative of the phase can be noisy. For these blocks the maximum of |(dφkl/dt)(ωx,ωy,t0)| over all (ωx,ωy)ε2 is comparable to the maximum obtained for blocks that cover the vehicles in motion.

However, (29) illustrates that the local phase change from multiple filter pairs centered at the same spatial position (k,l) can provide a constraint to robustly estimate motion and its direction. Given the block structure employed in the computation of the local phase, phase change information from multiple sources is utilized.

Indeed, if, for a particular block (k,l), (dθkl/dt)(ωx,ωy,t)=−vx(t)ωx−vy(t)ωy, then (dφkl/dt)(ωx,ωy,t) will be zero on the line vx(t)ωx+vy(t)ωy=0 and have opposite sign on either side of this line. For example, in FIGS. 7(b) and 7(c), (dφkl/dt)(ωx,ωy,t0) exhibits this property for blocks that cover a vehicle in motion. The PMI is a tool to evaluate this property.

Finally, the PMIs for all blocks are shown compactly in a heat map in FIG. 6(e). The figure shows that the blocks corresponding to the two moving vehicles have a high PMI value while the stationary background areas have a low PMI value, enabling detection of motion by employing thresholding. This is also exhibited in the plane entitled “Radon transform and extract strength orientation of plane” in FIG. 6.

Relationship to Biological Motion Detectors. One way to implement local motion detectors is to apply a complex-valued Gabor receptive field (5) to the video signal u, and then take the derivative of the phase with respect to time or apply a high-pass filter on the phase to approximate the derivative.

An alternate implementation without explicitly computing the phase is provided herein. This implementation elucidates the relation between the phase-based motion detector disclosed earlier and some elementary motion detection models used in biology, such as the Reichardt motion detector and motion energy detector.

Assuming that the local phase θ00(ωx,ωy,t) is differentiable, then

\(\begin{matrix}
{{\frac{d\; {\varphi_{00}\left( {\omega_{x},\omega_{y},t} \right)}}{dt} = \frac{\begin{matrix}
{{\left( {{{db}\left( {\omega_{x},\omega_{y},t} \right)}/{dt}} \right){a\left( {\omega_{x},\omega_{y},t} \right)}} -} \\
{\left( {{da}{\left( {\omega_{x},\omega_{y},t} \right)/{dt}}} \right){b\left( {\omega_{x},\omega_{y},t} \right)}}
\end{matrix}}{\left\lbrack {a\left( {\omega_{x},\omega_{y},t} \right)} \right\rbrack^{2} + \left\lbrack \left( {\omega_{x},\omega_{y},t} \right) \right\rbrack^{2}}},} & (42)
\end{matrix}\)

where a(ωx,ωy,t) and b(ωx,ωy,t) are, respectively, the real and imaginary parts of A00(ωx,ωy,t)ejφ(ωx,ωy,t).

The denominator of (42) is the square of the local amplitude of u, and the numerator is of the form of a second order Volterra kernel. Thus, the time derivative of the local phase can be viewed as a second order Volterra kernel that processes two normalized spatially filtered inputs V1 and V2.

An well-known Reichardt motion detector is shown in FIG. 8. It is equipped with a quadrature pair of Gabor filters whose outputs are r1(t)=a(ωx,ωy,t) and r2(t)=b(ωx,ωy,t), respectively, for a particular value of (ωx,ωy). The pair of Gabor filters that provide these outputs are the real and imaginary parts of w(x,y)e−j(ωx x+ωy y). It also includes a temporal high-pass filter g1(t) and temporal low-pass filter g2(t). The output of the elaborated Reichardt detector follows the diagram in FIG. 8 and can be expressed as

(r2*g1)(t)(r1*g2)(t)−(r1*g1)(t)(r2*g2)(t).  (43)

The response can also be characterized by a second order Volterra kernel. It should be noted that there is a similarity between (43) and the numerator of (42). In fact, the phase-based motion detector shares some properties with the Reichardt motion detector. For example, a single phase-based motion detector is tuned to the temporal frequency of a moving sinusoidal grating.

Since the motion energy detector is formally equivalent to an elaborated Reichardt motion detector, the structure of the motion energy detector with divisive normalization is also similar to the phase-based motion detector.

The phase-based motion detection algorithm can be applied to video sequences to detect local motion. Further, the detected local motion can be used in motion segmentation tasks. In one embodiment, the algorithm can be implemented in PyCUDA and executed on an NVIDIA GeForce GTX TITAN GPU. In some embodiments, computations use single precision floating points. The phase-based motion detection algorithm can also be implemented in real-time using parallel computing devices. In some embodiments, the algorithm can be implemented on a fast GPU based on the FFT and Matrix-Matrix multiplication. Such operations can be implemented in hardware, for example, in FPGAs.

In certain embodiments, the disclosed motion detection algorithm can be applied to video sequences that do not exhibit camera egomotion. For these video sequences, the standard deviation of the Gaussian window functions can be set to 4 pixels and the block size can be set to 32×32 pixels.

### Examples of Phase-Based Motion Detection

A first video, illustrated in FIG. 9, is a viewpoint from a highway surveillance camera (“highway video”) under good illumination conditions and high contrast. The video has moderate noise, particularly on the road surface. The detected motion is shown in the top left panel of FIG. 9. The phase-based motion detection algorithm captures both the moving cars and the tree leaves moving (due to the wind). As shown, in the time interval between the 9th and 10th second, the camera was slightly moved left and rightwards within 5 frames, again possibly due to the wind. However, movement due to this shift is captured by the motion detection algorithm and the algorithm determines the direction of this movement. In this video, we already noted that this algorithm suffers from the aperture problem. For example, in front of the van where a long, horizontal edge is present, the detected motion is mostly pointing downwards. In addition to moving downwards, the edge is also moving to the left, however. This is expected since the algorithm only detects motion locally and does not take into account the overall shape of any object.

The range of the screen intensity is squeezed from [0, 1] to [0.2, 0.4], resulting in a video with a lower mean luminance and lower contrast. The motion detection results on the low-contrast video are shown in the bottom panels of FIG. 9. FIG. 9 shows that while the motion detection performance is degraded, the phase-based motion detector detects most of the moving vehicles.

A second video depicts the viewpoint of a surveillance camera in a train station (“train station video”). The video exhibits moderate room light with a low noise level. The front side of the video has high contrast; illumination on the back side is low. The detected motion is shown in the video of FIG. 10. As shown, movements of people are successfully captured by the motion detection algorithm.

A third video is a “thermal video” with a large amount of background noise (“thermal video”). In this example, the threshold for detecting motion is raised by approximately 60% in order to mitigate the increased level of noise. The detected motion is shown in the video of FIG. 11.

A fourth video depicts the viewpoint of a highway surveillance camera at night (“winterstreet video”). As shown, the overall illumination on the lower-left side is low whereas illumination is moderate on the upper-right side where the road is covered by snow. The detected motions are shown in the video in FIG. 12. It should be noted that car movements are successfully detected. Car movements on the lower-left side, however, suffer from low illumination and some parts of the car are not detected well due to the trade-off employed for noise suppression.

With a higher threshold, embodiments of the phase-base motion detection algorithm are able to detect motion under noisy conditions. This is depicted in FIGS. 13 and 14, in which Gaussian white noise with a standard deviation of 5% of the maximum luminance range has been added to the original “highway video” and “train station video.”

Motion Segmentation. The detected motion signals in the depicted video sequences can be useful for segmenting moving objects from the background. To this end, a larger threshold is applied to only signal motion for salient objects. The 32×32 blocks, however, introduce large boundaries around the moving objects. To reduce the boundary and to segment the moving object more closely to the actual object boundary, the motion detection algorithm can be applied around the detected boundary with 16×16 blocks. If 16×16 blocks do not indicate motion, then the corresponding area can be removed from the segmented object area.

FIG. 15 depicts a result of applying embodiments of the motion based segmentation on a 2-second segment of the “highway video.” With a higher threshold, the movement of the leaves is no longer picked up by the phase-based motion detector. Therefore, only the cars were identified as moving objects. Although the moving objects are not perfectly segmented on their boundary, they are mostly captured.

FIGS. 16-18 depict the results of applying the motion segmentation to a 2-second segment of the “train station video,” the “thermal video,” and the “winterstreet video,” respectively. As shown in FIG. 16, the segmentation results in the detection of people moving in the scene, as opposed to non-salient objects that can be detected. FIG. 17 also illustrates the segmentation of moving people, as opposed to non-salient objects, in the “thermal video” scene. Finally, FIG. 18 depicts the segmentation of moving cars in the “winterstreet video” scene, as opposed to non-salient objects that otherwise can be detected (such as smaller objects that are disturbed by wind movement). These results show that for the purpose of detecting local motion and its use as a motion segmentation cue, the local phase-based motion detector works as well as, if not better than, a simple thresholding segmentation using an optic flow based algorithm.

Although one or more embodiments have been described herein in some detail for clarity of understanding, it should be recognized that certain changes and modifications can be made without departing from the spirit of the disclosure. The embodiments described herein can employ various computer-implemented operations involving data stored in computer systems. For example, these operations can require physical manipulation of physical quantitiesusually, though not necessarily, these quantities can take the form of electrical or magnetic signals, where they or representations of them are capable of being stored, transferred, combined, compared, or otherwise manipulated. Further, such manipulations are often referred to in terms, such as producing, yielding, identifying, determining, or comparing. Any operations described herein that form part of one or more embodiments of the disclosure can be useful machine operations. In addition, one or more embodiments of the disclosure also relate to a device or an apparatus for performing these operations. The apparatus can be specially constructed for specific required purposes, or it can be a general purpose computer selectively activated or configured by a computer program stored in the computer. In particular, various general purpose machines can be used with computer programs written in accordance with the teachings herein, or it can be more convenient to construct a more specialized apparatus to perform the required operations.

The embodiments described herein can be practiced with other computer system configurations including hand-held devices, microprocessor systems, microprocessor-based or programmable consumer electronics, minicomputers, mainframe computers, and the like.

One or more embodiments of the present disclosure can be implemented as one or more computer programs or as one or more computer program modules embodied in one or more computer readable media. The term computer readable medium refers to any data storage device that can store data which can thereafter be input to a computer system—computer readable media can be based on any existing or subsequently developed technology for embodying computer programs in a manner that enables them to be read by a computer. Examples of a computer readable medium include a hard drive, network attached storage (NAS), read-only memory, random-access memory (e.g., a flash memory device), a CD (Compact Discs)—CD-ROM, a CD-R, or a CD-RW, a DVD (Digital Versatile Disc), a magnetic tape, and other optical and non-optical data storage devices. The computer readable medium can also be distributed over a network coupled computer system so that the computer readable code is stored and executed in a distributed fashion.

Although one or more embodiments of the present disclosure have been described in some detail for clarity of understanding, it will be apparent that certain changes and modifications can be made within the scope of the claims. Accordingly, the described embodiments are to be considered as illustrative and not restrictive, and the scope of the claims is not to be limited to details given herein, but can be modified within the scope and equivalents of the claims. In the claims, elements do not imply any particular order of operation, unless explicitly stated in the claims.

Many variations, modifications, additions, and improvements can be made. Plural instances can be provided for components, operations or structures described herein as a single instance. Boundaries between various components, operations and data stores are somewhat arbitrary, and particular operations are illustrated in the context of specific illustrative configurations. Other allocations of functionality are envisioned and can fall within the scope of the disclosure(s). In general, structures and functionality presented as separate components in exemplary configurations can be implemented as a combined structure or component. Similarly, structures and functionality presented as a single component can be implemented as separate components. These and other variations, modifications, additions, and improvements can fall within the scope of the appended claim(s).

