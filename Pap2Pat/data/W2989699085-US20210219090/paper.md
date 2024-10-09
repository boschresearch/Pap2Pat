# II. SYSTEM MODEL

The system model comprises two loudspeakers (left and right channels) positioned in a room and a single microphone, assumed to be positioned in the vicinity of a listener. The signal measured by the microphone, y(f ), is given by:

where f denotes frequency, s L (f ) and s R (f ) are the input signals of the left and right channels, respectively, and H L (f ) and H R (f ) are the RTFs of the left and right loudspeakers, respectively. For mono playback, s L (f ) = s R (f ) = s(f ). Finally, note that in practice a noise component that can model acoustic, modelling, and transducer noise may be added to y(f ). However, this noise component is not added to the equations throughout the paper for simplicity, and since it is not required for the development of the proposed method.

## III. CURRENT METHODS FOR RTF ESTIMATION

A current method for RTF estimation, dual-channel FFT analysis [29], is presented as background. This method has been chosen since it works with various calibration signals, including real-world audio signals, which is the area of interest in this paper. Consider, for simplicity, a single-channel system, which will be extended below to the two-channel case. Following the notation of Eq. ( 1), the single-channel system equation is given by:

(

As detailed at the end of this section, the estimated RTF is calculated using the auto spectra of the input signal, and the cross spectrum between the input signal and the output signal. The auto spectra of s(f ) is defined as:

where E[•] is the statistical expectation and (•) * denotes the complex conjugate. In practice, the statistical expectation is approximated by averaging spectra over multiple time blocks, as described in Section V. The cross spectrum is given by:

and is approximated in practice using time averaging, as in the case of the auto spectra. Given the spectra, there are several ways to estimate the RTF, H(f ), with the specific implementation chosen according to where noise is added in the processing chain. One estimate of the RTF, Ĥ(f ), is given by:

and is derived based on a noise-reduction criterion and under the assumption that noise is added to the output signal, i.e., the microphone [30].

This section presented RTF estimation when a single loudspeaker is employed. When both loudspeakers are employed, the output y(f ) will include contributions from both loudspeakers. For demonstrating this, we employ the notation of the left and right RTFs and input signals as in Eq. (1); in particular, H L (f ) is to be estimated, but when both s L (f ) and s R (f ) are non-zero. Including the contribution of a non-zero s R (f ) in y(f ), as in Eq. ( 1), the estimated RTF from Eq. ( 5) is now denoted as ĤL (f ), and is given as:

where S s L s R (f ) is the cross spectrum between the left and right input signals. This demonstrates that when signals of both channels are simultaneously employed, there is an error in the estimation if the left and right signals are correlated. If s L (f ) and s R (f ) are uncorrelated, S s L s R (f ) from the last equation is zero, and the RTF could be estimated using the single output signal, y(f ). This is the main principle behind the proposed method presented in the following sections, where decorrelation is achieved by separation in frequency.

### IV. PROPOSED METHOD FOR RTF ESTIMATION

The proposed estimation methods includes a pre-processing method for producing calibration signals, and a post-processing method that estimates RTFs, as described in this section.

## A. Pre-Processing -Calibration Signals

A method for producing two uncorrelated signals given a two-channel input signal is proposed; the method employs a filter bank and a complementary filter bank. At this stage, the filter banks are presented in a generic manner. Various sets of center frequencies, filter bandwidths, number of bands, and filter implementations can be considered, with an example implementation provided in Section V.

To construct the filter banks, I center frequencies, f i , i = 0, . . .I -1, are initially selected, with their values restricted to the range between zero and half of the sampling frequency, f s /2. For each center frequency, a corresponding frequency band, O i , is defined. For each center frequency and frequency band, a corresponding filter, B i (f ), is constructed.

Filters for the left and right loudspeakers are constructed next. The filter for the left loudspeaker is constructed as a summation of filters for even center frequency indices:

Similarly, a filter for the right loudspeaker is comprised of a summation of filters for odd indices:

where it has been assumed, for simplicity, that I is even. Next, two signals are generated as loudspeaker input signals given the two-channel input signal and G L (f ) and G R (f ):

for left and right loudspeakers, respectively. The cross-spectrum between the two signals is given by:

Now, since s L (f ) and s R (f ) cannot be assumed to be uncorrelated, as they could be identical for a mono signal, or highly correlated for a stereo signal, achieving decorrelation between these signals requires:

Substituting Eqs. ( 7) and ( 8) in Eq. ( 12), the condition in Eq. ( 12) can be reformulated as:

This is a sufficient condition to ensure zero correlation if the filters are equal to zero outside their bandwidth, or low correlation if they have a small gain outside their bandwidth. The proposed de-correlated calibration signals form the basis for RTF estimation.

## B. Post-Processing -RTF Estimation With Proposed Calibration Signals

As an initial step, RTF estimation is described in this section for the case of ideal filters, with the following assumptions: i) Filters B i (f ) used for generating the calibration signals are ideal, with:

ii) The frequency bands used for defining these filters do not overlap, i.e.:

iii) The union of all frequency bands covers the entire frequency range, i.e.:

From Eqs. ( 14) and ( 15), i.e. ideal filter with non-overlapping bands, it is clear that Eq. ( 13) is satisfied, and the correlation of the calibration signals as in Eq. ( 11) becomes zero. Next, RTF estimation is developed by defining two sets of calibration signals:

and

The two sets are defined as in Eqs. ( 9) and ( 10), but with interchanged filters between left and right channels. The two filters sets are employed at different system operating times. Due to the ideal filters which satisfy Eq. ( 12), the correlation of the calibration signals as in Eq. ( 11) is zero, i.e.  17)) with y(f ) = y 1 (f ) from Eq. ( 19); and, (3) calibration signals set 2 (Eq. ( 18)) with y(f ) = y 2 (f ) from Eq. ( 20).

The calibration signals are played back by the loudspeakers, instead of playback of the original audio signals, as in Eq. ( 1), and are recorded by the microphone. The new system model in this case becomes:

A system block diagram is shown in Fig. 1. In the diagram, the processing of the left and right input signals before playback is controlled by a single switch with three different states: (1) normal playback (Eq. ( 1)), (2) calibration signals set 1 (Eq. ( 19)), and, (3) calibration signals set 2 (Eq. ( 20)). RTFs are estimated using the measured signals in Eqs. ( 19) and (20). Initially, RTFs between these measured signals and the calibration signals from Eqs. ( 17) and ( 18) are estimated. For y 1 (f ), for example, H 1 L (f ) is defined similarly to Eq. ( 5), using:

where the last line was derived using Eq. ( 11) and the conclusion derived above that the correlation is zero for the case of ideal filters. Note that in order to avoid a zero denominator due to the construction of r 1 (f ) in Eq. ( 17), only frequency bands of even indexes are considered. Repeating the same estimation process for y 2 (f ) and l 2 (f ), y 2 (f ) and r 2 (f ), and y 1 (f ) and r 1 (f ), will lead to estimation of the two RTFs for the entire frequency range, due to Eq. ( 16):

and

Note that while this estimation process with ideal filters leads to zero estimation error, filters in practice are never ideal. RTF estimation is described now for the case of practical filters, with the following assumptions: 

where is a predefined threshold. It is important to note that O pass i (f ) and O stop i (f ) do not cover the entire frequency range; there are frequencies in the transition between these two frequency bands.

ii) The pass bands used for defining these filters do not overlap, i.e.:

iii) The union of all pass bands covers the entire frequency range, i.e.:

Under these assumptions, the derivation of the estimation method for ideal filters is repeated with the following differences. B * i (f ), B j (f ) = 0 from Eq. ( 13) is now replaced by

where S is a subset of bands which are sufficiently distant from one another such that any one pass band overlaps only with stop bands from the other bands. This leads to Eq. ( 12) being replaced by 11) for frequency bands in S. This leads to a small correlation between signals l(f ) and r(f ). RTF estimation is repeated for more band subsets, until the entire frequency range is covered. This process is demonstrated in the next section for a specific filter implementation, and can be extended to multiple sets of calibration signals.

### V. ANALYSIS OF RTF ESTIMATION

An analysis of RTF estimation using the proposed method is presented for an experimental system comprising a stereo loudspeaker system and a single microphone positioned in a room, for multiple audio signals, and for example filter banks designed for the proposed estimation method. The analysis includes an investigation of the frequency-dependent error between estimated and measured RTFs, the total error, and errors in room acoustic parameters calculated using the RTFs, the RT and the EDT.

## A. Setup

The analysis was conducted for two different environments, in order to test its performance under various acoustic conditions.

### TABLE I SIX ACOUSTIC CONDITIONS OF TWO-CHANNELS RTFS FOR ENVIRONMENT 2

Environment 1-Meeting Room at Ben-Gurion University: The first set of RTFs was measured in a meeting room at Ben-Gurion University of the Negev, with dimensions of (7.2, 6.4, 3.1) m, an approximate volume of 143 m 3 , and an RT of about 0.5 s. The RTFs were measured using a system comprised of two KRK ROKIT 6 loudspeakers and a Bruel & Kjaer 1/2-inch diffuse-field microphone, which were connected via an ESI U24XL soundcard to a laptop. The RT was calculated from measured RIRs using the Schroeder backward integration [31]. The left and right loudspeakers were positioned at (0.3, 1.6, 0.7) m and (0.3, 0.8, 0.7) m, with a distance of 0.8 m between the loudspeakers. The system configuration was chosen since it models a two-channel setup such as a stereo TV. The microphone was positioned at (2.8, 1.2, 1.05) m, which is 2.5 m away from the middle point connecting the loudspeakers. The system was placed slightly towards the room corner due to a large meeting table positioned in the room.

Environment 2-Speech & Acoustic Lab at Bar-Ilan University: The method was applied also to multiple RTFs from the database described in Ref. [32]. In particular, six different RTFs from this database are used in this analysis, which correspond to three different RTs of 160, 360, and 610 ms, and can model an office and meeting rooms. The configuration in Ref. [32], involves a linear microphone array and a array of loudspeakers mounted on two half circles with a radius, r, of 1 and 2 m, around the center of the microphone array. Out of this configuration, the setup employed the fourth array microphone, positioned close to the origin of the circle, and of the loudspeakers positioned at angles -60 and -45 • for a radius of 1 m, and -30 and 15 • for a radius of 2 m. See Ref. [32] for a diagram of this setup. The specific loudspeakers were chosen since the distances between the loudspeakers are similar to configuration 1, and to practical systems such as TV stereo. Overall, the six two-channel RTFs correspond to six acoustic conditions, which are presented in Table I.

For both environments, the analysis is provided for various stereo input signals that include white noise, speech, and music. Three different 20-second duration stereo audio signals were used as input signals:

1) white (uniform) noise, 2) jazz music (taken from [33]), 3) pop music (taken from [34]), and 4) speech (taken from [35]).

## B. Methods

The methods presented in this section are organized as follows. First, an implementation of filter banks designed for the task in hand is presented. Then, the measurement procedure of the RTFs and associated pre-processing of these functions is described. Finally, the application of the method to these functions is presented, including the derivation of the errors.

The example design of filter banks for the proposed estimation method is based on 1/2-octave filters with discrete-Fouriertransform (DFT) based implementation. Two sets of filter banks are employed, following the general framework presented for practical filters in the previous section. I = 16 center frequencies are selected for the first set of filter banks, and I = 15 center frequencies are selected for the second set of filter banks, with the sampling frequency, f s , set to 44100 Hz. The center frequencies are presented in Table II for both sets. Note that the center frequencies of the set 2 are shifted by a 1/4 octave compared to those in set 1. The reason for this choice will be apparent shortly. For both sets, and for each center frequency, a corresponding frequency band, O i , is defined as follows:

where O 0 is modified to start at 0 Hz and O I-1 is modified to end at f s /2. For both sets and for each frequency band, a corresponding filter, b i [t], i = 0, . . .I -1, where t is the discrete time index, is constructed using a DFT-based implementation as [36]:

where N = 7055 is the DFT length used for constructing these filters, which, combined with f s , yield a time duration of 160-ms, and q = 0, . . ., N -1 is the DFT frequency index. In particular, DFT frequency indices that correspond to negative frequencies are also included in the summation in Eq. ( 29), so that the filters are real in the time domain. The filters in the frequency domain, B i (f ), are calculated by applying a DFT on b i [t]. Then, G L (f ) and G R (f ) are constructed as in Eqs. ( 7) and ( 8), respectively, using filters B i (f ).

As an illustrative example, filter B 4 (f ) from set 1 is presented in Fig. 2 for a DFT of length 5 N for improved frequency resolution. A magnitude close to unity is evident at the corresponding octave band, while a relatively high attenuation is observed away from the pass band. A logarithmic y-axis is used in this figure. An ideal filter corresponding to B 4 (f ) is also presented, but with a linear y-axis. The remaining filters, B i (f ), show similar behavior. Filters G L (f ) and G R (f ) for set 1 are presented in Fig. 3 for a DFT of length 5 N . Due to the construction using filters from Eq. ( 29), G L (f ) and G R (f ) sum to unity at the original DFT frequencies, and the inverse DFT of the summation of these functions gives an impulse function, which was a consideration for this specific implementation, as discussed in the next section. G L (f ) and G R (f ) constructed using ideal filter are also illustrated using a linear y-axis scale. Filters from set 2 are not presented as they are similar in behavior. In Fig. 4,|G  * L (f )G R (f )|, which is proportional to the correlation (c.f. Eq. ( 11)), is presented for both sets. High values of |G * L (f )G R (f )| are evident for both sets at frequencies in the transition between the frequency bands. At these frequencies, correlation is expected to be higher, and this may degrade RTF estimation in Eq. (21). However, at frequencies where |G * L (f )G R (f )| is high for set 1, it is low for set 2 and vice versa. L (f )G R (f )| for both sets is lower than approximately -20 dB at all frequencies, which can facilitate improved estimation using two sets compared to estimation using a single set, as demonstrated in the next section. This is the reason that the filters are divided into two sets in the manner described in Table II.

Next, the mapping of frequencies that have minimum   sets can be considered, such as a fixed mapping using the center frequencies of each set. Finally, note that the curves that correspond to ideal filters cannot be seen in Figs. 4 and5, as

For environment 1, the RTFs of the two channels were measured as follows. Each loudspeaker (separately) played back a 20-second white-noise signal. The signal recorded by the microphone along with the input signal of the loudspeakers were recorded by the computer. RTFs from the two loudspeakers to the microphone position were then computed using these signals and MATLAB's tfestimate function, with a 1-second duration window and an overlap factor of 2. For each transfer function, a corresponding room impulse response (RIR) was calculated using an inverse DFT, and these are denoted h L [t] and h R [t] for the left and right channels, respectively. The system buffer, or time delay, due to all hardware components including the sound card was compensated for. For environment 2, RIRs from Table I were initially downloaded (see Ref. [32]), and then resampled to meet the sampling rate of the filters. The resampled RIRs were truncated to a 1-second duration, and corresponding RTFs were then calculated.

To investigate estimation using the proposed method, signals y 1 (f ) and y 2 (f ) as in Eqs. ( 19) and ( 20), respectively, were generated in a computer simulation using the measured RTFs and calibration signals generated using the filters presented in this section. Noise was generated using a zero-mean Gaussian distribution and added to the output signals to model measurement noise. The variance of the noise was set equal over frequency to produce a 40 dB average signal-to-noise ratio (SNR).

, and H 2 R (f ) were calculated using MATLAB's tfestimate function. As an initial step, MATLAB's tfestimate function computes the auto and cross spectra using estimates of the statistical expectation, which are calculated by averaging spectra over multiple time blocks. In particular, all of the signals are first split up into B segments with an overlap factor of 1/2, which are then used for approximating the expectation. E.g., the auto-spectra of s L (f ) is approximated as:

where n is the time-block discrete index, and s * L, n (f ) is the input signal at block n; moreover, due to the overlap factor of 1/2, all neighboring segments of a signal share half of the samples. Furthermore, the block time duration is assumed to be sufficiently long compared to the RTF, H(f ), in time, as required by the multiplicative transfer function assumption [37]. Finally, a Hamming window function was applied to each time block in practice for a modified periodogram with desired frequency characteristics [38]. Given the auto and cross spectra,

, and H 2 R (f ) were calculated for both sets as in Eq. ( 21) Estimated left and right RTFs, ĤL (f ) and ĤR (f ), respectively, were then estimated twice. First, ĤL (f ) and ĤR (f ) were estimated for set 1 only, as in Eqs. ( 23) and (24). Then, ĤL (f ) and ĤR (f ) were estimated for both sets, mapping frequencies that have a pointwise minimum of |G * L (f )G R (f )| of both sets (c.f. Fig. 5 and the discussion that follows).

A frequency dependent error was defined as To evaluate errors in RT and EDT, measured and estimated RIRs were initially calculated for the two channels by applying an inverse FFT on the corresponding RTFs. Measured RIRs are denoted as h L [t] and h R [t], and estimated RIRs are denoted ĥL [t] and ĥR [t] for the left and right channels, respectively. RTs were calculated for the estimtated RIRs using the Schroeder backward integration [31], as the RTs for the measured responses. Errors in RT were calculated as the absolute value of the difference between these estimated RTs and the measured RT. The RT and EDT were calculated using a 20-dB and a 10-dB dynamic range, respectively, see Ref. [31] for more detail.  

## C. Results

In this section the frequency-dependent error is initially analyzed for the RTFs measured in environment 1. Then, errors in frequency-independent measures, the total error, the RT, and the EDT are presented for both environments.

h L [t] and H L (f ) measured in environment 1 are presented in Figs. 6 and7, respectively. The frequency dependent error for the left channel, |H L (f ) -ĤL (f )|, estimated using set 1 only is presented in Fig. 8. The difference signal shows high errors at frequencies near the transition between the pass and stop bands of the filters used to construct G L (f ) and G R (f ). Similar results are evident for the right channel RTF and for calibration signals generated for the remaining input signals, and are thus not presented. In Fig. 9, the difference between the measured RTF and the RTF estimated using both sets is presented. The difference signal in this case is 20 dB lower than the measured RTF at most frequencies, including the transitions between the frequency bands. The normalized error averaged in 1/3 octaves is presented in Fig. 10     but is typically significantly lower. The total estimation error for the left channel, the error in the RT, and the error in the EDT are presented in Table III for all input signals. Finally, the mean and variance of the total estimation error for the left channel, the error in the RT, and the error in the EDT over the six conditions  In conclusion, frequency dependent errors, total (frequencyindependent) errors, and errors in room acoustic parameters have been presented in this section for multiple acoustic conditions. These errors are reasonably low, demonstrating the effectiveness of the proposed estimation method.

### VI. LISTENING TEST

A listening test was performed with the aim of evaluating the perceptual-transparency of the calibration signals when played back using the system loudspeakers with speech and music input signals. The listening tests were conducted in the same meeting room described in the previous section, but with the left and right loudspeakers positioned at (3.2, 6.1, 0.7) m and (4, 6.1, 0.7) m (keeping the same distance of 0.8 m between the loudspeakers), and the listeners were positioned at (3.6, 3.93, 0.7) m, which is 2.17 m on the axis of the loudspeaker middle point.

## A. Methodology

The listening tests were designed for evaluating the perceptual-transparency of the developed method, and for comparing its performance with that of the baseline solution of signal playback from a single loudspeaker. For this purpose, three systems are considered:

• Reference playback of the original stereo audio signals,

• Test playback of the signals after applying the developed method, i.e. playback for the calibration signals, and • Anchor playback from the left loudspeaker only. An ABX comparison-based test was conducted [39] that employs three audio signals with a 5-sec duration, played back with pauses of 1.5-sec between the signals, as presented in Table V. In the table, signal X is either Reference or Test with equal probability for the sequences in lines 1-2, or Reference or Anchor for the sequences in lines 3-4. Lines 1-2 serve to investigate if the Test system is perceptually-transparent compared to the Reference system, and, similarly, lines 3-4 serve to investigate if the Anchor system is perceptually-transparent compared to the Reference system. The signal types employed were the speech and music input signals defined in Section V. Different segments of the same audio material were used for producing signals A, B, and X, and in each test an ABX sequence was played only once. After playback, listeners were required to answer two questions: 1) Is system X the same as system A, or is it the same as system B? 2) Did you hear a difference between system A and system B, or did you guess? 24 normal hearing subjects (19 male, 4 female) participated in a listening experiment. Prior to the experiment, the subjects were trained using six examples of Anchor and Test systems. Testing began only after the subjects' training results were examined, showing that the subjects understood the instructions. For each listener, the experiment included 24 trials, corresponding to four repetitions of each of the six conditions (Test/Anchor × Jazz/Pop/Speech). The order of the tests and the order of signals A and B in each test were selected randomly. The results were averaged across subjects. . 11, 12, and 13 show the average success rate of Test and Anchor systems for jazz music, pop music, and speech, respectively. Fig. 14 shows the overall success rate, which is the average for all signal types. In each figure, 95% confidence intervals for discrete variables are plotted (for more details, see Wilson Score Intervals [40]), and a guess report is also included in the caption of the figures corresponding to the second question the listeners were asked. A success rate of 50% is interpreted   as perceptually-transparent since it corresponds to the average success rate of an equiprobable guess. A success rate of 100% is interpreted as completely non-transparent, and a 75% rate is interpreted as partially-transparent. The results show that the method developed is perceptually-transparent for the jazz music audio recording, and is partially perceptually-transparent for the pop music and speech. On the other hand, the anchor system, or baseline solution is very close to being completely non-perceptually-transparent for all input signals.

# Figs

## VII. CONCLUSION

An estimation method for a two-channel RTF using a single microphone was presented. The method was validated on measured RTFs in a simulation study, showing low estimation errors. The method was also investigated in a listening test, and was shown to be perceptually-transparent for an example of a music audio recording, and partially-perceptually transparent for other examples. The proposed approach therefore enables the estimation of a two-channel RTF in a perceptually-transparent manner, using the original audio signals.

One direction for future work could be the application of the method sequentially over limited frequency regions. While this may extend the estimation time, it may improve perceptual transparency. Another direction for future work is the extension of the method to more loudspeaker which should be relatively straightforward.

The proposed method has the following limitations. First, due to the use of practical filters for generating the calibration signals with non-zero stop band magnitude, there is signal leakage, or crosstalk between the filters used for the two channels. This leakage introduces an interference in the RTF estimation function, limiting the estimation accuracy. A second limitation is related to the application of the method, e.g. to RTF equalization. Due to the use of a single microphone, minor changes in the measurement geometry may lead to high variation of the measured RTF in particular at high frequencies. The measured transfer function at the microphone position may therefore be different than the one at a listener's position, especially at high frequencies. Finally, the perception of the calibration signals demonstrates additional limitations. A further study is required to understand these perceptual limitations, and their dependence on signal type, filter design, etc. Future work could also include the implementation and evaluation of the method for sound calibration in a room.

