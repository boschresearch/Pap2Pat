# Introduction

Major issues inhibiting successful patient recovery in intensive care units (ICUs) are the frequent occurrence of clinical alarms and the harsh, shrill noises that generally characterize these sounds. Alarms sound frequently to alert clinicians of physiological aberrancy that exceeds a threshold, yet many alarms have low-positive predictive value [1]. As stated by Edworthy and colleagues, multiparameter auditory warnings can be combined to create varying degrees of urgency [2]. Although the implementation of these results has proven useful to alert clinicians of possible danger, the potential negative consequences from the piercing alarm sounds were not considered from the patient perspective. While clinicians can suffer from alarm fatigue and desensitization, in this project, the patient-specific consequences are of the utmost concern, as patients commonly experience sleep deprivation, post-traumatic stress disorder (PTSD) anchored to critical illness, and delirium after a stay in the ICU [3]. Despite surviving an ICU stay, 88% of ICU patients experience hallucinatory/delusional intrusive memories related to ICU care for up to 8 months after hospital discharge [3], and the incidence of cognitive impairment as a function of ICU stay increases from 6 to 25% of patients [4].

While the underlying causes of these neuropsychological outcomes are not determined, the frequent, loud noises produced by clinical alarms often disturb patients' sleep patterns and sound for extended lengths of time with no explanation to the patient, the reason behind the alarm. Compared to other high-consequence industries, health care suffers from poor positive predictive value alarms, as 67.2% of the alarms of the ICUs are false positives [5].

Our approach of sheltering the patients from alarms is accomplished by the creation of a wearable frequency-selective silencing device which silences the frequencies corresponding to the alarm noises (primarily patient monitor red/crisis alarm) and will allow the passage of all normal sounds (speech and other environmental stimuli), while maintaining their quality to reduce the likelihood of delirium.

## Subtypes of PTSD anchored to critical illness: impact of sound

Research is still ongoing to determine the specific sound exposure level of sound and the impact on neuropsychological outcomes in the ICU; specifically, the fractionation of sound into alarm and nonalarm contributions and the psychoacoustic features of sound (e.g., roughness, sharpness, and amplitude envelope) that may be deleterious to the patient. In the case of passive noise cancellation, sound source localization from a point different from the patient's ears could lead to spatial disorientation. Within the DSM-5 types of PTSD, there is a dissociative subtype of PTSD that is defined by symptoms of derealization and depersonalization [6]. The depersonalization experience could be an "out-of-body" experience, which could exacerbate the PTSD symptomatology. In an effort to not solve one problem and make manifold problems in the process, our approach and design will build from a single microphone passive cancellation process to a microphone array active cancellation process as described below.

# Device design needs

lack of stimulation of the auditory sense can contribute to PTSD and delirium, which is why noise-canceling headphones and/or simple earplugs that dampen all environmental noise entirely are not the desired solution.

## Wearer comfort and sound reproduction

Although patients can have full degree-of-freedom head movement, patients and clinicians may be concerned that wearing headphones or earbuds would be uncomfortable to wear for prolonged periods of time; thus, future iterations of our design will incorporate the work by Voix and colleagues to develop comfortable wearable devices [7]. With wearable devices, there is additional concern of microphone placement and sound localization. With respect to the concern of the microphone being overly sensitive and amplifying environmental sounds that would be otherwise filtered by the human ear, we attenuated this difference by the application of an Audio-Technica (Tokyo, Japan) AT8131 windscreen. An additional concern was the quality of the audio path and exacerbation of spatial disorientation. As an initial step, a single microphone was used. However, future iterations of our design will use a microphone array with digital signal processing (DSP) tools for the real-time synthesis of a 3D sound pressure field using Ambisonics technologies to achieve the spatialization of monophonic signal or the reconstruction of natural 3D recorded sound pressure fields as guided by the work of Gauthier and colleagues [8]. As the focus on a "ground-up" ICU design from a multisensory aspect flourishes, ICU rooms are made to be quieter and more anechoic. As that is achieved, wave field synthesis (WFS), an open-loop technology, can be explored in concordance with environmental design. Specifically, adaptive wave field synthesis, combining WFS and active control to reproduce the spatial character of natural hearing, will ameliorate concerns of patient dissociative subtypes of PTSD symptomatology [9].

# Digital signal processing

To remove the alarm sound, MATLAB (MathWorks, Natick MA) digital signal processing was utilized to initially implement and test our digital filters. A spectral analysis was performed on a single alarm sound to obtain its frequency components. Then, an Infinite Impulse Response (IIR) Elliptic bandstop filter was created to block the frequency that specifically dominated in the spectral analysis. The width of the stopband had to be optimized so that the alarm component was completely blocked, yet the effect on environmental noise was minimized. This led to the creation of filters targeting the common red/patient crisis alarm with the most important ones focused at 960, 1920, 2880 and 3840 Hz.

The dynamic digital filter was then generated in Simulink (MathWorks, Natick MA) using the filter specifications determined in MATLAB. The design is two-fold in that it contains both a detector and a series of filters. The detector continuously processes all incoming environmental sounds and determines the power present in the unfiltered environmental noise as compared to the power present in the filtered version. If this difference exceeds a predetermined threshold, this serves to indicate that an alarm is present in the environment. If the alarm sound is detected, the detector switches on the digital filter, and the filtered version of the noise is passed to the patient. This switching mechanism is critical to the design as it ensures that unnecessary processing and potential distortion will not occur for the patient if no alarms are sounding in the environment.

## Auditory masking

When auditory filtering is used, there is a concern of inadvertently filtering desired auditory stimuli. This is especially important when one needs to respond to the auditory stimulus. A relatively understudied source of response failures deals with simultaneous masking, a condition where concurrent sounds interact in ways that make one or more imperceptible due to physical limitations on perception. Bolton and colleagues have developed a novel combination of psychophysical modeling and formal verification with model checking to detect masking in a modeled configuration of medical alarms. This builds on previous work by adding the ability to detect additive masking while concurrently improving method usability and scalability [10]. The psychoacoustics used to describe masking represent frequency on the Bark scale, which maps a frequency (in Hz) to a location on the basilar membrane where the sound stimulates the receptors the strongest. Frequency to Bark conversion is calculated as z sound = 13*arctan (0.00076*f sound ) + 3.5*arctan ((f sound /7500) 2 ). As the alarm we filtered, the "red" high acuity patient alarm has a spectral component of the peak frequency of its narrow bandwidth outside the range of other typical environmental stimuli (e.g., speech), we did not pursue further model checking for additive masking. However, this approach can be used as other patient alarms (e.g., ventilator and infusion pump) are added to the alarm filtering schemata.

# Device components

The hardware portion of this device continuously completes the digital filtering task during the device's operation. To do this, the Simulink code for the detector and filter has been uploaded onto a Raspberry Pi (Raspberry Pi Foundation, Cambridge, UK) to allow for alarm filtration. A microphone connected to the Raspberry Pi obtains and passes the environmental sound to the digital detector (Figure 1).

# Proof of concept

## Experimental design and testing

To prove objectively that the device accomplished our aims, an experiment was performed to prove that the frequency components specific to the alarms were missing from the filtered sound. In the initial stages of the project, a Fast Fourier Transform (FFT) was performed using MATLAB on the unfiltered alarm sound sample and the filtered alarm in order to compare the magnitudes of the frequency components present between the two sounds (Figures 2 and3).  

## Results

In the objective testing using MATLAB, the series of bandstop filters created on MATLAB dampened the magnitudes of the frequencies present in the alarm in the order of 10 3 , as seen in Figure 2.

Once the filtering on MATLAB proved successful, Simulink (Mathworks) was used to compile the software and deploy the data onto a Raspberry Pi device. By inputting a file (.wave) with both the alarm sound and environmental noise present, it was proven that the Simulink software was able to successfully filter the alarm frequencies as shown in Figure 3.

# Limitations and future directions

As of now, this device relies on the use of noise-canceling headphones to transmit the filtered sound to the patient. Future designs will incorporate a wireless, in-ear device that can perform all the necessary filtering functions and transmission of the filtered sound in the device itself. With an aggressive goal to reduce cost and time of development, our first model uses passive filtering; however, further developments will incorporate active noisecancellation which will obviate the need for the passive device to activate (~100-300 ms) and avoid a slight perceived auditory click of activation. With evolving design, this technologycentered initial approach will require FDA exemption status, so it can be studied in the clinical environment.

# Conclusion

Audible medical alarms are the cause of a number of hazards in hospital and ICU settings. Their shrill acoustic features and the frequency at which they alarm (both in sheer number and frequency spectrum) are responsible for a number of negative consequences, especially for patients. Patients can experience PTSD and delirium secondary to sleep disturbance from alarms and health care providers' divided and diminished attentional resources allocated to alarms. This frequency-selective silencing device was created to alleviate these problems and create a more comfortable environment for the patients during their length of stay in the ICU and promote patient safety.

# Acknowledgements

We would like to thank the Departments of Anesthesiology and Hearing and Speech Sciences at Vanderbilt University, particularly Dr. Ben Hornsby. We would also like to thank the Departments of Electrical Engineering and Computer Science at Vanderbilt University, especially Dr. A. B. Bonds, Dr. Dean Wilkes, and Garrett Hoffman for their assistance. We

# Author details

Alyna Pradhan 1 , Elizabeth Reynolds 1 , Brittany Sweyer 1 and Joseph J. Schlesinger 2 * *Address all correspondence to: joseph.j.schlesinger@vanderbilt.edu 1 Vanderbilt University, Nashville, TN, USA 2 Vanderbilt University Medical Center, Nashville, TN, USA

