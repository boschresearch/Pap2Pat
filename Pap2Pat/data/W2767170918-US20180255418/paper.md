# I. INTRODUCTION

Enhancing noisy signals, even if recorded in low echoic enclosure, is a cumbersome task, due to the co-existence of interfering speakers and background noise contaminating the desired speaker. In this work, we focus on a multimicrophone solution for extracting the desired speaker from a noisy mixture of multiple speakers.

Beamforming is a widely-used method for speech enhancement using microphone arrays [1]. A comprehensive overview of various speech enhancement and source extraction algorithms is presented in [2]. The minimum variance distortionless response (MVDR)-BF [3], [4] steers a beam towards the desired source such that the desired signal remains undistorted while minimizing the other noise signals. Yet, if interfering speaker is active and a background noise is also present, the MVDR-BF might not effectively mitigate an interfering speaker.

The LCMV-BF was successfully applied in speech enhancement tasks with multiple signals of interest [5]. The LCMV criterion minimizes the noise power at the BF output while satisfying a set of linear constrains, such that the desired source is maintained while the interfering signals are blocked. The LCMV-BF and the MVDR-BF can be designed by using the RTFs 1 [4], [5], rather than a simple steering vector, which is based on the time difference of arrival (TDOA) between microphone pairs, to guarantee sufficiently high performance measures in a wide range of reverberation levels. 1 The RTF is defined as the ratio of the two acoustic transfer functions (ATFs) relating a source signal and a pair of microphones There are many scenarios for which both the desired speaker and the interfering speakers are located in approximately fixed positions, e.g. around a table in a conference room. Nordholm et al. [6], [7] proposed to use either the MVDR-BF, implemented in a general sidelobe canceller (GSC) structure, or the multichannel Wiener filter to extract a single desired source. Both solutions are only capable of suppressing the background noise and are not aiming at the cancellation of a competing speaker. Calibration stage may be beneficial if the speakers' positions are approximately constant. In [8], the authors used recorded signals in the calibration stage in order to find the BF parameters, and in the test phase they used a "master-slave" structure in which the BF weights of the "master" BF, applied to the real signals, are copied from the "slave" BF, learned from the pre-recorded signals.

The LCMV-BF is a more suitable solution in multiple concurrent speakers scenarios. To apply the LCMV-BF, it is necessary to estimate the RTFs and the noise covariance matrix. In this paper, we present a practical end-to-end implementation of a multichannel speech enhancement system based on the LCMV beamformer and a post-processing stage. A recently proposed neural network mixture-maximum (NN-MM) algorithm [9] is utilized to derive a voice activity detector (VAD). A new speaker position identifier (SPI) is proposed based on a pre-trained RTF library. Finally, the NN-MM algorithm is applied to the LCMV output as a postfilter.

## II. METHOD A. Problem Formulation

Consider an array with M microphones in a predefined fixed position. The array captures a desired speaker contaminated by interfering speaker and stationary background noise. Each of the involved signals undergo filtering by the acoustic impulse response (AIR) before being picked up by the microphones. In the time-domain the signal received by the m-th microphone is given by:

where s d (n), s i (n) and v m (n) are the desired source, the interfering source and the stationary background noise, respectively. In real-life scenarios more than two speakers can be simultaneously active. In this paper, for simplicity, we focus on the two speakers scenario. The AIR between the desired speaker and the m-th microphone is h d m (n) and similarly, the AIR between the interfering source and the m-th microphone is h i m (n). In the short-time Fourier transform (STFT) domain z m (n) can be stated as:

where l and k are the time-frame and the frequency indexes, respectively. The terms h d m (l, k) and h i m (l, k) are the ATFs, defined as the Fourier transform of the corresponding AIRs. The received signals in (2) can be conveniently formulated in a vector notation:

where:

Assuming the desired speech signals, the interference and the noise signals are uncorrelated, the correlation matrix of the received signals is given by:

with:

and (•) H is the conjugate-transpose operation.

# B. System overview

In this paper, we propose a new control mechanism for the update of the LCMV-BF parameters. The noise covariance matrix is initialized by averaging the first frames of the utterance, assumed to be noise-only frames. The NN-MM algorithm [9] is then applied to the reference microphone to extract an SPP map. A VAD is calculated based on the SPP detector and used to control the noise estimation update. In the calibration stage, an RTF library, consisting of a specific RTF for each position, is calculated. In the test stage, the RTFs-matrix is initialized with the RTFs of this library. A new scheme for SPI is also proposed to classify speech-active frames to be either associated with the desired or interfering sources. The classification results of the SPI control the RTFsmatrix update. Finally, the LCMV is applied to the noisy input, followed by a postfilter based on the NN-MM algorithm [9].

# C. Linearly Constrained Minimum Variance

In this work, we are interested in extracting the desired speaker from the noisy signal, while suppressing the interference signal. For that, we are applying a BF w(l, k) to the noisy signal z(l, k). The BF output ŝd (l, k) is given by:

where w(l, k) = [w 1 (l, k), . . . , w M (l, k)] T . The filters are set to satisfy the LCMV criterion with multiple constraints [10]:

where g(l, k) is the desired response, set in our case to [1, 0] T , and

is the RTFs-matrix, with

and

where 'ref' is the reference microphone. The well-known solution to ( 8) is given by,

To calculate (12), an estimate of the RTFs-matrix C(l, k) and the noise correlation matrix Φ vv are required.

# D. Noise estimation

In order to estimate Φ vv , we assume that there are time segments for which none of the speakers is active. These segments are utilized for estimating the stationary noise power spectral density (PSD). Define l start v , l stop v as a noise-only time segment and initialize the corresponding PSD matrix:

We assume that the first 0.5 sec can be utilized for initializing Φ vv , and discuss a VAD-based adaptation scheme in Sec. III.

# E. RTF estimation

This section is dedicated to the estimation of the RTFsmatrix C(l, k) (9). In static scenarios, the RTFs of the desired and the interfering sources can be pre-estimated in a calibration stage. Under the assumption that the sources' positions are approximately fixed, their identity as either desired or interference source can be determined. The RTFs library can be constructed off-line using different speakers and utterances than used in the test stage. As the match between the preestimated RTFs and the corresponding RTFs of the actual environment is presumably high, good identification results may be obtained.

It is assumed that there are time-frames in which only one source (either desired or interference) is active. These frames, [l start , l stop ], can be identified and classified to desired/interference segment as described in Sec. III. This segment can then be used for estimating the corresponding RTF. This assumption, although restrictive, can be met in realistic scenarios, for which double-talk scenarios only rarely occurs. Now, applying the generalized eigenvalue decomposition (GEVD) to Φzz (l, k) and the stationary-noise PSD matrix Φvv (l, k) we have:

where λ(k) is the generalized-eigenvalue, f (k) is the corresponding generalized-eigenvector and Φzz (l, k) is the correlation matrix estimated from the frames [l start , l stop ] and ( 13).

Under the assumption that only one speaker is active at this segment, the eigenvector associated with the largest eigenvalue is a scaled version of an RTF c(l, k) ∈ {c d (l, k), c i (l, k)}. Therefore, we normalize the result to obtain a proper RTF:

# F. DNN-based SPP post filter

The output of the BF ŝd (l, k) (7) is a single channel signal contaminated by residual noise. We apply the NN-MM algorithm [9] to the BF output to enhance the noisy signal. The NN-MM algorithm utilizes a phoneme-based Mixture of Gaussians (MoG) where each Gaussian represents a different phoneme, and a trained deep neural network (DNN) phonemeclassifier, which classifies time-frames to one of the phonemes in the phoneme-based MoG. By merging the generative MoG and the discriminative DNN, the NN-MM constructs a timefrequency SPP map ρ(l, k). A soft spectral attenuation, which was found useful for speech enhancement [9], [11], is then applied to the BF output:

where β is the soft attenuation level. Note, that ( 16) is carried out in the log-spectrum domain.

## III. THE LCMV CONTROL MECHANISMS

Until now it was assumed that the time-segments in which each speaker is active and their classification as desired/interference source are known. In this section we describe control mechanisms that will be utilized to infer this information from the measured data in real-life scenarios.

# A. SPP-based VAD

As was mentioned above, the noise PSD matrix Φ vv (l, k) is a crucial component in the LCMV BF design. In (13) the time-frames in which only the background noise is active are required. Here, we propose an SPP-based VAD to determine these noise-only frames. The noisy signal from the reference microphone, denoted z ref (l, k), is used as the input to the NN-MM algorithm. The NN-MM calculates the SPP of the noisy signal, ρ(l, k). The probabilities are then aggregated across frequencies to yield a VAD decision per frame:

where T r is the threshold value. In our implementation we set T r = N DFT /4, where N DFT is the STFT frame-length. Note that the proposed VAD is set to the value '1' if any speech source is active, regardless of the identity of this source. Given that the current frame is noise-dominant, the noise estimation can be recursively updated:

where α is the learning rate factor. Otherwise, no noise adaptation is applied.

# B. Speaker position identification based on pre-trained RTFs

An accurate RTF estimation is a crucial component in the BF design. For that, time-frames dominated by a single speaker should be determined. Given the VAD in (17), we know whether any speech source is active or not. Yet, we do not know whether the desired speaker, the interference speaker or both are active.

In our scenario, the speakers position are fixed, and the reverberation level is low. The fixed positions makes the pretraining stage feasible. Consequently, in the calibration stage an RTF library, which consists of a specific RTF for each position, is measured. We set the components of the RTF library to c s (k), s = 1, . . . , N s , where N s is the number of possible positions (in our experiments N s = 4). This stage is only carried out once and does not recur. The RTFs-matrix (9), is then initialized with the components from the library, without loss of generality it is set to C(k) = c 1 (k), c 4 (k) . At the test phase, given speech-active frames, an RTF is estimated using (15). The estimated RTF ĉ(l, k) is then projected to each component of the RTF library, by calculating the cosine distance:

The fact that we deal with low reverberation level makes the distance measure (19) a valid affinity measure between impulse responses (see discussion in [12].). Under the assumption that only one speaker is active, the position of the active speaker is determined by I(l):  signal. Note, that the VAD accurately tracks the speech-active frames. Additionally, it can be easily verified that when both the desired and the interfering speakers are active, the VAD is on as well. In order to evaluate the proposed SPI scheme, we estimated the RTF based on time-frames classified by the VAD as speech-active. Define I(l, k) = argmax i D i (l, k) the frequency-wise speaker position identifier. Figure 3 depicts these decisions for a specific set of speech time-frames. We first analyzed frames from the segment [0 ÷ 3]sec in which the desired speaker is active. Fig. 3a illustrates the frequency-wise SPI decisions. It is clear that, in this case, most frequencies are associated with position #1, which is occupied by the desired speaker with only low percentage of misclassification.

The aggregated measure in (20) will therefore identify the first position as the source of the estimated RTF. We further examined time-frames where both speakers are active. It can be easily deduced from Fig. 3b, that in this segment I(l, k) is not dominated by any position and hence will not be determined as either desired or interference speaker, and consequently no valid RTF can be estimated. Finally, the estimated desired signal, s(l, k) (16), is depicted in Fig. 4. First, the BF suppresses the interfering speaker power by approximately 20dB. The NN-MM algorithm was then applied to attenuate the residual background noise. It is evident that the background noise was significantly suppressed by the joint application of the BF and the postfilter. 

## V. CONCLUSION

In this paper, a system for speaker extraction and noise reduction was presented. New SPP-based VAD controls the noise covariance matrix update, and an SPI method, which is based on an RTF library, controls the RTFs-matrix update. The updated LCMV-BF was then applied to enhance the speech. The NN-MM algorithm was used as a postfilter to attenuate the residual noise. The proposed algorithm was examined using real-life recordings in a low-reverberant enclosure, and proved to perform well in a wide range of SNR and SIR levels.

# A. Experiment setup

The algorithm performance was evaluated by a set of experiments using a recording campaign carried out in a low echoic enclosure. There are four positions in the experiment, denoted 1, 2, 3, 4. Microphone array consisting of seven omnidirectional microphones arranged in U-shape was used.

In order to control the signal to noise ratio (SNR) and the signal to interfering ratio (SIR), the desired speaker, the interfering speakers and the background noise were separately recorded. The desired speaker was located at position #1. The fifth microphone was chosen to be the reference microphone. The other positions were occupied with the interfering speaker. The background noise was recorded separately. For the recording campaign, we used 6 speakers (3 male and 3 female speakers) and recorded 1800 utterances. The desired speaker was counting, while the interfering speakers were reading from   the Harvard database [13]. The separate recordings were then used to synthesize real-life scenarios. The time-line for each scenario is described in Table I, and explained in the sequel. At 0÷0.5sec the speakers are inactive, at 0.5÷3sec the desired speaker speaks alone, at 3 ÷ 6sec only the interference speaker is active, at 6÷9sec the sources are not active and at 9÷16sec the desired speaker and the interfering speaker are all active. Note, that the background noise is present during the entire utterance.

# B. Experimental results

To evaluate the enhancement capabilities, we evaluated the SNRout and the SIRout at the output of the algorithm as a function of SIRin at the input to the algorithm in the range {-5, 0, 5, 10, 15}dB for SNRin in the range {-5, 0, 5, 10}dB. In Fig. 1 we present the results obtained by averaging of 15 signals for each scenario. Due to space constrains we only present the results for SNRin=-5,10dB. The resulting SNRout and SIRout are presented with and without the postfilter. It is easily verified that the SIRout is approximately linearly growing with SIRin. Additionally, the NN-MM postfilter significantly improves the SNRout. This is consistent for all levels of SNRin. Interestingly, the postfilter also improves SIRout. This may be attributed to the spectral shape distortion introduced to the interference source resulting by the application of the LCMV-BF. To further evaluate the performance of the algorithm we set SIRin to 5dB, and the SNRin to 2dB. The desired speaker was placed in the position #1, and the interfering speaker was placed in position #3. The noisy STFT at the reference microphone z ref is presented in Fig. 2. The decisions of the SPP-based VAD are marked with a red line on top of the time

