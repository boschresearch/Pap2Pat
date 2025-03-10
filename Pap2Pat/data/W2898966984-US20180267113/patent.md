# DESCRIPTION

## FIELD OF THE INVENTION

This invention relates to magnetoresistive (MR) sensors.

## BACKGROUND

Magnetoresistance is a change in electrical resistance that depends on magnetic field. The presence of an object of interest (e.g., a magnetic particle) can be sensed by the change in resistance of the MR sensor. Biological assays can be constructed by making magnetic particles bind to MR sensors under biologically specific circumstances. For example, if the MR sensors and magnetic particles are coated with an antigen and a corresponding antibody, respectively or vice versa, then binding of antibody to antigen can be detected via the MR effect.

In biological applications, it is often desired to employ a large array of MR sensors in order to conduct large-scale assays. In such cases, system performance is often limited by electrical noise, and noise mitigation is also of more general interest for all applications of MR sensors. Accordingly, it would be an advance in the art to mitigate noise in MR sensors, especially in connection with arrays of MR sensors.

## SUMMARY

The present work has two aspects, which can be practiced individually or in combination. The first aspect relates to use of correlated double sampling (CDS) for MR sensors combined with modulation of an applied magnetic field. The second aspect relates to MR sensor arrays having input and output multiplexing and demultiplexing for row and column line selection, in combination with a per-sensor switch to prevent noise accumulation from idle MR sensors.

This work provides correlated double sampling in connection with MR sensors. The MR sensor output is sampled at two closely spaced times. The first sample is MR signal+baseline+noise, and the second sample is baseline+noise only. The difference between the first and second signals will have baseline cancellation and significant noise suppression because of the relatively low noise frequencies involved and because both signals are provided by the same circuitry. Further elaborations of this approach (e.g., as described below) can be used to provide low-noise temperature correction for MR sensors, and suitable architectures for low-noise MR sensor arrays.

More specifically an MR sensor array can include an analog multiplexer (Mux) and demultiplexer (deMux) to provide column line and row line selectors (or vice versa). Introduction of the Mux and the deMux dramatically reduces the number of input/output pads of the microarray chip, which in turn greatly simplifies the interface with sensor readout circuits. Adopting a two dimensional matrix structure allows sensor elements to be individually accessible in time and also improves power efficiency of the array.

Each magnetoresistive sensor in an array can have its own on/off switch. Using such switches, only sensors in selected pixels are accessible at the readout time, while the other sensors are disconnected from the row and/or column lines. This advantageously prevents noise from unselected sensors from being transmitted to the input of readout circuits. Another advantage of this methodology is to preserve the signal bandwidth of the readout channel by disconnecting unread sensors from the channel. Without it, the signal bandwidth is narrowed due to the unread sensors connected to the channel. The switches can be metal-oxide-semiconductor devices or other semiconductor devices such as switching diodes. The number of switching devices per sensor element can be one or more.

This can provide a broader scalability of magnetoresistive sensor arrays which can accommodate more than 1,000 sensors per array. In medical applications, demand for large-scale sensor arrays accommodating numerous types of analytes such as human proteins is increasing. This work provides architectures for large-scale magnetoresistive sensors array without disadvantages in channel bandwidth and noise performance. Correlated double sampling and temperature correction techniques can be used to build temperature insensitive and high throughput data acquisition systems using magnetoresistive sensors, although the techniques are suitable for arrays with less than 1000 sensors as well.

These approaches are broadly applicable, e.g., in both biological and non-biological settings. Applications include medical, mobile and industrial applications of magnetoresistive sensors. Exemplary medical applications include diagnosis and/or prognosis of a disease and drug discovery targeting a specific disease. For mobile and industrial applications, quantification of a minute change of the magnetic field and/or magnetically actuated reaction can be provided.

Significant advantages are provided.

1. Correlated double sampling and temperature correction methods can provide ultra-high throughput in data acquisition in a large-scale sensor array with large dynamic range and high precision. For example, the readout speed per channel can be 100× faster with the CDS approach than with prior approaches (e.g., lock-in double modulation techniques as described below).

2. The MR sensor array architectures can provide constant channel bandwidth and fixed noise performance regardless of the number of sensors in the array.

Several variations are possible. The biasing of the magnetoresistive sensors can be provided by a bias voltage or by a bias current. A modulated magnetic field of square, sinusoidal or return-to-zero waveform are suitable for CDS techniques. More generally, any modulation waveform which includes a zero magnetic field portion of the waveform can also be utilized.

## DETAILED DESCRIPTION

### A) Introduction

Molecular diagnostics is used extensively today by the medical community for disease diagnosis, prognosis, therapy monitoring and drug discovery. As researchers begin to understand the numerous biomarkers associated with complex diseases such as cancers, new sensing technologies emerge to effectively detect and measure the biomarkers of interest in patients' samples. The demand for high sensitivity, broad linear dynamic range, and large multiplexing capability requires high performance sensing technologies. Conventional optical techniques, which rely on a fluorescent tag to label biomarkers of interest, have a limited dynamic range due to the optical background noise and also inherently have relatively low sensitivity. By replacing the fluorescent tag with a magnetic nanoparticle and the bulky optics with a magnetoresistive (MR) sensor, researchers have achieved highly sensitive detection with a broad linear dynamic range.

FIG. 1A schematically shows a magnetic particle 106 in proximity to a MR sensor 102. The presence of the magnetic field from magnetic particle 106 at MR sensor 102 changes the electrical resistance of MR sensor 102. FIGS. 1B-D show images of exemplary MR sensors. FIG. 1B is an image of a 64 element giant magnetoresistive (GMR) spin valve sensor array. FIG. 1C is a magnified view of a single sensor in the array of FIG. 1B. Multiple GMR sensor strips form the GMR sensor. FIG. 1D is an image showing super paramagnetic nanoparticles on the surface of the GMR sensor.

The MR biosensor typically includes elaborately engineered thin film stacks of magnetic and non-magnetic materials. Multiple narrow and long strips of the thin film stacks form a MR sensor (FIGS. 1B-C). It senses the minute change of the induced magnetic field by the number of magnetic nanoparticles adjacent to it in the circumstance of the external magnetic field (FIG. 1D). The number of magnetic nanoparticles is proportional to the degree of the reaction between the antibodies on the sensor surface and the analytes. If the antibodies are paired with the target analytes, the resistance of the MR sensor changes.

FIGS. 2A-B show examples of specific biomarker detection by magneto-resistive sensors. FIG. 2A is a standard binding curve (Signal vs. concentration of CEA (Carcinoembryonic antigen, which is a cancer biomarker)). FIG. 2B shows transient binding curves (Signal vs. time) of three biomarkers. BSA and epoxy is a biological control and a reference, respectively. A minute signal of interest is distinguishable from the control.

Since the MR sensor has both magnetic and resistive characteristics, it generates noises such as 1/f noise, thermal noise, Barkhausen noise and so on. Barkhausen noise can be eliminated by utilizing shape anisotropy of the film strips and/or applying strong magnetic field to the sensor at the preconditioning step. If Barkhausen noise is excluded, 1/f noise dominates the total noise from the sensor at the low frequency range and thermal noise at the frequency range over the corner frequency of 1/f noise. FIG. 3A shows voltage noise measured from an exemplary MR sensor at fixed current. Input voltage noise of the sensor is 4.76 nVrms/√Hz, which is close to the theoretical thermal noise floor 4kBTR. The 1/f noise corner frequency is at 285 Hz.

The signal of interest is commonly located at low frequency range, so 1/f noise degrades the limit of signal detection. Not only 1/f noise from the sensor, but 1/f noise caused by data acquiring electronics is also problematic. FIG. 3B shows an example of the noise profile of a commercial operational amplifier (OPA656 from Texas Instruments, Inc.), which shows the dominant 1/f noise at lower frequency range. 1/f noise is noise that has a power spectral density proportional to 1/f. The corner is where the 1/f noise intersects the thermal noise.

In order to avoid the degradation of signal-to-noise ratio by 1/f noise of the data acquisition electronics, the frequency division multiplexing (FDM) has been used to measure the change of MR ratio of the sensors for the biological reactions between analytes and antibodies. However, as the size of the sensor array increases, the non-ideal phenomena in FDM such as harmonic distortion become more prominent. Furthermore, the data acquisition time for an entire sensor array will dramatically increase so that using FDM in a large-scale sensor array is unappealing.

### B) General Principles

FIG. 1A shows an exemplary embodiment of the invention. This embodiment is apparatus for magnetic field sensing where the apparatus includes:

1) a magnetic field source 104 configured to provide a modulated magnetic field, where the modulated magnetic field has intervals of zero magnetic field intensity and/or zero crossings of magnetic field intensity;

2) one or more magnetoresistive sensors 102 having electrical resistances that depend on magnetic field intensity at locations of the magnetoresistive sensors, where the magnetoresistive sensors are disposed in the modulated magnetic field; and

3) electrical circuitry 110 configured to provide electrical signals that depend on electrical resistances of the magnetoresistive sensors.

The electrical circuitry is further configured to sample the electrical signals synchronously with the modulated magnetic field. More specifically, the electrical signals are sampled during the intervals of zero magnetic field intensity of the modulated magnetic field and/or at the zero crossings of magnetic field intensity of the modulated magnetic field to provide reference sampled data. The electrical signals are sampled at times the magnetic field intensity of the modulated magnetic field is non-zero to provide measurement sampled data. The apparatus is configured to provide a difference between the measurement sampled data and the reference sampled data as a measurement output.

The net effect of this approach for handling the signals from the MR sensor is to cancel the baseline signal in the measurement output and also to significantly reduce low frequency noise in the measurement output. Here the ‘baseline’ signal is the signal that is provided by a magnetoresistive sensor in the absence of a magnetic field. Note that magnetoresistance is a change in resistance caused by an applied magnetic field. For example, the resistance may change from R to R+ΔR due to an applied magnetic field, and in this example R is the baseline and ΔR is the magnetoresistive effect. If a current I flows through the sensor, the baseline voltage signal is IR and the magnetoresistive voltage signal is I ΔR. In practice, the total signal (e.g., I(R+ΔR)) is measured and then processed to determine the magnetoresistive part of the total signal. It is convenient to refer to these total signals from magnetoresistive sensors as ‘measurement signals’ having corresponding ‘measurement sampled data’, as above.

Practice of the invention does not depend critically on how the difference between the measurement sampled data and the reference sampled data is provided. For example this difference can be provided by an analog difference circuit or by a digital difference circuit. Practice of the invention also does not depend critically on how the modulated magnetic field is provided to the MR sensors. However, it is preferred for this field to be provided in a way that is suitable for integration with MR sensor arrays. For example, the modulated magnetic field can be provided by field wires or integrated circuit traces disposed beneath the array of MR sensor elements.

The magnetic field modulation is preferably periodic. Suitable magnetic field modulation wave forms include, but are not limited to: sinusoids, square waves, and return to zero (RZ) waveforms. Any magnetic field modulation wave form having zero crossings or intervals of zero intensity can be employed. Here a square wave (e.g., 1) of FIG. 4B) is defined as periodic modulation between zero intensity and one other non-zero magnetic field intensity, where the field intensity is held constant except when switching between the two states, and the switching pattern is 0+0+0+0+ (or 0−0−0−0−) etc. A return-to-zero (RZ) modulation (e.g., 3) of FIG. 4B) is defined as periodic modulation between zero intensity and two other non-zero magnetic field intensities. Here the two non-zero magnetic field intensities have equal magnitude and opposite polarity. The field intensity is held constant except when switching between the three states, and the switching pattern is 0+0−0+0− (or 0−0+0−0+) etc.

As described in greater detail below, the relation between sampling rate of the electrical signals and modulation frequency of the magnetic field depends on details of the CDS methods being employed. Common options are the modulation frequency of the modulated magnetic field being 1/2 or 1/4 of the sampling rate of the electrical signals.

In preferred embodiments, the apparatus further includes one or more baseline suppressors configured to reduce the direct current (DC) baseline of the magnetoresistive sensors. This can be helpful for preventing saturation when amplifying weak MR signals.

Temperature compensation is an important consideration when using MR sensors. One known approach to MR sensor temperature compensation relies on using the baseline signal to temperature correct the MR signal. Since CDS removes the baseline signal from the measurement output, special measures are needed to combine CDS and temperature compensation.

In an embodiment, the apparatus further includes bias circuitry 108 on FIG. 1A to apply an electrical bias to the magnetoresistive sensors 102, where the electrical bias is modulated synchronously with the modulated magnetic field between a first bias and a second bias.

The electrical signals are sampled during the intervals of zero magnetic field intensity of the modulated magnetic field and/or at the zero crossings of magnetic field intensity of the modulated magnetic field and when the electrical bias is the first bias to provide first sampled data.

The electrical signals are sampled during the intervals of zero magnetic field intensity of the modulated magnetic field and/or at the zero crossings of magnetic field intensity of the modulated magnetic field and when the electrical bias is the second bias to provide second sampled data.

The apparatus is further configured to provide a difference between the first sampled data and the second sampled data as a baseline output. The measurement sampled data is all sampled at times having the same electrical bias.

The apparatus is further configured to automatically determine a temperature-corrected measurement from the measurement output and the baseline output, and to provide the temperature-corrected measurement as a temperature corrected output.

The first and second sampled data is sampled at two different electrical bias values and at zero magnetic field in order to provide a baseline signal for temperature correction. Details of this are given in section D below.

The magnetoresistive sensors can be configured to be disposed in a magnetic field to be quantified that is superposed with the modulated magnetic field. For example, the magnetic field to be quantified can be generated by magnetic particles 106 on FIG. 1A captured on or near surfaces of the magnetoresistive sensors. Suitable magnetic particles include but are not limited to: superparamagnetic particles, anti ferromagnetic particles, and ferromagnetic particles with near-zero remanence. The magnetic particles can be conjugated to analytes of interest, and the apparatus can be configured to quantify the analytes (e.g., in a biological assay).

The second aspect of this work relates to low noise MR sensor array architectures. An exemplary embodiment is apparatus for magnetic field sensing, where the apparatus includes:

1) a 2-D array of magnetoresistive sensors (1002 on FIG. 10);

2) an analog demultiplexer (1004 on FIG. 10) for selectively providing excitation to one of the rows or columns of the 2-D array; and

3) an analog multiplexer (1006 on FIG. 10) for selectively reading signals out from one of the rows or columns of the 2-D array.

The demultiplexer and multiplexer function as row and column selectors respectively, or vice versa. Each magnetoresistive sensor (MR on FIG. 10) of the 2-D array has an associated sensor switch (S on FIG. 10). The sensor switches are configured to disable all sensors being read out by the multiplexer except the sensor being driven by the demultiplexer (e.g., FIG. 11).

### C) Correlated Double Sampling (CDS)

FIGS. 4A-B show operation principle of correlated double sampling for magnetoresistive sensors. FIG. 4A is a conceptual diagram. On/Off timing for electrical switches are shown on the right box as {circle around (1)} and {circle around (2)}. They are non-overlapping. Note that switches inside the dotted box are physical switches in the electrical circuitry, while the switches to the right of the magnetic excitation block are not physical elements. Instead, they schematically represent the modulation of the magnetic field. FIG. 4B shows examples of suitable magnetic field modulation wave forms: 1) square, 2) sinusoidal and 3) return-to-zero (RZ). {circle around (1)} when H field=0 and {circle around (2)} when H field in non-zero.

In general terms, CDS is a known circuit design technique in order to eliminate background noise such as non-ideal offsets and 1/f noise from measured signals of interest. The basic idea is to first sample and store background noise only in the form of electronic charges by capacitors. Then signal+background is sampled and stored again right after the former capturing event. A difference circuit subtracts one from the other, and thereby only the signal of interest remains. The order of sampling events can be swapped. There are many examples of utilization of the CDS technique. A common application is the integrated image sensors widely used in cameras. Another research group has proposed the CDS technique in connection with a capacitive position sensing system.

In this work we provide a novel CDS technique to effectively suppress the background noise and offsets of the magnetoresistive sensors (FIG. 4A). It utilizes a modulated magnetic field as a signal excitation source. A modulated magnetic field of square, sinusoidal or return-to-zero waveforms are applicable to our CDS techniques (FIG. 4B). Other types of waveform which passes zero magnetic field point can also be utilized. A conventional MR sensor and the sandwich assay technique can be utilized as a sensor and its biological interface. Since MR sensors respond to the in-plane magnetic fields on their magnetic free layers, the presence of the modulated field changes the magnetoresistance of the sensors. If there is zero magnetic field, a sensor under test produces only baseline signal and noise. On the other hand, it will produce finite magnetoresistive signal as well as baseline signal and noises in the presence of non-zero magnetic field. Provided that temporal difference between two measurements ({circle around (1)} and {circle around (2)}) is sufficiently small, the 1/f noise and offset from sensors and electronics at {circle around (1)} and {circle around (2)} become highly correlated and thereby the subtraction between two measured data will remove a large portion of 1/f noise and offset. Therefore a signal having reduced 1/f noise and reduced offset can be obtained using the present CDS technique.

D) Correlated Double Sampling with Temperature Correction

Because the MR sensor has both resisitve and magnetoresistive properties, it has not only the temperature coefficient of resistance (TCR) but also the temperature coefficient of magnetoresistance (TCMR). Because the MR signal obtained by the present CDS technique is a complex function of TCR and TCMR and it is sensitive to the temperature change, a special temperature correction treatment is required. In this work, we show how to provide temperature correction for the CDS MR sensor technique.

FIG. 5 shows the overall functional diagram for the data acquisition system with CDS and TC techniques. This signal path is utilized for the measurement of both the CDS signal and the baseline signal.

In order to minimize the temperature fluctuation effect on the sensor in CDS, the system with a proper temperature correction (TC) technique is provided (e.g., FIG. 5). In order to increase the gain of the signal path without saturation, the baseline suppressor is introduced. The suppressor can be any circuit having the effect of reducing the baseline from the MR sensors. For example, the suppressor can be a current source, current-mode digital to analog converter, or a R−2R ladder to increase the tolerance against the process variation of the MR sensor. The output of the baseline suppressor subtracted from the output of MR sensor under no magnetic field is the net baseline signal comparable to the magnitude of the MR signal. The suppressed baseline and MR signal are amplified and provided to the correlated double sampler. The processed signal can be digitized and filtered in the digital domain. Finally, a novel temperature correction algorithm eliminates temperature drift noise from the measured data which can be realized in the software domain.

The baseline signal is used to extract the degree of the temperature drift at the moment, and the extracted information of temperature drift is utilized to compensate the measured MR signal to make it temperature insensitive. Because the CDS operation for obtaining MR signal (VMR) also removes the baseline signal from measured signal, a unique method to measure only the baseline signal (VBASE) is necessary. In order to improve the performance of the temperature correction, VBASE should be 1/f noise and offset-reduced. It employs an additional CDS phase during the operation.

FIG. 6A shows correlated double sampling technique for 1/f noise and offset-reduced baseline signal. FIG. 6B shows correlated double sampling technique for 1/f noise and offset-reduced MR signal detection. In FIG. 6A, the electrical bias voltage into the MR sensor is given pulsed form. In FIG. 6B, the pulsed external magnetic field (schematically shown by two coil symbols around R) is provided to the sensor, thereby changing the resistance of the MR sensor. R and Rc are the MR sensor and the baseline suppressing resistor, respectively. Dots on the timing graph indicate the moments to be sampled at the correlated double sampler.

Here we provide the novel correlated double sampling techniques to measure both the 1/f noise and offset-reduced baseline signal and the MR signal (FIGS. 6A-B). The virtues of this approach include: 1) the simplicity in the circuit design because the correlated double sampling in FIGS. 6A-B shares most of the signal path; and 2) the magnetic field modulation is utilized in the correlated double sampling. To measure the 1/f noise and offset-reduced baseline signal, the bias voltage exciting the MR sensor R gets a pulsed form. It changes from V to V+ΔV and going back to V (FIG. 6A). CDS operation is done by sampling the baseline signal with respect to these two levels. The path output VBASE is

\(V_{BASE} = {{\left( {\left( {\frac{V + {\Delta \; V}}{R} + \frac{- V}{R_{C}}} \right) - \left( {\frac{V}{R} + \frac{- V}{R_{C}}} \right)} \right)G_{PATH}} = {\frac{\Delta \; V}{R}G_{PATH}}}\)
\(R = {\frac{\Delta \; V}{V_{BASE}}G_{PATH}}\)

where GPATH is the transimpedance gain of the analog circuits. Since VBASE results from the CDS operation, it is 1/f noise and offset-reduced. So is R.

For measuring the MR signal, the pulsed external magnetic field from 0 to ΔH is applied to the MR sensor (FIG. 6B). Its resistance corresponding to the field changes from R to R+ΔR. The MR signal in voltage, VMR, is

\(V_{MR} = {{\left( {\left( {\frac{V}{R + {\Delta \; R}} + \frac{- V}{R_{C}}} \right) - \left( {\frac{V}{R}\; + \frac{- V}{R_{C}}} \right)} \right)G_{PATH}} \approx {{- \frac{\Delta \; R}{R^{2}}}G_{PATH}V}}\)
\(\frac{\Delta \; R}{R^{2}} \approx {- \frac{V_{MR}}{G_{PATH}V}}\)

Like the former case,

\(\frac{\Delta \; R}{R^{2}}\)

is 1/f noise and offset-reduced.

Because the sensors are resistive, the expression of the measured output voltage depends on the type of excitation methods: voltage and current excitation. A common voltage excitation method generates the output voltage containing the reciprocal terms of the resistance of sensors. On the other hand, a common current excitation method produces the output voltage including the proportional terms of the resistance of sensors. An example derivation for the output signal of the current excitation method is shown here.

Vout=I·R=IR0(1+αΔT)

where I and α is the excitation current and the temperature coefficient of resistance, respectively.

We provide here a new temperature correction algorithm suitable for use in connection with CDS MR sensors.

We define the following terms.

GPATH: temperature insensitive transimpedance gain of the analog circuits

R0, ΔR0: temperature independent resistance and magnetoresistance, respectively

α, β: temperature coefficient of nominal resistance and magnetoresistance, respectively

VMR,measured(t): the measured MR signal (temperature sensitive)

VBASE,measured(t): the measured baseline signal (temperature sensitive)

VMR,corrected(t): the desired MR signal after temperature correction

ΔT: temperature change at time t comparing to the initial temperature at time 0

In the ideal condition where temperature does not change, VMR and VBASE are as follows:

\({V_{{MR},{ideal}}(t)} = {{G_{PATH}{V\left( {\frac{1}{R_{0} + {\Delta \; R_{0}}} - \frac{1}{R_{0}}} \right)}} \approx {- \frac{G_{PATH}V\; \Delta \; R_{0}}{R_{0}^{2}}}}\)
\({V_{{BASE},{ideal}}(t)} = \frac{G_{PATH}\Delta \; V}{R_{0}}\)

Including temperature fluctuation effect, VMR and VBASE become

\({V_{{MR},{measured}}(t)} = {{- \frac{G_{PATH}V\; \Delta \; R_{0}}{R_{0}^{2}}} \cdot \frac{1 + {\beta \; \Delta \; T}}{\left( {1 + {\alpha \; \Delta \; T}} \right)^{2}}}\)
\({V_{{BASE},{measured}}(t)} = \frac{G_{PATH}\Delta \; V}{R_{0}\left( {1 + {\alpha \; \Delta \; T}} \right)}\)

Initial values of these two terms at time 0 are as follows.

\({V_{{MR},{measured}}(0)} = {- \frac{G_{PATH}V\; \Delta \; R_{0}}{R_{0}^{2}}}\)
\({V_{{BASE},{measured}}(0)} = \frac{G_{PATH}\Delta \; V}{R_{0}\left( {1 + {\alpha \; \Delta \; T}} \right)}\)

Normalizing the MR signal and the baseline signal to their initial magnitude at time 0,

\(\frac{V_{{MR},{measured}}(t)}{V_{{MR},{measured}}(0)} = \frac{1 + {\beta \; \Delta \; T}}{\left( {1 + {{\alpha\Delta}\; T}} \right)^{2}}\)
\(\frac{V_{{BASE},{measured}}(t)}{V_{{BASE},{measured}}(0)} = \frac{1}{1 + {\alpha \; \Delta \; T}}\)

First, the temperature dependent component of the nominal resistance in a MR sensor is derived.

\({\alpha \; \Delta \; T} = {\frac{V_{{BASE},{measured}}(0)}{V_{{BASE},{measured}}(t)} - 1}\)

Next, the temperature dependent component of the magnetoresistance is expressed as follows.

\({\beta \; \Delta \; T} = {{{\frac{V_{{MR},{measured}}(t)}{V_{{MR},{measured}}(0)} \cdot \left( {1 + {\alpha \; \Delta \; T}} \right)^{2}} - 1} = {{\frac{V_{{MR},{measured}}(t)}{V_{{MR},{measured}}(0)} \cdot \left( \frac{V_{{BASE},{measured}}(0)}{V_{{BASE},{measured}}(t)} \right)^{2}} - 1}}\)

The ratio of the temperature coefficient of MR to that of nominal R is defined here.

\(\kappa \overset{\Delta}{=}{\frac{\beta}{\alpha} = \frac{{\frac{V_{{MR},{measued}}(t)}{V_{{MR},{measured}}(0)} \cdot \left( \frac{V_{{BASE},{measured}}(0)}{V_{{BASE},{measured}}(t)} \right)^{2}} - 1}{\frac{V_{{BASE},{measured}}(0)}{V_{{BASE},{measured}}(t)} - 1}}\)

The equation of VMR,measured can be represented without two temperature coefficients.

\({V_{{MR},{measured}}(t)} = {{- \frac{G_{PATH}V\; \Delta \; R_{0}}{R_{0}^{2}}} \cdot \frac{1 + {\kappa \left( {\frac{V_{{BASE},{measured}}(0)}{V_{{BASE},{measured}}(t)} - 1} \right)}}{\left( \frac{V_{{BASE},{measured}}(0)}{V_{{BASE},{measured}}(t)} \right)^{2}}}\)

In order to desensitize it from temperature fluctuation, we can multiply it with the term below.

\({V_{{MR},{corrected}}(t)} = {{{V_{{MR},{measured}}(t)} \cdot \frac{\left( \frac{V_{{BASE},{measured}}(0)}{V_{{BASE},{measured}}(t)} \right)^{2}}{1 + {\kappa \left( {\frac{V_{{BASE},{measured}}(0)}{V_{{BASE},{measured}}(t)} - 1} \right)}}} = {- \frac{G_{PATH}V\; \Delta \; R_{0}}{R_{0}^{2}}}}\)

So the temperature insensitive magnetoresistive voltage output is derived only with the VMR,measured and VBASE,measured, without the knowledge of the temperature coefficients of both nominal resistance and magnetoresistance of the MR sensor.

The algorithm for the temperature correction in case of current excitation on MR sensors is also given here.

VMR,ideal(t)=APATHI((R0+ΔR0)−R0)=APATHIΔR0

Considering temperature fluctuation,

\({V_{{MR},{measured}}(t)} = {{A_{PATH}I\; \Delta \; {R_{0}\left( {1 + {\beta \; \Delta \; T}} \right)}} = {A_{PATH}I\; \Delta \; {R_{0}\left( {1 + {\kappa \left( {\frac{V_{{BASE},{measured}}(t)}{V_{{BASE},{measured}}(0)} - 1} \right)}} \right)}}}\)
\(\mspace{20mu} {where}\)
\(\mspace{20mu} {\kappa \overset{\Delta}{=}{\frac{\beta}{\alpha} = \frac{\frac{V_{{MR},{measured}}(t)}{V_{{MR},{measured}}(0)} - 1}{\frac{V_{{BASE},{measured}}(t)}{V_{{BASE},{measured}}(0)} - 1}}}\)

APATH: temperature insensitive voltage gain of the analog circuits

Temperature desensitization is done by this multiplication.

\({V_{{MR},{corrected}}(t)} = {{{V_{{MR},{measured}}(t)} \cdot \frac{1}{1 + {\kappa \left( {\frac{V_{{BASE},{measured}}(t)}{V_{{BASE},{measured}}(0)} - 1} \right)}}} = {A_{PATH}I\; \Delta \; R_{0}}}\)

### E) Experimental Work

FIGS. 7A-D show experimental results of correlated double sampling. FIG. 7A shows measured referred to input noise (RTI) in baseline. γ is the slope of the 1/f noise. Typically 0.5≤γ≤2. FIG. 7B shows the CDS effect on the results of FIG. 7A. The 1/f noise is eliminated. FIG. 7C shows measured referred to input noise (RTI) in the magnetoresistive signal. FIG. 7D shows the CDS effect on the results of FIG. 7C. Most of the 1/f noise is suppressed.

FIGS. 8A-D show experimental results demonstrating temperature correction technique. FIG. 8A shows the response of nominal resistance to the temperature change due to the cold hexane solution applied at six minutes. FIG. 8B shows the response of magnetic resistance. κ (the ratio of TCMR to TCR) is −5.11 and it will be used in the temperature correction of ΔR. FIG. 8C shows the response of magnetic resistance. R and ΔR are simultaneously measured using CDS. FIG. 8D shows the measured ΔMR ratio (dash curve) and the corrected ΔMR ratio (solid curve) using the present temperature correction in ppm. The corrected ΔMR ratio stays at around the 0 ppm regardless of the temperature change.

FIG. 9A shows results from a binding experiment using magnetic nanoparticles. This plot shows binding curves for five sensors, one of which is covered by the thick passivation layer and serves as a control. The control cannot be influenced by nanoparticles on the thick passivation layer because the distance between particles and the control is beyond the limit of the proximity effect of the particles. The error bar represents the noise from binding kinetics and measurement setup.

FIG. 9B is an SEM image of sensor 1. Particle coverage is 51.02%. FIG. 9C is an SEM image of sensor 2. Particle coverage is 16.03%. FIG. 9D is an SEM image of sensor 3. Particle coverage is 12.85%. FIG. 9E is an SEM image of sensor 4. Particle coverage is 7.67%.

Experiments to confirm the functionality of the present CDS and TC techniques have been conducted using GMR SV sensors arrays (FIGS. 7A-D and 8A-D). If CDS is not performed in the acquisition of VBASE,measured and VMR,measured, these signals will be contaminated with explicit 1/f noise (FIGS. 7A and 7C). The amplitude of the 1/f noise overwhelms the effect of temperature change on the sensors, thereby temperature correction will not properly work. Utilizing the present CDS technique in the measurement can effectively suppress 1/f noise from the measured signals (FIGS. 7B and 7D). The evaluation result of the present TC is shown in FIGS. 8A-D. When the cold hexane solution is applied to the sensor surface at six minutes, the nominal resistance (R0) and MR rapidly changes corresponding to the abrupt temperature change (FIGS. 8A and 8C). As time goes on, surface temperature starts to return to the original temperature and R0 and MR are restored to the initial values. The ratio of two temperature coefficients is constant regardless of the temperature change (FIG. 8B). With the information of temperature drift extracted from the R0 change, the measured MR can be made temperature-insensitive using the present TC technique (FIG. 8D).

FIGS. 9A-E show results from a binding experiment with Fe3O4 superparamagnetic nanoparticles of 15 nm in diameter using chemical absorption between Polyethylenimine and the surfactant of the particles. The reaction can be quantitatively measured. Validation of the quantitative result in FIG. 9A has been done analyzing SEM images through the percentage of the area coverage by nanoparticles (FIGS. 9B-E). Therefore it is demonstrated through the experiments that the combination of the present CDS and temperature correction techniques is effective to produce a noise resilient output from magnetoresistive sensors.

To better appreciate this work, we briefly compare these results to earlier double modulation work. This earlier work utilizes double modulation and the Fast Fourier Transform (FFT) to separate the analyte-related signals from background noise and harmonics. In spite of its high frequency resolution and superior thermal noise profile by frequency binning, FFT requires a large number of samples taken for 500 milliseconds to provide a frequency resolution of 2 Hz. It has an additional timing penalty to complete post-processing using measured samples, which is comparable to or more than sampling time, e.g., in the order of seconds. These considerations lead to a conclusion that the spectral analysis is not favorable to the large-scale magnetoresistive (MR) sensor array system regardless of in-pixel switching. In order to enhance the readout performance, we need to explore a different readout scheme other than spectral analysis.

Generally, a large-scale sensor array contains a thousand or more sensors. In order to guarantee real time analysis using a magnetoresistive biosensor array, the system needs to measure the entire array within a specified period of time. Despite the conventional spectral analysis having good SNR performance, a long readout time per column (or channel) can be a fatal disadvantage for real time analysis in bioassays. So fast readout performance is crucial to large-scale MR sensor arrays and corresponding measurement systems.

Correlated double sampling (CDS) as described above can help solve this problem. Basically this technique has been developed in order to mitigate 1/f noise, which is a significant source of noise harming the readout performance of circuits. Theoretically CDS operation just needs two subsequent data acquisitions. If the temporal difference between two acquisitions Δt is getting smaller, CDS can produce 1/f noise-reduced output signals at high speed. This exactly meets our needs to build a high speed data acquisition circuits for large-scale MR sensor arrays. In order to lower the thermal noise, multiple samples of CDS measurements can be taken then averaged. The above described experiments for the proof-of-concept demonstrate that the readout throughput of 48.8 samples per second per channel was achieved when the magnetic field was modulated at 3.125 kHz (2 CDS samples were taken during each period of the field modulation, so the CDS sampling rate was 6.25 KHz) and the 64 CDS output samples are averaged in experiments. These results are 24.4 times faster than the throughput of the conventional double modulation technique with assumptions that the FFT processing penalty is neglected and frequency division multiplexing is not utilized. Therefore, the readout time according to this work is shown to be faster than the conventional spectral analysis and is favorable to the large-scale MR sensor array and system.

### F) Low Noise MR Sensor Array Architecture

Conventional MR sensors arrays consist of only MR sensors and wires in a two dimensional matrix structure like Random Access Memories. They have been scaled up by simply increasing the number of rows and columns. Sensor arrays of this kind having up to 256 elements have been demonstrated.

There is a need for a large-scale microarray to accommodate numerous analyte types of interest among the more than hundreds of thousands of analytes such as human proteins in some biological applications. The conventional way to increase only the number of sensors and wires to more than 256 is hardly achievable because it scales poorly. Connectivity is poor (more pads are required), noise is worse and channel bandwidth is undesirably narrowed.

We provide a MR sensor array architecture which can accommodate more than 10,000 sensors per array. FIG. 10 shows an example. Here 1002 is an MR sensor array. The number of rows and columns can be larger than 100 and thereby more than 10,000 MR sensors can be in the array. The number of pins (or pads) is minimized by utilizing an analog multiplexer 1006 and demultiplexer 1004. Each pixel (e.g., 1008) includes one switch S and one magnetoresistive sensor MR. However, there can be variations for the number of switches inside the pixel. An excitation source 1010 can drive either voltage or current to the sensor array, while multiplexer 1006 provides signals to readout circuitry 1012.

One of the key features of this large-scale MR sensor array is that it has a pair of analog multiplexer (Mux) and demultiplexer (deMux) as column line (heavy dashed lines e.g., 1020) and row line (heavy solid lines e.g., 1018) selectors, respectively. In the example of FIG. 10, 1014 is the row selection input to demultiplexer 1004, and 1016 is the column selection input to multiplexer 1006. Introduction of the Mux and the deMux dramatically reduces the number of input/output pads of the microarray chip, which in turn greatly simplifies the interface with sensor readout circuits. Adopting a two dimensional matrix structure makes the large-scale sensor array to be randomly accessible in time and to be power efficient. However, the fabrication of this array can be complex since both CMOS processes for analog Mux/deMux and non-CMOS post fabrication processes for MR sensors are required, which may increase the total fabrication cost. This cost issue can be resolved by adopting advanced semiconductor fabrication techniques for mass production.

The other key feature is to introduce a switch S (e.g., a metal-oxide-semiconductor (MOS) device) for each pixel as an on/off switch of a sensor. Only sensors in selected pixels are accessible at specific readout time via a turn-on MOS switch and others are disconnected to the column lines to be read by data acquisition circuits. FIG. 11 shows a sensor readout example. Here the pixel at row 1 and column 1 is measured through a turned-on switch, and the state of all switches is shown by ‘ON’ or ‘OFF’ on the figure. Noise generated from other sensors on column 1 is rejected by the turned-off switches. Thus other sensors become transparent when a sensor at row 1 and column 1 is read out by the following readout circuitry on column 1, which improves signal to noise ratio of the data acquisition system. Furthermore, disconnecting unused MR sensors from the column lines also prevents the signal bandwidth of a readout channel from being narrowed.

These benefits are demonstrated by an analog circuit simulation as shown on FIGS. 12A-D. These results are from AC simulation and noise simulation results of a transimpedance amplifier which reads an MR sensor out of at most 128 sensors per column. FIGS. 12A and 12C show magnitude and cumulative output noise, respectively, for a conventional MR sensor array (no per-pixel switches). Note that N indicates additional MR sensors attached to the same channel. As N increases, the channel bandwidth gets narrower and the output noise profile gets worse. Both bandwidth and output noise of the amplifier are heavily dependent on the number of sensors per column.

FIGS. 12B and 12D show magnitude and cumulative output noise, respectively, for a sensor array as on FIG. 10 (i.e., including per-pixel switches). Neither bandwidth nor output noise changes as the number of sensors per column increases.

MOS switches for the large-scale MR sensor array are preferred because of their good on/off switching performance. However MOS switches are not required for practicing the invention. For example, switching diodes can also be utilized in a large-scale MR sensor array as signal switches for a simpler implementation.

