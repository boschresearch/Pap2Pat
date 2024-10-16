# Figure of Merit (FOM) and consumed power

From the CMT analysis (see Supplementary material) one can show that:

where the γ 1 /γ 2 is the gain/loss of the first/second cavity. In our settings γ 1 = γ 2 = γ 0 . The total power P consumed by the platform is

In our experimental platfrom f min = 2.58 MHz and f max = 2.74 MHz, which are the lower/upper bound of frequency range used to perform the measurements. Taking into account the fact that the input signal a in TL 1 has a uniform spectral density, the F OM introduced in Ref. 38 can be written as

We used the S 21 measurements to fit the measurements with CMT parameters, allowing us to estimate the total power P using Eq.8. Finally, along with experimental data of α N EA this allows to estimate the F OM using Eq.9.

Circuit In the first resonator these resistors are connected to the output voltage port of an operational amplifier (Op Amp) in order to produce gain. The Op Amp used in the circuit is one of the three on-chip Op Amps of the Analog Devices ADA4862-3 triple amplifier. The internal resistance between the inverting port to ground is R G1 = 550 Ohm . This is the same as the resistance between the output port and the inverting input port R G2 = 550 Ohm (see extended data The assembly was performed under a microscope with a custom built micro-translational stage to achieve the 20µm gap between the two gold-metalized surfaces of the glass plates (see inset in Fig.

Extended Data Figure 3c). The spacing between the pair of glass plates with gold nanolayers forms a capacitance of about 35 pF, when the mass is at rest. When an acceleration is applied to the platform, the plates are moving closer to one another, leading to an increase of the capacitance. The open parts of the metalized surfaces were connected to the circuit as it is discusses above, while the platform and the mass are grounded. The pair of glass plates form the parasitic capacitances The inset shows the magnified view of the area between the capacitor plates which is about 20 um.

a * (t) requiring the normalization:

, where W is an energy stored in the circuit. This yields that

The voltage V(t) and its derivative V(t) can then be expressed in terms of the complex mode amplitudes as:

from where the expression for the current follows immediately using the second equation of Eq.

## (S3).

We are now moving forward with the description of the PT symmetric system of coupled RLC circuits (Fig. 1a of the main text) using the complex amplitudes representation. First, we write Kirchhoff's laws for the voltages at the nodes of the RLC resonators. They take the form

where

L C is the gain/loss of the first/second LC resonator due to the negative/positive resistance ∓R 1,2 and κ = Cc C is the ratio of the coupling capacitor C c to the capacitance C, which represents the coupling strength between the two resonators. Equation (S6) can be rewritten in terms of the complex amplitudes a 1 , a 2 and their conjugates a * 1 , a * 2 as 1, 2

where it was assumed that the coupling between the resonators is weak i.e. κ 1. We can simplify further the above equation by invoking a rotating-wave approximation. This allows us to decouple a and a * and re-write Eq. (S7) in a CMT form:

where H 0 is the (dimensionless) Hamiltonian of the two-mode system (below a tilde will indicate dimensionless operators).

Next, we incorporate in our modeling the (weak) coupling of the LC resonators to the transmission lines occurring via the capacitance C e = κ e C, κ e 1. At the transmission lines the voltage V TL and the current I TL are represented as a superposition of a forward (+) and a backward (-) propagating wave i.e.

, where Z 0 is a characteristic impedance of the transmission line. At the same time we express the voltages in terms of complex wave amplitudes as: V ± TL = ± Z 0 2 (S ± + S ± * ), where S ± = |S ± |e -iω 0 t . The Kirchhoff's equations that describe the voltage and current at the junction between the transmission line and a resonator with loss given by γ 0 is:

Furthermore, assuming weak coupling κ e 1 and considering a rotating-wave approximation, we can re-write the above set of equations in the form:

where

Combining together Eqs. (S8,S10) allows us to describe our RLC circuit in a temporal CMT form, where after redefinition of phase factors of the propagated waves in the transmission lines as S ± -→ ±iS ± . we get:

Using Eq. (S8) and Eq. (S11) we are now able to map the electronic circuit used in our experiment to the CMT formalism which allows to generalize the analysis of our platform the broad range of frameworks. In the sections below we proceed with the general CMT analysis.

For convenience we have redefined the various parameters associated with the LRC circuit as:

and γ e → 2γ e . Moreover, since γ e and κ e are directly related (see above), we will be referring to the isolated PT -dimer (zero coupling with the transmission lines i.e. κ e = 0) with the equivalent condition γ e = 0.

### S2 Analysis of the CMT Model and Scattering Approach

We first analyze the eigen-spectrum of the Hamiltonian H 0 (see previous section) which describes the isolated system (i.e. γ e = 0) : where γ 1,2 are the dimensionless linewidths of the two resonant modes due to the presence of the gain/loss elements at the first and the second LC resonator respectively. In case of PT symmetric configurations the gain/loss elements are perfectly balanced and therefore γ 1 = γ 2 = γ 0 .

Direct diagonalization of Eq. (S12) allows us to evaluate the (dimensionless) eigenfrequencies and the eigenvectors of the coupled mode system:

From Eq. (S13) we conclude that the two modes of the PT circuit demonstrate an exceptional point (EP) degeneracy when the coupling constant κ becomes equal to the gain/loss strength i.e.

κ EP = γ 0 . For this coupling strength, the value of the degenerate frequency becomes ω

Next, we assume that the couple resonators are initially positioned at the EP configuration while a small perturbation , associated with a small variation at the coupling capacitor due to an applied acceleration, is imposed to the system. Such perturbations will affect the coupling rate as κ = κ EP → κ EP + . At the same time they will induce a shift at the natural frequencies of the resonators ω 0 → ω 0 (1 -) (see Eq. (S8)). Finally, we take into account the linewidth broadening of the natural frequencies of the individual resonators due to their coupling to the transmission lines (see Eq. (S11)). Incorporating these perturbation effects in Eq. (S12), we come up with the following (dimensionless) effective Hamiltonian (see Eq. ( S11))

where the (dimensionless) linewidth broadening term γ e is introduced via the matrix W, see Eq. (S11). A direct diagonalization of H eff gives us the eigenmodes of the open system

which, similar to the isolated system (see Eq. (S13)), they also have an EP degeneracy at = EP = 0. Notice that for γ e = 0, the eigenmodes of Eq. (S15) coincide with the eigenmodes ω

± ( ) of the Hamiltonian H 0 ( ) = H eff ( ; γ e = 0) describing the isolated PT -symmetric dimer in the case that a perturbation has modified the coupling between the two resonators and their natural frequencies as discussed above.

The scattering matrix that describes the transport properties of our system is evaluated from Eq. (S11) and takes the form

where I is an identity matrix and G( ω) is the Green's function associated with the effective Hamiltonian H eff of Eq. (S14). A direct substitution of Eq. (S14) into Eq. (S16) allows us to evaluate the individual Green's function matrix elements:

and via Eq. (S16) the transmittance. The latter takes the form

which allow us to extract analytically the trajectories of the frequencies associated with the transmission peaks. The later are the physical observables that have been used in our sensing study (see main text) and they take the form:

where TPD = -γ 0 + γ 2 0 + γ 2 e ( = EP = 0) is their coalescence point. At this perturbation strength we have that ω ± = ω TPD = 1 -TPD ( = ω EP = 1). From the above equation it is straightforward to show that the transmission peak frequencies around the transmission peak degeneracy (TPD) point, follow a sublinear Puiseux expansion with a fractional 1/2 power. This is a consequence of the EP degeneracy of the eigenfrequencies of the underlying isolated system. It is crucial to point out that while ω ± follow closely the trajectories of the corresponding eigenfrequencies ω

± , their degeneracy occurs at a different parameter value i.e. TPD > EP . As a result, at the TPD the bi-orthogonal basis of the effective Hamiltonian Eq. (S14) does not collapse and, therefore, the associated Petermann factor does not diverge. This divergence of the Petermann factor was considered the source of the sensitivity limitations imposed to the Brillouin ring laser gyroscope in Ref. 18 . Furthermore, the separation of TPD and EP guarantees the analyticity of the various physical observables in the proximity of TPD.

Furthermore, from Eqs. (S18,S19) we can calculate the scaling of the transmittance peak T peak as follows:

This implies that at the point of transmittance peak coalescence = T P D , the transmittance peak approaches the value T peak (

Finally, from Eq. (S16,S17) we have identified the lasing conditions of the open system, as the frequency ω L and perturbation L values for which the scattering matrix diverges. The corresponding values for lasing action are L = -γ 0 + γ 2 0 -γ 2 e , and ω L = 1 -L . We have, therefore, that: L < EP = 0 < TPD .

A panorama of the transmittance spectrum versus the perturbation strength is shown as density plots for various representative values of γ e > γ 0 in Figs. S2a-d. At the same figures we also report the trajectory of the transmission peaks (green dashed lines) Eq. (S19), together with the eigenmodes Re ω eff ± ( ; γ e ) of the Hamiltonian H eff , see Eq. (S15). We point out that these modes are the same with the eigenmodes of H 0 ( ), and therefore we will not distinguish them in this work.

### S3 Quantifications of Sensitivity Enhancement and Non-Orthogonality of modes

In order to quantify the non-orthogonal nature of the eigenmodes of our system, and specifically its proximity to an EP, we are introducing the so-called Petermann factor (P F ) 18 . Specifically:

where

is a traceless part of the Hamiltonian H eff . Notice that the P F ( ) evaluated in Eq. (S21) is the same one associated with the H eff ( ; γ e = 0) ≡ H 0 ( ) and therefore we do not distinguish these two below. We will show that the Petermann factor P F is related with the so-called noise enhancement factor (NEF) of our PT -symmetric circuit.

Furthermore, in order to quantify the sensitivity enhancement associated with the square-root degeneracy of the eigenfrequencies of the system (SEF mode ), we have intrioduced the sensitivity enhancement factor

where ∆ ω eff = ( ω eff + -ω eff -). The final equality in Eq. (S22) requires to substitute the expressions for the resonant frequencies of the H eff from Eq. (S15). It turns out that both P F ( ) and SEF mode ( ) are given by the same expressions.

Since our sensing protocol utilizes the transmission peak frequencies ω ± for measuring the differential acceleration, it is natural to introduce an associated sensitivity enhancement factor which is given by:

where ∆ ω = ω + -ω -. From the above expression we see that the SEF diverges at TPD = -γ 0 + γ 2 0 + γ 2 e where the transmission peaks coalesce.

These three quantities are reported in Fig. S2 for three representative values of linewidth broadening γ e due to the coupling of the PT -symmetric circuit to the transmission lines.

S4 Thermal noise associated with the transmission line and the gain/loss elements of the

#### PT -symmetric circuit

The transport properties our PT -symmetric circuit (see Fig. S1) in the presence of noise sources can be analyzed using a temporal CMT 1,3 :

where t = ω 0 • t is the dimensionless time, H eff is the effective Hamiltonian given by Eq. (S14),

K is a matrix modeling the coupling between the system and the various noise sources involved in the problem and C is a matrix that describes a direct scattering process and has to satisfy the relation CK * = -K 3 . In the scenario that we consider here, the coupling matrices K and C have the form:

Finally, in Eq. (S24) the state vector a describes the excitation inside the scattering domain, and n in (n out ) are state vectors describing incoming (outgoing) excitations from the noise sources to the system (from the system to the noise sources, including the transmission lines).

We assume that there are four noise sources whose inputs are described by the vector 

where k b is the Boltzmann cnstant, T TL l is the temperature of the noise reservoir associated with the transmission line l, T l is the temperature of the noise source associated with the gain/loss elements at the resonator l, Z is the impedance of the transmission lines, R is the resistance responsible for the amplification/attenuation mechanisms associated with the two modes of the system, and ∆ fis the frequency bandwidth over which the signal at each frequency is measured (i.e. ∆ f = 1/τ is inversely proportional to the sampling time τ over which the signal is measured and averaged).

Finally, δ ij and δ(x) are the Kronecker delta and the Dirac delta functions respectively.

The output noise signal n out is evaluated from Eq. (S24) and takes the form

where G is the Green's function given by Eq. (S16). The vector component n out l describes the noise output detected at the l-resonator of the system and n out TL l describes the noise output emitted at the l-th transmission line (see Fig. S1). Below we analyze the effects of the output noise signal at the right transmission line n out TL 2 , on the transmission measurements (we assume that the incident signal is from the left transmission line). The right noise output is given by

where G lm are the Green's function elements given by Eq. (S17). Armed with this knowledge we are now able to evaluate the noise power associated with measurements at the right transmission line:

where the super-index C indicates the cumulative circuit noise from the gain/loss elements of the circuit (denoted with the super-index PT ) and the ambient noise originating from the transmission lines (denoted with the super-index T L). The contribution from the internal (external) noise sources n in 1,2 (n in TL 1,2 ) are denoted as S PT TL 2 (S T L TL 2 ) and are given by:

(S30)

Since our sensing scheme relies on measuring the frequency splitting between the transmission peaks ∆ ω, it is important the analyze the noise power at frequencies ω ± , for ≥ TPD (see Eq.

(S19)), where its contribution will be detrimental. In this respect, we evaluate at ω ± the Green's function elements from Eq. (S17) and using Eq. (S30), we get that:

which allow us to conclude that both S PT TL 2 and S T L TL 2 saturate to a final value at perturbations = TPD where the transmission peaks coalesce and the SEF diverges (see Eq. (S23)).

Next, we evaluate the noise enhancement factors N EF PT TL 2 ( ) and N EF T L TL 2 ( ), defined as the ratio of the noise power at a perturbation to the noise power evaluated at the → ∞ limit. In the domain ≥ TPD we get

where the asymptotic noise power values

4k B T Z∆ f have been evaluated directly from Eq. (S31).

For the specific experimental parameters used in our set-up (R ≈ 1200 Ohm, Z ≈ 50 Ohm, and γ 0 > γ e ) we can make further progress in the evaluation of the total noise enhancement factor. 

where P F ( ) is the Petermann factor, see Eq. (S21). In fact, Eq. (S33) can be further approximated at the weak coupling limit to the transmission lines γ e γ 0 . In this case, the noise enhancement factor approaches the Petermann factor P F (see Fig. S2), i.e.

For the completeness of the study, we also report the noise enhancement factor in the parameter range < TPD . In this case we have that the noise power (see Eq. (S30)) becomes:

and consequently the corresponding noise enhancement factors are

The dependence of N EF PT TL 2 and N EF T L TL 2 from the perturbation is shown in Fig. S2e-h for three typical cases of γ e < γ 0 . In all cases, the noise enhancement factor does not offsets the sensitivity enhancement factor SEF at the proximity of the TPD in agreement with the conclusions of our experimental analysis (see main text). not able to estimate all these contributions we are proceeding by assuming that this proportionality factor is mainly dominated by the noise produced by the gain/loss elements of the circuit and the ambient noise of the transmission lines. A closer inspection of Eq. (S18) reveals that the spectral width is

(S37)

The uncertainty in the measurement of the transmission peak splitting ∆ ω, due to the generated cumulative circuit noise, is then evaluated using the results from Eq. (S29):

where we have introduced the partial uncertainties σ PT ∆ ω ( ) and σ T L ∆ ω ( ) associated with the gain/loss power noise from the circuit and with the ambient noise from the transmission lines. The expression in the denominator in Eq. (S38) is the output field intensity a out L2 = S 21 a in L1 at the right transmission line, where we have assumed an input signal from the left transmission line a in L1 and S 21 is the element of the scattering matrix given by Eq. (S18). Obviously the above expression Eq.

(S38) applies for the perturbation range ≥ TPD where the transmission spectrum demonstrates two peaks. In this domain the noise powers S PT L2 and S T L L2 are given by Eq. (S31). Finally, the value of the transmission coefficient at the position of the peaks in this parameter domain, is found from Eq. (S18) to be:

which indicates that the signal transmitted from the left to the right transmission line is enhanced in a same manner as a Petermann Factor (PF) of the isolated system (see Eq. (S21) and Fig. S2).

Furthermore, substituting in Eq. (S38) the expressions for S PT L 2 , S T L L 2 from Eq. (S31) we get

One can also introduce the uncertainty enhancement factor which describes the degree of enhancement in the uncertainty measurements of the transmission peak frequency splittings with respect to system configurations away from the TPD. We have

where the "asymptotic" uncertainties have been calculated from Eq. (S40) to be σ

Since our experimental platform operates under weak coupling conditions γ e ≤ γ 0 1

(units of ω 0 ), we deduce from the above equation that both enhancement factors Σ PT ∆ ω ( ) and Σ T L ∆ ω ( ) experience small variations in the proximity of ≈ TPD , see Fig. S3a. We conclude, therefore, that the noise enhancement of the proposed platform leaves unaffected the uncertainty of the measurement of the transmission peak frequency splitting in the vicinity of = TPD and does not offset the sensitivity enhancement, which diverges at the same point, see Eq. (S23). This can be contrasted with the results of Ref. 17,18 where they have found that the improved responsivity of a laser gyroscope operating near an EP is precisely compensated by increased laser noise.

S6 Uncertainty in the measurement of transmission peak splitting due to fluctuations of the coupling strength between the two modes Apart from the noise originated from the transmission lines and the gain/loss elements of the electronic circuit, our sensing platform suffers also from noise associated with fluctuations at the variation of the coupling constant κ between the two resonators. These fluctuations are characterized by an uncertainty σ κ in the coupling variation . Their physical origin ranges from the thermal motion of the test-mass (which is used to perturb the coupling strength -coupling capacitance in our circuit) when external acceleration is applied, to fluctuations of the coupling capacitance due to thermal expansion of the glass plates used in our platform, or to variations in their dielectric properties. This uncertainty will be enhanced by the SEF given by Eq. (S23), thus resulting in a cumulative coupling uncertainty (σ κ ∆ ω ( )) 2 = 4 • SEF ( ) (σ κ ) 2 . We infer, therefore, that the uncertainty due to fluctuations of the coupling strength sets the floor level for our measurements.

At the same time, we are pointing out, that this type of noise is not dictated by the presence of the exceptional points. This is not the case with the current optical EP-based lasing platforms whose noise-floor is inherently associated with the formation of EP itself.

Next we estimate the uncertainty σ κ pertaining to the above analysis. It can be decomposed to the thermal noise σ κ ,th associated with the Brownian motion of the test-mass and the remaining noise-sources. We will refer to these sources as added noise sources and they will be characterized by σ κ ,add . Typically, these noise sources prohibit our system from reaching the floor noise level which is dictated by Brownian thermal noise. The uncertainty associated with the latter one is:

where a is the applied acceleration, and α th = 4k b T ωn mQ is the thermal noise equivalent acceleration (see main text), where ω n = 2π • f n and f n is the natural frequency of the mechanical degree of freedom (spring-mass) of our platform, m is the mass of the spring-mass and Qis the quality factor of the mechanical spring-mass resonator. The sensitivity parameter ∂ /∂a = Const that appears in Eq. (S42) describes the sensitivity of the coupling strength to the applied acceleration and is determined by the design of the electronic circuit and the spring-mass.

### S7 Cumulative characterization of uncertainty in the presence of noise sources

We are now ready to describe in a compact manner all the above noise sources. The cumulative uncertainty is given as a sum of the partial uncertainties i.e. σ 2 ∆ ω = σ C ∆ ω 2 + (σ κ ∆ ω ) 2 . Using Eqs.

(S23,S38,S40,S42) we have At this point, it is possible to estimate the noise equivalent acceleration a 2 N EA ( ) =

where the sensitivity of the frequency splitting between the transmission peaks with respect to an applied acceleration a is χ 2 ( ) = 4SEF ( ) • (∂ /∂a) 2 . We have where the first term describes α 2 PT , the second is α 2 T L , the third is α 2 th and the last term is associated with α 2 add (see Eq. ( 5) of the main text).

From Eq. (S44) we can easily deduce that when = TPD = -γ 0 + γ 2 0 + γ 2 e the noise contributions α 2 PT + α 2 T L to α N EA go to zero (see blue dashed line on Fig. S3b). Such behavior indicates that the proposed sensing platform is capable of mitigating these noise effects at the vicinity of = TPD . Consequently, at the vicinity of = TPD , the noise equivalent acceleration a N EA is suppressed (see dark red line on Fig. S3b) to the value determined by the joint contributions of the thermal noise equivalent acceleration α th and the added noise α 2 add (see green dotted line on Fig. S3b). Specifically, we will have: 

# Supplementary Material S1 CMT modeling of the electronic circuit

The electronic circuit of Fig. 1a can be modeled using a CMT picture, see Fig. S1. This mapping allows us to extend the conclusions of our investigations to a broader family of systems where CMT is applicable. At the same time it provides a simple mathematical description of our experimental set-up.

Let us first start from the description of an LC circuit, which is described by a set of equations:

The above equations can be re-written in the form of a second order differential equation for the voltage:

which can be solved easily, giving

where |V | is the voltage amplitude of the LC resonator, φ is the associated phase and ω 0 = 1 √ LC is the natural frequency of the circuit.

It is useful to change variables and define the complex mode amplitude a(t) and its conjugate

