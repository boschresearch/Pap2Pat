# Introduction

Transformation induced plasticity (TRIP) and toughening by mechanically induced martensitic transformation during deformation has demonstrated substantial enhancements of uniform ductility and fracture toughness of materials. The TRIP effect has been thoroughly studied in ferrous systems during the last few decades, leading to success of both homogenous and dispersed austenite toughened TRIP steels [1]. Martensitic transformation also exists in titanium alloy systems, from BCC β phase transforming to HCP α' martensite or orthorhombic α" martensite. Deformation induced α" martensite has been reported in several commercial metastable β titanium alloys, such as β-CEZ [2], and Ti-10-2-3 [3], which have shown mechanical behaviors similar to those of TRIP steels. This offers the potential of using the same concept and knowledge of advanced TRIP steel development to design high performance TRIP titanium alloys with excellent strength/toughness combinations.

Early studies of TRIP titanium alloys date to the 1970s [4]. The initial work investigated TRIP behaviors in binary alloys with eutectoid β stabilizing elements, such as Fe, Mn, and Cr. Nowadays, research efforts on TRIP titanium have been mostly made on design of multicomponent homogenous β alloys. Empirical or indirect quantities were usually used as indicators of β phase transformation stability, such as Mo equivalent value [5], Ms temperature [5,6], and Bo-Md maps [7,8]. Recent developments of multicomponent CALPHAD thermodynamic [9] and mobility databases [10] for titanium systems enable computational design of multiphase alloys with dispersed metastable β particles for TRIP toughening using the fundamental framework developed for TRIP steel design. This work follows a systems design approach to computationally design novel near-α TRIP titanium alloys for naval structural applications. The design process integrated processing/structure/properties/performance relations with CALPHAD based mechanistic models including the Olson-Cohen heterogeneous martensite nucleation theory.

# Conceptual Design of Near-α TRIP Ti alloys

## Property Objectives

To develop new titanium alloys as naval structural materials especially for heavy welded structures, near-α alloys are usually first considered. Due to low β eutectoid alloying element contents, near-α alloys yield less segregation during fusion welding. Targeting marine environment applications, Ti-5111 (Ti-5Al-1V-1Sn-1Zr-0.8Mo-0.1Fe-0.1Si, wt%), a weldable near-α alloy with high toughness, intermediate strength and good stress-corrosion cracking (SCC) resistance, has been developed by the US Navy and TIMET in the 1980s. Compared to the general-purpose workhorse alloy Ti-6Al-4V, Ti-5111 has better fracture toughness but lower yield strength as shown in Figure 1(a).

According to the materials selection method in conceptual design proposed by Ashby [11], the performance index M for naval structural materials selection is M= KIC/σy, where KIC is fracture toughness, and σy is yield strength. This index is directly related to critical flaw size of fracture at the yield stress . M values of 0.5 in 1/2 and 1.0 in 1/2 are minimum and ideal requirement respectively by the US Navy for structural materials [10]. The blue lines in Figure 1(a) indicate these two requirements. This work aims to design a near-α titanium alloy for naval applications combining the high strength of Ti-64 and the high fracture toughness of Ti-5111. In addition, the designed alloys should keep the good SCC resistance and weldability of Ti-5111. In order to achieve the design goal, TRIP toughening was introduced to compensate for the concomitant decrease of toughness with increase of strength. 

## TRIP toughening

Mechanical deformation can stimulate the kinetics of martensite transformation with additional thermodynamic driving force by applied stress and new nucleation sites for martensite by plastic strain. As shown in the stress vs. temperature diagram of Figure 1(b), such transformation includes two modes, stress-assisted and strain-induced transformation [13]. In the stress-assisted regime, applied stress assists martensite nucleation on the same sites responsible for transformation upon cooling. In the straininduced regime, slip yielding procedes the onset of martensitic transformation, which can then occur on new potent nucleation sites produced by plastic deformation. The temperature defines the approximate boundary of the two modes, at which the transformation stress is equal to the yield stress for slip of the alloy. This characteristic temperature can act as a single quantitative characterization of phase stability with respect to mechanically induced transformation. Due to the transformation dilatation, varies with stress state. in uniaxial tension (ut) usually serves as a convenient experimental measure of transformation stability.

The mechanically induced martensitic transformation is found to promote an initial upward stress-strain curvature during deformation due to the combined influence of transformation softening and hardening of transformation product. This unique deformation behavior imparting high stability to plastic flow was proved to delay not only necking during tension but also shear localization both within tensile necks and at crack tips in austenitic steels. Quantitative mechanics modeling also demonstrated transformation toughening via delay of the shear localization driven by void softening in ductile solids [15]. Besides homogenous alloys, dispersed phase systems with metastable particles can exhibit the same transformation plasticity and toughening features. The benefits in fracture toughness strongly depend on the transformation stability of the metastable parent phase [14,15]. The maximum transformation toughening was found at the for the crack-tip (ct) stress state in TRIP steels, as shown in Figure 1(c). The toughening effects are also sensitive to transformation volume change δ, with the toughness increase scaling with the cubic power of δ [15]. Therefore, the transformable phase in TRIP alloys should be designed to have optimal transformation stability and large transformation dilatation to take full advantage of transformation toughening.

## System Structure

A systems approach integrating processing/structure/properties/performance interactions has been successfully applied to computational design of various hierarchically structured materials [16]. This approach was used here through CALPHAD software and databases to achieve the property goals mentioned in 2.1 by a structure of α+β subsystems. The systems design chart for a near-α TRIP titanium alloy is shown in Figure 2. Conventional wrought processing of Ti-5111 with hot rolling and two-step heat treatment (β solution and α+β aging with controlled cooling) was taken to produce a final lamellar colony α+β microstructure. Of the two subsystems, the β subsystem is the focus of this design to provide TRIP toughening, while the α subsystem is primarily to provide strength. For the β subsystem, the phase stability of martensitic transformation was optimized to ensure (ct) close to room temperature and to maximize martensitic transformation dilatation. Brittle grain boundary α (GB-α), Ti3Al and other intermetallic phases need to be prevented to achieve the fracture toughness objective. Overall composition should be similar to Ti-5111 to keep its good SCC resistance and weldability. 

# Model Development and Design Integration

## Transformation Stability Model

For development of TRIP steels, the kinetics of mechanically induced martensitic transformation has been quantitatively modeled based on the Olson-Cohen theory of heterogeneous nucleation [1]. A similar approach can be adopted for titanium alloys with model parameters calibrated to experimental data.

According to the Olson-Cohen theory [17][18][19][20], the critical condition for martensite to nucleate is stated in Equation 1, where the total molar driving force, consisting of chemical thermodynamic driving force and mechanical driving force by applied stress, reaches a critical value ΔGcrit.

(1)

The chemical driving force ΔGchem is the difference in molar Gibbs free energy between product and parent phase with the same composition due to the diffusionless nature of martensitic transformation. ΔGchem can be calculated by Equation 2 using ThermoCalc software with the TiGen database [9] which was developed specifically for low temperature martensitic transformation calculations in titanium alloys.

(2)

The mechanical driving force ΔGmech was estimated following Patel and Cohen [21] by calculating the interaction work of the resolved stresses acting through the shape strain of the most favorable orientation in a randomly oriented polycrystalline matrix. The invariant-plane shape strain associated with martensitic transformation is composed of a shear strain (γ) in its habit plane and a dilatation (δ) normal to it. With a Mohr's circle analysis expressing the stress in von Mises equivalent tensile stress [22,23], the mechanical driving forces of uniaxial-tension and elastic Mode I crack-tip stress states were derived as Equation 3 and 4 respectively. For the shear strain of orthorhombic martensite in titanium alloys, γ=0.13 was used throughout the calculations [24].

(3) (4)

The critical driving force ΔGcrit is described in Equation 5 combines a nucleation defect potency term G0 and frictional work term Wf for martensite interfacial motion due to solution hardening. The frictional work is assumed to have the same dependence of substitutional element content as the linear relation of solid solution hardening in titanium alloys. ΔGcrit was modeled with G0 as constant and Wf as a superposition of linear chemical composition terms by fitting to the chemical driving force at the measured MS temperature of binary systems [9].

(5)

Combining Equation 1-5, the transformation-controlled yield stress at different temperatures in the stress-assisted regime can be calculated. The slip yield stress variation in the strain-induced regime was measured via tensile tests at various temperatures. The slip yield stress was found to linearly increase at about -1.5MPa/ o C in the temperature range from -80 o C to 120 o C for both Ti-5111 and Ti-64. The temperature can then be determined by the intersection of the transformation stress and the slip stress as functions of temperature.

## Transformation Dilatation Model

As quantified in previous steel research, transformation toughening effect is sensitive to martensitic transformation dilation. In order to calculate the transformation dilatation for TRIP alloy design, room temperature molar volumes of β, α', and α" phases were modeled as functions of chemical composition in the CALPHAD framework with literature data and supplemental x-ray diffraction measurements for titanium based solid solutions [25]. The molar volume Vm was expressed as the sum of a linear mixture of pure elements and regular-solution interaction terms as represented in Equation 6, where xi is the molar fraction of component i, Vi is the component volume, and Ωij is the interaction parameter.

# (6)

The transformation dilatation δ can then be calculated by Equation 7. The stable martensitic structure is predicted to be the phase with a smaller molar volume. Due to scatter of lattice parameter measurements, the relative uncertainty is about 1% associated with molar volume prediction.

(7)

## Yield Strength Model

For near-α titanium alloys without strengthening precipitates, solid solution strengthening and intrinsic yield strength of α and β phase dominate overall room temperature yield strength (~90% of the value in β processed Ti-64 [26]), while microstructure has a small contribution. Thus, it is reasonable to predict yield strength as a function of composition only based on solution strengthening. The yield strength model (Equation 8) in this work was developed using strength-composition data of annealed low alloyed binary systems [27]. Oxygen solution strengthening was taken from [28].

(8)

## Preventing Detrimental Phases

Continuous GB-α decreases fracture toughness in titanium alloys. When cooling from the β phase region with a small undercooling, α phase nucleates preferentially on β grain boundaries forming a continuous α layer. Temperature-timetransformation (TTT) diagrams of three β titanium alloys have shown that GB-α is most likely to form at 100-200 o C below β transus [29]. In order to inhibit GB-α formation, β to α transformation should be slowed before intragranular α plates become dominant. In this design, coarsening rate constant was calculated to control the kinetics of GB-α formation. For multicomponent systems, the Morral and Purdy normalized coarsening rate constant (KMP) can act as an indicator of transformation kinetics for α precipitates in a β matrix [30]. The constant is defined in Equation 9, where σ is α/β interfacial energy, Vm is molar volume, is the difference in equilibrium composition of element i across a α/β interface, D is the matrix of diffusivities in the β phase and i,j,k go through all alloying elements except the solvent. The calculations of normalized KMP were performed at 150 o C below the β transus using the MADE design software by QuesTek Innovations LLC with Ti-DATA-v3 (also named TTTI3) thermodynamic database by Thermotech Ltd. and the TIMOB12 mobility database [10]. The rate constant KMP of a designed alloy was kept the same order of magnitude as that of Ti-5111 at the aging temperature.

# (9)

In addition to GB-α, Ti3Al, an intermetallic compound of D019 structure (ordered HCP), is also known to cause embrittlement. To avoid this phase, the final aging temperature is kept higher than the Ti3Al solvus temperature calculated by ThermoCalc with the TTTI3 database.

## Computational Design Integration

With subsystem models developed, the models are integrated with the CALPHAD tools to devise an optimal composition meeting all property objectives. The integrated computational design process is represented in Figure 2  After a series of trial calculations, a composition design space satisfying all design requirements and constraints can be defined. Final optimization within the composition design space was undertaken by cross-plot parametric design to identify the alloy composition representing the best compromise of different design objectives. An example of a cross-plot for a prototype alloy Ti-8111Fe design is presented in Figure 3 

# Experimental Calibration and Validation

The proposed models for martensitic and dilatations were calibrated by key experiments using advanced techniques such as atom probe tomography (APT), synchrotron high energy x-ray diffraction (HEXRD) and tensile tests at various testing temperature. The schematic of Figure 4(a) presents the experimental calibration flow for the transformation stability model.

The accuracy of prediction depends highly on the accuracy of CALPHAD databases. The calculated chemical and critical driving force were likely overestimated because of overestimation of β to α" transformation enthalpy change by treating α" as α' in TiGen database. A calibration of ΔGcrit and ΔGchem was carried out with tensile measurements in Ti-1023 alloy [24], defining the transformation yield stress.

Transformation stability of a dispersed phase is not only dependent on its chemical composition but also microstructural features such as particle size due to the statistical nature of heterogeneous nucleation. Experimental investigation on retained β stability dependence on size was undertaken with the Ti-64 alloy.

(ut) measurement by the Bolling-Richman single specimen technique [31] showed that size had limited impact on transformation stability. However, APT microanalysis revealed that the composition of retained β plates had strong size dependence likely due to capillarity in the Ti-8111Fe prototype alloy, for which a correction term of predicted β composition may need for ΔGchem.

Unlike the 3-4% level in steels, the martensitic transformation dilatation is typically less than 1% in titanium alloys, which is comparable to the uncertainty of current molar volume model [25]. The comparison between prediction and measurement of molar volume for α" and β is shown in Figure 4(b). The accuracy of the current model is partly limited by experimental uncertainties. HEXRD measurement of lattice parameters for composition of interest is ongoing for further calibration for much improved accuracy of the dilatation prediction. 

# Conclusion

A CALPHAD based computational systems design framework for near-α TRIP titanium alloys was established. Predictive models of martensitic transformation stability, transformation dilatation, yield strength prediction and detrimental phase inhibition, were developed and integrated for parametric design optimization to achieve property objectives. Proposed models were calibrated with key experiments and prototype alloy validation is underway.

# Acknowledgements

The authors thank funding from US Office of Naval Research through Cyberalloys 2020: Naval Materials by Design Project (Contract No. N000141612400), coordinated by Dr. William Mullins.

