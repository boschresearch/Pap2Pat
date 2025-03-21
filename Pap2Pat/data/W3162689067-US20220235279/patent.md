# DESCRIPTION

## FIELD OF INVENTION

The present invention relates to the field of catalytic cracking and relates in particular to a method of reducing octane loss in catalytic cracking of gasoline in S-zorb plant.

## BACKGROUND ART

Catalytic cracking technology is one of the main methods of petroleum secondary processing. Through the joint action of heat energy and catalyst, the heavy oil is converted to cracking gas, gasoline and diesel oil, and then the olefins are converted into LPG by-products through adsorption desulfurization in S-zorb unit. S-zorb unit has low antiknock index loss, good octane number retention, low hydrogen consumption, low energy consumption, high yield of light oil and by-products rich in olefins. Therefore, the study of octane number loss in S-zorb unit catalytic cracking technology is conducive to achieve better cleaning and efficiency maximization of finished products, which is also one of the problems with important application value in chemical industry.

In order to reduce the octane loss of FCC gasoline in S-zorb unit, it is necessary to build a data analysis model to express the reaction process. The key point is to determine the variables that have influence on the octane number content of the product in the catalytic cracking process. From the production process of FCC gasoline in S-zorb unit, there are many variables that affect the octane number content of final product, mainly including raw material properties, adsorbent factors and unit operation conditions. The methods for determining the properties of raw materials, adsorbent factors and operating conditions of the plant are described below.

### (1) Raw Materials

The determination of raw material properties is mainly based on chemical mechanism. In actual production, by increasing the blending amount of residuum to increase the content of monocyclic aromatics, dealkylation can generate higher octane number olefin aromatics; By adjusting the variety of raw materials, reducing the sodium content and saturated hydrocarbon content of raw materials, increasing the density of raw materials to increase the octane number of products; and by dehydroaromation to generate high octane number components. Liu et al. (Analysis of factors affecting octane number loss of gasoline in S-zorb unit, petrochemical design, 2019) pointed out that in order to maintain liquid level reflux of refined gasoline and form secondary reaction, the increase of olefin reaction saturation depth will also increase octane number loss, so the refined gasoline reflux can be regulated to reduce this loss.

### (2) Adsorbent Factors

The determination of adsorbent factors is mainly based on chemical mechanism and operation experience. The main adsorbent active substances of S-zrob unit are nickel and zinc oxide. In the process of adsorbent reaction, the increase of sulfur and carbon retention rate of raw and regenerated adsorbents is beneficial to reduce the octane number loss of the product, and also affects the desulfurization rate; Zou et al. (The influence of Zn2SiO4 in S-zorb adsorbent on the octane number of gasoline and desulfurization capacity of adsorbent, Journal of petroleum processing, 2020) have studied that the loss of octane number can be reduced by increasing the mass fraction of zinc silicate phase in the adsorbent. At the same time, the increase of the outer surface of the adsorbent will also lead to the weakening of the adsorption capacity of the adsorbent for olefins, reducing the ratio of olefin saturation hydrogenation, thus reducing the loss of octane number.

### (3) Operating Conditions of the Plant

At present, in the application of S-zorb unit, the temperature, pressure and feed of the unit are usually regulated to achieve the optimal desulfurization rate and octane number retention. Firstly, the reaction temperature is an important aspect of the application of S-zorb device. Olefin hydrogenation saturation is a strong exothermic reaction, and the increase of reaction temperature will inhibit this reaction, so as to improve the octane number retention. Ma et al. (Optimization operation, technology application and research for reducing octane number loss of gasoline in S-zorb unit, 2020) have studied that the octane number retention of product increases first and then decreases with the increase of temperature, and the critical point is about 427° C. Secondly, reaction pressure is also an important aspect of regulation. Olefin hydrogenation saturation is a volume reduction reaction. The increase of reaction pressure will accelerate the reaction and increase the loss of octane number, but at the same time, the sulfur content of refined gasoline will decrease. To adjust the pressure at different points, it is necessary to find a balance between sulfur content and octane number content. In 2019, the set pressure of S-zorb unit system will be adjusted from 2.5 MPa to 2.45 Mpa, and the differential pressure of filter ME101 will rise to 11 kpa. Finally, in the aspect of feed, hydrogen oil ratio and mass space velocity affect the utility of the unit. Zhou et al. (Analysis and measures for the cause of large octane number loss in S-zorb unit, Yunnan chemical industry, 2019) pointed out that the hydrogen oil ratio, that is, the ratio of gasoline feed to circulating hydrogen, is adopted in S-zorb unit with a molar ratio. Under the condition of constant system pressure, the increase of hydrogen oil ratio will increase the rate of olefin hydrogenation saturation reaction, resulting in octane number loss, but at the same time it can also inhibit the adsorption of adsorbent; The increase of mass space velocity, which is the ratio of gasoline feed to gasoline storage, will inhibit the olefin hydrogenation saturation reaction and reduce the octane number loss, but also reduce the desulfurization rate. Therefore, in terms of feed, it needs to be adjusted accurately to achieve the balance of desulfurization and octane number retention.

To sum up, at present, the process modeling of catalytic cracking technology mainly relies on the existing chemical mechanism to select specific variables to build the model. Because the model based on the chemical mechanism has higher requirements for raw materials, amounts of unit operating points, complex reaction mechanism and nonlinear relationship between variables, the mathematical model based on the chemical principle cannot fully consider the process modeling. Because of the influence of operating point data, raw material data and catalyst data on the octane number loss of final product, the large octane number loss of product often occurs in the application of S-zorb catalytic cracking technology. Therefore, it is necessary to further model the catalytic cracking process of S-zorb unit and obtain the method to determine the catalytic cracking process of S-zorb unit, it provides technical support for the popularization and application of catalytic cracking technology in S-zorb unit.

## SUMMARY OF THE INVENTION

Employing data analysis to determine the variables of FCC gasoline process is conducive to obtain the ideal FCC process model and accurate optimal operating conditions, so as to accurately control the point of FCC technology, and reduce the octane loss in the process of FCC gasoline on the premise of meeting the desulfurization requirements. In view of this, in order to solve the problem of incomplete consideration of variables in the process modeling of catalytic cracking technology by using chemical principle, which leads to the increase of octane number loss, we take the octane number loss and sulfur content of the final product as dependent variables, take the operating point data, raw material data and catalyst data of S-zorb unit as independent variables, and establish a mathematical function on this basis to achieve the ideal FCC process model. By controlling the independent variable data, the dependent variable is gradually reduced, and the octane number loss in FCC gasoline process is reduced on the premise of meeting the desulfurization requirements, so as to reduce the octane number loss in refined oil, improve the quality of refined oil, and enrich the selection method of FCC technical operation variables.

The method of reducing octane loss in catalytic cracking of gasoline in S-Zorb plant comprising the following steps:

(1) Collecting equipment data and adjusting differences there among to construct initial data sample set;

i. Measuring and collecting a device data in a specified time interval, the device data comprising operation point data denoted with operating point variables a11, a12, . . . , a1m, a21, a22, . . . , a2m, . . . , aj1, aj2, . . . , ajm, raw material data denoted with raw material point variables b11, b12, . . . , b1n, b21, b22, . . . , b2n, . . . , b71, b72, . . . , b7n, catalyst data denoted with catalyst variables c11, c12, . . . , c1n, c21, c22, . . . , c2n, . . . , c41, c42, . . . , c4n, and product data denoted with product variables; the product data comprising product octane loss data x1, x2, . . . , xn and product sulfur content data y1, y2, . . . , yn; m being a sample number of the operating point variables and being positive integer; n being a sample number of the raw material variables, of the catalyst variables, and of the product variables, and being positive integer; j being a number of the operating point variables being positive integers; the operation point data comprising j of following variables : hydrogen oil ratio, pressure difference of reaction filter, pressure of reductor, flow rate of fluidized hydrogen in reductor, pressure of reactor, temperature of reactor, pressure difference of reactor, temperature of fluidized hydrogen in D-105, pressure of fluidized hydrogen in D-105, flow rate of fluidized hydrogen in D-105, pressure of back blowing hydrogen, pressure of stabilizing tower top, inlet temperature of tower top, outlet temperature of tower top, liquid level of tower top, temperature of tower top, liquid level of D-201 tower top reflux tank, temperature of dry gas out of device, temperature of gasoline out of the device, flow rate of gasoline out of the device, pressure of steam into the device, flow rate of steam into the device, flow rate to feed buffer tank, flow rate of fresh hydrogen, light hydrocarbon into the device, dry gas into the device, flow rate of dirty oil out of the device, temperature of fuel gas into the device, pressure of fuel gas into the device, flow rate of fuel gas into the device, flow rate of nitrogen into the device, pressure of nitrogen into the device, temperature of 1.0 MPa steam into the device, flow rate of circulating water into the device, flow rate of circulating water out of the device, flow rate of 0.3 MPa condensate water out of the device, flow rate of deaerated water into device, flow rate of non-purified air into the device, pressure of non-purified air into the device, pressure difference of D-107 reagent transfer line, flow rate of lifting nitrogen, and total flow of catalytic gasoline into the device; where in j>20;

The raw material data comprising sulfur content of raw material, octane number of raw materials, saturated hydrocarbon, olefin, aromatics, bromine number, and density;

The catalyst data comprising spent sorbent coke, spent sorbent sulfur, regenerated sorbent coke, and regenerated sorbent sulfur; the product data comprising sulfur content of product, octane number loss of product;

ii. Adjusting difference of collection frequency of the operation point data, raw material data, catalyst data and product data: for a sample at time k, it includes a1k, a2k, . . . , ajk, b1k, b2k, . . . , b7k, c1k, c2k, . . . , c4k, x1, x2, . . . , xk, y1, y2, . . . , yk; for

\({m = {40n}},{a_{ik} = \frac{\sum_{x = {k - {40}}}^{k}a_{ix}}{40}},\)

wherein i ranging from 1 to j, k=0,40,80, . . . , n; constructing initial data sample set;

(2) Collating data sample set;

i. Marking bad values outside a normal range of the operation point data due to measurement error; for example, the normal range of pressure difference of reaction filter is 10 KPa to 35 KPa; if a measured value is 40 KPa, then it is out of the normal range of pressure difference of reaction filter;

ii. Marking bad values with large error in the operation point data: calculating arithmetic mean

\({\overset{\_}{a_{\iota k}} = \frac{\left( {a_{i1} + a_{i2} + \ldots + a_{im}} \right)}{m}},\)

wherein i ranging from 1 to j, and residual error vi=aik−, wherein k ranging from 1 to m, of each type of data according to the pauta criterion, then calculating standard error ∂ by bessel

\({{{Formula}\mspace{14mu}\partial} = {\left( \frac{\sum_{i = 1}^{j}v_{i}^{2}}{j - l} \right)^{\frac{1}{2}} = \left\{ {\frac{1}{j - 1} \cdot \left\lbrack {{\sum_{i = 1}^{j}a_{ik}^{2}} - \frac{\left( {\sum_{i = 1}^{j}a_{ik}} \right)^{2}}{j}} \right\rbrack} \right\}^{\frac{1}{2}}}};\)

if residual error vi of measured value aik meets requirement |vi|=|aik−|>3∂, considering aik as the bad value with larger error;

iii. Processing the bad values in step i and step ii in the operation point data; counting average number of the bad values in each measured variable ai., defining the average number as incomplete data judgment point α. ai. means all the data of variable i. if number of the bad values in a variable ai. exceeds α, eliminating the variable ai.; if number of the bad values in a variable ai. being below α, making each bad value

\({a_{ik} = \frac{a_{{ik} - 1} + a_{{ik} + 1}}{2}};\)

(3) Employing local linear embedding to reduce dimension of independent variables, and trimming the independent variables to obtain reserved independent variables;

i. Employing local linear embedding to reduce dimension of independent variables in data sample set in step b to obtain a weight coefficient matrix; wherein the independent variables comprise the operation point variables, the raw material variables and the catalyst variables;

ii. Ordering the independent variables according to an absolute value of the first column of the weight coefficient matrix from largest to smallest, and reserving the top 10% as reserved independent variables;

(4) Calculating correlation coefficients of the reserved independent variables and removing variables with too high correlation coefficients to obtain main variables;

i. Calculating correlation coefficients Riu between the reserved independent variables in step c; the equation of definition of correlation coefficient is

\(R_{iu} = \frac{\sum\limits_{k = 1}^{m}{\left( {a_{ik} - \overset{\_}{a_{\iota k}}} \right)\left( {a_{uk} - \overset{\_}{a_{uk}}} \right)}}{\sqrt{\sum\limits_{k = 1}^{m}{\left( {a_{ik} - \overset{\_}{a_{\iota k}}} \right)^{2}{\sum\limits_{k = 1}^{m}\left( {a_{uk} - \overset{\_}{a_{uk}}} \right)^{2}}}}}\)

wherein i ranging from 1 to j, u ranging from 1 to j;

When absolute value of any Riu greater than 0.8, considering the correlation coefficient is too high, then calculating Σk=1j|Rik| and Σk=1j|Ruk|, if Σk=1j|Rik|>Σk=1j|Ruk|, eliminating ai.; finally obtaining main variables;

ii. Adding octane number of raw materials as one of the main variables to obtain: main11, main12, . . . , main1m, main21, main22, . . . , main2m, . . . , mainl1, mainl2, . . . , mainlm, l being a number of the main variables and being a positive integer;

(5) Constructing a BP neural network model of the main variables to obtain optimal octane loss prediction model;

i. Building a BP neural network with the main variables main11, main12, . . . , main1m, main21, main22, . . . , main2m, . . . , mainl1, mainl2, . . . , mainlm, in step d as an input layer, with predicted product sulfur content and predicted product octane number loss as an output layer, with a hidden layer and a number of hidden layer neuron as h=[√{square root over (l+2)}+5];

Taking 85% of the samples as training set randomly and the other 15% as testing set;

For a weight matrix Wa between the input layer and the hidden layer; employing linear weighted sum to obtain

\({Netin}_{i_{1}} = {\sum\limits_{j = 1}^{n}{{main}_{j}W_{a_{i_{1}j}}}}\)

of an i1th neuron of the hidden layer, wherein i1 ranging from 1 to h; obtaining an output of the i1th neuron

\(H_{i} = {f\left( {{Netin}_{i_{1}} - q_{a_{i_{1}}}} \right)}\)

wherein a hidden layer threshold vector qa by a activation sigmod function

\(\begin{matrix}
{{{f(x)} = \frac{1}{1 + {\exp\left( {- x} \right)}}};} & \;
\end{matrix}\)

For a weight matrix Wb between the hidden layer and the output layer, employing linear weighted sum to obtain

\({Outnetin}_{i_{1}} = {\sum\limits_{j = 1}^{n}{H_{j}W_{b_{i_{2}j}}}}\)

of the i2th neuron of the output layer, wherein i2 ranging from 1 to h; obtaining an output of the i2th neuron wherein an output layer threshold vector qb by inverse function:

\({{out}_{i_{1}} = {f^{- 1}\left( {{Outnetin}_{i_{2}} - q_{b_{i_{2}}}} \right)}};\)

for real output vectors z1, z2, obtaining a least square error of prediction result as:

\({E_{K} = {\frac{1}{2}{\sum\limits_{i_{2} = 1}^{2}\left( {{out}_{i_{2}} - z_{i_{2}}} \right)}}};\)

ii. Employing genetic algorithm to obtain optimal parameters of the neural network: firstly, constructing each individual by means of real coding to consist of the weight matrix Wa between the input layer and the hidden layer, the threshold vector qa of the hidden layer, the weight matrix Wb between the hidden layer and the output layer, and the threshold vector qb of the output layer, with a population size N; initiating the N individuals with random values, and setting a current number of iterations Nit=0; then performing selection, crossover and mutation; selecting each individual by employing a roulette algorithm, with probability of each individual e being selected and passed on to a next generation as:

\({p_{e} = \frac{f_{e}}{\sum\limits_{e = 1}^{N}f_{e}}},\)

with fitness value for fe being defined as:

\({f_{e} = {\frac{1}{2}{\sum\limits_{e = 1}^{2}\left( {{out}_{e} - z_{e}} \right)}}};\)

Employing a roulette algorithm for crossover operation, conducting selection operation by means of optionally selecting two individuals to be crossed over, and setting a crossover probability Pc=0.8; performing real value mutation, that is, performing bit inversion on a real code of the individual generated subsequent to the crossover operation with a mutation probability Pm=0.008, thereby generating a new individual; increasing the current number of iterations by one; continuing iteration of crossover operation, selection operation, and simple mutation;

For example, formula of cross between the g1 individual and the g2 individual at the j1 intersection position is as follows:

\(\left\{ \begin{matrix}
{{id_{g_{1}j_{1}}} = {{i{d_{g_{1}j_{1}}\left( {1 - {RAN}} \right)}} + {id_{g_{2}j_{1}}\ RAN}}} \\
{{id_{g_{2}j_{1}}} = {{i{d_{g_{2}j_{1}}\left( {1 - {RAN}} \right)}} + {id_{g_{1}j_{1}}\ RAN}}}
\end{matrix} \right.,\)

where RAN is random number in [0, 1];

Formula of the j2 mutation location of the g3 individual being as follows:

\({{id_{g_{3}j_{2}}} = \left\{ \begin{matrix}
{{{id_{g_{3}j_{2}}} + {\left( {{id_{g_{3}j_{2}}} - {id_{\max}}} \right) \times {f\left( N_{it} \right)}}},\ {r_{1} > {0.5}}} \\
{{{id_{g_{3}j_{2}}} + {\left( {{id_{\min}} - {id_{g_{3}j_{2}}}} \right) \times {f\left( N_{it} \right)}}},\ {r_{1} \leq {0.5}}}
\end{matrix} \right.},\)

wherein idmax being the upper bound of idgj, idmin being the lower bound of idgj, r1 being the random number in [0, 1]; f(Nit) being mutation formula:

\({{f\left( N_{it} \right)} = {r_{2}\left( {1 - \frac{N_{it}}{G_{\max}}} \right)}^{2}},\)

r2 being the random number in [0, 1], Nit being the current iteration number, Gmax being the maximum number of iterations;

Until one of stop conditions is reached:

First, the fitness of optimal individual fe stop rising;

Second, the current number of iterations Nit reaches the maximum iteration number Gmax;

Obtaining an optimal neural network with the weight matrix Wa between the input layer and the hidden layer, the threshold vector qa of the hidden layer, the weight matrix Wb between the hidden layer and the output layer, and the threshold vector qb of the output layer upon termination of the iteration;

iii. Applying the optimal initial weights Wa, Wb and thresholds qa, qb obtained by genetic algorithm to the neural network for prediction;

If EK is less than 0.1, saving the network model optimized by genetic algorithm, that is an optimal prediction model of octane number loss; if not, proceeding to step i;

(6) Employing the optimal octane loss prediction model to obtain predicted optimal operating conditions;

i. Employing random operation conditions value of the main1., main2., . . . , mainl. to simulate adjustment process according to the normal range of the operation point variables, to obtain random samples, under condition of keeping variables other than the main variables unchanged; employing the optimal prediction model to the random samples;

ii. Discarding a series of qualified samples according to the product sulfur content>10 ppm;

iii. Setting the decrease of octane number loss as weight of the qualified samples, to obtain optimal conditions by weighted average of the qualified samples operation conditions value.

Matlab software is used for the local linear embedding dimension reduction, the establishment of BP neural network model optimized by genetic algorithm and data fitting.

The technical conception of the invention is: through the operation variables determined by the method proposed in the invention, the specific optimal operation variable conditions are obtained based on the specific enterprise data, so as to reduce the octane number loss in the process of catalytic cracking gasoline in the S-zorb unit.

The beneficial effects of the invention are as follows:

(1) In different enterprises, S-zorb units may have different optimal reaction conditions due to different local gas pressure or temperature. Therefore, data analysis method can be used to obtain the method to reduce octane number loss in the process of FCC gasoline in S-zorb unit, and the influencing factors of octane number loss in S-zorb unit can be analyzed according to local conditions.

(2) There is a nonlinear relationship between the operating variables of S-zorb device. The invention uses local linear embedding as a nonlinear dimension reduction method, retains the weight relationship between the original variables, and overcomes the influence of subjective factors.

(3) S-zorb unit has high requirements for raw materials, many operation points and complex reaction mechanism. The invention adopts the BP neural network model optimized by genetic algorithm, which is essentially different from the commonly used method of determining the operation variables by using the chemical mechanism and is also a beneficial supplement to the existing method.

## EMBODIMENTS

The present invention will be further described with reference to the accompanying drawings:

As shown in FIG. 1, The method of reducing octane loss in catalytic cracking of gasoline in S-Zorb plant comprising the following steps:

(1) Collecting equipment data and adjusting differences thereamong to construct initial data sample set;

i. Measuring and collecting a device data in a specified time interval, the device data comprising operation point data denoted with operating point variables a11, a12, . . . , a1m, a21, a22, . . . , a2m, . . . , aj1, aj2, . . . , ajm, raw material data denoted with raw material point variables b11, b12, . . . , b1n, b21, b22, . . . , b2n, . . . , b71, b72, . . . , b7n, catalyst data denoted with catalyst variables c11, c12, . . . , c1n, c21, c22, . . . , c2n, . . . , c41, c42, . . . , c4n, and product data denoted with product variables; the product data comprising product octane loss data x1, x2, . . . , xn and product sulfur content data y1, y2, . . . , yn; m being a sample number of the operating point variables and being positive integer; n being a sample number of the raw material variables, of the catalyst variables, and of the product variables, and being positive integer; j being a number of the operating point variables being positive integers;

The operation point data comprising j of following variables: hydrogen oil ratio, pressure difference of reaction filter, pressure of reductor, flow rate of fluidized hydrogen in reductor, pressure of reactor, temperature of reactor, pressure difference of reactor, temperature of fluidized hydrogen in D-105, pressure of fluidized hydrogen in D-105, flow rate of fluidized hydrogen in D-105, pressure of back blowing hydrogen, pressure of stabilizing tower top, inlet temperature of tower top, outlet temperature of tower top, liquid level of tower top, temperature of tower top, liquid level of D-201 tower top reflux tank, temperature of dry gas out of device, temperature of gasoline out of the device, flow rate of gasoline out of the device, pressure of steam into the device, flow rate of steam into the device, flow rate to feed buffer tank, flow rate of fresh hydrogen, light hydrocarbon into the device, dry gas into the device, flow rate of dirty oil out of the device, temperature of fuel gas into the device, pressure of fuel gas into the device, flow rate of fuel gas into the device, flow rate of nitrogen into the device, pressure of nitrogen into the device, temperature of 1.0 MPa steam into the device, flow rate of circulating water into the device, flow rate of circulating water out of the device, flow rate of 0.3 MPa condensate water out of the device, flow rate of deaerated water into device, flow rate of non-purified air into the device, pressure of non-purified air into the device, pressure difference of D-107 reagent transfer line, flow rate of lifting nitrogen, total flow of catalytic gasoline into the device, flow rate of 1# catalytic gasoline into the unit, flow rate of 2# catalytic gasoline into the unit, flow rate of 3# catalytic gasoline into the unit, liquid level of raw material buffer tank, temperature of raw material into the unit, flow rate of raw material into the unit, outlet flow rate of raw material pump, hydrogen flow rate of hydrogen mixing point, inlet temperature of main pipe of raw material heat exchanger, pressure difference of main pipe of raw material heat exchanger, inlet temperature of heating furnace, outlet temperature of heating furnace, oxygen content pressure, furnace pressure, inlet temperature of reactor, outlet temperature of reactor, outlet pressure of radiation chamber , gas inlet pressure of main nozzle of heating furnace, pressure in front of main nozzle valve of heating furnace, outlet pressure of K-101 machine, D-104 pressure, liquid level, flow rate of destabilizer, temperature of destabilizer, D-121 pressure, liquid level, flow rate of top flare, temperature of top flare, reaction system pressure, temperature of reductor, flow rate of regeneration air, flow rate of regeneration cold nitrogen, flow rate of R-102 regenerator lifting nitrogen, flow rate of regeneration cold nitrogen generator pressure, top and bottom differential pressure, top flue gas temperature, lower temperature, receiver differential pressure, storage capacity, oxygen content of regeneration flue gas, D-110 top and bottom differential pressure, R-102 transfer agent line differential pressure, flare gas discharge flow rate, new hydrogen flow rate into the unit, product gasoline flow rate out of the unit, cumulative flow of raw material into the unit, cumulative flow of waste hydrogen discharge, cumulative flow of flare gas discharge, inlet manifold temperature of E-101 shell side, temperature of E-101 tube side inlet main pipe, pressure of E-101 tube side inlet main pipe, temperature of E-101 shell side outlet main pipe, pressure of E-101 shell side outlet main pipe, D-204 liquid level, D-101 raw material buffer tank pressure, D-203 fuel gas inlet pipe temperature, top outlet pipe temperature, outlet fuel gas flow rate, top outlet pipe, bottom liquid level, D-202 liquid level, D-201 water drum boundary, D-125 liquid level, D-125 pressure , D-124 liquid level, D-124 pressure, D-123 steam outlet flow rate, condensate tank liquid level, condensate inlet flow rate, D-122 liquid level, inlet pipe temperature, top outlet pipe temperature, D-121 water level, D-114 liquid level, D-113 top vent line flow rate, D-110 steam coil inlet flow rate, bottom pressure, bottom fluidizing nitrogen flow rate, D-109 pressure, adsorbent level, loose air flow rate, D-107 lower loose air flow rate, D-107 temperature, D-107 top pressure, D-107 bottom pressure, bottom discharge slide valve differential pressure, bottom slide valve, D-106 pressure instrument nozzle back blowing air flow rate, temperature, hot nitrogen flow rate, D-105 lower cone loose air flow rate, upper jumper loose air flow rate, D-103 bottom liquid level, D-102 temperature, D-101 dehydrator liquid level, C-201 lower feed pipe temperature, C-201#37 layer tray temperature, A-202 a/b outlet main pipe temperature, A-201 outlet main pipe temperature, EH-101 outlet, D-110 top pressure, pressure differential in regenerator receiver and LH, pressure differential in regeneration feed tank and LH, preheated air outlet pressure, PDI-2107 point, flue gas radiation chamber temperature, flue gas outlet temperature of convection chamber, pressure of hydrogen mixing point at outlet of recycle hydrogen compressor, flow rate of recycle hydrogen to lock hopper leg, D-113 pressure, flow rate of hot recycle gas to R-101 bottom riser, differential pressure of hot nitrogen filter ME-113, differential pressure of cold nitrogen filter ME-114, pressure of flue gas inlet of preheated air , temperature of flue gas inlet of preheated air, pressure of air outlet, temperature of air outlet, bypass flow rate of feed control valve, emergency hydrogen main , emergency hydrogen flow rate to R-101, emergency hydrogen flow rate to D-102, liquid level of flare drum D-206, inlet pressure of blower, dew point temperature of non-purified air after drying, differential pressure between reactor receiver and LH, differential pressure of make-up hydrogen of back blowing gas collector, low pressure hot nitrogen pressure, flow rate of return pipe at outlet of make-up hydrogen compressor, liquid level of lock hopper, oxygen content, top pressure, hydrocarbon content control, hydrogen charging line pressure control, nitrogen filter outlet gas flow rate, hydrogen filter outlet gas flow rate, R-102 lower pressure, bed adsorbent level density, bottom nozzle pressure difference, nitrogen line pressure behind bottom discharge slide valve, bottom slide valve differential pressure, bottom cone temperature, ventilation baffle 1# temperature, ventilation baffle 3# temperature, R-101 lower bed pressure drop, upper bed pressure drop, top reaction product outlet pipe temperature, the upper and lower bottom grilles pressure differential, temperature in the middle of the bed, pressure in the middle of the bed, temperature in the lower part of the bed, pressure in the outlet main pipe of P-105 a/b, differential pressure in the inlet filter of P-101 b, pressure differential in the inlet filter of P-101 a, t pressure differential in the filters of ME-115, pressure differential in the filters of ME-112, pressure differential in the filters of ME-109, pressure differential in the filters of ME-108, pressure differential in the filters of ME-105, pressure differential in the inlet and outlet of ME-104, pressure differential in the inlet and outlet of ME-103, pressure in the back blowing main pipe of ME-101, pressure in the back blowing main pipe of ME-103, pressure from the outlet of K-103 to K-101 outlet pipe, inlet pressure of K-103 a/b, temperature of K-103 a/b, outlet pressure of K-103 a/b, temperature of K-103 a/b, inlet pressure of K-102 a/b, temperature of K-102 a/b, outlet pressure of K-102 a/b, temperature of K-102 a/b, left exhaust temperature of K-101 a/b, right exhaust temperature of K-101 a/b, left exhaust pressure of K-101 a/b, right exhaust pressure of K-101 a/b, inlet temperature of K-101 a/b, pressure of K-101 a/b, HV2533 manual operator, F-101 long light line pressure, circulating hydrogen outlet pipe temperature, radiation chamber bottom pressure, radiation chamber outlet pressure, outlet main pipe pressure, outlet branch pipe 1# temperature, outlet branch pipe 2# temperature, outlet branch pipe 3# temperature, outlet branch pipe 4# temperature, EH-103 inlet flow rate, heating element temperature, heating element humidity, EH-102 heating element a beam temperature, EH-102 heating element b beam temperature, EH-102 outlet air main pipe temperature, EH-101 heating element temperature, EH-101 heating element humidity, E-203 reboiler tube side outlet condensate flow rate, E-203 shell side outlet pipe temperature , E-205 shell side outlet pipe temperature, E-205 tube side inlet pipe temperature, E-106 tube side inlet pipe temperature, E-106 tube side outlet pipe temperature, E-105 tube side outlet pipe temperature, E-101 shell side inlet main pipe temperature, filter ME-101 outlet temperature, filter ME-101 differential pressure, filter ME-101 back blowing pressure, filter ME-101 preheater outlet air temperature, convection chamber outlet temperature, D-121 sulfur-containing sewage displacement, D-201 sulfur-containing sewage displacement, D-121 sulfur-containing sewage liquid level, D-201 sulfur-containing sewage liquid level, E-101abc tube side outlet temperature, E-101abc shell side outlet temperature, E E-101def tube side outlet temperature, E-101def shell side outlet temperature, E-101 shell side inlet main pipe temperature, E-101 shell side outlet main pipe temperature, reactor linear velocity, storage capacity, mass space velocity, material level, heating furnace efficiency, hydrocracking light naphtha inlet flow rate, hydrocracking light naphtha cumulative flow, gasoline product degassing split flow rate, gasoline product degassing split cumulative flow, 8.0 MPa hydrogen to recycle hydrogen compressor inlet flow rate, 8.0 MPa hydrogen to recycle hydrogen compressor cumulative flow, 8.0 MPa hydrogen flow rate, 8.0 MPa hydrogen cumulative flow; where in j>20;

The raw material data comprising sulfur content of raw material, octane number of raw materials, saturated hydrocarbon, olefin, aromatics, bromine number, and density;

The catalyst data comprising spent sorbent coke, spent sorbent sulfur, regenerated sorbent coke, and regenerated sorbent sulfur; the product data comprising sulfur content of product, octane number loss of product;

ii. Adjusting difference of collection frequency of the operation point data, raw material data, catalyst data and product data: taking the operation point data corresponding to the product data as mean value measuring in previous two hours, corresponding to the product data, the raw material data, and the catalyst data measured at that time, and constructing initial data sample set;

(2) Collating data sample set;

i. Marking bad values outside a normal range of the operation point data due to measurement error; for example, the normal range of pressure difference of reaction filter is 10 KPa to 35 KPa; if a measured value is 40 KPa, then it is out of the normal range of pressure difference of reaction filter;

ii. Marking bad values with large error in the operation point data: calculating arithmetic mean

\({\overset{\_}{a_{\iota k}} = \frac{\left( {a_{i1} + a_{i2} + \ldots + a_{im}} \right)}{m}},\)

wherein i ranging from 1 to j, and residual error vi=aik−, wherein k ranging from 1 to m, of each type of data according to the pauta criterion, then calculating standard error ∂ by bessel

\({{{formula}\mspace{14mu}\partial} = {\left( \frac{\sum\limits_{i = 1}^{j}v_{i}^{2}}{j - 1} \right)^{\frac{1}{2}} = \left\{ {\frac{1}{j - 1} \cdot \left\lbrack {{\sum\limits_{i = 1}^{j}a_{ik}^{2}} - \frac{\left( {\sum\limits_{i = 1}^{j}a_{ik}} \right)^{2}}{j}} \right\rbrack} \right\}^{\frac{1}{2}}}};\)

if residual error vi of measured value aik meets requirement |vi|=|aik−|>3∂, considering aik as the bad value with larger error;

iii. Processing the bad values in step i and step ii in the operation point data; counting average number of the bad values in each measured variable ai., defining the average number as incomplete data judgment point α, if number of the bad values in a variable ai. exceeds α, eliminating the variable ai.; if number of the bad values in a variable ai. being below α, making each bad value

\({a_{ik} = \frac{a_{{ik} - 1} + a_{{ik} + 1}}{2}};\)

(3) Employing local linear embedding to reduce dimension of independent variables, and trimming the independent variables to obtain reserved independent variables;

i. Employing local linear embedding to reduce dimension of independent variables in data sample set in step b to obtain a weight coefficient matrix; wherein the independent variables comprise the operation point variables, the raw material variables and the catalyst variables; employing the local linear embedding method to reduce the dimension of the independent variables in step b:

Step1, the locally linear range uses the K-nearest neighbor principle. because of locally linearity, representing each data point xi by a linear combination of its nearest neighbor data points. that is xi=Σj=1kwjixji, Ni=knn(xi, k), Ni=[x1i, . . . , xki], where wi is k×1 column vector, wji is row j of wi, xji is the j th nearest neighbor to xi, (1≤j≤k), wi=[w1i, . . . , wki]T, xi=[x1i, . . . , xDi]T, where D is the dimension of xi;

Step2,to solve the weight coefficient matrix means to solve the constrained optimization problem as follows: arg min Σi=1N||xi−Σj=1kwjixji||2, s.t.Σj=1kwji=1;

Step3, thus, deducing the expression of the weight coefficient matrix:

ϕ(w)=Σi=1N||xi−Σj=1kwjixji||2=Σi=1N||xi−Σj=1kwji(xi−xji)||2=Σi=1N||Xi−Σj=1kwi(Xi−Ni)||2, Xi=[xi, . . . , xi], Ni=[x1i, . . . , xki]=Σi=1NwiT(Xi−N)T(Xi−N)wi;

Step4, then viewing Si as local covariance matrix, Si=(Xi−Ni)T(Xi−Ni). viewing it as: ϕ(w)=Σi=1NwiTSiwi, and employing the lagrange multiplier: L(wi)=wiTSiwi+l(wiT1k−1), where 1k is k×1 column vector with entries of 1; taking derivative of L(wi):

\({\frac{\partial{L\left( w_{i} \right)}}{\partial w_{i}} = {{{2S_{i}w_{i}} + {l1_{k}}} = 0}},{{w_{i} = \frac{S_{i}^{- 1}1_{k}}{1_{k}^{T}S_{i}^{- 1}1_{k}}};}\)

Step5, the low-dimensional representation should have the same locally geometric property, so employing same linear representation expression to finally form the quadratic form; therefore, mapping a low-dimensional space to solve the following constrained optimization problem:

\({{\arg{\min\limits_{Y}{y(Y)}}} = {\sum\limits_{i = 1}^{N}{{y_{i} - {\sum\limits_{j = 1}^{k}{w_{ji}y_{ji}}}}}^{2}}},{{s.t.{\sum\limits_{i = 1}^{k}{y_{i}y_{i}^{T}}}} = {NI}_{d \times d}},\)

the output result is the d×N matrix Y=[y1, y2, . . . , yN], and low-dimensional space vectors comprise Y;

Step6, employing sparse matrix W to represent w: Σj=1Nwjiyji=Σj=1kwjiyji=YWi,

\(\left\{ {\begin{matrix}
{{W_{ji} = w_{ji}},} & {j\mspace{14mu}{is}\mspace{14mu}{the}\mspace{14mu}{nearest}\mspace{14mu}{neighbor}\mspace{14mu}{to}\mspace{14mu} i} \\
{{W_{ji} = 0},} & {others}
\end{matrix},} \right.\)

where Wi is the i column of W(N×N), Ii is the i column of unit matrix I(N×N), yi is the i column of Y; so, y(Y)=Σi=1N||Y(li−Wi)||2=tr[Y(I−W)(I−W)TYT];

Step7, making M=(I−W)(I−W)T; employing the lagrange multiplier again: L(Y)=YMYT+l(YYT−NI); taking derivative of L(Y):

\({\frac{\partial L}{\partial Y} = {{{2{MY}^{T}} + {2{lY}^{T}}} = 0}},{{{2{MY}^{T}} = {l^{\prime}Y^{T}}};}\)

so Y is the matrix composed of the eigenvectors of M; Step8, to reduce the data to D dimension, taking the minimum d eigenvectors corresponding to non-zero Eigen values of M; generally, the first minimum Eigen value is close to 0, so abandon it;

Step9, obtaining the weight coefficient matrix by taking the eigenvectors corresponding to the previous [2, d+1] eigen values from the smallest to the largest;

ii. Ordering the independent variables according to an absolute value of the first column of the weight coefficient matrix from largest to smallest, and reserving the top 10% as reserved independent variables;

(4) Calculating correlation coefficients of the reserved independent variables and removing variables with too high correlation coefficients to obtain main variables;

i. Calculating correlation coefficients Riu between the reserved independent variables in step c; the equation of definition of correlation coefficient is

\(R_{iu} = \frac{\sum_{k = 1}^{m}{\left( {a_{ik} - \overset{\_}{a_{ik}}} \right)\left( {a_{uk} - \overset{\_}{a_{uk}}} \right)}}{\sqrt{\sum_{k = 1}^{m}{\left( {a_{ik} - \overset{\_}{a_{ik}}} \right)^{2}{\sum_{k = 1}^{m}\left( {a_{uk} - \overset{\_}{a_{uk}}} \right)^{2}}}}}\)

wherein i ranging from 1 to j, u ranging from 1 to j;

When absolute value of any Riu greater than 0.8, considering the correlation coefficient is too high, then calculating Σk=1j|Rik| and Σk=1j|Ruk|, if Σk=1j|Rik|>Σk=1j|Ruk|, eliminating ai. ; finally obtaining main variables;

ii. Adding octane number of raw materials as one of the main variables to obtain: main11, main12, . . . , main1m, main21, main22, . . . , main2m, . . . , mainl1, mainl2, . . . , mainlm, l being a number of the main variables and being a positive integer;

(5) Constructing a BP neural network model of the main variables to obtain optimal octane loss prediction model;

i. Building a BP neural network with the main variables main11, main12, . . . , main1m,main21, main22, . . . , main2m, . . . , mainl1,mainl2, . . . , mainlm, in step d as an input layer, with predicted product sulfur content and predicted product octane number loss as an output layer, with a hidden layer and a number of hidden layer neuron as h=[√{square root over (l+2)}+5];

Taking 85% of the samples as training set randomly and the other 15% as testing set;

For a weight matrix Wa between the input layer and the hidden layer; employing linear weighted sum to obtain

\({Netin}_{i_{1}} = {\sum\limits_{j = 1}^{n}{{main}_{j}W_{a_{i_{1}j}}}}\)

of an i1th neuron of the hidden layer, wherein i1 ranging from 1 to h; obtaining an output of the i1th neuron

\(H_{i} = {f\left( {{Netin}_{i_{1}} - q_{a_{i_{1}}}} \right)}\)

wherein a hidden layer threshold vector qa by a activation sigmod function

\(\begin{matrix}
{{{f(x)} = \frac{1}{1 + {\exp\left( {- x} \right)}}};} & 
\end{matrix}\)

For a weight matrix Wb between the hidden layer and the output layer, employing linear weighted sum to obtain

\({Outnetin}_{i_{1}} = {\sum_{j = 1}^{n}{H_{j}W_{b_{i_{2}j}}}}\)

of the i2th neuron of the output layer, wherein i2 ranging from 1 to h; obtaining an output of the i2th neuron wherein an output layer threshold vector qb by inverse function:

\({{out}_{i_{1}} = {f^{- 1}\left( {{Outnetin}_{i_{2}} - q_{b_{i_{2}}}} \right)}};\)

for real output vectors z1, z2, obtaining a least square error of prediction result as:

\({E_{K} = {\frac{1}{2}{\sum\limits_{i_{2} = 1}^{2}\left( {{out}_{i_{2}} - z_{i_{2}}} \right)}}};\)

ii. Employing genetic algorithm to obtain optimal parameters of the neural network: firstly, constructing each individual by means of real coding to consist of the weight matrix Wa between the input layer and the hidden layer, the threshold vector qa of the hidden layer, the weight matrix Wb between the hidden layer and the output layer, and the threshold vector qb of the output layer, with a population size N; initiating the N individuals with random values, and setting a current number of iterations Nit=0; then performing selection, crossover and mutation; selecting each individual by employing a roulette algorithm, with probability of each individual e being selected and passed on to a next generation as:

\({p_{e} = \frac{f_{e}}{\sum_{e = 1}^{N}f_{e}}},\)

with fitness value for fe being defined as:

\({f_{e} = {\frac{1}{2}{\sum\limits_{e = 1}^{2}\left( {{out}_{e} - z_{e}} \right)}}};\)

Employing a roulette algorithm for crossover operation, conducting selection operation by means of optionally selecting two individuals to be crossed over, and setting a crossover probability Pc=0.8; performing real value mutation, that is, performing bit inversion on a real code of the individual generated subsequent to the crossover operation with a mutation probability Pm=0.008, thereby generating a new individual; increasing the current number of iterations by one; continuing iteration of crossover operation, selection operation, and simple mutation;

For example, formula of cross between the g1 individual and the g2 individual at the j1 intersection position is as follows:

\(\left\{ \begin{matrix}
{{id_{g_{1}j_{1}}} = {{i{d_{g_{1}j_{1}}\left( {1 - {RAN}} \right)}} + {id_{g_{2}j_{1}}\ RAN}}} \\
{{id_{g_{2}j_{1}}} = {{i{d_{g_{2}j_{1}}\left( {1 - {RAN}} \right)}} + {id_{g_{1}j_{1}}\ RAN}}}
\end{matrix} \right.,\)

where RAN is random number in [0, 1];

Formula of the j2 mutation location of the g3 individual being as follows:

\({id_{g_{3}j_{2}}} = \left\{ {\begin{matrix}
{{{id_{g_{3}j_{2}}} + {\left( {{id_{g_{3}j_{2}}} - {id_{\max}}} \right) \times {f\left( N_{it} \right)}}},{r_{1} > {0.5}}} \\
{{{id_{g_{3}j_{2}}} + {\left( {{id_{\min}} - {id_{g_{3}j_{2}}}} \right) \times {f\left( N_{it} \right)}}},{r_{1} \leq {0.5}}}
\end{matrix},} \right.\)

wherein idmax being the upper bound of idgj, idmin being the lower bound of idgj, r1 being the random number in [0, 1]; f(Nit) being mutation formula:

\({{f\left( N_{it} \right)} = {r_{2}\left( {1 - \frac{N_{it}}{G_{\max}}} \right)}^{2}},\)

r2 being the random number in [0, 1], Nit being the current iteration number, Gmax being the maximum number of iterations;

Until one of stop conditions is reached:

First, the fitness of optimal individual fe stop rising;

Second, the current number of iterations Nit reaches the maximum iteration number Gmax;

Obtaining an optimal neural network with the weight matrix Wa between the input layer and the hidden layer, the threshold vector qa of the hidden layer, the weight matrix Wb between the hidden layer and the output layer, and the threshold vector qb of the output layer upon termination of the iteration;

iii. Applying the optimal initial weights Wa, Wb and thresholds qa, qb obtained by genetic algorithm to the neural network for prediction;

If EK is less than 0.1, saving the network model optimized by genetic algorithm, that is an optimal prediction model of octane number loss; if not, proceeding to step i;

(6) Employing the optimal octane loss prediction model to obtain predicted optimal operating conditions;

i. Employing random operation conditions value of the main1., main2., . . . , mainl. to simulate adjustment process according to the normal range of the operation point variables, to obtain random samples, under condition of keeping variables other than the main variables unchanged; employing the optimal prediction model to the random samples;

ii. Discarding a series of qualified samples according to the product sulfur content>10 ppm;

iii. Setting the decrease of octane number loss as weight of the qualified samples, to obtain optimal conditions by weighted average of the qualified samples operation conditions value.

Employing the method of reducing octane loss in catalytic cracking of gasoline in S-Zorb plant is helpful to analyze the influencing factors of the octane loss of S-Zorb unit, obtain the optimal conditions of main operating variables, and reduce the octane loss of the unit.

The content described in the embodiments of the present specification is merely an enumeration of the implementation forms of the inventive concept, and the scope of the present invention shall not be construed as being limited to the specific forms expressed in the embodiments. Equivalent technical means that a skilled person of the art may construct from the conception of the present invention shall fall under the scope of the present invention.

