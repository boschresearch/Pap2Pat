# DESCRIPTION

This application claims the benefit of U.S. provisional patent application Ser. No. 62/432,908, filed 12 Dec. 2016, for METHODS FOR DETECTING AND MAPPING SPINAL CORD EPIDURALLY-EVOKED POTENTIALS, incorporated herein by reference.

## FIELD OF THE INVENTION

Embodiments of the present invention relate to a novel approach to automatically detect the occurrence of evoked potentials, quantify the attributes of the signal and visualize the effect across a high number of spinal cord epidural stimulation parameters. This new method is designed to automate the current process for performing this task that has been accomplished manually by data analysts through observation of the raw electromyography (EMG) signals, which is laborious and time-consuming as well as being prone to human errors. The proposed method provides fast and accurate framework for activation detection and visualization of the results within five main algorithms.

## BACKGROUND

This invention relates in general to detection of evoked potentials in the field of lumbosacral spinal cord epidural stimulation. Previously it has been shown that epidural electrical stimulation with a combination of locomotor training and/or pharmacological interventions in animal models was able to highly promote spinal circuits functionality after complete spinal cord transections in rats. Subsequently, in the past several years, clinical studies have also reported that lumbosacral spinal cord epidural stimulation (scES) combined with activity-based training progressively re-enabled full weight bearing standing and volitional control of lower limbs in individuals with chronic complete paralysis. Remarkably, the appropriate selection of stimulation configuration (amplitude, pulse width, frequency and anode/cathode assignment) was shown to be critical to promote the generation of effective motor patterns. Mapping experiments were initially performed with participants in supine position, recording motor evoked potentials from different lower limb muscles using surface EMG during scES with different sets of electrode configuration, in order to study the topographical features of recruiting leg muscles by scES and also to provide useful information for the selection of electrode configurations applied for promoting lower limb motor function. EMG is a diagnostic procedure that uses electrodes to detect electrical signals transmitted by motor neurons that cause muscles to contract. The task of determining the links between scES parameters and the characteristics of the evoked potentials detected by EMG is referred to as “mapping” task in this study.

To study the characteristics of the scES induced evoked potentials, the first step is to localize them inside raw EMG signals that are recorded from several leg muscles by segmenting each EMG signal based on the stimulation onset. The precise detection of each epidurally evoked potential in order to determine the effective threshold for scES intensity that triggered the occurrence of the first visible evoked potential for each muscle, is one of the most challenging tasks in the EMG analysis in the scES content. This task is usually performed by visual inspection by a trained observer, which is considered to be the most accurate method for activation detection. However, it is a laborious task when facing a great stack of data recorded from several muscles during various experiments and therefore can be prone to human errors and also would limit the ability to allow scalability to a high number of patients. Therefore, to facilitate the activation detection process, an accurate computer-based method is proposed in this work.

There have been several methods proposed for computer-based change detection for EMG signals in the literature such as single or double threshold detector, Teager-Kaiser Energy Operation, wavelet template matching, supervised and unsupervised learning algorithms or statistical criterion determination methods like hidden Markov models (HMM) or Gaussian mixture models (GMM). The main goal of all such methods is to convert the original raw signals into a set of estimated sequences that make the highest distinction between the signals before and after change and detect the occurrence of the change and the corresponding time instant t=0 as early as possible.

Most of the automatic onset detection methods can be divided into three main stages: conditioning, decision threshold, and post-processing. In the conditioning stage, the EMG signal goes through a test function, which is a type of event indicator. In the second stage, the algorithm will set a threshold that indicates the first point of the signal change. Finally, the last stage deals with the false alarms by setting certain constraints on the detected onset values. Most of the methods differ based on the type of test function, the decision rule, which involves the selection of constant or dynamic thresholds, and the heuristic constraints for the final detected onset, which varies based on the application and the characteristics of the EMG signals. There are several categories for the event indicator function such as on-line versus off-line, or supervised versus unsupervised learning algorithms. If an algorithm is causal, meaning that it operates only based on current and previous samples of the signal and not the future values, the method is called on-line, otherwise it is considered off-line. Also, if the training input data for a learning method is already labeled using a priori information, the method is supervised, and if the algorithm estimates a model for the input data using certain parameter estimation techniques, it is an unsupervised technique.

In every activation detection method, sensitivity to the noise level in the signal is a great challenge. Selection of a proper conditioning and post-processing method usually helps to minimize the effect of noise on the accuracy of the method. It is also notable that some of the proposed methods, i.e. supervised methods, are highly dependent on the prior information about the signal which makes those methods semi-automatic and their accuracy application-dependent.

## SUMMARY

Voluntary movements and standing of spinal cord injured patients have been facilitated using lumbosacral scES. Identifying the appropriate stimulation configurations (amplitude, pulse width, frequency, and anode/cathode assignment) is an arduous task and requires extensive mapping of the spinal cord using evoked potentials. Effective visualization and detection of muscle evoked potentials induced by scES from the recorded EMG signals is critical to identify the optimal configurations and to understand the effect of specific scES parameters on muscle activation. The present invention is a novel method for automatically detecting the occurrence of evoked potentials, quantifying the attributes of the signal and visualizing the effect across a high number of scES parameters. This new method is designed to automate the current process for performing this task that has been accomplished manually by data analysts through observation of the raw EMG signals, which is laborious and time-consuming as well as being prone to human errors. The proposed method provides fast and accurate framework for activation detection and visualization of the results within five main algorithms. The first algorithm converts the one-dimensional EMG signal into its 2-D representation by overlaying the located signal activation building blocks. Second, the Generalized Gaussian Markov Random Field (GGMRF) technique is applied to the constructed 2-D EMG representation to de-noise the EMG signal. Thirdly, the evoked potentials are detected using a statistically optimal maximum likelihood estimator together with comparing the probability density functions of the muscle activations to the background noise utilizing a log-likelihood ratio. Fourthly, several features of the motor units such as peak-to-peak, latency, integrated EMG and Min-max time intervals are extracted from the evoked muscle responses. Finally, the extracted features are visualized as Colormap images or another convenient form of chart, graph or table. In comparing the automatic method vs. manual EMG processing on more than 700 EMG signals from five individuals, the new automated approach decreased the processing time from several hours to less than 15 seconds for each set of data, and demonstrated an averaged accuracy of 98.28% based on the combined false positive and false negative error rates. The sensitivity of the new method to signal to noise ratio was tested using simulated EMG signals and compared to two existing methods, where the novel technique showed much lower sensitivity to signal to noise ration. In conclusion, this study clearly demonstrates the advantages of the proposed approach for improving the accuracy and speed in complex data analysis.

Disclosed herein is a novel method that addresses the two main challenges that a fully automatic activation detection method is facing by proposing an unsupervised and on-line approach that deals with the stochastic characteristics of the EMG signals in the scES application. This novel method is adapted to automatically detect epidurally evoked potentials using a general framework in the context of scES-EMG mapping and is able to effectively de-noise, detect, extract the key features and visualize the occurrence of muscle evoked potentials that are induced by scES and increase the accuracy and efficiency of the physiological mapping process in order to determine the underlying relationships between the scES parameters and muscle activations. Consequently, this framework assists the data analysts to promptly decide on further adjustments or improvements in designing future experiments.

This summary is provided to introduce a selection of the concepts that are described in further detail in the detailed description and drawings contained herein. This summary is not intended to identify any primary or essential features of the claimed subject matter. Some or all of the described features may be present in the corresponding independent or dependent claims, but should not be construed to be a limitation unless expressly recited in a particular claim. Each embodiment described herein is not necessarily intended to address every object described herein, and each embodiment does not necessarily include each feature described. Other forms, embodiments, objects, advantages, benefits, features, and aspects of the present invention will become apparent to one of skill in the art from the detailed description and drawings contained herein. Moreover, the various apparatuses and methods described in this summary section, as well as elsewhere in this application, can be expressed as a large number of different combinations and subcombinations. All such useful, novel, and inventive combinations and subcombinations are contemplated herein, it being recognized that the explicit expression of each of these combinations is unnecessary.

## DETAILED DESCRIPTION OF THE PREFERRED EMBODIMENTS

For the purposes of promoting an understanding of the principles of the invention, reference will now be made to selected embodiments illustrated in the drawings and specific language will be used to describe the same. It will nevertheless be understood that no limitation of the scope of the invention is thereby intended; any alterations and further modifications of the described or illustrated embodiments, and any further applications of the principles of the invention as illustrated herein are contemplated as would normally occur to one skilled in the art to which the invention relates. At least one embodiment of the invention is shown in great detail, although it will be apparent to those skilled in the relevant art that some features or some combinations of features may not be shown for the sake of clarity.

Any reference to “invention” within this document is a reference to an embodiment of a family of inventions, with no single embodiment including features that are necessarily included in all embodiments, unless otherwise stated. Furthermore, although there may be references to “advantages” provided by some embodiments of the present invention, other embodiments may not include those same advantages, or may include different advantages. Any advantages described herein are not to be construed as limiting to any of the claims.

Specific quantities (spatial dimensions, dimensionless parameters, etc.) may be used explicitly or implicitly herein, such specific quantities are presented as examples only and are approximate values unless otherwise indicated. Discussions pertaining to specific compositions of matter, if present, are presented as examples only and do not limit the applicability of other compositions of matter, especially other compositions of matter with similar properties, unless otherwise indicated.

In some embodiments, the present invention is a method for detection and characterization of evoked potentials in muscles comprising multiple steps. Referring now to FIG. 1, in an initial step 10, epidural stimulation is applied to a patient and an electrical signal evoked from the patient's muscle in response to the epidural stimulation is detected by EMG or other suitable diagnostic process. In a first step 12, the electrical signal is temporally segmented into sequential segments. In a second step 14, image processing techniques are applied to the signal to reduce signal noise. In a third step 16, evoked potentials are detected within the electric signal. In a fourth step 18, features of the evoked potentials are extracted. In a fifth step 20, the evoked potentials are converted into a graphical form for ease of visualization by analysts. Each of these steps are described in further detail below.

2. Materials and Methods

Participants:

In this study, five male individuals with motor complete SCI participated. Two of these participants have AIS grade B and three of them have AIS grade A. The average age of these five individuals at the time of the experiments was 29.82±4.458 years old and the average time since injury was 4.22±1.553 years.

Spinal Cord Epidural Stimulation:

A stimulation unit in combination with a chronical 16-electrode array was surgically implanted at the T11-L1 vertebral levels over the spinal-cord segments L1-S2. It was used to deliver electrical stimulation to the lumbosacral spinal cord of each SCI individual. The scES lower limbs mapping experiments started 2-3 weeks after the surgical implantation.

2.1 EMG Data Acquisition

The supine experiments were performed with the participants relaxed in a supine position. The electrical stimulation waveform had a rectangular, biphasic shape with pulse duration of 450 μsec. In each experiment a particular combination of electrode array is selected to activate, which is referred to as the stimulation configuration. A total of 12 different stimulation configurations were examined for each individual. For each configuration, the scES intensity (in volts) was increased while the frequency (in hertz) was fixed at (2 Hz). This allowed a simple evoked potential as well as a reasonable time frame in which to complete the experiments. During each intensity ramp up, the scES intensity started at a pre-threshold value and increased with 0.1 or 0.5 V increments up to 10 V. scES delivered a minimum of five stimulus pulses at each intensity level. During the performance of each experiment, the surface EMG signals were recorded from 14 leg muscles, using bipolar surface electrodes that were placed on the left (L) and right (R) soleus (SOL), medial gastrocnemius (MG), tibialis anterior (TA), vastus lateralis (VL), rectus femoris (RF), medial hamstrings (MH), and gluteus maximus (GL). The recorded EMG signals were digitized with a sampling rate of 2000 samples per second. In addition, two more surfaced electrodes were placed laterally over the paraspinal muscles in order to record the onset of the stimulus.

2.2 Methodology

In this section, a set of five algorithms is proposed for the mapping task in order to convert the raw recorded EMG signal into its significant building blocks, which are evoked potentials induced by ES, and extract several features of these evoked potentials and visualize them in order to effectively represent the desired hidden information in the EMG records to the data analysts. Moreover, the pseudocode of each step of the framework is presented below.

2.2.1 2-D Representation of EMG Signal

From a computational point of view, each single record of the EMG (x_k,k≥1) is a set of sample observations of a discrete random process (X_k,k≥1). The EMG signals, which were recorded from leg muscles during supine experiments, consist of evoked potentials (w_1, w_2, . . . , w_NϵW), which were induced by ES, and the corresponding stimulation onset timings (t_i), are marked using the paraspinal muscles signals. Utilizing this information, the whole EMG signal can be segmented into its building blocks (W set) where each segment is the time interval between two consecutive stimulation pulsations (FIG. 2A, 2B). Subsequently, the first algorithm converts the EMG signal, X_k, to a 3-D image, δ_k (x,y,z), by overlaying all these EMG portions and then showing their value in 3-D graphs (FIG. 2C). By using the Colormap technique, a 3-D graph can be converted to a 2-D image where the amplitude values are represented by colors (FIG. 2D). Each row in the Colormap image is one segment of the whole EMG signal (Algorithm I, below).

2.2.2 Noise Reduction

After signal to image conversion, it is possible to use image-processing techniques for smoothing the images and consequently de-noising the signals. The 2-D generalized Gaussian Markov Random Field (GGMRF) model was applied to the constructed 2-D images so as to reduce the noise level from the EMG signal. This is an image smoothing method, which preserves continuity and removes inconsistencies in the image that in this context is caused by background noise in the original EMG signals. In this method, each pixel's value, which is the evoked potential amplitude in μV, is being compared to 8-neighborhood pixel set and recalculated using Equation 2.1.

\(\begin{matrix}
{{\hat{\delta}}_{s} = {\underset{\delta_{s}}{argmin}\left\{ {{{\delta_{s} - {\overset{\sim}{\delta}}_{s}}}^{q} + {\sigma^{q}\lambda^{p}{\sum\limits_{r \in v_{s}}{b_{s,r}{{{\overset{\sim}{\delta}}_{s} - \delta_{r}}}^{p}}}}} \right\}}} & {{Equation}\mspace{14mu} 2.1}
\end{matrix}\)

Where δs, {circumflex over (δ)}s and {tilde over (δ)}s are original pixel value, its recalculated value, and expected estimate respectively. vs is the 8-neighborhood pixel set; bs,r is the GGMRF potential; and a and λ are scaling factors. The parameter pϵ[1.01, 2.0] controls the smoothing level (e.g., p=2 for smooth versus p=1.01 for relatively abrupt edges). The parameter qϵ{1, 2} determines the Gaussian (q=2) or Laplace (q=1) prior distribution of the estimator. Our simulations were conducted with σ=1, λ=5, p=1.01, q=2, and bs,r=√{square root over (2)}. An example of the input and output of the GGMRF method and their corresponding muscle activation segments is demonstrated in FIG. 3 (Algorithm II, below).

The advantage of spatial smoothing of EMG signals, compared to the traditional signal low pass and high pass filtering techniques, is that this method offers the option of comparing each evoked potential with the previous and the next activation, and it reduces the signal irregularities that are caused by different sources of noise. Unlike the filtering methods, the image smoothing method offers a de-noised signal without any significant changes in the position and original shape of muscle activations.

2.2.3 Activation Detection

The activation detection algorithm is designed to determine the presence or absence of scES induced evoked potentials in each segment of the EMG signals and consequently the corresponding stimulation intensity threshold. The pre-assumptions for this task are: 1) The intensity threshold Vs0, which caused the earliest evoked potential, is an unknown random value with unknown distribution; 2) The amplitude of the first visible evoked potential is also an unknown value. These are valid assumptions because of the non-stationary nature of EMG signals and the fact that no a priori information about the distribution of the changing parameters is present. It is also notable that these onset values are highly variable and alter based on the choice of stimulation configuration, frequency, muscle type, and also depending on the day-to-day and pre-post training variability. As mentioned above, scES delivers the minimum of five pulse stimulations at each stimulus voltage referred to as an event, (wi+j, 0≤j≤Ni) where min(Ni)=5. Therefore, it is assumed that if at least 50 percent of the EMG segments corresponding to the same stimulation intensity show epidurally evoked potentials, that intensity will be considered as the intensity threshold Vs0.

The general technique implemented in this step is known as the statistically optimal decision (SOD) method. One derivation of SOD is the approximated generalized likelihood-ratio (AGLR) detector. Here, this method is modified and adapted to the present activation detection application. The modified method has three main phases. In the first phase, each segmented and de-noised portion of the signal (w_iϵW) is modeled by a Gaussian probability density function (pdf) and the model parameters μi and σi are estimated using the maximum likelihood estimation (MLE) method (pθ(wi)). FIG. 4B shows the histograms of the one segment of the EMG and its estimated Gaussian distribution. From the statistical point of view, the activation detection method represents a binary selection between the null hypothesis HO that says “there is no significant change in the pdf pθ(wi) of the ith segment of the signal” and the alternate hypothesis that says “there is a significant change in the parameters of pdf pθ(wi).” Therefore, in the second phase, the Gaussian model of all the EMG segments will be compared to the Gaussian model of the background noise by the log-likelihood ratio (LLR) measure. Eq. 2.2 shows the general formulation of the LLR.

\(\begin{matrix}
{s_{k} = {\ln \left( \frac{p_{\theta_{1}}\left( y_{i_{k}} \right)}{p_{\theta_{0}}\left( y_{i_{k}} \right)} \right)}} & {{Equation}\mspace{14mu} 2.2}
\end{matrix}\)

Where yiis the kth sampled-value of wi segment. In order to reduce the high computational cost of this equation, it is presupposed that the occurrence of the scES induced muscle activation does not change the mean μ of the Gaussian pdf and the most significant changes happen in the standard deviation σi of the pdf as shown in FIG. 4C. Therefore, the Eq. 2.2 is modified and simplified herein to Eq. 2.3.

\(\begin{matrix}
{s_{k} = {{\ln \left( \frac{\sigma_{0}}{\sigma_{i}} \right)} + {\frac{1}{2}\left( {y_{i_{k}} - \mu} \right)^{2}\left( {\frac{1}{\sigma_{0}^{2}} - \frac{1}{\sigma_{i}^{2}}} \right)}}} & {{Equation}\mspace{14mu} 2.3}
\end{matrix}\)

The sum of all the sk values over one segment is referred to as CUSUM value Si and is calculated based on Eq. 2.4.

\(\begin{matrix}
{S_{i} = {{\sum\limits_{k = j}^{N_{i}}s_{k}} = {{\left( {N_{i} - j + 1} \right){\ln \left( \frac{\sigma_{0}}{\sigma_{i}} \right)}} + {\frac{\left( {N_{i} - j} \right)}{2}\left( {\frac{\sigma_{i}^{2}}{\sigma_{0}^{2}} - 1} \right)}}}} & {{Equation}\mspace{14mu} 2.4}
\end{matrix}\)

Eq. 2.4 is used to calculate one value for each segment of the signal that represents the highest statistical difference between that segment and the background noise (FIG. 4D).

In the third phase of the algorithm, a dynamic threshold h is calculated for each EMG signal in order to find the first segment of the signal that includes evoked potential and its corresponding stimulation intensity Vs0. In comparison, traditional AGLR uses a constant threshold. Based on the experimental observations, the first event corresponding to the lowest stimulation voltage does not usually trigger any muscle activation and can be considered as baseline. Consequently, the threshold value h can be computed as the summation of maximum and standard deviation of the set of Si that belongs to the baseline (Eq. 2.5).

h=Smax+σS  Equation 2.5

All the steps of the activation detection method are demonstrated in FIG. 4 (Algorithm III, below).

2.2.4 Feature Extraction

The objective of this step is to represent each potential evoked by scES with a set of features that offers the essential characteristics of that evoked potential. As a result, several parameters are selected for the EMG fragments that were segmented in the previous step. These parameters can be calculated automatically or observed visually using the 2-D representation of the EMG signal. Parameters such as activation latency, overall onset of muscle activations and number of peaks of the evoked potentials are observable parameters from 2-D image demonstration of the EMG signal (FIG. 5A). The calculated parameters in this framework are: Peak-to-peak value, which is the absolute value of the difference between the highest and the lowest peaks in the signal and its normalized value based on the highest peak between left and right muscle; Activation latency, the time interval between the stimulus timing and the onset of muscle activation; Time interval between minimum and maximum values, the time interval between the highest and lowest peak; Integrated EMG value, the area under the motor unit curvature after rectifying (taking the absolute value of) the EMG signal; and binary 0/1 values: an indication of the absence or presence of evoked potentials in each segment of the signal (Algorithm IV, below). The aforementioned features are illustrated in FIG. 5B.

2.2.5 Visualization

The last step of the proposed framework is to represent the data processing results in informative ways to show the connection between stimulation parameters and generated results from the computer-based method for each muscle in order to make a convenient representation for the examiner to interpret the data and modify the experiments accordingly. FIG. 6 shows the transformation of 14 EMG signals (FIG. 6A) into a single Colormap image that is showing the peak-to-peak values and the binary image that represents the binary values 0/1 that are the output of the onset detection algorithm (FIG. 6B).

Not every possible stimulation intensity is typically tested in most experimental trials, particularly voltages above the minimum voltage necessary to evoke an activation potential in a muscle. For example, in one set of experiments, testing begins by applying a low voltage and ramping up with 0.1-volt increments. Once all the muscles start to show activations, increments increase to 0.5-volts, and stimulation is applied up to 10-volts, or the highest intensity that the patient feels is comfortable. This increase in increments results in some gaps between data points corresponding to overlooked stimulation voltages. Therefore in order to maintain the continuity and resolution of the Colormap images in the visualization step, the missing values need to be interpolated based on the observed values. This task has been done using cubic smoothing spline method. Assume that there is a given set of coordinates (x0, y0), (x1, y1), . . . , (xn, yn) where the values of xi are in ascending order (stimulation voltages). The objective of the cubic smoothing spline method is to link the gap between adjacent points (xi, yi), (xi+1, yi+1) using the cubic functions Pi; i=0, . . . , n−1; in order to piece together a curve with continuous first and second derivatives. In other words, this technique tends to preserve the values of observed data and interpolated the missing values using the piecewise curve function. The curve function also needs to satisfy the end points matching conditions. The smoothing spline method allows selection of the smoothing parameter. The smoothing parameter determines the relative weight that one would like to place on the contradictory demands of having Pi be smooth (p=0), where Pi is the least-squares straight line that is fitted on the data versus having Pi be close to the data (p=1) so that it is variational cubic spline interpolant. In one embodiment, p=1 in order to preserve a smoothed yet accurately interpolated curves (Algorithm V, below).

3 Results

In this section, the performance of the computer-based activation detection algorithm has been evaluated by comparing the output of the algorithm with the output of manually detected evoked potentials by trained data analysts as the ground truth. The proposed method was also compared with two other existing methods to show its advantages. Finally, the run-time of all the algorithms is presented.

3.1 Comparison with Manual Activation Detection

This comparison is based on calculating sensitivity, specificity, Dice similarity and accuracy as evaluation measures. These parameters are calculated based on true positive (TP), true negative (TN), false positive (FP), and false negative (FN) values. The mathematical equations for calculating these parameters and their values from comparing automatic vs. manual activation detection method on 700 EMG signals recorded from 14 leg muscles of five participants during supine experiments are presented in Table 1.

This table shows the five-number summary of all the comparison measurements. These five values are maximum, median, upper and lower quartile, and minimum values of all the measurements (outliers are excluded). Moreover, the box-plots of all the performance measurement parameters for each individual are shown in FIG. 7. The mean and root mean square error (RMSE) of all the measurements (including outliers) are presented separated based on subjects in Table 2, and separated by muscles in Table 3.

3.2 Comparison with Other Activation Detection Methods

The performance of proposed method was compared with two other methods: the Teager-Kaiser Energy Operation (TKEO) method and AGLR without GGMRF smoothing. The comparison is based on recorded EMG signals as well as simulated EMG signal. The simulated EMG signal was designed using an activation shape signal, X(k) that is convolved with a train of Dirac delta impulses Σn=1k0.01n δ(t−n), where the amplitudes are linearly increasing. The additive white Gaussian noise, n(t), will then be added to the signal based on the desired signal to noise ratio (SNR) to generate the final simulated signal. This signal has 50 segments, and the first 20 segments do not include any activation, and the first 10 segments are considered as baseline. One embodiment of the pseudocode of the TKEO method implementation is presented in Algorithm VI, below.

The results of comparing the proposed method with regular AGLR and TKEO based on the total accuracy in the recorded EMG signals from five patients are presented in Table 4.

As indicated in Table 4, AGLR and TKEO showed lower accuracy rates compared to the AGLR+GGMRF method disclosed herein. This shows that adding the GGMRF smoothing technique to the pre-processing step increases the effectiveness of the activation detection method.

In order to show the sensitivity of the proposed framework to SNR and to compare it with other methods, the SNR of the stimulated signal was increased from −20 to 9 dB and the accuracy measurement versus SNR plotted. The results are shown in FIG. 8. It is clear from this plot that the AGLR with GGMRF significantly outperforms other methods in signals with lower SNR values.

3.3 Calculating Total Run-Time of the Algorithms

The hardware that was used to process the EMG signals and calculate the run-time is a Dell computer, Optiplex 9020, Intel® Core™i7-4790 CPU @ 3.60 GHz, 16.0 GB RAM, 64-bit Operating System. The software is MATLAB™ R2011a. The run-time of the proposed framework is directly dependent on the length of the experiments. Table 5 presents the average run-time of each of five algorithms and the total time for 10 intensity ramp-up experiments with 5 to 7 minutes length.

The average and standard deviation of total execution time for processing the data through all five algorithms is approximately 12.71±2.33 seconds, which compared to the previous manual methods that used to take up to several days, the disclosed automatic method is outstandingly time-efficient. Visualization of the extracted features of the evoked potentials in a visually perceptible format, specifically, colormap images, has been found to greatly aid experimentalists in their efforts to understand the effects of scES and its various parameters (voltage, frequency and electrode configuration) on the motor function of the paralyzed muscles in SCI patients. FIG. 9(A-C) displays a series of colormap images which allow an experimentalist to easily view how different muscles respond to changes in stimulation voltage, frequency and configuration.

4 Discussion

Proposed herein is a novel framework consisting of five algorithms for activation detection and visualization of EMG signals recorded from multiple leg muscles of individuals with spinal cord injuries who have epidural stimulator implantation. Using this framework, a raw EMG signal is converted into a two/three dimensional image, the signal is de-noised using GGMRF image smoothing techniques, the occurrence of scES induced muscle activation is automatically detected, features of the muscle activation are extracted, and visual output is generated for interpretation. Each of these five novel algorithms has several advantages. For instance, the first algorithm that converts signals into images has several benefits such as clearly showing the latencies of all activations as well as the overall intensity onset of scES induced motor responses. It is also useful for the next step that is GGMRF image smoothing to get a de-noised signal without affecting the shape and latency of muscle activations. As it is shown in the results section, adding this step to the framework is also noticeably advantageous for the performance of the next step, which is the activation detection. In the activation detection algorithm, a statistically optimal decision method was developed by applying maximum likelihood estimator (MLE) together with comparing the probability density functions of the muscle activations to the background noise utilizing a log-likelihood ratio and calculating the dynamic activation threshold. In comparing the automatic method for activation threshold detection vs. manual detection (ground truth) on 700 EMG signals, the new automated approach developed here demonstrated an overall accuracy of 98.28% based on the errors of combined false positive and false negative data. It is important to note that the proposed method does not need any a priori information for the statistical model, which makes it a fully automatic method that uses only the current and previous EMG signal values to build the statistical model. Finally, the combination of modified SOD method and GGMRF has proven to have minimum sensitivity to the changes in the signal to noise ratio compared to the other well-known EMG onset detection methods, i.e. SOD method without smoothing and TKEO method using both simulated EMG signal and real EMG signals. Comparing the three methods on the recorded EMG signals indicates the robustness in the accuracy of the proposed activation method in the situation where no information about the noise level in the signal is known. In addition, the feature extraction and visualization steps of the framework help analysts to make accurate and quick connections between the desired EMG features and the scES parameters like intensity voltage, configuration and frequency. In conclusion, this method clearly demonstrates the advantages of implementing a set of algorithms for improving the accuracy and speed in complex EMG data analysis.

Various aspects of different embodiments of the present invention are expressed in paragraphs X1 and X2 as follows:

X1. One aspect of the present invention pertains to a method for detection and characterization of evoked potentials in muscles, comprising recording electrical signals at least one of a patient's muscles; dividing the electrical signals into sequential segments; calculating, for each segment, a highest statistical difference Si between the electrical signal in that segment and background noise; calculating a dynamic threshold h; and detecting an evoked potential in one of the patient's muscles if Si>h in at least 50% of the segments.

X2. Another aspect of the present invention pertains to a method for detection and characterization of evoked potentials in muscles, comprising delivering a plurality of epidural stimulations to a patient at a stimulation voltage, each of the plurality of epidural stimulations separated by a time interval; recording electrical signals at least one of the patient's muscles, wherein the recording is concurrent with the delivering; dividing the electrical signals into sequential segments; calculating, for each segment, a highest statistical difference Si between the electrical signal in that segment and background noise; calculating a dynamic threshold h; determining whether Si>h in at least 50% of the segments; and increasing the stimulation voltage until an evoked potential is detected; wherein the evoked potential is detected if Si>h in at least 50% of the segments.

X3. A further aspect of the present invention pertains to a method for determining the location a muscle activation potential evoked from epidural stimulation and minimum voltage required to evoke activation potential, comprising delivering a plurality of epidural stimulations to a patient at a stimulation voltage; recording electrical signals at a plurality of the patient's muscles; dividing the electrical signals into sequential segments; reducing the noise of the electrical signals; calculating, for each segment, a highest statistical difference Si between the electrical signal in that segment and background noise; calculating a dynamic threshold h; determining whether Si>h in at least 50% of the segments; and increasing the stimulation voltage until an activation potential is detected in one of the plurality of muscles, wherein the activation potential is detected if Si>h in at least 50% of the segments.

Yet other embodiments pertain to any of the previous statements X1 or X2 which are combined with one or more of the following other aspects.

Wherein the method further comprises delivering a plurality of epidural stimulations to the patient's spinal cord at a first stimulation voltage, each of the plurality of epidural stimulations separated by a time interval.

Wherein the delivering and the recording occur concurrently.

Wherein each of the sequential segments has a duration equal to the time interval.

Wherein each segment temporally overlaps with delivery of one of the plurality of epidural stimulations.

Wherein the electrical signals are electromyography signals.

Wherein the method further comprises reducing the noise of the electrical signals.

Wherein reducing the noise comprises converting each electrical signal into a 2-D image; and applying an image smoothing method to the 2-D image to reduce signal noise.

Wherein the 2-D image comprises a plurality of pixels, each pixel having a value corresponding to an amplitude of the evoked potential, and wherein applying the image smoothing method to the 2-D image comprises recalculating the value of each pixel in the 2-D image using the following equation

\({\hat{\delta}}_{s} = {\underset{\delta_{s}}{argmin}\left\{ {{{\delta_{s} - {\overset{\sim}{\delta}}_{s}}}^{q} + {\sigma^{q}\lambda^{p}{\sum\limits_{r \in v_{s}}{b_{s,r}{{{\overset{\sim}{\delta}}_{s} - \delta_{r}}}^{p}}}}} \right\}}\)

Wherein the 2-D image comprises a plurality of pixels, each pixel having a value corresponding to an amplitude of the evoked potential, and wherein applying the image smoothing method to the 2-D image comprises recalculating the value of each pixel in the 2-D image using a 2-D generalized Gaussian Markov Random Field model.

Wherein an event is delivery of a plurality of epidural stimulations at a stimulation voltage.

Wherein a plurality of events are applied to a patient, each event including a different stimulation voltage.

Wherein a plurality of events are applied to a patient, each event including increasing stimulation voltages.

Wherein a baseline is a first event applied to a patient

Wherein Si is determined by

\(S_{i} = {{\sum\limits_{k = j}^{N_{i}}s_{k}} = {{\left( {N_{i} - j + 1} \right){\ln \left( \frac{\sigma_{0}}{\sigma_{i}} \right)}} + {\frac{\left( {N_{i} - j} \right)}{2}{\left( {\frac{\sigma_{i}^{2}}{\sigma_{0}^{2}} - 1} \right).}}}}\)

Wherein σi is an estimated standard deviation.

Wherein Ni is at least 5.

Wherein h is determined by

h=Smax+σS.

Wherein Smax is a maximum deviation of the set Si of the baseline.

Wherein σSi is a standard deviation of the set Si of the baseline.

Wherein the baseline is the lowest stimulation voltage event.

Wherein the method further comprises delivering a plurality of epidural stimulations to the patient's spinal cord at a first stimulation voltage, followed by delivering a plurality of epidural stimulations to the patient's spinal cord at a second stimulation voltage, wherein the second stimulation voltage is unequal to the first stimulation voltage.

Wherein the second stimulation voltage is higher than the first stimulation voltage.

Wherein the method further comprises extracting at least one feature of the evoked potential.

Wherein the method further comprises extracting at least one feature of the activation potential.

Wherein the feature is one of a peak-to-peak interval, a min-max interval, an activation latency, and an integrated EMG.

Wherein the method further comprises displaying the at least one feature in a visually perceptible format.

Wherein the visually perceptible format is a colormap image.

Wherein recording electrical signals at least one of the patient's muscles includes recording electrical signals at a plurality of the patient's muscles, and wherein detecting an evoked potential in one of the patient's muscles includes associating the evoked potential with one of the patient's muscles in the plurality of the patient's muscles.

The foregoing detailed description is given primarily for clearness of understanding and no unnecessary limitations are to be understood therefrom for modifications can be made by those skilled in the art upon reading this disclosure and may be made without departing from the spirit of the invention.

