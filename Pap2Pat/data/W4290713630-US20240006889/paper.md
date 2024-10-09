# I. INTRODUCTION

P ERMANENT magnet synchronous generators (PMSGs)   have been the preferred choice for offshore wind energy harvesting systems due to their higher torque density, increased efficiency, improved reliability, and better fault ride through capability [1]- [3]. AC-DC converters are needed to interface between the variable-voltage variable-frequency type output of the PMSGs and a constant dc network. A diode bridge rectifier is the simplest ac-dc converter with high efficiency. However, it cannot regulate the output dc voltage. Therefore, it requires additional dc-dc converters with inversely proportional relationship between the dc-dc converter gain and wind speed. This increases the voltage and current rating of the semiconductor devices, thereby increasing the switch volt-ampere (VA) rating and the conduction losses. A conventional two-level six-switch converter, suitable for low-voltage applications, can regulate both the output dc-link voltage and the input power factor. Neutral-point-clamped and flying-capacitor-based converters are used for medium-voltage (MV) applications [4], [5]. However, a neutral-point-clamped converter requires an excessive number of clamping diodes as the number of levels increases, which results in higher conduction and switching losses. In addition, the problems of dc-link voltage balancing and uneven distribution of losses among the semiconductors limit their capability. The flying-capacitor-based topologies require a large number of clamping capacitors, which are costly and prone to failure. The reduced-switch multilevel rectifiers proposed in [6]- [8] are suitable for MV generators in an offshore wind energy conversion system. However, all these converters process full power, thereby increasing their cost, complexity, and conversion losses.

An integrated generator-rectifier topology has been shown to be one of several promising alternatives for harvesting energy from offshore wind [9]- [11]. In this topology, a turbine is connected to a multiport PMSG. Each port of the PMSG is connected to either a passive or an active rectifier, as shown in Fig. 1(a). The dc outputs of these rectifiers are then connected in series to form a dc link. This type of connection is shown to curtail the amount of power processed by the active rectifier. The reduction in active rectification, along with eliminating passive rectifier bulky filter capacitors by phase-shifting the generator back electromotive forces (EMFs), improves overall system efficiency, power density, and reliability.

The use of dc collection networks to harvest energy from an offshore wind farm is an emerging trend. This is attributed to the replacement of low-frequency transformers by medium-frequency transformers, which significantly reduces size, weight, and cost of the overall system. Previous approaches in the literature have investigated 1) the use of a medium-voltage dc (MVDC) collection grid within the wind farm followed by an MV-to-high-voltage (HV) conversion stage in the offshore substation [12]- [15] or 2) a substationless architecture where the dc outputs of several wind turbines are connected in series to form the high-voltage dc (HVDC) [16]- [27]. Thus, an open question remains: how do we interface the integrated generator-rectifier topology to an MVDC or HVDC grid? A conventional solution could be to connect an isolated dc-dc converter at the integrated generator-rectifier output to interface the dc grid, as shown in Fig. 1(a). In this approach, the active rectifier dc-link voltage (V act ) remains unregulated and increases with the decrease in PMSG speed. This article proposes a grid interface architecture using an additional isolated dc-dc converter, as shown in Fig. 1(b), which directly regulates the active rectifier voltage, further reducing the switch VA rating of the overall architecture by 14%. The key contribution of this article is an analytical framework for designing the system so that the required VA rating is minimized. The reduction in the VA rating requirement translates into overall loss reduction ranging between 28% and 72%, depending on the extracted power. The additional dc-dc converter processes a maximum of 7.6% of the total power. A maximum power point tracking (MPPT) algorithm is proposed based on the relationship between the active rectifier d-axis current and generated power. An active rectifier dc-link voltage controller design is also presented.

While there are various isolated dc-dc converters including dual-active-bridge (DAB), single-active-bridge (SAB), seriesresonant converter (SRC), and full-bridge (FB) [15], [19], [20], [23] that can be used to create the proposed grid interface, this article uses an FB topology. The DAB and SRC topologies require active switches on both sides of the medium-frequency transformer, which is redundant for unidirectional power flow applications, such as a wind energy system [15]. Both the input and the output of DAB, SAB, and SRC are capacitive. Therefore, these voltages must be regulated to prevent unequal power sharing among the converters when multiple converters are used with their inputs in parallel and outputs in series [19]. This power-balancing scheme requires a complicated control strategy involving a large number of sensors. Furthermore, the active switches, gate driver components, auxiliary power supplies, capacitors, and sensors on the secondary side of the medium-frequency transformer in the DAB, SAB, and SRC topologies require HV insulation [15], [16]. An FB converter topology eliminates all these shortcomings due to its characteristic features such as input is connected to a voltage-source, its output behaves like a current source, and there are no active switches and capacitors on the secondary side.

The rest of this article is organized as follows. Section II presents an integrated generator-converter architecture for the offshore wind energy system, which reduces the number of active switches and capacitors. A design framework to optimize the total switch VA rating requirement in the architecture is presented next. The advantages of the proposed topology are shown by an example in Section III. An MPPT algorithm using the proposed topology is developed in Section IV. The effectiveness of the proposed converter architecture and its control strategy are verified by simulation and experimental results in Sections V and VI, respectively. Finally, Section VII concludes this article.

# II. SYSTEM DESIGN

The proposed generator-converter architecture comprises a six-switch two-level active rectifier along with several passive diode bridge rectifiers and two isolated dc-dc converters, as shown in Fig. 1(b). The PMSG has k three-phase ac ports, of which one is connected to the active rectifier and the remaining are connected to the passive diode bridge rectifiers. The rectifier outputs are serially stacked to form an intermediate dc link, V dc . Two isolated dc-dc converters-Converters I and II-act as interfaces between the rectifier outputs and the dc grid. Converters I and II have transformer turns ratios 1:n 1 and 1:n 2 , respectively. Converter I takes power from V dc while operating at a fixed duty ratio of 0.5, resulting in an input-output voltage conversion ratio of (1:n 1 ). Choosing a fixed duty ratio of 0.5 ensures the maximum utilization of all the switches and the transformer, thereby resulting in a minimum number converter modules and/or input voltage requirement for a given grid voltage. Moreover, operating Converter I with the fixed duty ratio reduces the control complexity and the number of sensors. Converter II is connected to the active rectifier output (V act ) while operating with a controllable duty ratio (d), resulting in a conversion ratio of (1:2 d n 2 ). The two dc-dc converter outputs are serially stacked to connect the dc grid, V grid , through an inductor, L grid .

The design objective is to minimize the sum of VA rating of all the active switches used in the entire architecture, including the active rectifier as well as the isolated dc-dc converters. The design variables are the number of ac ports k and voltage conversion ratios of the dc-dc converters n 1 and 2 d n 2 , while the turbine operates over a speed range of 0.55 to 1 p.u., similar to that of doubly-fed induction-generator-based wind-energy conversion systems [28]. In the following subsections, the voltage and current ratings of individual converters are determined as functions of the design variables.

## A. Active Rectifier Output Voltage as a Function of Design Variables

The maximum active rectifier output voltage determines the switch voltage rating of the active rectifier and Converter II. The generator EMF is proportional to its rotational speed, and the peak line-to-neutral induced EMF of each port is expressed as

where E 0 is the sum of the EMFs for all the generator ports at rated speed ω 0 and ω is the normalized generator speed.

Neglecting the generator winding resistance and the diode voltage drop, the dc output voltage of each passive rectifier is

where L is the generator synchronous inductance and I dc,1 is the diode rectifier output current averaged over a fundamental period, as shown in Fig. 1(b). The passive rectifiers are assumed to be operated in Mode I with the commutation angle less than π/3 [9], [29]. In this mode, three out of six diodes conduct during the commutation interval and the input-output voltage relationship follows (2). Passive rectifiers in this architecture are the line-commutated rectifiers operating at ac fundamental frequency. Hence, the maximum blocking voltage of these diodes is equal to the peak of the line-to-line voltage, i.e., √ 3E ω . As Converters I and II operate with voltage conversion ratios of 1:n 1 and 1:2 d n 2 , respectively, the dc grid voltage is

where V act is the dc output voltage of the active rectifier. At rated generator speed, the controllability of the active rectifier requires

Operating the active rectifier at its minimum controllable output voltage and Converter II with duty ratio d = 0 ensures that minimum power is processed by the active rectifier at the rated speed. Using (2) and ( 4), (3) can be expressed as

) where I dc,1,0 = I dc,1 at rated generator speed. This equation gives the required transformer turns ratio of Converter I, n 1 , as a function of k. To follow this grid voltage, V grid , at all the operating speeds, the variation of active rectifier dc-link voltage with ω and d can be calculated from ( 3) and ( 5) as

where n = n 2 /n 1 . Equation ( 6) highlights that the active rectifier dc-link voltage depends on the generator speed ω, number of ports k, and the duty ratio of Converter II, d.

## B. Active Rectifier Input Current as a Function of Design Variables

The maximum active rectifier input current determines the active rectifier's switch current rating. Assume that the active rectifier is lossless and operating at unity power factor gives

where P act is the power processed by the active rectifier, I ac is the peak ac line current, and I dc,2 is the current drawn by Converter II averaged over one fundamental period, respectively. I dc,1 and I dc,2 can be expressed in terms of the dc grid current, I grid , following the conversion ratio of the corresponding dc-dc converters as

Using ( 1) and ( 8) in (7) yields

In a wind energy system, maximum power extraction at different wind speeds is achieved by delivering power to the grid following a cubic relationship with ω. For a constant grid voltage, this relationship results in

where C MPP is a proportionality constant. Equations ( 10) and ( 9) result in

## C. Normalization

The next step is to normalize ( 6) and (11) to make this design procedure independent of actual values of V grid , E 0 , ω 0 , and rated power. Using current and voltage base values as respectively, the normalized active rectifier output voltage is

where L pu is the generator synchronous inductance normalized by L base = V base /k ω 0 I base . Similarly, the normalized active rectifier input current is

Using ( 13) in ( 14) yields

This equation shows that the normalized active rectifier input current is independent of n and d. Assuming L pu as 0.05, Fig. 2 illustrates the variation of I ac,pu with ω for different numbers of ac ports k.

## D. Minimization of the Total Switch VA Rating

The total normalized switch VA rating of the proposed converter topology is VA total,pu = VA ConvI, pu + VA Conv II, pu + VA act, pu (16) where VA Conv I, pu , VA Conv II, pu , and VA act, pu are the normalized VA ratings of Converter I, Converter II, and the active rectifier, respectively. Converter I consists of four active switches; therefore, its total switch VA rating is as grid current is maximum at rated speed, ω = 1. Using ( 5) in ( 17) followed by normalization results in

Converter II consists of four active switches as well. Therefore, its total switch VA rating is

Normalizing this equation yields

where V act, pu is obtained from (13). Similarly, the normalized switch VA rating of the two-level six-switch active rectifier can be obtained as

As the design objective is to minimize the total normalized switch VA rating, the optimization is expressed as

For k ac port, solving this optimization results in

n 1 is computed from (5) and the optimum transformer turns ratio for Converter II, n 2,opt = n 1 n opt,k . Variations of n 1 and n 2,opt as functions of the number of ac ports are shown in Fig. 3. Fig. 4 shows the minimum switch VA rating requirement as a function of k. Three design points are highlighted in the figure to illustrate the advantage of the proposed architecture. Point A refers to the design architecture with only one generator ac port that is connected to an active rectifier followed by a grid-tied fixed-duty dc-dc converter. The total switch VA rating requirement for this design case is 10.93 p.u. Point B refers to a design architecture, where the output of a five-port integrated generator-rectifier proposed in [9] is connected to a grid-tied fixed-duty dc-dc converter. In this case, the required total switch VA rating is 7.48 p.u. Finally, point C refers to the proposed grid interface with a five-port integrated generator-rectifier, where the two dc-dc converters, Converters I and II, work together to reduce the total switch VA rating to 6.42 p.u.

The substantial reduction in the total switch VA rating can be predominantly attributed to the reduction in the active rectifier dc-link voltage rating. With the optimized design for a five-port generator, Fig. 5(a) shows the allowable duty ratio d for Converter II. The d max line signifies the lowest bound of the active rectifier voltage required to maintain desired power flow control. However, operating along the d min line ensures that the active rectifier output voltage remains constant and equal to its value at the rated speed. Operating Converter II within this region guarantees that the maximum of the active rectifier output voltage remains at 0.2 p.u. independent of the speed, as shown in Fig. 5(b). In contrast, the absence of Converter II increases the voltage to 0.51 p.u., resulting in an increase in the switch VA rating. Therefore, for a five-port system with n 2 = n 2,opt , the active rectifier voltage rating is reduced by 60.7% in the proposed architecture.

# III. DESIGN EXAMPLE

This section illustrates the improvements of the proposed dc grid interface by a design example. A 10-MW wind-turbinedriven multiport PMSG is considered [30]. At the rated rotational speed of 9.6 r/min, each generator port is assumed to generate a line-to-line rms voltage of 415 V with a frequency of 19.2 Hz. One active and four passive rectifiers, along with two isolated dc-dc converters, are connected as proposed to create a module. Twenty such modules are stacked in series to connect the wind turbine output to a 66-kV dc grid through a 10-mH inductor, as shown in Fig. 6.

The synchronous inductance of the PMSG is chosen to be 1.3 mH, which is 0.05 p.u. The ratings and parameters of the system are tabulated in Table I. Based on the above ratings and parameters, n 1 and n 2,opt are calculated as 1.215 and 1.87, respectively. The required voltage and current ratings of the  semiconductor devices can be calculated following the design steps discussed in Section II. The devices are then selected with reasonable safety factors, as tabulated in Table II. The conventional dc grid interface architecture where Converter II is absent is also designed for comparison. The total switch VA rating for the conventional architecture is 15.41 × 10 6 VA, whereas it is reduced to 11.9 × 10 6 VA (a saving of 22.8%) with the proposed one. The analytical results, as shown in Fig. 4, indicate a saving of 14.2% in switch VA rating requirement for a five-port system. This difference between the analytical results and the design example is due to the nonavailability of devices with exact required ratings. In addition, a reduction in the switch VA rating translates into the improved system efficiency. The detailed loss analysis of the conventional and proposed dc grid interfaces is illustrated in the Appendix. This generalized design framework for the converter architecture is independent of the type of the devices used. Though insulated gate bipolar transistors (IGBTs) have been used in this example, a similar analysis can be performed using silicon carbide devices.

The proposed topology is compared with the conventional dc grid interface in terms of the losses within the individual converters, as shown in Fig. 7. The continuous lines in these figures indicate the results obtained from the analysis in the Appendix, whereas the dot points are from a PLECS simulation. The losses within the active rectifier in the proposed topology are substantially reduced. This is due to the use of low-voltage devices for the active rectifier and its regulated dc-link voltage. The architectures are also compared in terms of the total conversion losses in normalized values based on (54) in Fig. 8. The conversion loss is reduced due to the proposed architecture by 28.3% at the rated speed and 71.7% at the minimum speed. The difference in the results obtained from the simulation and the analysis is primarily due to the way the device characteristics  have been captured in the loss model. In the PLECS simulation, multiple data points have been used, whereas curve-fitting equations were used in the analysis, as explained in the Appendix.

# IV. CONTROL STRATEGY

This section develops the control framework for the proposed architecture. The system output is assumed to be connected to a stiff dc grid. A switching cycle average model of the system is shown in Fig. 9. The passive rectifiers are modeled as a generator-speed-dependent voltage source in series with an impedance representing the voltage drop due to commutation. The active rectifier is modeled as a controllable current source in parallel with a capacitor. Converters I and II are modeled as dc transformers with their voltage conversion ratio (1:n 1 ) and (1:2 d n 2 ), respectively.

Out of the four distinct converters in the proposed architecture, the generator-side passive rectifiers and Converter I, which is operated at a constant duty ratio of 0.5, do not actively regulate any system variables. The generator-side active rectifier controls the power harvested from the wind and Converter II regulates its input voltage v act . Control laws and a design framework for the controller parameters are developed as follows.

## A. Active Rectifier Control

The MPPT ability is achieved if the generated power follows the optimum cubic relationship

where C p,mpp is a constant and can be obtained from the wind turbine characteristic. The active rectifier processes a part of the generated power given by

assuming the active rectifier to be lossless, and E sd and I sd are the d-axis components of the generator-induced EMF and current vectors, respectively. The d-axis is considered to be aligned with the generator-induced EMF vector. Therefore

And the power processed by all the passive rectifiers is Based on ( 2) and ( 24)-( 27), the active rectifier input current should follow the below equation to ensure MPPT:

This equation is used to create the reference value for the d-axis current. The dand q-axis current controllers are designed and implemented following the procedure mentioned in [9]. A block diagram of the active rectifier control strategy is shown in Fig. 10.

## B. Converter II Control

The switch duty ratio of Converter II (d) is used to control the active rectifier dc-link voltage V act following (6), which can be expressed in

where

is constant at some operating point ω = ω op . Considering slower dynamics of the wind speed and the rotational speed as compared to that of the active rectifier dc-link voltage, the small-signal model of ( 29) is

where V act,0 and d 0 are the steady-state values of V act and d, respectively, around which the system is perturbed and Δv act and Δd are the corresponding perturbed quantities. The active rectifier dc-link voltage controller, whose output is the duty ratio d of Converter II, can be designed based on the small-signal model ( 31). An integrator-type controller gain (K iv ) can be designed as

where ω BW,v is the desired bandwidth of the active rectifier dclink voltage controller. The control block diagram of Converter II is shown in Fig. 10.

# V. SIMULATION RESULTS

This section illustrates the performance of the proposed integrated generator-converter architecture and its control for the 10-MW offshore wind energy harvesting system. The ratings and parameters of the simulated system are tabulated in Table I.

## A. Steady-State Results

The steady-state simulation results compare the proposed dc grid interface topology with the conventional one, where Converter II is not used. Fig. 11 illustrates that the inclusion of Converter II in the proposed topology does not influence the active rectifier current. Fig. 12(a) shows that the active rectifier voltage increases to 1501 V as speed reduces to its minimum value, 5.28 r/min (i.e., 0.55 p.u. of 9.6 r/min), for the conventional topology, whereas this voltage remains fairly constant at 588.7 V in the proposed one. Therefore, the voltage rating of the active switches in the active rectifier of the proposed topology is 2.55 times less than that of the conventional topology. Fig. 12(b) illustrates that the maximum value of the intermediate dc-link voltage V dc is equal (2730 V) for both the conventional and the proposed topologies, indicating equal voltage rating of the active switches in Converter I for both the topologies. However, V dc remains fairly constant throughout the operating range for the conventional topology, whereas in the proposed topology, it decreases with the speed. Operating at a lower voltage moderates the failure rate of the switches and, hence, improves the proposed system's reliability [31].

Fig. 13 illustrates the power processed by different converters in one module of the conventional and proposed topologies. Fig. 13(a) shows that the active rectifier processes an equal amount of power for both the topologies. The maximum power processed by the active rectifier in a module is 112.5 kW, which is about 22.5% of the total power, and the rest, 77.5%, of the active power is processed by the passive rectifiers. Fig. 13(b) shows that a fraction of the total power is processed by Converter II in the proposed topology. The maximum power processed by Converter II in a module is 38 kW, which is 7.6% of the total power.

## B. Dynamic Results

Figs. 14 and 15 illustrate the maximum power point (MPP) tracking ability of the proposed power electronics and control systems. To reduce the simulation time, the inertia constant is chosen to be 5.74 × 10 6 kg•m 2 , which is 250 times less than that of a reference design [32]. At t = 2 s, a step change of wind speed from the rated 12 to 6.6 m/s is applied; this changes the PMSG rotational speed from its rated value of 9.6 to 5.28 r/min (i.e., 0.55 × 9.6 r/min) and the generator output power from its rated value of 10 to 1.67 MW [i.e., (0.55) 3 × 10 MW]. At t = 5 s, the wind speed goes back to its rated value and so do the PMSG rotational speed and generator output power. Fig. 15 shows the dynamics of several electrical quantities corresponding to the wind speed transients shown in Fig. 14(a). The dc grid current varies from 151.5 to 25 A and again back to 151.5 A. The active rectifier ac current magnitude ranges between 220 and 

# VI. EXPERIMENTAL RESULTS

## A. Experimental Setup

A low-power laboratory prototype has been developed to validate the effectiveness of the proposed converter topology and the control strategy. A Samsung DC96-01218D permanent magnet machine was redesigned and modified to create a three-port generator [33]. Two ports are connected to passive rectifiers and the remaining one to an active rectifier. A TI HV motor control kit is used as the active rectifier in this setup. The entire setup is shown in Fig. 16. Each phase has an equivalent series resistance of 3 Ω and an equivalent series inductance of 7.5 mH, measured at 60 Hz. The machine produces a sine-wave back EMF with a back-EMF constant 0.204 V (peak line to neutral)/r/min. The generator is connected to the prime mover through a gear box with the gear ratio of 5:1. The prime mover is driven by a Kollmorgen drive in a torque control mode. The torque reference value is generated by an Arduino program, which emulates a wind turbine characteristics.  

## B. Steady-State Results

The steady-state experimental results are used to compare the proposed dc grid interface topology against the conventional one, where Converter II is not used. Fig. 17(a) illustrates that the maximum value of the intermediate dc-link voltage V dc is almost equal (131 V) for both the conventional and proposed topologies, indicating an equal voltage rating of the active switches in Converter I for both the topologies. However, V dc remains fairly constant throughout the operating range for the conventional topology, whereas it decreases with the wind speed in the proposed topology. In the analysis, transformer leakage inductance is not considered; this results in the differences between the analytical and experimental data. Fig. 17    that the active rectifier voltage increases to 73 V as the emulated wind speed falls to its minimum value, 6.6 m/s, for the conventional topology, whereas in the proposed one, this voltage can be regulated at 53 V. The variation of Converter II duty ratio with wind speed is shown in Fig. 17 Fig. 18 shows the active, passive, intermediate dc-bus, and dc grid current waveforms. The active rectifier current is sinusoidal, whereas the passive rectifier current is nonsinusoidal as expected. Fig. 19 shows the intermediate and active rectifier dc links and transformer primary voltage of Converters I and II. The oscillations observed on the transformer primary voltage are mainly due to the ringing caused by the transformer leakage inductance and the device capacitance when all the switches are turned OFF.  The duty ratio of Converter I remains constant at 0.48 throughout the operating range. The intermediate dc-link voltage, which is also the Converter I input voltage, determines the magnitude of the Transformer I primary voltage waveform. It decreases from 129.7 V at a wind speed of 12 m/s to 98.6 V at 6.6 m/s. The active rectifier dc-link voltage is maintained at 53 V. Therefore, the magnitude of Transformer II primary voltage waveform remains unchanged. However, its duty ratio increases to 0.43 at 6.6-m/s wind speed from 0.02 at 12 m/s.    changes from the rated 12 to 6.6 m/s. Thus, the PMSG rotational speed lowers from its rated value, 150 r/min, to 83 r/min (i.e., close to 0.55 × 150 r/min or 82.5 r/min) and the generator output power from its rated value, 160 W, to 20 W (i.e., close to (0.55) 3 × 160 W or 26.6 W). At t = 5.5 s, the wind speed returns to its rated value and so do the PMSG rotational speed and generator output power. 

# VII. CONCLUSION

This article presented a dc grid interface for an integrated generator-rectifier architecture for harvesting energy from offshore wind. The proposed architecture employs a multiport PMSG connected to series-stacked passive and active rectifiers followed by two dc-dc converters, as opposed to one dc-dc converter in a conventional connection. Although adding Converter II in the proposed architecture leads to more number of active switches and gate drivers, the total switch VA rating and conversion losses are substantially reduced compared to a conventional topology. Using a 10-MW illustrative design, this article shows that an additional dc-dc converter reduces the total switch VA rating by 22.8%, which translates into overall loss reduction ranging between 28.3% and 71.7%, depending on the extracted power. An analytical framework to design a system with a minimum switch VA rating is also presented. An MPPT algorithm based on the relationship between the generated power and the d-axis component of the active rectifier current is developed. The active rectifier dc-link voltage is shown to be regulated by Converter II. The analytical and experimental results validate the effectiveness of the proposed converter architecture and its control strategy. This approach opens up opportunities for integrating dc collection networks with offshore wind farms through an efficient, reliable, and cost-effective energy conversion system.

# APPENDIX LOSS ANALYSIS

The conversion losses within the semiconductors of the proposed and the conventional dc grid architectures are estimated.

## A. Diode Bridge Rectifiers

For the diode bridge rectifiers, switching loss is negligible as compared to the conduction loss as the diodes go through natural commutation. In this architecture, three-phase diode bridge rectifiers are used at the generator end, whereas single-phase bridge rectifiers are used at the dc grid side. As two diodes conduct at any time, the power loss within a three-phase passive rectifier is

where v F (i F ) is the forward voltage drop of the diode as a function of its forward current i F . The v F -i F relationship can be approximated from the device datasheet as

where V F 0 and V F N are the threshold voltage drop and the voltage drop at the rated current, I F N , respectively [34]. At the MPPs, the diode forward current in the generator-side passive rectifiers is

Equations ( 33)-( 35) are used to compute the loss within the generator-side passive rectifiers as a function of ω. The total loss within all the three-phase diode bridge rectifiers is

The forward current through the dc-grid-side diodes in Converter I is I grid . Therefore, power loss within the rectifier in Converter I is

Equations ( 34) and (37), along with (10)  The loss parameters of the rectifier diodes used in this example are obtained from the device datasheets and are presented in Table III.

## B. Active Rectifier

The conduction loss within the active rectifier is calculated following the procedures mentioned in [34] and [35]. At unity power factor, conduction loss within an active switch, P igbt,act cond and an antiparallel diodes P diode,act cond are estimated using [34, eq. ( 15)] with θ = π. Therefore, total conduction loss in the active rectifier is

Switching energy losses in the active rectifier involve three components: turn-ON (E on ), turn-OFF (E off ), and diode reverse recovery (E rec ). The device datasheet provides these energy components as functions of the operating current i C and voltage V CC . The E on and E off characteristics of the selected device can be approximated as

where E ON,rated and E OFF,rated are the turn-ON and turn-OFF energy loss at the rated operating voltage V CE,rated and current I CN , respectively. The active rectifier current i C is sinusoidal with the peak value of I ac and V CC = V act . Thus, the turn-ON and turn-OFF power losses within the active rectifier averaged over a fundamental period are P act on = 6 π F sw,act E on (I ac , V act )

where F sw,act is the switching frequency of the active rectifier. The diode reverse-recovery energy loss (E rec ) as given in the datasheet can be approximated as

(42) where the parameters a 0 , a 1 , and a 2 are obtained from a curvefitting program. The average diode reverse-recovery power loss over a fundamental period within the active rectifier is  

Table II gives the devices selected for the active rectifier in both the conventional and proposed architectures. The parameters of these devices as obtained from their datasheets are given in Table IV and are used to calculate the losses within the active rectifier.

## C. Converter I

As the duty ratio of Converter I is fixed at 0.5, a suitable design of snubber capacitance and transformer leakage inductance ensures soft switching. Assuming this, the active side of Converter I incurs only the conduction loss. Since two active switches conduct at any time, the power loss within the active side of Converter I is

where v CE (i C ) is the voltage drop of the active switch as a function of its current i C . The v CE -i C relationship can be approximated from the device datasheet as

where V C0 and V CEN are the threshold voltage drop and the voltage drop at the rated current I CN , respectively [34]. At the MPPs, the current i C is where P 0 is the output power. At MPPs, it follows that

where P rated is the rated output power.

