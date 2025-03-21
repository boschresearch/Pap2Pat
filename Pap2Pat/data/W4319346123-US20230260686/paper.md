# INTRODUCTION

Driven by the decarbonization and clean energy transformation around the world, the global demand for electrified vehicles (EVs) is predicted to grow rapidly. 1,2 NdFeB permanent magnets (PMs) are commonly used in the EV traction motors. They contain rare earth elements of Nd, Pr, Dy, Tb, which are susceptible to price volatility and supply chain vulnerability. On the other hand, emerging research in developing novel lower-cost PMs without rare earth elements hasn't surpassed the performance of commercial NdFeB.

Since 2012, GE Research has explored an alternative approach to develop a soft magnetic dual phase laminate material ("dual phase") coupled with novel machine design, potentially eliminating rare earth PMs. Dual phase offers the ability to locally control the magnetic saturation level and permeability in a motor laminate. By assigning the non-magnetic state to the bridges and center posts, the magnetic flux leakage is significantly reduced allowing improvements in motor efficiency, power density, or reduction in size. Dual phase also allows the decoupling of electromagnetic and mechanical design, opening up the design space for advanced electric machines. The key metallurgical mechanism is the nitrogen induced phase transformation from ferritic phase (magnetic) to austenite phase (non-magnetic). 3 Starting with a ferritic phase, the laminate is coated with a nitrogen stop-off mask at the regions where magnetic properties should be maintained. A high-temperature

# ARTICLE

scitation.org/journal/adv solution/gas nitriding heat treatment is applied to diffuse nitrogen gas into the bare regions, turning ferrite into austenite when nitrogen content is sufficiently high. The other emerging material that allows a monolithic structure to tune magnetic/nonmagnetic state is Hitachi Metal's bi-state magnetic laminate. [4][5][6] That invention utilized a different metallurgical mechanism to dissolve carbides in a magnetic region by localized laser heating, which transforms ferrite into austenite phase by carbon stabilization. From 2012 to 2015, GE's dual phase was advanced from Technical Readiness Level (TRL) 1 to 3 through computational alloy design, proof of concept nitriding trials, lab-scale laminate processing feasibility, and magnetic and mechanical property evaluation. Subsequent research was focused on further maturing TRL from 3 to 6 in 2016 to 2020 through laminate scale up trials, fabricating and testing a subscale 3.7kW and a full-scale 30kW synchronous reluctance motor prototype. A 25% increase in peak power density and 7% efficiency increase was validated in the subscale prototype using a dual phase rotor without PMs compared to an electrical steel motor. 7,8 The present work summarizes the development of dual phase, manufacturing trials, and full-scale 30kW motor prototype demonstration.

## ALLOY DEVELOPMENT

The success criteria of dual phase alloy design included the ability to maintain magnetic properties of a coated region while transforming bare regions to the non-magnetic state and identifying a practical solution nitriding window while obtaining desirable saturation magnetization and coercivity in the magnetic region. Initial alloy design approaches were based on a Schaeffler diagram [Fig. 1(a)] for steels, an empirical relationship between the existing phases and their compositions in Ni equivalence (austenite stabilizing elements) and Cr equivalence (ferrite stabilizing ele-ments). Several alloy compositions were designed for transformation to austenite through the introduction of nitrogen. The open symbols represent nitrogen-free alloys that mostly reside in the ferrite and/or martensite phase fields to ensure ferromagnetism. The closed symbols represent the same alloy compositions with the addition of 0.9 wt.% nitrogen, raising the Ni equivalence to the point where the material becomes austenite. A computational thermodynamics, kinetics and experimental study of these compositions was performed to select a preferred composition and a solution nitriding process window that resulted the most favorable balance of properties. Thermo-Calc was used to calculate the equilibrium phases at solution nitriding temperatures, while DICTRA was used to estimate the minimum nitriding time required to fully diffuse nitrogen through the laminate thickness. Guided by the computational results, solution nitriding trials were performed with 0.25mm thin sheets. The down-selected alloy experimentally proved dual phase capability in the predicted solution nitriding temperature/time window [Figs. 1(b) and 1(c)]. The masked region maintained its magnetic properties, indicating that the stopoff mask and heat treatment did not introduce any degradation of performance.

## MAGNETIC, MECHANICAL PROPERTIES

Table I compares the magnetic and mechanical properties of GE dual phase with two major categories of commercial soft magnetic materials frequently used in electric machines (HF10 and Hiperco50HS) and Hitachi Metal's bi-state laminate material. DC and AC BH curves and core loss data were measured on stack and bonded ring cores per ASTM A773/A773M and A772/A772M. The core loss of dual phase lies between that of HF10 and Hiperco50HS, while Hitachi material has significantly higher core loss possibly  due to the dispersed carbides in the ferritic matrix that pin magnetic domain walls and increase hysteresis loss. Electrical resistivity of dual phase is similar to that of silicon steel (∼50μΩ.cm), suggesting that higher core loss than silicon steel is attributed to its higher hysteresis loss. In terms of strength capability, the magnetic phase of dual phase reaches similar yield strength as HF10 and the non-magnetic phase has similar stress capability as Hiperco50HS.

While the bridges and center posts in various machine topologies have the highest flux leakage, they also share high stress localization. Therefore, the unique benefit of the high strength capability in the non-magnetic phase is especially advantageous. The nitrogen content in the non-magnetic phase of dual phase was found to contribute to the mechanical strength, which is consistent with literature. 9 In contrast, the Hitachi material exhibits higher yield strength in the magnetic phase than the non-magnetic phase. Its strength in the non-magnetic phase is relatively low and comparable to HF10, which may limit its application in high-speed machines.

Both the Hitachi material and GE's dual phase alloy show 1.5T saturation flux density, lower than commercial single phase electrical steels.

As many motors have a max operating temperature of 180 ○ C (limited by insulation materials), the thermal stability of dual phase was also evaluated. After being exposed in air at 180 ○ C for 5000 hours, magnetic and non-magnetic regions maintained the same properties. The transition region between the magnetic and nonmagnetic regions as a result of nitrogen diffusion grew from 100μm to 200μm after this thermal exposure. Having a low saturation magnetization value, the expansion of the transition region was further verified by electromagnetic analysis to have a negligible impact on the motor performance.

## LAMINATE MANUFACTURING TRIALS

A scalable dual phase laminate manufacturing route was developed in collaboration with multiple US manufacturers, as displayed in Fig. 2. In order to generate a dual phase laminate, the addition of three processes (application of a stop-off mask coating, solution nitriding, and coating removal) within the existing manufacturing route of electrical steels is needed. To demonstrate the scalability of this technology, ∼1000lbs of dual phase sheet with a thickness FIG. 2. Dual phase laminate processing route for motor prototype. The inset with dash line shows the saturation magnetization mapping of a randomly selected full-scale rotor laminate.

# ARTICLE

scitation.org/journal/adv of 0.25mm and width of 280mm was produced within industry standard specifications of composition range, surface finish, and thickness tolerance. A durable heat treatment fixture was designed for batch processing of up to 240 laminates per solution nitriding run. Stop-off mask coating and removal methods were modified to improve manufacturing efficiency. Sensitivity of the processing variables as well as impact on the material properties and motor performance was investigated. Residual magnetization in the nonmagnetic region was present due to process variations, but motor performance simulations suggested that a saturation magnetization of up to 0.5T would cause no harm on torque output. Lower than expected saturation in the magnetic region had a significant impact on torque output and required stringent control in the mask coating parameters. The masking and removal processes were also optimized to minimize the introduction of residual stress due to coating thickness variation and mechanical removal. Figure 2 inset shows an excellent control of saturation magnetization in the magnetic and non-magnetic regions in a randomly selected full-scale rotor laminate.

## PROTOTYPE DESIGN, FABRICATION, AND TESTING

A 55kW peak power 8-pole synchronous reluctance motor was designed and fabricated to verify the efficacy of the dual phase material. A 2-layer, 8-pole design, rated for 55kW peak and 30kW continuous power with 300mm stator outer diameter and 70mm stack length was selected based on detailed finite element analysis (FEA). The base and top speeds are 2800rpm and 14 000rpm, respectively. A power density of 5.86 kW/L is predicted, with 1.87 kW/kg specific power. The FEA plots of flux density at different operating conditions are shown [Figs. 3(a) and 3(b)]. Rotor stress analysis was performed based on maximum interference and maximum speed target (14 000rpm) to ensure an adequate interference pressure between rotor core and the shaft.

The motor prototype was fabricated, as shown in Fig. 2. Measurements on the prototype were conducted over an operating voltage range between 300 and 450Vdc and a speed range between 500 and 12 000rpm with a maximum per-phase current of 400A rms. The current angle is regulated to operate the motor at the maximum torque per ampere at each speed. The 3-phase input voltage, current, and temperatures were measured at each operating speed, and the power output, power factor, and efficiency were derived.

The tests showed that the measured continuous power output meets the design target of 30 kW at the speed range between 2800 and 8000 rpm [Fig. 3(c)]. The shaft torque also meets the target at speeds up to 8000 rpm. The maximum measured efficiency is 94%, which meets the FreedomCAR 2020 advanced traction motor target of 94-96% [Fig. 3(d)]. The causes for the discrepancy between the predicted (56.2kW) and measured peak power (41.7kW) outputs were investigated by scrutinizing both the experimental data and simulation methods. Two reasons were found to be responsible: differences between the measured and simulated properties of the HF10 steel used for the stator core and lower saturation flux density, magnetic permeability, and core loss of the dual phase than the ones used in the original design. The dual phase data used in the original design was measured on a ring-shaped specimen that underwent a lab scale processing procedure, which was explored but not achieved in a production environment.

In order to establish the benefits of the dual phase material, a synchronous reluctance motor applying a single phase magnetic material (HF10) for the stator and rotor cores was designed to obtain the same peak power of 55kW at 2800rpm. It was found that this motor was unable to maintain the power at 14 000rpm. This  

### ACKNOWLEDGMENTS

The work was financially supported by the Department of Energy, Office of Energy Efficiency and Renewable Energy, Vehicle Technology Office, under Award Number DE-EE0005573 and DE-EE0007755.

### DATA AVAILABILITY

The data that support the findings of this study are available from the corresponding author upon reasonable request.

# ARTICLE

scitation.org/journal/adv limitation can be mitigated by lowering the number of poles. However, a design with a lower number of poles leads to higher flux per pole and requires larger and heavier magnetic cores (Table II).

In contrast, dual phase enables a light-weight motor which can be designed to maintain the power over a wide speed range.

## SUMMARY AND FUTURE DEVELOPMENT

Dual phase soft magnetic material was developed with balanced magnetic and mechanical properties that offered a new degree of freedom in decoupling electromagnetic and mechanical design of advanced electric machines. Laminate manufacturing trials and superior performance in a 30kW motor prototype without using PMs were successfully demonstrated.

To broaden the applications in various electric machine topologies, future development of dual phase involves increasing saturation flux density (by composition and process modification), reducing core loss for higher power output, efficiency, and lower operating temperature, enhancing mechanical strength for higher rotation speed. Further simplification and tighter control of the masking and removal processes are highly desired. Market adoption in adjacent industrial sectors (Oil & Gas, HVAC, power generation, Aerospace) will likely help increase the demand and production volume and thus lower manufacturing cost.

## AUTHOR DECLARATIONS

### Conflict of Interest

The authors have no conflicts to disclose. 

