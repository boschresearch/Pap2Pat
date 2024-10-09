# DESCRIPTION

## STATEMENT OF GOVERNMENT INTEREST

This invention was made with Government support under 1910397 awarded by the National Science Foundation. The Government has certain rights in this invention.

## TECHNICAL FIELD

This specification relates generally to methods, systems, and computer readable media for dynamic routing of users under a mixed information framework.

## BACKGROUND

Dynamic Traffic Assignment (DTA) algorithms have been used to capture dynamic interaction between supply and demand under equilibrium and non-equilibrium conditions in a transportation network. The two optimal conditions for a transportation network are Dynamic User Equilibrium (DUE) and Dynamic System Optimal (DSO) equilibrium. Many conventional DTA algorithms solve for one of Wardrop's equilibrium conditions using a single group of drivers who share a common objective of minimizing their own travel cost or the total system cost.

## SUMMARY

This document describes methods and systems for dynamic routing of users. The methods and systems can be used for reducing traffic congestion using the competing strategies between informed and uninformed drivers. Under a mixed information framework, a navigation app provides within-day route suggestions to informed drivers using predicted information about the time-varying route habits of uninformed drivers. The informed users detour from initially proposed routes to minimize network congestion after traffic disruptions, pushing the system toward optimal equilibrium, while uninformed drivers make day-to-day decisions which push the system toward user equilibrium. Simulations considering varying fractions of informed drivers show that congestion is reduced during abrupt phase transition before reaching equilibrium by approximately 59.2% when 20% of drivers are informed, and is nearly eliminated when 80% of drivers are informed, which could be achieved through connected vehicle technologies. Shared memory multi-core parallelization improved the computational efficiency

In some examples, a method includes determining a first traffic flow model for uninformed drivers of vehicles and determining a second traffic flow model for informed drivers of vehicles. Each of the informed drivers makes driving decisions based on receiving dynamic routes from a traffic routing system. The method includes iteratively updating the second traffic flow model using the first traffic flow model until a convergence criterion is met. The method includes sending, to at least one informed driver, a first dynamic route from a first origin to a first destination using the second traffic flow model.

The computer systems described in this specification may be implemented in hardware, software, firmware, or any combination thereof. In some examples, the computer systems may be implemented using a computer readable medium having stored thereon computer executable instructions that when executed by the processor of a computer control the computer to perform steps. Examples of suitable computer readable media include non-transitory computer readable media, such as disk memory devices, chip memory devices, programmable logic devices, and application specific integrated circuits. In addition, a computer readable medium that implements the subject matter described herein may be located on a single device or computing platform or may be distributed across multiple devices or computing platforms.

## DETAILED DESCRIPTION

This document describes an application of DTA which realistically simulates a transportation network in which drivers have different objectives and different time scales over which they make decisions in an attempt to optimize the system. We define informed drivers as the ones who are given predictive route guidance from a system manager (e.g., traffic operation center) through, for example, global positioning system (GPS)-based applications and assume that these drivers will make a bounded route choice with the provided guidance. Informed drivers are expected to comply with the provided guidance if they are given sufficient incentives and/or if the new route is not noticeably different from the original choice in terms of the cost. Such compliance will become more practical with shared autonomous vehicles that are expected to lower traveler's disutility of travel time through credits from the company for following those suggestions.

The role of information is especially relevant under expected and unexpected disruptions to infrastructure. Transportation networks are commonly impacted by short-term and long-term disruptions caused by natural or man-made events. For example, a multi-day construction zone on a highway can increase the travel time if travelers continue to follow the same route. Similarly, a post disaster event such as flooding of neighborhood streets or a tree collapse may result in reduced capacity on certain links.

The methods and systems described in this document use a mixed information framework for providing within-day route suggestions to informed drivers using predicted information about the time-varying route habits of uninformed drivers. The informed users detour from initially proposed routes to minimize network congestion after traffic disruptions, pushing the system toward optimal equilibrium, while uninformed drivers make day-to-day decisions which push the system toward user equilibrium.

FIG. 1 is a diagram illustrating an example mixed objective framework that provides a method for a group of informed drivers to reduce the within-day congestion caused by uninformed drivers who are making choices based on day-to-day habits on route and departure time after a traffic disruption. Informed drivers are provided with the within-day route guidance based on the anticipated behaviors of uninformed drivers on the network day-to-day, by adjusting route choices toward system optimum.

In some cases, the day-to-day evolution of traffic flows follows the same framework as the iterative process of DTA models and accurately simulates the iterative day-to-day transition of the adaptive and bounded behavior of uninformed drivers during the disruption of a transportation network. The resulting congestion patterns are caused by uninformed drivers' discrete decision-making processes before reaching equilibrium.

The day-to-day decision-making of uninformed drivers may result in congestion depending on levels of perturbations and network congestion. The systems and methods described in this document can be used to reduce the congestion caused by uninformed users making day-to-day decisions by strategically rerouting informed drivers. The within-day traffic dynamics are incorporated into the simulation at the end of the day to reoptimize (for example, offline) next day's informed driver strategy considering day-to-day dynamics of uninformed drivers. For an application to a post disaster event, day 1 of the model is after loading within-day travel behaviors of the day of the collapse. The methods and systems can be applied to inform human drivers, Connected Autonomous Vehicles (CAVs) operating in mixed autonomy networks, or both.

FIG. 2 is a block diagram of an example system 200 for dynamically providing routes to users of vehicles. The system 200 includes a traffic routing system 202 configured for modeling the behavior of uniformed drivers 204 and providing routes to informed drivers 206a-b over a network. The traffic routing system 202 can provide routes over a data communications network 208, e.g., a cellular telecommunications network that communicates wirelessly with computing devices in the vehicles 206a-b. The traffic routing system 202 can provide routes to vehicles 206a where the driver is using a navigation system, to vehicles 206b that are operating autonomously, or both.

The traffic routing system 202 includes one or more processors 210 and memory 212 storing executable instructions for the one or more processors 210. In operation, the traffic routing system 202 implements a dynamic traffic router using the processors 210 and memory 212 for sending dynamic routes to the informed drivers 206a-b.

The traffic routing system 202 includes an uninformed driver model builder 214 configured for determining a traffic flow model 216 for the uninformed drivers 204. Determining the traffic flow model 216 can include determining the first traffic flow model comprises determining a dynamic network loading (DNL) model using a day-to-day boundedly rational dynamic user equilibrium (BRDUE) algorithm. Determining the dynamic network loading (DNL) model using the day-to-day boundedly rational dynamic user equilibrium (BRDUE) algorithm comprises selecting one or more routes based on at least one simulated effective path delay. Further examples regarding the traffic flow model 216 for the uninformed drivers 204 is provided below.

The traffic routing system 202 includes an informed driver model builder 218 configured for determining a traffic flow model 220 for the informed drivers 206a-b. The informed drivers 206a-b make driving decisions based on receiving dynamic routes from the traffic routing system 202. The informed driver model builder 218 is configured for iteratively updating the traffic flow model 220 using the traffic flow model 216 for the uninformed drivers 204 until a convergence criterion is met.

Determining the traffic flow model 220 can include determining a dynamic network loading (DNL) model using a within-day dynamic system optimal (DSO) algorithm. Determining the dynamic network loading (DNL) model using the within-day dynamic system optimal (DSO) algorithm can include selecting one or more routes based on at least one path marginal cost (PMC). Iteratively updating the second traffic flow model can include iteratively updating, for each route of a plurality of routes, a demand for the route. Iteratively updating the second traffic flow model can include determining a route decision for at least one informed driver using an informed driver Mlogit model. Further examples regarding the traffic flow model 220 are provided below.

The traffic routing system 202 receives updated traffic data from a traffic information server 222. The traffic information server 222 can provide any appropriate information regarding traffic flow for the uninformed driver model builder 214 and the informed driver model builder 218. For example, the traffic information server 222 can provide live traffic flow data, e.g., from navigation systems in the vehicles 206a-b of the informed drivers. In another example, the traffic information server 222 can provide updates regarding road closures.

The traffic routing system 202 includes a dynamic traffic assignor 224 configured for sending, to one or more informed drivers 206a-b, dynamic routes using the traffic flow model 220. Sending a dynamic route can include sending the dynamic route to a navigation system in a vehicle 206a of an informed driver, causing the navigation system to present the dynamic route to the informed driver. Sending a first dynamic route comprises sending the first dynamic route to an autonomous driving system 206b for the at least one informed driver.

The traffic routing system 202 is illustrated in FIG. 2 as being a single computing system; however, in operation, various functions of the traffic routing system 202 can be distributed. For example, the model builders 214 and 218 can be implemented in a separate system from the dynamic traffic assignor 224, such that model building is performed offline and dynamic traffic assignment is performed by a separate system serving users.

In some examples, the model builders 214 and 218 can be implemented using parallel processing. An additional convenient property of the WD DSO methodology is that it is easily parallelized, allowing further computational improvements over the serial method. The ease of parallelization comes from the fact that each calculation of PMC only considers the effect of one path and departure time on all other paths and departure times. Each PMC calculation is independent of other PMC calculations. Therefore, parallelization can be applied to make the problem more computationally tractable.

FIG. 3 is a flow diagram of an example method 300 for determining traffic flow models that contain a mixture of informed and uninformed drivers with different routing behaviors towards reaching equilibrium across different time scales. Uninformed drivers make their route and departure time choices based on the memory of their own prior effective travel cost and selfishly seek to minimize their own travel time.

If all drivers are uninformed, the route choices will iteratively converge to the BRDUE conditions. The informed drivers in the presented model can be, for example, accessing an app, which they use to determine their route and departure time choice. The informed drivers make within-day decisions based on the information presented by the app, which suggests the best routes based on the predicted network state for that day. Unlike the uninformed drivers, informed drivers are given routes that seek to push the system toward WD DSO equilibrium. Informed drivers' route and departure time choices are calculated using a separate within-day DNL procedure. The within-day DNL procedure is used to calculate the PMC for each route and departure time. PMC considers the additional delay on all other drivers when an informed driver chooses a given route and departure time.


- - Group 1 (Uninformed): Choose route and departure time based on
    Effective Path Delay, using DTD BRDUE DTA algorithm, influenced the
    transition between the presence of perturbations and after removal
    of perturbations. Drivers are selfishly seeking to minimize their
    own travel time.
  - Group 2 (Informed): Choose route and departure time using a smart
    phone navigation app, or other appropriate navigation system, which
    suggests routes with the least PMC. This is calculated using a
    within-day DTA algorithm. These drivers are directed to push the
    system toward DSO, mitigating congestion caused by the inability of
    uninformed drivers to predict perturbations in the network.

The extent to which Group 2 (Informed drivers) can be rerouted is subject to additional constraints based on information gained for other informed drivers and their own indifference bands. Informed drivers should be convinced to choose a system optimal route and, in some cases, it will only work over time if the maximum deviation from a user optimal route is within their indifference band, which is defined as a range of total travel times over which the informed travelers are indifferent.

For example, if the shortest travel time at DUE between an OD pair is Z units and the indifference band for an informed traveler is z units, then informed travelers are convinced to switch their routes and departure times based on their experienced travel time such that their resulting travel time is at most Z+z. In some example, the range of indifference band is up to 400 seconds.

The method 300 starts from the initialization of the demand for each O-D pair at each departure time without informed drivers switching routes (302), run day to day and within-day DNL until the minimum solution is found in DSO with informed drivers strategy for a fixed number of days. The method 300 includes running the DTD BRDUE DNL model (304) and then calculating a path marginal cost (306). The method 300 includes running the WD DSO O-D DNL model (308) and updating the DSO O-D demand values (310). The method 300 includes checking if a convergence criterion is met (312), and if not, incrementing an iteration (314) and repeating the calculation of PMC, running the WD DSO DNL model, and updating the DSO O-D demand.

If the convergence criteria is met, the method 300 includes checking if a last day has been reached (316), e.g., a last day specified by a system operator. If so, then the method 300 stops (322). If not, then the method 300 includes incrementing the day (318), updating the BRDUE O-D demand values, and repeating the method 300 starting from running the DTD BRDUE DNL (304).

FIG. 4 shows a table of notations that summarizes the notations used in this document. The following sections describe examples of building traffic flow models for uninformed drivers and informed drivers.

Dynamic Network Loading Model

Consider a traffic network represented by a directed graph G=(, ) consisting of set  of all nodes, and set  of all directed links. The network is dynamic where set T denote the set of all discrete time interval indices ranging from 1,2, . . . , |T|, where each interval is one time unit wide; for our experiments, we consider each time unit to be 6 seconds.

Let ⊆N2 denote the set of all OD pairs with positive demand. In our model, travelers between an OD pair choose the departure time and routes. Denote by drs the total demand traveling from node r to node s (assumed to be known apriori). Let Krs denote the set of all routes connecting OD pair [r, s]∈ where each route k∈Krs is an ordered sequence of links appearing from start to end. Let K=Krs be the set of all routes in the network. The flow from node r to node s departing at time t via route k∈Krs is denoted by hk(t). Equation (1) defines the flow conservation for each OD pair.

drs=Σt∈TΣk∈Kk∈Khk(t) ∀[r, s]∈  (1)

Next, we describe the dynamic network loading model. Equation 2 denotes the link occupancy, or the number of vehicles on a given link l∈ at time t∈T , which is the difference between the cumulative arrival and departure curves Al(t) and Dl(t).

ol(t)=Al(t)−Dl(t) ∀l∈, t∈T  (2)

The density pl(t) on link l at time t is denoted by Equation 3 as a function of the number of lanes on the link (denoted by nl) and the length of the link (denoted by Ll).

\(\begin{matrix}
{{\rho_{l}(t)} = \frac{o_{l}(t)}{n_{l}L_{i}}} & (3)
\end{matrix}\)

This density function can be generalized for any spatial location x measured along the length of a link l at time t, represented as pl(t, x), by taking the limit of the ratio of total time with the total area in the time space diagram as the area of the region becomes infinitely close to zero centered at point (t, x).

Models for traffic flow determine the variation of density for different times and locations. The Lighthill-Whitham-Richards (LWR) model assumes a deterministic relationship between density and flow expressed as fundamental diagram and denoted by fl(⋅) for all links l∈. Incorporating the conservation of vehicles, the partial differential equation (PDE) in Equation 4 is then used to calculate dynamics of density and flow across each link:

∂tρl(t, xl)+∂xfl(ρl(t, xl)=0 xl∈[al, bl], ∀t∈Tand l∈  (4)

where xl is any point along the length of the link l∈ with al and bl denoting the start and end points of the link (assuming a parameterized curve that represents a link in two dimensions).

In our model, we assume the flow function fl(⋅) in the LWR model is given by a triangular fundamental diagram as shown in FIG. 5. This fundamental diagram uses two linear functions to approximate the relationship between flow and density on any given link. The intercept of the two functions is the critical density ρlc for the link, while the jam density ρljam is the location where the function with a negative slope intersects the density axis. Using the triangular fundamental diagram, the flow for a given density, forward wave speed v, and backward wave speed w is given by Equation 5.

\(\begin{matrix}
{{f_{l}(\rho)} = \left\{ \begin{matrix}
{v\rho} & {\rho \in \left\lbrack {0,\rho_{l}^{c}} \right\rbrack} \\
{- {w\left( {\rho - \rho_{l}^{jam}} \right.}} & {\rho \in \left\lbrack {\rho_{l}^{c},\rho_{l}^{jam}} \right\rbrack}
\end{matrix} \right.} & (5)
\end{matrix}\)

To solve the PDE in Equation 4 we need to know the time-varying rates of maximum flow that can enter each link (link demand) and the time-varying rates of maximum flow that can exit each link (link supply). The time-varying supply and demand functions for each link, denoted by S(ρl(t)) and D(ρl(t)) respectively, can then be approximated using the triangular fundamental diagram , where C is the link capacity.

\(\begin{matrix}
\begin{matrix}
{{D\left( {\rho_{l}(t)} \right)} = \left\{ \begin{matrix}
{v{\rho_{l}(t)}} & {\rho < \rho_{l}^{c}} \\
C & {\rho \geq \rho_{l}^{c}}
\end{matrix} \right.} & (6)
\end{matrix} \\
\begin{matrix}
{{S\left( {\rho_{l}(t)} \right)} = \left\{ \begin{matrix}
C & {\rho < \rho_{l}^{c}} \\
{- {w\left( {{\rho_{l}(t)} - \rho_{l}^{jam}} \right)}} & {\rho \geq \rho_{l}^{c}}
\end{matrix} \right.} & (7)
\end{matrix}
\end{matrix}\)

The flow model on each link can be extended to networks with multiple links meeting at junctions, which are nodes with at least one incoming and one outgoing link. Let ⊆ denote the set of all junctions. For a given junction n∈, conservation of flow across all links is given by Equation 8 which can be used as additional boundary condition to solve the combined PDEs for each incoming and outgoing link:

Σm∈Mfm(ρm(t, bm))=Σq∈Qfq(ρq(t, aq)) ∀t∈T, n∈  (8)

To prevent confusion, subscripts m or q are used in this document to indicate the association with inlink m or outlink q.

Various junction dynamics determine how flows split at each junction. In our model, we consider a path-based DNL that tracks flow on each path. The decision making of users who pass through each junction are considered in FIG. 6 to calculate the actual supply and demand on each of the connecting links. This is accomplished by calculating the proportion of users on an incoming link m∈M who will select the outgoing link q∈Q. Given the cumulative arrival and departure curves, it is possible to determine an entry time for each link τm(t) based on the exit time (t) for a link m. Let γm,k(t, bm) denote the proportion of flow leaving link m from its exit point bm along route k at time t. Following the first-in-first-out principle and using the link entry time for a given exit time, the proportional contribution of an individual path flow to the total flow on a given link at time t can be estimated as follows:

γm,k(t, bm)=γm,k(τm(t), am)  (9)

In other words, the proportion of flow leaving link m along path k at time t is equal to the proportion of flow entering link m at time τm(t). The sum of these proportions on link m over each path containing two connected links m and q gives the total proportion αm,q(t) of flow entering link q from link m at time t as shown in FIG. 6. That is,

αm,q(t)=γm,k(t, bm)  (10)

A distribution matrix n(t), for a junction n∈ satisfying conservation of flow in Equation 8, is then constructed in Equation 11 to track the distribution of flows between incoming and outgoing links.

n(t)={αm,q(t)} ∀m∈Mn, q∈Qn, n∈  (11)

The non-junction nodes such as source nodes with no incoming links and sink nodes with no outgoing links consider a simplified traffic dynamics. Sink nodes are assumed to have infinite sink capacity allowing the flow on routes terminating at the sink node to exit. On contrary, source nodes may not be able to load the entire demand if the outgoing links experience queue spillback. A point-queue model is used to account for the dynamics at origin nodes (which includes source nodes or junctions that also act as origins). In the following sections, examples of the uninformed and informed driver models are described.

Uninformed Driver Model

We model the day-to-day behavior of drivers after a disruption to the network where drivers adapt their departure time and route choice. Let  denote the set of days post disruption indexed by d ranging from 1,2 . . . , ||. The update dynamics of departure time and route choice for uninformed drivers is governed by an iterative structure where travelers adapt their routes to converge to the new post-disruption equilibrium. We approximate this dynamic using a multinomial Logit model described next.

First, to circumvent exponentially high number of routes, we narrow the set of possible routes over which travelers consider updating their routes. We define canonical routes as the set of routes that deviate from the fastest path (i.e. minimum travel time path) within a specified tolerance. For a traveler departing from O-D pair [r, s]∈ at time t∈T, the set of canonical routes is denoted by rs(t) and is defined as following:

{ rs ( t ) = \{ k ❘ k ∈ K rs , TT k ( t ) - TT rs * ( t ) TT rs * ( t )
≤ Θ \} ( 12 ) }

where TTk(t) is the travel time on route k for departure time t, TT*rs(t) is the travel time on the time-dependent shortest path connecting O-D pair [r, s]∈ for departure time t∈T, and Θ is the driver's perception deviance. We assume Θ to be fixed across all travelers. We note that the canonical route set is time-dependent since shortest path may be different for different departure times.

Building on the BRDUE model, we update the route and departure time decisions for uninformed drivers using a Multinomial Logit Model (Mlogit). Let (k, t)d denote the choice tuple representing the route and the departure time on day d∈. After executing the select choices on a given day, travelers update their choices (k, t)d+1 for the next day using the MLOGIT model.

The utility of a choice is approximated using the perceived cost of each route and departure time choice for every O-D pair. We assume homogeneity across all travelers between an origin-destination pair.

The perceived cost for each route and departure time, in terms of both travel time and schedule delay (early or late arrival), is calculated in Equation 13:

PCk(t)=TTk(t)+SCDk(t) ∀k∈K, t∈T  (13)

where SCDk(t) is the schedule delay cost for path k and departure time t, given by Equation 14,

\(\begin{matrix}
{{{SCD}_{k}(t)} = \left\{ {{\begin{matrix}
{\phi_{e}\left( {{{AT}_{k}(t)} - {TA}_{rs}} \right)} & {{{if}{{AT}_{k}(t)}} \leq {TA}_{rx}} \\
{\phi_{l}\left( {{{AT}_{k}(t)} - {TA}_{rs}} \right)} & {{{if}{{AT}_{k}(t)}} > {TA}_{rx}}
\end{matrix}{\forall{k\epsilon K_{rs}}}},{\left\lbrack {r,s} \right\rbrack\epsilon\mathcal{P}},{t\epsilon T}} \right.} & (14)
\end{matrix}\)

where ATk(t)=t+TTk(t) is the actual arrival time at the destination for route k and departure time t, TArs is the desired arrival time for all travelers associated with the OD pair [r,s] (a single value assumed to be known apriori for each OD pair), ϕe is the coefficient of early arrival penalty, and ϕl is the coefficient of late arrival penalty. Equation 13 can now be incorporated into the Mlogit model.

The Mlogit model estimates the probability of choosing an alternative given the utilities across all alternatives. Let Crs be the set of all alternatives for all travelers across an OD pair [r, s]∈, defined as follows:

Crs={(k, t)|k∈rs(t), t∈T}

For the Mlogit model, the utility of an alternative (k, t)∈Crs is given by U(k,t)=−PCk(t)+ε(k,t), where ε(k,t) are the error terms associated with the utilities that are assumed to be independent and identically distributed as a Gumbel distribution with a scale parameter θ>0 and location parameter assumed to be 0. Given the assumptions, the probability of choosing alternative (k, t)∈Crs for travelers between OD pair [r, s] is given by:

{ ( k , t ) = ( U ( k , t ) \textgreater{} max ( k ′ , t ′ ) ∈ C rs ( k
′ , t ′ ) ≠ ( k , t ) U ( k ′ , t ′ ) ) = exp ⁡ ( - θ ⁢ PC k ( t ) ) ∑ ( k
″ , t ″ ) ∈ C rs exp ⁡ ( - θ ⁢ PC k ″ ( t ″ ) ) ( 15 ) }

and the path flows for a given departure time is computed as:

hk(t)=drs(k,t) ∀(k, t)∈Crs, [r, s]∈  (16)

To model the boundedly-rational behavior of travelers, we consider an indifference band  that increases the utility of current alternative thus increasing the likelihood that the traveler continues to stay on the currently chosen alternative over the next day. Adding a superscript d denoting the day of travel, we denote by hkd(t) the number of travelers choosing route k at time t on day d. We can then update the flow on next day d+1, by considering the current flow on alternative (k, t) that continues to stay with the same alternative, and the flow from all other alternatives (k′, t′) that switch to the alternative (k, t).

Equation 17 shows the update of flow from one day to the next.

{ h k d + 1 ( t ) = h k d ( t ) ( k , t ) ← ( k , t ) + ∑ ( k ′ , t ′ )
∈ C rs ( k ′ , t ′ ) ≠ ( k , t ) h k ′ d ( t ′ ) ( k , t ) ← ( k ′ , t ′
) ( 17 ) }

where (k,t)←(k,t) is the probability that travelers choosing alternative (k, t)∈Crs will continue with the same alternative on the next day, computed as:

{ ( k , t ) ← ( k , t ) = e ( - θ × ( PC k ( t ) - Δ ) ) e ( - θ × ( PC
k ( t ) - Δ ) ) + ∑ ( k ″ , t ″ ) ∈ C rs ( k ″ , t ″ ) ≠ ( k , t ) e ( -
θ × PC k ″ ( t ″ ) ) ( 18 ) }

and (k,t)←(k′,t′) is the probability that travelers choosing alternative (k′, t′)∈Crs will switch their alternative to (k, t) on the next day, computed as:

{ ( k , t ) ← ( k ′ , t ′ ) = e ( - θ × PC k ( t ) ) e ( - θ × ( PC k ′
( t ′ ) - Δ ) ) + ∑ ( k ″ , t ″ ) ∈ C rs ( k ″ , t ″ ) ≠ ( k ′ , t ′ ) e
( - θ × PC k ″ ( t ″ ) ) ( 19 ) }

It is easy to verify that if =0, then (k,t)←(k′,t′)=(k,t)←(k,t)=(k,t), and Equation 17 reduces to Equation 16.

Informed Driver Model

Informed drivers in the presented model are given route suggestions that minimize a cost function representing the total system cost. These users seek to reduce congestion faced by all other drivers in the network, but without noticeably penalizing themselves. Such a cost function needs to consider both the system-level cost and the cost to the user when selecting a path and departure time.

In some examples, the system 202 can use a utility function in building the informed driver model. The utility function considers the travel cost and the benefit in terms of information gained for other drivers in the network. An example utility function is provided below.

\(U_{i,k} = {{PTT}_{i,k} - {\left( {\alpha/{❘K❘}} \right){\sum\limits_{j \in {x^{i}(t)}}{{\delta\sigma}\left( {k_{i},{k_{j \in {x^{i}(t)}}^{*}❘Y},\Psi} \right)}}}}\)

where ki is route for driver i, k*i is a canonical route for driver j, and δσ(ki, |Υ, ψ) is the variance reduction (e.g., information gain) of k* for driver j∈xi(t) on link i when driver j runs some other route k given current driver's observation Υ and other drivers' observations ψ under the traffic data variance σ (e.g., standard deviation of travel time) with weights on the observation δ (e.g., number of samples), where xi(t) is a list of all drivers using link i. The utility function Ui,k is the difference between PTT and the benefit of information gain to all other drivers when driver j takes a detour from path k* to k to gather information. These utility functions perform best under information sharing frameworks and simulations with large amounts of uncertainty. The example utility function presented above can be used to strategically alter the behavior of informed drivers by considering the trade-off of exploration and exploitation. The route with minimum disutility is presented to the informed driver, e.g., through a route suggestion app as being the most preferable route.

DSO Computation

Let h={hk(t)|k∈K, t∈T} denote the departure-rate pattern as a vector of all path flows at different departure times. The DSO formulation is defined using the following optimization problem

\(\begin{matrix}
{\min\limits_{h}\left( {{TSC} = {\sum_{k \in K}{\sum_{t \in T}{{h_{k}(t)} \times {{PC}_{k}(t)}}}}} \right)} & (20)
\end{matrix}\)

subject to the following constraints:

\(\begin{matrix}
\begin{matrix}
{{\sum_{t \in T}{\sum_{k \in K_{rs}}{h_{k}(t)}}} = {d_{rs}{\forall{\left\lbrack {r,s} \right\rbrack \in}}}} \\
{{{h_{k}(t)} \geq {0{\forall{k \in K}}}},{t \in T}}
\end{matrix} & {(21){and}(22)}
\end{matrix}\)

where hk(t) is the departure rate, and PCk,t is the perceived cost for route k at time t, and TSC is the total system cost.

A departure rate pattern h is a DSO solution if and only if it is equilibrated based on the corresponding path marginal cost (PMC). The PMC is defined as the increase in total system cost incurred when an additional unit of flow is added to the departure rate pattern hk(t). The PMC for route k at time t is calculated in Equation 23:

\(\begin{matrix}
{{PMC_{k,t}} = {\frac{{\partial T}SC}{\partial{h_{k}(t)}} = {{PMC_{k,t}^{TT}} + {PMC_{k,t}^{SCD}} + {P{C_{k}(t)}}}}} & (23)
\end{matrix}\)

where PMCk,tTT is the change in travel time cost for all other users caused by additional flow on route k at time t, PMCk,tSCD is the change in schedule delay cost for all other traffic caused by the additional flow on route k at time t, and PCk(t) is the perceived cost for an individual on route k at time t (Equation 13).

Naively using a DNL algorithm to calculate the PMC for each path and departure time can be computationally demanding. For a set of all time periods, the naive method requires |z,900 |×|T| DNL solutions per DSO iteration.

In some examples, we approximate the PMCk,tTT using the Bureau of Public Roads (BPR) function since solving the exact path marginal cost is complex due to the non-linear nature of the DNL procedure. While actual DNL is used for daily simulation of revised change in flow, the cost incurred by each traveler's route and departure time choice is estimated with revised BPR function.

Let's assume that an estimate for the travel time on route k at departure time t can be calculated using the BPR function:

{ TT k ( t ) ≈ t 0 , k × {[} 1 + α ( h k ( t ) k ) β {]} ( 24 ) }

where t0,k is the free flow travel time (defined as the sum of free flow travel time on path links), hk(t) is the flow (e.g., veh/hr) on route k at time t, Ck is the capacity of route k, and α and β are parameters. We define Ck to be the minimum capacity across all links along the path.

While the congested links and time of congestion are computed from DNL, we consider the revised BPR to approximate the change in cost to all other paths due to change in flow on path k. To compute the impact of one unit of flow with and without the presence of congestion, we find all the paths that go through congested links in route k and iterate through all of the links in route k. Once the value of PMCk,tTT is approximated, the revised destination arrival time is estimated at the destination of route k for a departure time t, and the new value of PMCk,tSDC is approximated using Equation 14 as before.

In some examples, substantial computational improvements are made by only calculating PMC for paths and times which incur congestion and which propagate congestion onto other paths and departure times. This is accomplished by avoiding computing PMC for all uncongested paths and times, since these paths and times are assumed to be traversed at the free flow travel time and have no marginal cost on other paths or departure times. In addition, no PMC calculations are required for other paths and departure times which are unaffected by congestion on a given path at a given time. As shown in the triangular fundamental diagram (Equation 5), there is no impact of an additional vehicle below critical density for the link. Using these methods, the total number of paths and departure times requiring PMC calculation is minimized for a given spatiotemporal distribution of congestion in the network. After PMC for each path is solved, informed drivers make an updated decision using the Informed Driver Mlogit Model (IDMM) described in the next subsection, then the DNL model is executed to generate a new congestion pattern based on the decisions of informed drivers.

Informed Driver Mlogit Model (IDMM)

Finding DSO for informed drivers requires multiple iterations of route and departure time decisions. Unlike the MSA and some conventional quadratic programming models, in each subiteration i of DSO computations route and departure time decisions for informed drivers are made using the Mlogit model. Mlogit models are used for alternative-invariant problems, meaning that the regressor does not vary over the alternatives but does vary over the individual. Since the PMC already accounts for the effect that selecting an alternative has on all other alternatives and presents it as a cost which varies only over the individual, the IDMM described in this section can be treated as alternative-invariant.

Informed drivers also consider route choice over a limited canonical set of routes as defined in Equation 12. For the informed drivers, the utility of an alternative (k,t)∈Crs is given by U(k,t)=−PMCk,t+ε(k,t). The PMC for each path k and departure time t available to the O-D pair p is calculated for use in the IDMM. As in the previous section, the selection of base alternative for each solution is sequentially selected from the set of paths between the O-D pair and the set of possible departure times.

PMCk,t=PCk(t)+PMCk,tTT+PMCk,tSCD  (25)

where PMCk,tSCD is the sum of schedule delays (Equation 14) for all other paths and departure times when 1 additional unit of flow is added to path k at time t, PMCk,tTT is the cost in terms of travel time for all other paths and departure times when 1 additional unit of flow is added to path k at time t, and PCk(t) is the perceived cost of current flow on path k at time t. Therefore, PMCk,t is the marginal cost of path k at time t on all other paths and departure times. We can add travel time without schedule delays because if drivers arrive within the desired arrival time window, there is no penalty, however, if not, those will be in the later time window. Having many drivers departing at the same time as an aggregate will incur congestion, which we want to avoid.

The update of flow from one iteration to the next is governed by the IDMM model. For each OD pair [r, s]∈, the model computes the probability of switching from all other route-departure time tuples (k′, t′)∈Crs; (k′, t′)≠(k, t) to a given alternative tuple (k, t)∈Crs. The total probability of choosing route k and departure time t in the next iteration also includes the proportion of drivers who already selected route k at time t and choose not to detour or adjust their departure time. Similarly to the uninformed model, a constant scaling parameter θ2 (0.04) is used for distribution of utility errors, along with the BR switching threshold Δ2 (800 seconds), which still applies to informed drivers since not all drivers will be convinced to switch when provided with a predictive alternate route.

Path flow update from iteration i to i+1 for computing DSO is computed as follows. First, adding a superscript i, DSO denoting the subiteration of DSO computation, we denote by hki,DSO(t) the number of travelers choosing route k at time t in DSO iteration i. We can then update the flow on next iteration i+1, by considering the current flow on alternative (k, t) that continues to stay with the same alternative, and the flow from all other alternatives (k′, t′) that switch to the alternative (k, t). We assume that the uninformed driver flow is unaffected and remains constant in the background for each DSO iteration.

Equation 26 shows the update of flow from one iteration to the next.

{ h k i + 1 , DSO ( t ) = h k i , DSO ( t ) ( k , t ) ← ( k , t ) DSO +
∑ ( k ′ , t ′ ) ∈ C rs ( k ′ , t ′ ) ≠ ( k , t ) h k ′ i , DSO ( t ′ ) (
k , t ) ← ( k ′ , t ′ ) DSO ( 26 ) }

where (k,t)←(k,t)DSO is the probability that travelers choosing alternative (k, t)∈Crs will continue with the same alternative in the next DSO iteration, computed as:

{ ( k , t ) ← ( k , t ) DSO = e ( - θ 2 × ( PMC k , t - Δ 2 ) ) e ( - θ
2 × ( PMC k , t - Δ 2 ) ) + ∑ ( k ″ , t ″ ) ∈ C rs ( k ″ , t ″ ) ≠ ( k ,
t ) e ( - θ 2 × PMC k ″ , t ″ ) ( 27 ) }

and (k,t)←(k′,t′)DSO is the probability that travelers choosing alternative (k′, t′)∈Crs will switch their alternative to (k, t) in the next DSO iteration, computed as:

{ ( k , t ) ← ( k ′ , t ′ ) DSO = e ( - θ 2 × PMC k , t ) e ( - θ 2 × (
PMC k ′ , t ′ - Δ 2 ) ) + ∑ ( k ″ , t ″ ) ∈ C rs ( k ″ , t ″ ) ≠ ( k ′ ,
t ′ ) e ( - θ 2 × PMC k ″ , t ″ ) ( 28 ) }

The iterative process of shifting travelers along different alternatives continues until convergence criteria is met. For example, the process can terminate after a fixed number of DSO iterations.

Although specific examples and features have been described above, these examples and features are not intended to limit the scope of the present disclosure, even where only a single example is described with respect to a particular feature. Examples of features provided in the disclosure are intended to be illustrative rather than restrictive unless stated otherwise. The above description is intended to cover such alternatives, modifications, and equivalents as would be apparent to a person skilled in the art having the benefit of this disclosure.

The scope of the present disclosure includes any feature or combination of features disclosed in this specification (either explicitly or implicitly), or any generalization of features disclosed, whether or not such features or generalizations mitigate any or all of the problems described in this specification. Accordingly, new claims may be formulated during prosecution of this application (or an application claiming priority to this application) to any such combination of features. In particular, with reference to the appended claims, features from dependent claims may be combined with those of the independent claims and features from respective independent claims may be combined in any appropriate manner and not merely in the specific combinations enumerated in the appended claims.

