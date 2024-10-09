# I. INTRODUCTION

Contacts are central to manipulation problems. Consequently, contact modeling has been an active area of research in robotics since the last several decades [1], [2], [3], [4], [5]. One of the most popular approaches to model contact dynamics is using Linear Complementarity Problem (LCP). LCP models are widely used for modeling contact dynamics in academia as well as in several physics simulation engines such as Bullet, ODE, etc. Trajectory optimization (TO) of LCP-based contact models has been used for manipulation [6], [7] and legged locomotion [8]. Lyapunov stability of linear systems with complementarity systems has also been studied [9], [10], [11]. However, most of these works assume deterministic contact models to perform TO. In reality, frictional interaction systems suffer from several uncertainties which lead to stochastic dynamics and thus, it is important to consider uncertainty during TO. Modeling uncertainty in LCP-based contact models leads to Stochastic Discrete-time Linear Complementarity System (SDLCS).

Fig. 1 pictorially shows a SDLCS we study in this paper. We consider the SDLCS that has uncertainty in parameters and additive noises in dynamics and complementarity constraints. As shown in Fig. 1, one should notice that uncertainty leads to stochastic evolution of system states in SDLCS. Thus, a robust optimization formulation should consider the uncertainty in state evolution. In some recent works that consider stochastic complementarity constraints, an expected residual minimization (ERM)-based [12] penalty is used to solve the robust optimization problem [13]. A major shortcoming of such an approach is that it fails to capture the stochastic evolution of system dynamics due to the Fig. 1: This paper presents chance-constrained optimization for SDLCS. The figure shows the case of a sliding box on a plane where the coefficient of friction is a Gaussian random variable. Note that w and v are additive uncertainty terms. stochastic complementarity constraint. In [14], the authors augment the formulation in [13] with chance constraints. However, this formulation has certain fundamental shortcomings which prevent constraint satisfaction guarantees. We present a formulation that circumvents these shortcomings by using a mixed integer formulation. Using some relaxation of the original joint chance complementarity constraint problem for the SDLCS, the resulting problem can be solved using mixed integer programming.

In this paper, we present a formulation of robust trajectory optimization for SDLCS. Since worst-case robust optimization is quite conservative and does not explicitly discuss stochastic evolution of states [15], this work considers probabilistic optimization with stochastic evolution of states. Robustness to uncertainty is provided by enforcing probabilistic satisfaction of state constraints. Under certain simplifications, we show that the chance-constrained problem can be reformulated as a Mixed Integer Quadratic Program with Chance Constraints.

Contributions. This paper has the following contributions: 1) We present a novel formulation for chance-constrained optimization of SDLCS. 2) We compare our proposed approach with several previously proposed techniques and demonstrate that our method outperforms the recent techniques in [13], [14]. The proposed algorithm is demonstrated on several manipulation systems with linear dynamics.

# II. RELATED WORK

In this section, we review some of the work which is most close to the work presented in this paper. Our work is closely related to TO techniques for contact-rich systems.

Contact-implicit TO techniques are becoming very popular for performing TO for contact-rich systems, and several techniques have been proposed for manipulation as well as legged locomotion [6], [8], [16]. All the above techniques assume perfect model knowledge and do not consider uncertainty.

There has been some recent work on robust TO in SNCS [13], [14], [17]. In [13], the authors have utilized the formulation of ERM for robust TO. ERM, first introduced in [12] for Stochastic Linear Complementarity Problem (SLCP), aims at minimizing the expected error in satisfying the SLCP. In [13], authors use ERM as an additional penalty term in their TO problem. However, such a formulation does not consider the stochastic state evolution of the system during optimization. A chance-constrained formulation for SNCS is presented in [14]. This method augments the ERMaugmented objective in [13] with additional chance constraints on satisfying the complementarity constraints. The formulation ignores the stochastic evolution of system state during optimization, and thus borrows the limitations of [13]. Furthermore, this formulation is incapable of enforcing a constraint violation probability smaller than 0.5 for any degree of uncertainty. Consequently, this method is very fragile for trajectories with the horizon, N > 1 as the chance of violating the constraints for such trajectories is 0.5N ≥ 1 [18]. Our formulation addresses these weaknesses under certain simplifying assumptions for SDLCS.

Another line of work which is relevant to understand some of our proposed work is related to chance-constrained optimization (CCO). This has been extensively studied in robotics as well as optimization literature [19], [20], [21]. In [19], authors have proposed stochastic optimization formulation for open-loop collision avoidance problems using chance constraints under Gaussian noise. [21] uses statistical moments of the distribution to handle non-Gaussian chance constraints. An important point to note here is that in all CC formulation for dynamic optimization, one needs to consider the CDF function for the joint probability distribution of all variables. However, such distribution is generally extremely challenging to compute. Thus, in general, the joint chance constraint is decomposed into individual chance constraints using Boole's inequality (see [19], [21]), which results in very conservative approximation of the individual constraints. Our formulation utilizes Boole's inequality to convert the original computationally intractable joint chance constraints into conservative but tractable independent chance constraints.

# III. PROBLEM PRELIMINARY

For the completeness of the paper, we provide a brief introduction to linear complementarity problem and its stochastic form. This is followed by a problem formulation for robust trajectory optimization for linear dynamical systems with stochastic complementarity solution. We also point several key differences of our approach from previous attempts for robust trajectory optimization for stochastic complementarity system.

## A. Discrete-time Linear Complementarity System (DLCS)

A DLCS is a discrete-time linear dynamical system with complementarity constraints [11] given by:

where k is the time-step index, x k ∈ R nx is the state, u k ∈ R nu is the control input, and λ k ∈ R nc is the algebraic variable (e.g., contact forces). In addition, The notation 0 ≤ a ⊥ b ≥ 0 denotes the complementarity constraints a ≥ 0, b ≥ 0, ab = 0. Given a x k , u k , an unique solution λ k+1 to (1b) exists if F is P-matrix [22]. If F does not satisfy the P-matrix property, it is possible that λ k+1 satisfying (1b) is non-unique or nonexistent.

## B. Contact-Implicit Trajectory Optimization

A contact-implicit trajectory optimization for the DLCS can be formulated as:

where x s , x g represent the initial and the terminal values, respectively, X ⊆ R nx and U ⊆ R nu are convex polytopes consisting of a finite number of linear inequality constraints, λ u is the upper bound of λ k , and N is the time horizon.

While (2) is widely used in various robotic applications, it can be fragile under uncertainty, which is often the case in model-based manipulation. Hence, we consider a novel formulation of (2) so that the generated trajectory from the optimization would be robust under uncertainty.

## C. Stochastic Discrete-time Linear Complementarity Systems (SDLCS)

We consider the following SDLCS, i.e. DLCS with uncertainty:

where

are known additive uncertainty. We consider the case where the coefficient matrix C in (3a) and F in (3b) are stochastic matrices to discuss a more realistic stochastic effect due to complementarity constraints. This corresponds to the case when one might have uncertainty arising from parameter identification leading to a SDLCS. An alternative to this is to allow the complementarity variable λ k+1 to be stochastic. However, such treatment is out of the scope of the current work. Our treatment of SDLCS leads to stochastic evolution of system states x k , while we treat λ k+1 as deterministic. The assumption of determinacy in λ k+1 is similar to several previous works [12], [13], [14], [23]. The authors in [13] use ERM to solve TO of SDLCS and use the following cost function:

where ψ is an Nonlinear Complementarity Problem (NCP) function, β is a weighting scalar. We compare the robustness of our formulation with (4) in Sec V.

# IV. ROBUST TRAJECTORY OPTIMIZATION FOR SDLCS

In this section, we describe our formulation for robust TO of SDLCS. We consider:

where Pr denotes the probability of an event and ∆ ∈ (0, 0.5] is the user-defined maximum violation probability, where the probability of violating constraints is bounded by ∆. x s , Σ s are the mean and covariance matrix of the state at k = 0. X and U are convex polytopes, consisting of a finite number of linear inequality constraints. In Sec IV-A, we describe how we convert (5c) to a tractable optimization problem.

For clarity of presentation, we explain the reasoning behind our formulation shown in (5). Since the underlying SDLCS is uncertain (also see Fig. 1), we consider a chance-constrained formulation for optimization to capture stochastic evolution of states (see discussion in Sec I) where we impose multiple constraints simultaneously. This is represented as joint chance constraints for the complementarity constraints as well as the states, which is succinctly written in Equation (5c)). Note that we represent the chance constraints on all the variables jointly (as is common in stochastic optimization for dynamic systems) using the cdf for the state as well as complementarity variables. We show in the rest of this section how the joint constraints can be decomposed into individual chance constraints using Boole's inequality. It is also important to note that unlike (5), the method in [13], [14] fails to capture the stochastic evolution of states in their formulation.

In this work, we make the following assumptions for (5): 1) Noise terms w k , v k follow Gaussian distribution.

2) The complementarity variable λ k+1 is deterministic.

3) Each element of vectors Cλ k+1 and F λ k+1 are independent Gaussian variables. We explain the rationale for above assumptions in Sec IV-B.

## A. Joint Linear Chance Constraints

We consider joint chance constraint such that multiple constraints are satisfied simultaneously with a prespecified probability. More specifically, we consider the joint chance constraint (5c) so that the complementarity constraints and state bound constraints over the whole time horizon of the optimized trajectory are satisfied with probability 1 -∆. We denote the complementarity relationship in (3b) succinctly as (λ k+1,i , y k+1,i ) ∈ S for i = 1, . . . , n c . Hence, in this optimization problem (5), we have the following joint chance constraints:

where is the logical AND operator. L represents the number of chance constraints involving x at k, except for the complementarity constraints. a l ∈ R nx is the constant vector and b l is a scalar.

Obtaining a cumulative distribution function (cdf) of ( 6) is challenging because the joint probability of states and complementarity variables is considered. The only way to decompose joint chance constraints is Boole's inequality [18] that converts the original computationally intractable joint chance constraints into conservative but tractable independent constraints. Hence, similar to previous works, we employ Boole's inequality [18] to get the conservative approximation of (6) as follows:

Using Boole's inequality again, we can further obtain the conservative chance constraints given by:

We discuss how to handle (8a) in Sec IV-B. We formulate (8b) as its equivalent deterministic form:

where xk , Σ x k are the mean and covariance matrix of x k , respectively. Φ -1 is an inverse of the cdf of the standard normal distribution.

Fig. 2: Deterministic and stochastic complementarity constraints. We have the complementarity constraints 0 ≤ λ k+1,i ⊥ y k+1,i ≥ 0 where y k+1,i has uncertainty and accepts the violation of ǫ.

## B. Chance Complementarity Constraints (CCC) for SDLCS

We make the assumptions as specified in Sec IV. While a more general formulation could allow the complementarity variable λ k+1 to be stochastic, we do not consider it here. However, we believe that allowing C and F to be stochastic can achieve a similar effect in SDLCS. Furthermore, in cases where the distribution of λ k+1 is known, our proposed formulation can be easily extended to incorporate stochasticity in λ k+1 . However, for brevity, we skip these details. The Gaussian assumption on uncertainty is made primarily to allow equivalent reformulation of the chance constraints to deterministic inequalities.

While [14] proposed a promising CCC, their formulation possesses empty solutions when ∆ ≤ 0.5 (see [14]). This can result in a very fragile trajectory since the total violation probability over N steps would be always more than 1 if N ≥ 1 (using Boole's inequality). This is because they use a Non-Linear Programming (NLP) formulation which needs to impose all CCC constraints simultaneously which compete with each other.

In our formulation, we decompose stochastic complementarity constraints into two modes (see Fig. 2) as follows:

where θ = ∆1 N nc . Note that now y k+1 ∼ N ȳk+1 , Σ y k+1 . To realize lower violation probabilities, we first propose the following CCC using MIP as:

where z k,i,0 , z k,i,1 represent the integer variables to represent the two modes which satisfies z k,i,0 + z k,i,1 = 1 for i-th complementarity constraint at instant k.

However, Pr (y k+1,i = 0) is zero (as probability measure for singleton sets is zero) so that we cannot directly use (11). To alleviate this issue while avoiding negative values for λ, we propose the following CCC using a relaxation for complementarity constraints (see Fig. 2):

where ǫ > 0 is the acceptable violation in the complementarity constraints.

We have two-sided linear chance constraints in (12a). We decompose (12a) as two one-sided chance constraints so that we can use the same reformulation in (9). Note that each one-sided chance constraints, obtained from the two-sided chance constraint, are formulated with a maximum violation probability of θ 2 . Since we have integer constraints, MIP can impose individual constraints for each mode. Thus, we do not need to impose all constraints simultaneously like the NLP formulation in [14]. This provides a lower bound for θ as function of ǫ, ȳk+1,i , and Σ y k+1 ,ii , which is presented as a lemma.

Lemma IV.1. Suppose the CCC are formulated as ( 12) and ǫ, ȳk+1,i , and Σ y k+1 ,ii are specified.

Proof. Consider case (i): From (9b) and (12a), the twoside chance constraints in (12a) are converted to their deterministic forms:

Simplifying this equation, we obtain the bound specified in (i). Consider case (ii): From (9b) and (12b), the one-side chance constraints in (12b) are converted as: ȳk+1,i ≥ ǫ + Σ y k+1 ,ii Φ -1 (1θ). Simplifying this equation, we obtain the bound specified in (ii).

Remark 1: From Lemma IV.1, it is easy to show that θ < 1  2 if ǫ 2Σy k+1 ,ii > Φ -1 ( 3 4 ) for case (i), and if (ȳ k+1,iǫ)/Σ y k+1 ii > Φ -1 ( 1 2 ) for case (ii). In contrast, the formulation in [14] cannot enforce the chance constraints for any θ < 0.5.

We use the following equations for uncertainty propagation in the SDLCS:

where W represents the noise covariance matrix and Cλ k+1 represents a mean of Cλ k+1 .

, which is a diagonal matrix because of the independence of random variables. Note that λ k+1 is a decision variable. Consequently, we introduce another simplification by considering the worstcase uncertainty for λ k+1 during uncertainty propagation. This conservative simplification offers computational advantages during the resulting optimization.

## C. Mixed-Integer Quadratic Programming with Chance Constraints (MIQPCC)

In this section, we present our MIQPCC formulation to solve (5). To impose our proposed CCC, one can solve either MIP or NLP. Our MIP-based method solves disjunctive inequalities while NLP needs to impose all CCC simultaneously, which yields an empty solution for ∆ ≤ 0.5.

Our proposed MIQPCC is formulated as follows:

where

are the binary decision variables for the i-th complementarity constraint at k to represent mode 1, 2, respectively. Using these binary variables, we employ big-M formulation to deal with disjunctive inequalities in our CCC. The parameter M is a valid upper bound for λ k , y k .

# V. NUMERICAL SIMULATIONS

We validate our proposed methods for three benchmark DLCS: a cartpole with softwalls, a sliding box with friction, and dual manipulators as illustrated in Fig. 3, inspired by [10]. Through the experiments, we try to answer the following questions:

1) Can our proposed optimization generate robust openloop trajectories? 2) Can our proposed formulation satisfy the probabilistic constraints imposed during optimization? 3) How does the proposed method compare against the previous methods for robust optimization in SDLCS?

## A. Implementation Details

We implemented our method in Python using Gurobi [24] to solve the proposed MIQP. We implemented the MPCC with PYROBOCOP [6] to solve the ERM-based method in [13] and the CCC method in [14]. The examples are implemented on a computer with Intel i7-8565U processor.

To verify the robustness of open-loop trajectories obtained from our proposed optimization, we use Monte Carlo simulations. We propagate the dynamics by finding the roots of the complementarity system with sampled parameters given the control sequence obtained from optimization. We run each case for 1000 trials with different sampled parameters to estimate the probability of failure. Note that unlike the continuous-domain dynamics, we cannot rollout the dynamics for SDLCS with the given control sequences since we do not have the access to λ k+1 . We add the noise sampled from the distribution which was used during optimization.

For simplicity, we show the continuous-time dynamics. We then discretize continuous-time dynamics into discrete-time dynamics using the explicit Euler method with sample time dt = 0.033. For notation simplicity, we denote x 0 , Σ 0 as mean and covariance matrix at k = 0 for states of systems, respectively.

## B. Example Details 1) Cartpole with Softwalls:

The continuous-time dynamics with complementarity constraints for the cartpole with softwalls is as follows:

where x 1 is the cart position, x 2 is the pole angle, the x 3 and x 4 are their derivatives. u 1 is the control and λ 1 , λ 2 are the reaction forces at from the wall 1, 2, respectively. We consider the additive noise w, the zero-mean i.i.d. Gaussian noise which standard deviation is 2 × 10 -4 , to x 1,k , x 2,k . k 1 = 10, k 2 = 10 are the stiffness of walls 1 and 2, respectively. In this example, we assume that the uncertainty also arises from the 1 k1 , 1 k2 which standard deviations are 10 -5 . g = 9.81 is the gravitational acceleration, m p = 0.1, m c = 1.0 are the mass of the pole, cart, respectively. l = 0.5 is the length of the pole and d = 0.15 is the distance from the origin of the coordinate to the walls.

The optimization setup is as follows. N = 20, M = 100, Q = diag(0, 0, 0, 0), R = 0.01, ǫ = 0.002, x 0 = [-0.15, 0, 0, 0] ⊤ , Σ 0 = diag(0, 0, 0, 0). We also have the following chance constraints:

## 2) Sliding Box with Friction:

The continuous-time quasistatic dynamics with complementarity constraints for sliding box with Coulomb friction is as follows:

x 1 is the box position and x 2 is the box velocity. u is the control and λ + , λ -are the positive and negative component of the friction force, respectively. γ is the slack variable. α = 4 is the damping constant, m = 1 is the mass of the box, and µ = 0.1 is the coefficient of friction. We consider the additive i.i.d. Gaussian noise w as x 1,k+1 = x 1,k + x 2,k dt + w. The standard deviations of w is 4 × 10 -4 . g = 9.81 is the gravitational acceleration. We assume that the uncertainty also arises from the µ which standard deviations are 10 -5 . The optimization setup is as follows. N = 20, M = 100, Q = diag(0, 0, 0, 0), R = 0.01, ǫ = 0.01, x 0 = [1, -1] ⊤ , Σ 0 = diag(0, 0). We also have the following chance constraints:

3) Dual Manipulators: We consider the example where the box is manipulated by two manipulators with Coulomb friction and the contact forces from the manipulators. The continuous-time quasi-static dynamics is as follows:

x 1 , x 3 , x 5 are the positions of the box, the left arm, the right arm, respectively and x 2 , x 4 , x 6 are their derivatives. u 1 , u 2 represent the controls of the left and the right arm, respectively. λ + , λ -are the positive and negative component of the friction force, respectively. γ is the slack variable. λ 1 , λ 2 are the contact forces from the left arm and the right arm, respectively. We set g = 9.81, m = 1, k = 100, µ = 0.1. We discretize the dynamics (17) with dt = 0.033 and add the zero-mean i.i.d. Gaussian noise w which standard deviation is 0.0002 such as x 1,k+1 = x 1,k + x 2,k dt + w. The standard derivation of µ and 1 k are 0.0001. The optimization setup in this example is as follows. N = 20, M = 50, Q = diag(0, 0, 0, 0, 0, 0), R = diag(1, 1), ǫ = 0.0042, x 0 = [0.1, -1.1, 0, 0, 0.1, 0] ⊤ , Σ 0 = diag(0, 0, 0, 0, 0, 0). We have the following chance constraints: Pr(x 1,k ≥ -0.17

## C. Robustness of Open-Loop Trajectories

The optimized control and state trajectories for the three systems using our proposed method are shown in Fig. 4-Fig. 6. Overall, these figures show that the planner generates state trajectories that are farther away from the bound specified in the chance constraints as the violation probability decreases. For instance, Fig. 4 shows that the trajectories are farther away from x = 0.05 as ∆ decreases. In addition, the trajectory with ∆ = 0.02 reaches its maximum value Fig. 4: State and control trajectories with different ∆ for the cartpole example. First, the cart moves in the negative direction to utilize the contact force λ 2 because the control input is bounded. Once the cart obtains enough λ 2 , the cart is accelerated to the positive direction. We can observe the effect of our proposed chance constraints in particular around t ∈ [0, 0.1] and t ∈ [0.4, 0.5]. When t ∈ [0, 0.1], the mode changes from the "contact on the wall 2" to the "no contact" and the cart tries to be far from wall 2 to satisfy the CCC. When t ∈ [0.4, 0.5], the trajectories are farther away from x 1 = 0.05 and x 2 = 0.15 as ∆ decreases.

earlier than other trajectories to account for the evolution of the uncertainty. We observe the same behavior for the other example too. In addition, these figures illustrate that the control costs increase as ∆ decreases. This illustrates the trade-off relation between safety and cost.

At this point, we would like to discuss the magnitude of uncertainty we consider in these problems. Compared to some other stochastic optimal control works [19], [20], the uncertainty in these problems is relatively smaller. There are several reasons why we need to have a smaller uncertainty. Note that as we have explained in Sec III, our approach satisfies joint constraints on multiple constraints together. First, our formulation has chance complementarity constraints in addition to chance constraints on states, which are commonly used. Our formulation has more number of chance constraints, and consequently, the lower uncertainty is required because of the conservative approximation of Boole's inequality to resolve joint chance constraints into individual constraints as explained in Sec IV-A, Sec IV-B. Second, we need to have a small ǫ to avoid large violation of complementarity constraints, which requires small uncertainty. Finally, we would like to emphasize that allowing larger uncertainties requires either better resolution of joint chance constraints or covariance steering approaches [20], which is out of scope for the current study.

## D. Monte Carlo Simulation Results

Table I-Table III show our Monte Carlo simulation results given the control sequences with different ∆ from the optimization compared to the ERM method in [13] and the CCC method in [14]. We run the ERM method in [13] with different weighting β and the CCC [14] with violation probability ∆ z = 0.5. β was chosen so that the magnitude of the ERM cost is a similar order of other costs. For a fair comparison, we regard that the constraints are violated if the chance constraints are not satisfied in our method. We regard Fig. 5: State and control trajectories with different ∆ for a sliding box with friction. First, the box is accelerated in the positive direction. Then, the control decreases with time to regulate the box around the origin by employing the friction forces. We can observe the effect of our proposed chance constraints in particular around t ∈ [0.2, 0.3] where the trajectories are farther away from x 1 = 0.88 as ∆ decreases. Fig. 6: Time history of x 1 with different maximum violation probabilities ∆ for dual manipulation. First, the box is pushed by the right arm in the negative direction. Next, the left arm regulates the box to the origin. In particular, around t ∈ 0.2 -0.3 s, the trajectories are farther away from x 1 = -0.17 as ∆ decreases.

that the constraints are violated in the ERM in [13] and the CCC methods in [14] if the terminal chance constraints used in our proposed method are not satisfied.

Table I shows that the empirically obtained violation probabilities are lower than the specified violation probabilities used in our proposed optimization. In contrast, the control sequences based on the ERM method in [13] show 100% violation probabilities with β = 10 4 , 10 5 , which are much worse than the obtained violation probabilities using our proposed method. With β = 10 3 , we got a relatively good violation probability. The CCC in [14] could also show the relatively good violation probability compared to the ERM-based method with β = 10 4 , 10 5 but shows the worse violation probability compared to our method with ∆ = 0.5 and the ERM with β = 10 3 . Thus, we confirm that our proposed approach satisfies chance constraints in the simulator in this example.

Table II shows that empirically obtained violation probabilities are lower than the specified violation probabilities used in our proposed optimization like the cartpole example, except for the cases with ∆ = 0.01, 0.002. There are several factors that contribute to the violation of the chance constraints. Unlike the cartpole example, F is not a P matrix so we can get the multiple solutions in λ, which can lead to non-Gaussian distributions. Also, even though ǫ is small, it  [13], and the CCC in [14] with ∆z = 0.5, and obtained ∆ from the simulation of "cartpole with softwalls" over 1000 samples.   [13], and the CCC in [14] with ∆z = 0.5, and obtained ∆ from the simulation of "a sliding box with friction" over 1000 samples. is not zero so the actual trajectory in the simulator cannot be exactly the same as the trajectory from the optimization even with no noise. While we can ignore these effects with relatively large ∆, we cannot ignore these effects anymore with the small ∆. Although the planner could not satisfy the chance constraints for all ∆ in this example, our method achieves much lower violation probabilities compared to the ERM in [13] and the CCC in [14]. Table III shows that we have the same discussion for the dual manipulators example as for the pushing a box example. Fig. 7 and Fig. 8 show that our proposed planner could successfully drive the system to the goal state. We also observe that with decreasing ∆, the system trajectories move further away from state set boundaries to satisfy tighter chance constraints. For Fig. 9, while the majority of the sampled trajectories converge to the specified terminal constraints, some of them clearly converged to other states. This result also shows that the true distribution of the uncertainty for the dynamics systems with LCS is not Gaussian.

# VI. DISCUSSION AND CONCLUSION

The hybrid dynamics of frictional interaction as well as uncertainty associated with frictional parameters make the efficient design of model-based controllers for manipulation challenging. In this paper, we presented a robust TO technique for contact-rich systems. We presented a formulation for chance constrained optimization for SDLCS which is solved using MIQPCC. We compared our proposed approach against other recent techniques for robust optimization for stochastic complementarity systems. We showed that our formulation leads to more robust trajectories compared to these techniques.

In the future, we would like to relax certain assumptions in this work. We would like to propose solutions for general non-linear stochastic complementarity systems in the presence of non-Gaussian noise. In the current work, using joint chance constraints on all the variables results in conservative solutions. To consider these problems, the study of nonlinear uncertainty propagation in SNCS is required. Also, we need to solve mixed-integer non-linear programming. We would also like investigate how we can relax the conservative solutions obtained by our proposed approach using better TABLE III: Comparison of our specified ∆ in optimization, specified β in ERM, and the CCC with ∆z = 0.5, and obtained ∆ from the simulation of "dual manipulation" over 1000 samples. measures for risk. We would also like to incorporate real-time sensor input [25] to develop algorithms for stochastic model predictive control of complex manipulation problems [17].

Another interesting line of work would to be to include a Reinforcement learning algorithm to get model updates [26] during learning.  

