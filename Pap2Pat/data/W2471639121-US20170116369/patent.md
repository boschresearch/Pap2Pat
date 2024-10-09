# DESCRIPTION

## BACKGROUND OF THE INVENTION

The present invention relates to a computational framework that identifies the optimum overall stoichiometry and selects for (non-)native metabolic reactions for optimizing the converting source metabolite(s) and target product(s).

Microbial metabolism describes the full range of enzymatic conversions of carbon substrates to cellular biomass precursors, energy equivalents and biochemical molecules. Metabolic engineering harnesses this metabolic machinery for converting feedstock substrates to a growing range of products [1-3]. Recent advances in multiplex engineering (e.g., MAGE [4]), efficient genome-editing (e.g., CRISPR-Cas [5,6]) and genome-wide regulation of gene expression through small RNAs [7] have brought closer the dream of “designer cells” that can catalyze any tailor-made stoichiometry-balanced metabolic conversion with high specificity and control [8].

Existing computational procedures for the de novo pathway design rely on either optimization techniques or graph-search approaches. Linear Programming (LP) and Mixed Integer Linear Programming (MILP) approaches for pathway design, in general, extract a minimal, stoichiometry-balanced sub-network that converts a source metabolite to a target chemical with high yield [9]. While early work was restricted to design pathways for small-to-medium size networks [10-12], recent procedures have reached up to genome-scale size [13-15] often using the concept of elementary modes [16] and comprehensive databases of reactions [17-20]. Generally, pathways are identified that maximize product yield given a single carbon substrate [21] without considering co-substrates, co-products, or complex overall stoichiometries.

Graph-based pathway design approaches [22] begin from the target chemical and iteratively retrace back a path to the source metabolite using a retrosynthetic algorithm. Using a depth-first search, variations of the k-shortest path approach have been used to design and classify pathways based on their length [23], negativity of free energy of change for each reaction step [24], or use of intermediate metabolites with the fewest connections [25]. Graph-search approaches can be supplemented with “reaction-rules” that can suggest de novo reaction steps between any two metabolites often absent in existing databases (e.g., BNICE [26], XTMS [27], GEM-Path [28]). In most cases, the consumption (or production) of cofactors and possibly co-reactants or co-products required for these pathways to operate is not directly tracked [29]. As a result, these procedures are often coupled with a post-processing step where a Flux Balance Analysis (FBA) is performed to select pathways that are stoichiometry-balanced and maximize the production of target chemicals. As with LP or MILP based approaches, generally mostly linear pathway topologies are traced.

Powerful as these approaches have been, their primary shortcoming lies in the fact that they aim to trace pathways connecting a single substrate (A) to a single product (B). Metabolic conversions do not generally involve linear paths from substrate to product [21]. Most metabolic engineering tasks recruit many more metabolites and reactions than the ones along the main carbon conversion path. Cofactor usage, co-reactant choices as well as stoichiometric ratios are important decision variables during the pathway design stage. It is the overall stoichiometry that globally captures the overall goal rather than just the origin and destination molecules. This overall stoichiometry can interact in complex ways with the rest of the metabolites forming highly non-intuitive networks constrained by thermodynamics.

The primary object, feature or advantage of the present invention is the development of a stoichiometry and pathway design tool that optimizes the overall stoichiometry (e.g., aA+cC→bB+dD) by exploring exhaustively co-reactant/co-product combinations. The coefficients in the overall stoichiometry (i.e., a, b, c and a) are critical as they ultimately define the carbon and energy efficiency of the conversion while meeting thermodynamic feasibility.

Yet another object, feature and advantage of the present invention is to directly include economic considerations implied by the prices or reactant and product molecules in the optimization formulation for designing the overall stoichiometry.

A further object, feature and advantage of the present invention is to identify intervening reactions from a universal database that link the chosen reactants and products in the stoichiometric ratios as guided by the overall stoichiometry of conversion.

Yet another object, feature and advantage of the present invention is that requirements on the minimality of size of the network and negativity of the free energy of change of each individual reaction step can also be imposed to help rank-order all identified designs. One or more of these and/or other objects, features and advantages of the present invention will become apparent after review of the following detailed description of the disclosed embodiments and appended claims. No single embodiment need exhibit all of these objects, features, or advantages. It is contemplated that different embodiments may have different objects, features, or advantages.

## SUMMARY OF THE INVENTION

The present invention provides a computational framework for designing optimum overall stoichiometry, and intermediate metabolic reaction steps of achieving the conversion between a source and target metabolite with alternate co-reactants/co-products combination. The source and target metabolites, and the combination of co-reactants/co-products are selected from a universal database, and may range from electron acceptor pairs such as iron(III)/iron(II) driving the oxidation of methane to liquid biofuels, to platform biochemicals such as 2,3-butanediol and 3-hydroxypropionate. Likewise, the set of intermediate biotransformations is selected from a curated database with over 6000 reactions. Combinatorial optimization is employed in the first step to identify the stoichiometric coefficients of the reactant and product metabolites in the overall conversion while maintaining thermodynamic feasibility considerations. In general, the optimization objective is to identify an overall conversion that maximally utilizes a limiting carbon resource towards a target product, while alternate fitness functions such as maximizing the difference between the prices of the target products and the cost of the reactants can also be explored. Participating metabolites could be known a priori or sourced from the database of metabolites. The second step searches through the universal database of elementally and charged balanced reactions to extract a (generally minimal) set of reactions that conform to the identified overall conversion stoichiometry identified under the first step. Additional constraints, such as minimality of reactions with positive Gibbs free energy change and minimizing the number of heterologous reactions in the optimal network can be included in the optimal formulation. The present invention was implemented for three separate case studies of increasing complexity. The first one exhaustively identifies networks that convert glucose to acetate while conserving all carbon atoms with no provision for any additional co-reactants or co-products in the spirit of the recent study by Bogorad and co-workers [30]. The second study, explores the combined use of methanol and carbon dioxide for the production of stoichiometry-feasible C2+ products. The third study, aims at designing thermodynamically feasible overall stoichiometries for fixing methane to acetate and other C2+ co-products. The two-stage procedure recapitulates existing pathway designs [31-34] and identifies novel pathway topologies inaccessible to existing algorithms. Overall conversion stoichiometries and pathway designs span a range of complex network topologies and provide valuable insight as to how the overall conversion pathway changes in response to alternate co-reactant and/or co-product scenarios.

According to one aspect, a computational method of designing de novo metabolic networks includes the steps of determining the overall stoichiometry of conversion for converting source metabolite(s) to the target product(s) by exhaustively exploring co-reactant/co-product combinations and their respective stoichiometric coefficients and identifying an optimal network of intervening metabolites and reactions from a database that link the chosen reactants and products in the desired stoichiometric ratios.

## DETAILED DESCRIPTION OF THE PREFERRED EMBODIMENTS

The present invention provides a computational framework that identifies the optimum overall stoichiometry and selects for (non-)native metabolic reactions for optimizing the converting source metabolite(s) and target product(s). Preferably the methods are computer implemented or computer assisted or otherwise automated. The term “computational” as used herein should be construed broadly to include, but not to be limited to, any number of electronic devices suitable for practicing the methodology described herein. It is further to be understood that because the invention relates to computer-assisted modeling that the scope of the invention is broader than the specific embodiments provided herein and that one skilled in the art would understand how to apply the present invention in different environments and contexts to address different problems in part due to the predictability associated with computer implementations. Where the methods are computer implemented in part, it is to be understood that instructions for performing the methods may be stored in whole or in part on computer readable non-transitory medium and the instructions may be executed on or by a computing device. Similarly, data may be stored in whole or in part on a computer readable non-transitory medium.

Despite enormous progress over the past few years, available pathway-design procedures generally are restricted to only (near) linear routes from the source (or metabolite in the host metabolome) to the target metabolite. Linear pathway designs miss cyclic networks with potential for higher efficiency (both carbon and energy) of production (e.g., 100% carbon efficiency in conversion of glucose to acetyl-CoA [30]). In addition, by restricting the degrees of freedom to just the source and target metabolite, the identification of alternative co-reactants/co-products combinations are ignored. While post-processing efforts restore stoichiometry-balance of pathways [28], this may lead to designs with suboptimal carbon and energy efficiencies.

The present invention formulates a two-step computational procedure (optStoic+minRxn/minFlux) for designing de novo networks that match an overall stoichiometry of chemical transformation. Performance criteria on the designed pathways (e.g., carbon yield/energy efficiency, pathway ΔG etc.) can systematically be imposed and rank-order synthetic pathways according to the design objective. Implementation for of this invention in three pathway design studies identified non-intuitive designs with improved efficiencies. Specifically, multiple alternatives for non-oxidative glycolysis are generated and non-intuitive ways of co-utilizing carbon dioxide with methanol are revealed for the production of C2+ metabolites with higher carbon efficiency. Likewise, several non-intuitive solutions were identified for driving forward the thermodynamically unfavorable conversion of methane to acetate and other C2+ metabolites.

### 1.1 Material and Methods

The optimization procedure is divided in two steps (see FIG. 1). The first step identifies the stoichiometric coefficients of the reactant and product metabolites in the overall conversion while maintaining thermodynamic feasibility considerations. The second step, searches through a database of elementally and charged balanced reactions to extract a (generally minimal) set of reactions that conform to the identified overall conversion stoichiometry identified under the first step. The following section describes each step in detail.

**Step 1: Determining Optimal Reactant and Product Combination and Overall Stoichiometry**

The procedure begins with an optimization task that establishes the maximum achievable yields of the envisioned bioconversion subject to thermodynamic restrictions. At this stage, not just the overall conversion stoichiometry but also some of the co-reactants and/or byproducts are yet to be determined. Generally, the goal during this scoping phase is to identify an overall conversion that maximally utilizes a limiting carbon resource towards a target product while the intervening reaction steps are left at this stage unexplored. Ancillary considerations may include (i) co-utilization of other carbon substrates (e.g., gaseous reactants), (ii) possible co-production of valuable by-products, (iii) co-generation of redox resources for biomass, etc. Both the identity of some of the reactants and products as well as the overall stoichiometry are degrees of freedom that can be optimized towards meeting the above stated performance objectives.

This optimization task requires access to a database of metabolites along with specific data for each one of them. In this paper we assembled a database of 5,753 metabolites extracted from the MetRxn database [35] (see Supplementary File 51). The following parameters are introduced that keep track of the elemental composition, charge information and free energy of formation data needed to describe the optimization problem:


- - n_(iq): \# of atoms of element q in metabolite i
  - e_(i): charge of metabolite i \[36\]  
    ΔG_(i)^(f): Transformed free energy of formation (at 25° C. and 0.1M
    ionic strength) of metabolite i \[37\] where i=1, . . . , N is the
    set I of metabolites present in the database and qεQ is the set of
    elements found in the metabolites (i.e., C, O, N, P, S, H, Fe, etc.)
    (see Supplementary File S1 for dataset).

For the sake of simplicity of presentation the optimization formulation is derived for the following bimolecular stoichiometry as shown in FIG. 1:

aA+cC→>bB+dD

Using this representation either all the metabolites participating in the reaction are known a priori implying that all coefficients are positive and non-zero or the presence of some of them is uncertain in which case the corresponding stoichiometric coefficients are allowed to assume a value of zero. Obviously, the list of reactants and products does not have to be restricted to two. More complex overall stoichiometries can be put forth with positive coefficients denoting products and negative reactants. Only one of the stoichiometric coefficients needs to be fixed to a finite value to provide a scaling for the remaining ones. Generally, we fix either the coefficient of the limiting carbon substrate or the primary product. By fixing this coefficient the presence of the corresponding reactant or product in the overall conversion is guaranteed. Note that setting the stoichiometric coefficient of a one-carbon molecule to one may not ensure that all other coefficients can assume integer values due to the balances on all other elements. However, all determined coefficients could be suitably scaled up to obtain an integer-only stoichiometry for all metabolites. The performance criteria of the overall conversion may involve (i) maximum yield for primary product B (i.e. max b while a=fixed), (ii) maximum co-utilization of free reactant C (max c, b=fixed) for a given product yield, (iii) minimum formation of by-product D (min d while b=fixed) or combinations thereof. The overall optimization formulation for Step 1 is as follows (optStoic):

\(\underset{({a,b,c,d})}{Maximize}\mspace{14mu} {f\left( {a,b,c,d} \right)}\mspace{14mu} ({optStoic})\)
\({subject}\mspace{14mu} {to}\)
\(\begin{matrix}
{{{{n_{Bq}b} + {n_{Dq}d} - {n_{Aq}a} - {n_{Cq}c}} = 0},{\forall{q \in Q}}} & (1) \\
{{{{e_{B}b} + {e_{D}d} - {e_{A}a} - {e_{C}c}} = 0},} & (2) \\
{{{{\Delta \; G_{B}^{f}b} + {\Delta \; G_{D}^{f}d} - {\Delta \; G_{A}^{f}a} - {\Delta \; G_{C}^{f}c}} \leq {{- \Delta}\; G^{\min}}},} & (3) \\
{{{h\left( {a,b,c,d} \right)} = 1},a,b,c,{d \in {^{+}\text{/}Z}}} & (4)
\end{matrix}\)

In formulation (optStoic), f (a,b,c,d) is a function of the overall stoichiometric coefficients quantifying a performance objective, Constraint (1) and (2) impose elemental and charge balances on the overall conversion respectively, while Constraint (3) imposes overall thermodynamic feasibility (ΔGoverall<0). ΔGmin quantifies the amount of “extra” ΔG available for the designed stoichiometry. The stoichiometry of the basis metabolite (usually the limiting carbon source) is set to a value of one. Constraint 4 generalizes the description of this scaling decision. Stoichiometric coefficients a,b,c,d can be declared as integer or real depending on the adopted scaling of the overall conversion. It is straightforward, to extend the optStoic formulation to account for more than two reactants and two products. In fact, a comprehensive list of putative co-reactants and co-products could be designed in the overall stoichiometry and then rely on the optStoic optimization problem to identify the optimal combination of co-reactants and co-products. A negative value for a stoichiometric coefficient declares a metabolite as a reactant while a positive value defines it as a product. Reactants or products with an inferred zero stoichiometric coefficient in essence “drop out” from the imposed overall stoichiometry.

The impact of cellular growth requirements on the flux allocation towards the target metabolite can be directly assessed by updating the overall stoichiometry to include biomass, growth (and non-growth) associated maintenance ATP as additional product metabolites:

\(\left. {{aA} + {cC}}\rightarrow{{bB} + {dD} + {\delta {\sum\limits_{k{{{ekem}{K}}}}{{coeff}_{k}M_{k}}}}} \right.\)

Here positive variable δ is the cellular growth coefficient, and biomass is represented as a weighted (by coeffk) sum of all the biomass precursors Mk (i.e., amino acids, lipids, cofactors as well as ATP requirements for cellular growth). Constraints for elemental and charge balances, and thermodynamic feasibility limitations are updated accordingly in optStoic:

\({{{n_{Bq}b} + {n_{Dq}d} + {\delta {\sum\limits_{k \in K}{n_{kq}{coeff}_{k}}}} - {n_{Aq}a} - {n_{Cq}c}} = 0},{q \in Q}\)
\({{{e_{B}b} + {e_{D}d} + {\delta {\sum\limits_{k \in K}{e_{k}{coeff}_{k}}}} - {e_{A}a} - {e_{C}c}} = 0},{{{\Delta \; G_{B}^{f}b} + {\Delta \; G_{D}^{f}d} + {\delta {\sum\limits_{k \in K}{\Delta \; G_{k}^{f}{coeff}_{k}}}} - {\Delta \; G_{A}^{f}a} - {\Delta \; G_{C}^{f}c}} = 0}\)

The trade-off between product yield and biomass formation can be assessed by fixing δ at different levels between zero and maximum growth and subsequently maximizing the target product coefficient.

Profit margin considerations (e.g., by using bulk market price of chemicals [38]) can be directly imposed in the optStoic formulation by specifying that the product prices exceed the reactant costs by a pre-specified margin profitmin.

prBb+prDd−prAa−prCc≧profitmin

where pri are the per mole prices of reactants and products i. Alternatively this margin could become the objective function that is maximized if an economic criterion is used to select reactant/product pairs. Trade-offs between the overall conversion stoichiometry and the negativity of the overall free energy of change can be drawn by varying the value of ΔGmin. For large values of ΔGmin overall conversions are obtained with a high thermodynamic driving force. As ΔGoverall is throttled back closer to zero more yield efficient conversions are obtained at the expense of a lower thermodynamic driving force that may limit flux per enzyme loading. Given that biomass formation is an endergonic process (ΔG>0) it is important to keep ΔGmin above the value needed for the desired growth. For example, for the iAF1260 metabolic model we find that the production of all constituents of biomass require a ΔG of 492.77 kcal g−1 biomass. Additional reserves for ΔG are needed to account for polymerization free energy costs of the biomass precursors not captured in the biomass equation. Alternatively, the overall stoichiometry could be expanded to directly include biomass, growth and non-growth associated maintenance ATP as product metabolites as described above.

Step 2: Identifying Reactions that Conform to the Identified Overall Stoichiometry

The second step identifies the smallest network of reactions that apportions the elemental composition of the substrates to the desired products in their corresponding stoichiometric ratios as determined in Step 1 (see FIG. 1). To this end we extracted a set of mass and charge balanced reactions J (i e, 6,302 reactions) from the MetRxn database [35] involving metabolites from set I (see Supplementary material 51 for datasets). In addition, exchange reactions for only the metabolites present in the overall stoichiometry are added to allow for their uptake and export, respectively. Therefore, all flux from the reactant metabolites is routed directly or recycled through intermediates towards the target metabolites. The optimization formulation for identifying the minimal number of reaction to match the identified stoichiometry requires the definition of the following parameters:

Sij: Stoichiometry matrix that describes the coefficient of metabolite i in reaction j (see Supplementary File S3 for dataset)

ΔGjLB, ΔGjUB: Lower and upper bound estimates for the ΔG of each reaction (see Supplementary File S4 for dataset)

LBj, UBj: Lower and upper bounds on the flux of each reaction j

The change in free energy ΔG of a reaction is a function of the non-standard activities of the participating metabolites as follows:

ΔGj=ΔGj0+RT ln Qj, ∀jεJ

where R is the gas constant and T is the temperature. ΔGj0 is the free-energy change of the reaction under standard conditions. Note that Q is the reaction quotient expressed as the ratio of the product of the activities (approximated by their molar concentration in an aqueous solution) of the products raised to their stoichiometric coefficient to that of the reactants. The reaction quotient Q for the overall conversion a A+c C→b B+dD is:

\(Q = \frac{{\lbrack B\rbrack^{b}\lbrack D\rbrack}^{d}}{{\lbrack A\rbrack^{a}\lbrack C\rbrack}^{c}}\)

where the expressions within brackets are the molar concentrations of each participating metabolite. The minimum (ΔGjLB) and maximum (ΔGjUB) bounds on the ΔG for each reaction in J are obtained by varying the concentration of the metabolites participating in the reaction by 1,000 fold of their transformed standard concentration (see Supplementary File S5). The wide range was chosen as a conservative estimate to allow for extreme fluctuations in intracellular metabolite concentrations in microorganisms (e.g., Bennet and co-workers [39] reported intracellular metabolite ranges in exponentially growing E. coli to vary between 10−3-102 mM). Reaction bounds LBj and UBj are determined according to the following rule:

\({LB}_{j} = \left\{ {{\begin{matrix}
{{0,{{{if}\mspace{14mu} \Delta \; G_{j}^{UB}} < 0}}\mspace{31mu}} \\
{{- M},{{{if}\mspace{14mu} \Delta \; G_{j}^{UB}} > 0}}
\end{matrix}{UB}_{j}} = \left\{ \begin{matrix}
{M,{{{if}\mspace{14mu} \Delta \; G_{j}^{LB}} < 0}} \\
{{0,{{{if}\mspace{14mu} \Delta \; G_{j}^{LB}} > 0}}\mspace{11mu}}
\end{matrix} \right.} \right.\)

where M is a large positive value (i.e., M=1,000) in relation the exchange flux of the metabolites of the overall stoichiometry (from Step 1). Additional information on directionality of reactions obtained from literature can be used, whenever available, to further constraint LBj and UBj. The directionality for 4,447 reactions (out of 6,302 within set J) was assigned by this procedure while the remaining 1,855 that lacked the free energy of formation for one or more metabolite were treated as reversible. Out of the 4,447 analyzed reactions, 2,205 were found to be irreversible whereas 2,242 were reversible. The identification of the minimal set of reactions that can match the desired overall stoichiometry (found after Step 1) is formulated as the following MILP (minRxn) problem:

\(\begin{matrix}
{{\underset{(y_{j})}{Minimize}\mspace{14mu} {\sum\limits_{j \in J}{y_{j}\mspace{14mu} ({minRxn})}}}{{subject}\mspace{14mu} {to}}} & (5) \\
{{{\sum\limits_{j \in J}{S_{ij}v_{j}}} = 0},{\forall{i \in I}}} & (6) \\
\left. \begin{matrix}
{{v_{A}^{ex} = {- a}},{v_{C}^{ex} = {- c}}} \\
{{{v_{B}^{ex} = b},{v_{D}^{ex} = d}}\mspace{31mu}}
\end{matrix} \right\rbrack & (7) \\
{{{{{LB}_{j}y_{j}} \leq v_{j} \leq {{UB}_{j}y_{j}}},{\forall{j \in J}}}{{v_{j} \in};{y_{j} \in \left\{ {0,1} \right\}}}} & (8)
\end{matrix}\)

Binary variables yj defined as

\(y_{j} = \left\{ \begin{matrix}
{1,{{{if}\mspace{14mu} {LB}_{j}} \leq v_{j} \leq {UB}_{j}}} \\
{{0,{{{if}\mspace{14mu} v_{j}} = 0}}\mspace{104mu}}
\end{matrix} \right.\)

control the addition (or not) of reaction j in the overall network. The objective function involves the minimization of the sum of yj's (Constraint 5) to extract the minimum number of reactions that can support the desired overall stoichiometry (optStoic) of Step 1. Constraint (6) ensures that all metabolites, including cofactors, are used in a stoichiometrically balanced manner. Constraint (7) sets the flux of the exchange reactions (i.e., for A, B, C and D) equal to their respective stoichiometric coefficients thus matching the overall desired stoichiometry (from Step 1) and providing a flux scaling. Constraint (8) ensures that reaction j is removed from the designed network when yj is equal to zero. Networks for different overall stoichiometries (from Step 1) can be obtained and contrasted for their overall performance metrics. The use of integer cut constraints to (i) disallow previously identified solutions and (ii) search for alternate optimal as well as sub-optimal solutions can be used to exhaustively explore all possible ways of linking reactants to products (Constraint 9).

\(\begin{matrix}
{{{{\sum\limits_{{j|y_{j}^{k}} = 0}y_{j}} + {\sum\limits_{{j|y_{j}^{k}} = 1}{\left( {1 - y_{j}} \right)1}}} \geq},{{\forall k} = 1},\ldots,K} & (9)
\end{matrix}\)

where k=1, . . . , K is the set of previously of explored solutions.

The resulting (minRxn) MILP formulation can be computationally challenging to solve as it involves as many as 6,302 binary variables associated with all the reactions in set J. A related LP formulation (minFlux) that is significantly (i.e., up to three orders of magnitude) less computationally taxing can be solved as a surrogate of minRxn. In contrast to minRxn that directly minimizes the total number of reactions in the designed network, minFlux minimizes the total metabolic flux of the chosen reactions. This modified objective function could be viewed as an approximation of the total enzyme-load imposed on the organism [40]:

\(\begin{matrix}
{{\underset{(x_{j})}{Minimize}{\sum\limits_{j \in J}{x_{j}\mspace{14mu} ({minFlux})}}}{{subject}\mspace{14mu} {to}}} & (10) \\
{{{\sum\limits_{j \in J}{S_{ij}v_{j}}} = 0},{\forall{i \in I}}} & (6) \\
\left. \begin{matrix}
{{v_{A}^{ex} = {- a}},{v_{C}^{ex} = {- c}}} \\
{{{v_{B}^{ex} = b},{v_{D}^{ex} = d}}\mspace{31mu}}
\end{matrix} \right\rbrack & (7) \\
{{{LB}_{j} \leq v_{j} \leq {UB}_{j}},{\forall{j \in J}}} & (11) \\
{{x_{j} \geq v_{j}},{\forall{j \in J}}} & (12) \\
{{{x_{j} \geq {- v_{j}}},{\forall{j \in J}}}{v_{j},{x_{j} \in}}} & (13)
\end{matrix}\)

In minFlux, the sum of the absolute values of the reaction fluxes denoted by xj is minimized (Constraint 10). Constraints (6) and (7) are the same as in (minRxn) formulation whereas Constraint (11) imposes bounds on fluxes without multiplication with a binary variable. Constraints (12) and (13) ensure that xj is greater than both vj and −vj. The minimization operator in the objective function ensures that for every j either Constraint (12) or (13) becomes active.

Alternate optimal (as well as suboptimal) basic flux combinations can also be explored by preventing all nonzero basic variables from an earlier solution k from reappearing in subsequent flux combinations (see Lee and co-workers [41] for details). In short, we first reorganize minFlux in standard form [42] and transform all the variables (i.e., xj and vj) to positive variable sl (where L is the set of variables for problem in standard form). Subsequently, a set of integer cut constraints similar to the ones described for formulation (minRxn) can be constructed. Binary variables ul denote the presence of nonzero basic variable l in a previously identified solution k. The following constraints prevents the reappearance of a previously found basic feasible solution:

\(\begin{matrix}
{{{ɛ\; u_{l}} \leq s_{l} \leq {Mu}_{l}},{\forall{l \in L}}} & (14) \\
{{{\sum\limits_{{l|u_{l}^{k}} = 1}\left( {1 - u_{l}} \right)} \geq 1},{{\forall k} = 1},\ldots,K} & (15)
\end{matrix}\)

where ε is a small positive value (ε=10−5) that ensures that sl is nonzero when up=1. It is important to stress that the addition of integer cuts converts the LP (minFlux) formulation to an MILP problem. Nevertheless, it is can be solved significantly faster (about two orders of magnitude) than minRxn as it involves much fewer binary variables.

Additional constraints can be added in either minRxn or minFlux optimization formulations to maintain the total number of reactions with a positive standard free energy of change at a minimum (e.g., less than pt):

\(\begin{matrix}
{{v_{j} \geq {{LB}_{j}u_{j}}},\left. {\forall j} \middle| {{\Delta \; G_{j}^{0}} \leq 0} \right.} & (16) \\
{{v_{j} \leq {{UB}_{j}u_{j}}},\left. {\forall j} \middle| {{\Delta \; G_{j}^{0}} \geq 0} \right.} & (17) \\
{{\sum\limits_{j}u_{j}} \leq p^{\prime}} & (18)
\end{matrix}\)

where uj is a binary variable which is defined as:

\(u_{j} = \left\{ \begin{matrix}
{1,{{{if}\mspace{14mu} {{sign}\left( v_{j} \right)}} = {{sign}\left( {\Delta \; G_{j}^{0}} \right)}}} \\
{{0,{otherwise}}\mspace{149mu}}
\end{matrix} \right.\)

Reactions with a positive standard free energy of change may require the accumulation of a significant reactant metabolite pool to drive the reaction forward. This is generally undesirable as it may throttle back the flux in the overall pathway by triggering cellular toxicity and/or pathway substrate inhibition.

In addition, formulations minRxn or minFlux can be augmented to control the number of organisms from which reactions are sourced in the construction of the conversion network to less than po.

\(\begin{matrix}
{{x_{j} \leq {M{\sum\limits_{o}{r_{o}{org}_{oj}}}}},{\forall{o \in O}}} & (19) \\
{{\sum\limits_{o}r_{o}} \leq p^{o}} & (20) \\
{r_{o} \in \left\{ {0,1} \right\}} & (21)
\end{matrix}\)

Here, parameter orgoj has a value of one if reaction j is present in organism o, and zero otherwise. Using binary variable ro, Constraint (19) ensures that a reaction j cannot carry any flux unless it is present in at least one organism o

\(\left( {{i.e.},{{\sum\limits_{o}r_{o}} \geq 1}} \right).\)

Constraint (20) sets an upper bound po on the number of organisms contributing reactions. One can avoid selecting the host organism a priori, thus allowing the optimization formulation to select the production host(s) best suited to construct the synthetic network. In addition, the definition of set O can be altered accordingly to minimize diversity in chosen genus instead of individual organisms. Alternatively, the production host could be pre-specified and then restrict the total number of heterologous reactions.

**1.2 Results**

The two-step stoichiometry and intervening reaction design procedure was implemented for three case studies that highlight the potential of the present invention in identifying novel stoichiometries and network designs. The first study explores pathways that successfully disassemble glucose to acetate with maximum carbon yield. The second study explores the reverse problem of identifying new ways of forming carbon-carbon bonds from methanol and CO2 to feasible C2+ products. Finally, the third study identifies overall stoichiometries for converting methane to acetate by identifying suitable co-reactant and co-product pairs to drive forward the thermodynamically unfavorable methane to acetate conversion.

**1.2.1 Case Study 1: Synthetic Pathways for Fully Converting Glucose to Acetate**

Conversion of glucose through central carbon metabolism to acetyl-CoA (through EMP glycolysis or Entner-Doudoroff pathway) is required by most microorganisms for the production of biomass precursors and cofactors [43]. These pathways are also often recruited for the production of various bioproducts in a variety of production hosts. The generation of ATP and redox equivalent for growth, however, comes at the expense of losing two carbon atoms per glucose molecule as carbon dioxide reducing carbon yield to a maximum of 67%. Alternate modes of glucose metabolism, such as the glycerate pathway [44] lead to the same carbon loss. An exception to this rule is found in some clostridial [45] and lactate-producing bacteria [46] that use a phosphoketolase enzyme to process glucose without any carbon loss as CO2. Recently, a synthetic, non-oxidative glycolysis (NOG) was designed and assembled demonstrating the feasibility of this concept [30] for bio-conversions. By expressing in E. coli heterologous phosphoketolase enzymes xylulose-5-phosphate phosphoketolase (XPK, E.C.#4.1.2.9) and fructose-6-phosphate phosphoketolase (FPK, E.C.#4.1.2.22) from B. adolescentis Bogorad and co-workers [30] assembled three cyclic networks demonstrating complete conversion of glucose to acetate. In this case study, we benchmark the present invention for the same conversion and explore additional network designs beyond the ones described in Bogorad and co-workers [30].

The first step, (i.e., OptStoic) here is redundant as the overall stoichiometry in the form of A→3B is fixed. Only networks that conserve all carbon flux from glucose to acetate satisfy the imposed overall stoichiometry. Results from both minRxn and minFlux converged to the same designs that achieve the overall conversion albeit with substantial differences in computational time. The smallest network (FIG. 2A) recapitulated the engineered construction of Bogorad and co-workers [30] where glucose undergoes a stepwise conversion to acetyl phosphate (actp) in a cyclic route. First, FPK cleaves fructose-6-phosphate (f6p) to erythrose-4-phosphate (e4p) and acetyl phosphate (actp). Next, e4p follows the reversal of Pentose Phosphate Pathway to produce two molecules of xylulose-5-phosphate (xu5p). Deacetylation of xu5p to glyceraldehyde-3-phosphate (g3p) by XFP produces two additional molecules of actp. Conversion of g3p to f6p through the reversal of upper glycolysis completes the cycle. Acetate kinase (ACK, E.C.#2.3.1.8) hydrolyses the three actp molecules to terminal acetate. A number alternate routes using FPK or XPK as the sole deacetylating reaction were identified similar to those constructed in Bogorad and co-workers [30] (see FIG. 2B for one of the constructions). Note that in this network design the need for cofactors nadh and nad is balanced with a zero net requirement. minRxn/minFlux can also be used to directly limit the number of reactions with a positive standard free energy of change. While both NOG and all designs shown in FIGS. 2A, B, D, E and F require at least two reactions with a positive standard free energy change, the design depicted in FIG. 2C involves a single reaction with positive ΔG0 whereby the thermodynamically unfavorable conversion of r5p to ru5p is avoided by routing the Pentose Phosphate Flux through C5 metabolism of phosphoribosyl pyrophosphate (prpp) and ribulose (rub) in E. coli. However, as a tradeoff this cycle consumes one additional ATP compared to other designs. Networks not involving any CO2 production through the phosphoketolase can also be designed (see FIG. 2D) where glucose uses the modified RuMP pathway to produce three molecules of ethylene glycol. Diol dehydratase (DDT, E.C.#4.2.1.28 [47]) removes a water molecule from ethylene glycol to synthesize acetaldehyde (acald), which can be oxidized to acetate in three steps. This route can be potentially advantageous for the co-utilization of five and six carbon substrates [48].

We next explored whether it is possible to construct the entire pathway in a single organism unlike the engineered NOG pathway that requires at least one heterologous enzyme (i.e., either FPK or XPK). FIG. 2E illustrates one such design with reactions from only clostridial species such as C. ljungdahlii [49] or thermophilic organisms such as Moorella thermoacetica [50]. Here, the EMP pathway is combined with the Wood-Ljungdahl cycle to fix the CO2 lost in the conversion of pyruvate (pyr) to acetyl-CoA. Two pyr molecules (from one glucose molecule) are decarboxylated by the pyr ferredoxin oxidoreductase enzyme (PFOR, E.C.#1.2.7.1) [51] to acetyl-CoA and CO2. Subsequently, one CO2 molecule enters the western branch of Wood-Ljungdahl cycle where it is reduced and fixed with thf to methf. Next, methf enters the eastern branch of Wood-Ljungdahl pathway to condense with the second CO2 molecule to synthesize the third molecule of acetyl-CoA. Conversion of acetyl-CoA to acetate completes the pathway. Note that all network designs introduced here (see FIG. 2) have a net zero ATP balance as specified in the overall stoichiometry. In contrast, the NOG pathway can produce two ATP molecules (per glucose molecule) from actp hydrolysis. By combining glycolysis and Wood-Ljungdahl we can in principle provide five ATP molecules (see FIG. 2E). However, thermodynamic constraints on the overall conversion (i.e., (i.e., ΔGoverall≦−5 kcal) do not allow more than three ATP to be generated. While the ATP generation efficiency of this pathway can be controlled by tuning the ATP and non-ATP producing isozymes of ACK, an alternate pathway (see FIG. 2F) with optimum generation of three ATP can be constructed using enzymes in the ED pathway. Here, the serine metabolism is utilized instead of the western branch to generate methf. However, practical hurdles in fixing all the CO2 released in pyruvate decarboxylation (PFOR) and glycine cleavage (GLYCL, E.C.#1.4.4.2) may make these pathways difficult to engineer.

In this example, we saw how optimization formulations minRxn/minFlux can be used to select reactions that fully convert glucose to acetate while exploring the impact of minimizing reactions with a positive ΔG0, selection of production host and minimality of reactions in the designed conversion pathway.

**1.2.2 Case-Study 2: Co-Utilization of Methanol and Carbon Dioxide to C2+ Compounds**

In the second case study, we focus on the design of the overall conversion when not all participating metabolites are known a priori. A recent study proposed and constructed a biological route for the direct condensation of methanol to ethanol [32] with 100% efficiency of carbon conversion. This motivated us to explore novel designs that can simultaneously convert methanol and co-utilize CO2 towards C2+ product metabolites with zero loss of carbon flux (i.e., A+C→B reaction). Here, unlike the previous case study, product metabolite B is unknown and could potentially be any of the 3330 C2+ metabolites in set I. The negative free energy of change for methanol condensation (ΔG=−16.25 kcal mol−1) allows for the endergonic uptake of some CO2 to become thermodynamically feasible. As a result, designed pathways have the potential to achieve higher carbon efficiency than existing methanol condensation routes [32] while also exhaustively exploring all possible C2+ product metabolites.

We chose maximization of the coefficient of CO2 in the overall stoichiometry as the design objective in optStoic while keeping the methanol coefficient at a value of one. This objective function maximizes the carbon yield of the desired product per mole of the limiting reactant (methanol). As many as 148 target metabolites from set I were identified as thermodynamically feasible products for the conversion (see Supplementary File S5 for full list). Table 1 shows ten of the designs in decreasing order of CO2 uptake. CO2 uptake varies in concert with the oxygen to hydrogen ratio (O:H) in the product metabolite. For example, malonate (C3H4O4), which has a O:H ratio of one has the largest stoichiometric coefficient for CO2 (i.e., 1.25), while 2-methyl butanal (O:H=0.1) has the lowest (0.0714). As hydrogen availability in the reactants is fixed (stoichiometry of methanol is fixed to one), a low O:H ratio in the product reduces water production to satisfy elemental hydrogen balance. Because the oxygen atoms in CO2 are routed to water for products with low O:H ratio, reduced water production limits caused by the fixed availability of H, reduces the co-utilization of CO2 and thus overall carbon yield. It is important to note that the O:H ratio is also critical in deciding whether a desired metabolite is a feasible target product. For example, several platform chemicals such as ethylene glycol (O:H=0.33), 1-butanol (O:H=0.125) and 1,3-propanediol (O:H=0.25) are not feasible solutions as mass conservation of hydrogen and oxygen cannot be simultaneously satisfied in the overall stoichiometry. Furthermore, metabolites with a very high O:H ratio, such as oxalate (O:H=2) and glyoxylate (O:H=1.5) are also not feasible due to limitations in oxygen atoms availability from CO2. Therefore, constraints of the overall design stoichiometry determine the feasibility of the target products as well as their maximum yields. It appears that in all designs thermodynamic feasibility is not the limiting constraint, instead elemental balances for H and O limit overall reaction stoichiometries.

From Table 1, we selected four products (i.e., acetate, 3-hydroxybuyrate, 2-ketoisovalerate and phloroglucinol) for constructing networks satisfying their overall reaction stoichiometry (see FIG. 3). Both 3-hydroxybuyrate and 2-ketoisovalerate are platform chemicals [52] that also serve as precursors to other biochemicals [28,52] while phloroglucinol is a phenolic derivative used as a building block for cosmetics [53] and explosives [54]. Note that for the construction of the networks we scaled up the overall stoichiometry such that all the coefficients are integers. Optimization formulations minRxn/minFlux revealed that the optimal reaction networks for each conversion involved a common core of reactions that initially convert the C1 substrates to an intermediate product (i.e., acetyl-CoA), which was subsequently routed towards the final product. As a result, the first example (acetate production) spans alternate routes of fixing CO2 with methanol to acetyl-CoA (and acetate). Each one of the identified networks is subsequently coupled with additional reactions to synthesize the three other target products (i.e., 3-hydroxybuyrate, 2-ketoisovalerate and phloroglucinol). The optimal network for converting methanol and CO2 to acetate is divided into two modules (see FIG. 3A). The first module condenses four molecules of CO2 and methanol to synthesize four acetyl-CoA molecules using a combination of methylotropic and Wood-Ljungdahl pathway enzymes. The methyl group of methanol is transferred to Corrinoid protein by CoM-Corrinoid methyltransferases (MTA, E.C.#2.1.1.90 and 2.1.1.246) [55,56], which subsequently condenses with CO2 to acetyl-CoA by acetyl-CoA synthase (ACS, E.C.#1.2.7.4 and 2.3.1.169) enzyme from the Wood-Ljungdahl pathway [57]. The reducing equivalents (ferredoxin) required for powering this conversion is supplied by methanol oxidation in methanol dehydrogenase (MEDH, E.C.#1.1.1.244) in the second module. This module assembles an alternative methanol condensation [32] cycle where four formaldehyde molecules enter a modified ribulose monophosphate (RuMP) Pathway [58] to condense to two actp molecules. Hexulose-6-phosphate synthase (HPS, E.C.#4.1.2.43) and 6-phospho-3-hexulo isomerase (PHI, E.C.#5.3.1.27) found in methylotrophs [58] fix formed into the five-carbon ru5p backbone which is subsequently cleaved in FPK. Pentose Phosphate enzymes convert the intermediate substrates back to ru5p to complete the cycle using reactions also present in the NOG cycle.

The design shown in FIG. 3A requires the fewest number of reactions, however, the oxygen-sensitive nature of the Wood-Ljungdahl enzymes (MTA, ACS) [32] would be a practical concern. The second synthetic design (see FIG. 3B) uses histidine degradation metabolism [59] and formate dehydrogenase (FORMD) from Clostridia [60] to fix CO2 for acetate production. Here, the RuMP cycle is altered to convert formaldehyde to glycerone instead of actp. Formaldehyde transketolase (FTKT, E.C.#2.2.1.3) from methylotropic yeasts such as P. pastoris [61]) is the only additional reaction required to fix an additional formaldehyde molecule with xu5p, and subsequently cleave it to glycerone. Subsequently, glycerone follows lactate metabolism to acetaldehyde (acald) (in Lactate Aldolase (LA, E.C.#4.1.2.36)), and oxidation of acetaldehyde completes the network.

A third design using predominantly E. coli reactions was also identified. Here, while half of the formaldehyde molecules (from methanol) are fixed in the modified RuMP cycle, the rest is fixed along with CO2 in a functional reversal of the glyoxylate shunt [62]. Here, glyoxylate is converted to glycine uses the folate-driven C1 metabolism in serine pathway to fix the remaining formaldehyde molecules. C1 metabolism in the serine pathway is combined with serine-glyoxylate aminotransferase (SERAT, E.C.#2.6.1.45) to fix the remaining formaldehyde to glyoxylate and produce hydroxypyruvate (hpyr). Phosphenolpyruvate (pep), from the reduction of hpyr in glycerate metabolism, fixes atmospheric CO2 in the anaplerotic pep carboxylase enzyme (PPC, E.C.#4.1.1.49). This flux is routed through malyl-CoA (in ATP-driven malate thiokinase (MTK, E.C.#6.2.1.9) [62]) to be cleaved to produce acetyl-CoA and glyoxylate by malyl-CoA ligase (MCL, E.C.#4.1.3.24). As all the reactions in this network are either native to E. coli or have been successfully expressed in prior studies (PC, MTK, MCL) [62,63], it has the fewest potential barriers for its implementation.

Each one of these cyclic routes can be combined with additional paths to route acetyl-CoA flux towards other target chemicals. FIGS. 4A, B and C show routes for converting methanol and CO2 to a C4, a C5 and a C6 product, respectively. Pathways for 3-hydroxybutyrate (3hbut) recapitulate existing engineered routes through acetoacetyl-CoA [64,65] while also proposing additional synthetic designs that use succinate metabolism and reversal of the β-oxidation pathway (see FIG. 4A). In addition to thiamine-dependent valine synthesis for 2-ketoisovalerate (2kiv) production [66], a novel route path linking β-oxidation reversal with valine degradation is also identified (see FIG. 4B). Here, n-butanoyl-CoA in the C4 β-oxidation cycle is isomerized to isobutyryl-CoA (ibutcoa) in iso-butyryl-CoA mutase (ICM, E.C.#5.4.99.13) [67]. Reversal of 2-ketoisovalerate oxidoreductase (KIVR, E.C.#1.2.1.25) in the valine degradation pathway converts 2-mpropcoa to the target product. In the case of phloroglucinol production, however, the traditional pathway using malonyl-CoA metabolism [68] was not identified by minFlux as it violates the energy requirement for the acetyl-CoA carboxylase (ACCOAC, E.C.#6.4.1.2) step. Instead, acetyl-CoA was converted to hydroxyl-butyryl-CoA (hbutcoa) which incorporates an additional acetyl-CoA molecule to form 3-hydroxy-5-oxohexanoyl-CoA (in 3-hydroxy-5-oxohexanoyl-CoA thiolase (HXCOAT, E.C.#2.8.3.8)). Cyclization and reduction of this molecule synthesizes phloroglucinol.

This example highlights several of the advantages of the present invention over existing pathway prospecting tools. First, we can set well-defined cutoffs for the performance of the pathway that do not require any post-processing steps unlike existing procedures [17,28,69]. Strict constraints of thermodynamics and overall stoichiometry filter out suboptimal routes and unbalanced conversions. The designs are not restricted to be linear paths [23,27,28] from a substrate to the product, but can explore cyclic routes connected not only by carbon transfer, but also through cofactor balances. More importantly, instead of exploring only A→B type of conversion [17,70], the networks can satisfy complex stoichiometries where the participating metabolites and their coefficients can be design variables. In addition, as seen in the first case study, the performance criteria for each of the two steps (i.e., the overall design and pathway construction) can be altered to match the specific requirements of the design.

**1.2.3 Case Study 3: Designing Thermodynamically Feasible Paths for the Conversion of Methane to Acetate**

In the previous case study, only co-product (B) was unknown in the overall conversion. In the third case study, both co-reactant (C) and co-product (D) are design variables. With increased production of methane from natural gas deposits through advanced extraction technologies [71], there is a growing interest of engineering metabolic routes of fixing this gaseous feedstock to C2+ liquid biofuel and biochemical targets [72]. However, the overall conversion creating a C—C bond by fixing methane with a C1 co-substrate (e.g., atmospheric CO2, CO from syn gas, etc.) is thermodynamically unfavorable (e.g., ΔG=11.05 kcal for CH4+CO2→CH3COOH reaction). Recent studies have suggested that such a conversion can be achieved when coupled with a suitable electron acceptor [73,74]. Several anaerobic microorganisms have evolved ways to couple oxidation of methane with reduction of electron acceptors such as nitrite, sulfate 79, iron and manganese 80. In this study, we first identify all electron acceptors that could be used to convert methane to acetate (C2 product) and rank them according to their carbon yield to acetate. Subsequently, we select five solutions from the list of feasible electron acceptors to design pathways that convert methane and a C1 co-substrate (CO2 or CO) to acetate along with a C2+ platform chemical [1,75].

Using optStoic and keeping the stoichiometry of acetate fixed at one (as basis), we maximized the stoichiometric coefficient of methane while allowing the production of up to two additional metabolites from set I. Non-carbon containing metabolites including metal ions, anions, protons and water were included as candidates in the overall stoichiometry. optStoic identified many distinct designs with alternative electron-acceptor combinations. Ten designs are shown in Table 2 (see Supplementary File S6 for all the designs). Here, the overall reaction stoichiometry has been rescaled for unit molar consumption of the electron acceptor. The only feasible stoichiometry with a single additional co-metabolite was oxygen. We did not analyze further this stoichiometry as designs for aerobic conversion of methane have already been explored extensively [72,76]. Results demonstrate the varying capacity of different electron-accepting pairs in oxidizing methane to acetate due to thermodynamic considerations. The reduction of one mole of tetrathionate (S4O62−) to hydrogen sulfide (H2S) accepts the maximum number of electrons (eighteen) thus converting 4.5 moles of methane to 2.25 moles of acetate. In contrast, one mole of iron(III)/iron(II) reduction (Fe3+/Fe2+) oxidizes only 0.25 moles of methane as it accepts only one electron. The electron acceptor pair S4O62−/H2S also supplies the oxygen required for the carbonyl group in acetate and oxidize additional hydrogen in methane to water. Most of the electron accepting pairs such as nitrate/nitrite (NO3−/NO2−) and sulfite/hydrogen sulfide (HSO3−/H2S) perform both tasks. Only pair Fe3+/Fe2+ performs the role of electron acceptor while water supplies the oxygen. Note that the commonly found electron pair sulfate/hydrogen sulfide reduction (SO42−/H2S) utilized by several marine anaerobic consortia for methane oxidation [77,78] was not identified as a feasible solution as ΔGoverall of the reaction (−4.41 kcal mol−1 acetate) was below the allowable ΔGmin (−5 kcal mole−1 acetate) set for this case study.

For the second step of optStoic we selected five pairs of electron acceptors from Table 2 (i.e., NO3−/NO2−, HSO3−/H2S, NO2−/NH4+, Fe3+/Fe2+ and HSO3−/S2O32−) with different efficiencies of methane fixation per mole of oxidizing metabolite. For a unit mole conversion of each pair, we searched for a stoichiometry that further improves methane uptake by allowing for up to two additional metabolites from set I (similar to Step 1). The co-substrates were restricted to CO2 and CO while the co-products were chosen from all C2+ compounds (3330 in set I). Table 3 compares ten of the designs for HSO3−/H2s and NO3−/NO2− electron acceptors. Both acceptors exhibit the same general trend with products with higher carbon ratio have higher stoichiometry of methane uptake (per unit mole of acetate production). In contrast to Case Study 2, it was the thermodynamic feasibility of the overall reaction and not the O:H ratio of the product that was limiting methane utilization. By allowing both the reactant and co-reactant stoichiometries to vary we have an additional degree to freedom to match the O:H ratio of the target product and maximize methane utilization all the way to the thermodynamic limit (i.e., ΔGoverall=−5 kcal). It is also interesting to note that NO3−/NO2− allows for much higher efficiency of methane fixation compared to HSO3−/H2S. This is also because the thermodynamic driving force and not the electron-accepting capability of the electron acceptor becomes the limiting factor in this case.

Each of the five electron acceptors was used to suggest minimal networks for fixing methane to a different target product (see FIGS. 5 and 6). Similar to previous study, results showed that a core set of reactions first converted methane and the co-reactant to intermediate acetyl-CoA. We used the first design (i.e., Fe3+/Fe2+ for acetate production) to

describe existing and novel routes of fixing methane and CO2 (or CO) to acetate (see FIG. 5). Additional designs concentrate on the paths from acetate to the final products (see FIG. 6). All designs reveal that the terminal acceptors exchanged electrons with a cofactor pair instead of directly catalyzing a reaction in the carbon-transfer network. Different cofactors were identified for the electron acceptors depending on the reduction reactions in the network. For example, Fe3+/Fe2+ and No2−/NH4+ use nadh as the electron donor, catalyzed by NAD:Fe oxidoreductase (E.C.#1.16.1.7, from denitrifying bacteria such as P. denitrificans [79]) and ammonia oxidoreductase (E.C.#1.16.1.15, from E. coli [80]) respectively. In contrast, HsO3−/H2s exchanges electrons with napdh using sulfite reductase (e.g., in E. coli [81], E.C.#1.8.1.2), while reduced ferredoxin does the same for NO3−/NO2− using a nitrite oxidoreductase (e.g., from N. gracilis [82], E.C.#1.7.7.2). In some cases photosynthetic enzymes found in plant chlorophylls were initially suggested such as ferredoxin-dependent thiosulfate reductase (E.C.#2.8.1.3, from A. thaliana [83]) for HsO3−/S2O32− (see FIG. 6C). Upon excluding them an alternate mechanism was identified by minFlux where HSO3− is converted to S2O32− through the oxidation of mercaptopyrvate (to pyruvate) by sulfurtransferases (E.C.#2.8.1.2) found in E. coli [84] (see FIG. 6C). Note that a few of the designs require electron transfer between NAD(P)H and ferredoxin for regeneration of reduced ferredoxin (fdr) (e.g., see FIGS. 5B and C). While the free energy change under standard conditions suggests that this reaction is favorable only in reverse (i.e., ΔGnad/fd=3.83 kcal [85]), there exists multiple experimental evidence alluding to the feasibility of electron transfer from NAD(P)H to ferredoxin [86].

FIG. 5 shows three alternate routes for the conversion of three molecules of methane and one molecule of CO2 to two acetate molecules with Fe3+/Fe2+ as the terminal electron acceptor. The smallest network (FIG. 5A) describes a functional reversal of the methanogenesis pathway where a molecule of methane and CO2 combine to synthesize acetyl-CoA. Acetyl-CoA is subsequently hydrolyzed to acetate. The key enzymes in this pathway are CoM reductase (MCR, E.C.#2.8.4.1), Corrinoid methyltransferase (MTBA, E.C.#2.1.1.246), heterodisulfide reductase (HDR, E.C.#1.8.98.1) and the acetyl-CoA synthase (ACS), all found in most methanotropic archaea and some methylotrophs [74]. However, in order to maintain the 1:1 stoichiometric balance of methane and CO2 in ACS reaction, one molecule of methane is oxidized to CO2 in a complex three-step cyclic route involving a functional reversal of the eastern branch of the Wood-Ljungdahl pathway. First, thf is converted to 5-methyl thf (mthf) by transferring methyl group from methyl Corrinoid protein homologous to MTBA reaction [87]. This substrate is subsequently oxidized by nad or ferredoxin cofactors (according to stoichiometric demands of each cofactor) and hydrolyzed to formate. Formate dehydrogenase (FDH, E.C. #1.2.1.2) oxidizes formate to CO2. Likewise, alternate routes for oxidizing methane can also be engineered that directly oxidizes methyl-coM to CO2 in the methylamine cycle. Here, the methyl group is transferred to dimethylamine (dma) in trimethylamine methyltransferase (TMMT, E.C. #2.1.1.247) that is homologous to MTBA [88]. Trimethylamine (tma), thus formed, is cleaved by tma oxide aldolase to produce formaldehyde. Oxidation of formaldehyde to CO2 completes the network. The third bypasses the ATPS and MTBA reactions by combining the two previous cyclic networks. Here, CO2 is first reduced to CO which is subsequently fixed to acetyl-CoA through the western branch of the Wood-Ljungdahl pathway (FIG. 5C). It must be noted that all the enzymes (except for the terminal electron acceptors) are present in most anaerobic methanogens that makes these networks easier to construct. This case study highlights the fact that the cofactor balances play a significant role in network-design. For example, the net reduction of 5-methyl thf to 5,10-methylene thf is accomplished by two opposite reactions involving nad and ferredoxin cofactors (FIG. 5A) in order to maintain the overall balance of individual cofactors.

FIG. 6 describes a few of the existing strategies and novel routes of for maximizing the production of four platform chemicals (i.e., 2,3-butanediol, 3-hydroxypropionate, 1-butanol and 1,3-propanediol [52,75]), each utilizing a different electron acceptor. In addition to existing routes of synthesizing the target product, we also identified alternate pathways with equal or higher carbon yields. For example, 2,3-butanediol (23but) could be synthesized from acetyl-CoA by first converting it to pyruvate (using pyruvate-ferredoxin oxidoreductase (PFOR) [51]) with subsequent dimerization to acetolactate (see FIG. 6A). Decarboxylation of acetolactate followed by reduction of acetolactate produces 2,3-butanediol. While standard pathways (from pyruvate [89]) lose two carbon atoms for each molecule of 23but, this pathway preserves all the carbon molecules as the lost CO2 is compensated in the PFO step. It is interesting to note that this pathway uses the same enzymes (except the MTBA reaction) of converting CO to 23bdo in a recent study in three separate acetogenic Clostridial species [34] as well as functionally expressed in E. coli [90]. This shows how overall stoichiometry constraints leverage known routes to allow for the uptake of co-reactants (methane in this case) that improves the overall carbon efficiency of conversion. An alternate pathway was also identified where one acetyl-CoA molecule is oxidized to acetaldehyde, which combines with a second acetyl-CoA molecule to form acetoin through the reversal of acetoin dehydrogenase (ACTDH, E.C. #2.3.1.190) found in acetoin consuming bacteria such as E. aerogenes [91].

Three pathways were identified for 3-hydroxypropionate (3 hp) production all of which have been explored previously (see FIG. 6B). While the first two paths hydrolyze and reduce pyruvate through lactate [92] and β-alanine [33] as intermediates, the third pathway (and shortest) path utilizes malonyl-CoA reduction [93]. However, unlike the first pathway, the other two are less energy-efficient due to an additional ATP requirement for pyruvate carboxylase (PC) and acetyl-CoA carboxylase (ACCOAC, E.C.#6.4.1.2) reactions respectively. Similarly, the shortest route for 1-butanol production (FIG. 6C) recapitulates existing strategies involving condensation of two molecules of acetyl-CoA in accoa acetyltransferase (ACT, E.C.#2.3.1.9) followed by a functional reversal of the β-oxidation pathway [31,94,95]. A so far unexplored pathway is also suggested that combines the oxidative branch of TCA cycle with succinate-semialdehyde metabolism to reach 1-butanol. Here, pyruvate (from acetyl-CoA) is first carboxylated to oxaloacetate in the ATP-dependent pyruvate carboxylase reaction (PC). The TCA cycle converts oxaloacetate and acetyl-CoA to 2-oxoglurate, which is decarboxylated to succinate-semialdehyde in akg decarboxylase (AKGCL, E.C. #4.1.1.71 found in Synechocystis [96]). Reduction of succinate semialdehyde, similar to β-oxidation reversal synthesizes 1-butanol. In the case of 1,3-propanediol (see FIG. 6D), the only identified pathway converts acetyl-CoA to pyruvate which is reduced back to g3p through gluconeogenesis. Glycerol, from g3p, is subsequently reduced to 13pdo in three steps by the native (e.g., in some Clostridia [97]) or engineered enzymes found in E. coli and K pneumonie (i.e., the DuPont pathway [98]). The present invention could not identify an alternate pathway in E. coli [99] where homoserine (hser) flux is routed towards 3-hydroxypropanal (2hpa) by engineering the native glutamate dehydrogenase to be promiscuous towards homoserine. The reason is because the intermediate metabolite 4-hydroxy-2-oxobutyrate (4hkbut) in the pathway as well as the reactions associated with the molecule (see FIG. 6D in red) was absent in our database. Upon inclusion of the metabolite and the reactions, minFlux could identify this pathway as an alternate more energy efficient route for 13pdo production.

In this study we identified and rank-ordered feasible electron acceptor pairs according to their methane oxidation potential. Unlike the previous example, thermodynamic feasibility and not elemental balances becomes the limiting factor in determining the optimum stoichiometric ratios in the overall reaction. minFlux identified relevant cofactor systems that coupled the methane utilization pathway with the terminal electron acceptors.

**1.3 Discussion**

The present invention develops a two-step computational procedure (optStoic+minRxn/minFlux) for designing de novo networks that match an overall stoichiometry of chemical transformation. Performance criteria on the designed pathways (e.g., carbon yield/energy efficiency, pathway ΔG etc.) can systematically be imposed and rank-order synthetic pathways according to the design objective. The three examples highlight the potential of this procedure for designing a thermodynamically feasible overall conversion stoichiometry, selecting the optimum combination of co-metabolites and co-products, and constructing non-intuitive synthetic biological routes for the overall conversion.

For the most part existing databases such as MetRxn [35] or Kegg [100] span a very large population of intermediate metabolites that can be produced from the reacting metabolites. In contrast, the number of terminal pathways towards target products tends to be much more limited. For example, acetyl-CoA is associated with 153 reactions, while 13pdo and phloroglucinol are involved in one and two reactions, respectively. Therefore, most of the novel network designs suggested by minRxn/minFlux stemmed from alternate intermediate metabolites and ways of producing them. A potential way of expanding the diversity of network design would be to consider hypothetical biotransformations generated by successively applying reaction operators on metabolites [29,70]. For example, in a recent work for synthesizing platform chemicals in E. coli, GEM-Path [28] suggested a pathway for 13pdo production from malate that involved two de novo reactions. By combining minRxn/minFlux with compilations of hypothetical reactions and metabolites (e.g., BNICE [70], GEM-Path [28], XTMS[27]) the scope and diversity of designed synthetic networks would increase significantly. In addition, integration of kinetic (e.g., BRENDA [101]) and toxicity information [102] can be incorporated within minRxn/minFlux to further restrict the design space by avoiding kinetic bottlenecks and toxic intermediates.

### 2 Alternative Embodiments

The publications and other material used herein to illuminate the background of the invention or provide additional details respecting the practice are herein incorporated by reference in their entirety. The present invention contemplates numerous variations, including variations in organisms, variations in bioprospecting objectives, variations in types of optimization problems formed and solutions used. These and/or other variations, modifications or alterations may be made therein without departing from the spirit and the scope of the invention as set forth in the appended claims.

## APPENDIX

Abbreviation for terminal and intermediate metabolites taking part in minimal networks


- 10fthf 10-Formyltetrahydrofolate;
- 13bpg 1,3-Bisphospho-D-glycerate;
- 13pdo 1,3-Propanediol;
- 1but 1-Butanol;
- 23bdo (R,R)-Butane-2,3-diol;
- 23hmbut (R)-2,3-Dihydroxy-3-methylbutanoate;
- 2alac (S)-2-Acetolactate;
- 2hetpp 2-Hydroxyethyl-ThPP
- 2hkbut 4-hydroxy-2-oxobutyrate
- 2kiv 2-keto-iso-valerate
- 2mmal (R)-2-Methylmalate;
- 2pg 2-Phospho-D-glycerate;
- 3hbtcoa (S)-3-Hydroxybutanoyl-CoA;
- 3hbut (R)-3-Hydroxybutanoate;
- 3hhex 3-Hydroxy-5-oxohexanoate
- 3hhexcoa 3-Hydroxy-5-oxohexanoyl-CoA
- 3 hp 3-Hydroxypropanal
- 3hpcoa Propenoyl-CoA;
- 3oprop 3-Oxopropanoate;
- 3pg 3-Phospho-D-glycerate;
- 3php 3-Phosphonooxypyruvate;
- 4hbtcoa 4-Hydroxybutyryl-CoA;
- 4hbut 4-Hydroxybutanoic acid;
- 5mthf 5-Methyltetrahydrofolate
- ac Acetate
- acact Acetoacetate
- acald Acetaldehyde
- accoa Acetyl-CoA
- achser O-Acetyl-L-homoserine;
- actcoa Acetoacetyl-CoA;
- actn Acetoin
- actp Acetyl phosphate
- akg alpha-Ketoglutaric acid
- alac 2-Acetolactate
- ara6p D-arabino-Hex-3-ulose 6-phosphate
- asp L-Aspartate;
- b-ala beta-Alanine;
- buta Butanal
- butcoa Butanoyl-CoA
- butcoa Butanoyl-CoA;
- ch4 Methane
- cit Citrate
- citcoa (3 S)-Citryl-CoA
- co Carbon monoxide
- co(I) Co(I) corrinoid protein
- co2 Carbon dioxide
- coa Coenzyme A
- coB Coenzyme B
- coM Coenzyme M
- com-cob CoM-S-S-CoB
- crtcoa Crotonoyl-CoA;
- dhap Dihydroxyacetone phosphate
- dhpgl Dihydrophloroglucinol
- dkhpdt 3,5-diketoheptanedioate
- dma Dimethylamine
- e4p D-Erythrose 4-phosphate
- etgly Ethylene glycol
- f6p D-Fructose 6-phosphate;
- fdo Oxidized ferredoxin
- fdp D-Fructose 1,6-bisphosphate
- fdr Reduced ferredoxin
- fe2 Iron(2+)
- fe3 Iron(3+)
- for Formate
- for-glu N-Formyl-L-glutamate
- form-glu N-Formimino-L-glutamate
- form-thf 5-Formiminotetrahydrofolate
- formd formaldehyde
- g3p D-Glyceraldehyde 3-phosphate
- g6p D-Glucose 6-phosphate;
- glc D-Glucose;
- glu L-Glutamate
- gluto Oxidized glutathione
- glutr Reduced Glutathione
- gly Glycine
- glyad glycoaldehyde
- glyc Glycerol
- glyc3p sn-Glycerol 3-phosphate;
- glycn Glycerone
- glycr Glycerate
- glyox Glyoxylate
- h2s Hydrogen sulfide;
- hpyr Hydroxypyruvate
- hser L-Homoserine;
- hso3 Sulfite
- ibutcoa Isobutyryl-CoA
- ibutcoa Isobutyryl-CoA
- icit Isocitrate
- lac L-Lactate
- laccoa Lactoyl-CoA
- lacd Lactaldehyde
- mal Malate
- malcoa Malonyl-CoA;
- malylcoa Malyl-CoA
- malylcoa Malyl-CoA;
- me-co(III) Methyl-Co(III) corrinoid protein
- me-coM Methylcoenzyme M
- meethf 5, 10-Methenyltetrahydrofolate
- meoh Methanol
- methf 5, 10-Methylenetetrahydrofolate
- mthgxl Methylglyoxal
- nad NAD+
- nadh NADH
- nadp NADP+
- nadph NADPH
- nh3 Ammonia
- no2 Nitrite
- oaa Oxaloacetate
- pep Phosphoenolpyruvate
- phgl Phloroglucinol
- prpp 5-Phosphoribosyl diphosphate;
- pser O-Phospho-L-serine;
- pyr Pyruvate
- r15bp D-Ribose 1,5-bisphosphate;
- r5p D-Ribose 5-phosphate;
- rib D-Ribose
- ru5p D-Ribulose 5-phosphate
- s17bp Sedoheptulose 1,7-bisphosphate
- s2o3 Thiosulfate
- s7p Sedoheptulose 7-phosphate
- s7p Sedoheptulose 7-phosphate;
- ser L-Serine;
- succ Succinate
- succal Succinate semialdehyde;
- succoa Succinyl-CoA;
- thf Tetrahydrofolate
- tma Trimethylamine
- tmaox Trimethylamine N-oxide;
- tpp Thiamin pyrophosphate;
- x1p L-Xylulose 1-phosphate
- xan Xanthine
- xans Xanthosine
- xmp Xanthosine 5′-phosphate
- xu L-Xylulose
- xu5p D-Xylulose 5-phosphate

### Abbreviation for the Reactions Described in the Minimal Networks

- 3HBTDH (S)-3-Hydroxybutanoyl-CoA:NADP+ oxidoreductase
- 3HBTDH (S)-3-Hydroxybutanoyl-CoA:NAD+ oxidoreductase
- 3HBTL (S)-3-hydroxybutanoyl-CoA hydro-lyase
- 3HPCH 3-Hydroxypropionyl-CoA hydrolase
- 3HPDH 3-hydroxypropionate:NADP+ oxidoreductase
- 3HXCT 3-hydroxybutyryl-CoA thiolase
- 3HXCTR 3-hydroxy-5-oxohexanoyl-CoA:acetate CoA-transferase
- 4HBTDH 4-hydroxybutanoate:NAD+ oxidoreductase
- 4HBTL 4-hydroxybutanoyl-CoA hydro-lyase
- 4HBTTR acetyl-CoA:4-hydroxybutanoate CoA-transferase
- 5MTHFRx 5-methyltetrahydrofolate:NAD+ oxidoreductase
- 5MTHFRy 5-methyltetrahydrofolate:ferredoxin oxidoreductase
- ACALD acetaldehyde:NAD+ oxidoreductase (CoA-acetylating)
- ACCOAC acetyl-coa carboxylase
- ACDC acetyl-coA decathonylase
- ACFTR Acetyl-CoA:formate C-acetyltransferase
- ACK acetate kinase (hydroxylating)
- ACK acetate kinate (ATP forming)
- ACNDH acetoin dehydrogenase
- ACONT Aconitase
- ACS acetyl-coA synthase
- ACTCH acetoacetyl-CoA hydrolase
- ACTPP
- ACTR Acetyl-CoA:acetyl-CoA C-acetyltransferase
- AHSTR Acetyl-CoA:L-homoserine 0-acetyltransferase
- AKGCL 2-Oxoglutarate carboxy-lyase
- ALACDC 2-acetolactate decarboxylase
- ALACL (S)-2-Acetolactate pyruvate-lyase (carboxylating)
- ALCD acetaldehyde:NAD+ oxidoreductase (CoA-acetylating)
- ALPYL 2-acetolactate pyruvate-lyase (carboxylating)
- ASPL L-aspartate 1-carboxy-lyase (beta-alanine-forming)
- ASPTA L-Aspartate:2-oxoglutamte aminotransferase
- BDODH (R,R)-Butane-2,3-diol:NAD+ oxidoreductase
- BTADH butanal:NAD+ oxidoreductase (CoA-acylating)
- BTCM isobutyryl-coa mutase
- BTDH butanoyl-CoA:NAD+ trans-2-oxidoreductase
- BUTDH 1-butanol dehydrogenase
- CO₂DH multi-step CO₂ folate reductase
- CODH carbon-monoxide,water:ferredoxin oxidoreductase
- CTCL (3 S)-citryl-CoA oxaloacetate-lyase (acetyl-CoA-forming)
- CTCTR Acetyl-CoA:citrate CoA-transferase
- DDT diol dehydratase
- DPGLDH dihydrophloroglucinol:NADP+ oxidoreductase
- DPGLH dihydrophloroglucinol hydrolase
- ENO enolase
- ETGLD 1,2-Ethanediol:NAD+ oxidoreductase
- F6PA fructose 6-phosphate aldolase
- FBA fructose-bisphosphate aldolase
- FBP fructose-bisphosphatase
- FDH formate dehydrogenase
- FDNADPR Ferredoxin:NADP+ oxidoreductase
- FDNADR Ferredoxin:NAD oxidoreductase
- FEDH Fe2+:NAD+ oxidoreductase
- FGLAH N-Formyl-L-glutamate amidohydrolase
- FGLFT 5-Formiminotetrahydrofolate:L-glutamate N-formiminotransferase
- FGLIH N-Formimino-L-glutamate iminohydrolase
- FORD Formaldehyde:NAD+ oxidoreductase
- FPK fructose-6-phosphate phosphoketolase
- FTFAL 5-Formiminotetrahydrofolate ammonia-lyase (cyclizing)
- FTHFH 10-Formyltetrahydrofolate amidohydrolase
- FTKT formaldehyde transketolase
- G3PD glycerol-3-phosphate dehydrogenase (NAD)
- G3PD2 sn-glycerol-3-phosphate:NADP+1-oxidoreductase
- G3PT glycerol-3-phosphatase
- GABT GABA transaminase (ambiguous);
- GAPD glyceraldehyde-3-phosphate dehydrogenase
- GHMT glycine hydroxymethyltransferase, reversible
- GLCL glycerol hydro-lyase (3-hydroxypropanal-forming)
- GLCRDH D-Glycerate:NAD+2-oxidoreductase
- GLCRK ATP:(R)-glycerate 2-phosphotransferase
- GLUDH promiscuous glutamate dehydrogenase;
- GLYCD glycerol:NAD+2-oxidoreductase
- GLYCDx Glycerol dehydrogenase
- GLYCHL Glycerol hydro-lyase
- GLYCL glycine cleavage system
- HBTDH (R)-3-Hydroxybutanoate:NAD+ oxidoreductase
- HBUTDC 4-hydroxy-2-oxobutyrate decarboxylase
- HDR heterodisulfide reductase
- HEX1 hexokinase (D-glucose:ATP)
- HMBL (R)-2,3-Dihydroxy-3-methylbutanoate hydro-lyase
- HMBTDH (R)-2,3-dihydroxy-3-methylbutanoate:NADP+ oxidoreductase
  (isomerizing)
- HPS hesulose-6-phosphate synthase
- HSDH hydrogen-sulfide:NADP+ oxidoreductase
- HXCOAT 3-hydroxy-5-oxohexanoyl-CoA thiolase
- ICDH Isocitrate:NADP+ oxidoreductase (decarboxylating)
- ICL Isocitrate Lyase
- ICM iso-butyryl-Coa mutase
- KIVDH 3-methyl-2-oxobutanoate:NAD+ oxidoreductase
  (CoA-mehtylpropanoylating)
- KIVR 2-ketoisovalerate oxidoreductase
- LA lactate aldolase
- LACAT Lacatate acyl transferase
- LACDH (S)-Lactate:NAD+ oxidoreductase
- LACDR (S)-lactaldehyde:NAD+ oxidoreductase
- LACDT Lactoyl-CoA dehydratase
- MALCDH malonyl-CoA dehydrogenase
- MALS malate synthase
- MCL malyl-coa ligase
- MCR CoM reductase
- MDH malate dehydrogenase (NADP)
- MDH malate dehydrogenase (NAD)
- MEDH methanol dehydrogenase
- MEDH methanol:NAD+ oxidoreductase
- METR methanol:coenzyme M methyltransferase
- MMALS 2-methyl malate synthase
- MTA/MTBA \[methyl-Co(III) corrinoid protein\]:coenzyme M
  methyltransferase
- MTHFH 5,10-Methenyltetrahydrofolate 5-hydrolase (decyclizing)
- MTHFL 5,10-methylenetetrahydrofolate folmaldehyde lyase
- MTHFR 5,10-methylenetetrahydrofolate:NAD+ oxidoreductase
- MTK malate thiokinase
- NH3DH ammonia:NAD+ oxidoreductase
- NIFDH nitrite:ferredoxin oxidoreductase
- PC pyruvate carboxylase
- PDC pyruvate carboxy-lyase (acetaldehyde-forming)
- PDODH propane-1,3-diol:NAD+1-oxidoreductase
- PFOR pyruvate:ferredoxin 2-oxidoreductase (CoA-acetylating)
- PGCD 3-Phospho-D-glycerate:NAD+2-oxidoreductase
- PGI glucose-6-phosphate isomerase
- PGK Phosphoglycerate kinase
- PGLSa Phloroglucinol synthase a
- PGLSb Phloroglucinol synthase b
- PGM D-phosphoglycerate 2,3-phosphomutase
- PHI 6-phospho-3-hexulo isomerase
- PPC phosphoenolpyruvate carboxylase
- PPS ATP:pyruvate,water phosphotransferase
- PRPPS ATP:ribose-1,5-bisphosphate phosphotransferase
- PSERT 3-Phosphoserine:2-oxoglutarate aminotransferase
- PSP O-phospho-L-serine phosphohydrolase
- R5PPT ATP:D-ribose-5-phosphate 1-phosphotransferase
- RIBI D-ribose aldose-ketose-isomerase
- RPE D-Ribulose-5-phosphate 3-epimerase
- RPI D-ribose-5-phosphate aldose-ketose-isomerase
- RUBK ATP:D-ribulose 5-phosphotransferase
- S2O3 Da Thiosulfate:thiol sulfurtransferase
- S2O3Db 3-Mercaptopyruvate:cyanide sulfurtransferase
- SBPH Sedoheptulose 1,7-bisphosphate 1-phosphohydrolase
- SBPL Sedoheptulose 1,7-bisphosphate D-glyceraldehyde-3-phosphate-lyase
- SERAT L-Serine:glyoxylate aminotransferase
- SUCADH succinate-semialdehyde:NADP+ oxidoreductase (CoA-acylating)
- SUCTR succinyl-CoA:acetoacetate CoA-transferase
- TALA transaldolase
- THD NADP transhydrogenase
- THFMT 5-methyltetrahydrofolate:corrinoid/iron-sulfur protein
  methyltransferase
- TKT1 transketolase
- TKT2 transketolase
- TMFL Trimethylamine-N-oxide formaldehyde-lyase
- TMMT trimethylamine methyltransferase
- TMMT trimethylamine:coenzyme M methyltransferase
- TMR NADH:trimethylamine-N-oxide oxidoreductase
- TPI triose-phosphate isomerase
- X1PL L-xylulose 1-phosphate glycolaldehyde-lyase
  (glycerone-phosphate-forming)
- X1PT ATP:L-xylulose 1-phosphotransferase
- X5PT ATP:D-xylulose 5-phosphotransferase
- XANH Xanthosine ribohydrolase
- XMPH xanthosine 5′-phosphate phosphohydrolase
- XMPS XMP:pyrophosphate phosphoribosyltransferase
- XPK xylulose-5-phosphate phosphoketolase

