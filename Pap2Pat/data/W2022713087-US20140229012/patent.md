# DESCRIPTION

## BACKGROUND OF THE INVENTION

1. Technical Field

The present disclosure relates generally to thermo-economic modeling and optimization of power plants, and more particularly, to thermo-economic modeling and optimization of a combined cooling, heating, and power plant.

2. Discussion of Related Art

Combined Cooling, Heating, and Power Plants (CCHP) are becoming increasingly popular in both residential and commercial sectors for meeting desired energy demands. Since these systems integrate cooling, heating and power generation capabilities at one site, they result in potentially lower capital costs. The presence of multiple energy sources which characterizes these systems also provides a significant potential for reducing energy consumption and greenhouse emissions.

A hierarchical paradigm including a supervisory control layer may be used to control such systems. The supervisory layer determines the set-points of important plant operation parameters such as component on/off states, water and gas temperatures, mass flow rates, etc.

However, it can be difficult to determine the set-points that would be most optimal for providing efficient plant operation. Detailed models for CCHP components are available. However, integration of such detailed models for plant-wide optimization may result in large computation times and other practical concerns related to implementation.

Thus, there is a need to develop reduced order models, which accurately capture important dependencies contained in the detailed models and also allow their use for efficient and robust optimization.

## SUMMARY OF THE INVENTION

According to an exemplary embodiment of the invention, a method to manage operating costs of a combined cooling heating and power (CCHP) plant includes converting complex models of underlying components of the plant into simplified models, performing an optimization that uses the simplified models as constraints of the optimization to output multiple decision variables, and adjusting controls of the plant based on one or more of the output decision variables.

According to an exemplary embodiment of the invention, a Combined Cooling Heating Power (CCHP) Plant includes a cooling element, a heating element, a power supplying element, and a computer comprising a memory including a program, and a processor configured to execute the program. The program includes instructions to convert complex models of underlying components of the elements into simplified models, perform an optimization that uses the simplified models as constraints of the optimization to output decision variables, and adjust controls of at least one of the elements of the plant based on one or more of the output decision variables.

## DETAILED DESCRIPTION

Exemplary embodiments of the invention are discussed in further detail with reference to FIGS. 1-11. This invention may, however, be embodied in different forms and should not be construed as limited to the embodiments set forth herein.

It is to be understood that the systems and methods described herein may be implemented in various forms of hardware, software, firmware, special purpose processors, or a combination thereof. In particular, at least a portion of the present invention may be implemented as an application comprising program instructions that are tangibly embodied on one or more program storage devices (e.g., hard disk, magnetic floppy disk, RAM, ROM, CD ROM, etc.) and executable by any device or machine comprising suitable architecture, such as a general purpose digital computer having a processor, memory, and input/output interfaces. It is to be further understood that, because some of the constituent system components and process steps depicted in the accompanying Figures may be implemented in software, the connections between system modules (or the logic flow of method steps) may differ depending upon the manner in which the present invention is programmed. Given the teachings herein, one of ordinary skill in the related art will be able to contemplate these and similar implementations of the present invention.

FIG. 1 illustrates a method of optimizing performance of a combined heating, cooling, and power (CCHP) plant, according to an exemplary embodiment of the invention. The method includes converting complex models of underlying components of the plant into simplified models (S101), performing an optimization that uses the simplified models as constraints of the optimization to output multiple decision variables (S102), and adjusting plant controls using the output decision variables (S103).

FIG. 2 illustrates an example of the CCHP plant including a cooling element 210, a heating element 220, and a power supply element 230. An exemplary embodiment of the CCHP plant is illustrated in FIG. 3. The CCHP plant includes seven electric chillers 211 that generate cold water (e.g., lowers temperature of water received) for cooling or for storage in a thermal energy storage (TES) tank 212. In an exemplary embodiment, the chillers 211 are electric chillers. The chillers 211 and the TES tank 212 form the source components of the cooling element 210 to meet cooling demands. The CCHP plant further includes a gas turbine 231 and a steam turbine 232 that provide electrical power. The thermodynamic energy of the exhaust from the gas turbine 231 is used to heat water in a Heat Recovery Steam Generator (HRSG) 221 to produce steam to drive the steam turbine 232 and hot water to provide heat. Thus, the gas turbine 231 and the steam turbine 232 form the source components of the power supply element 230 to meet power needs. The HRSG 221 or the HRSG 221 in combination with the gas turbine 231 may be considered the source components of the heating element 220 to meet the heating demands.

The CCHP plant illustrated in FIG. 3 is provided merely as an example for ease of understanding methods of optimizing similar or same such plants according to exemplary embodiments of the invention. However, the CCHP is not limited to any particular configuration, as the number and types of chillers, thermal energy storage systems, and turbines may vary, and some of these components may not be present in alternate configurations. For example, the method can be applied to a plant that includes only a heating element, only a cooling element, only a power element, or various combinations thereof.

FIG. 4 illustrates an example of a complex model of one of the chillers 211. The chiller 211 may include one or more underlying components, such as evaporators, condensers, compressors, cooling towers, and water pumps. In an exemplary embodiment of the invention, the evaporators and/or condensers are modeled using a Log Mean Temperature Difference (LMTD) approach, the compressors are modeled using a non-isentropic compression process with appropriate isentropic efficiency lookup maps, and the cooling towers are modeled using the Number of Transfer Units (NTU) framework. These models can be verified against experimental data available for the chillers 211. For example, if the coefficient of performance (COP), a chiller efficiency metric, of the experimental data matches well with predictions made by the selected model, the correct model has been chosen.

FIG. 5 illustrates a complex model of the TES tank 212. The tank 212 is divided into 100 control volumes along its height, and mass and energy conservation laws are applied to each control volume. It may be assumed that the tank 212 is well-insulated from the ambient and also that at any given time, the tank 212 is either charging or discharging. In the charging mode, a portion of the supply water from the chiller system is fed into the tank 212 for storage from the bottom. In the discharging mode, cold water from the tank 212 is used to meet cooling demands. The complex model may be verified if a temperature profile generated from experimental data compares well against the temperature profile of the complex model.

FIG. 6 illustrates a complex model of a gas turbine 231. Referring to FIG. 6, the model of the gas turbine (GT) includes a compressor 231-1, a combustor 231-2, and turbine 231-3. In this example, the GT model illustrated is that of a Solar Titan™ 130 gas turbine. However, the invention is not limited to any particular GT.

FIG. 7 illustrates a closed loop model of FIG. 6 including a temperature controller 701 and a power controller 702 with speed and acceleration control. The controllers control Turbine Exit temperature (TET), turbine output power, shaft speed, and shaft acceleration. The GT model may be generated based on thermodynamic laws of mass and energy combustion for each underlying component (e.g., compressor 231-1, combustor 231-2, turbine 231-3, and a generator shaft) and validated using data from on-field experiments.

Once the complex models of the components of the CCHP have been identified, one or more of these complex models is replaced with simplified versions that can be more easily optimized (See block S102).

The complex model of the chiller of a cooling element 210 can be simplified if certain assumptions are made. For example, one can assume that the return water temperature TCHWR,i (e.g., 60 degrees Fahrenheit) and the supply water temperature TCHWS,i (e.g., 40 degrees Fahrenheit) of a given chiller ‘i’ (e.g., i=one of the numbered chillers 211) are maintained close to their design values due to the action of its control valves. When this assumption is made, the chilled water mass flow rate MCHW,i (e.g. kg/s) of chiller ‘i’ becomes the only independent variable input to the model. Thus, the amount of cooling QCHW,i (KW) provided by chiller ‘i’ can be represented by Equation 1 as follows:

QCHW,i=mCHW,icp(TCHWR,i−TCHWS,i)   (1)

where cp is the specific heat capacity of water (e.g., KJ/kg K).

A chiller 211 includes a compressor and a water pump. Variables of interest in the context of optimization of the chiller 211 may include the compressor power consumption Wcomp,i and the water pump power consumption WCHWP. Using data obtained from the complex model of the chiller 211, a relationship between the compressor power consumption Wcomp,i and the amount of cooling QCHW,i may be obtained by performing a regression analysis on each of chillers 211. Table 1 shows examples of these relationships for each of the chillers in the CCHP plant.

As shown in Table 1, linear expressions based on the amount of cooling provided by each chiller can be used to represent power consumption of the corresponding chiller.

Regression analysis may also be used to express the total power consumed by the water pumps, condenser water pumps, and cooling towers of the chiller. For example, an expression can be obtained to represent the power consumption of the chilled water pump WCHWP of a water pump of chiller ‘i’ by regression analysis for each of the chillers 211 as shown symbolically in Equation 2:

\(\begin{matrix}
{W_{CHWP} = {f\left( {\sum\limits_{i}\; m_{{CHWP},i}} \right)}} & (2)
\end{matrix}\)

In an exemplar embodiment, a simplified model of a chiller assumes that the condenser water mass flow rate of a condenser of the chiller is controlled to be twice the chilled water flow rate to achieve a high COP. A condenser variable of interest in the context of optimization is the total power consumption of the condenser water pump WCWP for which a relationship of the form shown in Equation 3 may be obtained using regression:

\(\begin{matrix}
{W_{CWP} = {f\left( {\sum\limits_{i}\; m_{{CW},i}} \right)}} & (3)
\end{matrix}\)

Another variable of interest in the context of optimization is the total power consumption by the cooling tower fans WCTF, which may be represented by the form shown in Equation 4 obtained using regression:

\(\begin{matrix}
{W_{CTF} = {f\left( {\sum\limits_{i}\; m_{{CW},i}} \right)}} & (4)
\end{matrix}\)

To generate a simplified model of TES tank 212, a two layer model 812 may be used as shown in FIG. 8. The thermodynamics of the zones (layers) can be expressed by a pair of ordinary differential equations. However, when static energy and mass conservations for the supply and return valves are considered, the overall TES tank model 812 becomes Differential Algebraic (DAE). The TES tank has binary modes of operation (e.g., charging or discharging). The charging mode of the model 812 may be represented by the below equations 5-10 as follows.

\(\begin{matrix}
{m_{T} = {m_{CHW} - m_{L}}} & (5) \\
{{\rho \; c_{pw}\frac{T_{a}}{t}} = {{f_{a,c}m_{T}{c_{pw}\left( {T_{b} - T_{a}} \right)}} + {U_{c}{A\left( {T_{b} - T_{a}} \right)}}}} & (6) \\
{{\rho \; c_{pw}\frac{T_{b}}{t}} = {{f_{b,c}m_{T}{c_{pw}\left( {T_{{in},c} - T_{a}} \right)}} + {U_{c}{A\left( {T_{a} - T_{b}} \right)}}}} & (7) \\
{T_{{in},c} = {T_{LS} = T_{CHWS}}} & (8) \\
{{{m_{T}T_{{out},c}} + {m_{L}T_{LR}}} = {m_{CHW}T_{CHWR}}} & (9) \\
{{T_{{out},c}(t)} = {T_{a}\left( {t - {TD}_{c}} \right)}} & (10)
\end{matrix}\)

Equation 6 is an energy balance equation for the top layer ‘a’ of the TES tank during charging that is based on the temperatures of each layer (e.g., Ta and Tb), a time-constant multiplier for layer ‘a’ during charging (e.g., fa,c), mass flow rate through the tank mT , and a heat transfer coefficient between layers ‘a’ and ‘b’ during charging (e.g., UcA). Equation 7 is an energy balance equation for the bottom layer ‘b’ that is similar to Equation 6, but includes a temperature of inlet steam during charging (Tin,c) and a time-constant multiplier for layer ‘b’ during charging.

The discharging mode of the model 812 may be represented by the below equations 11-16.

\(\begin{matrix}
{m_{T} = {m_{L} - m_{CHW}}} & (11) \\
{{\rho \; c_{pw}\frac{T_{a}}{t}} = {{f_{a,d}m_{T}{c_{pw}\left( {T_{{in},d} - T_{a}} \right)}} + {U_{d}{A\left( {T_{b} - T_{a}} \right)}}}} & (12) \\
{{\rho \; c_{pw}\frac{T_{b}}{t}} = {{f_{b,d}m_{T}{c_{pw}\left( {T_{a} - T_{b}} \right)}} + {U_{d}{A\left( {T_{a} - T_{b}} \right)}}}} & (13) \\
{{{m_{T}T_{{out},d}} + {m_{CHW}T_{CHWS}}} = {m_{L}T_{LS}}} & (14) \\
{T_{{in},d} = {T_{CHWR} = T_{LR}}} & (15) \\
{{T_{{out},d}(t)} = {T_{b}\left( {t - {TD}_{d}} \right)}} & (16)
\end{matrix}\)

Equation 12 is an energy balance equation for the top layer ‘a’ of the TES tank during discharging that is similar to equation 6. Equation 13 is an energy balance equation for the bottom layer ‘b’ during discharging that is similar to equation 7.

As shown by constraints 10 and 16, the temperature of outlet steam during charging is based on the temperature of the top layer ‘a’ and a time-delay, and the temperature of the outlet steam during discharging is based on the temperature of the bottom layer ‘b’ and another time-delay.

In at least one embodiment of the invention, the time-delays are strongly dependent on the mass flow rate mT through the TES (e.g., the water mass flow rate in and out of a TES tank, kg/sec). In one embodiment, these time delays can be obtained by regression analysis as shown by equations 17 and 18, respectively, as follows:

\(\begin{matrix}
{{DT}_{c} = \frac{10^{7}}{{15.718\; m_{T}} + 1781.5}} & (17) \\
{{DT}_{d} = \frac{10^{7}}{{16.911\; m_{T}} + 332.82}} & (18)
\end{matrix}\)

In at least one embodiment, the TES tank model 812 includes parameters fa,c (e.g., time constant multiplier for layer ‘a’ for dynamics during charging), fb,c (e.g., time constant multiplier for layer ‘b’ for dynamics during charging), fa,d (e.g., time constant multiplier for layer ‘a’ for dynamics during discharging), fb,d (e.g., time constant multiplier for layer ‘b’ for dynamics during discharging), Uc (e.g., heat transfer coefficient between layer ‘a’ and ‘b’ during charging, and Ud (e.g., heat transfer coefficient between layer ‘a’ and ‘b’ during discharging).

These parameters are to be calibrated so that the predictions of the simplified and detailed models match closely, which may be expressed by equations 19 and 20 using a least-squares optimization.

\(\begin{matrix}
{\left\{ {f_{a,c},f_{b,c},U_{c}} \right\} = {{argmin}{\sum\limits_{k}\; \left( {{T_{{out},c}(k)} - {{\hat{T}}_{{out},c}(k)}} \right)^{2}}}} & (19) \\
{\left\{ {f_{a,d},f_{b,d},U_{d}} \right\} = {{argmin}{\sum\limits_{k}\; \left( {{T_{{out},d}(k)} - {{\hat{T}}_{{out},d}(k)}} \right)^{2}}}} & (20)
\end{matrix}\)

In exemplary embodiment of the invention, discretized forms of equations (5)-(18) serve as constraints for the optimization problems expressed in equations (19) and (20) and a simulated annealing based algorithm is used to determine the global minima. Exemplary parameters that may be obtained after averaging results from optimization runs over a range inputs using such an algorithm are shown in Table 2 below.

In an exemplary embodiment of the invention, a detailed closed loop gas turbine (GT) model (e.g., see FIG. 6 and FIG. 7) is used to develop regression based static relationships (e.g., equations 21-23) between selected GT inputs and outputs, which are relevant from an optimization perspective. The input variable is WGT, the desired electrical power produced by the GT, and the output variables of interest are the natural gas mass flow rate mf, exhaust gas mass flow rate mg , and the Turbine Exit Temperature TET of the exhaust gas.

mT=0.0447 WGT+0.2287   (21)

mg=0.2128 WGT2−1.8986 WGT+40.479   (22)

TET=0.06927 WGT4−2.126 WGT3+19.145 WGT2Tb −31.57 WGT+636.27   (23)

As shown above, each of parameters mf, mg, and TET are represented by polynomials that include a term having the desired electrical power of the GT WGT. The parameter mf is a first order polynomial, the parameter mg is a 2nd order polynomial, and the parameter TET is a fourth order polynomial. However, the above is merely an example of one type of gas turbine, as the polynomials may differ when a gas turbine of a different type is used.

FIG. 9 illustrates an HRSG 1421, which may include multiple components such as boilers, a superheater, steam drum, etc., but which is modeled as a lumped, counter-flow heat exchanger. In a further embodiment of the simplified model, the following assumptions are made: 1) there is no pressure drop in the gas stream from inlet to outlet (e.g., Pw,out=Pw,in), 2) pressure drops by a constant factor (fp,wSG) in the steam/water stream, and 3) the saturation temperature (Tw,sat) and specific enthalpy of vaporization (hfg) for water are linearly dependent on the saturation pressure (Pw,sat) in the operating range of the HRSG 1421. Equations 24 and 25 represent the saturation temperature (Tw,sat) and the specific enthalpy of vaporization (hfg), respectively.

Tw,sat=θT,1Pw,sat+θT,2   (24)

hfg=θh,1Pw,sat+θh,2   (25)

The above 2nd assumption results in the equation 26 as follows:

Pw,sat=fp,wSGPw,in   (26)

where the parameter Pw,out is the pressure of steam at the output of the HRSG 1421 and the parameter Pw,in is the pressure of water at its inlet.

Using a definition of heat exchanger effectiveness, equation 27 can be obtained as follows:

TET−Tg,out=ε(TET−Tw,in)   (27)

In an exemplary embodiment, the steam generator potential φ of the HRSG 1421 is defined as mg(TET−Tg,out)/mw where mw is the mass flow rate of water into the HRSG in kg/s. When φ is <cpw(Tw,sat), not enough thermodynamic potential exists for steam generation. When cpw(Tw,in−Tw,sat)≦φ≦cpw(Tw,in−Tw,sat)+hfg, steam in the saturated state is generated such that Tw,out=Tw,sat. When φ≧cpw(Tw,in−Tw,sat)+hfg, steam in the superheated state is generated according to equation 28 below.

\(\begin{matrix}
{T_{w,{out}} = {T_{w,{sat}} + {\frac{1}{c_{ps}}\left( {\varphi - {c_{pw}\left( {T_{w,{in}} - T_{w,{sat}}} \right)} + h_{fg}} \right)}}} & (28)
\end{matrix}\)

A schematic layout of a steam loop of the steam turbine 232 is illustrated in FIG. 10. A simplified model of the steam loop can be generated based on the assumptions: i) the deaerator and condensers are maintained at constant pressures, ii) the pressure and temperature of water exiting the steam loop is constant, iii) the steam driving a turbine of the steam turbine behaves like an ideal gas, and iv) the mass flow rate of steam in the steam loop is proportional of the fuel mass flow rate in the GT. In a further embodiment, it may be assumed that the ratio of steam used for driving the turbine, to that used for heating is constant at all times.

The above assumptions result in the following equations 29-33, which represent the simplified model of the steam loop.

\(\begin{matrix}
{m_{w\; 1} = {f_{1}^{w}m_{w}}} & (29) \\
{m_{w,2} = {\left( {1 - f_{1}^{w}} \right)m_{w}}} & (30) \\
{W_{p,1} = {\frac{m_{w\; 1}}{\rho}\left( {P_{dae} - P_{{cond},1}} \right)}} & (31) \\
{W_{p,2} = {\frac{m_{w}}{\rho}\left( {P_{w,{in}} - P_{dae}} \right)}} & (32) \\
{W_{ST} = {\frac{1}{1000}m_{w\; 1}c_{ps}\eta_{ST}{T_{w,{out}}\left( {1 - \left( \frac{P_{{cond},1}}{P_{w,{out}}} \right)^{0.25}} \right)}}} & (33)
\end{matrix}\)

where mw1 is mass flow rate of steam diverted to generate power from steam turbine, mw2 is mass flow rate of steam diverted to meet heating demand, f1w is a fraction of total mass of steam diverted to generate power from a steam turbine, mw is mass flow rate of steam/water, Pdae is the pressure at which the deaerator is maintained, Pcond,1 is the pressure at which condenser 1 is maintained, Wp1 is power consumption by pump 1, and Wp2 is power consumption of pump 2, WST is the power produced by the steam turbine, cps is the specific heat capacity of steam, and ηST is the isentropic efficiency of the steam turbine. In at least one embodiment of the invention, the following constraint (equation 34) is imposed for ensuring that the desired heating demand is met at all times as follows:

QH(t)≦Qh,max(t)=mw2(Tw,out−THWR)   (34)

where QH(t) is desired heating demand from the cogenerated steam at time t, QH,max(t) is the maximum heat that can be produced by the cogenerated steam and THWR is the hot water return temperature after serving the heating demand.

Once the simplified models of the underlying elements of the CCHP plant have been obtained, the method continues to block S102 to perform an optimization using these models as constraints to determine decision variables that can be used to adjust settings or controls within the actual plant.

This optimization may be referred to as a centralized supervisory optimization. The objective of this optimization is to determine, in advance, the optimal values of the plant inputs such that the total plant operating cost over a period of time (e.g., 24 hours) is minimized. The results of the optimization serve as set-points, which can be used by lower level feedback controllers, actuators, or valves such as a GT inlet valve, a chiller control valve, etc.

The optimization includes generation of an objective function that is to be minimized. Equation 35 shows an example of the objective function as follows:

\(\begin{matrix}
{J = {\sum\limits_{k = 1}^{24}\; \left( {\underset{\underset{{Grid}\mspace{14mu} {electricity}\mspace{14mu} {cost}}{}}{1000\; {c_{grid}(k)}{W_{grid}(k)}} + \underset{\underset{{Fuel}\mspace{14mu} {cost}}{}}{{c_{fuel}(k)}{m_{f}(k)}}} \right)}} & (35)
\end{matrix}\)

where cgrid is the price of power purchased from a grid and sampled every hour (e.g., $/KW), Wgrid is the power purchased from the grid every hour (e.g., kW), cfuel is the price of fuel ($/kg), and mf is the mass flow rate of the fuel (kg/s) which is typically natural gas.

In addition to the component level constraints defined by the simplified models presented above, in at least one embodiment of the invention, the optimization includes imposing certain demand and/or capacity constraints. Examples of the demand constraints are shown below by equations 36-37 as follows:

\(\begin{matrix}
{\mspace{79mu} {{\sum\limits_{i = 1}^{7}\; {Q_{{CHW},i}(k)}} = {1000\; {Q_{cooling}(k)}}}} & (36) \\
{{\underset{\underset{{Grid}\mspace{14mu} {power}\mspace{14mu} {purchased}}{}}{W_{grid}(k)} + \underset{\underset{{GT}\mspace{14mu} {power}\mspace{14mu} {produced}}{}}{W_{GT}(k)} + \underset{\underset{{ST}\mspace{14mu} {power}\mspace{14mu} {produced}}{}}{W_{ST}(k)}} = {\underset{\underset{{Campus}\mspace{14mu} {power}\mspace{14mu} {demand}}{}}{W_{elec}(k)} + \underset{\underset{{Steam}\mspace{14mu} {loop}\mspace{14mu} {power}\mspace{14mu} {consumption}}{}}{\frac{1}{1000}\left( {{W_{p\; 1}(k)} + {W_{p\; 2}(k)}} \right)} + \underset{\underset{{Chiller}\mspace{14mu} {bank}\mspace{14mu} {power}\mspace{14mu} {consumption}}{}}{\frac{1}{1000}\left( {{W_{CHWP}(k)} + {W_{CWP}(k)} + {W_{CTF}(k)} + {\sum\limits_{i}\; {W_{{comp},i}(k)}}} \right)}}} & (37)
\end{matrix}\)

where Qcooling is the forecasted hourly cooling demand (e.g., kW).

The capacity constraint may be imposed by the utility company providing the electricity. For example, the utility company could mandate that at least 1 MW of electricity be purchased periodically from the grid to stay in service.

The optimization can generate various decision variables such as the chilled water mass flow rate from each chiller mCHW,i(k), the total chilled water supply of the plant mL(k), the chilled water supply temperature from each chiller TCHWS(k), the temperature of a return water stream TLR(k), the operating power level of the GT WGT(k), and the power purchased from the grid Wgrid(k), where k=1, 2, . . . , 24 (e.g., for each hour of the day).

Since the charging/discharging mode of a TES of the simplified model may depend on the sign of

\({{\sum\limits_{i}\; {m_{{CHW},i}(k)}} - {m_{L}(k)}},\)

the optimization also determines at what time instances in the future does the tank need to be charged or discharged. In another embodiment, the initial TES tank state (e.g., water temperature of the two layers) is an input to the optimization.

At least one embodiment of the invention presents a novel application of various static and dynamic modeling tools (such as non-linear regression, global optimization and physics based modeling) to develop reduced order models of various CCHP components. The methodology is claimed to be generalizable in the sense that it would be applicable to most CCHP systems which have power production, energy storage and heat recovery features.

FIG. 11 shows an example of a computer system, which may implement the methods and systems of the present disclosure. The system and methods of the present disclosure, or part of the system and methods, may be implemented in the form of a software application running on a computer system, for example, a mainframe, personal computer (PC), handheld computer, server, etc. For example, the method of FIG. 1 may be implemented as software application(s). These software applications may be stored on a computer readable media (such as hard disk drive memory 1008) locally accessible by the computer system and accessible via a hard wired or wireless connection to a network, for example, a local area network, or the Internet.

The computer system referred to generally as system 1000 may include, for example, a central processing unit (CPU) 1001, a GPU (not shown), a random access memory (RAM) 1004, a printer interface 1010, a display unit 1011, a local area network (LAN) data transmission controller 1005, a LAN interface 1006, a network controller 1003, an internal bus 1002, and one or more input devices 1009, for example, a keyboard, mouse etc. As shown, the system 1000 may be connected to a data storage device, for example, a hard disk, 1008 via a link 1007. CPU 1001 may be the computer processor that performs some or all of the steps of the methods described above with reference to FIGS. 1-10.

In exemplary embodiment of the invention, the output decision variables are stored within a computer message for output across network 1002 to a computer system of the plant. The computer system of the plant, in response to the computer message may be configured to automatically adjust controls of the plant in view of the received output decision variables. For example, one of the decision variables could indicate the time at which water of the TES tank is to be charged or discharged and the control of the plant could be a timer that is automatically set by the received time. The optimization methods could be performed periodically and then the control would be re-adjusted each time the method is performed. This differs from a rule-based approach which uses the same rule no matter how conditions within the plant or demand forecasts have changed over time. Thus, embodiments of the invention are dynamic in nature, and allow for more efficient and cost effective management of a plant.

Although the illustrative embodiments have been described herein with reference to the accompanying drawings, it is to be understood that the present invention is not limited to those precise embodiments, and that various other changes and modifications may be affected therein by one of ordinary skill in the related art without departing from the scope or spirit of the invention. All such changes and modifications are intended to be included within the scope of the invention.

