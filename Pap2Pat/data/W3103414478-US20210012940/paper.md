# Introduction

Magnetization switching using current-induced spin-transfer torque (STT) 1, 2 has attracted increasing interest for non-volatile memory technologies like magnetoresistive random access memory [3][4][5] . However, the large current density required for STT switching is limiting the technological advancement in terms of the energy efficiency and bit density. Recently, there is a growing interest in the voltage or electric-field controlled switching mechanisms [6][7][8][9][10] as a possible solution to address the issues involving memory bandwidth and high-power consumption 8,11 .

Summary of key contributions. In this paper, we propose a composite structure that can enable electric-field controlled magnetization switching assisted solely by the interlayer exchange coupling (IEC) between the fixed and the free magnets. The magnets are separated by two tunnel barriers sandwiching a thin layer of a spacer material that exhibits large IEC. The electric-field control of IEC relies on the formation of a quantum-well (QW) within that spacer layer with discrete energy states positioned above the equilibrium Fermi level, which enables electric-field induced modulation of the transmission coefficient between the two magnets via the resonant tunneling phenomena. We use Non-Equilibrium Green's Function (NEGF) method 12 to show that a sizable bias-dependent oscillatory IEC could be induced which, in turn, could switch the free magnet to have either a ferromagnetic (F) or an antiferromagnetic (AF) configuration with respect to the fixed magnet, depending on the sign of the IEC. The configuration will be retained once the electric-field is removed because the barriers suppress the equilibrium IEC.

Switching in both directions could be possible for the same bias-polarity, but different magnitudes above the switching threshold, which is different from the existing electrical switching mechanisms. We use a coupled Landau-Lifshitz-Gilbert (LLG) equation 13,14 to show that the switching threshold of the electric-field controlled IEC energy is independent of the Gilbert damping and same for magnets with in-plane and perpendicular anisotropies. We argue that the proposed structure can be optimized to lower both the current in the structure and the operating voltage, while getting a sizable bias-dependent IEC for magnetization switching. On the other hand, the switching speed is inversely proportional to the Gilbert damping and slower for a perpendicular magnet as compared to an in-plane magnet. These unique features of the proposed structure suggest that devices with significantly improved energy-delay product can be designed.

2 Electric-field control of the interlayer exchange coupling (IEC) Basic mechanism. Our prediction is based on the well-established phenomenon that two ferromagnets (FM) separated by a metallic [15][16][17][18] or a non-metallic 19,20 spacer layer prefers either a F or an AF configuration at equilibrium, depending on the sign of the IEC. The sign of the IEC oscillates periodically as a function of the spacer thickness (see Fig. 1(a)), due to the quantum-interference by the majority and the minority spins in the spacer as they see different QW like potential profiles below the equilibrium Fermi level E F formed at the magnetic interfaces [21][22][23][24] . On the other hand, a metallic spacer which forms additional QW states above E F and the transparency between the magnets can be controlled using an electric-field via resonant tunneling phenomena. This structure will exhibit a bias-dependent oscillation in IEC that grows in magnitude. Barrier heights are 0.7 eV and widths are 1 nm each. Spacer thickness is 0.8 nm. a thick oxide barrier significantly reduces such IEC (see Fig. 1(b)) and the two FMs do not have a preferential configuration at equilibrium. We introduce two oxide barriers at the two magnetic interfaces of the structure in Fig. 1(a) (see Fig. 1(c)), which form a QW with discrete energy states above E F . At these discrete states, transmission coefficients are high as seen for the resonant tunneling diodes 25 . These states can be probed by tuning the contact electrochemical potentials (µ 1,2 ) with an electric-field across the structure. Subsequently, the two FMs feel a sizable IEC due to a spin-dependent interference by the filled states within the spacer, similar to the discussion in Fig. 1(a). We argue that the spin-dependent interference could be constructive or destructive depending on the electric-field controlled transmission coefficient, giving rise to a bias-dependent oscillation in IEC (see Fig.

# 1(c))

. The IEC strength is also expected to grow with increasing electric-field as the number of occupied QW states increases.

Model. We have analyzed the IEC between two magnets based on parameters calculated using the Non-Equilibrium Green's Function (NEGF) method. The IEC energy per unit area is usually taken as the difference of energy density change across the QW (∆E) between the ferromagnetic (F) and the antiferromagnetic (AF) configurations [21][22][23] , as given by

where the change in the energy density across the QW is calculated as 21 

with ∆n s = n s (d) -n s (0) being the change in the spin density across the QW. Note that the magnetization easy-axis is along z-direction in this discussion.

We calculate n s using the NEGF method using a single band effective mass 1D tight-binding

Hamiltonian is used here for calculations. We assume that the structure under consideration is spatially uniform along the transverse directions and transverse modes are nearly decoupled so that transport can be analyzed with 1D Hamiltonian for every mode. The spin density is given by

where

is the energy along the transverse plane y-z, D 0 is the 2D density of states on the transverse plane, σ z is the z-Pauli matrix, and G n is the correlation function. We approximate the D 0 with the 2D density of states of the bulk given by m * /πh 2 where m * is the effective mass and h = h/2π.

The correlation function is obtained as

where

is the occupation factor of j th contact with contact electrochemical potential µ j , A j = G R Γ j G R † is the spectral function with Γ j being the broadening function of the j th contact, G R = [EI -H -Σ] -1 is the Green's function, Σ is the total self-energy of the contacts, and H is the Hamiltonian of the structure. We assume that the voltage applied across the two-terminal structure mostly drops across the two oxide barriers. The details of the NEGF based calculations can be found in the supplementary information. In this paper, positive and negative IEC indicates AF and F configurations respectively.

# Materials and

Structure. An ideal material for the spacer of the proposed structure in Fig. 1(c) could be the transition metals e.g. Rh, Ru, Ir, Re, and Cu 15,26,27 , which exhibit large IEC strengths at equilibrium in a geometry shown in Fig. 1(a). The strength of the equilibrium IEC across a metallic spacer in Fig. 1(a) depends on the shape of the spin-dependent QW, which is determined by the mismatch of the d-electron bands between the FM and the metallic spacer material 15,24 , growth condition, and hybridization at the interfaces 27 . In this paper, we have calibrated the spacer parameters for NEGF calculations such that the first AF IEC strength in the structure in Fig. 1(a) is around ∼ 4 mJ/m 2 , comparable to a Co|Ru system 15 . We have set the spacer thickness to 0.8 nm.

The barrier heights in Fig. 1(c) were set around 0.7 eV, as typically observed for MgO 28,29 .

The barrier thicknesses were set to 1 nm each. It has been discussed both theoretically 30 and experimentally 31,32 that equilibirum IEC across such a thick oxide is negligible. A non-negligible equilibrium value could be seen for very thin oxide since the transmission coefficient could be due to the tunneling effect 31,32 . Bias-dependent IEC through a reasonably thick single oxide barrier has been discussed theoretically via high voltage tunneling 33,34 and experimentally via mobile oxygen vacancies 7 . However, these mechanisms could be subject to higher power consumption, oxide breakdown, and/or long switching time determined by the slow migration of oxygen ions 35, 36 . Voltage induced transition from ferromagnetic to antiferromagnetic configuration and vice versa has been demonstrated on synthetic antiferromagnetic (SAF) structures using ionic liquid gating 37 , however, the configuration switches back once the voltage is removed. Similar electricfield induced modulation of the IEC in a SAF layer with an oxide gate has been discussed 38 and combined with the voltage-controlled magnetic anisotropy to demonstrate a bi-directional switch-ing. A different mechanism of manipulating the interlayer exchange coupling has recently been demonstrated 39 with an oxide spacer that is capable of exhibiting a metal-insulator transition upon temperature change.

The mechanism proposed in this paper enables bias-dependent IEC via resonant tunneling phenomena, which have the promise to enable lower-voltage controlled operation and faster switching in a non-volatile manner, as compared to the existing mechanisms. Similar resonant tunneling have been demonstrated up to room temperature in a double-barrier magnetic tunnel junction (MTJ) [40][41][42] , where the QW forms within a thin magnetic layer and exhibits a bias-dependent oscillation in the magnetoresistance. Here, we argue that the resonant tunneling via a QW formed within a non-magnetic material that exhibits a large IEC and will exploit the property of the material to enable a bias-dependent oscillation in IEC.

# IEC assisted magnetization dynamics

Magnetization switching. The bias-dependent IEC should switch the free magnet to have either F or AF configuration with respect to the fixed magnet, as dictated by the sign of the IEC. The configuration will be retained once the electric-field is removed because the thick oxide barriers diminish the equilibrium IEC. Such bias-dependent change in IEC sign will enable magnetization switching in both directions for the same voltage polarity (but different magnitudes), which is very different from existing mechanisms for electrical switching. We simulate with three consecutive voltage pulses across the structure, with pulse width of 5 ns each and pulse heights corresponding We start with an F configuration as the initial condition and show the z component of the magnetization vectors (m z1 for fixed and m z2 for free) as a function of time, in Fig. 2(b). The magnetization dynamics have been simulated with an exchanged coupled LLG model 13,14 assuming single domain magnets under zero external magnetic field and negligible spin current. The first pulse (P4) induces an AF IEC peak and switches the free magnet to make it AF with respect to the fixed magnet. The AF configuration is retained when the pulse is removed. The second pulse (P3) induces a F IEC peak which switches the free magnet back to a F configuration with respect to the fixed magnet. Again, the F configuration is retained when the pulse is removed. The third pulse induces a weak AF peak with strength |J ex | below the switching threshold, hence, the free magnet does not switch.

Switching threshold. The threshold of the IEC strength required for magnetization switching (|J ex0 |) is given by

Here S is the cross-sectional area of the device, E 1 and E 2 are the thermal energy barriers of the fixed and the free magnets i.e. E 1 > E 2 . E 1,2 are determined by 1 2 M s H k Ω of the corresponding magnet where M s is the saturation magnetization, H k is the anisotropy field, and Ω is the magnet volume. Eq. ( 4) is obtained from the coupled LLG equation in Refs. 13,14 under zero external magnetic field and zero spin current. Note that Eq. ( 4) is valid for magnets with both in-plane and perpendicular magnetic anisotropies. An analytical derivation of Eq. ( 4) starting from the LLG model 13,14 and assuming perpendicular anisotropy is provided in the supplementary information.

The IEC induced switching mechanism does not depend on the Gilbert damping and the magnetic anisotropy, which is different from the non-equilibrium spin current based switching mechanisms 43 and similar to an external magnetic field induced switching.

Switching time. The IEC assisted switching time is given by

where θ 0 is the initial angle between the fixed and the free magnetizations in the units of radian (rad). γ is the gyromagnetic ration in the units of rad s -1 T -1 . Eq. (B) is valid only for magnets with perpendicular anisotropies. The constant prefactors are deduced from empirical fitting which can be revisited as the field evolves, however, functional dependence on the parameters are benchmarked with detailed LLG simulations in the supplementary information. The switching time for magnets with in-plane anisotropies are also affected by the demagnetization field and can be analyzed directly using the LLG equation. Note that the switching time is lower for larger IEC energy which is similar to the STT-mechanism where a higher spin current yields a lower switching time 43 . The pulse rise and fall times in Fig. 2(a) should be faster than the switching time in Eq. (B) in order to avoid any unwanted reverse switching due to slow change in the voltage amplitude.

Signature of bias-dependent IEC. The oscillation in equilibrium IEC as a function of the distance between the two magnets is observed in spin-valve like structures as a shift in the switching field within the hysteresis loop of the total moment M 15,17,18 . We argue that similar shift in the switching field should be observed for the proposed structure in Fig. 1(c) as a function of input voltage, while the distance between the two magnets is kept fixed. We simulate such M -H loops (see Figs. 2(c)-(f)) using the coupled LLG model 13,14 under an external magnetic field (H ext ) sweep, assuming negligible spin current, and using the bias-dependent IEC energy J ex calculated from the NEGF. For V in = 0 V, J ex is negligible (see, P1 in Fig. 1(c)) and the M -H loop is such that the two magnets are switching at the corresponding coercive fields (here, H k1 = 300 Oe for fixed and H k2 = 150 Oe for free in the simulations), as shown in Fig. 2(c). Note that the x-axis of Figs. 2(c)-(f) are normalized with respect to H k1 and y-axis are normalized with respect to the total magnetic amoment M 0 = M 1 + M 2 of the structure.

At V in = 1 V, we observe the first bias-dependent AF peak of +0.012 mJ/m 2 (see, P2 in Fig.

# 1(c))

. This exhibits as a sizable lowering of the switching field of the free magnet as shown in Fig.

# 2(d).

The fixed magnet switching field also changes slightly. Note that such bias-dependent change in the switching field will be an indication of the bias-dependent IEC, even if the IEC strength is below the switching threshold. At V in = 1.3 V, we observe the subsequent F peak of -0.08 mJ/m 2 (see, P3 in Fig. 1(c)) and the M -H loop exhibits a rectangular shape (see Fig. 2(d)). This suggests that the two magnets are in F configuration and they are switching simultaneously. At

V in = 1.6 V, we observe the second AF peak (see, P4 in Fig. 1(c)) and the M -H loop exhibits a large split due to a large shift in the free magnet switching field. The middle loop corresponding to the AF configuration with the total moment M 1 -M 2 .

4 Discussion on efficient design:

Delay and energy. The Gilbert damping and the magnetic anisotropy of the proposed device can be tuned to achieve fast switching operations (see Eq. (B)), while the IEC switching threshold J ex0 remains unaffected (see Eq. ( 4)). This is different from the STT-based devices where there exists a trade-off between the switching threshold and switching time in terms of these parameters 43 . We argue the proposed structure can achieve a sizable bias-dependent J ex > J ex0 while the current density J c of the structure can be significantly lower. This is because the magnitude of the J c is limited by the separation between the contact occupation factors

) with E being the energy, k B being the Boltzmann constant, and T being the temperature. However, with the increased transmission between the two FMs, a sizable IEC is felt by the FMs contributed by all the occupied QW electronic states positioned under the electrochemical potentials. Thus, the proposed device have the potential to achieve significantly low energy-delay product.

We have calculated the current density of the proposed structure using NEGF as J c = dE Re Tr i h (HG n -G n H) , which is shown in Fig. 3(a). When the contact electrochemical potential is at a QW energy state, the transmission coefficient between the magnets increases.

This, in turn, increases the conductance of the structure and the J c exhibits a peak at the QW state, as shown in Fig. 3(a). The position of the QW states can also be detected by looking at the sign change in d 2 J c /dV 2 in , as shown in Fig. 3(b).

QW dimensions. The charge current in the structure can be further decreased by using a We have analyzed the effect of various barrier height on the proposed mechanism of inducing a bias-dependent IEC in Fig. 4(a). A sizable IEC strength persist even for reasonably high barrier heights contributed by the large number of states within the spacer metal, positioned below the Fermi level. However, the bias-dependent oscillatory nature of the IEC shifts toward the higher operating voltage as we increase the barrier height. We also noted from our simulations that for a given barrier height, an additional sharp oscillation peak can be observed at lower operating voltages which occurred due to a small mismatch of transmission coefficients for the parallel and the antiparallel configurations. This sharp oscillation shifts toward higher operating voltages linearly with the increasing barrier height and periodically reoccurs at the lower voltage side. For a given barrier height, the voltage window required to observe this sharp oscillation is very small as compared to the technological interest and further evaluation of this additional oscillation we leave as future work.

We have also analyzed the effect of the spacer metal thickness on the proposed bias-dependent oscillatory IEC mechanism, as shown in Fig. 4(b). It is interesting to note that the oscillation peaks occur at lower operating voltages for a thicker spacer layer, but the strength of the peaks decreases as well. The former is observed because the spacer layer thickness defines the QW width. An increase in the QW width lowers the discrete energy states as well as the spacing between two consecutive states. Thus the operating voltage to observe an IEC peak lowers with increasing spacer thickness. Similar lowering of QW energy states for wider QW and its consequence on the operating voltage has been discussed for double-barrier MTJ 41 . The later observation is due to the fact that the distance between two magnets is increasing with increased spacer thickness and the IEC strength weakens. Similar weakening of the IEC strength with increasing distance between the magnets has been discussed for spin-valve like geometries 15-17, 21, 22, 22, 23 .

# Conclusion:

In conclusion, we propose a structure that enable electric-field controlled magnetization switching assisted solely the interlayer exchange coupling (IEC) between the fixed and the free magnets.

The two magnets are separated by two oxide barriers sandwiching a metallic spacer that exhibits high IEC strength. The basic idea relies on formation of a quantum-well (QW) within the metallic spacer, which contains discrete energy states above the Fermi level exhibiting high transmission coefficients due to the resonant tunneling phenomena. When the contact electrochemical potential is at one of these discrete states, the two magnets feel a sizable IEC contributed by all the filled QW states under the electrochemical potential. We predict a bias-dependent oscillation in IEC that grows by magnitude with voltage. Such oscillatory IEC can enable bi-directional switching for the same voltage polarity but different magnitudes above the switching threshold value. We show that the switching threshold of this new mechanism is independent of the Gilbert damping and same for magnets with in-plane and perpendicular anisotropies. However, the switching time is inversely proportional to the Gilbert damping and different for magnets with in-plane and perpendicular anisotropies. This decoupling of the dynamic parameter may lead to significant lowering of the energy-delay product as compared to the state-of-the-art mechanisms.

where Ψ is the wave function of the n th lattice point along y-direction. We work with a single band effective mass Hamiltonian, described by (1) equilibrium electrochemical potential µ eq , ( 2) exchange splitting ∆ ex , (3) barrier heights, ∆ B , (4) well-depth, ∆ B0 , (5) effective mass for ferro- 6) effective mass for oxide m * ox , (7) effective mass for metallic spacer m * n , and (8) contact electrochemical potentials µ 1,2 . Note that we view these parameters to take into account wide varieties of factors like imperfection at the ferromagnet-non-magnet interfaces by assuming effective values. Below, we present Hamiltonian for each transverse mode with wave vector k in the device.

# A.0.1 Ferromagnetic Layers

For the lattice points within the ferromagnetic layers (indicated by region-1 in Fig. 5), we have

with t f = h2 2m * f a 2 , q is the electron charge, h is the reduced Planck's constant, m * f is the effective mass in the ferromagnet, k is the transverse wavevector, ∆ ex is the exchange-splitting energy in the ferromagnet, I 2×2 is a 2 × 2 identity matix, σ is the Pauli spin matrices, and a is the lattice distance. Here, qV (n) is the potential on the n th lattice point of the structure. The potential is varied by the applied voltage V in across the structure which drops across each layer according to the resistance of each layer, as shown in Fig. 5. m 1 and m 2 are the magnetization vector of the fixed and the free magnet, respectively. Note that in Eq. (7a), m = m 1 for fixed magnet region and 

# A.0.2 Oxide Layers

For the lattice points within the oxide layers (indicated by regions 2 in Fig. 5), we have

with

ox is the effective mass, and ∆ B is the barrier height.

# A.0.3 Spacer Layer

For the lattice points within the metallic spacer layer (indicated by region 3 in Fig. 5), we have

with

n is the effective mass in the spacer, and ∆ B0 is the depth of the spindependent QW like potential below the equilibrium electrochemical potential.

# A.0.4 Ferromagnet | Oxide Interfaces

For the lattice points for the interface of the ferromagnet and oxide-1 layers (indicated by interface-1 in Fig. 5), we have

[β] = 0,

where m ≡ m 1 is for interface 1 and m ≡ m 2 is for interface 2.

# A.0.5 Oxide | Spacer Interfaces

For the lattice points for the interface of the oxide and spacer layers (indicated by interface-2 in Fig. 5), we have

Self-Energy of Contacts We will present self-energy matrices for each transverse mode with wave vector k in the device. The self-energy matrices are given by

where k ↑ 1,2 and k ↓ 1,2 are longitudinal wavevectors of up and down spins respectively, which are estimated from

with E C,1 and E C,2 being the bottom of the conduction bands for left and right magnetic contacts.

Note that in the present discussion, the magnetization m 2 of the free magnet can lie in an arbitrary direction, hence, the effective Σ 2 is given by

with (θ, φ) being a rotational matrix given by

Note that in the analysis presented here, we assume that the magnetization m 2 lies in the z-x plane creating an angle θ with the m 1 with φ = 0.

NEGF Quantities We calculate the following quantities:

• Green's function:

with Σ = Σ 1 + Σ 2 (see Eqs. ( 12) and ( 14)). H is the Hamiltonian of the system as discussed earlier.

• Spectral function:

with Γ = Γ 1 + Γ 2 and Γ 1,2 are broadening functions which represent the anti-Hermitian part of Σ 1,2 i.e. Γ 1,2 = i Σ 1,2 -Σ † 1,2 . Note that A/2π provides the density of states of the system.

• Correlation function:

with Σ in = Σ in 1 +Σ in 2 being the in-scattering function. Note that G n /2π provides the electron density of the system.

• In-scattering function:

with f 1,2 being the Fermi occupation factors of contacts 1 and 2, given by

Here, µ 1,2 are electrochemical potentials of contacts 1 and 2, k B is the Boltzmann constant, and T is the temperature. Note that in the present discussion:

• Current operator:

Current operator between two adjacent lattice points j and j + 1 is given by

The charge current density is given by

The spin current density is given by

where σ is the Pauli spin matrices. 

where σ z is the z-Pauli matrix, and G n is the correlation function. We assume that the structure under consideration is spatially uniform along the transverse directions and transverse modes are nearly decoupled so that transport can be analyzed with 1D Hamiltonian for every mode. Under such assumption, we do a mode summation on the transverse plane (y-z plane), to estimate the 2D z spin density at j th lattice point, as given by

where

is the energy along the transverse plane y-z, and D 0 is the 2D density of states on the transverse plane.

We approximate the D 0 with the 2D density of states of the bulk given by 47

where m * is the effective mass and h = h/2π. The change in z spin density across the quantumwell is given by

The total change in energy of the occupied states across the quantum-well is calculated as

which is in the units of J-m -2 .

In a magnetic structure under consideration, the interlayer exchange coupling energy density is calculated as the change in Eq. ( 29) from ferromagnetic (F) to antiferromagnetic (AF) configurations [21][22][23] J ex = ∆E F -∆E AF .

We have calibrated the spacer parameters such that the first AF IEC strength is around ∼ 4 mJ/m 2 , as shown in Fig. 1(a). For simplicity, we assume two oxide barriers are same with width of 1 nm each. The oxide barrier heights were set around 0.7 ∼ 0.8 eV, as typically observed for MgO 28,29 .

We assume that the voltage applied across the two-terminal structure mostly drops across the two oxide barriers. The NEGF setup has been discussed in detail in the supplementary information.

# B Switching Threshold and Time

In this section, we will derive the IEC assisted switching threshold in Eq. ( 2) of the main manuscript.

We will also discuss the switching time in Eq. ( 3) in terms of detailed numerical simulation using a coupled LLG equation.

# LLG Equation

We assume mono-domain magnets and analyze the magnetization dynamics using a coupled-Landau-Lifshitz-Gilbert (LLG) equation 13,14 , given by

where m 1 and m 2 are the magnetization vectors of FM-1 and FM-2 respectively, h is the reduced Planck's constant, S tot is the total cross-sectional area of the magnets, γ is the gyromagnetic ratio, α g is the Gilbert damping constant, H ef f indicates the effective magnetic field which includes the demagnetizing field and the anisotropy field of the corresponding magnet, J ex is given by Eq.

(1) in the main manuscript, and I S is given by Eq. (24). N S,1 and N S,2 are the number of spins in FM-1 and FM-2 respectively, where N S,1/2 = M s,1/2 Ω 1/2 /µ B , M s1 and M s2 are saturation magnetizations of FM-1 an FM-2, Ω 1 and Ω 2 are the volumes of FM-1 and FM-2, and µ B is the Bohr magneton.

Simplification We assume that the spin current in the structure is negligible i.e. I S = 0. There is no external magnetic field i.e. H ext = 0 and we assume perpendicular magnetic anisotropy so that the effective magnetic field in the structure is given by H ef f 1,2 = H K1,2 ẑ. Thus, Eqs. (31a)-(31b) reduces to

) , (32a)

Derivation of Switching Threshold For parallel conditions: m z1 = 1 -δ 1 and m z2 = 1 -δ 2 or m z1 = -1 + δ 1 and m z2 = -1 + δ 2 , we have from Eqs. (32a)-(32b)

which are stable only if (-J ex × S) < E 1 and (-J ex × S) < E 2 . Note that δ 1,2 → 0.

Similarly, for anti-parallel conditions: m z1 = 1 -δ 1 and m z2 = -1 + δ 2 or m z1 = -1 + δ 1 and m z2 = 1 -δ 2 , we have from Eqs. (32a)-(32b)

which are stable only if (J ex × S) < E 1 and (J ex × S) < E 2 .

Thus, the conditions for stability in either parallel or anti-parallel configurations are given by

which yields the condition for stability as

Thus, the condition required to make any stable configuration unstable is given by

which in turn, gives the switching threshold expression in Eq. ( 2) of the main manuscript. Note that for simplicity, the expression for switching threshold is derived assuming perpendicular magnetic anisotropy. However, the expression is valid for in-plane magnetic anisotropy as well.

Switching Time We provide an expression for the switching time given by Eq. ( 3) in the main manuscript

We have compared this simple expression with the detailed LLG simulation results from Eqs.

(31a)-(31b) as shown in Fig. 6 for different parameters. In most of our simulations, we have used 

# A NEGF Model

In this section, we discuss the Non-Equilibrium Green's Function (NEGF) method 12,47 used for quantum-transport simulations on the structure in Fig. 1 in the main manuscript.

Hamiltonian We write the tight-binding Hamiltonian of the structure as the following

