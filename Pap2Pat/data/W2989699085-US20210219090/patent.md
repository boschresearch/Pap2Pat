# DESCRIPTION

## FIELD OF THE INVENTION

The present invention relates to the field of sound calibration. More particularly, the invention relates to a method and system for estimating the Room Transfer Function (RTF) in order to enable automatic sound calibration while hearing, without the need of user intervention.

## BACKGROUND OF THE INVENTION

Sound calibration is employed in many commercial audio systems for improving sound quality and make adaptation of the audio system to the existing acoustic environment (which may vary, due to echoes, reflections from walls etc.). This process includes the estimation of the Room Transfer Function (RTF) between each loudspeaker and a microphone located at the listeners' position.

Current methods for RTF estimation employ calibration signals, such as noise or tones, in a dedicated process applied separately to each loudspeaker. However, such an estimation disrupts normal playback, is time consuming, and requires user intervention.

Sound calibration for audio systems is a process in which the parameters of each channel or each loudspeaker are adjusted to improve sound quality (e.g., by controlling the delay and gain of each loudspeaker). The parameters typically include frequency equalization, loudness level, and time-delays, and are adjusted based on the acoustic environment in the room and the location of the sound system. This process usually requires the use of a microphone for estimating the Room Transfer Function (RTF). Current methods for RTF estimation employ excitation, or calibration signals, to estimate the RTF in a dedicated process applied to each loudspeaker separately, and a microphone assumed to be located in the vicinity of the listeners. Excitation signals include maximum-length sequences, inverse-repeated sequences, sweep sines (linear and logarithmic), impulses, periodic impulse excitation, time-stretched pulses, random noise, pseudo-random noise, and periodic random excitation, while the variety of applications include sound calibration, video conferencing/multimedia communication systems, virtual and augmented reality, auralization, and spatialization of sounds. All the above methods employ a calibration signal, which makes the task of RTF estimation time-consuming, necessitates user intervention, and interrupts the normal use of the audio system.

There are also RTF estimation methods that employ non-dedicated source signals, which allows a more natural measurement of a system during playback. In this case, the source signals should cover all frequencies of interest in the long term, and typically require longer averaging times to achieve good estimates compared to typical excitation signals. Applications typically include echo cancellation and source localization, wherein speech signals are used for estimating the RTFs. However, these methods are suited for a system with a single loudspeaker. For multi-channel audio systems, these methods could still be applied, but may require playback using one loudspeaker at a time, which again may interrupt the normal playback of the system.

An RTF estimation process for multi-channel audio systems that more naturally integrates with the normal operation of the system and that is perceptually-transparent to listeners could be of great interest. Such a process could also be made automatic, without requiring user-intervention, and could therefore be applied when necessary to compensate for time-varying acoustic conditions.

The signal measured by the microphone, y(f), is given by:

Y(f)=HL(f) sL(f)+HR(f) sR(f),   (Eq. 1)

where f denotes frequency, sL (f) and sR (f) are the input signals of the left and right channels, respectively, and HL (f) and HR (f) are the RTFs of the left and right loudspeakers, respectively. For mono playback, sL(f)=sR(f)=s(f).

Practically, a noise component that can model acoustic noise, modelling noise, and transducer noise may be added to y(f) , however, noise is not added for simplicity.

One of the existing methods for RTF estimation is a dual-channel FFT analysis [20], which works with various calibration signals, including real-world audio signals. As an example, the estimation of the left RTF, HL(f), is presented. For this purpose, playback only from the left loudspeaker is employed, while the right input signal, sR (f), is assumed to be zero. Therefore Eq. (1) can be written as:

Y(f)=HL(f) sL(f).   (Eq. 2)

The estimated RTF is calculated using the auto spectra (which shows the distribution of a signal's energy across frequency) of the input signal, and the cross spectrum (an indication of how common activity between two processes is distributed across frequency) between the input signal and the output signal. The auto spectra of sL(f) is defined as:

SSS(f)=E[sL*(f)sL(f)]  (Eq. 3)

where E[*] is the statistical expectation and (·)*denotes the complex conjugate. In practice, the spectra are computed using estimations of the statistical expectation, calculated by averaging the spectra over multiple time blocks. For simplicity of notation, the spectra are presented using statistical expectations. Furthermore, the block time duration is assumed to be sufficiently long compared to the RTF, HL(f), in time, as required by the multiplicative transfer function assumption [21].

Also, a time window function may be applied to each block in practice for a modified periodogram (an estimate of the spectral density of a signal) with desired frequency characteristics [22] (details regarding the calculation of the spectra can be found in [20]).

The cross spectrum is given by:

SSy(f)=E[sL*(f)y(f)],   (Eq. 4)

and is approximated in practice using time averaging, as in the case of the auto spectra. Given the spectra, there are several ways to estimate the RTF, HL(f), with the specific implementation chosen according to where noise is added in the processing chain.

One estimate of the RTF, ĤL(f), is given by:

\(\begin{matrix}
{{{{\hat{H}}_{L}(f)} = \frac{s_{s_{L}y}(f)}{s_{s_{L}s_{L}}(f)}},} & \left( {{Eq}.\mspace{14mu} 5} \right)
\end{matrix}\)

which is proposed when noise is added to the output signal [23].

The description above presented RTF estimation when a single loudspeaker is employed. When both loudspeakers are employed, the output y(f) includes contributions from both loudspeakers. Including the contribution of a non-zero sR(f) in y(f), as in Eq. (1), FIL(f) from Eq. (5) may be rewritten as:

\(\begin{matrix}
{{{{\hat{H}}_{L}(f)} = {{H_{L}(f)} + {{H_{R}(f)}\frac{s_{s_{L}s_{R}}(f)}{s_{s_{L}s_{L}}(f)}}}},} & \left( {{Eq}.\mspace{14mu} 6} \right)
\end{matrix}\)

where Sss(f) is the cross spectrum between the left and right input signals. Hence, when signals of both channels are simultaneously employed, there is an error in the estimation if the left and right signals are correlated.

It is therefore an object of the present invention to provide a method and system for estimating the Room Transfer Function (RTF) in order to enable automatic sound calibration while hearing, without the need of user intervention.

It is another object of the present invention to provide a method and system for estimating the Room Transfer Function (RTF), the operation of which is perceptually-transparent to the listener, so as to ensure minimum hearing disturbance.

Other objects and advantages of the invention will become apparent as the description proceeds.

## SUMMARY OF THE INVENTION

A method for performing perceptually-transparent RTF estimation for a two-channel system with low estimation errors, comprising the steps of:


- - a) providing two loudspeakers for the left and right channels
    positioned in a room and a single microphone, positioned in the
    vicinity of a listener in the room;
  - b) performing spectral splitting using a filter bank and a
    complementary filter bank, to obtain separation in frequency between
    the two channels, by:
    - b.1) selecting I center frequencies, f_(i), i=0, . . . I−1, having
      values restricted to the range between zero and half of the
      sampling frequency, f_(s)/2;
    - b.2) for each center frequency, defining a corresponding frequency
      band, O_(i).
    - b.3) for each center frequency and frequency band, constructing a
      corresponding filter, B_(i)(f);
    - b.4) constructing a filter for the left loudspeaker as a summation
      of filters for even center frequencies;
    - b.5) constructing a filter for the right loudspeaker as a
      summation of filters for odd center frequencies;
  - c) generating calibration signals being uncorrelated across the two
    channels using the original audio signals and the constructed
    filters;
  - d) playing back the calibration signals by the loudspeakers, instead
    of playback of the original audio signals;
  - e) recording the playback of the calibration signals by the
    microphone; and
  - f) simultaneously estimating the two-channel RTF using the recorded
    played back calibration signals.

The two filter banks may be employed at different operating times.

Preferably, the center frequencies of a complementary set are shifted in frequency (e.g., ¼ octave for ½ octave band), compared to the center frequencies of a set.

Estimated RTFs may be constructed by merging the estimates from each set. Merging RTF estimates of multiple sets may be performed by fixed mapping or by using the pointwise minimum of ∥GL*(f)GR(f)∥.

RTF estimates may be performed peroidically every predetermined time, for automatically compensating changes in the acoustic environment.

A method for performing transparent RTF estimation for a multiple-channel system with low estimation errors, comprising the steps of:


- - a) providing a plurality of loudspeakers for the L channels
    positioned in a room and a single microphone, positioned in the
    vicinity of a listener in the room;
  - b) performing spectral splitting using a filter bank and
    complementary filter banks, to obtain separation in frequency
    between the multiple channels, by:
    - b.1) selecting/center frequencies, f_(i), i=0, . . . I=1, having
      values restricted to the range between zero and half of the
      sampling frequency, f_(s)/2;
    - b.2) for each center frequency, defining a corresponding frequency
      band, O_(i).
    - b.3) for each center frequency and frequency band, constructing a
      corresponding filter, B_(i)(f);
    - b.4) constructing a filter for eack loudspeaker as a summation of
      filters for predetermined center frequencies;
  - c) generating calibration signals being uncorrelated across the
    multiple channels using the original audio signals and the
    constructed filters;
  - d) playing back the calibration signals by the loudspeakers, instead
    of playback of the original audio signals;
  - e) recording the playback of the calibration signals by the
    microphone; and
  - f) simultaneously estimating the multiple-channel RTF using the
    recorded played back calibration signals.

A system for performing transparent RTF estimation for a multiple-channel system with low estimation errors, comprising:


- - a) a plurality of loudspeakers for the L channels positioned in a
    room and a single microphone, positioned in the vicinity of a
    listener in the room;
  - b) a filter bank and complementary filter banks, for performing
    spectral splitting;
  - c) a processor for separating in frequency between the multiple
    channels, which is adapted to:
    - c.1) select/center frequencies, f₁, i=0, . . . I−1, having values
      restricted to the range between zero and half of the sampling
      frequency, f_(s/)2;
    - c.2) for each center frequency, define a corresponding frequency
      band, O_(i).
    - c.3) for each center frequency and frequency band, construct a
      corresponding filter, B_(i)(f);
    - c.4) construct a filter for eack loudspeaker as a summation of
      filters for predetermined center frequencies;
    - c.5) generate calibration signals being uncorrelated across the
      multiple channels using the original audio signals and the
      constructed filters;
  - d) a player for playing back the calibration signals by the
    loudspeakers, instead of playback of the original audio signals;
  - e) a recorder for recording the playback of the calibration signals
    by the microphone; and
  - f) at least one processor for simultaneously estimating the
    multiple-channel RTF using the recorded played back calibration
    signals.

## DETAILED DESCRIPTION OF PREFERRED EMBODIMENTS

The present invention proposes a perceptually-transparent RTF estimation method for a two-channel system (that may be extended to a multiple-channel system) with low estimation errors. The proposed method employs calibration signals generated using the original audio signals and complementary filters. These calibration signals are uncorrelated across the two channels, which facilitates the estimation of both channels (or multiple channels in the case of a multiple-channel system) using a single microphone. In this embodiment, the microphone is positioned in the vicinity of a listener.

The proposed method is based on spectral splitting with complementary filter banks and is applied to produce signals for two channels, as described for example in [17, 18]. The proposed method employs complementary filter banks to produce estimation signals (referred to as calibration signals) for the two loudspeakers. These calibration signals are shown to be perceptually similar to the original, unprocessed audio signals, which could be explained by the phenomenon of spectral fusion [19]. By using complementary filter banks, the processed calibration signals become uncorrelated across the two channels and can be used for simultaneous estimation of the two-channel RTF.

Looking again at Eq. (1), if sL(f) and sR(f) are uncorrelated, Sss(f) from Eq. (6) is zero, and the RTF could be estimated using the single output signal, y(f). This is the main principle behind the proposed method presented in the following description, where decorrelation is achieved by separation in frequency, which is perceptually transparent to listeners. The basic processing operation is to transmit part of the frequencies to one loudspeaker and the remaining frequencies to another loudspeaker. The ear of the listener integrates these different components. The advantage is that calibration is performed during normal listening of the desired audio content. Another advantage of the proposed method is the fact that calibration may be peroidically done every predetermined time, such that any change in the acoustic environment will be automatically compensated.

Calibration Signals

According to the present invention, given a two-channel input signal, two uncorrelated signals are produced by employing a filter bank and a complementary filter bank. In this embodiment, the filter banks are presented in a generic manner, even though various sets of center frequencies, filter bandwidths, number of bands, and filter implementations can be used.

To construct the filter banks, I center frequencies, fi, i=0, . . . I−1, are initially selected, with their values restricted to the range between zero and half of the sampling frequency, fs/2. For each center frequency, a corresponding frequency band, Oi, is defined. For each center frequency and frequency band, a corresponding filter, Bi(f), is constructed.

Filters for the left and right loudspeakers are then constructed. The filter for the left loudspeaker is constructed as a summation of filters for even center frequency indices:

GL(f)=Σi=0,2,4, . . . , I−2 Bi(f).   (Eq. 7)

Similarly, a filter for the right loudspeaker is comprised of a summation of filters for odd indices:

GR(f)=Σi=1,3,5, . . . ,I−1 Bi(f),   (Eq. 8)

while assuming (for simplicity) that I is even.

Next, two signals are generated as loudspeaker input signals given the two-channel input signal and GL(f) and GR(f):

l(f)=GL(f)sL(f), and   (Eq. 9)

r(f)=GR(f)sR(f),   (Eq. 10)

for left and right loudspeakers, respectively. The cross-spectrum between the two signals is given by:

E[l*(f)r(f)]=GL*(f)GR(f)E[sL*(f)sR(f)].   (Eq. 11)

Since sL (f) and sR (f) cannot be assumed to be uncorrelated, as they could be identical for a mono signal, or highly correlated for a stereo signal, achieving decorrelation between these signals requires that:

GL*(f)GR(f)=0, ∀f ∈[,fs/2].   (Eq. 12)

Substituting Eqs. (7) and (8) in Eq. (12), the condition in Eq. (12) can be reformulated as:

Bi*(f)Bj(f)=0, ∀i evn and j odd.   (Eq. 13)

This is a sufficient condition to ensure zero correlation if the filters are equal to zero outside their bandwidth, or to ensure low correlation if they have a small gain outside their bandwidth. The proposed de-correlated calibration signals form the basis for RTF estimation.

RTF Estimation with Proposed Calibration Signals and Ideal Filters

RTF estimation is described below for the case of ideal filters, with the following assumptions:

Filters Bi (f) used for generating the calibration signals are ideal, with:

\(\begin{matrix}
{{B_{i}(f)} = \left\{ {\begin{matrix}
{1,} & {{\text{∀}f} \in {O_{i}(f)}} \\
{0,} & {{\text{∀}f} \notin {O_{i}(f)}}
\end{matrix}.} \right.} & \left( {{Eq}.\mspace{14mu} 14} \right)
\end{matrix}\)


- - The frequency bands used for defining these filters do not overlap,
    i.e.:

Oi∩0j=0, ∀ i≠j.   (Eq. 15)


- - The union of all frequency bands covers the entire frequency range,
    i.e.:

From Eqs. (14) and (15) (i.e., ideal filter with non-overlapping bands), it is clear that Eq. (13) is satisfied, and the correlation of the calibration signals as in Eq. (11) becomes zero. Then, RTF estimation is developed by defining two sets of calibration signals:

l1(f)=GL(f)sL(f), r1(f)=GR(f)sR(f),   (Eq. 17)


- - and

l2(f)=GR(f)sL(f), r2(f)=GL(f)sR(f).   (Eq. 18)

Set 1 is defined as in Eqs. (9) and (10). Set 2 (Eq. (18)) is defined as in Eqs. (9) and (10) but with interchanged filters between left and right channels.

Due to the ideal filters which satisfy Eq. (12), the correlation of the calibration signals as in Eq. (11) is zero, i.e. E[l1*(f)r1(f)]=E[l2*(f)r2(f)]=0.

The calibration signals are played back by the loudspeakers, instead of playback of the original audio signals, as in Eq. (1), and are recorded by the microphone. The new system model in this case becomes:

y1(f)=HL(f)l1(f)+HR(f)r1(f),   (Eq. 19)

y2(f)=HL(f)l2(f)+HR(f)r2(f).   (Eq. 20)

FIG. 1 illustrates the system block diagram, in which the processing of the left and right input signals before playback is controlled by a single switch with three different states:

(1) normal playback with no calibration, according to Eq. (1);

(2) calibration signals set 1 with with y(f)=y1(f), according to Eq. (19);

(3) calibration signals set 2 with y(f)=y2(f), according to Eq. (20).

RTFs are estimated using the measured signals in Eqs. (19) and (20). Initially, RTFs between these measured signals and the calibration signals from Eqs. (17) and (18) are estimated. For y1(f), for example, HL1(f) is defined similarly to Eq. (5), using:

\(\begin{matrix}
{{H_{L}^{1}(f)} = {\frac{s_{l_{1}y_{1}}}{s_{l_{1}l_{1}}} = \frac{E\left\lbrack {{l_{1}^{*}(f)}{y_{1}(f)}} \right\rbrack}{E\left\lbrack {{l_{1}^{*}(f)}{l_{1}(f)}} \right\rbrack}}} & \left( {{Eq}.\mspace{14mu} 21} \right) \\
{{= {\frac{{{H_{L}(f)}{E\left\lbrack {{l_{1}(f)}}^{2} \right\rbrack}} + {{H_{R}(f)}{E\left\lbrack {{l_{1}^{*}(f)}{r_{1}(f)}} \right\rbrack}}}{E\left\lbrack {{l_{1}(f)}}^{2} \right\rbrack} = {H_{L}(f)}}},{{\text{∀}f} \in O_{i}},{{for}\mspace{14mu}{even}\mspace{14mu} i},} & \left( {{Eq}.\mspace{14mu} 22} \right)
\end{matrix}\)

where the last line was derived using Eq. (11) and the conclusion derived above that the correlation is zero for the case of ideal filters.

In order to avoid a zero denominator due to the construction of r1(f) in Eq. (17), only frequency bands of even indices are considered. Repeating the same estimation process for y2(f) and l2(f), y2(f) and r2(f), and y1(f) and r1(f), will lead to estimation of the two RTFs for the entire frequency range, due to Eq. (16):

\(\begin{matrix}
{{{\hat{H}}_{L}(f)} = \left\{ {\begin{matrix}
{{H_{L}^{1}(f)},} & {{\text{∀}f} \in \left\{ {O_{i}(f)} \right\}_{{i = 0},2,4,\ldots,{I - 2}}} \\
{{H_{L}^{2}(f)},} & {{\text{∀}f} \in \left\{ {O_{i}(f)} \right\}_{{i = 1},3,5,\ldots,{I - 1}}}
\end{matrix},{and}} \right.} & \left( {{Eq}.\mspace{14mu} 23} \right) \\
{{{\hat{H}}_{R}(f)} = \left\{ {\begin{matrix}
{{H_{R}^{2}(f)},} & {{\text{∀}f} \in \left\{ {O_{i}(f)} \right\}_{{i = 0},2,4,\ldots,{I - 2}}} \\
{{H_{R}^{1}(f)},} & {{\text{∀}f} \in \left\{ {O_{i}(f)} \right\}_{{i = 1},3,5,\ldots,{I - 1}}}
\end{matrix}.} \right.} & \left( {{Eq}.\mspace{14mu} 24} \right)
\end{matrix}\)

While the estimation process with ideal filters presented above lead to an estimation process with zero error, filters in practice are never ideal. Therefore, a solution with practical filters is presented hereinbelow.

RTF Estimation with the Proposed Calibration Signals and Practical (Non-Ideal) Filters

RTF estimation is described below for the case of practical (non-ideal) filters, with the following assumptions:

Filters Bi (f) used for generating the calibration signals include a pass band, Oipass (f), and a stop band, Oistop(f), and are defined in a generic manner as:

Bi(f)≈1, ∀f ∈Oipass(f),

|Bi(f)∥<ε, ∀f ∈Oistop(f),   (Eq. 25)

where ε is a predefined threshold. Oipass(f) and Oistop(f) do not cover the entire frequency range, as there are frequencies in the transition between these two frequency bands.


- - The pass bands used for defining these filters do not overlap, i.e.:

Oipass ∩ Ojpass=0, ∀i≠j.   (Eq. 26)


- - The union of all pass bands covers the entire frequency range, i.e.:

∪i=0I−1Oipass=[0, fs/2].   (Eq. 27)

Under these assumptions, the derivation of the estimation method for ideal filters is repeated with the following differences. Bi*(f), Bj(f)=0 from Eq. (13) is now replaced by |Bi*(f)Bj(f)| ε at i, j, ∈ S , where S is a subset of bands which are sufficiently distant from one another such that any one pass band overlaps only with stop bands from the other bands. Therefore, Eq. (12) is replaced by |GL*(f)GR(f)|<ε, and Eq. (11) is replaced by E[l*(f)r(f)]<εE[sL(f)sR(f)] for frequency bands in S.

This leads to a small correlation between signals l(f) and r(f). RTF estimation is repeated for more band subsets, until the entire frequency range is covered. This process is described below for a specific filter implementation and two sets of calibration signals, and can be extended in a similar manner to various filter implementations and multiple sets of calibration signals.

Implementation using ½-octave FIR filters

A design example of filter banks for the proposed estimation method is presented below, based on ½-octave filters with Discrete-Fourier-transform (DFT) based implementation. Here, two sets of filter banks are employed, following the general framework presented for practical filters in the previous section. I=16 center frequencies are selected for the first set of filter banks, and I=15 center frequencies are selected for the second set of filter banks, with the sampling frequency, fs, set to 44100 Hz. The center frequencies are presented in Table 1 for both sets.

The center frequencies of set 2 are shifted by a ¼ octave compared to those in set 1. For both sets, and for each center frequency, a corresponding frequency band, 0i, is defined as follows:

Oi:=[2−1/4fi, 21/4fi), i=0,1, . . . , I−1,   (Eq. 28)

where 00 is modified to start at 0 Hz and is modified to end at fs/2. For both sets, and for each frequency band, a corresponding filter, bi[n], i=0, . . . I−1, where n is the discrete time index, is constructed using a DFT-based implementation as [24]:

bi[n]=Σq:=fq/NEOej2πqn/N, n=0, . . . , N−1,   (Eq. 29)

where N=7055 is the DFT length used for constructing these filters, which, when combined with fs, yield a time duration of 160-ms, and q=0, . . . , N−1 is the DFT frequency index. In particular, DFT frequency indices that correspond to negative frequencies are also included in the summation in Eq. (29), so that the filters are real in the time domain. The filters in the frequency domain, Bi(f), are calculated by applying a DFT on bi[n]. Then, GL(f) and GR(f) are constructed as in Eqs. (7) and (8), respectively, using filters Bi(f).

FIG. 2 is an illustrative example of filter B4(f) from set 1 for ½-octave filters for a DFT-based implementation of length SN, to obtain improved frequency resolution. A magnitude close to unity is observed at the corresponding octave band, while a relatively high attenuation is observed away from the pass band. The remaining filters, Bi(f), show similar behavior.

FIG. 3 is an illustrative example of filters GL(f) and GR (f) from set 1 for ½-octave filters for a DFT-based implementation of length SN. Due to the construction using filters from Eq. (29), GL(f) and GR(f) sum to unity at the original DFT frequencies, and the inverse DFT of the summation of these functions gives an impulse function, which was a consideration for this specific implementation. Filters from set 2 are not presented as they are similar in behavior.

FIG. 4 illustrates |GL*(f)GR(f)| for ½-octave filters with DFT-based implementation for both sets of filters with center frequencies given in Table 1. |GL*(f)GR(f)| is proportional to the correlation (see Eq. (11)). High values of |GL*(f)GR(f)∥ are obtained for both sets at frequencies in the transition between the frequency bands. At these frequencies, correlation is expected to be higher, and this may degrade RTF estimation in Eq. (21). However, at frequencies where |GL*(f)GR(f)| is high for set 1, it is low for set 2 and vice versa.

FIG. 5 presents the pointwise minimum of |GL*(f)GR(f)| between both sets, which can be considered as the effective |Gl*(f)GR(f)| for both sets. The pointwise minimum of |GL*(f)GR(f) | for both sets is lower than approximately −20 dB at all frequencies, which can facilitate improved estimation using two sets compared to estimation using a single set. This is the reason that the filters are divided into two sets in the manner described in Table 1 (i.e., using a ¼-octave shift between the two sets).

At the next stage, the mapping of frequencies that have minimum |GL*(f)GR(f)| for each set can be used for constructing estimated RTFs by merging the estimates from each set. At frequencies where |GL*(f)GR(f)| of set 1 is minimal, RTFs can be estimated (as described above with respect to RTF estimation with proposed calibration signals and ideal filters) for signals corresponding to set 1. Similarly, at frequencies where |GL*(f)GR(f)| of set 2 is minimal RTFs can be estimated using signals corresponding to set 2. Other methods for merging RTF estimates of multiple sets, such as a fixed mapping, can be implemented using the center frequencies of each set.

Analysis of RTF estimation using the proposed method is described below for an experimental system comprising a stereo loudspeaker system and a single microphone positioned in a room. The analysis includes an investigation of the frequency-dependent error between estimated and measured RTFs and the total error.

Setup

A set of RTFs was measured using a system comprised of two KRK ROKIT 6″ loudspeakers and a Bruel & Kjaer ½-inch diffuse-field microphone, which were connected via an ESI U24XL soundcard to a laptop. The room where the experiment took place is a meeting room at Ben-Gurion University of the Negev, with dimensions of (7.2, 6.4, 3.1) m, an approximate volume of 143 m3, and a reverberation time of about 0.5 s. The reverberation time was calculated from measured Room Impulse Responses (RIRs) using the Schroeder backward integration [25]. The left and right loudspeakers were positioned at (0.3, 1.6, 0.7) m and (0.3, 0.8, 0.7) m, with a distance of 0.8 m between the loudspeakers. The microphone was positioned at (2.8, 1.2, 1.05) m, which is 2.5 m away from the middle point connecting the loudspeakers. The system was placed slightly towards the room corner due to a large meeting table positioned in the room.

Input signals

An analysis is provided for various stereo input signals that include white noise, speech, and music, and for the ½-octave filters presented in the previous section. Three different 20-second duration stereo audio signals were used as input signals:


- - 1. white (uniform) noise,
  - 2. jazz music (taken from \[26\]),
  - 3. pop music (taken from \[27\]), and
  - 4. speech (taken from \[28\]).

Methods

The RTFs of the two channels were measured as follows. Each loudspeaker (separately) played back a 20-second white-noise signal. The signal recorded by the microphone along with the input signal of the loudspeakers were recorded by the computer. RTFs from the two loudspeakers to the microphone position were then computed using these signals and MATLAB's tfestimate function, with a 1-second duration window and an overlap factor of 2. For each transfer function, a corresponding RIR was calculated using an inverse DFT, and these are denoted hL, [n] and hR[n] for the left and right channels, respectively. The system buffer, or time delay, due to all hardware components including the sound card was compensated for.

To investigate estimation using the proposed method, signals y1(f) and y2 (f) as in Eqs. (19) and (20), respectively, were generated in a computer simulation using the measured RTFs and calibration signals generated using the filters presented in the previous section. Noise was generated using a zero-mean Gaussian distribution and added to the output signals to model measurement noise. The variance of the noise was set equal over frequency to produce a 40 dB average Signal-to-Noise Ratio (SNR). HL1(f), HL2(f), HR1(f), and HR2(f) were calculated for both sets as in Eq. (21) using MATLAB's tfestimate function with a 1-second duration window and an overlap factor of 2. Estimated left and right RTFs, ĤL (f) and ĤR(f), respectively, were then estimated twice. First, ĤL(f) and ĤR(f) were estimated for set 1 only, as in Eqs. (23) and (24). Then, ĤL(f) and ĤR(f) were estimated for both sets, using the implementation using ½-octave FIR filters that employs the pointwise minimum of |GL*(f)GR(f)∥ of both sets (see FIG. 5).

A frequency dependent error has been defined as |HL(f)−ĤL(f)| and |HR(f)−ĤR(f)|, for the left and right channels, respectively. A normalized error has been calculated as |HL(f)−ĤL(f)|/|HL(f)| for the two channels, respectively, and was averaged in ⅓ octaves so as to avoid ill-conditioning at frequencies at which the RTFs magnitudes are low. The total error has been calculated as ∥HL(f)−ĤL(f)∥/∥HL(f)−ĤR(f)∥/∥HR(F)∥ for the left and right loudspeakers, respectively, where ∥·∥ denotes the 2-norm.

Results

FIG. 6 shows measured RIR hL, [n] for left channel. FIG. 7 shows measured RTF for left channel (FL(f)).

FIG. 8 illustrates the frequency dependent error |HL(f)−ĤL(f)| for the left channel, estimated using set 1 only, which represents the difference between the measured RTF and the estimated RTF. The difference signal shows large errors at frequencies near the transition between the pass and stop bands of the filters used to construct GL (f) and GR(f). Similar results are obtained for the right channel RTF and for calibration signals generated for the remaining input signals.

FIG. 9 shows the difference between the measured RTF and the estimated RTF using both sets. The difference signal in this case is 20 dB lower than the measured RTF at most frequencies, including the transitions between the frequency bands.

FIG. 10 shows the normalized error averaged in ⅓ octaves for all the input signals used in the listening test. Here, the maximum error for these examples is less than −15 dB, but is typically significantly lower.

The total estimation error for the left channel is presented in Table 2 for all input signals.

It can be seen that the frequency dependent errors and total errors obtained using the method proposed by the present invention are reasonably low.

Listening Test

Several listening test have been performed for evaluating the perceptual-transparency of the calibration signals when played back using the system loudspeakers with speech and music input signals. The listening tests were conducted in the same room described earlier, but with the left and right loudspeakers positioned at (3.2, 6.1, 0.7) m and (4, 6.1, 0.7) m (keeping the same distance of 0.8 m between the loudspeakers), and the listeners were positioned at (3.6, 3.93, 0.7) m, which is 2.17 m on the axis of the loudspeaker middle point.

The listening tests were designed for evaluating the perceptual-transparency of the proposed method, and for comparing performance with that of the baseline solution of signal playback from a single loudspeaker. For this purpose, three systems are considered:

Reference


- - playback of the original stereo audio signals,

Test


- - playback of the signals after applying the developed method, i.e.
    playback for the calibration signals, and

Anchor


- - playback from the left loudspeaker only.

An ABX comparison-based test was conducted [29] that employs three audio signals with a 5-sec duration, played back with pauses of 1.5-sec between the signals, as presented in Table 3.

In Table 3, signal X is either Reference or Test with equal probability for the sequences in lines 1-2, or Reference or Anchor for the sequences in lines 3-4. Lines 1-2 serve to investigate if the Test system is perceptually-transparent compared to the Reference system, and, similarly, lines 3-4 serve to investigate if the Anchor system is perceptually-transparent compared to the Reference system. The signal types employed were the speech and music input signals defined in the analysis (described above) of RTF estimation (using the proposed method) for the experimental system described above. Different segments of the same audio material were used for producing signals A, B, and X, and in each test an ABX sequence has been played only once.

FIGS. 11, 12, and 13 show the average success rate of Test and Anchor systems for jazz music, pop music, and speech, respectively, following the listening test. FIG. 14 shows the overall success rate, which is the average for all signal types, following the listening test. A success rate of 50% is interpreted as perceptually-transparent since it corresponds to the average success rate of an equiprobable guess. A success rate of 100% is interpreted as completely non-transparent, and a 75% rate is interpreted as partially-transparent. The results show that the method developed is perceptually-transparent for the jazz music audio recording, and is partially perceptually-transparent for the pop music and speech. On the other hand, the anchor system, or baseline solution is very close to being completely non-perceptually-transparent for all input signals.

The proposed method may be adapted to perform transparent RTF estimation for a multiple-channel system with L loudspeakers for L corresponding audio channels (rather that two). In this case, spectral splitting is performed by using a filter bank and complementary filter banks, to obtain separation in frequency between some or all of these multiple channels (it is possible to use less filter banks than channels. For example, if it is desired to separate only one channel from the rest of the L−1 channels, and in this case, two filter banks will be sufficient). I center frequencies, fi, i=0, . . . I−1, with values restricted to the range between zero and half of the sampling frequency, fs/2 are selected, while for each center frequency, a corresponding frequency band, Oi is defined. A corresponding filter, B1 (f) is constructed for each center frequency and frequency band and a filter is constructed for eack loudspeaker as a summation of filters for predetermined center frequencies. Calibration signals which are uncorrelated across the multiple channels are then generated using the original audio signals and the constructed filters. These calibration signals are played-back by the plurality of loudspeakers and recorded by the microphone. The recorded played back calibration signals are used to simultaneously estimate the multiple-channel RTF.

The above examples and description have of course been provided only for the purpose of illustrations, and are not intended to limit the invention in any way. As will be appreciated by the skilled person, the invention can be carried out in a great variety of ways, employing more than one technique from those described above, including the internet, a cellular network or any other wireless data network, all without exceeding the scope of the invention.

