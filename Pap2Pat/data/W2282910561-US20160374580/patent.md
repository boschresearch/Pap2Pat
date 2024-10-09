# DESCRIPTION

## FIELD OF THE INVENTION

A method and system of predicting a hypotensive episode using one or more time varying hypotensive biomarkers corresponding to physiological processes in the patient, and generating an acute hypotension prediction classifier based upon classification of 3D temporal representation of two or more biomarkers before an appearance of hypotensive episode.

## BACKGROUND OF THE INVENTION

Acute hypotensive episodes (AHEs) are one of the most critical events that generally occur in intensive care units (ICUs). An acute hypotensive episode is a clinical condition typically characterized by abnormally low blood pressure values and other related values. For example, an acute hypotensive episode may occur in an interval of from 5 minutes up to 30 minutes or more during which at least 90% of the mean arterial pressure (MAP) measurements of a patient are at or below 70 mmHg. According to the other definition of acute hypotensive episode it appears when systolic value of arterial blood pressure (ABP) drops below 90 mmHg. Acute hypotensive episodes may occur due to a large number of causes. The causes of acute hypotensive episodes, among others, may include sepsis, myocardial infarction, cardiac arrhythmia, pulmonary embolism, hemorrhage, dehydration, anaphylaxis, medication, vasodilatory shock, or any of a wide variety of other causes. Often it may be crucial to determine the causes of the acute hypotensive episodes in order to administer appropriate patients' treatment before hypotensive episode. However, when the acute hypotensive episodes are not predicted in time, the practitioners are left with insufficient time to determine the causes of the acute hypotensive episodes and to start patient specific treatment. Also, due to insufficient time appropriate treatment may not be administered. If an acute hypotensive episode is not promptly and appropriately treated, it may result in an irreversible organ damage and, eventually death.

## SUMMARY OF THE INVENTION

The method includes determining a plurality of time varying hypotensive biomarkers corresponding to plurality of physiological processes in patient's organism as a non-linear dynamic complex system and generating an acute hypotension prediction classifier. The acute hypotensive prediction classifier is based upon identifying and classifying a three dimensional (3D) temporal representation of two or more biomarker dynamics that appear before a hypotensive episode occurs.

Classification of the 3D temporal representation is based on calculation and comparison with the critical threshold of the mathematical index (root mean square (RMS) of 2D areas of 3D dynamic images under comparison, cross-correlation of 3D images, different Euclidian distances, etc.) representing time dependences of difference between 3D dynamic images. Such index versus time reflects temporal dynamics of the difference between an initial (or “Standard”) 3D representation of selected high resolution ECG biomarkers (without or together with the additional biomarkers—oxygenation of microcirculatory blood flows monitored by NIRS, lung function estimated by monitoring of an end tidal CO2, etc.) and the evolution of such 3D representation in time before hypotensive episode.

An alarm signal, before the hypotensive event occurs, is generated when the mathematical index crosses the critical threshold. The alarm signal can be a visual alarm, audible alarm or both.

The system includes the high resolution (not less than 500 Hz) ECG subsystem. The additional monitors reflecting behaviour of the patient's organism as a holistic non-linear dynamic complex system before a hypotensive event can be included for example, near infrared spectroscopy (NIRS), end tidal expiratory CO2 concentration, etc. For example a personal computer (PC) is connected with the sensors and real-time monitors of plurality of biomarkers (selected ECG biomarkers, brain parenchymal blood oxygenation, end tidal expiratory CO2 concentration, etc.), processing subsystem that is configured to determine a plurality of selected time variation of selected biomarkers, acute hypotension episode prediction classifier's subsystem, which generates an alarm signal before hypotensive episode and which automatically makes alarm decision analyzing 3D temporal representation of two or more proposed biomarkers' comparing an initial “Standard” 3D representation and variable 3D representation before an appearance of hypotensive episode.

## DETAILED DESCRIPTION OF THE INVENTION

Electrocardiography (ECG) is the process of recording the electrical activity of a patients heart over time using electrodes (sensors) placed on the patient's body. FIG. 1 is a general block diagram of one embodiment of the inventive system. FIG. 1 shows a patient (1) and 10 electrodes, or sensors (2-11) attached to the patient for transmitting ECG signals to the ECG device (12). The ECG device is preferably a high resolution ECG device having a processor (12a), software (12b) and storage (12c). The processor and software are capable of making calculations using data generated by measuring devices attached to patient that measure biological outputs such as processing and analyzing ECG or respiratory signals(15). The ECG device could also be connected to a personal computer (13) that includes a processor, software and storage (13a) capable of processing and analyzing the ECG signals in order to predict a hypotensive event. The system also includes storage (12a or 13a) for storing threshold alarm values that can be compared to processed data. The system also includes an alarm (14) which activates before a hypotensive event occurs and gives a warning signal to the caregivers when the system predicts an upcoming hypotensive event. The advance warning signal gives caregivers the opportunity to take corrective or remedial action with the patient before the hypotensive event occurs in order to avoid pathophysiological consequences and unfavorable outcome of patient after hypotensive event. The system also has the ability to receive other signals from other devices that generate data of physiological measurements that can be used to calculate hypotension prediction specific biomarkers. (15).

As will be described in detail hereinafter, systems and methods that predict potential acute hypotensive episodes in patients are presented. The systems and methods predict the potential acute hypotensive episodes in an automated manner without human interference. A rapid, accurate, sensitive and specific prediction of the potential acute hypotensive episodes may provide adequate time to diagnose the cause of the potential acute hypotensive episodes in the patients. Therefore, the prediction of the acute hypotensive episodes may improve possibilities of determination of the kind of intervention or treatment required to prevent the patients from the potential acute hypotensive episodes. In one embodiment, the systems and methods predict the potential acute hypotensive episodes in patients who are admitted in intensive care units (ICUs).

Referring to FIG. 2, which is a diagrammatic illustration of the architecture of the ECG biomarkers processing—subsystem referred to in FIG. 1.

The processing of the ECG signal to derive the prognostic biomarkers V[dsk(JT,QRS)] and J[dsk(JT, QRS),JT] works as follows. ECG signals are received via sensors attached to a patient. The ECG signals from the sensors are preferably synchronous on a number of channels, preferably 10 to 12 channels, and the sampling frequency is not less than 500 Hz. This allows for continuous registration of the ECG signals with needed temporal resolution.

The ECG signal is processed for calculation of RR′n, JT′n and QRS′n intervals for use in data arrays for each cardio cycle (n) measured. For these calculations, RRn′ is the duration of ECG RR interval meaning the time between 2 R peaks in milliseconds (ms). This interval is used as a time stamp (marker) for all calculations used during processing and also used for the synchronization of ECG and blood pressure data. JTn′ is the duration of the ECG JT interval meaning the interval from the junction point J (at the end of the QRS interval) until the end of the T wave in ms. QRS′n is the duration of the ECG QRS complex interval in ms.

Normalization of the JTn and QRSn data for each cardio cycle (n) to interval [0,1] is also performed using the following formula:

\({{JT} = \frac{{JT}^{\prime} - {JT}_{\min}}{{JT}_{\max} - {JT}_{\min}}},{{{where}\mspace{14mu} {JT}_{{mi}n}} = {140\mspace{14mu} {ms}}},{{JT}_{\max} = {40\mspace{14mu} {ms}}}\)

QRSn′ is the duration interval of ECG QRS complex in ms. n=(0,1,2, etc.) is the number of cardio cycles measured.

\({{QRS} = \frac{{QRS}^{\prime} - {QRS}_{\min}}{{QRS}_{\max} - {QRS}_{\min}}},{{{where}\mspace{14mu} {QRS}_{{mi}n}} = {40\mspace{14mu} {ms}}},{{QRS}_{\max} = {150\mspace{14mu} {ms}}}\)

Processing then occurs for formation of matrixes An for every cardio cycle n. A series of second order matrixes is constructed as follows:

\(A_{n}:=\begin{bmatrix}
{JT}_{n} & {{JT}_{n - 1} - {QRS}_{n - 1}} \\
{{JT}_{n + 1} - {QRS}_{n + 1}} & {QRS}_{n}
\end{bmatrix}\)

again, where n is the number of cardiocycles.

Calculation of dsk (JTn,QRSn) for every cardio cycle n is performed. Calculations of mathematical characteristics: difference of matrix An:dfrAn:=JTn−QRSn, co-diagonal product of matrix An: cdp An:=(JTn−1−QRSn−1)·(JTn+1−QRSn+1). Discriminant is calculated as follows: dsk(JTn,QRSn)=dsk An=(dfrAn)2+4cdp An.

Calculation of biomarkers J (dsk(JTn,QRSn)JT) and V (dsk(JTn,QRSn)) for 20 cardio cycles is performed as follows. The slope of linear dependence between dsk(JTn,QRSn) and JTn for each 20 cardio cycles results in J(dsk(JT,QRS),JT); and the ratio between the standard deviation and the mean of dsk(JTn,QRSn) in each 20 cardio cycles of dsk(JTn,QRSn) results in V[dsk(JT,QRS)].

Processing of J(dsk(QRS,JT)JT) and V(dsk(QRS,JT)) data series is done in order to predict hypotensive events. One embodiment of the invention uses the following algorithm of J(dsk(QRS,JT)) and V(dsk(QRS,JT)) data processing for prediction of hypotension events as shown in FIG. 3. The preferred algorithm uses the following steps:

Input data of J(dsk(QRS,JT)) and V(dsk(QRS,JT)) pairs reading and forming of the data array A{ti, 1 . . . N}. Data array A{ti, 1 . . . N} is formed from pairs of J(dsk(QRS,JT)JT) and V(dsk(QRS,JT)) data points received within a set time interval (preferably 15 min). Approximate number of points of data array N is ˜45 (˜3 points per minute). Data are updated periodically every 5 minutes by forming new data array A{ti, 1 . . . N}.

Formation of J(dsk(QRS,JT)) and V(dsk(QRS,JT)) data points distribution field array and calculation of density of J(dsk(QRS,JT)) and V(dsk(QRS,JT)) data points. Pairs of J(dsk(QRS,JT)JT) and V(dsk(QRS,JT)) points are plotted in field J(y—axis) vs V(x—axis). The field area is limited from min V=−0.5 to max V=5 in x axis. Field area is limited from min J=−4 to max J=4 in y axis. Limited area is segmented by steps ΔV=0.25 in x axis and Δs=0.2 in y axis. Finally, the two dimensional (2D) array of data points distribution density—D{ti, 1 . . . n, 1 . . . m} is calculated. (FIGS. 5-13). Here n is the number of discrete segments in x axis and m is the number of discrete segments in y axis.

Next, contour plot is calculated on density D{ti, 1:n, 1:m} on set threshold level=0.29*max(D{ti, 1 . . . n, 1 . . . m}). The contour plot also can be calculated from the density function D{ti, 1:n, 1:m} using different threshold values, e.g. level+0.29 below the maximal value 1.0 of maxD or other levels.

Calculation of contour Area(ti,), centroids coordinates Xc(ti) and Yc(ti) and maximum value of density function Dmax(ti) and Dmax_NORM(ti). These parameters are calculated during each cycle of data processing:


- - Area of the contour is Area(t_(i)). The sum value of all areas is
    calculated if there are only a few contours found. An example of
    graphing Area verses time can be seen in FIG. 15.
  - The coordinates of contour center of mass (centroids) Xc(t_(i)) and
    Yc(t_(i)). The centroids are calculated for the contour having
    maximal area, if there are only a few contours found.
  - Maximum value of density function D_(max)(t_(i))=max (D{t_(i), 1:n,
    1:m}) and normalized value of maximum density
    D_(max\_NORM)(t_(i))=max (D{t_(i), 1:n, 1:m})/sum (D{t_(i), 1:n,
    1:m}).

Accumulating data within a set time interval T by updating them by data period Δt. Storing reference set of data {D{t0, 1:n, 1:m}; Area(t0); Xc(t0),Yc(t0); Dmax(t0); Dmax_NORM(t0)} that corresponds the initial stable conditions. Tracking and visualizing centroids within set time interval T by updating data periodically also occurs. An example of graphing Dmax_NORM verses time can be seen in FIG. 16.

Calculation of cross-correlation function and correlation coefficient between current density D{ti, 1 . . . n, 1 . . . m} and stored density D{t0, 1 . . . n, 1 . . . m} occurs. Calculation is performed of 2D cross-correlation function cDij and 2D correlation coefficient rDij between current D{ti, 1 . . . n, 1 . . . m} and stored reference value of density distribution D{t0, 1 . . . n, 1 . . . m}. Determination of peak coordinates xpeak_C_Dij and ypeak_C_Dij of cross-correlation function cDij. Calculation of 2D auto-correlation cDii function for stored value of density distribution D{t0, 1 . . . n, 1 . . . m}. Determination reference peak coordinates xpeak_0 and ypeak_0 of cross-correlation function cDii. An example of graphing rDij verses time can be seen in FIG. 17.

Calculation of Euclidean distances ΔE1 between current centroids Xc(ti),Yc(ti) and stored reference centroid values Xc(t0),Yc(t0). An example of graphing ΔE1 verses time can be seen in FIG. 18.

Calculation of Euclidean distances ΔE2 between current set of multiple factors at time moment ti and stored set of reference multiple factors corresponding to time moment t0. Set of multiple factors consists of:


- - centroids Xc(t_(i)), Yc(t_(i))
  - Area(t_(i))

normalized maximum density Dmax_NORM(ti). An example of graphing ΔE2 verses time can be seen in FIG. 19.

Calculation of Euclidean distances ΔE3 between parameters of autocorrelation and cross-correlation functions of density distributions current density D{ti, 1 . . . n, 1 . . . m} and stored density D{t0, 1 . . . n, 1 . . . m}. Calculation of Euclidean distances ΔE3 of peak coordinates shift xpeak_C_Dij and ypeak_C_Dij from reference peak coordinates xpeak_0 and ypeak_0. An example of graphing ΔE3 verses time can be seen in FIG. 21.

Calculation root mean square (RMS) between current density distribution D{1 . . . n, 1 . . . m} and stored reference value of density distribution D{t0, 1 . . . n, 1 . . . m}. An example of graphing RMS can be seen in FIG. 14.

Compare current values of monitored factors Dmax_NORM, Area, ΔE1, ΔE2, ΔE3, rDij or RMS versus time with critical threshold values, or alarm values. Forming of alarm signal predicting of the hypotension episode the cases when monitored factors meets, reaches or exceeds the critical threshold values or alarm values. For example, FIG. 14 shows a graph of RMS calculations in relative units verses time and the RMS(t) crossing the critical threshold of 0.7 at a time approximately 75 minutes on the x-axis.

FIG. 15 shows a graph of Area in relative units verses time with the threshold number equal to 0.16 relative units. The graph shows the time of predicting the hypotensive event is at approximately 110 minutes as that is the time the measured units value reaches the threshold number. At this time, because the measured factor reaches the threshold value the processor can be programmed to generate an alarm to warn of the predicted upcoming hypotensive event.

FIG. 16 shows a graph of Dmax_NORM in relative units verses time with the threshold number equal to 0.35 relative units. The graph shows the time of predicting the hypotensive event is at approximately 110 minutes as that is the time the measured units reaches the threshold number. At this time, because the measured factor reaches the threshold value the processor can be programmed to generate an alarm to warn of the predicted upcoming hypotensive event.

FIG. 17 shows a graph of rDij in relative units verses time with the threshold number equal to 0.7 relative units. The graph shows the time of predicting the hypotensive event is at approximately 90 minutes as that is the time the measured units reaches the threshold number. At this time, because the measured factor reaches the threshold value the processor can be programmed to generate an alarm to warn of the predicted upcoming hypotensive event.

FIG. 18 shows a graph of ΔE1 in relative units verses time with the threshold number equal to 0.2 relative units. The graph shows the time of predicting the hypotensive event is at approximately 93 minutes as that is the time the measured units reaches the threshold number. At this time, because the measured factor reaches the threshold value the processor can be programmed to generate an alarm to warn of the predicted upcoming hypotensive event.

FIG. 19 shows a graph of AE2 in relative units verses time with the threshold number equal to 0.28 relative units. The graph shows the time of predicting the hypotensive event is at approximately 98 minutes as that is the time the measured units reaches the threshold number. At this time, because the measured factor reaches the threshold value the processor can be programmed to generate an alarm to warn of the predicted upcoming hypotensive event.

FIG. 20 shows a graph of AE3 in relative units verses time with the threshold number equal to 0.7 relative units. The graph shows the time of predicting the hypotensive event is at approximately 88 minutes as that is the time the measured units reaches the threshold number. At this time, because the measured factor reaches the threshold value the processor can be programmed to generate an alarm to warn of the predicted upcoming hypotensive event.

The invention contemplates one or more or various combinations of the monitored factors being used to determine when an alarm should be generated to warn of an upcoming hypotensive event. While single monitored factors can be used to trigger and alarm the sensitivity of different monitored factors can vary in clinical testing. Accordingly, other embodiments use a combination of more than one monitoring factor in an integrated alarm. The integrated alarm can be set to trigger in a variety of circumstances. For example, it can be triggered when more than one monitoring factors shows an alarm or it can be triggered when a majority of the monitored factors being monitored it triggered indicating and showing an alarm. In the preferred embodiment, all monitored factors are used to decide if an alarm should be triggered when a majority of the monitored factors cross their thresholds.

Affirmative prediction is indicated by comparing two 3D images—initial one peak image and other images with less height than the main peak and with other peaks which represent chaotic process. The 3D image representing the chaotic process reflects the patient's organism is approaching hypotensive event. When the patient is healthy the system measurements will generate images which will show a simple peak representative of a steady state. As the patient becomes less healthy, begins to depart from a steady state the system measurements will generate more chaotic images. The closer the patient gets to a hypertensive event the more and more chaotic the images become (as the system measurements move further from a steady state) which is indicative of a system when the organism as a non-linear complex dynamic system is unstable.

Euclidian distance can be one of the possible ways to monitor the difference between the initial 3D image of proposed biomarker and the next time generated images as the time gets closer to a hypotensive event. Correlation is another way to monitor such differences. Other image analysis methods can also be used, like RMS(t) function.

FIG. 21 is a Receiver Operation Characteristic (ROC) curve generated from cardiologic patients validating and confirming the reliability of the invention method and device. The inventive method and system (FIG. 1) has been prospectively validated on 60 patients of cardiological intensive care units of three independent cardiological clinics. Patients with and without hypotensive episodes were included into prospective clinical study. ROC analysis has been used for estimation of sensitivity, specificity and area under curve (AUC) of hypotension episode prediction system. FIG. 21 shows the ROC curve of the clinically validated system using the most reliable monitoring factor ΔE1. The ROC curve confirms that the inventive hypotension episode prediction method and apparatus predicthypotensive episodes with very high and clinically acceptable sensitivity at 85% and specificity at 92%. The Area Under the ROC Curve (AUC) is also high at 94%. Sensitivity, specificity and AUC values all confirm that invented system solves the problem of reliable prediction of hypotensive episodes and that it can be widely used in clinical practice

Although the invention has been described with reference to a particular arrangement of parts, features and the like, these are not intended to exhaust all possible arrangements or features, and indeed many other modifications and variations will be ascertainable to those of skill in the art.

While only certain features of the invention have been illustrated and described herein, many modifications and changes will occur to those skilled in the art. It is, therefore, to be understood that the appended claims are intended to cover all such modifications and changes as fall within the true spirit of the invention.

