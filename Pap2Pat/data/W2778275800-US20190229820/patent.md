# DESCRIPTION

## FIELD OF THE DISCLOSURE

This application is related to radio frequency (RF) receivers, and specifically to spectrum sensing in RF receivers.

## BACKGROUND

Mobile devices are increasingly being used for entertainment, such as gaming and video streaming. The coexistence of these new services with the Internet of Things (IoT) and machine-to-machine communications means that wireless applications may quickly become starved for bandwidth. Millimeter wave and other radio frequency (RF) spectrum can provide much needed increases in throughput but pose a challenge of high-speed sampling required to sense the spectrum. This may be a particular challenge for relatively low-rate IoT applications, which are likely to benefit from opportunistic decentralized spectrum access. To achieve efficient usage of the spectrum, sensing techniques are needed which overcome the bottleneck of sampling at the Nyquist rate, which is generally too time and/or energy intensive, particularly for low-power wireless devices.

Two classes of solutions have been proposed to overcome this bottleneck. The first approach uses a sub-Nyquist sampling front end using analog-to-digital conversion techniques named xampling architectures. Xampling architectures preprocess a signal in the analog domain and then sample at a lower rate compared with what the Nyquist theorem dictates. The aim is to reduce the complexity and energy cost for the analog-to-digital converter hardware. However, prior xampling approaches increase complexity in the reconstruction of the underlying signal, and accurate spectrum sensing may not be guaranteed in lower signal-to-noise ratio (SNR) signals.

The second approach consists in selecting opportunistically, and in a cognitive fashion, a small section of spectrum at a time, relying on an analog front end able to switch between small sub-bands. This approach may be better able to cope with lower SNR signals. However, for sensing a broad spectrum, the second approach may take too much time to determine and use available spectrum before the environment has changed.

## SUMMARY

An active sequential xampling receiver for spectrum sensing is disclosed. The receiver includes a dynamically adjustable analog front end to perform sub-Nyquist energy sensing across a broad radio frequency (RF) spectrum. In an exemplary aspect, the receiver includes a dynamic modulator which modulates the broad RF spectrum to dynamically select sub-bands (e.g., RF channels) and fold their spectral content into a narrower baseband signal for energy detection. A controller adjusts the dynamic modulator to maximize utility of the spectrum detection based on past energy observations.

Nyquist sampling at very high carriers can be prohibitively costly for low-power wireless devices. In spectrum sensing, this limit calls for the receiver to include an analog front end that can sweep different bands quickly in order to use the available spectrum opportunistically. Thus, the sensing action of the analog front end maximizes a utility function decreasing linearly with the number of measurements and increasing as a function of the active spectrum components that are correctly detected. The optimization selects the best linear combinations of sub-bands to mix in order to accrue maximum utility. The structure of the utility represents the trade-off between exploration, exploitation, and risk of making an error that is characteristic of the spectrum-sensing problem.

An exemplary embodiment relates to an RF receiver. The RF receiver includes a dynamic modulator configured to modulate a received signal such that one or more portions of the received signal are dynamically selected and folded into a baseband of a modulated signal. The RF receiver also includes an energy detector configured to sample an energy of the modulated signal at a sub-Nyquist rate. The RF receiver also includes a controller configured to adjust the dynamic modulator based on an output of the energy detector.

Another exemplary embodiment relates to a method for sensing occupied RF spectrum. The method includes receiving an RF signal and sequentially modulating the RF signal using a sensing matrix to produce a set of modulated signals. The method also includes detecting a signal occupancy for each of the set of modulated signals. In addition, coefficients of the sensing matrix are dynamically adjusted based on detecting the signal occupancy.

Another exemplary embodiment relates to an analog front end for an RF receiver. The analog front end includes a dynamic modulator configured to convert an incoming RF signal having a first bandwidth to a modulated signal having content of the first bandwidth dynamically folded in a second bandwidth narrower than the first bandwidth. The analog front end also includes an energy detector configured to sense signal energy of the modulated signal within the second RF bandwidth.

Those skilled in the art will appreciate the scope of the present disclosure and realize additional aspects thereof after reading the following detailed description of the preferred embodiments in association with the accompanying drawing figures.

## DETAILED DESCRIPTION

The embodiments set forth below represent the necessary information to enable those skilled in the art to practice the embodiments and illustrate the best mode of practicing the embodiments. Upon reading the following description in light of the accompanying drawing figures, those skilled in the art will understand the concepts of the disclosure and will recognize applications of these concepts not particularly addressed herein. It should be understood that these concepts and applications fall within the scope of the disclosure and the accompanying claims.

It will be understood that, although the terms first, second, etc. may be used herein to describe various elements, these elements should not be limited by these terms. These terms are only used to distinguish one element from another. For example, a first element could be termed a second element, and, similarly, a second element could be termed a first element, without departing from the scope of the present disclosure. As used herein, the term “and/or” includes any and all combinations of one or more of the associated listed items.

It will be understood that when an element is referred to as being “connected” or “coupled” to another element, it can be directly connected or coupled to the other element or intervening elements may be present. In contrast, when an element is referred to as being “directly connected” or “directly coupled” to another element, there are no intervening elements present.

The terminology used herein is for the purpose of describing particular embodiments only and is not intended to be limiting of the disclosure. As used herein, the singular forms “a,” “an,” and “the” are intended to include the plural forms as well, unless the context clearly indicates otherwise. It will be further understood that the terms “comprises,” “comprising,” “includes,” and/or “including” when used herein specify the presence of stated features, integers, steps, operations, elements, and/or components, but do not preclude the presence or addition of one or more other features, integers, steps, operations, elements, components, and/or groups thereof.

Unless otherwise defined, all terms (including technical and scientific terms) used herein have the same meaning as commonly understood by one of ordinary skill in the art to which this disclosure belongs. It will be further understood that terms used herein should be interpreted as having a meaning that is consistent with their meaning in the context of this specification and the relevant art and will not be interpreted in an idealized or overly formal sense unless expressly so defined herein.

An active sequential xampling receiver for spectrum sensing is disclosed. The receiver includes a dynamically adjustable analog front end to perform sub-Nyquist energy sensing across a broad radio frequency (RF) spectrum. In an exemplary aspect, the receiver includes a dynamic modulator which modulates the broad RF spectrum to dynamically select sub-bands (e.g., RF channels) and fold their spectral content into a narrower baseband signal for energy detection. A controller adjusts the dynamic modulator to maximize utility of the spectrum detection based on past energy observations.

Nyquist sampling at very high carriers can be prohibitively costly for low-power wireless devices. In spectrum sensing, this limit calls for the receiver to include an analog front end that can sweep different bands quickly in order to use the available spectrum opportunistically. Thus, the sensing action of the analog front end maximizes a utility function decreasing linearly with the number of measurements and increasing as a function of the active spectrum components that are correctly detected. The optimization selects the best linear combinations of sub-bands to mix in order to accrue maximum utility. The structure of the utility represents the trade-off between exploration, exploitation, and risk of making an error that is characteristic of the spectrum-sensing problem.

Compared with other multi-band signals receivers, the hardware in the architecture according to the present disclosure is simpler, since the architecture uses a single non-coherent receiver and a single sampling device that collects energy measurements sequentially, sampling at a fraction of the Nyquist rate. A time-dependent utility function is used to optimize the trade-off between sensing and exploitation.

It is important to remark that the optimum action generally does not attempt the full recovery of all the white spaces. The optimum decision may be conservative and sense a very limited portion of the spectrum. Furthermore, since scanning one sub-band at a time is a possible action of the active spectrum-sensing strategy, the method of the present disclosure subsumes previous techniques to scan the spectrum optimally, without mixing it. This approach is referred to as direct inspection and is discussed in Section III, A.

The present disclosure is more closely related to the stochastic optimization schemes that extend the framework and optimize a compressive spectrum-sensing action based on previous observations. The common goal of stochastic optimization schemes is the recovery of the full support of a given vector. Typically, such techniques are shown to be able to cope with lower signal-to-noise ratio (SNR) in the signal reconstruction with low complexity. What these stochastic optimization schemes do not capture is that, in cognitive spectrum-sensing applications, a timely decision is also desirable to have enough time to exploit the spectrum. The method of the present disclosure is also adaptive with respect to the time horizon K, the number of resources N, the prior probabilities on the states of each resources, and the parameters that characterize the utility function, that is, reward and penalty for good/bad decisions.

Based on performance analysis, it is the clear that sparse and adaptive sensing matrix designs outperform dense sensing matrices and those that are sparse but static. There are two main reasons for this: (1) through belief propagation algorithms, they achieve near-optimum detection performance, and (2) they mitigate the aforementioned noise-folding phenomena. The method of the present disclosure is applicable not only when the utility comes from finding empty entries (e.g., spectrum sensing) but also when one is interested in finding the occupied ones (e.g., in a RADAR application).

More specifically, the present disclosure is organized as follows: Section I is dedicated to the signal model and the analog front end of the detector according to the present disclosure, and Section II formulates the optimization problem. Then, Section III addresses the optimal dynamic design for the direct inspection case (III, A), in which there is no mixing of sub-bands (also known as scanning receiver), and a group testing case (III, B) in which is introduced the possibility of mixing different bands. Section IV is dedicated to additional discussions: an alternative standard method for detection based on maximum likelihood estimate and LASSO relaxation, hardware limitations of the architecture according to the present disclosure, and the extension of the framework according to the present disclosure to other applications. The present disclosure demonstrates that, even if finding the optimal policy is exponentially complex in the number of resources, the approximation factor for a greedy procedure can be characterized. Numerical results to sustain the claims of the present disclosure are presented in Section V.

Regarding notation, bold lowercase represents vectors, bold uppercase represent matrices, and calligraphic letters indicate sets. For example, sA indicates the entries i∈ of vector s, and ∥y∥A2 represents the weighted 2-norm yT Ay. For any set function ƒ (), the marginal increment for adding element a is defined as ∂aƒ()=ƒ(+a)−ƒ().

### A. Cognitive Radio Scenario

FIG. 1A is a schematic diagram of a cognitive radio scenario 10. The cognitive radio scenario 10 includes a number of RF devices, which may include one or more user equipment (UE) 12, base stations 14, and similar devices. Each of the UEs 12 and base stations 14 may send and/or receive signals over a common RF spectrum. Accordingly, a receiver 16 in the cognitive radio scenario 10 may need to quickly and accurately sense which portions of the RF spectrum are occupied in order to receive and/or transmit signals within the RF spectrum as needed.

FIG. 1B is a graphical representation of an RF spectrum 18 of the cognitive radio scenario 10 of FIG. 1A. The RF spectrum 18 may be spectrum with opportunistic access, such as millimeter wave (60-80 GHz), citizens broadband radio service (CBRS), or other frequencies. The RF spectrum 18 being sensed by the receiver 16 can be represented in the frequency domain as X(ƒ) and in the time domain as x(t). In addition, there may be N channels 20 (e.g., sub-bands centered at frequencies ƒ1, ƒ2, . . . , ƒi, . . . , ƒN) of the RF spectrum 18, each channel 20 having a channel width Rc such that the RF spectrum 18 has a bandwidth of W=NRc.

In the context of cognitive radio for the RF spectrum 18, each transmission includes large amounts of control signals overhead in addition to the payload. Therefore, it can be assumed that the activity of the UEs 12 and base stations 14 over one or more channels 20 will persist for several sampling periods Ts. However, assuming this interval T lasts for a multiple K of the sampling period Ts (i.e., T=KTs), the sensing mechanism of the receiver 16 should provide the fastest decision it can. The goal of the receiver 16 according to the present disclosure is to sequentially sense the spectrum for a first portion of this interval T and transmit the most it can during the remaining time over the channels 20 found empty (or, alternatively, process one or more occupied channels 20).

### B. Spectrum Sensing Architecture

FIG. 2 is a diagram of an exemplary receiver 16 configured to sense spectrum at a sub-Nyquist rate by dynamically modulating portions of a broad spectrum. The receiver 16 includes an analog front end 22, which includes an energy detector 24 and a dynamic modulator 26. The energy detector 24 is configured to sample energy of an input signal at a sub-Nyquist rate. In an exemplary aspect, the energy detector 24 is a single-channel detector which can operate quickly with low power demands by filtering and sampling a single channel baseband input signal.

The dynamic modulator 26 facilitates use of the single channel energy detector 24 by modulating a received signal x(t) (e.g., the RF spectrum 18) such that portions (e.g., sub-bands or channels 20) of the received signal x(t) are dynamically selected and folded into the single channel baseband input signal of the energy detector 24. The portions of the received signal x(t) which are selected and folded into the baseband input signal by the dynamic modulator 26 are selected by a controller 28 in order to maximize utility of the spectrum sensing function as described further below in Sections II and III. The controller 28 can control the dynamic modulator 26 through a sensing matrix B or other control signals.

The receiver 16 can thus perform carrier sensing over multiple bands simultaneously. The receiver 16 has the advantage of being sequential, and not requiring time accurate time offset between sampling channel as in some approaches. In addition, the spectrum sensing function of the receiver 16 is robust to the noise-folding problem, in which SNR deteriorates approximately linear in the number of bands that are aliased prior to sampling.

FIG. 3 is a diagram of the exemplary receiver 16 of FIG. 2, illustrating in greater detail components of the analog front end 22. In the proposed analog front end 22, the dynamic modulator 26 folds the spectrum present in specific sub-bands onto the center frequency of the energy detector 24 for filtering and sampling, during what can be referred to as a sub-Nyquist carrier sensing phase. The samples are spaced by intervals of duration

\(T_{s} = \frac{1}{R_{s}}\)

which is a factor 1/N smaller than the total spectrum. As the diagram in FIG. 3 shows, rather than having a filter bank architecture, the analog front end 22 performs sequential non-coherent tests. These tests are designed according to a utility-maximizing strategy, such as with the sensing matrix B chosen by the controller 28 of FIG. 2 via a greedy algorithm, and the tests' thresholds y (described further below in Sections II and III). It is assumed that the complex envelope of the analog signal we are exploring is a multicomponent signal, whose components are a frequency band width equal to W=NRs. During the interval 0≤t<T the received signal is:

\(\begin{matrix}
{{y(t)} = {{x(t)} + {w(t)}}} & {{EQ}.\mspace{14mu} 1} \\
{{x(t)} = {\sum\limits_{i = 1}^{N}\; {s_{i}{x_{i}(t)}e^{{- j}\; 2\; \pi \; {R_{s}{({i - 1})}}^{t}}}}} & {{EQ}.\mspace{14mu} 2}
\end{matrix}\)

with (t)˜(0, N0δ(τ)) being additive white Gaussian noise. The components of the received signals xi(t) correspond to each primary user source, modeled as band-limited random processes with bandwidth Rs; they are equal in the mean square sense to the following process:

\(\begin{matrix}
{{x_{i}(t)} = {\sum\limits_{k = 1}^{N}\; {{x_{i}\lbrack k\rbrack}{{{sinc}\left( {\pi \left( {{R_{s}t} - k + 1} \right)} \right)}.}}}} & {{EQ}.\mspace{14mu} 3}
\end{matrix}\)

The dynamic modulator 26 modulates the received signal y(t) over the period (k−1)Ts≤t<kTs with:

βk(t)=Σi=1N√{square root over (bki)}ej(2πR(i−1)t+ϕ).  EQ. 4

to produce a modulated signal, where bki are the coefficients of the sensing matrix B and the phase ϕi accounts for the delay in generating the tone at the ith frequency plus the oscillator phase. In this regard, the dynamic modulator 26 can be implemented with a set of L voltage controlled oscillators (VCOs) 30. The sensing matrix B can therefore control a voltage level generation network 32 for the inputs to the VCOs 30 (and/or gains 34). The VCOs 30 are not required to be synchronized or phase-locked. Furthermore, the switching frequency of the VCOs 30 may also be Rs (i.e., the single channel bandwidth).

The energy detector 24 receives and samples an energy of the modulated signal. In an exemplary aspect, the energy detector 24 includes a low-pass filter (LPF) 36, which is convolved with the modulated signal. The LPF 36 may have an impulse response sinc(πRst) and outputs the filtered modulated signal c(t). The energy detector 24 also includes a sampling circuit 38, which then samples the filtered modulated signal c(t) at times kTs; k=1, . . . ,  in the single-channel baseband. This operation can be considered equivalent to an orthogonal projection, as shown below:

\(\begin{matrix}
{{c\lbrack k\rbrack} = {\left. {\left\lbrack {{y(t)}{\beta_{k}(t)}} \right\rbrack*R_{s}{{sinc}\left( {\pi \; R_{s}t} \right)}} \right|_{t = {kT}_{s}} = {\sum\limits_{i = 1}^{N}\; {\sqrt{b_{ki}}e^{j\; \varphi_{i}}Y_{ki}}}}} & {{EQ}.\mspace{14mu} 5}
\end{matrix}\)

where Yki represents the orthogonal projections over the period (k−1)Ts≤t<kTs of y(t) over the following signals:

Yki=y(t),Rsej2πR(i−1)t sinc(π(Rst−k+1)).  EQ. 6

If the periodic signals were not truncated in time, the relationship would be exact; in practice, however, there are some approximation errors due to the windowing of the signal over the prescribed interval [(k−1)Ts, kTs]. The effect of this can be mitigated by using raised cosine filtering and a non-rectangular window to reduce the effect of side lobes. Considering that the signals

{ej2πR(i−1)t sinc(π(Rst−k+1))}i,k∈Z

form an orthogonal basis, and that Equation 1 is equivalent to the following:

\(\begin{matrix}
{{x(t)} = {\sum\limits_{k = 1}^{K}\; {\sum\limits_{i = 1}^{N}\; {s_{i}{x_{i}\lbrack k\rbrack}e^{j\; 2\pi \; {R_{s}{({i - 1})}}t}{{sinc}\left( {\pi \left( {{R_{s}t} - k + 1} \right)} \right)}}}}} & {{EQ}.\mspace{14mu} 7} \\
{Y_{ki} = {{s_{i}{x_{i}\lbrack k\rbrack}} + {w_{i}\lbrack k\rbrack}}} & {{EQ}.\mspace{14mu} 8}
\end{matrix}\)

where wi[k]˜C(0; ni). If xi[k] is also modelled as i.i.d. xi[k]˜C(0; φi), then for a given state s:

Yki˜C(0,φi+N0),  EQ. 9

where φ is a vector collecting the average, unknown a priori, received signal power from the existing communications. The energy detector 24 samples for k=1, . . . , κ are as follows:

\(\begin{matrix}
{{c\lbrack k\rbrack} = {\sum\limits_{i = 1}^{N}\; {\sqrt{b_{ki}}{e^{j\; \varphi_{i}}\left( {{s_{i}{x_{i}\lbrack k\rbrack}} + {w_{i}\lbrack k\rbrack}} \right)}}}} & {{EQ}.\mspace{14mu} 10}
\end{matrix}\)

and therefore (assuming ϕi's are independent and uniformly distributed in [0, 2π)) they are also conditionally zero mean Gaussian random variables:

c[k]˜C(0,θ[k]),  EQ. 11

θ[k]=θ(bk,s)bkT(φ+n)  EQ. 12

It follows that, with reference to FIGS. 1A and 1B, the information for the detection of communications by the UEs 12 and/or base stations 14 is embedded in the variance of the sample, which is the energy received during the kth period. Sufficient statistics for the problem are as follows:

y[k]|c[k]|2  EQ 13

which are exponentially distributed, that is, y[k]˜Exp(θ[k]).

### C. Hardware Considerations

The circuit diagram of FIG. 3 assumes a settling time for the VCOs 30 much smaller than Ts (e.g., the sampling period for the single channel sub-band). If this assumption does not hold, one should use a low-pass filter with a smaller bandwidth and collect the samples c[k] at an even slower rate than Rs to wait for the VCOs to settle. This modification does not alter the statistical characterization of the samples, derived in subsection I.B above. The drawback of taking samples less often is that (assuming the same occupancy coherence time) one has accrued less information than what is available in the received signal and has less than K slots to decide. Given that the strategy is derived as a function of K, this does not invalidate the findings. Another possibility is to replace the L tunable VCOs 30 with N oscillators at constant frequencies, corresponding to the N possible bands of the signal. Using N oscillators increases the power consumption and cost of the circuit but significantly reduces the switching time between two measurements. Hence, this is the natural choice if one wants to exploit a dense sensing matrix. Instead, the use of a set of VCOs 30 is preferable if the matrices are sparse because a small number of VCOs can synthesize the mixing signal. The switching is performed by a multiplexer that takes the sum of the up to L tones selected by the vector bk.

In general, since the detection of the signal is the focus, with reasonably good device components, calibration can be expected to be either far less demanding or unnecessary, if one accepts loss in sensitivity. The binary coefficients for the vector b can be set to ones and zeros, as discussed in Section III, B. Controlling the gains 34 is unnecessary for the system to work, and it may be preferable not to add tunable gains 34 because they can be another possible source of uncertainty and complexity in the system. Finally, imperfect tuning of the VCOs 30 reduces the SNR, either by spreading or misplacing the center frequency of the components of interest, but not fundamentally impairing its detection.

### II. Optimization Framework

With reference to FIGS. 1A-3, the receiver 16 can be modeled as needing to divide K instants of time available between the sensing and the exploitation of a set ={1; 2, : : : , N} of sub-bands (e.g., channels 20 of the RF spectrum 18). A utility function of the receiver 16 accrues a reward that is a function of the underlying state vector for these items:

s[s1, . . . ,sN]∈{0,1}N  EQ. 14

where the entries si∈{0,1}, as well as the residual time available after sensing. The state variables si are indicators of good/bad (0=1) state of a resource; for the cognitive spectrum sensing application 0 would mean the channel is “idle” and 1 would mean the channel is “busy”. The receiver 16 acquires information about the entries via random observations coming from a known probability density function parameterized by an unknown vector.

During the times devoted to sensing k=1, 2, . . . , <K the receiver 16 can dynamically and adaptively design each measurement by selecting a subset of entries of s to probe through a sensing vector bk=[bk1, bk2, . . . , bkN]. The bki's will be non-zero only on the channels that are actively sensed; it is assumed the measurement provides an observation y[k] drawn from a density ƒθ[k](y) that is a function of both the choice of bk and the state s, i.e. θ[k]=θ(bk, s). It is assumed the state variables si are mutually independent Bernoulli random variables with known prior probabilities given by a vector ω=[ω1, ω2, . . . , ωN] where ωi=P(si=0). As described further in Section III below, the receiver can be designed with:


- - 1) the
    ×N measurement matrix B (exploration phase)
  - 2) a set of N decision rules δ={δ_(i)∈{0,1}: i=1, 2, . . . , N} over
    the unknown states s_(i) of the resources (at the end of the
    exploration phase).  
    Notice that the design of B includes:
  - the measurement vectors b_(k) for each test at time k=1, 2, . . . ,
    (matrix rows),
  - the sensing (exploration) time
    to acquire information on the states s_(i) via the observations
    y\[k\] (number of rows).

The total utility for the receiver 16 will be proportional to the time left for exploitation (K−k). A reward ri>0 can be used for correctly detecting an empty/busy resource and a penalty pi<0 for failing to detect a busy/empty resource. The utility of the detection function can be written as:

\(\begin{matrix}
{{U\left( {s,,K,B,\delta}\; \right)}\overset{\Delta}{=}\left\{ \begin{matrix}
{{\left( {K - k} \right){\sum\limits_{i = 1}^{N}\; {\omega_{i}{r_{i}\left( {1 - \alpha_{i}} \right)}}}} + {\left( {1 - \omega_{i}} \right)p_{i}\beta_{i}}} & {{case}\mspace{14mu} 0} \\
{{\left( {K - k} \right){\sum\limits_{i = 1}^{N}\; {\left( {1 - \omega_{i}} \right)\left( {1 - \beta_{i}} \right)r_{i}}}} + {\omega_{i}\alpha_{i}p_{i}}} & {{case}\mspace{14mu} 1}
\end{matrix} \right.} & {{EQ}.\mspace{14mu} 15}
\end{matrix}\)

where αi; βi denote the type I and type II errors probability respectively (e.g., αi=P(δi=1|si=0) and βi=P (δi=0|si=1).

To differentiate between case 0 and case 1 allows to consider applications where the utility comes from an action on the entries detected as empty/busy: e.g., in a spectrum sensing application, the utility would come from the decision on transmitting over frequency bands found empty, whereas for a RADAR application, it makes more sense to consider the utility comes from taking action on the frequency (spatial directions) found busy. Finding the optimal policy corresponds to solving the following optimization problem:

maxB,δ[U(s,,K,B,δ)]  EQ. 16

This approach can be modified to fit different observation models and assumptions, but as an example this disclosure considers the following form for the function θ:

θ[k]=θ(bk,s)=bk(φT+wT)  EQ. 17

where φ=[φ1, φ2, . . . , φN] is a non-negative vector, such that the state variable si=1 when φi>0 and 0 when φi=0. The vector w=[w1, w2, . . . , wN] models a generic additive system noise. An exemplary aspect of this disclosure concerns the detection of the non-negative entries of φ and consequently the maximization of the utility accruable from the resources declared to be in the empty/busy state (Equation 15). The observation model also assumes that ƒθ[k](y)≡Exp(θ[k]), i.e.:

\(\begin{matrix}
{{{y\lbrack k\rbrack} \sim {f_{\theta {\lbrack k\rbrack}}(y)}} = {\frac{1}{\theta \lbrack k\rbrack}e^{- \frac{y}{\theta {\lbrack k\rbrack}}}}} & {{EQ}.\mspace{14mu} 18}
\end{matrix}\)

where, for convenience, the alternative parameterization for the exponential distribution is generally used herein. In the context of RF spectrum sensing, this choice of distribution models the energy of complex circularly symmetric signal samples in each sub-band with zero mean and variance φi embedded in additive white Gaussian noise with variance w1.

### III. Dynamic Design of Sensing Matrices

**A. Direct Inspection Case**

In the direct inspection (DI) case, bk is limited to only one non-zero entry i, that is, bki≠0, bkj=0 ∀j≠i. This means that there is an underlying hypothesis testing:

0: y[k]˜Exp(θ0[k])

1: y[k]˜Exp(θ[k])

with θ0[k]=bkini and θ[k]=bki(φi+ni)>θ0[k]. In this context, it is known that the signal energy is a sufficient statistic for the test and the energy detection is optimal. Assuming no prior knowledge over the φi's in case of existing communication, to set the test threshold alone is needed, which is set in order to maximize the utility defined in Equation 15. Defining θ*[k]=max{y[k], bki(φmin+ωi)} obtains the following:

\(\begin{matrix}
{{y\lbrack k\rbrack}_{\begin{matrix}
 < \\
H_{0}
\end{matrix}}^{\begin{matrix}
H_{1} \\
 > 
\end{matrix}}\frac{\ln \left( {\gamma_{i}\frac{\theta*\lbrack k\rbrack}{\theta_{0}}} \right)}{\frac{1}{\theta_{0}} - \frac{1}{\theta*\lbrack k\rbrack}}} & {{EQ}.\mspace{14mu} 19} \\
{\gamma_{i}\overset{\Delta}{=}\left\{ \begin{matrix}
\frac{r_{i}\omega_{i}}{{\rho_{i}}\left( {1 - \omega_{i}} \right)} & {{case}\mspace{14mu} 0} \\
\frac{\left. {{\rho_{i}}\omega_{i}} \right)}{r_{i}\left( {1 - \omega_{i}} \right)} & {{case}\mspace{14mu} 1}
\end{matrix} \right.} & {{EQ}.\mspace{14mu} 20}
\end{matrix}\)

Notice that, assuming a minimum average received signal power of φmin>0 in the case of existing transmission, this makes the test meaningful also for values of γi<1.

Assumption 1:

To simplify the decision problem, every resource is assumed to be sensed before being declared empty/busy. This can be enforced as a standard/protocol rule or numerically guaranteed by setting ∀i∈,

\(\omega_{i} < {\frac{\rho_{i}}{\rho_{i} + r_{i}}\mspace{11mu} {\left( {{case}\mspace{14mu} 0} \right)/\omega_{i}}} > {\frac{r_{i}}{{\rho_{i}} + r_{i}}\mspace{11mu} {\left( {{case}\mspace{14mu} 1} \right).}}\)

It is clear that the optimality of the test completely characterizes the set of decision rules δ for the sensed resources, while Assumption 1 gives the decision rule for the non-sensed resources. This implies that for the DI case, the optimization in Equation 16 can be expressed solely in terms of B. It is also known that for this type of text, where there is uncertainty in a parameter of the alternative hypothesis, one does not know the exact miss probability β, thus an upper-bound is used, which reflects in a lower bound for the achievable utility. Since this test is part of the DI strategy, the superscript DI is added to the test error probabilities αi and βi as follows:

\(\begin{matrix}
{\alpha_{i}^{DI} = {\min \left\{ {\left( \frac{{\rho_{i}}\left( {1 - \omega_{i}} \right)}{r_{i}{\omega_{i}\left( {1 + \frac{\phi \; \min}{n_{i}}} \right)}} \right)^{\frac{1 + \frac{\phi \; \min}{n_{i}}}{\frac{\phi \; \min}{n_{i}}}},1} \right\}}} & {{EQ}.\mspace{14mu} 21} \\
{\beta_{i}^{DI} = {1 - {\left( \alpha_{i}^{DI} \right)^{\frac{1}{1 + \frac{\phi_{i}}{n_{i}}}}.}}} & {{EQ}.\mspace{14mu} 22}
\end{matrix}\)

The above shows that the false alarm probability is independent from the alternative hypothesis, whereas the detection improves with the true average transmitted power φi. What can be guaranteed, since φi≥φmin, is that

\(\begin{matrix}
{{\beta_{i}^{DI} \leq {1 - \left( \frac{\rho_{i}\left( {1 - \omega_{i}} \right)}{r_{i}{\omega_{i}\left( {1 + \frac{\phi_{\min}}{n_{i}}} \right)}} \right)^{\frac{n_{i}}{\phi \; \min}}}} = \beta_{i,\max}^{DI}} & {{EQ}.\mspace{14mu} 23}
\end{matrix}\)

The threshold in Equation 20 is the optimal threshold that minimizes the Bayesian risk (maximizes the utility) for the binary case, when ωi is known. It is common practice to replace the maximum likelihood estimate for the unknown ωi (Generalized Likelihood Ratio Test (GLRT)) and then reduce to the binary case using the same threshold. A local, more powerful test exists for θ→θ0, but GLRT is preferred for its high SNR range.

Note that the test performance for the DI case does not depend on bki; therefore, for the DI case no further optimization is needed over the sensing matrix B other than selecting the non-zero entries.

Under Assumption 1, the optimization problem in Equation 16 can be rewritten for the DI case as follows:

\(\begin{matrix}
{\underset{ \subseteq }{maximize}\mspace{11mu} {U^{DI}()}} & {{EQ}.\mspace{14mu} 24} \\
{{U^{DI}()}\overset{\Delta}{=}{\left( {K - {}} \right){\sum\limits_{i \in A}\; u_{i}^{DI}}}} & {{EQ}.\mspace{14mu} 25} \\
{u_{i}^{DI}\overset{\Delta}{=}{{\omega_{i}{r_{i}\left( {1 - \alpha_{i}^{DI}} \right)}} - {\left( {1 - \omega_{i}} \right)\rho_{i}\beta_{i,\max}^{DI}}}} & {{EQ}.\mspace{14mu} 26}
\end{matrix}\)

The following lemma is then introduced:

Lemma 1:

UDI() is a normalized, non-monotone, non-negative sub-modular function of .

Lemma 1 implies that there are diminishing returns in augmenting sets by adding a certain action to bigger and bigger sets. The maximization of a non-monotonic sub-modular function is generally NP-hard, but the case of interest is not as difficult. By sorting the resources i so that

u1DI≥u2DI≥ . . . ≥uNDI  EQ. 27

the set of size i, i={1, . . . , i} will be such that for any set X of size |X|=i, so that

\({\sum\limits_{k = 1}^{i}\; u_{k}^{DI}} \geq {\sum\limits_{k \in X}^{\;}\; {u_{k}^{DI}.}}\)

Therefore, what remains is to find the best set size i such that

\(\begin{matrix}
{{{U^{DI}()} \leq {U^{DI}\left( _{i} \right)} \leq_{i}^{\max}\left( {\left( {K - i} \right){\sum\limits_{k = 1}^{i}\; u_{k}^{DI}}} \right)}\mspace{14mu}} & {{EQ}.\mspace{14mu} 28}
\end{matrix}\)

The maximum in Equation 28 is attained for the following:

i*=iinf{i: ∂i+1UDI(i)<0}  EQ. 29

where

∂i+1UDI(i)=(K−i)ui+1DI−Σk=1i+1ukDI.

Given that the function is sub-modular, as soon as this condition is attained, it is maintained for i+2, i+3, and so on, given that the marginal returns continue to decrease. This maximization is greedy and stops when the marginal reward becomes negative.

**B. Group Testing Approach**

The test is now allowed to mix different sub-bands, that is, the vector bk to have more than one non-zero entry. The main idea of this section is to develop a dynamic simple strategy that can be characterized in closed form, and gives a sufficient condition to claim a group testing (GT) strategy would outperform the DI alternative. From the sensing matrix B, the sets k={i∈: bki≠0} and i={1≤k≤: bki≠0} can be defined. The convention is used that, whenever bk is the argument of a function, then the set k is also the argument of that function. Similarly, when B is the argument of a function, then all the sets k for 0≤k≤−1 and all the sets i for i∈ are arguments of that function as well.

As outlined previously, aliasing of the spectrum comes with an associated noise-folding phenomenon. The effect is particularly severe in a non-coherent scheme such as that of the present disclosure. The samples are collected sequentially and not in parallel, which means that there are no multiple observations of the same value but only sequential observations tied to the same underlying random process.

To mitigate the noise-folding effects and reduce the hardware complexity, the method of the present disclosure focuses on low-density measurement matrices. The goal is to develop a relatively simple dynamic strategy for choosing a sensing matrix the utility of which can be expressed in closed form and that outperforms the DI alternative. A common approach for recovery with low-density measurement matrices is to use belief propagation via message passing, the most well-known application of which is low-density parity check (LDPC) optimum error correction decoding.

For LDPC (and compressive sensing methods), performance guarantees come as asymptotic bounds on the 2-norm, but little is known for optimal design in the finite regime. A difficulty in the design arises from the inherent multi-hypothesis testing problem associated with sensing several resources at the same time. This is why, to develop the dynamic design according to the present disclosure, a GT approach allows consideration of a binary hypothesis test for each measurement. In this way, the complexity of the analysis is relatively low, and the expected performance for any sensing matrix can be derived under mild assumptions. In the model of the present disclosure, an uninformative prior can be assigned to the φi's to run the belief propagation message-passing algorithm on the obtained measurements. Prior to providing more details, a remark regarding related GT approaches is in order.

Note that in the context of GT, little is known in presence of measurement errors that depend on the group size, which is the scenario the present disclosure considers. In the model of the present disclosure, the false alarm and misdetection probabilities depend on the optimization of the test threshold; therefore, the noise is not independently added, nor can an independent dilution be considered. Furthermore, the strategy derived depends on the finite horizon for K; that is, the results are not asymptotic.

For each test a binary group test is defined as follows:

\(\begin{matrix}
\left\{ \begin{matrix}
{H_{0}\text{:}} & {{\forall{i \in {_{k}\mspace{25mu} s_{i}}}} = 0} \\
\; & {\left. \Rightarrow{\theta_{0}\lbrack k\rbrack} \right. = {b_{k}^{T}n}} \\
{H_{1}\text{:}} & {{\exists{i \in {_{k}\mspace{14mu} {s.t.\mspace{14mu} s_{i}}}}} = 1} \\
\; & {\left. \Rightarrow{{\theta \lbrack k\rbrack} \geq {{\left. (_{i}^{\min}b_{ki} \right)\phi_{\min}} + {b_{k}^{T}n}}} \right. = {\theta_{\min}\lbrack k\rbrack}}
\end{matrix} \right. & {{EQ}.\mspace{14mu} 30}
\end{matrix}\)

Such a test is envisioned to be useful for a downlink transmission in which the access point may want to allow multiple communications at the same time and can alert the signal units over a narrowband signaling channel to access the spectrum.

It is important to highlight that the two hypotheses pertain exclusively to the group of sub-bands explored in test, that is, k, not the whole spectrum. Also note that this GT approach pertains to the design of the sensing matrix and detection algorithm and not to the underlying observation model. The different approaches against which the method of the present disclosure is compared subsequently use detection strategies that are multi-hypothesis tests.

The test can be written as follows:

\(\begin{matrix}
{\frac{\begin{matrix}
\max & {f_{\theta {\lbrack k\rbrack}}\left( {y\lbrack k\rbrack} \right)} \\
{{\theta \lbrack k\rbrack} \geq {\theta_{\min}\lbrack k\rbrack}} & \;
\end{matrix}}{{{f_{\theta}}_{0}\lbrack k\rbrack}\left( {y\lbrack k\rbrack} \right)}\begin{matrix}
\begin{matrix}
H_{1} \\
 < 
\end{matrix} \\
\begin{matrix}
 > \\
H_{0}
\end{matrix}
\end{matrix}\gamma \; k} & {{EQ}.\mspace{14mu} 31}
\end{matrix}\)

for which the following can be derived:

\(\begin{matrix}
{{\alpha \left( {b_{k},\gamma_{k}} \right)} = \left( \frac{1}{\gamma_{k}\frac{\theta_{\min}}{\theta_{0}}} \right)^{\frac{\frac{\theta_{\min}}{\theta_{0}}}{\frac{\theta_{\min}}{\theta_{0}} - 1}}} & {{EQ}.\mspace{14mu} 32} \\
{{\beta \left( {b_{k},\gamma_{k}} \right)} = {1 - \left( {\alpha \left( {b_{k},\gamma_{k}} \right)} \right)^{\frac{\theta_{0}}{\theta_{\min}}}}} & {{EQ}.\mspace{14mu} 33}
\end{matrix}\)

The decision declares that resource i is busy (l is true) if the majority of the tests where resource i is involved is positive, else it accepts the null hypothesis 0 for resource i. Thus:

\(\begin{matrix}
{{\pi_{0}\left( {i,b,\gamma} \right)} = {{\left( {1 - {\prod\limits_{j \in {A_{k}\backslash i}}\omega_{j}}} \right)\left( {1 - {\beta_{i}\left( {b,{\gamma;0}} \right)}} \right)} + {{\alpha \left( {b,\gamma} \right)}{\prod\limits_{j \in {A_{k}\backslash i}}\omega_{i}}}}} & {{EQ}.\mspace{14mu} 34} \\
{\mspace{79mu} {{\pi_{i}\left( {i,b,\gamma} \right)} = {1 = {\beta_{i}\left( {b,{\gamma;1}} \right)}}}} & {{EQ}.\mspace{14mu} 35}
\end{matrix}\)

where the functions πi(i, b, γ), j=0, 1 are only defined when bi≠0. These functions represent the probabilities of declaring 1 in a group-test defined by b with threshold γ and given si=j, j=0, 1. Notice that the error probabilities α, β refer to each binary hypothesis testing defined in Equation 30. The notation for βi(b, γ; si) indicates the probability of having a missed-detection conditioned on the state si of one of the resources. It then follows that

\(\begin{matrix}
{{\alpha_{i}^{GT}\left( {B,\gamma} \right)}\overset{\Delta}{=}{1 - {F_{PBD}\left( {{{\left\lceil \frac{B_{i}}{2} \right\rceil - 1};{B_{i}}},\left\{ {{\pi_{0}\left( {i,b_{k},\gamma_{k}} \right)}:{k \in B_{i}}} \right\}} \right)}}} & {{EQ}.\mspace{14mu} 36} \\
{{\beta_{i}^{GT}\left( {B,\gamma} \right)}\overset{\Delta}{=}{F_{PBD}\left( {{{\left\lceil \frac{B_{i}}{2} \right\rceil - 1};{B_{i}}},\left\{ {{\pi_{1}\left( {i,b_{k},\gamma_{k}} \right)}:{k \in B_{i}}} \right\}} \right)}} & {{EQ}.\mspace{14mu} 37}
\end{matrix}\)

where FPBD(k; n; p) indicates the cumulative distribution function of a Poisson binomial distribution parameterized by p∈[0; 1]n. One can then replace Equations 36 and 37 in Equation 15 to solve the optimization in Equation 16, where the equivalence between the decision rules δ and the selection of the thresholds γ is essentially the same as for the DI case.

Notice that in order for Equations 36 and 37 to hold, each of the tests must be independent, conditioned on the state of the resource i. This is true if the sensing matrix, in the language used for LDPC codes, does not have length-4 cycles; that is, two different measurements do not mix more than one sub-band in common. Such a condition is typically required for belief propagation algorithms, for example, message passing, which suffer from loopy networks with short cycles.

The optimization remains extremely complex due to the complexity of the decision space for B and the sum of an exponentially growing number of terms for the probabilities defined in Equations 36 and 37. Nevertheless, it gives a method to evaluate the objective of the optimization for any sensing matrix B, where the optimization over γ can be numerically solved. Equations 36 and 37 are monotonic functions of the probabilities π0, π1 defined in Equations 34 and 35, which are monotonic in the γk 's, and therefore a unique solution for γ exists. Next, additional constraints to Equation 16 are introduced, in particular on the structure of B, in order to evaluate whether GT strategy is superior to the DI approach.

Note that a maximum likelihood (ML) or a maximum a posteriori probability estimator, for a rank-deficient sensing matrix, does not provide optimality guarantees in terms of minimum error probability or minimum Bayesian risk. Nevertheless, for the same sensing matrix, the maximum a posteriori probability estimator is expected to outperform the binary GT hypothesis in Equation 30 by simply adding more degrees of freedom to the decision in the κ-th dimensional space of the observations. Therefore, the evaluation of the objective in Equation 16 via Equations 36 and 37 provides a benchmark for the utility obtainable with a more refined detection method.

1. The pairwise tests case: To start, matrices B are considered that have the following property: each resource is sensed only one time, either directly inspected or mixed with another resource, and no test mixes more than two resources, that is, |k|≤L=2, ||≤1 ∀k=1, . . . , κ, i=1, . . . , N. Consider the test that mixes entries i and j. According to the strategy derived at the beginning of the section, one can use Equations 34, 35, 36, and 37 to write out the per-time instant utility obtainable after the decision. First, from Equation 30, without prior knowledge over φi, φj other than the threshold φmin, the best choice to minimize α is to set bi=bj. This false alarm probability is referred to as αij). Therefore, similar to the DI case, one can consider binary coefficients for bk, that is, bki≠0→bki=1. This holds true also for the extension of L>2 and gives implementation advantages as discussed in Section I, B.

A missed detection event in Equation 30 can occur for three different states of the resources i, j; an upper-bound for the corresponding miss detection probability is established by always considering θ=θmin and is referred to as βij,max. What is obtained is the following:

uijGTωiωj(ri+rj)(1−αij)+[(ωi(1−ωj)(ri+ρ1)+ωj(1−ωi)(rj+ρi)+(1−ωi)(1−ωj)(ρi+ρj))]βij,max  EQ. 38

where the threshold for this test γij has been set to maximize Equation 38, that is,

\(\begin{matrix}
{\gamma_{ij} = {\frac{\omega_{i}{\omega_{j}\left( {r_{i} + r_{j}} \right)}}{{\left( {1 - \omega_{i}} \right)\left( {{\rho_{i}} - {\omega_{j}r_{j}}} \right)} + {\left( {1 - \omega_{j}} \right)\left( {{\rho_{j}} - {\omega_{i}r_{i}}} \right)}}.}} & {{EQ}.\mspace{14mu} 39}
\end{matrix}\)

Consider then a graph in which each resource is a vertex and the edge weight uij between two vertices ij is the utility (per time instant) uijGT just defined. The weight of the loops uiiGT are given by uiDI in Equation 26. The problem can then be translated into a particular instance of a max-cut problem: picking a subset of the edges and forming a subgraph, in which each edge represents a test, to maximize the objective in Equation 16. Formally, the equation can be written as follows:

\(\begin{matrix}
\begin{matrix}
\begin{matrix}
{maximize} \\
ɛ
\end{matrix} & {U^{GT}(ɛ)} \\
{{subject}\mspace{14mu} {to}} & {{\deg \; {ɛ(i)}} \leq {i\mspace{14mu} {\forall{i \in }}}}
\end{matrix} & {{EQ}.\mspace{14mu} 40} \\
{where} & \; \\
{{U^{GT}(ɛ)}\underset{\Delta}{=}{\left( {K - {ɛ}} \right)\left( {\sum\limits_{{ij} \in ɛ}u_{ij}^{GT}} \right)}} & {{EQ}.\mspace{14mu} 41}
\end{matrix}\)

and degε(i) is the nodal degree of node i induced by the undirected graph =(, ε). It is possible to map the constraint on the nodal degree in the objective of Equation 40 by adding a penalty for the violation of such constraint. This guarantees that the optimal solution will be equivalent to Equation 40, that is, no set of edges that violates the constraint can improve the objective, and any feasible set of edges would have the same objective in the two problems. The optimization can be rewritten as follows:

\(\begin{matrix}
{{\begin{matrix}
{maximize} \\
ɛ
\end{matrix}{U^{GT}(ɛ)}} - {M{\sum\limits_{i \in N}^{\;}\; {\mathrm{\Upsilon}\left( {\deg \; {ɛ(i)}} \right)}}}} & {{EQ}.\mspace{14mu} 42} \\
{where} & \; \\
{{\mathrm{\Upsilon}(n)}\overset{\Delta}{=}\left\{ \begin{matrix}
0 & {{{for}\mspace{14mu} n} \leq 1} \\
{n - 1} & {{{for}\mspace{14mu} n} \geq 2}
\end{matrix} \right.} & {{EQ}.\mspace{14mu} 43}
\end{matrix}\)

and M is a positive constant.

Lemma 2:

For M>0, the objective in Equation 42 is a non-monotone sub-modular function of ε, and it is possible to find M*>0 such that for any M>M* the two optimizations of Equations 40 to 42 are equivalent.

The extension of this result for L>2 can now be discussed to develop a general algorithm that leverages the sub-modularity of the optimum design problem in Equation 40.

2. Extension to L>2: If more than two channels are mixed, instead of just edges or self-loops to indicate the tests, cycles of length can be obtained up to L. The nodal degree in Equation 42 then is interpreted as the number of cycles to which a node belongs, and the set of edges is replaced with the set of cycles. The set ε of edges is then replaced with the set C of possible cycles, and use c to indicate the generic cycle, which could be a self-loop, an edge, or a cycle with length 3 or greater. With these substitutions the proof of sub-modularity in Lemma 2 naturally extends to this case as well. In light of the constraint |i|≤1, no node can be in two cycles.

3. The factor approximation of the greedy algorithm: Having proved the sub-modularity of Equation 42 in Lemma 2, it is natural to resort to a greedy procedure; however, it is important to highlight that the objective in Equation 42 does not respect the non-negativity property. Due to the particular structure of the problem, it is possible to find a factor approximation for the output of the greedy algorithm.

Lemma 3:

Algorithm 1 guarantees an α-constant factor approximation of the optimal solution for Equation 42, where

\(\begin{matrix}
{\alpha = {\frac{1}{\min \left\{ {L_{eff},\frac{K}{2}} \right\}}{\frac{K - 1}{K - {\min \left\{ {L_{eff},\frac{K}{2}} \right\}}}.}}} & {{EQ}.\mspace{14mu} 44}
\end{matrix}\)

Note that

\(\begin{matrix}
{{\partial_{C^{\prime}}{U^{GT}{()}}} = {{\sum\limits_{C \in}^{\;}\; u_{C}} + {\left( {K - {} - 1} \right)u_{C^{\prime}}}}} & {{EQ}.\mspace{14mu} 45}
\end{matrix}\)

so, as long as the number of tests |C| added in the greedy maximization is less than the time horizon K, then

{ arg   max C ∈ C  ∂ C  U GT  ( ) = arg   max C ∈ C  u C . EQ .
 46 }

This relation indicates that, in the greedy procedure, edges are added in decreasing order of utility, respecting the constraint on the nodal degree in light of Lemma 2. Also, from Equation 45, it is easy to find that the optimal |C| never exceeds

\(\left\lceil \frac{K - 1}{2} \right\rceil.\)

In the greedy procedure in Algorithm 1, there is a constant number of operations per query, which indicates the overall complexity of the algorithm is dominated by the sorting of all possible cycles' utilities. In the worst case, sorting n values require O(n2) operations, thus the complexity is given by

\({0\left( \left( {\sum\limits_{ = 1}^{L}\left( \frac{n}{} \right)} \right)^{2} \right)},\)

that is, polynomial in N and exponential in L.

**C. Additional Applications of the Stochastic Optimization**

The analysis for the factor approximation of the greedy strategy transcends the spectrum-sensing application discussed in the present disclosure. Group testing has been applied to a number of disparate contexts to model the outcome of sequential tests. As long as one has a way to define the per-time utility derived from each test as in Equation 38 and an overall utility as in Equation 41, then the results of the present disclosure can be applied. Classes of problems that can be formulated in a similar way include job scheduling for data centers, design of parity checks for rateless coding, and dynamic advertisement that promotes an offer that bundles two products/services together, for example. Obviously, in all these cases the statistics of the observations are radically different.

### IV. Approximate Maximum Likelihood Estimate for Mixed Tests

The previous sections have provided methods that find a low-density measurement matrix. As will be apparent in the numerical results in Section V, the noise-folding phenomenon justifies the use of sparse-sensing matrices. They are also ideal when one wants to apply belief propagation to the decision problem. However, for the sake of comparison, an approach is proposed here which can be applied to any measurement matrix B and that can be mapped into previous solutions.

Assume that K measurements have been collected, by mixing a set ⊆ of sub-bands. One could ignore the prior ωi and derive the maximum likelihood (ML) estimate for φ. The log-likelihood function is as follows:

\(\begin{matrix}
{{\log \left( {f\left( y \middle| \phi_{A} \right)} \right)} = {{{- {\sum\limits_{k = 1}^{\kappa}{\log \; {\theta \lbrack k\rbrack}}}} + \frac{y\lbrack k\rbrack}{\theta \lbrack k\rbrack}}\overset{{\theta {\lbrack k\rbrack}}\rightarrow{y{\lbrack k\rbrack}}}{\approx}{{- {\sum\limits_{k = 1}^{\kappa}1}} + {\log \mspace{14mu} {y\lbrack k\rbrack}} + {\frac{1}{2}\left( \frac{{y\lbrack k\rbrack} - {\theta \lbrack k\rbrack}}{y\lbrack k\rbrack} \right)^{2}}}}} & {{EQ}.\mspace{14mu} 47}
\end{matrix}\)

where the linearization corresponds to the Taylor expansion of the likelihood function around the observations mean (recall Equations 14 and 15). A possible approach consists in solving the following LASSO problem:

\(\begin{matrix}
{{\hat{\phi}}_{A} = {{\begin{matrix}
{\arg {\mspace{11mu} \;}\min} \\
\phi_{A}
\end{matrix}{{\lambda_{A}\phi_{A}^{T}}}_{1}} + {\frac{1}{2}{\left( {y - {B\left( {\phi_{A}^{T} + n_{A}^{T}} \right)}} \right)}_{C^{- 1}}^{2}}}} & {{EQ}.\mspace{14mu} 48}
\end{matrix}\)

with C=diag(y) denoting the covariance of the observations and  the vector of weights for the weighted 1-norm. The first penalty term in the objective enhances sparsity, while the second term comes from the ML estimate in Equation 47. To incorporate the information of the prior beliefs ωi, one can set λi=i from Equation 20, ∀i∈, to favor the estimates φi>0 for entries with lower thresholds γi. Alternatively, one can also set λi=λ∀i∈.

### V. Simulation Results

This section showcases the ability of the approach of the present disclosure to dynamically switch between a DI receiver (scanning receiver) and a GT approach, based on the expected occupancy (the vector of priors ω), the time available K, the minimum SNR threshold

\({{SNR}_{\min} = \frac{\phi min}{w}},\)

and the number of resources N. In the context of spectrum sensing (case 0), the parameters ri and ρi can be mapped into a maximization of the overall weighted network throughput: the reward ri can be proportional to the achievable rate over the channel i in the absence of primary user communications, that is, ri ∝log(1+SNRi,S), where the suffix S indicates the secondary communication, whereas the penalty ρi can be made proportional to the loss in rate caused to the primary communication due to the interference added by the secondary.

For the cognitive radio application, the concept of exploitation of the resource is tied to the definition of utility function chosen in Equation 15, which is expressed in bits /s/ . From Equations 15 and 16, ri's and ρi's can be normalized over the communication bandwidth without altering the optimization. The longer the time available to transmit, the larger the number of bits that can be transmitted over that band.

For the other case, that is, when the reward comes from detecting correctly which resources are busy, for example, a RADAR application, it is not immediately clear why the utility would be proportional to the number of remaining time instants. To interpret this, the action upon declaration of si=1 is modelled as a Bernoulli trial that accrues a reward ri if such action is successful, that is, the target is actually hit, and this happens with a certain probability ρi for each attempt. The number of attempts Ti necessary to hit the target is then geometrically distributed. One can find then that the expected reward is equal to

riP(Ti≤(K−κ))=riΣk−1K-κρi(1−pi)k−1=ri(1−(1−pi)K-κ)≈(K−κ)ripi

for small pi, which would motivate having an expected utility that increases linearly with time. The ρi associated with this case models an intervention cost, the main purpose of which is to limit the false alarm rate.

It is important to highlight, however, that the time dependency in the optimization objective prevents the formulation from returning to a standard constant false alarm rate (CFAR) detection method. Nevertheless, the model can apply to electronic warfare (tentatives of creating jamming), wake-up radio, and other problems where the action (and the associated utility) is on the channels that are declared busy. For all the figures, reference is made to L=2, 3 as the maximum number of resources per test allowed in the greedy procedure in Algorithm 1. Theoretically, the optimal value for UGT monotonically increases with L since increasing L introduces additional degrees of freedom. However, the simulations used the greedy solution and, as proved in Lemma 3, the approximation factor of the greedy maximization is potentially worse for higher values of L, as the following numerical results show.

“Group Testing” indicates the utility obtained with the GT approach. The maximum a posteriori probability estimator (MAP estimator) is the estimator that knows the true values Φi, uses the same matrix B of the GT approach, but then decides on each resource based on the posterior for ωi, using belief propagation.

1. Spectrum sensing vs. RADAR: Even though in light of the symmetry in the definition of the threshold γi one can switch the r's and ρ's to go from spectrum sensing (case 0) to RADAR (case 1) and find the same trends, even for the combined tests, to avoid confusion, the difference in the two scenarios is highlighted in the first simulation presented in FIGS. 4A and 4B.

FIG. 4A is a graphical representation comparing utility for different optimization approaches for the spectrum sensing application. FIG. 4B is a graphical representation comparing utility for different optimization approaches for the RADAR application.

For the experiment in FIGS. 4A and 4B, the following were set−K=30, N=60, and ri=r, ρi=ρ, and ωi=ω, SNRi=SNRmin(10 dB) ∀i−—so that we have that for ω equal to

\(\frac{\rho}{\rho + r}\mspace{14mu} {or}\mspace{14mu} \frac{r}{\rho + r}\)

for case 0 and case 1, respectively. These are the threshold values given in Assumption 1 to guarantee that no resource can give positive utility if not tested. In both scenarios the utility increases with the ratio

\(\frac{\rho}{r},\)

since the prior probability that favors a positive utility function increases as well for both the spectrum-sensing and RADAR applications.

However, the gain for the GT approach over the DI approach happens in complementary ranges: when

\(\frac{\rho}{r} > 1\)

for the spectrum-sensing application and when

\(\frac{\rho}{r} < 1\)

in the RADAR application. When the penalty increases with respect to the reward, the GT approach for spectrum sensing is conservative and does not transmit in any of the channels in a group that tested positively; nevertheless, as the priors ωi increase, it is possible to find multiple empty sub-bands with just one test and gain in utility compared with the DI approach.

For the RADAR application, when the penalty increases with respect to the reward, there is a disadvantage in declaring as busy all the elements in the test, even if the prior ω decreases. Clearly, this limits the benefit of combined tests, whereas when

\(\frac{\rho}{r}\)

decreases, there is a gain since one element found busy in the pool guarantees higher reward. Apart from this asymmetry, both cases show the same trends in utility over the number of available resources N, and the value of SNRmin.

2. Utility for different N: FIG. 5A is a graphical representation comparing utility for different optimization approaches versus a ratio horizon K over a number of resources N with the horizon K equal to 10. FIG. 5B is a graphical representation comparing utility for different optimization approaches versus the ratio horizon K over the number of resources N with the horizon K equal to 30.

FIGS. 5A and 5B thus plot the utility (normalized over K2) over the ratio

\(\frac{K}{N}\)

for two different horizons, that is, K=10 and K=30 and SNRmin=10 dB. Only for

\({\frac{K}{N}\overset{<}{\approx}0.75},\)

the GT approach outperforms all competing options, whereas when the horizon K increases, almost no benefit comes from mixing resources. This suggests that there is enough time to test them independently with high accuracy. This experiment looked at case 0 and set

\({\omega_{i} \sim \left( {0.7,\frac{\rho \; i}{\rho_{i} + r_{i}}} \right)},{where}\)
\(r_{i} = {{{\log \left( {1 + {SNR}_{i,S}} \right)}\mspace{14mu} {and}\mspace{14mu} \rho_{i}} = {{5r_{i}\mspace{14mu} {with}\mspace{14mu} {SNR}_{i,S_{dB}}} \sim {{\left( \left\lbrack {10,20} \right\rbrack \right)}.}}}\)

The SNR for the test,

\(\frac{\phi_{i}}{n_{i}},\)

is generated uniformly between 10 dB and 20 dB; recall that the only information used in the algorithm is the minimum SNR value, that is, in this case 10 dB. In the regime considered, the DI approach is approximately constant since it is easy to show

\(U^{{DI},{OPT}} \leq {\frac{K^{2}}{4}u_{\max}}\)

irrespective of N.

3. Utility for different SNRmin: FIG. 6A is a graphical representation comparing utility for different optimization approaches versus the minimum SNR with the horizon K equal to 30. FIG. 6B is a graphical representation comparing utility for different optimization approaches versus the minimum SNR with the horizon K equal to 10. This set of experiments studied how the utility behaves versus the minimum SNR in each active sub-band. In this case the SNR was drawn uniformly between SNRminand SNRmin+10, and once again only the value of

\({SNR}_{\min} = \frac{\phi_{\min}}{w}\)

was used in the optimization, which is shown in the abscissa of the figures. Matching intuition, the GT approach outperformed the DI approach only when SNRmin was sufficiently high and the gain in utility was larger for K=10 than for K=30.

For this experiment the number of resources was fixed to N=20 and, as previously highlighted, increasing K for fixed N diminishes the benefit of combining resources in a test. In this case the utility was also plotted that was obtainable with the approximate ML estimate obtained via compressive sensing, described in Section IV. For this case, to illustrate the noise-folding issue, a dense matrix that had the same aspect ratio of the one found via the GT approach was used, that is, one that scans the same set of resources for the same number of tests.

To show reasonable results, only for the ML estimate via compressive sensing, the mean of y[k] over 10 samples was taken. Despite having more measurements, such approach gives a much lower utility than the DI and the GT approach of the present disclosure due to the negative effect of noise folding. For K=30, the approach of the present disclosure was also compared with the performance obtained using belief propagation in a loopy network and an LDPC matrix. Considering N=20 resources and an expected sparsity approximately equal to 4, a regular LDPC matrix was chosen with a row weight of 5 and a column weight of 3, resulting in 12 tests. The LDPC was not implemented for K=10 since the constraints on the regularity would have given either a diagonal matrix (same as DI) or a relatively dense matrix. The absence of any optimization in the choice of which and how many resources to test produces a utility that, for low SNR, is lower than the DI approach proposed. For a high enough SNR, the LDPC design can outperform the DI approach but still gives a utility lower than the GT strategy with L=2. This highlights the benefit of having an active sub-Nyquist receiver compared with a static offline selection of the parameters.

The various illustrative logical blocks, modules, and circuits described in connection with the embodiments disclosed herein may be implemented or performed with a processor, a digital signal processor (DSP), an application specific integrated circuit (ASIC), a field programmable gate array (FPGA), or other programmable logic device, a discrete gate or transistor logic, discrete hardware components, or any combination thereof designed to perform the functions described herein. Furthermore, a controller may be a processor. A processor may be a microprocessor, but in the alternative, the processor may be any conventional processor, controller, microcontroller, or state machine. A processor may also be implemented as a combination of computing devices (e.g., a combination of a DSP and a microprocessor, a plurality of microprocessors, one or more microprocessors in conjunction with a DSP core, or any other such configuration).

The embodiments disclosed herein may be embodied in hardware and in instructions that are stored in hardware, and may reside, for example, in RAM, flash memory, ROM, electrically programmable ROM (EPROM), electrically erasable programmable ROM (EEPROM), registers, a hard disk, a removable disk, a CD-ROM, or any other form of computer-readable medium known in the art. An exemplary storage medium is coupled to the processor such that the processor can read information from, and write information to, the storage medium. In the alternative, the storage medium may be integral to the processor. The processor and the storage medium may reside in an ASIC. The ASIC may reside in a remote station. In the alternative, the processor and the storage medium may reside as discrete components in a remote station, base station, or server.

It is also noted that the operational steps described in any of the exemplary embodiments herein are described to provide examples and discussion. The operations described may be performed in numerous different sequences other than the illustrated sequences. Furthermore, operations described in a single operational step may actually be performed in a number of different steps. Additionally, one or more operational steps discussed in the exemplary embodiments may be combined. Those of skill in the art will also understand that information and signals may be represented using any of a variety of technologies and techniques. For example, data, instructions, commands, information, signals, bits, symbols, and chips, that may be references throughout the above description, may be represented by voltages, currents, electromagnetic waves, magnetic fields, or particles, optical fields or particles, or any combination thereof.

Unless otherwise expressly stated, it is in no way intended that any method set forth herein be construed as requiring that its steps be performed in a specific order. Accordingly, where a method claim does not actually recite an order to be followed by its steps, or it is not otherwise specifically stated in the claims or descriptions that the steps are to be limited to a specific order, it is in no way intended that any particular order be inferred.

Those skilled in the art will recognize improvements and modifications to the preferred embodiments of the present disclosure. All such improvements and modifications are considered within the scope of the concepts disclosed herein and the claims that follow.

