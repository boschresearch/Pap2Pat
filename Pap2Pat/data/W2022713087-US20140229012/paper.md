# I. INTRODUCTION

Combined Cooling, Heating and Power (CCHP) plants are becoming increasingly popular in both residential and commercial sectors for meeting desired thermal and electricity demands [1]. Since these systems integrate cooling, heating and power generation capabilities at one site, they result in potentially lower capital and operating costs and facilitate ease of maintenance and operation [2]. Advanced features such as gas turbine-steam turbine combined cycles (co-generation) and thermal energy storage (TES) can be incorporated in such systems to improve the efficiency of energy conversion, and reduce operating costs. One such central facility, which uses these features, is located at the University of California, Irvine (UCI). It serves two important objectives [3]:

1) Produce and distribute chilled water (for campus cooling and de-humidification needs), high temperature hot water and steam (for campus heating and hot water requirements), and compressed air, to campus buildings.

2) Produce and distribute electricity for the lighting and equipment needs of the campus.

Effectively designed control systems can help in realizing the full potential of energy and cost savings that are provided by a CCHP plant. These plants are complex systems comprised of components with diverse dynamic response characteristics at various time-scales. A hierarchical paradigm is usually advocated for the control of such systems [4,5]. It involves an outermost supervisory control layer which determines the setpoints for the important plant operation parameters such as which components should be operating (on/off states) and at what conditions must they be operating (temperatures, pressures, mass flow rates, power levels, etc.). The inner layer, consisting of component level feedback controllers, then seeks to achieve these set-points by adjusting underlying actuators such as control valves, compressors and pumps. The focus of this paper is on the design of the supervisory control layer, using a systems engineering approach, which uses model based optimization to determine the optimal plant operation parameters or set-points for control of the CCHP system at UCI. Abstract-In this paper, we develop a modeling and optimization procedure for minimizing the operating costs of a combined cooling, heating, and power (CCHP) plant at the University of California, Irvine, which uses co-generation and Thermal Energy Storage (TES) capabilities. Co-generation allows the production of thermal energy along with electricity, by recovering heat from the generators in a power plant. TES provides the ability to 'reshape' the cooling demands during the course of a day, in refrigeration and air-conditioning plants. Therefore, both cogeneration and TES provide a potential to improve the efficiency and economy of energy conversion. The proposed modeling and optimization approach aims to design a supervisory control strategy to effectively utilize this potential, and involves analysis over multiple physical domains which the CCHP system spans, such as thermal, mechanical, chemical and electrical. Advantages of the proposed methodology are demonstrated using simulation case studies.  The determination of optimal set-points necessitates the development of high-fidelity models which accurately characterize their effect on important thermo-economic variables such as amount of utility consumption, plant efficiency and operating costs. Detailed models for CCHP system component dynamics are widely available [6,7]. However, integration of such detailed models for plant-wide optimization would potentially result in undesirably large computation times and other associated challenges [6]. This is particularly important in the context of CCHP, where, apart from dimensionality concerns, other characteristics such as : (a) mixed-integer variables to represent dispatch states (on/off) of the components, and (b) nonlinear thennodynamic constraints, result in increased computational complexity of optimization. Therefore, reduced order models are needed which can capture the important dependencies expressed by detailed models.

In this paper, we develop reduced order thermo-economic models from experimentally validated, detailed models of the CCHP components and integrate them in an optimization framework. This involves analysis over multiple physical domains which the system spans, such as thermal, mechanical, chemical and electrical. We demonstrate the efficacy of the proposed approach through simulated case studies.

## II. SYSTEM DESCRIPTION AND MODELING

### A. System Description

A schematic layout of the CCHP plant at VCI is shown in Fig. 1. A set of 7 electric chillers provides cold water, which can be directly supplied to the campus for cooling, or stored in a thermal energy storage (TES) tank for later use. An on-site gas turbine (GT), which drives a generator, is the primary source of electrical power for the campus. Furthermore, exhaust gas from the GT is used to produce steam in a heat recovery steam generator (HRSG). Steam is used for two purposes: (a) drive a steam turbine to produce additional power, and (b) produce hot water to meet a part of the campus heating load along with boilers. Steam can also be used to drive a chiller unit to provide additional cooling, but this capability is currently not used. An option of purchasing electricity from the grid is also available. 

#### 1) Electric chillers:

The detailed electric chiller model developed is an integration of static models for the underlying components, such as evaporators, condensers, compressors, cooling towers and pumps. These components were modeled using standard approaches in the thermodynamics literature [9,10] such as LMTD and NTU-effectiveness. The models were validated against available experimental data (Fig. 2). 

#### 2) Thermal Energy Storage (TES):

A dynamic, finite element based model is used for the TES, which divides the tank into 100 control volumes along its height. Energy and mass conservation laws are applied to each control volume. At any given time, the tank operates in one of two modes -charging and discharging -and therefore the resulting model is hybrid. In the charging mode, a portion of the cold supply water from the chillers is fed into the tank for storage. In the discharging mode, cold water from the tank is released to meet the campus cooling load. The temperature profiles predicted by the TES model are similar to experimentally determined profiles (Fig. 3).  Exit Temperature (TET), turbine output power, shaft speed and shaft acceleration, were also included, resulting in a closed loop model. This model was validated using data from on-field experiments, one result from which has been shown in Fig. 4.

### III. REDUCED ORDER MODELING

The complexity of the models (e.g. 100 state TES model) described in section II makes them unsuitable for direct use in optimization. In this section, reduced order models for the system components are developed for characteristics relevant from the perspective of thermo-economic plant optimization.

#### A. Electric Chillers

It is assumed that T CHW R and TCHWS,i are maintained close to their design values of 60 F and 40 F due to the action of control valves. Therefore, the only independent variable in the i'" chiller model is the chilled water mass flow, mCHW,i. The amount of cooling provided by each chiller is expressed by (1). Linear regression, ( 2) is then used to express the corresponding power requirement by the chiller compressor, where the obtained coefficient values are in Table I. Regression analysis is also used to express the total power consumed by the chilled water pumps, condenser water pumps and cooling tower fans.

QCHW,i = mCHW,i Cpw(TCHWR -TCHWS,i) (1) Weomp,i = aiQcHw,i + hi where, i = 1,2, ... ,7

##### B. Thermal Energy Storage (TES)

We use a stratified, two-layer modeling paradigm [11] (Fig. 5), to develop a simplified representation of the TES dynamics. The thermodynamics of the two layers can be expressed by a pair of ODEs. However, when static energy and mass conservations for the supply and return valves are considered, the overall TES model becomes Differential Algebraic (DAE).

Discretized forms of (3) -( 16) serve as constraints and a simulated annealing based algorithm in MA TLAB was used to determine the global minima. The parameters obtained are shown in Table II, after averaging results from optimization runs over a range of inputs. Outputs from the 2-layer and 100 node models were observed to be close (Fig. 6). 

###### C. Gas Turbine (GT)

The detailed GT model is used to develop regression based static relationships ( 19)-(21) between selected GT inputs and outputs, relevant from the perspective of optimization. The input variable is W GT 1 the desired electrical power produced by the GT. The output variables of interest are the corresponding values of natural gas mass flow rate, exhaust gas mass flow rate, and Turbine Exit Temperature.  

###### E. Steam loop

We define the steam loop as the section of the CCHP system associated with co-generated steam (Fig. 7). The following assumptions are used to develop a model for the steam loop: 1) The deaerator and condensers operate at constant pressures.

2) The pressure and temperature of water exiting the steam loop (entering the HRSG) are controlled to be constant. 3) Steam driving the turbine behaves like an ideal gas. 4) Mass flow rate of steam (water) in steam loop (HRSG) is set proportional to the fuel mass flow rate in the GT. Similarly, the ratio of steam used for driving the turbine, to that used for heating, is constant at all times. 

###### F. Integration ofcomponent models

It is important to check the functional integrity of the overall system when the reduced order models are combined to create a master model. This was verified by setting the input variables to design values. It was observed (Table III) that the output deviations from design values are within acceptable limits. 

###### D. Heat recovery Steam Generator (HRSG)

The HRSG, which consists of multiple components such as superheater, economizer, boilers, etc., is modeled as a lumped, counter-flow heat exchanger with the following assumptions. 1) There is no pressure drop in the gas stream from inlet to outlet, i.e. PW,out == Pw,in 2) Pressure drops by constant factor in the steam/water stream.

3) The saturation temperature (Tw,sat) and specific enthalpy of vaporization (h f g ) for water are linearly dependent on the saturation pressure (Pw,sat) in the operating range of the HRSG:

Tw,sat == 8T ,l P w,sat + 8T ,z 1 and (22) hf g == 8h ,l P w,sat + 8h ,z . (23) Assumption 2 results in the following equation: Next, using the definition of heat exchanger effectiveness [9],

We define the steam generation potential ¢ of the HRSG as mg(TET -Tg,out)/m w and consider following scenarios:

Not enough thermodynamic potential exists to generate steam.

In this case, steam in saturated state is generated, i.e. 

#### IV. OPTIMIZATION FRAMEWORK

The underlying objective of the optimization problem is to determine, in advance, the optimal values of the plant inputs such that the total plant operating cost over a 24-hour long time period in the future is minimized. The results of the optimization serve as set-points which lower level feedback controllers can attempt to achieve through appropriate actuators

##### B. Constraints

The reduced order models in section III serve as constraints in the optimization. In addition to these, certain demand and capacity constraints are also imposed:

1) Cooling Demand Constraint: For all k == 1,2, ... ,24:

or such as GT inlet valves, chiller control valves, etc. Details of this supervisory optimization framework are presented below.

##### A. Objective Function

The objective function, which represents the total CCHP operating cost in the look-ahead period, is expressed as:

2) Electricity Demand Constraint: For all k == 1,2, ... ,24:

-.-- A. Load profiles and utility prices Fig. 8 shows the cooling demand profile inspired by the trends in [11] and the electrical demand profile, based on measured data. The electricity rate schedule applied corresponds to June 2011 schedule E-20 tariffs of the Pacific Gas and Electric Company (PG&E), with three different rate slabs for off-peak, part-peak and peak load hours (Table IV) [12]. The natural gas price is $6.55 per 1000 cubic feet, which was the June 2011 schedule G-NR2 tariff of PG&E [12]. The optimization is performed at midnight.

##### B. Results

The nonlinear solver [mincon in the MATLAB optimization toolbox, with the interior-point algorithm, was used and the resulting optimal overall operating cost, compared with the costs for the two baseline strategies, is shown in Table V. Here, it is assumed that the tank is completely discharged at the initial time with uniform water temperature of 60 F inside.

Different sets of initial points arrive at different optimal solutions. After multiple trials, it was found that an initial condition set where the TES is charged from midnight -9 am and discharged for all times provides a consistently lower value of the objective function, than other randomly chosen initial points. This initial condition set was used in the optimization. 3) Capacity constraints: Appropriate capacity constraints are imposed on each input variable due to hardware capacity limitations An important constraint is also imposed by the utility company, mandating that at least 1 MW of electricity must be purchased at all times from the grid to stay in service.

##### D.Decision variables

The optimization variables, where k == 1,2, ... ,24, are: Since the charging/discharging mode of TES depends on the sign of(Il=l mCHW,i (k) -mL(k)), no binary variables are needed to characterize it. Also, the initial tank state (water temperature in the two layers) is an input to the optimization.

## V.CASE STUDY

A case study is presented in this section to demonstrate the benefits of using the modeling and optimization approach described. Here, look-ahead optimization is performed for prescribed cooling and electricity demands, and gas and electricity price schedules. The optimization results are compared against two baseline strategies. In the first baseline strategy, two potentially advantageous features, i.e. the TES and co-generation are not used. In the second baseline strategy, a heuristic, rule-based methodology using physical intuition is used to determine the operating parameters of the plant.  Fig. 9 shows the total cooling load to which the chillers are subjected to, when operating as per the optimal strategy versus the first baseline strategy. The role of TES in re-shaping the chiller load profile so as to shift peak loads to more economical off-peak and part-peak periods (Table IV) is evident. Similarly, Fig. 10 quantifies the role of cogeneration in bringing down grid and GT power levels. Here, the difference between the two curves represents the power generated by steam turbine. The second baseline strategy, is based on the following heuristic but intuitive guidelines: 1) The TES is begun to be charged (with chillers running at full capacity) at midnight. This is continued in the rest of the offpeak price regime until T LS and T CH W R violate constraints.

2) The TES is discharged at its maximum discharge rate to provide campus cooling, with chillers turned off, in the peak electricity price regime beginning at noon. This is continued in the rest of the regime until T LS and T CH W R violate constraints.

3) Chillers are turned on in decreasing order of design COPs. 4) T CH W S and T LR are set to their design values of 40 F and 60 F. 5) The GT is always given preference over the grid. This is based on relative analysis of the corresponding $/kWh rates. The values of mCHW,i(k) and mL(k) are calculated from rules 1-4 using a simple procedure using knowledge of prescribed cooling demands. Then, W g r i d (k) and W GT (k) are calculated using rule 5 to meet the prescribed electricity demands.

### C.Discussion

The rule based strategy represents an intuitive methodology aimed at achieving optimal operation. However, as suggested by Table V, the optimal strategy based on the approach in section IV is still able to perform better than this strategy by around 8.5%, in terms of operating cost. This clearly highlights the advantage of a systematic modeling and optimization procedure for the operation of a large scale, complex energy generation and distribution system such as a CCHP plant.

The proposed modeling and optimization procedure also allows quantification of the economic benefits of using TES and co-generation capabilities in a cooling and power plant. As indicated in Table V, the use of these features promises cost savings of around 19% for the test case under investigation. This would potentially translate into a satisfactory pay-back period for the initial capital expenditures incurred in the purchases and installations associated with these capabilities.

The high sensitivity of the optimal solution to the choice of initial conditions, as stated earlier, suggests the occurrence of multiple local minima. Our future work will focus on refinement of the optimization framework presented in this paper, by using global optimization algorithms such as multistart [13,14] to determine a more optimal operating point than the current best achieved using the local solvers.

### VI. CONCLUSIONS

The modeling and optimization of a campus CCHP plant was studied in this paper. Reduced order, simplified thermoeconomic models spanning multiple physical domains, were obtained from detailed, experimentally validated component models by using static and dynamic system identification techniques. A model-based, look-ahead optimization problem was then formulated to minimize the operating cost of the plant, by making use of forecasted electric and thermal demands. The proposed methodology was shown to achieve around 8.5% improvement over a rule-based optimization strategy.

