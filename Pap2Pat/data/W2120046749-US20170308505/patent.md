# DESCRIPTION

## FIELD OF INVENTION

The present invention relates to system for automated detection of critical transitions and, more particularly, to a system for automated detection of critical transitions using predicted system trajectories.

## BACKGROUND OF INVENTION

One central characteristic of complex social-technological systems is their self-organized emerging interactions which provide the benefits of exchanging information and resources effectively, yet at the same time increases the risk and pace of spreading attacks or failures. A small perturbation on a complex system operating in a high-risk unstable region can induce a critical transition that leads to unstoppable catastrophic failures.

There are a few recent works of early warning signals for heterogeneously networked dynamical systems. Kwon and Yang (see the List of Incorporated Cited Literature References, Literature Reference No. 1) use transfer entropy to analyze financial market data. They calculate pair-wise transfer entropy to form a transfer entropy matrix and demonstrate the asymmetrical influence from mature markets to emerging markets using transfer entropy. Their method estimates global transfer entropy, not local transfer entropy changing in time; therefore, their method cannot handle dynamics and structure changes in directional influence.

Staniek and Lehnertz (see Literature Reference No. 4) introduced a robust and computationally efficient method to estimate transfer entropy using a symbolization technique. Their demonstration of symbolic transfer entropy (STE) on brain electrical activity data shows STE is able to detect the asymmetric dependences and identify the hemisphere containing the epileptic focus without observing actual seizure activity. However, their emphasis is also not on identifying the dynamics of the complex system structure.

Scheffer et al. (see Literature Reference No. 5) surveys state-of-the-art methods that originated in the ecological domain. These methods focus only on homogeneous lattices with signals such as increased temporal correlation, skewness, and spatial correlations of the population dynamics, thus are not able to deal with heterogeneously networked dynamical systems.

Moon and Lu (see Literature References No. 2 and 3) developed a spectral early warning signals (EWS) theory that detects the approaching of critical transitions and can estimate the system structure and network connectivity near critical transitions using the covariance matrix. Although spectral EWS quantifies how much entities of a system are moving together, the symmetric nature of covariance spectrum does not permit the analysis of directional influences among entities.

Thus, a continuing need exists for a system for automated detection of critical transitions in heterogeneously networked dynamical system using an information dynamic spectrum framework that permits analysis of directional influences among entities.

## SUMMARY OF INVENTION

The present invention relates to system for predicting system trajectories toward critical transitions. The system comprises one or more processors and a memory having instructions such that when the instructions are executed, the one or more processors perform multiple operations. A set of multivariate time series of observables of a complex system is transformed into a set of symbolic multivariate time series. Pair-wise series of a transfer entropy (TE) measure are determined. An associative transfer entropy (ATE) measure is determined. The ATE measure is comprised of an ATE+ positive influence class and an ATE− negative influence class. Then, ATE+, TE, and ATE− trajectories are estimated over time. Finally, a critical transition in the complex system is predicted using at least one of the ATE+, TE, and ATE− trajectories.

In another aspect, the system estimates the TE trajectory by the natural logarithm (ln) with an unknown coefficient a and a constant c according to the following:

g(t)=a ln(t)+c,

where t represents time.

In another aspect, the system estimates the unknown coefficient a with various discrete time steps by taking the derivative of g(t)=a ln(t)+c to obtain

\({{^{\prime}(t)} = \frac{a}{t}},\)

then obtaining a discretized version of the unknown coefficient a according to the following:

\(\frac{\Delta }{\Delta \; t} = {a{\frac{1}{t}.}}\)

In another aspect, the system determines the unknown coefficient a according to the following:


- - for a fixed timestep Δt in a window \[T_(start), T_(end)\],
    determining the following matrix equation:

\({{\begin{bmatrix}
\frac{1}{t_{1} + {\Delta \; t\text{/}2}} \\
\frac{1}{t_{2} + {\Delta \; t\text{/}2}} \\
\vdots \\
\frac{1}{t_{k} + {\Delta \; t\text{/}2}}
\end{bmatrix}a} = \begin{bmatrix}
\frac{{\left( {t_{1} + {\Delta \; t}} \right)} - {\left( t_{1} \right)}}{\Delta \; t} \\
\frac{{\left( {t_{2} + {\Delta \; t}} \right)} - {\left( t_{2} \right)}}{\Delta \; t} \\
\vdots \\
\frac{{\left( {t_{k} + {\Delta \; t}} \right)} - {\left( t_{k} \right)}}{\Delta \; t}
\end{bmatrix}},\)

where t1, . . . , tk+Δtε [Tstart, Tend]; and


- - determining an approximation of a_(Δt) for the fixed timestep Δt
    according to the following:

\({a_{\Delta \; t} = \left. {argmin}_{a}||{{\begin{bmatrix}
\frac{1}{t_{1} + {\Delta \; t\text{/}2}} \\
\frac{1}{t_{2} + {\Delta \; t\text{/}2}} \\
\vdots \\
\frac{1}{t_{k} + {\Delta \; t\text{/}2}}
\end{bmatrix}a} - \begin{bmatrix}
\frac{{\left( {t_{1} + {\Delta \; t}} \right)} - {\left( t_{1} \right)}}{\Delta \; t} \\
\frac{{\left( {t_{2} + {\Delta \; t}} \right)} - {\left( t_{2} \right)}}{\Delta \; t} \\
\vdots \\
\frac{{\left( {t_{k} + {\Delta \; t}} \right)} - {\left( t_{k} \right)}}{\Delta \; t}
\end{bmatrix}} \right.||_{2}},\)

where argmin represents a minimization, tk represents a kth time point, and wherein the constant c corresponding to this timestep is

cΔt=g(Tend)−aΔt ln(Tend).

In another aspect, the system determines a predicted value for a future time Tend+td according to the following:


- - F_(Δt)(t_(d))=a_(Δt) ln(T_(end)+t_(d))+c_(Δt), where t_(d) is the
    desired time length for prediction.

## DETAILED DESCRIPTION

The present invention relates to a system for automated detection of critical transitions and, more particularly, to a system for automated detection of critical transitions using predicted system trajectories.

The following description is presented to enable one of ordinary skill in the art to make and use the invention and to incorporate it in the context of particular applications. Various modifications, as well as a variety of uses in different applications will be readily apparent to those skilled in the art, and the general principles defined herein may be applied to a wide range of aspects. Thus, the present invention is not intended to be limited to the aspects presented, but is to be accorded the widest scope consistent with the principles and novel features disclosed herein.

In the following detailed description, numerous specific details are set forth in order to provide a more thorough understanding of the present invention. However, it will be apparent to one skilled in the art that the present invention may be practiced without necessarily being limited to these specific details. In other instances, well-known structures and devices are shown in block diagram form, rather than in detail, in order to avoid obscuring the present invention.

The reader's attention is directed to all papers and documents which are filed concurrently with this specification and which are open to public inspection with this specification, and the contents of all such papers and documents are incorporated herein by reference. All the features disclosed in this specification, (including any accompanying claims, abstract, and drawings) may be replaced by alternative features serving the same, equivalent or similar purpose, unless expressly stated otherwise. Thus, unless expressly stated otherwise, each feature disclosed is one example only of a generic series of equivalent or similar features.

Furthermore, any element in a claim that does not explicitly state “means for” performing a specified function, or “step for” performing a specific function, is not to be interpreted as a “means” or “step” clause as specified in 35 U.S.C. Section 112, Paragraph 6. In particular, the use of “step of” or “act of” in the claims herein is not intended to invoke the provisions of 35 U.S.C. 112, Paragraph 6.

Before describing the invention in detail, first a list of cited references is provided. Next, a description of the various principal aspects of the present invention is provided. Subsequently, an introduction provides the reader with a general understanding of the present invention. Finally, specific details of the present invention are provided to give an understanding of the specific aspects.

### (2) PRINCIPAL ASPECTS

The present invention has three “principal” aspects. The first is a system for automated detection of critical transitions. The system is typically in the form of a computer system operating software or in the form of a “hard-coded” instruction set. This system may be incorporated into a wide variety of devices that provide different functionalities. The second principal aspect is a method, typically in the form of software, operated using a data processing system (computer). The third principal aspect is a computer program product. The computer program product generally represents computer-readable instructions stored on a non-transitory computer-readable medium such as an optical storage device, e.g., a compact disc (CD) or digital versatile disc (DVD), or a magnetic storage device such as a floppy disk or magnetic tape. Other, non-limiting examples of computer-readable media include hard disks, read-only memory (ROM), and flash-type memories. These aspects will be described in more detail below.

A block diagram depicting an example of a system (i.e., computer system 100) of the present invention is provided in FIG. 1. The computer system 100 is configured to perform calculations, processes, operations, and/or functions associated with a program or algorithm. In one aspect, certain processes and steps discussed herein are realized as a series of instructions (e.g., software program) that reside within computer readable memory units and are executed by one or more processors of the computer system 100. When executed, the instructions cause the computer system 100 to perform specific actions and exhibit specific behavior, such as described herein.

The computer system 100 may include an address/data bus 102 that is configured to communicate information. Additionally, one or more data processing units, such as a processor 104 (or processors), are coupled with the address/data bus 102. The processor 104 is configured to process information and instructions. In an aspect, the processor 104 is a microprocessor. Alternatively, the processor 104 may be a different type of processor such as a parallel processor, or a field programmable gate array.

The computer system 100 is configured to utilize one or more data storage units. The computer system 100 may include a volatile memory unit 106 (e.g., random access memory (“RAM”), static RAM, dynamic RAM, etc.) coupled with the address/data bus 102, wherein a volatile memory unit 106 is configured to store information and instructions for the processor 104. The computer system 100 further may include a non-volatile memory unit 108 (e.g., read-only memory (“ROM”), programmable ROM (“PROM”), erasable programmable ROM (“EPROM”), electrically erasable programmable ROM “EEPROM”), flash memory, etc.) coupled with the address/data bus 102, wherein the non-volatile memory unit 108 is configured to store static information and instructions for the processor 104. Alternatively, the computer system 100 may execute instructions retrieved from an online data storage unit such as in “Cloud” computing. In an aspect, the computer system 100 also may include one or more interfaces, such as an interface 110, coupled with the address/data bus 102. The one or more interfaces are configured to enable the computer system 100 to interface with other electronic devices and computer systems. The communication interfaces implemented by the one or more interfaces may include wireline (e.g., serial cables, modems, network adaptors, etc.) and/or wireless (e.g., wireless modems, wireless network adaptors, etc.) communication technology.

In one aspect, the computer system 100 may include an input device 112 coupled with the address/data bus 102, wherein the input device 112 is configured to communicate information and command selections to the processor 100. In accordance with one aspect, the input device 112 is an alphanumeric input device, such as a keyboard, that may include alphanumeric and/or function keys. Alternatively, the input device 112 may be an input device other than an alphanumeric input device. In an aspect, the computer system 100 may include a cursor control device 114 coupled with the address/data bus 102, wherein the cursor control device 114 is configured to communicate user input information and/or command selections to the processor 100. In an aspect, the cursor control device 114 is implemented using a device such as a mouse, a track-ball, a track-pad, an optical tracking device, or a touch screen. The foregoing notwithstanding, in an aspect, the cursor control device 114 is directed and/or activated via input from the input device 112, such as in response to the use of special keys and key sequence commands associated with the input device 112. In an alternative aspect, the cursor control device 114 is configured to be directed or guided by voice commands.

In an aspect, the computer system 100 further may include one or more optional computer usable data storage devices, such as a storage device 116, coupled with the address/data bus 102. The storage device 116 is configured to store information and/or computer executable instructions. In one aspect, the storage device 116 is a storage device such as a magnetic or optical disk drive (e.g., hard disk drive (“HDD”), floppy diskette, compact disk read only memory (“CD-ROM”), digital versatile disk (“DVD”)). Pursuant to one aspect, a display device 118 is coupled with the address/data bus 102, wherein the display device 118 is configured to display video and/or graphics. In an aspect, the display device 118 may include a cathode ray tube (“CRT”), liquid crystal display (“LCD”), field emission display (“FED”), plasma display, or any other display device suitable for displaying video and/or graphic images and alphanumeric characters recognizable to a user.

The computer system 100 presented herein is an example computing environment in accordance with an aspect. However, the non-limiting example of the computer system 100 is not strictly limited to being a computer system. For example, an aspect provides that the computer system 100 represents a type of data processing analysis that may be used in accordance with various aspects described herein. Moreover, other computing systems may also be implemented. Indeed, the spirit and scope of the present technology is not limited to any single data processing environment. Thus, in an aspect, one or more operations of various aspects of the present technology are controlled or implemented using computer-executable instructions, such as program modules, being executed by a computer. In one implementation, such program modules include routines, programs, objects, components and/or data structures that are configured to perform particular tasks or implement particular abstract data types. In addition, an aspect provides that one or more aspects of the present technology are implemented by utilizing one or more distributed computing environments, such as where tasks are performed by remote processing devices that are linked through a communications network, or such as where various program modules are located in both local and remote computer-storage media including memory-storage devices.

An illustrative diagram of a computer program product (i.e., storage device) embodying the present invention is depicted in FIG. 2. The computer program product is depicted as floppy disk 200 or an optical disk 202 such as a CD or DVD. However, as mentioned previously, the computer program product generally represents computer-readable instructions stored on any compatible non-transitory computer-readable medium. The term “instructions” as used with respect to this invention generally indicates a set of operations to be performed on a computer, and may represent pieces of a whole program or individual, separable, software modules. Non-limiting examples of “instruction” include computer program code (source or object code) and “hard-coded” electronics (i.e. computer operations coded into a computer chip). The “instruction” is stored on any non-transitory computer-readable medium, such as in the memory of a computer or on a floppy disk, a CD-ROM, and a flash drive. In either event, the instructions are encoded on a non-transitory computer-readable medium.

### (3) INTRODUCTION

One central characteristic of complex social-technological systems is their self-organized emerging interactions which provide the benefits of exchanging information and resources effectively, yet at the same time increase the risk and pace of spreading attacks or failures. A small perturbation on a complex system operating in a high-risk unstable region can induce a critical transition that leads to unstoppable catastrophic failures. In the system according to the principles of the present invention, catastrophic failures can be avoided by detecting early warnings of critical transitions and predicting the likelihood of system trajectories and the lead time to the critical points.

The invention described herein is built upon the invention described in U.S. application Ser. No. 13/904,945, entitled, “Detection and Identification of Directional Influences Using Dynamic Spectrum” (hereinafter referred to as the '945 application), which is an information dynamic spectrum framework that goes beyond unidirectional diffusion dynamics to investigate heterogeneously networked dynamical systems with transient directional influence. The '945 application is hereby incorporated by reference as though fully set forth herein.

The '945 application describes the development of a novel Associative Transfer Entropy (ATE) measure which decomposes the pair-wise directional influence of transfer entropy to associative states of asymmetric, directional information flows. Multivariate time series of complex systems were transformed into the spectrum of Transfer Entropy Matrix (TEM) and Associative Transfer Entropy Matrix (ATEM) to capture information dynamics of the system. The novel spectral radius measures of TEM and ATEM were developed to detect early warning signals of source-driven instability, and induce directional influence structure to identify the source and reveal dynamics of directional influences. The framework described in the '945 application enables one not only to accurately detect, predict, and mitigate abrupt behavior changes in complex systems, but also to understand, design, and build more sustainable and resilient complex systems.

The idea of associative transfer entropy is to decompose transfer entropy (TE) by constraining associated states of two processes. The simplest case of ATE is two influence classes: one positive ATE+ and the other negative ATE−. In this case, ATE is able to distinguish two situations where the amount of information transfer is the same but have opposite effects: the source drives the destination the same direction in ATE−, and the source drives the destination the opposite direction in ATE−. For dynamic data, meaning the amount of information flow is not constant, the TE/ATE of time series in a local time window is calculated, so that TE/ATE becomes a function of time. Such decomposition further enables one to investigate ATEM in the form of ATEM+ and ATEM−.

Given ATE+/TE cross-over signature as the early warning signals of critical transition, the present invention predicts (1) the likelihood of system trajectories and (2) the lead time to critical points. It was first observed that ATE+ and TE are maximized, at the same time that ATE− flattened, prior to the system switching to alternative stable regimes. Therefore, model-based statistical forecasting was applied to estimate the likelihood of ATE+/TE/ATE− trajectories. The lead time is predicted by estimating the critical point based on the projected flattening of ATE− trajectories. The prediction method according to the principles of the present invention will continuously output the update of probabilistic cones as the system progresses. Determining the likelihood and lead time of critical points will enable further developments of a mitigation strategy to avoid critical transitions. Each of these aspects will be described in further detail below.

### (4) SPECIFIC DETAILS OF THE INVENTION

Described is a system to address the need of automated detection of emerging transitions, and identify sources of instability from time series of complex systems. The techniques according to the principles of the present invention can be used to detect directional influences apart from intrinsic dynamics so that one can derive encapsulated interaction modules to predict behavior trajectories. The system according to the principles of the present invention will enable the advancement in analyzing dynamics of complex networks.

Advantages of the system and method described herein include, but are not limited to, (1) providing an effective measure for quantifying associative, asymmetric directional influences, whereas other methods only can handle either symmetric or directional influences; (2) providing an effective formulation for capturing system-wise directional influences, whereas other methods can only handle pair-wise directional influence, or system-wise symmetrical influence; (3) providing an effective measure for detecting instability in systems with directional influence dynamics, whereas other methods assume un-directional diffusion dynamics; (4) providing an effective method for characterizing instability trends of aggregated directional influences, whereas other methods can only detect instability with simple thresholding; and (5) providing an effective method to reveal sources and structures in changing dynamics of directional influences, whereas other methods can only handle stationary dynamics.

(4.1) Background: Information Dynamic Spectrum

The asymmetric measure, transfer entropy,

\(\begin{matrix}
{{T_{x_{j}\rightarrow x_{i}} = {\Sigma_{{({x_{i,{t + 1}},x_{i,t},x_{j,t}})} \in D}{p\left( {x_{i,{t + 1}},x_{i,t},x_{j,t}} \right)}\log \frac{p\left( {\left. x_{i,{t + 1}} \middle| x_{i,t} \right.,x_{j,t}} \right)}{p\left( x_{i,{t + 1}} \middle| x_{i,t} \right)}}},} & (1)
\end{matrix}\)

quantifies the amount of information transfer from source xj to destination xi. It has been used to demonstrate the asymmetrical influence from mature markets to emerging markets by analyzing stock market indices, as described in Literature Reference Nos. 1 and 6. Yet, current state-of-the-art only considers average pair-wise information transfers and statistical analysis, without including the more fundamental object of an information dynamic spectrum (i.e., time-varying information transfer) to explain the emergence of directional influences.

In the previously developed information dynamic spectrum theory described in the '945 application, the dynamics of a complex network were formulated as: dX=F(X)dt+σdW, where F:mm is a differentiable function that explains the dynamics of the system of m elements X(t)=[x1(t) x2(t) . . . xm(t)]T and is defined by F(X(t))=[f1(X(t)) f2(X(t)) . . . fm(X(t))]T. This captures both the dynamics of individual entities and the networked interactions between the entities. For example, element xi(t) can be the ith stock index of the tth trading day. The last term, σdW, corresponds to white noise scaled by σ. To reveal the unknown F(X), this problem is further simplified by linear approximation: F(X)≈F(X0)+J(X0)(X−X0), for X near X0, where

\(J = \left\lbrack \frac{\partial f_{i}}{\partial x_{j}} \right\rbrack_{i,{j = 1},{\ldots \; m}}\)

is the Jacobian matrix. Therefore, the local temporal dynamics can be obtained pair-wise. The measure associative transfer entropy (ATE) at state Dk, for i≠j is defined by:

\(\begin{matrix}
{{T_{x_{j}\rightarrow x_{i}}^{D_{k}} = {\Sigma_{{({x_{i,{t + 1}},x_{i,t},x_{j,t}})} \in D}{p\left( {x_{i,{t + 1}},x_{i,t},x_{j,t}} \right)}\log \frac{p\left( {\left. x_{i,{t + 1}} \middle| x_{i,t} \right.,x_{j,t}} \right)}{p\left( x_{i,{t + 1}} \middle| x_{i,t} \right)}}},} & (2)
\end{matrix}\)

where Dk is a subset of D that represents a certain associated state between xi and xj. The purpose of ATE is to capture information transfer between two variables for a particular state association. For example, TE may be decomposed into two influence classes: one positive and the other negative.

If the internal dynamics within each node is negligible comparing to interactions among nodes, it is conjectured that

\({\frac{\partial f_{i}}{\partial x_{j}} \sim {\left( {T_{x_{j}\rightarrow x_{i}}^{D_{1}},T_{x_{j}\rightarrow x_{i}}^{D_{2}},\ldots,T_{x_{j}\rightarrow x_{i}}^{D_{s}}} \right)}},\)

for some linear function g. Let TDbe an associative transfer entropy matrix (ATEM):

\(\begin{matrix}
{T^{D_{k}} = {\begin{bmatrix}
T_{x_{1}\rightarrow x_{1}}^{D_{k}} & T_{x_{2}\rightarrow x_{1}}^{D_{k}} & \ldots & T_{x_{m}\rightarrow x_{1}}^{D_{k}} \\
T_{x_{1}\rightarrow x_{2}}^{D_{k}} & T_{x_{2}\rightarrow x_{2}}^{D_{k}} & \ldots & T_{x_{m}\rightarrow x_{2}}^{D_{k}} \\
\; & \vdots & \; & \; \\
T_{x_{1}\rightarrow x_{m}}^{D_{k}} & T_{x_{2}\rightarrow x_{m}}^{D_{k}} & \ldots & T_{x_{m}\rightarrow x_{m}}^{D_{k}}
\end{bmatrix}.}} & (3)
\end{matrix}\)

To appropriately deal with dynamic data, meaning the amount of information flow from one to another is not static, TE/ATE curves were generated as functions of time, calculated over sliding windows.

Since the TEM matrix is non-symmetric, its eigenvalues are complex-valued. The spectral radius of the TEM matrix is used to measure the total amount of information flow of the entire network.

To efficiently estimate transfer entropy of continuous data, Staniek and Lehnertz (see Literature Reference No. 4) proposed a method using a symbolization technique that is robust and computationally fast, which had been introduced with the concept of permutation entropy. In the '945 application, the symbolization technique of Staniek and Lehnertz was adapted to calculate ATE. Specifically, the continuous-valued time sequence {x(t)}t=1N was symbolized by first ordering the values of {x(t), x(t+1), . . . x(t+m)} with {1, 2, . . . , m} and denoting {circumflex over (x)}(t)=associated permutation of order m the symbol of x(t) at t. Then, the ATE of {x(t)}t=1N is estimated by calculating ATE of {{circumflex over (x)}(t)}t=1N.

FIGS. 3A and 3B show an ATE analysis of a non-foster network from the invention described in the '945 application. The circuit is initially operated in the stable region, where there is no oscillation. Then a small perturbation is added. It is unknown whether the circuit will become oscillatory (unstable) or stay stable. An ATE analysis was performed to detect if the circuits would become synchronized (unstable). The plot in FIG. 3A is the circuit in voltage over time, where Ant1 represents Antenna 1, Ant2 represents Antenna 2, i1 represents port 1, and i2 represents port 2. The plot in FIG. 3B shows the TE/ATE+/ATE− curves over time. The curves are obtained from the absolute sum of spectrum of TEM/ATEM+/ATEM−, respectively. It was found that the spectral radius of TEM/ATEM+/ATEM− also show similar outcomes, but since TEM is the sum of ATEM+ and ATEM−, the ATE+ curve will never cross the TE curve. Thus, the absolute sum of the spectrum is more informative. As shown in FIG. 3B, the ATE+ curve crosses over the TE curve near time point 800, indicating the increasing in synchronization. In addition, the ATE+ curve reaches its peak right before full synchronization, while the ATE− curve flattens because there is no negative association.

(4.2) Probabilistic Cones for Trajectories Prediction

In the system according to the principles of the present invention, model-based statistical forecasting is used to estimate the TE/ATE+/ATE− trajectories. An advantage of analyzing the TE/ATE curves is that TE/ATE removes the spikes of the raw data, as shown in the circuit data example in FIG. 3A. It has been observed that the TE curve in this case can be well approximated by the natural logarithm with an unknown coefficient a and a constant c according to the following:

g(t)=a ln(t)+c.  (4)

FIG. 4A shows curve fitting with a plot of the exponential function, and FIG. 4B illustrates curve fitting with a plot of the logarithmic function. The bold solid curves 400 are the TE curve from FIG. 3B. The bold dashed curves 402 are the fitted curves in the interval tε[700,1100]. The unbolded dashed curves 404 are the projections from the fitted curves. FIG. 4B shows that the logarithm is appropriate to fit the TE curve.

To estimate the coefficient a from TE/ATE± curves, instead of fitting them deterministically with the logarithmic function in equation (4), the rate of change was estimated with various discrete time steps. This generates a prediction cone, which will be described in detail below. From the derivative of equation (4),

\(\begin{matrix}
{{{^{\prime}(t)} = \frac{a}{t}},} & (5)
\end{matrix}\)

the following discretized version for the unknown a was obtained:

\(\begin{matrix}
{\frac{\Delta }{\Delta \; t} = {a{\frac{1}{t}.}}} & (6)
\end{matrix}\)

For a fixed timestep Δt in a window [Tstart, Tend], the least squares was used to solve the unknown a. First, the following matrix equation was written:

\(\begin{matrix}
{{{\begin{bmatrix}
\frac{1}{t_{1} + {\Delta \; t\text{/}2}} \\
\frac{1}{t_{2} + {\Delta \; t\text{/}2}} \\
\vdots \\
\frac{1}{t_{k} + {\Delta \; t\text{/}2}}
\end{bmatrix}a} = \begin{bmatrix}
\frac{{\left( {t_{1} + {\Delta \; t}} \right)} - {\left( t_{1} \right)}}{\Delta \; t} \\
\frac{{\left( {t_{2} + {\Delta \; t}} \right)} - {\left( t_{2} \right)}}{\Delta \; t} \\
\vdots \\
\frac{{\left( {t_{k} + {\Delta \; t}} \right)} - {\left( t_{k} \right)}}{\Delta \; t}
\end{bmatrix}},} & (7)
\end{matrix}\)

where t1, . . . , tk+Δtε[Tstart, Tend], where tk is the kth time point. The approximation of αΔt for the fixed timestep Δt was then obtained according to the following:

\(\begin{matrix}
{a_{\Delta \; t} = \left. {argmin}_{a}||{{\begin{bmatrix}
\frac{1}{t_{1} + {\Delta \; t\text{/}2}} \\
\frac{1}{t_{2} + {\Delta \; t\text{/}2}} \\
\vdots \\
\frac{1}{t_{k} + {\Delta \; t\text{/}2}}
\end{bmatrix}a} - \begin{bmatrix}
\frac{{\left( {t_{1} + {\Delta \; t}} \right)} - {\left( t_{1} \right)}}{\Delta \; t} \\
\frac{{\left( {t_{2} + {\Delta \; t}} \right)} - {\left( t_{2} \right)}}{\Delta \; t} \\
\vdots \\
\frac{{\left( {t_{k} + {\Delta \; t}} \right)} - {\left( t_{k} \right)}}{\Delta \; t}
\end{bmatrix}}||{}_{2}. \right.} & (8)
\end{matrix}\)

The constant corresponding to this timestep is then cΔt=g(Tend)−aΔt ln(Tend). Therefore, the predicted value for the future time Tend+td is

FΔt(td)=aΔt ln(Tend+td)+cΔt.  (9)

td is the desired time length for prediction.

Now that a method to estimate the constants c and a has been established, a probabilistic prediction cone (or light cone) can be generated at each time point as one varies Δt to obtain multiple estimates of c and a. Therefore, a probabilistic prediction cone at a given time consists of a collection of natural logarithm curves starting from that point.

To estimate the error of this prediction for the immediate next timestep, the following was calculated:

errorΔt(i)=g(ti+Δt)−[aΔt ln(ti+Δt)+c(i)],  (10)

where

c(i)=g(ti−1)−aΔt ln(ti−1).  (11)

Let E be the collection of all errorΔt over all timesteps Δt and let σ=standard deviation of E. Let G be the collection of all predicted values GΔt(td) over all timesteps Δt and μ=mean(G). Therefore, the 95% confidence interval for the future time Tend+td is:

\(\begin{matrix}
{{{CI} = \left\lbrack {{\mu - {1.96\frac{\sigma}{\sqrt{N}}}},{\mu + {1.96\frac{\sigma}{\sqrt{N}}}}} \right\rbrack},} & (12)
\end{matrix}\)

where N is the size of E.

FIG. 5 shows the 95% confidence interval of a predicted trajectory in unbolded solid lines 500. The predicted trajectory for TE is represented by the unbolded dashed line 502. The bold solid line 504 depicts the actual trajectory of TE. The prediction value and confidence interval are generated from the prediction cones, described above. Two points of the actual trajectory were outside the 95% confidence interval, right before the non-foster circuits were fully synched around time t=1500. These points are represented by diamonds 504 and indicate the possibility of a trend toward a critical transition.

FIGS. 6A and 6B illustrate two time snapshots of the prediction cones 600 produced according to the method described above and the predicted trajectory value (represented by bold dashed curves 602). The prediction cones are used to generate the prediction values with confidence intervals in FIG. 5. The solid bold curves 604 represent the actual TE trajectory.

FIG. 7 is a flow diagram depicting the system for predicting system trajectories toward critical transitions according to the principles of the present invention. In a first step 700, a set of multivariate time series of observables of a complex system is transformed into a set of symbolic multivariate time series. In a second step 702, the system determines pair-wise time series of a TE measure. In a third step 704, an ATE measure is determined. In a fourth step 706, the system estimates ATE+, TE, and ATE− trajectories over time. In a fifth step 708, a critical transition in the system is predicted using at least one of the ATE+, TE, and ATE− trajectories.

In summary, the present invention is a system and method for analyzing time series of complex systems to detect trends toward critical transitions, especially for complex systems with directional influence dynamics. The described system and method can be deployed as embedded decision support modules to provide early indication of critical transitions in complex systems, including, but not limited to, vehicle health management, prognostics for complex electronics, crisis management in supply chains, social unrests, financial market instability, and epileptic seizures in brain networks. The technology described herein will result in accurate detection of upcoming critical transitions of system behaviors, accurate characterization of instability trends toward critical transitions, and accurate identification of instability sources and propagation structure changes. Applications of the present invention included, but are not limited to, vehicle health management, complex electronics, smart power grid, social network analysis, social instability, supply-chain crisis management, cyber security, and epileptic seizure detection.

