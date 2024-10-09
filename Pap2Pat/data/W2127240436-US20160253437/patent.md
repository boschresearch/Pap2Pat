# DESCRIPTION

## FIELD OF THE INVENTION

This invention pertains to the field of cyber-physical systems (CPS), and, in particular to models approximating the behavior of CPS and methods for monitoring the actual CPS that are based on the models.

## BACKGROUND OF THE INVENTION

Formal verification and validation play a crucial role in making cyber-physical systems (CPS) safe. Formal methods make strong guarantees about the system behavior if accurate models of the system can be obtained, including models of the controller and of the physical dynamics. In CPS, models are essential; but any model that can be built necessarily deviates from the real world. If the real system fits to the model, the behavior of the real system can be guaranteed to satisfy the correctness properties verified with respect to the model. If not, then this verification is impossible.

Cyber-physical systems (“CPS”) span controllers and the relevant dynamics of the environment. Since safety is crucial for CPS, their models (e. g., hybrid system models) need to be verified formally. Formal verification guarantees that a model is safe with respect to a safety property. The remaining task is to validate whether the models are adequate, such that the verification results transfer to the system implementation.

Actual system execution, however, provides many opportunities for surprising deviations from the model. Faults may cause the system to function improperly, sensors may deliver uncertain values and actuators may suffer from disturbance. The formal verification may have assumed simpler ideal-world dynamics for tractability reasons or made un-realistically strong assumptions about the behavior of other agents in the environment. Simpler models are often better for real-time decisions and optimizations, because they make predictions feasible to compute at the required rate. The same phenomenon of simplicity for predictability is often exploited for the models in formal verification and validation. As a consequence, the verification results obtained about models of a CPS only apply to the actual CPS at runtime to the extent that the system fits to the model.

Validation, i.e., checking whether a CPS implementation fits to a model, is an interesting but difficult problem. CPS models are more difficult to analyze than ordinary (discrete) programs because of the physical plant, the environment, sensor inaccuracies, and actuator disturbance. In CPS, models are essential; but any model necessarily deviates from the real world. Still, good models can be correct within certain error margins.

## SUMMARY OF THE INVENTION

Herein we introduce a method (referred to herein as “ModelPlex”) to synthesize monitors by theorem proving. The method uses sound proof rules to formally verify that a model is safe and to synthesize provably correct monitors that validate compliance of system executions with the model.

This invention performs runtime model validation. That is, validating whether a model, shown for example, in FIG. 3 as reference number 100, which is assumed for verification purposes is adequate for a particular system execution to ensure that the verification results apply to the current execution. The invention checks system execution with respect to a monitor specification 104, and thus, belongs to the field of runtime verification. Herein, the term runtime validation is used to clearly convey the purpose of monitoring. While “runtime verification” monitors properties without offline verification, “runtime validation” monitors model adequacy to transfer offline verification results. The focus of the invention is on verifiably correct runtime validation to ensure that verified properties of models provably apply, which is important for safety and certification of CPS.

If an observed system execution fits to the verified model 12, then this execution is safe according to the offline verification result about the model. If it does not fit, then the system is potentially unsafe because it no longer has an applicable safety proof, so a verified fail-safe action to avoid safety risks is initiated. Checking whether a system execution fits to a verified model 12 includes checking that the actions chosen by the (unverified) controller implementation fit to one of the choices and requirements of the verified controller model. It also includes checking that the observed states can be explained by the plant model. The crucial questions are: How can a compliance monitor be synthesized that provably represents the verified model? How much safety margin does a system need to ensure that fail-safe actions are initiated early enough for the system to remain safe even if its behavior ceases to comply with the model?

The second question is related to feedback control and can only be answered when assuming constraints on the deviation of the real system dynamics from the plant model. Otherwise, if the real system can be infinitely far off from the model, safety guarantees are impossible. By the sampling theorem in signal processing, such constraints further enable compliance monitoring solely on the basis of sample points instead of the unobservable intermediate states about which no sensor data exists. When such constraints are not available, the method of the present invention still generates verifiably correct runtime tests, which detect deviation from the model at the sampling points, not just between them. A fail-safe action will then lead to best-effort mitigation of safety risks (rather than guaranteed safety).

As presented herein, the present invention is a method to synthesize verifiably correct runtime validation monitors automatically. ModelPlex uses theorem proving with sound proof rules to turn hybrid system models into monitors in a verifiably correct way. Upon non-compliance with the model, ModelPlex initiates provably safe fail-safe actions.

ModelPlex is a principle to build and verify high-assurance controllers for safety-critical computerized systems that interact physically with their environment. It guarantees that verification results about CPS models transfer to the real system by safeguarding against deviations from the verified model. Monitors created by ModelPlex are provably correct and check at runtime whether or not the actual behavior of a CPS complies with the verified model and its assumptions. Upon non-compliance, ModelPlex initiates fail-safe fallback strategies. To initiate the fallback strategies early enough, ModelPlex uses prediction on the basis of disturbed plant models to check safety for the next control cycle. This way, ModelPlex ensures that verification results about a model of a CPS transfer to the actual system behavior at runtime.

## DETAILED DESCRIPTION OF THE INVENTION

### Preliminaries: Differential Dynamic Logic

For hybrid systems verification differential dynamic logic  is used, which has a notation for hybrid systems as hybrid programs.  allows us to make statements that we want to be true for all runs of a hybrid program ([α]ø) or for at least one run αø) of a hybrid program.

Both constructs are necessary to derive safe monitors: [α]ø proofs are needed to ensure that all behavior of a model (including controllers) is safe; αø proofs are needed to find monitor specifications that detect whether or not system execution fits to the verified model.

Table 1 summarizes the relevant syntax fragment of hybrid programs together with an informal semantics. The semantics ρ(α) of hybrid program α is a relation on initial and final states of running α. The set of  formulas is generated by the following grammar (<∈{<, <, =, ≧, >}, and θ1, θ2 are arithmetic expressions in +, −, ·, / over the reals):

Φ::=θ1˜θ2|Φ|Φψ|Φψ|Φ→ψ|∀xΦ|∃xΦ|[α]Φ|αΦ

Differential dynamic logic comes uses a theorem prover with a verification technique to prove correctness properties of hybrid programs. One example of a theorem prover and the one that is used in the preferred embodiment of the invention is KeYmaera.

### ModelPlex Approach for Verified Runtime Validation

CPS are almost impossible to get right without sufficient attention to prior analysis, for instance by formal verification and formal validation techniques. We assume to be given a verified model of a CPS, i.e. formula (1) is proved valid. Note that differential dynamic logic () and KeYmaera as a theorem prover are used to illustrate the concepts herein. The concept of ModelPlex is not predicated on the use of KeYmaera to prove (1). Other verification techniques could be used to establish validity of this formula. The flexibility of the underlying logic , its support for both [α]Φ and αΦ, and its proof calculus, however, are exploited for systematically constructing monitors from proofs in the sequel.

Φ→[α*]ψ with invariant φ→[α]φs.t.Φ→φ and φ→ψ  (1)

Formula (1) expresses that all runs of the hybrid system α*, which start in states that satisfy the precondition ø and repeat the model α arbitrarily many times, must end in states that satisfy the post condition ψ. Formula (1) is proved using some form of induction, which shows that a loop invariant φ holds after every run of α if it was true before. The model α is a hybrid system model 100 of a CPS, which means that it describes both the discrete control actions of the controllers in the system and the continuous physics of the plant and the system's environment.

The safety guarantees obtained by proving formula (1) about the model α* transfer to the real system, if the actual CPS execution fits to α*. Because safety properties should be preserved, a CPS γ fits to a model α*, if the CPS reaches at most those states that are reachable by the model, i.e., ρ(γ)ρ(α*). However, we do not know γ and therefore need to find a condition based on α* that can be checked at runtime to see if concrete runs of γ behave like α*.

Checking the post condition ψ is not sufficient because, if ψ does not hold, the system is already unsafe. Checking the invariant φ is insufficient as well, because if φ does not hold, the controller can no longer guarantee safety, even though the system may not yet be unsafe. But if we detect when a CPS is about to deviate from α* before leaving φ, we can still switch to a fail-safe controller to avoid ψ from happening.

As shown in FIG. 1, ModelPlex derives three kinds of monitors, a model monitor 20, a controller monitor 22, and a prediction monitor 24. Reachability between consecutive states in α, αctrl, and αδplant are checked by verifying states during execution against the corresponding monitor.

Model monitor 20—In each state vi the sample point vi−1 from the previous execution γi−1 is tested for deviation from the single α, not α* i. e., test (vi−1, vi) ∈ρ(α). If violated, other verified properties may no longer hold for the system. The system, however, is still safe if a prediction monitor 24 was satisfied on vi−1.Frequent violations indicate an inadequate model that should be revised to better reflect reality.

Controller monitor 22—In intermediate state {tilde over (v)}i the current controller decisions of the implementation γctrl are tested for compliance with the model, i.e., test (vi, {tilde over (v)}i) ∈ρ(αctrl). Controller monitors 22 are designed for switching between controllers similar to Simplex. If violated, the commands from a fail-safe controller replace the current controller's decisions to ensure that no unsafe commands are ever actuated.

Prediction monitor 24—In intermediate state {tilde over (v)}i the worst-case safety impact of the current controller decisions are tested with respect to the predictions of a bounded deviation plant model αδplant, which has a tolerance around the model plant αplant, i.e., check vi+1|=φ for all vi+1 such that ({tilde over (v)}i, vi+1) ∈ρ(αδplant). Note, that all vi+1 are simultaneously checked by checking {tilde over (v)}i for a characterizing condition of αδplant. If violated, the current control choice is not guaranteed to keep the system safe until the next control cycle and, thus, a fail-safe controller takes over.

The assumption for the prediction monitor 24 is that the real execution is not arbitrarily far off the plant models used for safety verification, because otherwise guarantees can neither be made on unobservable intermediate states nor on safety of the future system evolution. A separation of disturbance causes in the models can be used: ideal plant models αplant for correctness verification purposes, implementation deviation plant models αδplant for monitoring purposes. Any deviation model (e.g., piecewise constant disturbance, differential inclusion models of disturbance) is supported, as long as the deviation is bounded and differential invariants can be found. It is assumed that monitor evaluations are at most some s time units apart (e.g., along with a recurring controller execution). Note that disturbance in αδplant is more manageable compared to α*, as single runs α can be focused on instead of repetitions for monitoring.

### Relation Between States

A check that inspects states of the actual CPS to detect deviation from the model α* is systematically derived. First, a notion of state recall is established and shows that, when all previous state pairs comply with the model, compliance of the entire execution can be checked by checking the latest two states (vi−1, vi).

Definition 1 (State recall). V is used to denote the set of variables whose state we want to recall. YV−≡x∈Vx=x− are used to express a characterization of the values of variables in a state prior to a run of α, where the fresh variables x− to are always presumed to occur solely in YV−. The variables in x− can be used to recall this state. Likewise, YV+≡x∈Vx=x+ is used to characterize the posterior states and expect fresh x+.

With this notation, the following lemma states that an interconnected sequence of α transitions forms a transition of α*.

Lemma 1 (Loop prior and posterior state). Let a be a hybrid program and α* be the program that repeats arbitrarily many times. Assume that all consecutive pairs of states (vi−1, vi) ∈ρ(α) of n ∈+ executions, whose valuations are recalled with YVi≡x∈Vx=xi and YVi−1 are plausible with respect to the model α, i.e., . ≦i≦n (YVi−1→αYVi) with YV−=YV0 and YV+=YVn. Then, the sequence of states originates from an α* execution from YV0 to YVn, i.e., YV−→α*YV+.

Lemma 1 enables us to check compliance with the model α* up to the current state by checking reachability of a posterior state from a prior state on each execution of α (i.e., online monitoring, which is easier because the loop was eliminated). To find compliance checks systematically, we construct formula (2), which relates a prior state of a CPS to its posterior state through at least one path through the model α. Consecutive states for α* mean before and after executions of α (i.e., α;↓α;↓α, not within α).

YV−→(α)YV+  (2)

Formula (2) is satisfied in a state v, if there is at least one run of the model α starting in the state v recalled by YV− and which results in a state w recalled using YV+. In other words, at least one path through α explains how the prior state v got transformed into the posterior state w. The dL formula (2) characterizes the state transition relation of the model α directly. Its violation witnesses compliance violation. Compliance at all intermediate states cannot be observed by real-world sensors. (See Section ‘Monitoring Compliance Guarantees for Unobservable Intermediate States’ herein).

In principle, formula (2) would be a monitor, because it relates a prior state to a posterior state through the model of a CPS, but the formula is difficult, if not impossible, to evaluate at runtime, because it refers to a hybrid system α, which includes non-determinism and differential equations. The basic observation is that any formula that is equivalent to (2) but conceptually easier to evaluate in a state would be a correct monitor 112. We use theorem proving for simplifying formula (2) into quantifier-free first-order real arithmetic form so that it can be evaluated efficiently at runtime. The resulting first-order real arithmetic formula can be easily implemented in a runtime monitor and executed along with the actual controller. A monitor 112 is executable code that only returns true if the transition from the prior system state to the posterior state is compliant with the model 100. Thus, deviations from the model 100 can be detected at runtime, so that appropriate fallback and mitigation strategies can be initiated.

Remark 1. The complexity for evaluating an arithmetic formula over the reals for concrete numbers is linear in the formula size, as opposed to deciding the validity of such formulas, which is doubly exponential. Evaluating the same formula on floating point numbers is inexpensive, but may yield wrong results due to rounding errors; on exact rationals, the bit-complexity can be non-negligible. Interval arithmetic is used to obtain reliable results efficiently.

### Example 1

A simple water tank is used as a running example to illustrate the concepts throughout this section. The water tank has a current level x and a maximum level m. The water tank controller, which runs at least every ε time units, non-deterministically chooses any flow f between a maximum outflow −1 and a maximum

\(\frac{m - x}{ɛ}.\)

This water tank never overflows, as witnessed by a proof for the following dL formula.

\(\left. \underset{\begin{matrix}
 \\
\varphi
\end{matrix}}{0 \leq x \leq {m\bigwedge ɛ} > 0}\rightarrow{\left\lbrack \left( {{f\mspace{14mu} \text{:=}\mspace{14mu}*};{?\left( {{- 1} \leq f \leq \frac{m - x}{ɛ}} \right)};{t\mspace{20mu} \text{:=}\mspace{14mu} 0};\left( {{x^{\prime} = f},{t^{\prime} = {{{1\&}x} \geq {0\bigwedge t} \leq ɛ}}} \right)} \right)^{*} \right\rbrack \overset{\underset{}{\varphi}}{\left( {0 \leq x \leq m} \right)}} \right.\)

### ModelPlex Monitor Synthesis

This section introduces the nature of ModelPlex monitor specifications, the approach in this invention for generating such specifications from hybrid system models, and how to turn those specifications into monitor code that can be executed at runtime along with the controller.

A ModelPlex specification 104 corresponds to the  formula (2). If the current state of a system does not satisfy a ModelPlex specification 104, some behavior that is not reflected in the model 100 occurred (e.g., the wrong control action was taken, unanticipated dynamics in the environment occurred, sensor uncertainty led to unexpected values, or the system was applied outside the specified operating environment).

A model monitor Xm checks that two consecutive states  and  can be explained by an execution of the model α, i.e., (, ) ∈ρ(α). In the sequel, BV(α) are bound variables in α, FV (φ) are free variables in φ, Σ is the set of all variables, and A\B denotes the set of variables being in some set A but not in some other set B. Furthermore, we use v|A to denote v projected onto the variables in A.

Theorem 1 (Model monitor correctness). Let α* be provably safe, so Φ→[α*]ψ. Let Vm= BV (α) ∪ FV (ψ). Let v0, v1, v2, v3 . . . ∈n be a sequence of states, with v0  Φ and that agree on Σ\Vm, i.e., v0|Σ\v=vk|Σ\Vfor all k. We define (v, vi+1) xm as xm evaluated in the state resulting from v by interpreting x+ as vi+1(x) for all x ∈Vm, i.e., vxvxm. If vi, vi+1)xm for all i<n then we have vnψ where

Xm≡(Φ|const→αYv+)  (3)

and Φ|const denotes the conditions of Φ that involve only constants that do not change in α, i. e., FV (φ|const) ∩ BV (α)=ø.

The approach shown herein to generate monitor specifications from hybrid system models 102 takes a verified  formula (1) as input 100 and produces a monitor xm in quantifier-free first-order form as output. The algorithm involves the following steps:


- - 1. A
    formula (1) about a model α of the form Φ→\[α\*\]ψ is turned into a
    specification conjecture (3) of the form Φ\|_(const)→
    α
    Y_(vm)⁺. See process **102**, resulting in monitor specification
    **104** in FIG. 3.
  - 2.Theorem proving on the specification conjecture (3) is applied
    until no further proof rules are applicable and only first-order
    real arithmetic formulas remain open. See process **106**, resulting
    in monitor conditions **108**, containing only first-order logic
    (FOL) in FIG. 3. Process **106** is also shown in more detail in
    FIG. 4, and an algorithmic representation of process **106** is
    shown in Section D herein.
  - 3. The monitor specification x_(m) is the conjunction of the
    unprovable first-order real arithmetic formulas from open sub-goals.

Generate the monitor conjecture.  formula (1) is mapped syntactically to a specification conjecture of the form (3). By design, this conjecture will not be provable. But the unprovable branches of a proof attempt will reveal information that, had it been in the premises, would make (3) provable. Through Yv+, those unprovable conditions collect the relations of the posterior state of model α characterized by x+ to the prior state x, i.e., the conditions are a representation of (2) in quantifier-free first-order real arithmetic.

### Example 2

The specification conjecture for the water tank model is given below. It is constructed from the model by removing the loop, flipping the modality, and formulating the specification requirement as a property, since we are interested in a relation between two consecutive states v and w (recalled by x+, f+ and t+). Using theorem proving, we analyze the conjecture to reveal the actual monitor specification 104.

\(\left. \underset{\begin{matrix}
 \\
{\varphi \; {lowest}}
\end{matrix}}{ɛ > 0}\rightarrow{{\langle{{f\mspace{14mu} \text{:=}\mspace{14mu}*};{?\left( {{- 1} \leq f \leq \frac{m - x}{ɛ}} \right)};{t\mspace{14mu} \text{:=}\mspace{14mu} 0};\left( {{x^{\prime} = f},{t^{\prime} = {{{1\&}x} \geq {0\bigwedge t} \leq ɛ}}} \right)}\rangle}\overset{\underset{}{\mathrm{\Upsilon}_{V_{m}}^{+}}}{\left( {x = {{x^{*}\bigwedge f} = {{f^{*}\bigwedge t} = t^{*}}}} \right)}} \right.\)

Use theorem proving to analyze the specification conjecture. The proof rules of dL are used to analyze the specification conjecture xm. These proof rules syntactically decompose a hybrid model 100 into easier-to-handle parts, which leads to sequents with first-order real arithmetic formulas towards the leaves of a proof. Using real arithmetic quantifier elimination we close sequents with logical tautologies, which do not need to be checked at runtime since they always evaluate to true for any input. The conjunction of the remaining open sequents is the monitor specification 104, which implies (2).

A complete sequence of proof rules applied to the monitor conjecture of the water tank is described in below in Section B. Most steps are simple when analyzing specification conjectures: sequential composition (;), nondeterministic choice (∪), deterministic assignment (:=) and logical connectives (r etc.) replace current facts with simpler ones or branch the proof. Challenges arise from handling nondeterministic assignment and differential equations in hybrid programs.

First, consider nondeterministic assignment x :=*. The proof rule for non-deterministic assignment (*) results in a new existentially quantified variable. By sequent proof rule ∃r, this existentially quantified variable is instantiated with an arbitrary term θ, which is often a new logical variable that is implicitly existentially quantified. Weakening (Wr) removes facts that are no longer necessary.

\(\left( {\langle*\rangle} \right)\frac{\exists{X{\langle{x\mspace{14mu} \text{:=}\mspace{14mu} X}\rangle}\varphi_{1}}}{{\langle{x\mspace{14mu} \text{:=}\mspace{14mu}*}\rangle}\varphi}\mspace{14mu} \left( {\exists r} \right)\frac{{\Gamma \vdash {\varphi (\theta)}},{\exists{x\; {\varphi (x)}}},\Delta_{2}}{{\Gamma \vdash {\exists{x\; {\varphi (x)}}}},\Delta}({Wr})\frac{\Gamma \vdash \Delta}{{\Gamma \vdash \varphi},\Delta}\)

1 X is a new logical variable

2 θ is an arbitrary term, often a new (existential) logical variable X.

Optimization 1 (Instantiation Trigger). If the variable is not changed in the remaining α, xi=xi+ is YV+ and X is not bound in YV+, then instantiate the existential quantifier by rule ∃r with the corresponding xi+ that is part of the specification conjecture (i.e., θ=xi+), since subsequent proof steps are going to reveal θ=xi+ anyway.

Otherwise, a new logical variable is introduced which may result in an existential quantifier in the monitor specification if no further constraints can be found later in the proof.

### Example 3

The corresponding steps in the water tank proof use * for the nondeterministic flow assignment (f:=*) and ∃r to instantiate the resulting existential quantifier ∃F with a new logical variable F (plant is an abbreviation for x′=f, t′=1&0≦xt≦ε). The proof without and with application of Opt. 1 is given as.

Next, differential equations are handled. Even when the differential equation can be solved, existentially and universally quantified variables remain. Inspect the corresponding proof rule from the dL calculus. For differential equations it must be proven that there exists a duration t, such that the differential equation stays within the evolution domain H throughout all intermediate times {tilde over (t)} and the result satisfies φ at the end. At this point there are three options:

i. Option 1: instantiate the existential quantifier, if it is known that the duration will be t+;

ii. Option 2: introduce a new logical variable, which is the generic case that always yields correct results, but may discover monitor specifications that are harder to evaluate;

\(\left( {\langle^{\prime}\rangle} \right)\frac{\exists{T \geq {0\left( {{\left( {\forall{0 \leq \overset{\_}{t} \leq {T\mspace{14mu} {\langle{x\mspace{14mu} \text{:=}\mspace{14mu} {y\left( \overset{\_}{t} \right)}}\rangle}H}}} \right)\bigwedge{\langle{x\mspace{14mu} \text{:=}\mspace{14mu} {y(T)}}\rangle}}\varphi} \right)_{1}}}}{{\langle{x^{\prime} = {{\theta\&}\mspace{14mu} H}}\rangle}\varphi}({QE})\frac{{{QE}(\varphi)}_{2}}{\varphi}\)

1 T and {tilde over (t)} are fresh logical variables and x :=y(T) is the discrete assignment belonging to the solution y of the differential equation with constant symbol x as symbolic initial value

2 iff Φ≡QE (Φ), Φ is a first-order real arithmetic formula, QE(Φ) is an equivalent quantifier-free formula computable by [7]

iii. Option 3: use quantifier elimination (QE) to obtain an equivalent quantifier-free result (a possible optimization could inspect the size of the resulting formula).

### Example 4

In the analysis of the water tank example, the differential equation are solved (see ′ and the substitutions f :=F and t :=0 are applied. In the next step (see ∃r,Wr), the existential quantifier ∃T is instantiated with t+ (i.e., T=t+ using Option 1 with the last conjunct) and uses weakening right (Wr) to systematically get rid of the existential quantifier that would otherwise still be left around by rule ∃r. Finally, quantifier elimination (QE) is used to reveal an equivalent quantifier-free formula, shown as reference number 108 in FIG. 3.

The analysis of the specification conjecture finishes with collecting the open sequents from the proof to create the monitor specification xmdef (open sequent) 104. The collected open sequents may include new logical variables and new (Skolem) function symbols that were introduced for nondeterministic assignments and differential equations when handling existential or universal quantifiers. The invertible quantifier rule i∃ is used to re-introduce existential quantifiers for the new logical variables. Often, the now quantified logical variables are discovered to be equal to one of the post-state variables later in the proof, because those variables did not change in the model after the assignment. If this is the case, proof rule ∃σ can be used to further simplify the monitor specification by substituting the corresponding logical variable x with its equal term θ.

\(\left( {i\exists} \right)\frac{{\Gamma \vdash {\exists{\vdash {{\langle\rangle}{X\left( {\Lambda_{i}\left( {\Phi_{i} \vdash \psi_{i}} \right)} \right)}}}}},\Delta_{1}}{\Gamma,{\Phi_{1} \vdash \psi_{2}},{\Delta\cdots\Gamma},{\Phi_{1} \vdash \psi_{2}},\Delta}\left( {\exists o} \right)\frac{{\varphi (\theta)}_{2}}{\exists{x\left( {x = {\theta\bigwedge{\varphi (x)}}} \right)}}\)

1 Among all open branches, free logical variable X only occurs in the branches Γ, Φ, , ψ, Δ

2 Logical variable x does not appear in term θ

### Example 5

The two open sequents of Examples 3 and 4 use a new logical variable F for the nondeterministic flow assignment f := *. After further steps in the proof, the assumptions reveal additional information F=f+. Thus, the existential quantifier is re-introduced over all the open branches (i∃) and substitute f+ for F (∃σ). The sole open sequent of this proof attempt is the monitor specification xm of the water tank model.

**Controller Monitor Synthesis**

A controller monitor xc, shown as reference number 112 in FIG. 3, checks that two consecutive states v and w are reachable with one controller execution αctrl, i. e., (v,w) ∈ ρ(αctrl) with Vc, =BV (αctrl) ∪ FV (ψ). Controller monitors 112 are systematically derived in processes 106 and 110 from formulas 104: φ|const→αctrlYV+. A controller monitor 112 can be used to initiate controller switching similar to Simplex.

Theorem 2 (Controller monitor correctness). Let α of the canonical form αctrl; αplant Assume |=Φ→[α*]φ has been proven with invariant φ as in (1). Let v Φ|const̂Φ, as checked by xm(Theorem 1). Furthermore, let {tilde over (v)} be a post-controller state. If (v, {tilde over (v)})  xc with xc ≡Φ|const→αctrlYV+ then we have that (v, {tilde over (v)}) ∈ρ(αctrl) and {tilde over (v)}|=φ.

**Monitoring in the Presence of Expected Uncertainty and Disturbance**

Up to now exact ideal-world models have been considered. However, real-world clocks drift, sensors measure with some uncertainty, and actuators are subject to disturbance. This makes the exact models safe but too conservative, which means that monitors for exact models are likely to fall back to a fail-safe controller unnecessarily often. This section is a discussion of how ModelPlex specifications are found such that the safety property (1) and the monitor specification become more robust to expected uncertainty and disturbance. That way, only unexpected deviations beyond those captured in the normal operational uncertainty and disturbance of a* cause the monitor to initiate fail-safe actions.

In dL we can, for example, use nondeterministic assignment from an interval to model sensor uncertainty and piecewise constant actuator disturbance, or differential inequalities for actuator disturbance. Such models include non-determinism about sensed values in the controller model and often need more complex physics models than differential equations with polynomial solutions.

**Example 6**

Clock drift, sensor uncertainty and actuator disturbance are incorporated into the water tank model to express expected deviation. The measured level x, is within a known sensor uncertainty u of the real level x (i.e. x ∈[x−u, x+ u]). Differential inequalities are used to model clock drift and actuator disturbance. The clock, which wakes the controller, is slower than the real time by at most a time drift of c; it can be arbitrarily fast. The water flow disturbance is at most d, but the water tank is allowed to drain arbitrarily fast (even leaks when the pump is on). To illustrate different modeling possibilities, we use additive clock drift and multiplicative actuator disturbance.

\(\left. {0 \leq x \leq {m\bigwedge ɛ} > {0\bigwedge c} < {1\bigwedge 0} \leq {u\bigwedge 0} < d}\rightarrow{\quad{\left\lbrack \left( {{x_{s}\mspace{14mu} \text{:=}\mspace{14mu}*};{?\left( {{x - u} \leq x_{s} \leq {x + u}} \right)};{f\mspace{14mu} \text{:=}\mspace{14mu}*};{?\left( {{- 1} \leq f \leq {\frac{m - x_{s} - u}{ɛ}\left( {1 - c} \right)}} \right)};{t\mspace{14mu} \text{:=}\mspace{14mu} 0};\left\{ {{x^{\prime} \leq {fd}},{{1 - c} \leq {t^{\prime}x} \geq {0\bigwedge t} \leq ɛ}} \right\}} \right)^{*} \right\rbrack \left( {0 \leq x \leq m} \right)}} \right.\)

Example6 can be analyzed in the same way as the previous examples, with the crucial exception of the differential inequalities. The proof rule (′) cannot be used to analyze this model, because differential inequalities do not have polynomial solutions. Instead, the DR and DE proof rules of  are used to turn differential inequalities into a differential- algebraic constraint form that lets us proceed with the proof. Rule DE turns a differential inequality x′≦θ into a quantified differential equation ∃{tilde over (d)}(x′={tilde over (d)}&{tilde over (d)}≦θ) with an equivalent differential-algebraic constraint. Rule DR turns a differential-algebraic constraint E into another differential-algebraic constraint , which implies , written →.

\(({DR})\frac{\left. \rightarrow{{\delta ()}\varphi_{1}} \right.}{(\delta)\varphi}({DE})\frac{\forall{{X\left( {\exists\left. {\overset{\_}{d}\left( {X = {{\overset{\_}{d}\bigwedge\overset{\_}{d}} \leq {\theta\bigwedge H}}} \right)}\rightarrow{X \leq {\theta\bigwedge H}} \right.} \right)}\left( {\exists{\overset{\_}{d}\left( {x^{\prime} = {{{\overset{\_}{d}\&}\mspace{14mu} \overset{\_}{d}} \leq {\theta\bigwedge H}}} \right)}} \right)\varphi_{2}}}{\left( {{{x^{\prime} \leq \theta}\&}\mspace{14mu} H} \right)\varphi}\)

1 differential refinement: differential-algebraic constraints ,  have the same changed variables

2 differential inequality elimination: special case of DR, which rephrases the differential inequalities ≦as differential-algebraic constraints (accordingly for other or mixed inequalities systems).

Currently, for finding model monitors, our prototype tool solves differential equations by the proof rule (′). Thus, it finds model monitor specifications for differential algebraic equations with polynomial solutions and for differential algebraic inequalities, which can be refined into solvable differential algebraic equations as in Example 6. For prediction monitors (discussed in Section below)  techniques are used for finding differential variants and invariants, differential cuts, and differential auxiliaries to handle differential equations and inequalities without polynomial solutions.

**Monitoring Compliance Guarantees for Unobservable Intermediate States**

With controller monitors, non-compliance of a controller implementation with respect to the modeled controller can be detected right away. With model monitors, non-compliance of the actual system dynamics with respect to the modeled dynamics can be detected when they first occur. In such cases, a fail-safe action is switched to, which is verified using standard techniques, in both non-compliance cases. The crucial question is: can such a method always guarantee safety? The answer is linked to the image computation problem in model checking (i. e., approximation of states reachable from a current state), which is known to be not semi-decidable by numerical evaluation at points; approximation with uniform error is only possible if a bound is known for the continuous derivatives. This implies that additional assumptions are needed about the deviation between the actual and the modeled continuous dynamics to guarantee compliance for unobservable intermediate states. Unbounded deviation from the model between sample points just is unsafe, no matter how hard a controller tries. Hence, worst-case bounds capture how well reality is reflected in the model.

A prediction monitor is derived to check whether a current control decision will be able to keep the system safe for time s even if the actual continuous dynamics deviate from the model. A prediction monitor checks the current state, because all previous states are ensured by a model monitor and subsequent states are then safe by (1).

Definition 2 (ε-bounded plant with disturbance δ). Let αplant be a model of the form x′=θ& H. An ε-bounded plant with disturbance δ, written αδplant, is a plant model of the form xo :=0; (f(θ, δ) ≦x′≦g(θ, δ) & H xo≦ε) for some f, g with fresh variable ε>0 and assuming xo′=1. That disturbance δ is constant if x ∈δ; it is additive if f(θ, δ)=θ−δ and g(θ, δ) =θ+δ.

Theorem 3 (Prediction monitor correctness). Let α* be provably safe, i. e., Φ→[α*]ψ has been proved using invariant φ as in (1). Let Vp=BV (α) ∪ FV ([α]φ]). Let vΦ|constφ, as checked by Xm from Theorem 1. Further assume {tilde over (v)} such that (v, {tilde over (v)}) ∈ρ(αctrl), as checked by Xc from Theorem 2. If (v, {tilde over (v)}) Xp with Xp≡(Φ|constφ)→αctrl(YV+[αδplant]φ), then we have for all ({tilde over (v)}, ω) ∈ρ(αδplant) that ω|=φ.

Remark 2. By adding a controller execution αctrl prior to the disturbed plant model, we synthesize prediction monitors that take the actual controller decisions into account. For safety purposes, a monitor definition without controller Xp≡(Φ|constφ)→[αδplant]φ could be used, but doing so results in a conservative monitor, which has to keep the CPS safe without knowledge of the actual controller decision.

**Decidability and Computability**

One useful characteristic of ModelPlex beyond soundness is that monitor synthesis is computable, which yields a synthesis algorithm, and that the correctness of those synthesized monitors with respect to their specification is decidable. See Theorem 4.

Theorem 4 (Monitor correctness is decidable and monitor synthesis computable). Assume canonical models of the form α≡□αctrl; αplant without nested loops, with solvable differential equations in αplant and disturbed plants αδplant with constant additive disturbance δ (see Definition. 2). Then, monitor correctness is decidable, i. e., the formulas Xm→αYV+, Xc→αctrlYV+ γV+, and Xp→αctrl(YV+[αδplant]φ) are decidable. Also, monitor synthesis is computable, i. e., the functions synthm: α>YV+→Xm. synthc: <αctrl>YV+→Xc and synthp: <αctrl>(YV+[αδplant]φ)→Xp are computable.

**Evaluation**

A software prototype was developed and integrated into the modeling tool Sphinx to automate many of the described steps. The prototype generates Xm, Xc, and Xp conjectures from hybrid programs, collects open sequents, and interacts with KeYmaera.

To evaluate the method, we created monitors for prior case studies of non-deterministic hybrid models of autonomous cars, train control systems, and robots, for example, adaptive cruise control, intelligent speed adaptation, the European train control system, and ground robot collision avoidance. Table 2 summarizes the evaluation. For the model, the dimension in terms of the number of function symbols and state variables is listed, as is the size of the safety proof (i. e., number of proof steps and branches).

For the monitor, the dimension of the monitor conjecture is listed in terms of the number of variables. The number of steps and open sequents are compared when deriving the monitor using manual proof steps to apply Option 1 and fully automated w/o Option 1, and the number of steps in the monitor correctness proof. Finally, the monitor size in terms of arithmetic, comparison, and logical operators in the monitor formula is listed.

Although the number of steps and open sequents differ significantly between manual interaction for Option 1 and fully automated synthesis, the synthesized monitors are logically equivalent. But applying Option 1 usually results in structurally simpler monitors, because the conjunction over a smaller number of open sequents (See Table 2) can still be simplified automatically. The model monitors for cruise control and speed limit control are significantly larger than the other monitors, because their size already prevents automated simplification by Mathematica. As future work, KeYmaera will be adapted to allow user-defined tactics to apply Option 1 automatically.

## A. Proofs

### A.1 Formal Semantics of

ModelPlex bases on a reachability relation semantics instead of trace semantics, since it is easier to handle and suffices for checking at sample points.

The semantics of , as defined in [27], is a Kripke semantics in which states of the Kripke model are states of the hybrid system. Let  denote the set of real numbers. A state is a map v:V→; the set of all states is denoted by Sta. We write v|=Φ if formula Φ is true at state v (Def. 4). Likewise, θ, denotes the real value of term θ at state v. The semantics of HP α is captured by the state transitions that are possible by running α. For continuous evolutions, the transition relation holds for pairs of states that can be interconnected by a continuous flow respecting the differential equation and invariant region. That is, there is a continuous transition along xI=θ & H from state v to state w, if there is a solution of the differential equation xI=θ that starts in state v and ends in w and that always remains within the region H during its evolution.

Definition 3 (Transition semantics of hybrid programs). The transition relation ρ specifies which state w is reachable from a state v by operations of α. It is defined as follows.


- - 1. (ν,ω)∈ρ(x:=θ) iff
    z
    _(ν)=
    z
    _(ω)f·a·z≠x and
    x
    _(ω)=
    θ
    _(ν).
  - 2. (ν,ω)∈ρ(x:=\*) iff
    z
    _(ν)=
    z
    _(ω)f·a·z≠x.
  - 3. (ν,ω)∈ρ(?φ) iff ν=ω and ν
    φ.
  - 4. (ν,ω)∈ρ(x′₁=θ₁, . . . ,x′_(n)=θ_(n)&H) iff for some r≦0, there is
    a (flow) function φ:\[0,r\]→Sta with φ(0)=ν,φ(r)=ω, such that for
    each time ζ∈\[0, r\]:
    - (i) The differential equation holds, i.e.,

\({\frac{\lbrack x\rbrack_{w}}{t}(\zeta)} = \left. ||\theta_{i} \right.||_{\psi {(\zeta)}}\)


- - - for each x_(i),. (ii) For other variables y∉{x₁, . . . ,x_(n), }
      the value remains constant, i.e.,
      y
      _(φ(ζ))=
      y
      _(φ(0)).
    - (iii) The invariant is always respected, i.e., φ(ζ)
      H.

  - 5. ρ(α∪β)=ρ(α)∪ρ(β)

  - 6. ρ(α;β)={(ν,ω):(ν,z)∈ρ(α),(z,ω)∈ρ(β) for a state z}

  - 7. ρ(α\*)=∪_(n∈N)ρ(α^(n)) where α^(i+1){circumflex over
    (=)}(α;α^(i))and α⁰ {circumflex over (=)}?true.

Definition 4 (Interpretation of dL formulas). The interpretation  of a dL formula with respect to state v is defined as follows.

1. vθ1˜θ2iff[θ1]˜[θ2for ˜∈]{=≦, <, ≧, >}

2. vφΛΦiff v Φ and v ψ, accordingly for —, V,→⇄

3. v∀x φ iff wΦ for all w that agree with v except for the value of x

4. v|=∃xΦiff wΦ for some w that agrees with v except for the value of x

5. v[α]Φ iff wΦ∀w with (v, w) ∈ρ(α)

6. v[α]Φ iff w∃w with (v, w)∈ρ(α)

We write |= Φ to denote that Φ is valid, i.e., that v |=Φ∀v.

### A.2 Soundness

We recall Lemma 1.

Lemma 1 (Loop prior and posterior state). Let α be a hybrid program and α* be the program that repeats α arbitrarily many times. Assume that all consecutive pairs of states (vi−1, Vi) ∈ρ(α) of n ∈+ executions, whose valuations are recalled with YVi≡x∈Vx=xi and YVi−1 are plausible w.r.t. the model α, i.e., |=1≦i≦n(YVi−1→αYVi) with YV−=YV0 and YV+=YVn. Then, the sequence of states originates from an α* execution from YV0 to YVn, i.e., |=YV−→α*YV+.

Proof. Follows directly from the transition semantics of α*: ρ(α*) =where αi+1≅(α; αi) and α0 ≅? true.

We recall Theorem 1.

Theorem 1 (Model monitor correctness). Let α* be provably safe, so |=Φ→[α*]ψ. Let Vm=BV (α) ∪ FV (ψ). Let v0, v1, v2, v3 . . . ∈n be a sequence of states, with v0Φ and that agree on Σ/Vm, i.e., 0|Σ/V=k|Σ/Vfor all k. We define (, i+1) xm as xm evaluated in the state resulting from v by interpreting x+ as i+1(x) for all x ∈ Vm, i.e., xvxm. If i, i+1) xm for all i < n then we have n  where

Xm≡(Φ|const→αYV+)  (3)

and Φ|const denotes the conditions of Φ that involve only constants that do not change in α, i.e., FV (Φ|const) ∩BV(α)=ø.

Proof. By induction over n. If n=0 then (0, 0) ∈ρ(α*)trivially by definition of ρ and Φ→[α*]ψ implies 0 ψ. For n>0 assume (0, n) |ρ(α*) and (n, n+1)  (α) Λx∈Vx=x+. Then there exists μ such that (vn+v, μ) ∈ρ(α) and the two states agree on all variables except the ones modified by α, i.e., vn+v|Σ/BV(α=μ|Σ/BB(α). Thus, μ YV+, i.e. μx∈Vx=x+, which in turn yields μ(x)=μ(x+)=(vn+v(x+)=vn+1(x) (in other words, μ|Vm=vn+1|Vm). Since also vn|Σ/Vwe get μ=n+1 and (n, n+1) ∈ρ(α). Hence (0, n+1) ∈ρ(α*) because by induction hypothesis (0, n) ∈ρ(α*) and we conclude n+1ψ by assumption Φ→[α]ψ using 0Φ.

We recall Theorem 2.

Theorem 2 (Controller monitor correctness). Let α of the canonical form αctrl; αplant. Assume Φ→[α*]ψ has been proven with invariant φ as in (1). Let Φ|constψ, as checked by xm (Theorem 1). Furthermore, let  be a post-controller state. If (v,) Xc with Xc≡Φ|const→αctrlYV+ = then we have that (v,) ∈ρ(αctrl) and φ.

Proof. Consider a state Φ|constφ. Assume (v, ) Xc, i.e., Xc. Then there exists μ such that , μ) ∈ρ(αctrl) and the two states agree on all variables except the ones modified by αctrl, i.e., |Σ/BV(αctrl))=μ|Σ/BV(αctrl). Thus YV+, i.e., μ|=xeVx=x+, which in turn yields μ(x)=μ(x+)=(x+)=(x) (in other words, μ|Vc=Vc). Since also μ|Σ.V=Σ/Vwe get μ= and (v,) ∈ρ(αctrl). Then we have  φ because by assumption φ→[αctrl;αplant]φ ρ(αplant) is reflexive as ODE can evolve for time 0.

We recall Theorem 3.

Theorem 3 (Prediction monitor correctness). Let α* be provably safe, i.e., Φ→[α*]ψ has been proved using invariant φ as in (1.) Let Vp=BV(α) ∪FV([α]φ). Let Φ|const φ, as checked by Xm from Theorem 1. Further assume  such that (, ) ∈ρ(αctrl), as checked by Xc from Theorem 2. If (, ) Xp with Xp≡(Φ|constφ) →αctrlYV+[αδplant]φ), then we have for all (,w) ∈ρ(αδplant) that w φ.

Proof. Consider a state  such that Φ|xonstφ. Let  be some state such that (,) ∈ρ(αctrl). Then we have φ because by assumption φ→[αctrl; αplant]φ and ρ(αδplant) is reflexive as ODE can evolve for time 0. Furthermore Φ|const since |Σ/BV(αctrl)=|Σ/BV(αctrl) and FV(Φ|const) ∩BV(αctrl) =ø. Assume (,) Xp, i.e., Xp. Then there exists μ such that μYV+[αδplant]φ with (, μ) ∈ρ(αctrl) and the two states agree on all variables except the ones modified by αctrl, i.e., |Σ/BV(αctrl)=μ|Σ/BV(αctrl). Thus μ(x)=μ(x+)=(x+)=(x). (in other words, μ|Vp=|Vp). However, from Xp we know that μ[αδplant]φ. Thus, by the coincidence lemma, [αδplant]φ since FV ([αδplant]φ)  Vp and hence we have w  φ for all (,w) ∈ρ(αδplant).

Observe that this is also true for all intermediate times ç∈[0,w(t)] by the transition semantics of differential equations, where w(t)≦∈ because αδplant is bounded by ∈.

### A.3 Decidability and Computability

From Lemma 1 it follows that online monitoring (i.e., monitoring the last two consecutive states) is permissible. So, ModelPlex turns questions [α*]Φ and a*Φ into [α]Φ and αΦ, respectively. For decidability, we first consider canonical hybrid programs α of the form α≡αctrl; αplant where αctrl and αplant are free of further nested loops.

We split Theorem 4 (decidability and computability) into Theorem 5 (decidability) and Theorem 6 (computability) and prove them separately. To handle differential inequalities in dL formulas of the form [αδplant]Φ, the subsequent proofs additionally assume the rules for handling differential-algebraic equations in the dL calculus.

Theorem 5 (Monitor correctness is decidable). Monitor correctness is decidable for canonical models of the form α≡αctrl; αplant without nested loops, with solvable differential equations in αplant and disturbed plans αδplant with constant additive disturbance δ i.e., Xm→αYV+,Xc→αctrlYV+, and Xp→αYV+[αδplant]Φ) are decidable.

Proof. From relative decidability of  (i.e.,  formulas without free variables) are decidable relative to an oracle for discrete loop invariants/variants and continuous differential invariants/variants. Since neither αctrl nor αplant contain nested loops, we manage without an oracle for loop invariants/variants. Further, since the differential equation systems in αplant are solvable, we have an effective oracle for differential invariants/variants. Let Cl∀(Φ) denote the universal closure of  formula Φ (i.e., Cl∀(Φ)≡∀z∈FV(Φ)z. Φ). Note that when F then also Cl∀(F) by a standard argument.

Model monitor Xm→αYV+: Follows from relative decidability of , because Cl∀(XmαYV+) contains no free variables.

Controller monitor Xc→αctrlYV+: Follows from relative decidability of , because Cl∀(Xc→αctrlYV+) contains no free variables.

Prediction monitor Xpαctrl(YV+[αδplant]Φ):-Decidability for αctrl follows from case Xc→αctrlYV+ (controller monitor) above. It remains to show decidability of Xp→αctrl[αδplant]Φ, which by decidability of the controller monitor is (XpYV+)→[αplant]Φ. Since the disturbance δ in αδplant is constant additive and the differential equations in αplant are solvable, we have the disturbance functions f(θ,δ) and g(θ,δ) applied to the solution as an oracle (By design, the disturbed plant αδplant also includes a clock x0, so the oracle additionally includes the trivial differential invariant x0≧0) for differential invariants (i. e., the differential invariant is a pipe around the solution without disturbance). Specifically, to show (XpYV+)→[αδplant]Φ by Def. 2 we have to show (XpΛYV+)→[x0:=0; {θ−δ≦x′≦θ+δ&H Λx0 ≦ε}]Φ We proceed with only (XpΛYV+) →[x0:=0{x′≦θ+δ&H Λx0≦ε}]Φ p since the case θ−δ≦x′ follows in a similar manner. By definition of αδplant we know 0≦x0, and hence continue with (XpΛYV+)→[{x′≦θ+δ&HΛ0≦x0≦ε}]Φ by differential cut 0≦x0. Using the differential cut rule, we further supply the oracle solx+δx0, where solx denotes the solution of x′=θ in αplant and δx0 the solution for the disturbance since δ is constant additive. This leads to two proof obligations:

Prove oracle (XpΛYV+)→[x′≦θ+δ&0≦x0≦ε]x≦solx+δx0, which by rule differential invariant is valid if we can show 0≦x0≦ε→x′≦sol′x+(δx0)′ where the primed variables are replaced with the respective right-hand side of the differential equation system. From Def. 2 we know that x′0=1 and δ′=0 and since solx is the solution of x′=θ in αplant we further know that sol′x=θ; hence we have to show 0≦x0≦ε→θ+δ≦θ+δ, which is trivially true.

Use oracle (XpΛYV+)→[x′≦θ+δ&HΛ0≦x0≦εΛx≦solx+δx0]φ, which by rule differential weaken is valid if we can show

(XpΛYV+)→∀α((HΛ0≦x0≦εΛx≦solx+δx0)→Φ)

where ∀α denotes the universal closure w.r.t. x, i. e., ∀x. But, if Xp is a correct monitor, this is provable by quantifier elimination. Furthermore, we cannot get a better result than differential weaken, because the evolution domain constraint contains the oracle's answer for the differential equation system, which characterizes exactly the reachable set of the differential equation system.

We conclude that the oracle is proven correct and its usage is decidable.

For computability, we start with a theoretical proof on the basis of decidability, before we give a constructive proof, which is more useful in practice.

Theorem 6 (Monitor synthesis is computable). Synthesis of Xm, Xc, and Xp monitors is computable for canonical models of the form α≡αctrl; αplant without nested loops, with solvable differential equations in αplant and plants αδplant with constant additive disturbance δ, i. e., synthm: αYV+→Xm, synthc: αctrlYV+→Xc, and synthp: α(YV+[αplant]Φ)→Xp are computable.

Proof. Follows immediately from Theorem 5 with recursive enumeration of monitors.

We give a constructive proof of Theorem 6. The proof is based on the observation that, except for loop and differential invariants/variants, rule application in the  calculus is deterministic: we know that, relative to an oracle for first-order invariants and variants, the  calculus gives a semidecision-procedure for  formulas with differential equations having first-order definable flows.

Proof. For the sake of a contradiction, suppose that monitor synthesis stopped with some open sequent not being a first-order quantifier-free formula. Then, the open sequent either contains a hybrid program with nondeterministic repetition or a differential equation at top level, or it is not quantifier-free. But this contradicts our assumption that both αctrl and αplant are free from loops and that the differential equations are solvable and disturbance is constant, in which case for

Model monitor synthesis Xm: the solution rule ′ would make progress, because the differential equations in αplant are solvable; and for

Prediction monitor synthesis Xp: the disturbance functions f(θ,δ) and g(θ,δ) applied to the solution provide differential invariants (see proof of Theorem 5) so that the differential cut rule, the differential invariant rule, and the differential weakening rule would make progress.

In the case of the open sequent not being quantifier-free, the quantifier elimination rule QE would be applicable and turn the formula including quantifiers into an equivalent quantifier-free formula. Hence, the open sequent neither contains nondeterministic repetition, nor a differential equation, nor a quantifier. Thus we conclude that the open sequent is a first-order quantifier-free formula.

## B. Water Tank Monitor Specification Conjecture Analysis

Proof 1 shows a complete sequence of proof rules applied to the water tank specification conjecture of Example 2 on page 7, with Φ≡ε>0 and Y+≡x=x+Λf =f+Λt =t+.

\(\left( {\Lambda \; r} \right)\frac{{\Gamma \vdash \varphi},{\Gamma \vdash \psi},\Delta}{{\Gamma \vdash {\varphi\bigwedge\psi}},\Delta}({Wr})\frac{\Gamma \vdash \Delta}{{\Gamma \vdash \varphi},\Delta}({QE})\frac{{{QE}(\varphi)}_{1}}{\varphi}\)
\(\left( {\langle;\rangle} \right)\frac{{\langle\alpha\rangle}{\langle\beta\rangle}\varphi}{{\langle{\alpha;\beta}\rangle}\varphi}\left( {\langle?\rangle} \right)\frac{H\bigwedge\psi}{\langle{?{{H\rangle}\psi}}}\left( {\langle\text{:=}\rangle} \right)\frac{\varphi_{x}^{\theta}}{{\langle{x\mspace{14mu} \text{:=}\mspace{14mu} \theta}\rangle}\varphi}\left( {\langle*\rangle} \right)\frac{\exists{X{\langle{x\mspace{14mu} \text{:=}\mspace{14mu} X}\rangle}\varphi_{2}}}{{\langle{x\mspace{14mu} \text{:=}\mspace{14mu}*}\rangle}\varphi}\)
\(\left( {\langle^{\prime}\rangle} \right)\frac{\exists{t \geq {0\left( {{\left( {\forall{0 \leq \overset{\_}{t} \leq {t{\langle{x\mspace{14mu} \text{:=}\mspace{14mu} {y\left( \overset{\_}{t} \right)}}\rangle}H}}} \right)\bigwedge{\langle{x\mspace{14mu} \text{:=}\mspace{14mu} y*(t)}\rangle}}\varphi} \right)_{3}}}}{{\langle{x^{\prime} = {{\theta\&}\mspace{14mu} H}}\rangle}\varphi}\left( {\exists r} \right)\frac{{\Gamma \vdash {\varphi (\theta)}},{\exists{x\; {\varphi (x)}}},\Delta_{4}}{{\Gamma \vdash {\exists{x\; {\varphi (x)}}}},\Delta}\)
\(\left( {i\exists} \right)\frac{{\Gamma \vdash {\exists{\vdash {{\langle\rangle}{X\left( {\Lambda_{i}\left( {\Phi_{i} \vdash \psi_{i}} \right)} \right)}}}}},\Delta_{5}}{\Gamma,{\Phi_{1} \vdash \psi_{1}},{\Delta\cdots\Gamma},{\Phi_{n} \vdash \psi_{n}},\Delta}\left( {\exists\sigma} \right)\frac{\varphi_{x}^{\theta}}{\exists{x\left( {x = {\theta\bigwedge{\varphi (x)}}} \right)}}\)

1 iff Φ≡QE(Φ), Φ is a first order real arithmetic formula, QE)(Φ) is a quantifier free formula

2 X is a new logical variable p 3 t and {tilde over (t)} are fresh logical variables and x:=y(t) is the discrete assignment belonging to the solution y of the differential equation with constant symbol x as symbolic initial value

4 θ is an arbitrary term, often a new (existential) logistical variable X.

5 Among all open branches, free logical variable X only occurs in the branches Γ, Φ, ├ψ, Δ

Proof 1. Analysis of the water tank monitor specification conjecture (plant is an abbreviation for x′=f, t′=1 & x≧0 t≦ε)

[00116] Proof 1: Analysis of the water tank monitor specification conjecture (plant is an abbreviation for x′=f, t′=1 & x ≧0t≦ ε)

### Example 7

We start at the point where we have to handle the differential inequalities. First, we eliminate the differential inequalities by rephrasing them as differential-algebraic constraints in step (DE). Then, we refine by instantiating the existential quantifiers with the worst-case evolution in step (DR). The resulting differential equation has polynomial solutions and, thus, we can use ′ and proceed with the proof as before.

As expected, we get a more permissive monitor specification. One conjunct of the monitor specification is shown in (Xm1) Such a monitor specification says that there exists a real flow F, a real time T, and a real level Xs, such that the measured flow f+, the clock t+, and the measured level x+ can be explained with the model.

## C. Monitor Synthesis and Fallback Controller Design

### C.1 Design-By-Contract Monitoring

Preconditions, postconditions and invariants are crucial conditions in CPS design. Monitors for these conditions can check (i) whether or not it is safe to start a particular controller (i. e., check that the precondition of a controller is satisfied), (ii) whether or not a controller complies with its specification (i. e., check that a controller delivers set values that satisfy its post condition), and (iii) whether or not the system is still within its safety bounds (i. e., check that the loop invariant of α* is satisfied).

Precondition and post condition monitors are useful to decide whether or not it is safe to invoke a controller in the current state, and whether or not to trust a controller output. An invariant monitor of a CPS α* captures the main assumptions that have to be true throughout system execution. When an invariant monitor is unsatisfied, it may no longer be safe to run the CPS; a fail-safe controller can act as a mitigation strategy.

Design-by-contract monitors are useful to monitor specific design decisions, which are explicitly marked in the model. Our approach systematically creates monitors for a complete specification of the behavior of the model.

### C.2 Monitor Synthesis

Once we found a model monitor, controller monitor, or prediction monitor specification, we want to turn it into an actual monitor implementation (e. g., in C). The main challenge is to reliably transfer the monitor specification, which is evaluated on , into executable code that uses floating point representations. We use the interval arithmetic library Apron to represent each real arithmetic value with an interval of a pair of floating point numbers. The interval reliably contains the real.

For certification purposes one still has to argue for the correctness of the actual machine code of the synthesized monitor. This entails that the transformation from the monitor specification as a first-order formula into actual code that evaluates the formula must be formally verified. If the synthesized code is still a high-level language, a certified compiler, can be used to produce machine code. Such a comprehensive proof chain suitable for certification is part of our ongoing research.

### C.3 Designing for a Fail-Safe Fallback Controller

When we design a system for a fail-safe fallback controller ctrlsafe, it is important to know within which bounds the fail-safe controller can still keep our CPS safe, and which design limits we want a controller implementation to obey. The invariant of a CPS with the fail-safe fallback controller describes the safety bounds. When we start the fail-safe fallback controller ctrlsafe in a state where its invariant G is satisfied, it will guarantee to keep the CPS in a state that satisfies the safety property ψ.

So, to safely operate an experimental controller ctrlexp, we want a monitor that informs us when the experimental controller can no longer guarantee the invariant of the fail-safe controller or when it is about to violate the design limits.

A design for a CPS with a fail-safe fallback controller, therefore, involves proving two properties. First, we prove that the fail-safe controller ctrlsafe ensures the safety property ψ as in formula (4) below. This property is only provable if we discover an invariant G for the CPS with the fail-safe controller. Then we use G as the safety condition for generating a prediction monitor.

ø→[(ctrlsafe;plant)*@inv(G)]ψ

With this generic structure in mind, we can design for a fallback controller invoked by a model monitor Xm, controller monitor Xc, or prediction monitor Xp. Upon violation of either Xm, Xc, or Xp by the actual system execution, the set values of a fail-safe controller are used instead.

### D. Monitor Synthesis Algorithm

Algorithm 1 lists the ModelPlex specification conjecture analysis algorithm 106, which turns a specification conjecture into an actual monitor, and is shown in flow-chart form in FIG. 4. The algorithm takes a hybrid system model α, a set of variables V that we want to monitor, and an initial condition ø including constraints on the variables not changed in α. (Usually, we want a monitor for all the bound variables of the hybrid system model, i.e., V=BV (α).

### E. Simulation

To illustrate the behavior of the water tank model with a fallback controller, we created two monitors: Monitor Xm validates the complete model (as in the examples throughout this work) and is executed at the beginning of each control cycle (before the controller runs). Monitor Xc validates only the controller of the model α (compares prior and post state of f:=*; ?

\(\left. {{- 1} \leq f \leq \frac{m - x}{ɛ}} \right)\)

the controiier but before control actions are issued. Thus, monitor Xc resembles conventional runtime verification approaches, which do not check CPS behavior for compliance with the complete hybrid model. This way, we detect unexpected deviations from the model at the beginning of each control cycle, while we detect unsafe control actions immediately before they are taken. With only monitor Xm in place we would require an additional control cycle to detect unsafe control action, whereas with only monitor Xc in place we would miss deviations from the model. Note that we could run monitor Xm in place of Xc to achieve the same effect. But monitor Xm implements a more complicated formula, which is unnecessary when only the controller output should be validated.

FIG. 2 shows a plot of the variable traces of one simulation run. In the simulation, we ran the pump controller every 2 s (ε=2 s, indicated by the grid for the abscissa and the marks on sensor and actuator plots). The controller was set to pump with

\(\frac{5\left( {m - x_{0}} \right)}{ɛ} = \frac{5}{2}\)

for the first three controller cycles, which is unsafe on the third controller cycle. Monitor B immediately detects this violation at t=4, because on the third controller cycle setting

\(f = \frac{5}{2}\)

violates

\(f \leq {\frac{m - x_{1}}{ɛ}.}\)

The fail-safe action at t=4 drains the tank and, after that, normal operation continues until t=12. Unexpected disturbance

\(x^{\prime} = {f + \frac{1}{20}}\)

occurs throughout t=[12,14], which is detected by monitor Xm. Note, that such a deviation would remain undetected with conventional approaches (monitor Xc is completely unaware of the deviation). In this simulation run, the disturbance is small enough to let the fail-safe action at t=14 keep the water tank in a safe state.

