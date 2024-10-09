# DESCRIPTION

## FIELD OF THE INVENTION

The present invention relates generally to heading error correction and, more particularly, to a system and method for using a pulsed Rb-87 magnetometer at geomagnetic fields to suppress heading error.

## BACKGROUND OF THE INVENTION

Total-field atomic magnetometers measure the magnitude of the magnetic field by directly measuring the Larmor precession frequency of the electron spins of alkali-metal atoms in the presence of the field. They can operate in geomagnetic fields (10-100 μT) and have a wide range of applications, including space magnetometry, fundamental physics experiments, biomedical imaging, archaeological mapping, mineral exploration, searches for unexploded ordnance, and magnetic navigation. The highest sensitivity for scalar magnetometers has been achieved in a pulsed pump-probe arrangement with a sensitivity of 0.54 fT/√{square root over (Hz)} in a field of 7.3 μT. However, practical magnetometers need to operate in geomagnetic field around 50 μT.

Recently an all-optical pulsed gradiometer has reached a magnetometer sensitivity of 14 fT/√{square root over (Hz)} over a broad range including Earth's field. One major and practical challenge of Earth's field magnetometers is the control of heading errors which otherwise significantly limit their accuracy. They cause the measured field values to depend on the orientation of the sensor with respect to the field, especially presenting problems for the magnetometry-based navigation.

All alkali-metal magnetometers suffer from heading errors because alkali-metal isotopes have nonzero nuclear spin of I>½. There are mainly two physical sources of heading errors: the nonlinear Zeeman splitting due to mixing of ground Zeeman states IF, m) and the difference in Larmor frequencies for the two hyperfine manifolds due to the nuclear magnetic moment. The non-linear splitting corresponds to a difference of 2.6 nT between neighboring Zeeman states for Rb-87 in a 50 μT field. At this field, the linear difference between Zeeman resonance frequencies in F=1 and F=2 states is 200 nT. These splittings of the Zeeman resonance lines produce broadening and asymmetries in the lineshape depending on the orientation of the sensor with respect to the field. For Rb-87 in a 50 μT field, the orientation-dependent shifts are on the order of 15 nT.

Previous approaches of reducing the heading errors in other alkali vapor systems have focused on suppressing the nonlinear Zeeman splitting, including double-modulated synchronous optical pumping, light polarization modulation, measurements of high-order polarization moments, use of tensor light-shift to cancel quadratic Zeeman splitting, and spin-locking with an additional radiofrequency (RF) field. However, they have some practical drawbacks such as complexity in implementation or requiring use of RF fields. These methods also do not cancel frequency shifts associated with the difference of Zeeman resonances for F=1 and F=2 states. In magnetometers operated with continuous optical pumping, the optimal sensitivity is achieved for spin polarization generally near 50%. As a result, there is usually a significant population in F=1 state which changes depending on the orientation of the magnetometer relative to the magnetic field.

As such, there is a need for an approach to reduce heading errors that avoid the above shortcomings.

## SUMMARY OF THE INVENTION

According to various embodiments, a method for reducing heading error in a magnetometer that uses Rb-87 atoms is disclosed. The method includes varying a direction and magnitude of a magnetic field at different spin polarization regimes.

According to various embodiments, a magnetometer adapted for reduced heading error is disclosed. The magnetometer includes a multipass cell containing Rb-87 vapor, a pump laser operated in a pulse mode that is synchronous with a Larmor frequency, and two orthogonal probe lasers configured to rotate to vary a direction and magnitude of a magnetic field at different spin polarization regimes.

Various other features and advantages will be made apparent from the following detailed description and the drawings.

## DETAILED DESCRIPTION OF THE INVENTION

Alkali-metal atomic magnetometers suffer from heading errors in geomagnetic fields as the measured magnetic field depends on the orientation of the sensor with respect to the field. In addition to the nonlinear Zeeman splitting, the difference between Zeeman resonances in the two hyperfine ground states can also generate heading errors depending on initial spin polarization.

Generally disclosed herein are embodiments for suppressing heading errors in an all-optical scalar magnetometer that uses free precession of polarized Rb-87 atoms by varying the direction and magnitude of the magnetic field at different spin polarization regimes. In the high polarization limit where the lower hyperfine ground state F=1 is almost depopulated, it is shown that heading errors can be corrected with an analytical expression, reducing the errors by up to two orders of magnitude in Earth's field. The linearity of the measured Zeeman precession frequency is also verified with the magnetic field. With lower spin polarization, it is found that the splitting of the Zeeman resonances for the two hyperfine states causes beating in the precession signals and nonlinearity of the measured precession frequency with the magnetic field. The frequency shifts are corrected by using the unique probe geometry where two orthogonal probe beams measure opposite relative phases between the two hyperfine states during the spin precession.

Generally disclosed herein are embodiments for correcting heading errors as a function of both the direction and magnitude of magnetic field at a wide range of initial spin polarization. With the all-optical, free-precession Rb-87 magnetometer, a short-pulse pumping technique is used to achieve very high initial spin polarization near 95% regardless of the field orientation such that the initial spin state is well-defined. The population of F=1 state becomes negligible, and Zeeman coherences decay much faster in F=1 state than in F=2 state due to spin-exchange collisions between alkali-metal atoms. In this high polarization limit, the polarization-dependent heading errors can be minimized. It is also determined that the average Larmor frequency is given by an analytical expression that depends on the angle between the pump laser and the magnetic field. It is shown this angle can be determined directly from the spin precession signals. Thus, a correction for the heading error can be calculated in real time. After heading errors are corrected, it is found that the accuracy of the magnetometer is on the order of 0.1 nT as a function of both the direction and the magnitude of the magnetic field for fields up to 50 μT.

At lower spin polarization, interesting effects are observed due to non-negligible contribution from the F=1 state. The difference in Zeeman frequencies of F=1 and F=2 states generate beating which is observable in the measurement of spin precession signals. Moreover, the measured spin precession frequency is no longer linear with the magnetic field, even though the splitting itself is linear with the field. Here two probe beams are used to further correct for these heading errors: one is collinear to the pump beam, and the other is perpendicular to the pump. These orthogonal probe beams measure opposite relative phases of the two hyperfine ground states during their precession, allowing one to cancel any effects from the splitting in their Larmor frequency by averaging the two probe measurements. This is because Zeeman coherences precess around the magnetic field in opposite directions for F=1 and F=2 states. As a result, the additional frequency shifts are canceled by averaging the measurements of the two orthogonal probes. Furthermore, experimental results are compared with a density matrix simulation to easily separate signals from F=1 and F=2 states and investigate frequency shifts due to the nuclear magnetic moment.

Analytical Correction of Heading Errors

For Rb-87 atoms in ground states with electronic spin S=½, the energy of the Zeeman sublevel |m with total atomic angular momentum F is given by the Breit-Rabi formula:

\(\begin{matrix}
{E = {{- \frac{\hslash\omega_{hf}}{2\left( {{2I} + 1} \right)}} - {{g_{I}\mu_{B}B_{m}} \pm {\frac{\hslash\omega_{hf}}{2}\sqrt{x^{2} + \frac{4mx}{{2I} + 1} + 1}}}}} & (1)
\end{matrix}\)

where x=(gS+gI)μBB/ℏωhf, gS and gI=μI/(μBI) are the electronic and nuclear Landé factors, respectively, μB is the Bohr Magneton, B is the magnetic field strength, ωhf is the hyperfine splitting, I is the nuclear spin, and the ± refers to the F=I±½ hyperfine components. In the Earth-field range, the m→m−1 Zeeman transition frequency is given by:

\(\begin{matrix}
{{\omega_{F,m} \simeq {\frac{\left( {{\pm \mu_{eff}} - {g_{I}\mu_{B}}} \right)B}{\hslash} \mp {\frac{\mu_{eff}^{2}B^{2}}{\hslash^{2}\omega_{hf}}\left( {{2m} - 1} \right)}}} = {\omega_{L} \mp {\omega_{rev}\left( {{2m} - 1} \right)}}} & (2)
\end{matrix}\)

where μeff=(gSμB+gIμB)/(2I+1), ωL=(±μeff−gIμB)B/ℏ is the Larmor frequency, and ωrev=μeff2B2/ℏ2ωhf is the quantum-beat revival frequency which is nonlinear to the field magnitude. The Larmor frequencies for the two hyperfine states are approximately opposite, but not exactly equal because of the gIμB term. The difference of absolute frequencies is proportional to the magnetic field and equal to 1.4 kHz at 50 μT, where the Larmor frequency is equal to 350 kHz for Rb-87 atoms. The nonlinear Zeeman effect in Earth's field causes a splitting of 18 Hz between neighboring Zeeman transitions, which is non-negligible for magnetometer operation.

The measured transverse spin component can be written in terms of the Rb-87 ground state density matrix as a weighted sum of coherences oscillating at different Zeeman frequencies, given by:

Sx=Tr[ρSx]=ΣF m′=m±1AF m,m′ρF m,m′  (3)

where ρF m, m′ is the off-diagonal element of density matrix for an ensemble of Rb-87 atoms in coupled basis |F m, and AF m,m′ is its amplitude. The measured spin precession frequency is therefore a combination of different Zeeman transition frequencies. Any variation in sensor's orientation with respect to the field can change the relative strength between the coherences, shifting the measured precession frequency.

In the high spin polarization limit, the modification of the measured field due to heading errors is:

\(\begin{matrix}
{B = {\frac{4hv}{\left( {g_{s} - {3g_{I}}} \right)\mu_{B}}\left\lbrack {1 - {\frac{3v}{v_{hf}}\sin\theta\frac{P\left( {7 + P^{2}} \right.}{5 + {3P^{2}}}}} \right\rbrack}} & (4)
\end{matrix}\)

where v=ω/2π is the measured precession frequency, vhf is the hyperfine splitting frequency, P is degree of initial spin polarization, and θ is the angular deviation of the pump beam from the nominal magnetometer orientation where the pump laser is perpendicular to the magnetic field. It is assumed the relative distribution of atoms in F=2 state is given by spin-temperature distribution. The spin temperature distribution is realized when the rate of spin-exchange collisions is higher than other relaxation rates. It is also realized during optical pumping on a pressure broadened optical resonance with fast J-damping in the excited state. These conditions are reasonably well-satisfied in the disclosed experiment. In a 50 μT Earth's field, the maximum size of the correction given by Eq. 4 is on the order of 15 nT with full polarization (P=1).

FIG. 1 shows the comparison between heading error correction calculated with Eq. 4 and numerical simulation of the density matrix evolution. The density matrix model includes optical pumping, free spin precession evolution, and signal fitting as done in the experiment. They agree well in high polarization limit. Thus, if the initial polarization is experimentally found and the angle is extracted, Eq. 4 can be used to find the heading-error free magnetic field. At low polarization more complex behavior is expected due to the incomplete depopulation of F=1 state.

A Pulsed-Pump Double-Probe Rb-87 Magnetometer

A compact integrated magnetometer is used for embodiments disclosed herein with schematic shown in FIG. 2(a). It includes a Rb-87 vapor cell, electric heaters, a pump laser, two probe lasers, and two polarimeters. The cell has height and width of 5 mm, and length of 10 mm. It contains internal mirrors that allows pump and probe beams to reflect back and forth many times inside the cell. The probe beams exit the cell after 11 passes. The sensor is placed inside a magnetic shielding on a rotation stage that allows rotation of the whole assembly relative to the magnetic field. The multipass cell is filled with enriched Rb-87 vapor and 700 Torr N2 buffer gas. It is typically heated to 100° C. giving a Rb-87 number density of 4×1012/cm3 as estimated based on measured transverse spin relaxation rate.

The pump laser is directed in x direction in FIG. 2(a), circularly polarized and tuned to the Rb-87 D1 line. It is operated in a pulsed mode with several watts instantaneous power. It has an adjustable repetition rate, number, and width of pulses. The usual pumping cycle includes 190 pulses with a 70 ns single pulse width that is much shorter than the Larmor period τ=2π/γBz. For a resonant build-up of the spin polarization, the pulse repetition rate is synchronous with the Larmor frequency. The magnetic field is created by a concentric set of cylindrical coils inside two layers of μ-metal magnetic shields. The spin free precession is detected by two off-resonant vertical-cavity surface-emitting laser (VCSEL) probe beams which are linearly polarized. One laser propagates in the x direction, parallel to the pump laser (“horizontal probe”), and the other propagates in the y direction, orthogonal to the pump laser (“vertical probe”). Each balanced polarimeter includes a half-wave plate, a polarizing beam-splitter, and two photodiodes with differential amplification. The two differential signals Vver=V1−V2 and Vhor=V3−V4 are recorded by a digital oscilloscope and have the general form of a sine wave with exponential decay plus an offset:

\(\begin{matrix}
{{V(t)} = {{V_{0}\mspace{11mu}{\cos\left( {{2\pi vt} + d} \right)}e^{- \frac{t}{T_{2}}}} + {V_{DC}(t)}}} & (5)
\end{matrix}\)

where V0 is the initial amplitude, v is the precession frequency, d is the phase delay, T2 is the transverse spin relaxation time, and Vic is the offset. FIG. 2(b) shows the experimentally measured signals at 50 μT. The vertical probe shows a smaller signal than the horizontal probe as it has a smaller interaction volume from a smaller overlap region with the pump beam. An external frequency counter (HP53310A) measures the frequency of the signal by detecting its zero-crossings during the free precession measurement time Tm=3 ms, which is comparable to T2. External high-pass filters are added with fc=20 kHz to cancel DC offsets in the signals going to the frequency counter. The frequency is continuously measured and the center frequency of its histogram distribution is read with a standard deviation of about 1 mHz.

FIG. 3 describes the pump-probe geometry after a change in sensor orientation. The horizontal probe is always collinear to the pump, and the vertical probe is always orthogonal to the pump. In the initial configuration (θ=0°), the pump and horizontal probe are in x, and the vertical probe is in y. After a sensor rotation, the pump beam and horizontal probe are in x″ direction and tilted by θ from the initial magnetometer orientation x where the field Bz is perpendicular to the spin. The vertical probe is in y″ direction at a small angle ϕ=11° from y. This is due to the small tilt of the sensor assembly relative to the vertical axis of the rotation stage that supports the sensor. With the tilt of the sensor, the rotation matrix transforming x, y, z to x″, y″, z″ coordinates is:

\(\begin{matrix}
{R = {{\begin{pmatrix}
{\cos\;\theta} & 0 & {{- {s{in}}}\;\theta} \\
0 & 1 & 0 \\
{\sin\;\theta} & 0 & {\cos\;\theta}
\end{pmatrix}\begin{pmatrix}
1 & 0 & 0 \\
0 & {\cos\;\varnothing} & {\sin\;\varnothing} \\
0 & {\sin\;\varnothing} & {\cos\;\varnothing}
\end{pmatrix}} = \begin{pmatrix}
{\cos\;\theta} & {{- {s{in}}}\;{\theta sin\varnothing}} & {{- {s{in}}}\;{\theta cos\varnothing}} \\
0 & {\cos\;\varnothing} & {{- {s{in}}}\;\varnothing} \\
{\sin\;\theta} & {\cos\;{\theta sin}\;\varnothing} & {\cos\;{\theta cos}\varnothing}
\end{pmatrix}}} & (6)
\end{matrix}\)

In the final configuration, the pump and the horizontal probe are therefore in {circumflex over (x)}″=cos θ{circumflex over (x)}+sin θ{circumflex over (z)}, and the vertical probe is in ŷ″=−sin θ sin ∅{circumflex over (z)}+cos ∅ŷ+cos θ sin ∅{circumflex over (z)}.

Measurement of Heading Errors

The pulsed pump laser can achieve very high initial spin polarization near 95%. This minimizes the polarization-dependent heading errors. In FIG. 4(a) the simulated signals for each hyperfine state are plotted separately, showing how much each hyperfine state contributes to Sx for initial atomic spin polarization P=0.95. The F=1 signal has a very small initial amplitude compared to the F=2 signal and decays faster during the precession. To maximize the polarization experimentally, the width and number of pump pulses are adjusted until the signal amplitude at t=0 in FIG. 4(a) saturates.

In order to apply Eq. 4 to correct for the heading error one must know the tilt angle θ of the magnetometer as shown in FIG. 3. In the absence of other information about the field direction one can find the angle θ from the signal itself by considering the DC component of the spin precession signal. FIGS. 4(b) and 4(c) show the measured signals at θ=45° which have nonzero time-varying DC offsets compared to FIG. 2. A digital low-pass filter is applied to the measured signal to extract the DC component. The DC offset measures the spin component parallel to the magnetic field. As shown in FIG. 3, the sensor has a small tilt about x by ϕ such that the vertical probe is not perfectly transverse to the field Bz. As a result, the vertical probe signal also gains a small DC offset.

From Eq. 6, the initial optically pumped spin is {right arrow over (S)}==S cos θ{circumflex over (x)}″+S sin θ{circumflex over (z)}. Ignoring the spin relaxation for simplicity, the precessing spin at angular velocity ω is then {right arrow over (S)}=S cos θ cos ωt{circumflex over (x)}+S cos θ sin ωtŷ+S sin θ{circumflex over (z)}. The horizontal probe detects the spin component:

Sx″={right arrow over (S)}·{circumflex over (x)}″=SAC+SDC=S cos2θ cos ωt+S sin2θ.  (7)

The first term is the projection of Sx component which oscillates. The second term is the projection of Sz component, resulting in the DC offset. Therefore, the ratio of the initial DC offset to maximum AC amplitude is

\(\frac{s_{DC}}{s_{AC}} = {\tan^{2}{\theta.}}\)

FIG. 5(a) shows good agreement between this equation and the measurements, allowing for estimating the magnitude of θ.

The magnitude of ϕ can also be determined based on the vertical probe signal. The vertical probe detects the spin component:

Sy″={right arrow over (S)}·ŷ″=SAC+SDC=S cos θ(cos ∅ sin ωt−sin θ sin ∅ cos ωt)+S sin θ cost θ sin ∅.  (8)

The ratio of the initial DC offset to maximum AC amplitude is then

\(\frac{s_{DC}}{s_{AC}} = {\sin\;{{\theta sin\varnothing}/{\sqrt{1 - {\cos^{2}\theta\sin^{2}\varnothing}}.}}}\)

FIG. 5(b) shows the measurement of the

\(\frac{s_{DC}}{s_{AC}}.\)

ratio of the vertical probe signal, which gives an estimation of ϕ=11.2°. The sign of θ and ϕ cannot be found independently since they are coupled as shown in the expression of

\(\frac{s_{DC}}{s_{AC}}\)

The ratio of DC to AC signals can also be used to convert the scalar magnetometer to a vector sensor. This involves the additional modulation of the probe laser to determine the sign of θ.

To measure the heading errors, the sensor is tilted with respect to the field in the range −65°<θ<65° and measure the spin precession frequency with the frequency counter. It is important to separate heading errors due to spin interactions from heading errors associated with remnant magnetization of magnetometer components. Rotation of the sensor relative to the field changes the projection of the remnant magnetic fields onto the leading field, resulting in frequency shifts that are hard to distinguish from atomic heading errors. The sensor was constructed with a minimal number of magnetic components. However, there are small amounts of polarizable ferrous materials present in the laser mounts and other electronic components. These components are degaussed, and heater electric currents are turned off during the measurement. Nevertheless, small offsets on the order of a few nT due to remnant magnetization of the sensor remained. To account for these offsets, the polarization of the pump laser was periodically reversed with a half-wave plate and measurements were taken with both polarizations. This approach is used to cancel heading errors by averaging the signals from the two pump polarizations. In this case the difference of the signals are taken to separate the heading errors due to the spin interaction and those due to magnetization of the components in the sensor head.

Heading Errors as a Function of the Sensor Orientation

FIG. 6 reports the measurement of heading errors in 10 μT and 50 μT fields as a function of the sensor's tilt angle θ. If a difference is taken between the two measurements at opposite pump polarizations, the field values at θ=0 are canceled to the order of 0.01 nT. The angle θ is determined from spin precession signals with an uncertainty of about 1°. Fitting to Eq. 4 gives an estimation of the initial polarization, about P=0.9 for the parallel probe signal and P=0.7 for the vertical probe signal. As described previously, the vertical probe has a smaller overlap with the pump beam than the horizontal probe and measures optical rotation from atoms that are less polarized. In a 10 μT field, the heading errors are expected to be only 4% of those in 50 μT. The inset of FIG. 6 shows that the residual errors are comparable and in fact slightly smaller for the case of B=50 μT. This indicates that the residuals are likely due to imperfection in the cancellation of remnant magnetization of sensor components. Even so, it is shown that the amplitude of heading errors due to atomic physics effects are reduced by about a factor of 50 for the horizontal probe measurement and a factor of 20 for the vertical probe measurement by the correction given by Eq. 4.

When the initial spin polarization is less than unity, there is some contribution from F=1 state. This manifests itself as an oscillation in the instantaneous spin precession frequency as illustrated in FIG. 7(a). The simulated spin precession signals are fit to Eq. 5 in individual time segments of 0.05 ms to show the time dependence of the spin precession frequency. It is found that it oscillates at 1.4 kHz, which is equal to the difference between Zeeman frequencies for F=1 and F=2 states at 50 μT. It is confirmed that at other magnetic fields the beating frequency is proportional to the magnetic field. As expected, the amplitude of the oscillations becomes larger for smaller spin polarization. The decay rate of the oscillations depends on the T2 of the F=1 coherences. This beating effect is not sensitive to the orientation of the sensor, so the oscillations at θ=0 and θ=45° are similar. However, for θ=45° one can observe a small additional slow drift of the spin precession frequency. This drift is due to differences in the relaxation rate of F=2 coherences, as discussed in more detail in the next section.

It is found that the oscillations in the instantaneous spin precession frequency have opposite sign for the horizontal and vertical probe beams, as illustrated in FIG. 7(b). As the two hyperfine states have opposite spin precession directions, the horizontal probe detects maximum signal when SxF=2 and SxF=1 are out of phase while the vertical probe detects maximum signal when they are in phase. Therefore, the frequency oscillation can be canceled by averaging the two probe measurements, which reduces the amplitude of frequency oscillations by more than two orders of magnitude. This was experimentally verified as shown in the inset of FIG. 7(b), which is based on fitting the experimental signal to Eq. 5. The two probe measurements show opposite sign of frequency oscillation. The oscillations are larger for the vertical probe beam because it detects a lower average spin polarization. The amplitudes of the experimentally observed oscillations in the instantaneous spin precession frequency appear larger than those predicted by the simulation. This could be due to spatial non-uniformity of the polarization in the cell which is not considered in the simulation.

Heading Errors as a Function of the Absolute Magnetic Field

In addition to investigating heading errors as a function of the angular orientation of the sensor, heading errors are also examined as a function of the absolute magnetic field. The spin precession frequencies are measured as a function of magnetic fields at high (P=0.85) and low (P=0.2) polarizations with the vertical probe. For these measurements it is necessary to create a well-controlled linear magnetic field ramp. The measurements are performed inside magnetic shields which generate a significant hysteresis of the magnetic field. To create a reproducible magnetic field a stair-case ramp is applied as illustrated in FIG. 8. The magnetic field scan is repeated several times without interruptions. The current through the magnetic field coil is monitored using a precision shunt resistor while the repetition rate of the optical pumping pulses is continuously adjusted under computer control to match the Larmor frequency. After several up and down sweeps, both the field and frequency measurements are averaged during the same time period to suppress any field fluctuations.

FIG. 9 shows the measured precession frequency as a function of fields with P=0.85 at θ=0°. With a quadratic fitting function, the frequency for upward and downward field sweeps show high curvature with opposite signs. This is due to the magnetic shield hysteresis, and averaging the two measurements reduces the curvature and residuals of linear fitting by two orders of magnitude.

FIG. 10 shows results of averaging the upward and downward field sweep measurements at two different polarizations P=0.2 and 0.85. Even though the first order heading error correction at θ=0° is zero from Eq. 4, the low polarization result (P=0.2) shows a curvature of −16×10−4 Hz/μT2, much higher than the curvature for high spin polarization (P=0.85) of 2×10−4 Hz/μT2.

FIG. 11 shows the simulated curvature as a function of polarization. The curvature is negligible in high polarization limit but starts to increase at P<0.7. The curvature C=16.52×10−4 Hz/μT2 at P=0.2 with the vertical probe agrees well with experimental measurement. This nonlinear frequency shift is due to the increase in population of F=1 state. The horizontal and vertical probe beams have opposite curvature signs. Therefore, averaging of the two signals can cancel the non-linearity of the frequency, similar to the cancellation of the instantaneous frequency oscillations described previously.

To understand the origin of the non-linearity the evolution of individual coherences is simulated. When θ=0° the F=2 state has two distinct coherences and F=1 state has one distinct coherence. Their initial amplitudes and relaxation are shown in FIG. 12 for P=0.85 and P=0.2. The relative strength of F=1 coherence is much higher at P=0.2 than at P=0.85. As the nuclear spin causes splitting of Zeeman frequencies between two hyperfine states, their interference can generate the observed frequency shift at low polarization. To check the origin of the non-linearity, the nuclear magnetic moment is nulled in the simulation by setting gI=0. The curvature at P=0.2 then reduced to C=0.2×10−4 Hz/μT2. This suggests that the nonlinear frequency shift at low polarization is caused by the linear Zeeman interaction of the nuclear magnetic moment.

## CONCLUSION

Generally disclosed herein are embodiments for reducing heading errors in Rb-87 magnetometer as a function of both the direction and magnitude of magnetic field at different initial spin polarizations. The novel double-probe sensor has shown high sensitivity and significant heading error suppression.

In the high spin polarization limit, heading errors can be corrected for by using analytical expression which is derived based on the density matrix formalism. With the correction, the measured field accuracy is about 0.1 nT in a 50 μT Earth's field. The linearity of the measured Zeeman frequency is verified with respect to the field up to Earth's field with a deviation of less than 0.05 nT. At lower polarization, additional heading errors are observed due to the difference in Larmor frequency of the F=1 and F=2 states. This generates beating in the measured frequency, and it is no longer linear with the magnetic field. Numerical simulation shows that this nonlinearity is caused by the linear Zeeman interaction of the nuclear magnetic moment. To cancel these frequency shifts, measurements from two orthogonal probe beams that measure opposite relative phases between the two hyperfine coherences are averaged.

These results are useful in reducing systematics of alkali-metal-vapor atomic magnetometers operating at geomagnetic fields, especially those in navigation systems. Disclosed herein are approaches for cancelling heading errors with wide range of spin polarizations, and the pump-probe geometry presented herein can give a real-time correction of heading errors. Furthermore, the use of a small sensor and VCSEL lasers makes it suitable for development of compact and miniaturized sensors.

It is understood that the above-described embodiments are only illustrative of the application of the principles of the present invention. The present invention may be embodied in other specific forms without departing from its spirit or essential characteristics. All changes that come within the meaning and range of equivalency of the claims are to be embraced within their scope. Thus, while the present invention has been fully described above with particularity and detail in connection with what is presently deemed to be the most practical and preferred embodiment of the invention, it will be apparent to those of ordinary skill in the art that numerous modifications may be made without departing from the principles and concepts of the invention as set forth in the claims.

