# Background

In conformal radiotherapy, geometric margins are commonly used to account for intra-fractional target motion [1,2]. These margins inevitably lead to inclusion of healthy tissue in the treated volume. In intensity modulated radiotherapy, additional motion effects arise due to so called interplay effects [3-5]. Treatments are delivered in small partial doses that only result in adequate total dosage if they match as intended. In anatomy's eye view, target motion leads to relative displacement of partial dose depositions and therefore results in local over- and under-dosage.

In a pilot project at Gesellschaft für Schwerionenforschung (GSI) [6-9], approximately 400 patients have been treated with scanned carbon ion beams with the rasterscan system [10]. For raster scanning, the target volume is divided in slices corresponding to equal ion energies. Irradiations are performed slice-by-slice. The required particle energy is requested from the synchrotron for each slice. Within each slice, a narrow pencil beam is scanned on a virtual raster grid. To achieve the desired dose distribution, the number of particles is optimized for each raster position during treatment planning including biological effects [11-16]. The scanning progress is intensity controlled. The carbon ion pencil beam is directed to the next raster position by a magnetic deflection system as soon as the planned number of particles has been deposited. After all points within a slice have been irradiated, the beam is aborted and the next energy level is requested from the accelerator. To date, only patients with tumors that are not subject to intra-fractional motion have been treated [7,17-19]. For treatments with scanned particle beams, target motion would inevitably lead to local over- and under-dosage due to the relative lateral motion between pencil beam positions as well as possible motion induced changes in radiological depths.

To treat moving targets, while maintaining the conformity between target and treated volume as well as avoiding local over- and under-dosage, we are investigating and developing a system to adapt 3D pencil beam positions to actual target positions in real time. Initially, simulation studies were performed to investigate the potential of target tracking with a scanned ion beam [4,20]. In beam's eye view, lateral motion adaptation of pencil beam positions is feasible by applying offsets to the raster scanner settings. Real time energy adaptation to compensate changes in radiological depth with the synchrotron directly is not (yet) possible. Therefore online adaptation of particle ranges has to be performed with an additional, dedicated energy modulation system. One of the possibilities is to use a dedicated absorber wedge system [21].

Prototype systems for lateral as well as longitudinal target tracking with a scanned ion beam have been developed. Experimental results are presented to demonstrate the feasibility of target tracking with a scanned ion beam and to show the performance of the individual prototype tracking sub-systems.

# Methods

## Simulation Of Target Motion

Lateral target motion orthogonal to the beam direction was achieved with a three-axes positioning table. A radiographic film was mounted on the table as detector. The motion was sinusoidal with a period of ~10 s and amplitudes of ± 15 mm in horizontal as well as vertical direction. No external motion monitoring device was used, instead table motion was continuously measured with encoders. Target displacements were evaluated from encoder data and sent directly to the therapy control system (TCS) for beam adaptation during irradiations.

To simulate motion induced variations in particle range, different particle energies were requested from the synchrotron. In a first experiment, three different particle energies were requested from the accelerator repeatedly in fixed order. The energy modulation system was used to adapt the effective particle energy at isocenter to the middle energy. In a second experiment, six different particle energies were requested in mixed order to test the functionality of the system for variable and alternating energy modulations. The maximum difference in energy corresponded to a water equivalent range difference of 27 mm. Again, the energy modulation system was used to adapt the effective particle energy to a single range.

## 3D Online Motion Compensation

### Lateral Motion Compensation

The raster scanning process is controlled by the TCS. Beam position as well as delivered number of particles are monitored in intervals of ~150 μs and ~10 μs respectively. The standard TCS can adjust small deviations of the actual beam position via a fast feedback loop. Whenever the beam position has been measured, possible deviations are fed back to the control of the scanning magnets to correct the beam position to the nominal position. Typically, deviations are within ± 0.5 mm and corrected after each measurement cycle. The irradiation time for an individual raster point is typically in the order of 5–10 ms.

Several processes are running simultaneously in the TCS including monitoring of the beam intensity, the beam position, and the raster scanner magnet settings. The individual processes communicate via a control loop as well as shared memory. For motion compensation, adaptation of lateral pencil beam positions was implemented by dynamically changing the nominal values of the beam positions in shared memory. As soon as the nominal values have been changed, the feedback loop adjusts the beam position accordingly. A dedicated, additional process running on the TCS receives displacement vectors and then changes the nominal beam positions in shared memory accordingly. In order to avoid hardware changes within the TCS for the prototype setup, a standard network connection (100 Hz) was used to transmit displacement vectors to the TCS. The actual displacement vector is added to the stationary nominal raster point position to compute the new, dynamic nominal position.

### Longitudinal Motion Compensation

To perform motion compensation in longitudinal direction, the energy of individual pencil beams has to be adjusted in quasi real time. Because fast active energy variation with the accelerator is not possible, a passive energy modulation system was developed and installed between beam exit window and isocenter [21]. The system consists of two opposing lucite wedge absorbers that are mounted on linear motor drives orthogonal to the beam direction (figure 1). By moving the wedges apart (together) with the linear motors, the thickness of absorber material in the beam path can be decreased (increased) to adapt the effective beam range at isocenter fast and continuously. The system has an active compensation area of 120 × 150 mm2. The absorber wedges were designed to provide homogeneous range adaptation within the active area by adequate overlap. If the treatment field exceeds the dimension of the active area in the horizontal direction of wedge motion both wedges can be moved synchronously to provide adequate range adaptation. The total wedge thickness of the prototype system corresponds to a maximum water equivalent range variation of ± 49.4 mm which should exceed the maximum clinically required range adaptation.

## Measurement And Analysis Of Dose Distributions

Different detectors were used to measure dose distributions: planar radiographic films for lateral 2D dose distributions and a range telescope for longitudinal 1D depth dose distributions [22].

Radiographic films (Kodak X-Omat V) were developed with a Kodak M35 processing machine. The films were digitalized with a Kodak LS75 laser densitometer and the FIPS Plus software for film dosimetry (PTW Freiburg) with a spatial resolution of 1 mm. Based on the film responses, absorbed doses were calculated according to Bathelt et al [23] and Spielberger at al [24]. Simple treatment plans were optimized to deliver homogeneous, quadratic dose distributions as well as line patterns. Geometric properties of motion compensation were assessed from the line patterns. For quadratic fields, the homogeneity index H was computed to compare dose distributions quantitatively:

\(H = 1 - \frac{1}{\overline{D}}\sqrt{\frac{\sum\limits_{i}{(D_{i} - \overline{D})}^{2}}{N - 1}}\)

with Di dose to each individual pixel, N number of pixels within the target area, and \(\overline{D}\)  mean dose within the target area.

The range telescope was used to measure depth dose distributions, so called Bragg peaks. The telescope consists of two parallel plate ionization chambers in front of and behind a water tank of variable thickness [22,25,26]. During the measurements, the thickness of the water tank was increased in steps of 50 μm.

# Results

## Lateral Motion Compensation

Figure 2 shows film responses for a quadratic, homogeneous field. Under motion, marked local over- as well as under-dosage are apparent and relevant dose is deposited outside of the target area. Lateral motion compensation restored the dose distribution on the moving film. In comparison to the reference dose distribution, only small differences within the irradiated area are visible. Homogeneity indices were 0.969, 0.655, and 0.963 for the dose distributions measured under stationary, moving, and motion compensated conditions respectively.

Film responses for line patterns are shown in figure 3a. In contrast to the regular, parallel lines on the stationary film, heavily distorted patterns were measured with the moving film. Motion compensation successfully restored the line patterns. A small residual motion artifact is present in the third line from top which was attributed to a sporadic communication delay between motion monitoring and compensation due to communication via a standard network connection. Figure 3b presents line profiles of the film responses for stationary and motion compensated measurements. Positional differences of the lines were on average 0.2 ± 0.2 mm. A maximum deviation of 1.6 mm was observed in the region of the residual motion artifact (figure 3b; S5). Differences in relative dose between the two experiments are within the precision of film measurements.

## Longitudinal Motion Compensation

The precision of longitudinal motion compensation is presented in figure 4. During irradiation, three different energy levels were adapted to the middle energy using the energy modulation system. The inlay shows that the difference to an individually measured depth dose distribution at the mean energy is ~0.1 mm.

The performance of energy adaptation for 6 different energy levels requested in random order from the accelerator is shown in figure 5. The energy modulation system successfully restored a single, effective particle energy at isocenter. Fluctuations around the reference depth dose distribution of ~2.5% on average (normalized to the Bragg peak) are mainly attributed to residual calibration uncertainties of the energy modulation system.

# Discussion

The results of our feasibility study demonstrate that motion compensation with scanned particle beams is feasible with high precision. Lateral as well as longitudinal compensation were successfully performed during irradiations. In a next step, both motion compensation sub-systems have to be integrated in the therapy control system. Especially replacing standard network connections to transmit compensation parameters should improve the reliability of the system. Furthermore, hardware improvements of the energy modulation system for longitudinal range compensation should be investigated, and implementation of motion monitoring has to be developed.

Re-design of the wedge system for fast longitudinal motion compensation is advisable since the thickness of the wedges can most likely be reduced to the compensation range required for patient treatments in order to reduce lateral scattering as well as fragmentation of the primary particle beam [27-29]. Furthermore, the active area of the wedge system (120 × 150 mm2) does currently not match the treatment area of the scanning system (200 × 200 mm2). The wedge size thus has to be increased at least in vertical direction. In contrast, the horizontal dimension of the active area does not necessarily have to match the scan area. If the center of mass of the wedges follows the left-right motion of the ion beam during raster scanning, an active area that is smaller than the maximum treatment area is sufficient. However, less wedge motion and therefore reduced system performance is required if the active area is sufficiently large to cover the complete scanning area. Detailed requirements on the compensation speed have to be derived from simulation studies, for example based on 4D computed tomography data [30-32].

Another problem of motion tracking that has not yet been solved adequately is precise monitoring of target motion. To date, several different methods have been reported in the literature. Currently, the most promising technique seems to be fluoroscopic motion detection because target motion is imaged directly [33-38]. Other techniques that monitor external surface motion have to be evaluated regarding the accuracy to derive target positions [39-46]. Since the particle range and thus the Bragg peak position are influenced by target motion and currently no motion monitoring system exists to determine changes in water-equivalent range a link to 4D treatment planning is required [47,48]. Motion states from 4DCT which are used to determine range changes could be detected by motion monitoring. Compensation vectors are then calculated during treatment planning and applied according to detected motion states. In case of motion irregularities or unknown motion states the treatment can be paused until the patient is back to normal breathing.

# Conclusion

The results of our study demonstrate the high precision that is technically feasible for motion tracking with scanned particle beams. Lateral motion compensation restored homogeneous dose distributions delivered to moving targets. Differences in dose uniformity between irradiation of a stationary radiographic film and a moving film using motion compensation were below 1%. Longitudinal compensation precision was well below 1 mm.

# Competing Interests

SOG and ER are now employed by Siemens Healthcare. Research was performed while both were employed by GSI.

# Authors' Contributions

All authors contributed to the design of the prototype system and the conceptual design of the study. Furthermore, SOG performed measurements, analyzed data, and drafted the manuscript. CB and ER supported measurements, analyzed data, and revised the manuscript. TH and GK improved the conceptual design and revised the manuscript. All authors read and approved the final manuscript.

