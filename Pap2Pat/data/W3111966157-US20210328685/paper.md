# I. INTRODUCTION

Nonclassical states of light are important resources for quantum technologies, such as quantum information processing, networking, and metrology [1]. Entangled photon pairs, in particular, have applications in solid-state quantum repeaters, a crucial component of long-distance quantum networking that overcomes transmission loss by leveraging the effects of entanglement swapping and quantum teleportation [2][3][4][5][6][7]. Despite the diverse applications for such nonclassical states of light, methods for generating them deterministically remain limited. Currently, successful approaches are based on spontaneous parametric down-conversion [8][9][10] or spontaneous four-wave mixing [11,12] with high performance [13][14][15]. A major drawback of such methods is that the number of photon pairs generated follows a Poissonian distribution [16], rendering the pair generation efficiency too low for scalable quantum systems [3]. Semiconductor quantum dots can deterministically emit entangled photon pairs via biexciton decay cascade [2,[17][18][19][20][21][22][23][24] with high fidelity and emission efficiency. This mechanism, however, requires careful engineering of quantum dots and pumping schemes that poses a technological challenge, motivating the search for alternative pathways to the generation pairs.

In this article, we provide the theoretical basis for a deterministic entangled photon pair source from a pair of dipole-coupled [25] three-level quantum emitters. Each emitter consists of a ground state and two optically active electronic excited states with mutually orthogonal transition dipole moments. The emergent electronic structure of the composite system then allows for the implementation of a radiative decay cascade from a symmetric doubly excited state of the pair, which results in the emission of two entangled photons of orthogonal polarization. We analyze the resulting emission spectra to note qualitative signatures of entanglement, especially in the cross-correlation spectrum.

To better quantify the entanglement of the emitted photon pairs in continuous frequency space, we calculate their entanglement entropy S and Bell state fidelity F. Importantly, Bell state fidelity F can be optimized at the expense of the entanglement entropy S by tuning the defect transition dipole moments and concentrating the probability density within the states of interest, or the ideal Bell state. In addition, we find that the entanglement measures of the emitted photons are robust to relative differences in frequency between the intermediate states, while the fidelity in the presence of phonon-based dephasing is limited when the dephasing rate is on the order of the radiative rate or higher. We also present a method of initializing the system with orthogonally polarized continuous wave lasers that involves two-photon absorption to enable Rabi oscillations between the ground and symmetric doubly excited state of the pair.

This scheme has the advantage of requiring only emitters with well understood singly-excited states that can be realized by a variety of physical systems, whereas accurate determination of the energetics of multiply excited states from first principles remains a challenge. We specifically discuss the applicability of defect emitters, given their fixed geometries enabling stable dipole coupling, diverse symmetries that allow nondegenerate transitions with orthogonal transition dipole moments, and emission properties that can be tailored via external fields. In addition, the chemical selection space of defect systems is vast. The present scheme is, however, likely amenable to dipole-coupled quantum dots or molecules as well, although they may lack certain advantages of dipolecoupled defect centers. The ability to generate entangled photon pairs from defects would enable on-chip integration [12] with quantum memories and emitters, minimizing the need to transduce photons from source to storage to emission in quantum technologies.

# II. MODEL

The system consists of two three-level systems denoted by i ∈ {α, β}. Each three-level system consists of a ground state |g i , an excited state |x i with energy hω x and transition dipole moment d x i = x i |er|g i = d x i x, and an excited state |y i with energy hω y and transition dipole moment d y i = y i |er|g i = d y i ŷ, where r is the position operator and e is the electron charge. The energy level diagram and dipoleallowed transitions are plotted in Fig. 1(a). The Hamiltonian H i of each isolated three-level system can be written as

When emitters α and β at positions r α and r β , respectively, are brought close and couple via electric dipole interactions, the total electronic Hamiltonian H el can be written in the product space of the two three-level systems as

where  include the interactions of static dipoles as diagonal terms in the single-emitter subspace. We also assume the orbitals of neighboring emitters do not hybridize in the interdefect ranges considered to be a few to tens of nanometers because, for defects specifically, orbitals can be localized within a few angstroms [26][27][28][29][30]. The dipole interaction energy J pq is [25]

where r is the relative permittivity of the host material, e s i is the unit vector of the dipole moment d s i , and n is the unit vector of r αr β . The coupling rates J pq can be calculated from the ab initio transition charge densities of the respective electronic transitions or can be obtained directly from the ab initio calculations of the excited states of the coupled emitter pair. Since transition dipole moments can be on the order of ∼1 eÅ in small-to medium-sized molecules [31] on the same size scale as defect emitters, we estimate that emitters spaced a few nm apart can have dipole interaction energies on the order of tens of μeV.

Assuming for the sake of simplicity that n lies on the x axis, and that the dipole moments of the same polarizations of emitters α and β are identical (d x ≡ d x α = d x β and d y ≡ d y α = d y β ), H el can be diagonalized to produce nine eigenstates with eigenenergies listed in Table I. The subscripts "A" and "S" stand for "antisymmetric" and "symmetric" combinations, respectively. The energy diagram of the eigenstates of H αβ and H el and their dipole-allowed transitions, derived from the dipole operator d listed in Table II in Appendix A, are plotted in Figs. 1(b) and 1(c). Notably, direct transitions between symmetric and antisymmetric states are dipole forbidden. From the energy diagram corresponding to H el , we see that a polarization-entangled photon pair can be emitted when the system is prepared in |xy S and irreversibly decays.

We calculate emission spectra into free space by coupling the emitter system initially prepared in |xy S to an unexcited continuum of photon modes and solving the time-dependent Schrödinger equation under the Weisskopf-Wigner approximation [32], similar to the approach introduced in Ref. [33]. The total Hamiltonian H of the coupled emitter-photon system is The photonic Hamiltonian H ph is H ph = jl hω j a † jl a jl , where a jl (a † jl ) are annihilation (creation) operators of the jth mode in the electromagnetic vacuum of free space with polarization l ∈ {X, Y } and energy hω j . In H ph , we have dropped the zero-point contribution with no loss of generality. The electron-photon coupling Hamiltonian in the RWA and dipole approximation is

, where E jl is the electric field with magnitude E in the l direction that we assume to be constant for all j, and d op = o|er|p with |o and |p being quantum states of the combined twoemitter system.

The ansatz for a general electron-photon wave function, noting that for a system prepared in |xy S there can be a maximum of two excitations distributed among the electronic and photonic states, is

where j and k are indices for the continuum of photon modes and |vac is the photon vacuum state, and c g jk , c x S j , c y S j , and c xy S are time-dependent amplitudes. We have dropped all antisymmetric, |yy , and |xx terms because the emitter system is initially prepared in |xy S .

We solve the time-dependent Schrödinger equation under the Weisskopf-Wigner approximation to find the final state of the electron-photon system under irreversible spontaneous decay [33]:

where

, and is the frequency spacing. Further details on obtaining Eq. ( 7) are in Appendix B.

# III. ENTANGLED PHOTON PAIRS

We explore the physical parameters that result in photon pair entanglement. First, we calculate spectra for a photon pair emitted by a dipole-coupled emitter pair and note spectral signatures of entanglement. We optimize the Bell state fidelity by tuning transition frequencies. These changes can be implemented by appropriate selection of an emitter system or applying external fields.

The emission cascade caused by the radiative decay of the optically excitable |xy S state of the composite emitter-emitter system results in the emission of x-and y-polarized photons whose number spectra are generally distinct, as we show in Fig. 2(a) for the parameters given in the figure caption. We calculate the number spectra, or the probability of finding an x-polarized (y-polarized) photon with frequency

. While the xpolarized photon spectrum N X (ω j ) (blue curve) peaks around the frequencies ω X,1 and ω X,2 , the maxima of the y-polarized spectrum are found at ω Y,1 and ω Y,2 , corresponding to the respective transitions in the two-photon cascade depicted in Fig. 1(c) as blue and red lines.

The emitted x-and y-polarized photons of different frequencies exhibit nontrivial correlations. We plot in Fig. 2

, measuring the probability to simultaneously detect an x-polarized photon of frequency ω j and a y-polarized photon of frequency ω k . The cross-correlation function features local maxima at two points. When an x-polarized photon is detected with frequency ω X,1 , the y-polarized photon is most likely detected with frequency ω Y,2 [i.e., N XY (ω X,1 , ω Y,2 ) is a maximum], and when an x-polarized photon is detected with frequency ω X,2 , the probability of simultaneously finding a y-polarized photon peaks for frequency ω Y,1 . This correlated behavior for a pure state is an intuitive signature of bipartite entanglement.

We consider two metrics to rigorously quantify the entanglement of emitted photon pairs. The first metric is the entanglement entropy S [34][35][36]:

We find the singular values λ n by Schmidt decomposition of the photonic portion | ph of the final state in Eq. ( 6):

where the creation operators b † nX = j ψ n j a † jX and c † nY = k φ nk a † kY in the Schmidt basis, λ n represent wave function coefficients in decreasing order with n starting at 0 and incrementing by 1, and ψ n j and φ nk are the eigenfunctions of c g jk . The entanglement entropy is zero if the state is factorizable and greater than zero for an entangled state.

In protocols based on entanglement, it is often convenient to work directly with Bell states, so the second and third metrics we consider are the Bell state efficiency η and fidelity F, where the Bell state | + = 1 the highest λ n to |10 and |01 , respectively:

We trace out all states where n 2 to write the reduced density matrix ρ R as

where

and the Bell state fidelity

In Fig. 3 we show how the entanglement can be optimized by tuning emitter parameters. In Fig. 3(a), we sweep d x while holding all other physical parameters described in Fig. 2 constant. As a result, ω Y,2 [ω X,2 ] shifts relative to ω Y,1 [ω X,1 ], modulating the distance between peaks of the single-photon spectrum of a given polarization. Notably, for the exact conditions plotted in Fig. 2,d x = d y , F is nearly 1 while η = 0.69. In Fig. 3(b), we zoom into the region around

Here we observe a minimum in S and F and a maximum in η. The entanglement entropy drops here because the frequency of a photon with a given polarization emitted by one of the two decay paths is the same as the photon with a given polarization emitted via the other decay path, so photon pairs emitted by either of the two decay paths are identical. The finite linewidth of the emissions, however, permits entanglement among photon modes within this peak, so the entanglement entropy does not bottom out at 0.

F and η of the Bell pair change in opposite directions surrounding the minimum of F and S. To understand the origin of this observation, in Fig. 3(c) we plot the first few Schmidt coefficients λ n when: (i) d x = d y , corresponding to the state analyzed in Fig. 2, (ii) S and F are minimized, and (iii) both η and F > 0.90. In (i), we see that λ n come in pairs, mean-ing that this state is a superposition of many high-fidelity, polarization-entangled Bell states. In (ii), where S and F are minimized, λ n decays more quickly than in (i). Nearly all of the population is concentrated in the first state, so there are fewer entangled states, lowering S. A balance is achieved in (iii) where probability density is concentrated within the first two pairs of entangled states, but λ 0 = λ 1 . Thus, by tuning the transition frequencies, we can optimize for F or η. The entanglement measures are robust to changes in ω X,1 -ω Y,1 , and F and S are relatively unaffected by up to an order of magnitude increase in γ g,y S , as shown in Appendix C. We also show that the fidelity in the presence of dephasing is limited by the radiative linewidth ∼γ g,yS in Appendix D, suggesting optimal operation under dilution fridge conditions. Finally, we note that the emitted photon pairs can undergo entanglement distillation to further enhance the Bell state fidelity [34,[37][38][39][40].

# IV. PUMPING SCHEME

We next describe a possible pumping scheme involving two-photon absorption via continuous wave lasers to initialize the composite emitter system in the doubly excited |xy S state from which the entangled photon pair is emitted after radiative decay cascade, analogous to schemes proposed for the Mølmer-Sørensen gate [41] and biexcitonic semiconducting quantum dots [42]. We consider a general scenario where the transition frequencies ω X,1 = ω X,2 and ω Y,1 = ω Y,2 . In this case each electronic transition of the system can be selectively addressed by choosing the right polarization and frequency of an external laser drive. In particular, the following two-photon driving Hamiltonian H can be realized if two lasers of polarizations and amplitudes E x x and E y ŷ, and respective frequencies ωX,1 = ω X,1 + δ and ωY,2 = ω Y,2 -δ, are used to illuminate the system: 

the first two lines of Eq. ( 14) represent a drive that is nearly resonant with the respective electronic transitions, whereas the remaining lines are off resonant. Furthermore, we assume that the sum of the drive frequencies is resonant with the two-photon transition from the ground state |g to the doubly excited state |xy S ( ωX,1 + ωY,2 = ω X,1 + ω Y,2 ). In this case it is possible to apply the rotating-wave approximation and neglect the off-resonant terms:

We derive the effective Hamiltonian of the driven system by first considering the dynamics of a trial wave function:

under the Hamiltonian in Eq. ( 15) expressed in the interaction picture with respect to the Hamitonian of the bare system (neglecting the small broadening due to spontaneous emission for the purpose of this derivation):

The following differential equations can be obtained:

ȧxy S = -iE x e i(ω X,2 -ωX,1 )t a y S -iE y e iδt a x S . (21) Equations ( 19) and ( 20) can be used to eliminate a x S and a y S in the adiabatic approximation:

Eqs. ( 22) and ( 23) can be inserted into Eqs. ( 18) and ( 21).

Neglecting rotating terms and small energy shifts, the effective dynamics are ȧg = -ig eff a xy S , (24) ȧxy S = -ig * eff a g , (25) which correspond to the effective Hamiltonian

with

This Hamiltonian induces Rabi oscillations between |g and |xy S with frequency 2|g eff |. If the illumination is applied for time τ drive = π/(2|g eff |), the system is driven from the ground state to the desired state |xy S . An analogous pumping scheme exploiting the state |y S with two lasers of polarizations and amplitudes E x x and E y ŷ, and respective frequencies ωX,2 = ω X,2 -δ and ωY,1 = ω Y,1 + δ, could be used to drive the system into the doubly excited state as well.

Lastly, we remark that optimizing pumping schemes for state preparation of highly excited states, such as the |xy S state that account for phonon-based dephasing and phonon-assisted transitions, is a complex and active area of research, as evidenced in the field of semiconducting quantum dots for deterministic generation of entangled photon pairs [43][44][45][46][47][48][49][50][51][52].

# V. CONCLUSIONS

The present study provides the theoretical basis for a deterministic entangled photon-pair source from dipole-coupled emitters. Specifically, we dipole couple two three-level emitter systems, each with excited states with orthogonal transition dipole moments, to form a composite emitter system. When the composite emitter system is excited to a symmetric doubly excited state and subsequently deexcites in a radiative cascade, two entangled photons are emitted. We find that the entanglement measures of the emitted photons are robust to relative differences in frequency between the intermediate states. Importantly, the Bell state fidelity F and efficiency η can be optimized, for example, by tuning the defect transition dipole moments.

The proposed scheme is especially amenable to defect emitters, although quantum dots or fixed molecules may be used to realize the scheme as well. Defects in both 2D and 3D have wide applicability in quantum technologies, especially as quantum memories because they combine the favorable coherence and nonclassical emission properties of isolated atoms [53,54] with the scalability and stability of solid-state technologies [55][56][57][58]. A key breakthrough that highlights their applicability is the experimental demonstration of memory-enhanced quantum communication for quantum repeaters [59].

Defects are natural candidates because of their fixed geometries enabling stable dipole coupling, diverse symmetries that allow well defined and orthogonal transition dipole moments, and emission properties that can be tailored chemically or externally and also integrated on-chip for a variety of quantum technologies. In addition, the chemical selection space of defect systems is vast, as the chemical identity of the defect and surrounding matrix can be permuted to discover the appropriate system for a specific application [60]. Because accurately computing multiple excited states remains a significant challenge [61], the present scheme involving just singly excited states is more amenable to computational searches 

## Initial

Final

of defect system candidates. A current challenge of realizing defect-based quantum emitters, however, is the relatively low phonon-limited quantum efficiency, the highest of which has been observed to be 87% ± 7% for single-photon emitters in hBN [62] as compared to theoretical predictions of >96% phonon-limited quantum efficiency in semiconductor quantum dots with realistic experimental parameters [63]. As is the case in semiconductor quantum dots [33,49,[64][65][66], system imperfections of defect-based systems may be modulated by coupling defects to external fields, including electric, magnetic, and strain, as well as to waveguides and sculpted electromagnetic environments of cavities to improve fidelity and collection efficiency. Several of these effects have been studied extensively in defect systems [67][68][69][70][71][72], thereby enabling near-term experimental observations of the present proposal.

Here we explicitly show how we obtain Eq. ( 7) in the main text, the wave function coefficient of the steady state electronphoton state. We reproduce the ansatz for a general electronphoton wave function from Eq. ( 5) in the main text:

The interaction Hamiltonian is: 

where we assume op is real. We now solve the differential equations in the Weisskopf-Wigner approximation. We first take Eq. (B4) and formally integrate it:

We get an analogous equation for c y S j and insert both into Eq. (B3): e -i(ω y S +ω k )(t-τ ) c xy S (τ )dτi g,y S t 0 e -i(ω y S +ω k )(t-τ ) c g jk (τ )dτ

In the Weisskopf-Wigner approximation it is commonly assumed that the time integrals can be extended to infinity and that the τ dependent coefficients can be extracted from the integral by setting τ = t. Since we are operating in the Schrödinger picture, we have to perform this procedure with caution and define the slowly-varying amplitudes of a coefficient c A (τ ) = e -iω A τ cA (τ ). We then set cA (τ ) ≈ cA (t ), which is equivalent to performing the Markov approximation in the interaction picture. In this approximation we get:

The integral in the last line can be further decomposed and the lower integration limit can be extended to -∞:

We further neglect the imaginary part of the parenthesis, the principal part (P{}) that generally leads to a spectral shift, and we retain only the delta function. We note that, in the discrete case, δ(ω k -ω j ) → δ jk / (which is a discrete representation of the delta function). Notice also that e -iω xy S t cxy S (t ) = c xy S (t ). We therefore get the result: We get a similar result for the first term in the second parenthesis of Eq. (B8):

The remaining terms in Eq. (B8) yield after applying the same procedure:

-π j y S ,xy S g,y S c g jk (t )δ(ω k -ω y S )

This term is neglected in the calculations because of the frequency restriction imposed by the delta function, although in principle this term is of the same order as the terms leading to decay. We therefore obtain:

Similarly, we can derive the remaining differential equations:  

This system of equations can be solved with the initial conditions: which matches Eq. ( 7) in the main text.

# APPENDIX C: ROBUST ENTANGLEMENT

In Fig. 4, we show that the entanglement of the emitted photon pair is robust to changes in ω X,1 relative to ω Y,1 , while F and S decrease as γ g,y S increases.

# APPENDIX D: DEPHASING

We consider the impact of emitter imperfections, such as phonon-based dephasing of defect emitters, that results in fluctuations in the energies of the defect emitters. We implement the effect of dephasing by averaging the final states of the emitted photons over an ensemble of quantum states generated using a probabilty distribution of emitter frequencies, reflecting the broadening of the transition frequencies due to dephasing effects [73]. The fidelity F de in the presence of dephasing can be estimated as where |ψ de (ω x S , ω y S , ω xy S ) is calculated just as |ψ is in Eq. (11), except that the central frequencies of the emitters ω i are substituted by ω 0 i in Eq. ( 7), where i ∈ {x S , y S , xy S }. Explicitly, |ψ = |ψ de (ω x S , ω y S , ω xy S ) , as in Eq. ( 11). We assume that ω 0

x S , ω 0 y S , and ω xy S belong to a probability distribution P. While the exact probability distribution depends on the microscopic physical mechanism underlying dephasing, we choose to represent P as a 3D Gaussian [74] i G i ( ω i , σ ), physically representing independent fluctuations of the energy levels of the relevant excited states following a Gaussian distribution. We plot the fidelity in the presence of phonon-based dephasing in Fig. 5, where σ i is the full width at half maximum, representing the dephasing rate and ω i = ω 0 i -ω i .

FIG. 5. Fidelity F de in the presence of Gaussian dephasing with dephasing rate σ , normalized by the radiative rate γ g,xS , for the conditions corresponding to the pink lines in Figs. 3 and4.

The fidelity in the presence of dephasing F de is limited by the radiative linewidth γ g,xS , suggesting ideal operation in dilution fridges for the rates described here. Lastly, we note that while we have considered the effect of phonon-based dephasing on the performance of the presently described scheme, we have not considered phonon-assisted transitions between, for instance, symmetric and antisymmetric states in the composite energy diagram in Fig. 1. These effects are known to have a major impact on the resulting collection efficiency of entangled photon pairs from the biexciton decay cascade of semiconducting quantum dots, as described in Sec. IV, and warrant further investigation upon selection of a candidate defect system.

# ACKNOWLEDGMENTS

We acknowledge fruitful discussions with Christopher Ciccarino, Stefan Krastanov, Matthew Trusheim, and Dirk Englund. This work was supported by the Department of Energy 'Photonics at Thermodynamic Limits' Energy Frontier Research Center under grant DE-SC0019140. T.N. is partially supported by the U.S. Department of Energy, Office of Science, Basic Energy Sciences (BES), Materials Sciences and Engineering Division under FWP ERKCK47 'Understanding and Controlling Entangled and Correlated Quantum States in Confined Solid-state Systems Created via Atomic Scale Manipulation'. D.S.W. is an NSF Graduate Research Fellow. P.N. is a Moore Inventor Fellow through Grant GBMF8048 from the Gordon and Betty Moore Foundation.

# APPENDIX A: DIPOLE OPERATOR

We explicitly write the dipole operator in the eigenbasis of the total electronic Hamiltonian H el in Table II.

