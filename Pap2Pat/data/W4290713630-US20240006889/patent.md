# DESCRIPTION

## FIELD

Fields of the invention includes power generation and rectification. An example application of the invention is to a wind-energy power generation system.

## BACKGROUND

Permanent magnet synchronous generators (PMSGs) have been the preferred choice for offshore wind energy harvesting systems. PMSGs have good torque density, efficiency, reliability, and fault ride through capability. AC-DC converters interface between the variable-voltage variable-frequency type output of the PMSGs and a constant dc network. A diode bridge rectifier provides high efficient ac-dc conversion but does not regulate output dc voltage. Additional dc-dc converters with an inversely proportional relationship between the dc-dc converter gain and wind speed are used to regulate dc ouptut. This approach requires high voltage and current rated semiconductor devices, which increases switch volt-ampere (VA) ratings and conduction losses.

A conventional two-level six-switch converter, suitable for low-voltage applications, can regulate both the output dc-link voltage and the input power factor. Neutral-point-clamped and flying-capacitor-based converters are used for medium-voltage (MV) applications. A. Nabae, et al., “A new neutral-point-clamped PWM inverter,” IEEE Trans. Ind. Appl., vol. IA-17, no. 5, pp. 518-523, September 1981; J. Rodriguez, S. Bernet, B. Wu, J. O. Pontt, and S. Kouro, “Multi-level voltage-source-converter topologies for industrial medium-voltage drives,” IEEE Trans. Ind. Electron., vol. 54, no. 6, pp. 2930-2945, December 2007. High conduction and switching losses are introduced by the number of clamping diodes that increase as the number of levels increases. Dc-link voltage balancing and uneven distribution of losses among the semiconductors further limit capability. Flying-capacitor-based topologies require costly and failure-prone clamping capacitors.

Reduced-switch multilevel rectifiers are suitable for MV generators in an offshore wind energy conversion system. Kolar and F. Zach, “A novel three-phase utility interface minimizing line current harmonics of high-power telecommunications rectifier modules,” IEEE Trans. Ind. Electron., vol. 44, no. 4, pp. 456-467, August 1997; D. Mukherjee and D. Kastha, “A reduced switch hybrid multilevel unidirectional rectifier,” IEEE Trans. Power Electron., vol. 34, no. 3, pp. 2070-2081, March 2019; D. Mukherjee and D. Kastha, “A minimum switch five-level unidirectional rectifier without any voltage balancing and pre-charging circuitry,” IEEE Trans. Power Electron., vol. 34, no. 12, pp. 11605-11615, December 2019. However, these converters process full power, thereby increasing their cost, complexity, and conversion losses.

One prior approach uses an MVDC collection grid within the wind farm followed by an MV to HV conversion stage in the offshore sub-station. See, C. Meyer et al, “Control and design of DC grids for offshore wind farms,” IEEE Trans. Ind. Appl., vol. 43, no. 6, pp. 1475-1482, November/December 2007; W. Chen, et al, “Analysis and comparison of medium voltage high power DC/DC converters for offshore wind energy systems,” IEEE Trans. Power Electron., vol. 28, no. 4, pp. 2014-2023, April 2013; H. Krishnamoorthy, et al, “Isolated AC-DC converter using medium frequency transformer for offshore wind turbine DC collection grid,” IEEE Trans. Ind. Electron., vol. 64, no. 11, pp. 8939-8947, November 2017; P. Hu, et al., “Modular isolated LLC DC/DC conversion system for offshore wind farm collection and integration,” IEEE Trans. Emerg. Sel. Topics Power Electron., vol. 9, no. 6, pp. 6713-6725, December 2021.

Another prior approach is a sub-station-less architecture where the dc outputs of several wind turbines are connected in series to form the HVDC. See, M. Popat, B. Wu, and N. R. Zargari, “A novel decoupled interconnecting method for current-source converter-based offshore wind farms,” IEEE Trans. Power Electron., vol. 27, no. 10, pp. 4224-4233, October 2012; S. Chuangpishit, A, et al, “Topology design for collector systems of offshore wind farms with pure DC power systems,” IEEE Trans. Ind. Electron., vol. 61, no. 1, pp. 320-328, January 2014; R. Barrera-Cardenas and M. Molinas, “Comparative study of wind turbine power converters based on medium-frequency AC-Link for offshore DC-Grids,” IEEE Trans. Emerg. Sel. Topics Power Electron., vol. 3, no. 2, pp. 525-541, June 2015; Q. Wei, et al, “A medium-frequency transformer-based wind energy conversion system used for current-source converter-based offshore wind farm,” IEEE Trans. Power Electron., vol. 32, no. 1, pp. 248-259, January 2017; Wei, B. et al, “Bipolar operation investigation of current source converter based wind energy conversion systems,” IEEE Trans. Power Electron., vol. 33, no. 2, pp. 1294-1302, February 2018; Rong, G. et al, “ALL-DC offshore wind farm with series-connected wind turbines to overcome unequal wind speeds,” IEEE Trans. Power Electron., vol. 34, no. 2, pp. 1370-1381, February 2019; M. Guan, “A series-connected offshore wind farm based on modular dual-active-bridge (DAB) isolated DC-DC converter,” IEEE Trans. Energy Conyers., vol. 34, no. 3, pp. 1422-1431, September 2019; H. Zhang, et al, “Overvolt-age limitation method of an offshore wind farm with DC series-parallel collection grid,” IEEE Trans. Sustain. Energy, vol. 10, no. 1, pp. 204-213, January 2019; G. Guo et al., “HB and FB MMC based onshore converter in series-connected offshore wind farm,” IEEE Trans. Power Electron., vol. 35, no. 3, pp. 2646-2658, March 2020; G. Guo et al., “Series-connected-based offshore wind farms with full-bridge modular multilevel converter as grid- and generator-side con-verters,” IEEE Trans. Ind. Electron., vol. 67, no. 4, pp. 2798-2809, April 2020; Y. Fu, et al, “Collection system topology for deep-sea offshore wind farms considering wind characteristics,” IEEE Trans. Energy Conyers., vol. 37, no. 1, pp. 631-642, March 2022; M. Pape and M. Kazerani, “A generic power converter sizing framework for series-connected DC offshore wind farms,” IEEE Trans. Power Electron., vol. 37, no. 2, pp. 2307-2320, February 2022. These prior designs fail to provide an interface of the integrated generator-rectifier topology to a medium voltage dc (MVDC) or high voltage dc (HVDC) grid. Some of the present inventors have advanced the state of the art with Integrated Generator-Rectifier Systems that minimize ripple. An integrated generator-rectifier topology is a good alternative to harvest energy from offshore wind. In this topology, a turbine is connected to a multiport PMSG. P. T. Huynh, P. J. Wang, and A. Banerjee, “An integrated permanent-magnet-synchronous generator-rectifier architecture for limited-speed-range applications,” IEEE Trans. Power Electron., vol. 35, no. 5, pp. 4767-4779, May 2020; P. Huynh, S. Tungare, and A. Banerjee, “Maximum power point tracking for wind turbine using integrated generator-rectifier systems,” IEEE Trans. Power Electron., vol. 36, no. 1, pp. 504-512, January 2021; P. Huynh and A. Banerjee, “Active voltage-ripple compensation in an integrated generator-rectifier system,” IEEE Trans. Power Electron., vol. 36, no. 2, pp. 2270-2282, February 2021. In these topologies, each port of the PMSG is connected to either a passive or an active rectifier. The dc outputs of these rectifiers are then connected in series to form a dc link. This type of connection limits the amount of power processed by the active rectifier. The reduction in active rectification, along with eliminating passive rectifier bulky filter capacitors by phase-shifting the generator back electromotive forces (EMFs), improves overall system efficiency, power density, and reliability.

P. Huynh and A. Banerjee, U.S. Pat. No. 11,183,946, discloses such an integrated generator-rectifier AC-DC conversion circuit and system that can include serially stacked passive and active rectifiers connected to multiple AC ports of an electrical power generator driven by mechanical energy captured by an energy harvester. The series-stacked passive rectifiers are power by multiple three-phase AC ports, each of the ports is implemented as a separate magnetic structure. While this avoids coupling between phases, each separate magnetic structure adds significant weight and significant expense.

More recently, some of the present inventors have provided another advance in the art. Banerjee et al., U.S. patent application Ser. No. 18/182,610, filed Mar. 13, 2023, and incorporated by reference herein, discloses an integrated multi-port generator-rectifier device that includes multiple passive output ports provided from a plurality of passive-rectifier windings on a common, single magnetic structure, wherein the passive-rectifier windings interact with a plurality of magnetic poles, wherein the passive rectifier windings are serially connected, wherein each of the passive rectifier windings comprises a pitch that is a fraction of magnet pole pitch and a pattern to magnetically decouple back emf phases of the separate rectifiers, the device further comprising an active port provided by an active rectifier.

## SUMMARY OF THE INVENTION

A preferred embodiment provides a generator-rectifier system and grid interface includes an active rectifier configured to accept an input from one of a plurality of ac ports of a multi-port permanent magnet synchronous generator. Passive rectifiers are connected to the others of the plurality of ac ports of the multi-port permanent magnet synchronous generator. Connections provide outputs of the active rectifier and the passive rectifiers. A first converter is controlled at a fixed duty ratio driven by the outputs to interface with a dc grid or at a low grid frequency switching waveform to create a grid frequency ac output to interface with an ac grid. A second converter is connected the output of the active rectifier, the second converter being controlled at a variable duty ratio to interface with the dc grid or an above grid frequency switching waveform to create an above grid frequency ac waveform to interface with an ac grid. Connections provide a serial stack of outputs of the first and second converters.

## DETAILED DESCRIPTION OF THE PREFERRED EMBODIMENTS

Embodiments of the present invention include an integrated generator-rectifier topology/system that can harvest energy from an energy source/system, such as offshore wing. A turbine is connected to a multi-port permanent magnet synchronous generator (PMSG). Each port of the PMSG is connected to either a passive or an active rectifier. Dc outputs of the rectifiers are connected in series to form a dc-link to reduce an amount of power processed by the active rectifier. The reduction in active rectification along with the elimination of passive rectifier bulky filter capacitors by phase-shifting the generator back electromotive forces (EMFs) improve the overall system efficiency, power density, and reliability.

Embodiments of the present disclosure include a dc-grid interface circuit between the integrated generator-rectifier topology and a medium-voltage dc (MVDC) or high voltage dc (HVDC) grid. An isolated dc-dc converter at the integrated generator-rectifier output provides an interface to the dc grid.

Preferred embodiment generator-rectifier systems and grid interfaces include an integrated multi-port generator-rectifier device as disclosed in Banerjee et al., U.S. patent application Ser. No. 18/182,610, filed Mar. 13, 2023, or an integrated multi-port generator-rectifier device as disclosed in Huynh & Banerjee U.S. Pat. No. 11,183,946. A grid-interface architecture includes an isolated dc-dc converter (or dc-ac converter) that directly regulate active-rectifier voltage, further reducing the switch volt-ampere (VA) rating of the overall architecture, e.g. by 14%. In preferred embodiments, the system is designed so that a required VA-rating is minimized. In a preferred implementation, the reduction in the VA rating requirement can provide an overall loss reduction ranging between 28% and 72%, depending on the extracted power. An additional dc-dc converter (or dc-ac converter) used processes a maximum of 7.6% of the total power.

Preferred embodiments include a maximum power point tracking (MPPT) control method based on the relationship between the active-rectifier d-axis current and generated power. Preferred embodiments include an active rectifier dc link voltage controller design.

Preferred embodiments are implemented with a full-bridge (FB) topology. Various other isolated dc-dc converters can be used, including dual active bridge (DAB), single active bridge (SAB), and series resonant converter (SRC). The DAB and SRC topologies require active switches on both sides of the medium-frequency transformer, which is redundant for unidirectional power flow applications such as a wind energy system. Both input and the output of DAB, SAB, and SRC are capacitive. Therefore, these voltages must be regulated to prevent unequal power sharing among the converters when multiple converters are used with their inputs in parallel and outputs in series. This power-balancing scheme requires a complicated control strategy involving many sensors. Further, the active switches, gate-driver components, auxiliary power supplies, capacitors, and sensors on the secondary side of the medium frequency transformer in the DAB, SAB, and SRC topologies require high voltage insulation. Embodiments using the DAB, SAB, and SRC topologies still provide advantages compared to the prior art, but an FB converter topology eliminates shortcomings of the other topologies due to inherent FB characteristics: input is connected to a voltage source, its output behaves like a current-source, and there are no active switches and capacitors on the secondary side.

Preferred embodiments include an integrated generator-converter architecture for an energy system (such as an offshore wind energy system), which reduces the number of active switches and capacitors. Preferred embodiments include a topology that can optimize the total switch VA rating requirement in the architecture.

Preferred embodiments provide an integrated generator-rectifier architecture for harvesting energy from a power source/energy system such as offshore wind. A majority of the power is processed by reliable, efficient, and inexpensive diodes operating at the generator frequency.

Embodiments include a dc grid interface circuit for an integrated-generator-rectifier and a control strategy for maximum power point tracking. In one example, using a 10MW illustrative design, it is shown that the preferred architecture reduces the total switch volt-ampere rating requirement by 22.8% which translates into overall loss reduction ranging between 28.3% and 71.7%, depending on the extracted power.

In preferred embodiments, the maximum power point tracking control method is based upon current and the generated power. Experimental results obtained from a laboratory prototype validate the effectiveness of the converter architecture and its control strategy. This approach provides opportunities for integrating dc-collection networks with offshore wind farms through an efficient, reliable, and cost-effective energy-conversion system.

Preferred embodiments of the invention will now be discussed with respect to experiments and drawings. Broader aspects of the invention will be understood by artisans in view of the general knowledge in the art and the description of the experiments that follows.

FIG. 1A shows a preferred generator-rectifier system and grid interface 100 coupled to a wind turbine 102. The turbine drives a multi-power PMSG 104 having k three-phase ac ports. One of the k ac ports is connected to an active rectifier 106. If more than one of the k ac ports is connected to the active rectifier, more power is processed actively and the benefit of the invention is lessened, but some benefit remains. The remaining k ac ports of the PMSG 104 are connected to passive rectifiers 108. Outputs of the active rectifier 106 and the passive rectifier 108 are serially stacked to form an intermediate dc link, Vac. Two isolated dc-dc converters 110 and 112—Converters I and II—act as interfaces between the rectifier outputs and the dc grid. Converters 110 and 112 can also be dc-ac converters to interface to an ac grid.

The active rectifier 106 can be a six-switch two-level active rectifier 120. The passive rectifiers 108 can include passive diode bridge rectifiers 122. In

Converters I and II have transformer turns ratios 1:n1 and 1:n2, respectively. Converter I takes power from Vdc while operating at a preferred fixed duty ratio of 0.5, resulting in an input-output voltage conversion ratio of (km). Choosing a fixed duty ratio of 0.5 ensures the maximum utilization of all the switches in the Converter I transformer, thereby resulting in a minimum number of converter modules and/or input voltage requirement for a given grid voltage. Ratios of less that 0.5 are less optimal but can be used, but provide a less efficient operating/design point for Converter I. Operating Converter I with a fixed duty ratio also reduces the control complexity and the number of sensors. Specifically, Converter I does not require circuitry to measure voltage for active voltage balancing, and does not require a closed loop controller to regulate power flow. Switching in Converter I can be implemented in a simple open-loop manner using a microcontroller without any feedback or other communications. Converter II is connected to the active rectifier output (Vact) while operating with a variable duty ratio d, resulting in a conversion ratio of (1:2 d n2). The two dc-dc converter outputs are serially stacked to connect the dc grid, Vgrid, through an inductor, Lgrid.

FIG. 1B shows a system 101 for interface to an ac grid (single-phase or multi-phase). Converter I 130 is a dc-to-ac converter and generates a six-step voltage waveform that matches the ac grid frequency. Converter II 132 is a dc-to-ac converter switched at a frequency greater than grid frequency such that the difference of voltages of the two converters contains a sinusoidal component of the ac grid voltage. A transformer 134 provides isolation and a voltage step up or step down to the ac grid as well as provides a mechanism to add or subtract voltages from two converters. FIG. 1C shows a system 103 that is similar to the system 101. In FIG. 1C, outputs of the active rectifier 106 and the passive rectifier 108 are directly connected to the respective Converter I 130 and Converter II 132. Unlike in the system 101, active power cannot circulate between Converter I and Converter II in the system 103. In the converter 101 of FIG. 1B, circulating power between Converter I and Converter II needs to be regulated by a suitable conventional control strategy. In the dc-grid system 100 of FIG. 1A circulating power is not a concern between Converter I and II because of diodes at the secondary of the transformer in Converter II. Stacking of the outputs is preferred in FIG. 1A because removing the stacking will increase the total switch volt-ampere rating.

An objective is to minimize the sum of VA (volt-amp) rating of all the active switches used in the entire architecture, including the active rectifier 106 as well as the isolated dc-dc converters 110 and 112 (Converters I and II). The design variables are the number of ac ports k and voltage conversion ratios of the dc-dc converters n1 and 2 dn2, while the turbine 102 operates over a speed range of 0.55 to 1 p.u., similar to that of doubly-fed induction-generator-based wind-energy conversion systems.

The control objective for a dc-ac conversion is the same, namely to allow Vact to remain constant across all speed and allow Vdc to vary. This permits use of a lower power rated active rectifier 108 compared to conventional approaches. Operationally, Converter I can run a six-step ac waveform, for example, and process a large majority of the power. Converter II can run a high frequency switching waveform to process the remaining power.

Active Rectifier Output Voltage as a Function of Design Variables

The maximum active rectifier output voltage determines the switch voltage rating of the active rectifier 106 and Converter II 112. The generator EMF is proportional to its rotational speed, and the peak line-to-neutral induced EMF of each port is expressed as:

\(\begin{matrix}
{E_{\omega} = \frac{\omega E_{0}}{k}} & (1)
\end{matrix}\)

where E0 is the sum of the EMFs for all the generator ports at rated speed ω0 and ω is the normalized generator speed. Neglecting the generator winding resistance and the diode voltage drop, the dc output voltage of each passive rectifier is:

\(\begin{matrix}
{V_{pas} = {\underset{V_{p}}{\underset{︸}{\frac{3\sqrt{3}}{\pi}E_{\omega}}} - \underset{V_{x}}{\underset{︸}{\frac{3}{\pi}{\omega\omega}_{0}{LI}_{{dc},1}}}}} & (2)
\end{matrix}\)

where L is the generator synchronous inductance and Idc,1 is the output current of the passive rectifiers 108 averaged over a fundamental period. The passive rectifiers 108 are assumed to be operated in Mode I with the commutation angle less than π/3. In this mode, three out of six diodes in the bridge 122 conduct during the commutation interval and the input-output voltage relationship follows (2). Passive rectifiers in this architecture are the line-commutated rectifiers operating at ac fundamental frequency. Hence, the maximum blocking voltage of these diodes is equal to the peak of the line-to-line voltage, i.e., √{square root over (3Eω)}. As Converters I and II operate with voltage conversion ratios of 1:n1 and 1:2 d n2, respectively, the dc grid voltage is:

Vgrid=n1[(k−1)Vpas+Vact]+2dn2Vact  (3)

where is the dc output voltage of the active rectifier. At rated generator speed, the controllability of the active rectifier requires:

\(\begin{matrix}
{V_{act} \geq {\frac{\sqrt{3}E_{0}}{k}.}} & (4)
\end{matrix}\)

Operating the active rectifier at its minimum controllable output voltage and Converter II with duty ratio d=0 ensures that minimum power is processed by the active rectifier at the rated speed. Using (2) and (4), (3) can be expressed as:

\(\begin{matrix}
{V_{grid} = {{\frac{3{n_{1}\left( {k - 1} \right)}}{\pi}\left\lbrack {\frac{\sqrt{3}E_{0}}{k} - {\omega_{0}{LI}_{{dc},1,0}}} \right\rbrack} + \frac{\sqrt{3}n_{1}E_{0}}{k}}} & (5)
\end{matrix}\)

where Idc,1,0=Idc,1 at rated generator speed. This equation gives the required transformer turns ratio of Converter I, n1, as a function of k. To follow this grid voltage, Vgrid, at all the operating speeds, the variation of active rectifier dc-link voltage with co and d can be calculated from (3) and (5) as:

\(\begin{matrix}
{{V_{act}\left( {n,k,d,\omega} \right)} =} & (6)
\end{matrix}\)
\(\left\lbrack {{\left( {\frac{3\left( {k - 1} \right)\left( {1 - \omega} \right)}{\pi} + 1} \right)\frac{\sqrt{3}E_{0}}{k}} - {\frac{3\left( {k - 1} \right)\omega_{0}L}{\pi}\left( {I_{{dc},1,0} - {I_{{dc},1}\omega}} \right)}} \right\rbrack\frac{1}{\left( {1 + {2{dn}}} \right)}\)

where n=n2/n1. Equation (6) highlights that the active rectifier dc-link voltage depends on the generator speed co, number of ports k, and the duty ratio of Converter II, d.

The active rectifier processes a small amount of the incoming power at the rated condition. In an example, active rectifier processes ⅕th of the incoming power at the rated condition. The passive rectifier processes ⅘th of the power at the rated condition. Converter I processes the entire power at rated condition. Converter II process a small fraction, e.g. a maximum of 8% power, at the minimum speed.

Active Rectifier Input Current as a Function of Design Variables

The maximum active rectifier input current determines the active rectifier's switch current rating. Assume that the active rectifier is lossless and operating at unity power factor gives:

Pact= 3/2EωIac=Vact(Idc,1+Idc,2)  (7)

where Pact is the power processed by the active rectifier, Iac is the peak ac line current, and Idc,2 is the current drawn by Converter II averaged over one fundamental period, respectively. Idc,1 and Idc,2 can be expressed in terms of the dc grid current, Igrid, following the conversion ratio of the corresponding dc-dc converters as:

Idc,1=n1Igrid

Idc,2=2dn2Igrid,  (8)

Using (1) and (8) in (7) yields:

\(\begin{matrix}
{I_{ac} = {\frac{2kV_{act}}{3\omega E_{0}}\left( {n_{1} + {2{dn}_{2}}} \right){I_{grid}.}}} & (9)
\end{matrix}\)

In a wind energy system, maximum power extraction at different wind speeds is achieved by delivering power to the grid following a cubic relationship with co. For a constant grid voltage, this relationship results in:

Igrid=CMPPω3  (10)

where CMPP is a proportionality constant. Equations (10) and (9) result in:

\(\begin{matrix}
{{I_{ac}\left( {n_{1},n_{2},k,d,\omega} \right)} = {\frac{2kV_{act}}{3E_{0}}\left( {n_{1} + {2{dn}_{2}}} \right)C_{MPP}{\omega^{2}.}}} & (11)
\end{matrix}\)

Normalization

The next step is to normalize (6) and (11) to make this design procedure independent of actual values of Vgrid, E0, ω0, and rated power. Using current and voltage base values as:

Ibase=n1CMPP and

Vbase=√{square root over (3)}E0  (12)

respectively, the normalized active rectifier output voltage is:

\(\begin{matrix}
{{V_{{act},{pu}}\left( {n,d,k,\omega} \right)} =} & (13)
\end{matrix}\)
\(\left\lbrack {{\left( {\frac{3\left( {k - 1} \right)\left( {1 - \omega} \right)}{\pi} + 1} \right)\frac{1}{k}} - {\frac{3\left( {k - 1} \right)L_{pu}}{\pi k}\left( {1 - \omega^{4}} \right)}} \right\rbrack\frac{1}{\left( {1 + {2{dn}}} \right)}\)

where Lpu is the generator synchronous inductance normalized by Lbase=Vbase/k ω0 Ibase Similarly, the normalized active rectifier input current is:

\(\begin{matrix}
{I_{{ac},{pu}} = {\frac{2kV_{{act},{pu}}}{\sqrt{3}}\left( {1 + {2{dn}}} \right){\omega^{2}.}}} & (14)
\end{matrix}\)

Using (13) in (14) yields

\(\begin{matrix}
{{I_{{ac},{pu}}\left( {k,\omega} \right)} = {{\frac{2k\omega^{2}}{\sqrt{3}}\left\lbrack {{\left( {\frac{2k\omega^{2}}{\sqrt{3}} + 1} \right)\frac{1}{k}} - {\frac{3\left( {k - 1} \right)\left( {1 - \omega} \right)}{\pi}\left( {1 - \omega^{4}} \right)}} \right\rbrack}.}} & (15)
\end{matrix}\)

This equation shows that the normalized active rectifier input current is independent of n and d. Assuming Lpu as 0.05, FIG. 2 illustrates the variation of Iac,pu with co for different numbers of ac ports k.

Minimization of the Total Switch VA Rating

The total normalized switch VA rating of the generator-rectifier system and grid interface 100 is:

VAtotal,pu=VAConvI,pu+VAConvII,pu+VAact,pu  (16)

where VAConv I, pu, VAConv II, pu, and VAact, pu are the normalized VA ratings of Converter I, Converter II, and the active rectifier 106, respectively. Converter I consists of four active switches; therefore, its total switch VA rating is:

\(\begin{matrix}
\begin{matrix}
{{VA}_{{Conv}I} = {4\frac{V_{grid}}{n_{1}} \times {\max\left( {n_{1}I_{grid}} \right)}}} \\
{= {4C_{MPP}V_{grid}}}
\end{matrix} & (17)
\end{matrix}\)

as grid current is maximum at rated speed, ω=1. Using (5) in (17) followed by normalization results in:

\(\begin{matrix}
{{VA}_{{{Conv}I},{pu}} = {{\frac{4}{k}\left\lbrack {\frac{3\left( {k - 1} \right)\left( {1 - L_{pu}} \right)}{\pi} + 1} \right\rbrack}.}} & (18)
\end{matrix}\)

Converter II consists of four active switches as well. Therefore, its total switch VA rating is:

VAConvII=4 max(Vact)×max(n2Igrid)=4n2CMPP max(Vact).  (19)

Normalizing this equation yields:

VAConvII,pu=4nmax(Vact,pu)  (20)

where Vact, pu is obtained from (13). Similarly, the normalized switch VA rating of the two-level six-switch active rectifier can be obtained as:

VAact,pu=6[max(Vact,pu)×max(Iac,pu)].  (21)

As the design objective is to minimize the total normalized switch VA rating, the optimization is expressed as:

\(\begin{matrix}
{{\min\limits_{k,d,n}{VA}_{{total},{pu}}}{{s.t.\omega} \in \left\lbrack {0.55,1} \right\rbrack}{k > 1}{n \geq 0}{d \in {\left\lbrack {0,0.5} \right\rbrack.}}} & (22)
\end{matrix}\)

For k ac ports, solving this optimization results in:

\(\begin{matrix}
{n_{{opt},k} = {\underset{n}{\arg\min}{\left( {VA}_{{total},{pu}} \right).}}} & (23)
\end{matrix}\)

n1 is computed from (5) and the optimum transformer turns ratio for Converter II, n2,opt=n1nopt,k. Variations of n1 and n2,opt as functions of the number of ac ports are shown in FIG. 3. FIG. 4 shows the minimum switch VA rating requirement as a function of k. Three design points are highlighted illustrate an advantage of the system 100. Point A refers to a design architecture with only one generator ac port that is connected to an active rectifier followed by a grid-tied fixed-duty dc-dc converter. The total switch VA rating requirement for this design case is 10.93 p.u. Point B refers to a design architecture, where the output of a five-port integrated generator-rectifier that is connected to a grid-tied fixed-duty dc-dc converter as in P. T. Huynh, P. J. Wang, and A. Banerjee, “An integrated permanent-magnet-synchronous generator-rectifier architecture for limited-speed-range applications,” IEEE Trans. Power Electron., vol. 35, no. 5, pp. 4767-4779, May 2020. In this case, the required total switch VA rating is 7.48 p.u. Finally, point C refers to the present grid interface 100 with a five-port integrated generator-rectifier, where the two dc-dc converters, Converters I and II, work together to reduce the total switch VA rating to 6.42 p.u.

The substantial reduction in the total switch VA rating can be predominantly attributed to the reduction in the active rectifier dc-link voltage rating. With the optimized design for a five-port generator, FIG. 5A shows the allowable duty ratio d for Converter II. The dmax line signifies the lowest bound of the active rectifier voltage required to maintain desired power flow control. However, operating along the drain line ensures that the active rectifier output voltage remains constant and equal to its value at the rated speed. Operating Converter II within this region guarantees that the maximum of the active rectifier output voltage remains at 0.2 p.u. independent of the speed, as shown in FIG. 5B. In contrast, the absence of Converter II increases the voltage to p.u., resulting in an increase in the switch VA rating. Therefore, for a five-port system with n2=n2,opt, the active rectifier voltage rating is reduced by 60.7% in the present interface 100.

A 10-MW Wind-Turbine-Driven Multiport PMSG Example

FIG. 6 shows a 10-MW wind-turbine-driven multiport PMSG 600 with a plurality of generator-rectifier system and grid interfaces 100 of the invention. At a rated rotational speed of 9.6 r/min, each generator port is assumed to generate a line-to-line rms voltage of 415 V with a frequency of 19.2 Hz. One active and four passive rectifiers, along with two isolated dc-dc converters, are connected as discussed above to form each module 100. Twenty such modules 100 are stacked in series to connect the wind turbine output to a 66-kV dc grid through a 10-mH inductor.

The synchronous inductance of the PMSG is chosen to be 1.3 mH, which is p.u. The ratings and parameters of the system are tabulated in Table I. Based on the above ratings and parameters, n1 and n2,opt are calculated as 1.215 and 1.87, respectively. The required voltage and current ratings of the semiconductor devices can be calculated as explained above.

The devices are then selected with reasonable safety factors, as tabulated in Table II. The conventional dc grid interface architecture where Converter II is absent is also designed for comparison. The total switch VA rating for the conventional architecture is 15.41×106 VA whereas it is reduced to 11.9×106 VA (a saving of 22.8%) with the interfaces 100. The analytical results, as shown in FIG. 4, indicate a saving of 14.2% in switch VA rating requirement for a five-port system. This difference between the analytical results and the design example is due to the nonavailability of devices with exact required ratings. In addition, a reduction in the switch VA rating translates into the improved system efficiency. This generalized design framework for the converter architecture is independent of the type of the devices used. Insulated gate bipolar transistors (IGBTs) were used to make the comparisons in this example. A similar analysis can be performed using silicon carbide devices.

The present topology is compared with the conventional dc grid interface in terms of the losses within the individual converters, as shown in FIG. 7. The losses within the active rectifier in the present topology are substantially reduced. This is due to the use of low-voltage devices for the active rectifier and its regulated dc-link voltage. The architectures are also compared in terms of FIG. 8. The conversion loss is reduced due to the present architecture by 28.3% at the rated speed and 71.7% at the minimum speed. The difference in the results obtained from the simulation and the analysis is primarily due to the way the device characteristics have been captured in the loss model. In the PLECS simulation, multiple data points have been used, whereas curve-fitting equations were used in the analysis.

Control Strategy

A preferred control strategy for the generator-rectifier system and grid interface 100 or the system 600 is discussed next. The strategy is discussed with the interface or system connected to a stiff dc grid, i.e., a grid whose voltage is actively regulated to maintain a relatively constant voltage. A switching cycle average model of the system is shown in FIG. 9. The passive rectifiers are modeled as a generator-speed-dependent voltage source in series with an impedance representing the voltage drop due to commutation. The active rectifier is modeled as a controllable current source in parallel with a capacitor. Converters I and II are modeled as dc transformers with their voltage conversion ratio (1:n1) and (1:2 d n2), respectively.

The passive rectifiers 108 and Converter I 110, which is operated at a constant duty ratio of 0.5, do not actively regulate any system variables. The generator-side active rectifier 106 controls the power harvested from the wind and Converter II 112 regulates its input voltage vact.

Active Rectifier Control

MPPT ability is achieved if the total generated power follows the optimum cubic relationship:

Pgen,mpp=Cp,mppω3  (24)

where Cp,mpp is a characteristic constant of the wind turbine. The active rectifier 106 processes a part of the generated power given by:

Pact= 3/2EsdIsd  (25)

Assuming the active rectifier to be lossless, and Esd and Isd are the d-axis components of the generator-induced EMF and current vectors, respectively. The d-axis is considered to be aligned with the generator-induced EMF vector. Therefore,

\(\begin{matrix}
{{E_{sd} = \frac{\omega E_{0}}{k}},{E_{sq} = 0.}} & (26)
\end{matrix}\)

The power processed by all the passive rectifiers is:

Ppas=(k−1)VpasIdc,1.  (27)

Based on (2) and (24)-(27), the active rectifier input current should follow the below equation to ensure MPPT:

\(\begin{matrix}
{{I_{{sd},{mpp}}\left( {\omega,I_{{dc},1}} \right)} = {\frac{2{kC}_{p,{mpp}}\omega^{2}}{3E_{0}} - {\frac{2\sqrt{3}\left( {k - 1} \right)}{\pi}I_{{dc},1}} + {\frac{2{k\left( {k - 1} \right)}\omega_{0}L}{\pi E_{0}}{I_{{dc},1}^{2}.}}}} & (28)
\end{matrix}\)

This equation is used to create the reference value for the d-axis current. The d- and q-axis current controllers are designed and implemented following a published procedure in P. T. Huynh, P. J. Wang, and A. Banerjee, “An integrated permanent-magnet-synchronous generator-rectifier architecture for limited-speed-range applications,” IEEE Trans. Power Electron., vol. 35, no. 5, pp. 4767-4779, May 2020. A block diagram of the active rectifier control strategy is shown in FIG. 10. The FIG. 10 control strategy effectively maintains the dc link voltage of the active rectifier constant at all speeds using converter II and lets the total dc link voltage (Vdc) vary depending on the speed. The duty ratio control of Converter II allows this, though the dc grid voltage remains constant for all speeds.

Converter II Control

The switch duty ratio of Converter II (d) is used to control the active rectifier dc-link voltage Vact following (6), which can be expressed in:

\(\begin{matrix}
{V_{act} = \frac{C_{1}(\omega)}{\left( {1 + {2{dn}}} \right)}} & (29)
\end{matrix}\)
\(where\)
\(\begin{matrix}
{{C_{1}(\omega)} = \left\lbrack {{\left( {\frac{3\left( {k - 1} \right)\left( {1 - \omega} \right)}{\pi} + 1} \right)\frac{\sqrt{3}E_{0}}{k}} - {\frac{3\left( {k - 1} \right)\omega_{0}L}{\pi}\left( {I_{{dc},1,0} - {I_{{dc},1}\omega}} \right)}} \right\rbrack} & (30)
\end{matrix}\)

is constant at some operating point ω=ωop. Considering slower dynamics of the wind speed and the rotational speed as compared to that of the active rectifier dc-link voltage, the small-signal model of (29) is:

\(\begin{matrix}
{{\Delta v_{act}} = {\frac{2nV_{{act},0}}{1 + {2d_{0}n}}\Delta d}} & (31)
\end{matrix}\)

where Vact,1 and do are the steady-state values of Vact and d, respectively, around which the system is perturbed and Δvact and Δd are the corresponding perturbed quantities. The active rectifier dc-link voltage controller, whose output is the duty ratio d of Converter II, can be designed based on the small-signal model (31). An integrator-type controller gain (Kiv) can be:

\(\begin{matrix}
{K_{iv} = {{- \frac{2nV_{{act},0}}{1 + {2{nd}_{0}}}}\omega_{{BW},v}}} & (32)
\end{matrix}\)

where ωBW,v is the desired bandwidth of the active rectifier dc-link voltage controller. The control block diagram of Converter II is shown in FIG. 10.

Simulation Results

Simulations were conducted using low-power laboratory prototype and confirmed performance improvements. In a conventional design, active rectifier voltage increases to 73 V as the emulated wind speed falls to its minimum value, 6.6 m/s but was regulated to 53V in the present generator-rectifier system and grid interface. The duty ratio of Converter I remains constant at 0.48 through-out the operating range. The intermediate dc-link voltage, which is also the Converter I input voltage, determines the magnitude of the Transformer I primary voltage waveform. It decreases from 129.7 V at a wind speed of 12 m/s to 98.6 V at 6.6 m/s. The active rectifier dc-link voltage is maintained at 53 V. Therefore, the magnitude of Transformer II primary voltage waveform remains unchanged. However, its duty ratio increases to 0.43 at 6.6-m/s wind speed from 0.02 at 12 m/s.

Dynamic testing showed the MPP tracking ability of the present generator-rectifier and grid interface. With a change of wind speed from a rated 12 to 6.6 m/s, the PMSG rotational speed lowers from its rated value, 150 r/min, to 83 r/min (i.e., close to 0.55×150 r/min or 82.5 r/min) and the generator output power from its rated value, 160 W, to 20 W (i.e., close to (0.55)3×160 W or 26.6 W). At t=5.5 s, the wind speed returns to its rated value and so do the PMSG rotational speed and generator output power. The intermediate dc-link voltage reduces from 129.7 V to 98.6 at t=1.8 s when the wind speed changes from 12 to 6.6 m/s. The voltage again goes back to 129.7 V at t=11.93 s when wind speed reverts to 12 m/s. However, the active rectifier dc-link voltage was regulated within 53 V.

Simulations showed that the additional dc-dc converter in the present design reduces the total switch VA rating by 22.8%, which translates into overall loss reduction ranging between 28.3% and 71.7%, depending on the extracted power. The active rectifier dc-link voltage was shown to be regulated by Converter II.

While specific embodiments of the present invention have been shown and described, it should be understood that other modifications, substitutions and alternatives are apparent to one of ordinary skill in the art. Such modifications, substitutions and alternatives can be made without departing from the spirit and scope of the invention, which should be determined from the appended claims.

Various features of the invention are set forth in the appended claims.

