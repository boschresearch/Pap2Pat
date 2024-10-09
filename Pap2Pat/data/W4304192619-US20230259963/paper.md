# Introduction

Motivation: Causal Bayesian Networks (CBN) ( [Pea09,Spi10]), have become the popular choice to model causal relationships in many real-world systems. These models can simulate the effects of external interventions that forcibly fix target system variables to desired target values. The simulation is done via the do() operator ( [Pea09]) wherein the CBN is altered by breaking incoming edges of the target variables and fixing them to desired target values. Pre-estimating the effect of interventions can help in decision making, for example, interventions on a CBN describing gene interactions can guide gene editing experiments.

However, real-world interventions are not always precise and mistakenly end up intervening other unintended targets. For example, gene knockout experiments via the CRISPR-Cas9 gene-editing technology perform unintended cleavage at unknown genome sites ( [FFK + 13, WWW + 15]). Moreover, the unintended intervention targets can themselves be noisy i.e. different individuals targeted by the same intervention might undergo completely different off-target interventions. For example, [AWL18] demonstrated that same gene editing experiment (using CRISPR-Cas9) on mice embryos exhibited different unintended cleavage for different mice. In such situations, units (samples) that underwent different unintended interventions are not segregated and therefore the generated distribution becomes a mixture of individual interventional distributions. We ask the following natural question. by C X . Unless otherwise specified, all random variables in this paper are discrete and have finite support i.e. |C X | < ∞. A tuple or set of random variables is denoted by capital bold face letter (e.g. X) and the corresponding lower case bold faced letter x will denote the assignment X = x. Let, C X = ∏ X i ∈X C X i denote the set of all possible values that can be taken by X. Probability of X taking the value x is denoted by P(X = x) or equivalently as P(x) and probability of X = x given Y = y is denoted as P(X = x|Y = y) or equivalently with P(x|y). We will use [n] to denote the set {1, 2, ..., n}, [m, n] to denote set {m, m + 1, . . . , n}, calligraphic capital letters e.g. S to denote sets. Size of any set S is denoted by |S|. R, R + and R ≥0 will denote the set of real numbers, positive real numbers and non-negative real numbers respectively.

Bayesian Network Let G = {V, E } be a directed acyclic graph (DAG) with node set V = {V 1 , . . . , V n } where each node V i represents a random variable. G is called a Bayesian Network if the following factorization of the joint probability of V holds.

where pa(V i ) are parent nodes of V i .

A causal Bayesian Network is a Bayesian Network where all edges denote direct causal relationships. It allows for modeling effect of external actions called "interventions", by appropriate modification of the Bayesian Network. A formal definition of causal Bayesian Networks can be found in Definition 1.3.1, [Pea09].

Interventions: As mentioned above, these capture external actions on a system under consideration, for example, dosage of medicines administered to a patient, providing subsidies to poorer sections of the population, etc. A natural way to model them in causal Bayesian Networks is to perform the act of causal surgery, wherein, incoming edges into the node(s) to be intervened are removed and the node(s) is forcibly fixed to the desired value. As described in Definition 1.3.1, [Pea09], the new network thus obtained is treated as the Bayesian Network modelling effect of the intervention. Formally, following the notation in [Pea09], if we perform intervention on nodes X ⊆ V with a desire to set it to value x * ∈ C X , then the effect of this intervention (also known as interventional distribution) is a probability distribution on V denoted as P(v|do(x * )) (or P x * (v)). In the intervened Bayesian Network, conditional probability distributions (CPD) P(X i |pa(X i )) of all X i ∈ X that are intervened and set to x * i , changes to the Kronecker delta function

The CPD of the non-intervened nodes i.e. V \ X remains unchanged. Hence the interventional distribution factorizes as: 

# Problem Formulation and Main Theorem

As motivated in Section 1, the intended interventions performed during an experiment often have hidden off-target effects, which could themselves be stochastic, leading to different hidden treatments on different individuals. We can model such a situation as an unknown mixture of different interventions. Here is a formal definition. Definition 3.1 (Mixture of Interventions). Let G = {V, E } be a causal Bayesian Network. A probability distribution P mix (V ) is called a mixture of interventions if for some m ∈ N, there exist subsets T 1 , . . . , T m ⊆ V , corresponding values t i ∈ C T i , and positive scalar weights

where t i = t j for all i = j ∈ [m]2 . We allow T i = ∅, in which case, P t i (V ) is defined as P(V ). Note that for P mix to be a valid distribution ∑ m i=1 π i = 1. We refer to the set T = {(t i , π i ), i ∈ [m]} as a set of intervention tuples generating the mixture.

# Uniqueness and Identifiability :

In our mixture model, each of the targets t i , corresponds to an intervention that intentionally or unintentionally transpired in the experiment. Since our ultimate goal is to recover them from the mixture distribution (see Question 1.1), the problem only makes sense if they "uniquely" define the mixture. Formally, there should not exist two distinct sets of intervention tuples

} which generate the same mixture distribution, i.e.,

An immediate next question is that of "identifiability". Given access to a causal Bayesian Network and the joint distribution P(V ) it captures, does there exist an algorithm, that takes as input the mixture distribution P mix (V ) and exactly recovers the unknown set of intervention tuples that generated P mix (V )?

In the general case, the answer to both these questions is no! Using a very simple network, with just one node, we show that mixture distributions need not be unique, motivating the need for more assumptions.

More complicated examples with multiple nodes can be easily created in the same way, but, for a cleaner presentation we stick to this example since its purpose is to only motivate an assumption we make next.

Example 3.1. Consider a causal Bayesian Network with a single binary variable V = {V 1 }, i.e. C V 1 = {0, 1} and denote P(V 1 = 0), P(V 1 = 1) by p 0 , p 1 respectively. Define the mixture,

On setting V 1 = 0 and then V 1 = 1 in the above equation, and rearranging the terms, we obtain

The above 2 × 2 matrix is singular and has rank 1 i.e. the system does not have a unique solution. In fact, when 0 < p 0 < 1,

, 0}. Therefore, uniqueness of intervention tuples does not hold in general.

Even though the example looks very simple, it captures the main reason behind the non-identifiability of the set of intervention tuples. Exactly like the above example, for any mixture, we can obtain systems of linear equations by evaluating marginal probabilities of P mix for different settings of V . Our goal then would be to find settings which help us solve these systems uniquely and recover the set of intervention tuples. Unfortunately, in this process, similar to the above example, the linear systems will have dependent equations and therefore infinitely many solutions. To get over this issue, we focus our attention on sets of intervention tuples, where, for each variable there exists some value that is missing from all of it's intervention targets. In, our main theorem, we show that any mixture generated by such a set cannot be generated by any other set of this kind. Next, we formally state the assumption and then discuss why it is extremely mild and reasonable in most real situations. Assumption 3.1 (Exclusion). Let T be a set of intervention tuples as defined in Definition 3.1. We say that T satisfies exclusion, if for all V i ∈ V , there exists vi ∈ C V i such that vi / ∈ t for any target t belonging to any tuple in T . We say that a mixture of interventions P mix (V ) satisfies exclusion if some set of intervention tuples T generating it satisfies exclusion.

Remark 3.1. This assumption puts only a mild constraint on the set of mixtures we consider. For example, in a network with n nodes and each node having ≤ k possible values, excluding a fixed value of each node, can still generate arbitrary mixtures over Ω(k n ) allowed targets. Without exclusion, there are O((k + 1) n ) possible targets that generate the mixtures. Therefore the reduction is minimal compared to the size of the space of targets we are searching in. In real-world applications, it's common for nodes to have a large number of possible values. Therefore, for each node, the possibility of off-target interventions impacting all values becomes unlikely. We also emphasize that the values missing from the targets can be different for different input mixtures and are not known to our algorithms. Our identifiability algorithm only uses existence of such missing values making its interpretation even more general.

Even though the above assumption helps us tackle the singularity problem outlined in Example 3.1, it is not enough to guarantee uniqueness of intervention tuples in general. We also assume a simple "positivity" assumption on the causal Bayesian Network, which demands that the joint probability P(v) > 0 for any setting V = v. In fact, using the same example as above (Example 3.1), we show that not assuming p 0 , p 1 > 0, can lead to multiple set of intervention tuples satisfying Assumption 3.1 and generating the same mixture. To see this, we consider the input mixture P mix (V ) = P(V ). The set of intervention tuples T 1 = {(∅, 1)} for it clearly satisfies Assumption 3.1 as intervention targets (V 1 = a) and (V 1 = b) are excluded. Now, if p 1 = 0, then P 0 (V 1 ) = P(V 1 ) and for any π 0 ∈ [0, 1], we can trivially write

} is another set of intervention tuples for P mix , implying non-uniqueness. Here is the statement of our assumption. Assumption 3.2 (Positivity). Let V be the set of nodes in our causal Bayesian Network and P(V ) be the corresponding joint probability distribution. We assume that P(v) > 0 for all v ∈ C V . Remark 3.2. As a straight forward consequence of this assumption, for every random variable V i ∈ V , we can show that the conditional probability distributions are positive as well i.e. P(v i |pa(v i )) > 0 for all v i ∈ C V i and setting pa(v i ) of the parents. This positivity assumption is commonly assumed in many works related to causal graphs. For example, [HB12] assume positivity throughout their discussion when characterizing the Interventional Markov Equivalence class.

Having stated these assumptions, we are now ready to state the main theorem of this paper. A detailed proof is provided in Section 4.

Theorem 1. Let G = {V, E } be a causal Bayesian Network and P(V ) be the associated joint probability distribution satisfying Assumption 3.2. Let P mix (V ) (Definition 3.1) be any mixture of interventions that satisfies Assumption 3.1. The following are true.

1. There exists a unique set of intervention tuples T = {(t 1 , π 1 ), . . . , (t m , π m )} satisfying Assumption 3.1, such that

2. Given access to G, P(V ) and P mix (V ), there exists an algorithm, that runs in time n * (m * k max ) O(1) , and, outputs the set of intervention tuples T (satisfying Assumption 3.1) generating it. Here n is the number of nodes in G, m is the size of set T and k max is the maximum number of distinct values that any node can take.

Remark 3.3. Though Assumption 3.2 is a sufficient conditions for Theorem 1, it is not necessary. In Example B.1, we give an example that does not satisfy this assumption but is uniquely generated by a set of intervention tuples satisfying Assumption 3.1.

# Proof of Main Theorem

In this section, we provide rigorous proof to both parts of Theorem 1 together. Our uniqueness proof (for Part 1) is constructive and gives an algorithm as described in Part 2. Our proof goes via an induction argument on the number of nodes n present in the given Bayesian Network. There are many lemmas stated throughout the proof. For a cleaner exposition, all of their proofs are provided in Appendix A.

## Base Case (n = 1)

Consider a causal Bayesian Network G = (V, E ) with only one vertex V and no edges (i.e. E = ∅), such that P(V) satisfies Assumption 3.2. Let C V = {v 1 , . . . , v k } be the set of values that V can take. Therefore, by Assumption 3.2, P(v i ) > 0 for all i ∈ [k]. Next, consider any mixture of interventions P mix (V) that satisfies Assumption 3.1. Writing the most general form of P mix , i.e. allowing for scalar weights to be ≥ 0, we can write,

where

. By the notation in Definition 3.1, P ∅ (V) = P(V). Subtracting P(V) from both sides and setting π 0 = 1 -∑ k i=1 π i , we get,

Recall, from the definition of interventions in Section 2, for any

gives us k linear equations which can be written in the following matrix form:

where b i = P mix (v i ) -P(v i ) and a i = P(v i ) > 0 (Assumption 3.2). Any set of intervention tuples T generating P mix (V) can be obtained as a solution to the above system. Since, in Part 1 of the theorem we restrict our focus to T that satisfy Assumption 3.1, we know there exists some i ∈ [k], such that π i = 0. In the following lemma, we show that such a system under these assumptions has a unique solution when π 1 , . . . , π k ∈ R ≥0 . Proof of this lemma is presented in Appendix A.1.

Lemma 4.1. Consider the following linear system.

Assume that a 1 , . . . , a k > 0, ∑ k j=1 a j = c and it has at least one solution. Then, rank of the above matrix is k -1 and there are infinitely many solutions. Under the assumption that x ∈ R ≥0 and x i = 0 for some i ∈ [k], the solution becomes unique. Given access to a j s, b j s and c, there exists an algorithm that computes this solution in k O(1) time.

It's easy to see that Equation 1 satisfies all requirements of Lemma 4.1, implying the base case of our induction proof.

Inductive hypothesis (n = N): Assume, Theorem 1 is true for all causal Bayesian Networks on N nodes, that satisfy Assumption 3.2 and input mixtures that satisfy Assumption 3.1.

## Induction step (n = N + 1):

Assuming the above inductive hypothesis, we show that Theorem 1 is true for all causal Bayesian Networks on N + 1 nodes, and mixture of interventions on it, satisfying Assumptions 3.2 and 3.1 respectively. Let V = {V 1 , . . . , V N+1 }, P(V ) be the distribution of V and P mix (V ) be any mixture of interventions that satisfies Assumption 3.1. We wish to show that there is a unique set of intervention tuples satisfying Assumption 3.1 that generates P mix (V ). Without loss of generality let V 1 ≺ . . . ≺ V N+1 be a topological order for G. We will now marginalize on V N+1 to reduce our problem to the n = N case, so that we can use the inductive hypothesis. The following lemma is required to make this argument. We present it's proof in Appendix A.2. Lemma 4.2. Let V N = {V 1 , . . . , V N }, 1. P(V N ) is generated by the CBN G N obtained by deleting vertex V N+1 (and all its incoming edges) from G, and satisfies Assumption 3.2.

2. P mix (V N ) can be written as a mixture of interventions on G N that satisfies Assumption 3.1.

3. Given access to P(V ) and P mix (V ), in O(k max ) time we can create access to P(V N ) and P mix (V N ), by marginalizing on V N+1 .

Using the inductive hypothesis with this claim, we get that there exists a unique set of intervention tuples S = {(s 1 , µ 1 ), . . . , (s q , µ q )}3 satisfying Assumption 3.1 that generates P mix (V N ), i.e.,

The induction hypothesis also implies that S can be computed in N * (q * k max ) O(1) time using access to P(V N ) and P mix (V N ). The next step in our proof then is to show that, for a given G, P(V ) and P mix (V ), the set of intervention tuples S can be uniquely lifted to a set T of intervention tuples that satisfies Assumption 3.1 and generates P mix (V ). We also show that using access to G, P(V ) and P mix (V ), the lifting process runs in (m * k max ) O(1) time implying that T can be computed in (N + 1) * (m * k max ) O(1) time.

### Lifting S

In this section we lift the set of intervention tuples S generating P mix (V N ) uniquely to a set of intervention tuples satisfying Assumption 3.1 generating P mix (V ). Let T = {(t 1 , π 1 ), . . . , (t m , π m )} be any arbitrary set of intervention tuples satisfying Assumption 3.1 that generates P mix (V ), i.e.

(2)

First, we give a lemma that connects targets t 1 , . . . t m inside T with targets s 1 , . . . s q inside S. We present it's proof in Appendix A.3. Lemma 4.3. For every t i , i ∈ [m], there is some s j , j ∈ [q] such that, either t i = s j or t i = s j ∪ {v} for some v in C V N+1 .

For j ∈ [q], we define sets S j = {s j , s j ∪ {v 1 }, . . . s j ∪ {v k }} where C V N+1 = {v 1 , . . . , v k }. Since the targets s j , j ∈ [q] are distinct, the sets S j , j ∈ [q] are disjoint. Lemma 4.3 implies that {t 1 , . . . , t m } ⊂ S 1 ∪ . . . S q Since T was arbitrary, for every such T , there exist non-negative scalars π s , s ∈ S 1 ∪ . . . ∪ S q such that Equation 2 can be written as,

Any solution of Equation 3 with π s ≥ 0 gives a set of intervention tuples for P mix . We show that there is a unique such set which satisfies Assumption 3.1.

Lemma 4.4. Let π s , s ∈ S 1 ∪ . . . ∪ S q be some non-negative solution to Equation 3 and the set T = {(s, π s ) : π s > 0} be the corresponding set of intervention tuples. There exists a unique T that satisfies Assumption 3.1.

Proof. We show that enforcing Assumption 3.1 uniquely determines all π s as solutions to a sequence of system of linear equations, implying that there is a unique T that satisfies Assumption 3.1. To construct this sequence, we need an ordering on s 1 , . . . , s q . So, without loss of generality, we assume that for j 1 ≤ j 2 , s j 2 ⊆ s j 1 . The linear equations are created by using specific settings for V in Equation 3 which enable us to decompose the linear system into a sequence of simpler systems i.e. one for each S i . We propose these settings next and explain why and how they work. Since S satisfies Assumption 3.1, there exists vi

The following lemma is used to decompose the system of equations into simpler systems. Proof is presented in Appendix A.4.

Lemma 4.5. For i ∈ [q], l ∈ [k] and s ∈ S i+1 ∪ . . . ∪ S q , P s (v i,l ) = 0 Using this in Equation 3, leaves us with the following simpler system for every i ∈ [q],

Suppose all π s , s ∈ S 1 ∪ . . . ∪ S i-1 , have been determined. Then the left had side of this equation is completely known and has no unknown variables. We denote it by ∆ going forward. Therefore, by varying l ∈ [k], we have k equations in k + 1 variables π s , s ∈ S i . In the next lemma, we will obtain a linear equation satisfied by these k + 1 variables and reduce the system to k equations in k variables. On marginalizing over V N+1 in Equation 3, we get Lemma 4.6. For all i ∈ [q] and (s i , µ i ) ∈ S, the following holds.

Proof of Lemma 4.6 is presented in Appendix A.5. By making the substitution from this lemma above into Equation 4, we get the equation

(5) that gives a system of k equations in k variables when we vary l ∈ [k]. Clearly we are looking for nonnegative solutions for π s i ∪{v l } , l ∈ [k]. When we enforce Assumption 3.1, there is some l ∈ [k] such that π s i ∪{v l } = 0. In Lemma 4.7, we show that we can uniquely solve Equation 5 for such

Lemma 4.7. For every i ∈ [q], Equation 5 has a unique solution when we enforce that π s i ∪{v l } , l ∈ [k] are non-negative and at least one of them is 0.

We present a proof of this Lemma in Appendix A.6. This lemma implies that under enforcement of Assumption 3.1, all targets ∈ S i (and their respective mixing coefficients) that appear in P mix (V ) get uniquely identified. Using this technique from i = 1 to q, any set of intervention tuples satisfying Assumption 3.1 that generates P mix (V ) gets uniquely identified. Therefore, there is a unique set of intervention tuples T that generates P mix and satisfies Assumption 3.1.

The lifting of targets in S i is done in Lemma 4.7 using technique from Lemma 4.1 which takes (k max ) O(1) time. This is repeated for all i ∈ [q], therefore, we spend (q * k max ) O(1) time. It's easy to see that q ≤ m and so using the induction hypothesis the set of intervention tuples is computed in (N + 1) * (m * k max ) O(1) time, completing the induction step. We describe our complete algorithm in Algorithm 1. It's correctness and time complexity follows from the discussion in this section. For better understanding, in Examples C.1 and C.2, we provide two worked out examples on small problem instances, that illustrate important aspects of our algorithm.

# Simulation Study

The main purpose of this simulation study is to experimentally analyze the performance of Algorithm 2 which modifies Algorithm 1 to make it work with finite number of samples from distributions P mix (V ) and P(V ).

# Algorithm 1: DISENTANGLE-INFINITE

input : Variables V = (V 1 , . . . , V N+1 ), CBN G, Distributions P(V ), P mix (V ) output: Set of intervention tuples T 1. When |V | = 1, setup the linear system in Equation 1 and solve it using technique described in Lemma 4.1 to obtain a set T of intervention tuples. return T .

2. Let V 1 ≺ . . . ≺ V N+1 denote a topological order in G. Marginalize on V N+1 to create access to P mix (V N ) and P(V N ) where

Recursively call this algorithm with inputs G N , P(V N ), P mix (V N ), to compute the unique set of intervention tuples S = {(s 1 , µ 1 ), . . . , (s q , µ q )} that satisfies Assumption 3.1 and generates P mix (V N ). Let s 1 , . . . , s q be ordered such that i ≤ j implies that s j ⊆ s i . For each i ∈ [N], by inspecting s j , j ∈ [q], identify vi ∈ C V i such that vi / ∈ s j for any j ∈ [q]. Define s -j = { vi :

3. For each fixed i ∈ [q], evaluate distributions for different v i,l , l ∈ [k], to setup the system of equations described in Equation 5. Solve the system using the technique outlined in proof of Lemma 4.7 (which in turn uses Lemma 4.1). At the end of this process collect all the intervention tuples thus obtained (for all i ∈ [q]), in the set T . return T .

# Simulation Setup:

For each simulation setting (N, M)5 we randomly sample a directed acyclic graph on N nodes (each having 3 categorical values), from the Scale-Free (SF) model ( [BA99]), with number of edges chosen uniformly randomly from the set of integers [N, 5N]. Given this graph, we model the conditional probability distribution of each node as a multinoulli distribution with Dirichlet priors having fixed parameter α = 2 for all categories. This is done to conform with Assumption 3.2. This generates our causal Bayesian Network G. We estimate marginal probabilities of the joint distribution defined by G by generating M samples using ancestral sampling on the network. Now, to create input instances, we first choose an integer m uniformly randomly from the set [4, 16] and use this as the number of intervention tuples in the mixture. Then we iterate from 1 to m to build each intervention target of the mixture. First, we choose the size of the target by picking an integer r uniformly randomly from the set {0, . . . , N}. Then we uniformly randomly choose an r-sized subset of [N], defining the variables in the current target. For each of these variables, we first choose a category uniformly randomly and remove it from consideration (in order to satisfy Assumption 3.1). From the remaining categories, we uniformly randomly select one for each of the variables in the target. Finally, we generate m scalar weights for the mixing coefficients such that they sum to 1. In order to make sure that these coefficients are not too small, we generate them with Dirichlet priors with all parameter values fixed to 2. The settings for number of nodes N and sample size M used in the experiment are (N, M) ∈ {4, 8, 12} × {2 4 , 2 5 , . . . , 2 20 } where × is the direct product of sets.

Results Discussion: Figure 1 presents four plots that demonstrate performance of our algorithm as sample size M varies in {2 4 , 2 5 , . . . , 2 20 }. We also vary the number of nodes N in {4, 8, 12} and show separate plots for each N in each of the figures. The four plots in Figure 1, demonstrate four different accuracy metrics we describe in Appendix F. In Figure 1a, we plot the average recall of intervention targets as M increases. Recall for a single input instance is the number of intervention targets in the input that are identified in the output, as defined in Appendix F. Average recall is the average of this over all random instances generated in the simulation. We observe a general trend of increase in the recall as we increase the number of samples. Also, a relatively larger number of samples are required to achieve the same level of recall for mixtures generated from CBN with a large number of nodes as compared to smaller ones. This trend is expected as Algorithm 2 estimates the intervention targets by sequentially adding nodes to them. Hence for larger-sized CBNs, the error accumulated is larger as compared to smaller ones.

In Figure 1b, we plot the average root-mean-squared error (RMSE) between the estimated and actual mixing coefficients. For each input, RMSE is calculated using the definition supplied in Appendix F. Then it is averaged over all the random input instances. We observe a fast decrease in the average RMSE as M increases. We also observe that the average RMSE is higher for higher N. This is also expected since for distributions on larger number of variables, more samples will be needed to estimate marginal probabilities accurately.

In Figure 1c, we plot average False-Positive RMSE (Section Appendix F) or FP-RMSE as M increases. For each input instance, FP-RMSE computes the RMSE in mixing proportions for components which are not present in actual target set but predicted by our algorithm. This is then averaged over all the random input instances. For each value of N, we observe a similar decreasing trend in this plot showing that incorrect targets in our output have very small mixing proportions (as sample size increases) and therefore even if they are present in the output their contribution is insignificant.

In Figure 1d, we plot average False-Negative RMSE (Section Appendix F) or FN-RMSE as M increases. For each input instance, FN-RMSE computes the RMSE in mixing proportions for components present in the actual target but not present in the output targets. This is then averaged over all the random input instances. Even though we observe a clear decreasing trend in this situation as well, the rate is much slower as N increases. This implies that the sample complexity of our algorithm is high and it might need too many samples to correctly identify the coefficients of targets present in the input. Reducing the sample complexity is an interesting research direction which we plan to pursue in a future work.

In Figure 3, we demonstrate and compare performance of our Algorithm (as M, N increase), for CBNs generated using different random graph models (Scale-Free and Erdös-Rényi). We observe no significant difference in performance and make a conjecture that only high level graph parameters (such as number of nodes, edges, in-degree etc.) might be having an impact on performance and the topology (given these parameters) might not be that crucial.

To further understand the performance of our algorithm with respect to the number of nodes, in Figure 2, we plot the Average Recall and Average RMSE as number of nodes varies from 4 to 32, for a fixed sample size of ∼ 10 6 . We observe that recall decreases and RMSE increases very quickly as number of nodes increase. Even though this is expected since error is accumulated as we successively add nodes and find new intervention targets, such performance for a very large sample size indicates bad dependence of sample complexity on the number of nodes. Improving this needs more exploration and is left for future work.

Limitations and Future Directions: The increasing trend in recall and decreasing trend in RMSE of mixing coefficients shows promise. But the current algorithm appears to be expensive in terms of sample complexity, especially for mixture generated from larger graphs as seen in Figures 1a,1d and Figure 2. Hence, it will be interesting to explore directions which could reduce sample complexity. We leave this for future work. Another limitation is the absence of baseline works to compare to. Since, ours is the first paper that proves identifiability of such mixtures and gives the first such algorithm, there are no prior works to compare against. In future, we plan to compare our algorithm on a related or downstream task that might have been explored in other works such as [TMCH98, SWU20, JKSB20].

# Conclusion

In this paper, we investigated the problem of identifying individual intervention targets from a mixture of interventions on a causal Bayesian Network. This problem is well motivated from the real-world scenario wherein experiments/interventions are accompanied by stochastic hidden off-target effects. We modeled this problem as a mixture of intervention distributions and constructed examples to show that, in general, it is impossible to identify all targets in it. Then, we proposed a mild positivity assumption on the underlying network and a very reasonable exclusion assumption on the intervention targets that can appear in the mixture distribution. Using these assumptions we proved that given access to the underlying CBN and the mixture distribution, there is a unique set of intervention targets that satisfies our exclusion assumption and also generates the mixture. Our uniqueness proof also provides an algorithm that uses access to the underlying distributions and efficiently identifies all the targets along with their coefficients in the mixture. In order to work with finitely many samples from the distributions, we created a small modification to our algorithm and validated it's performance using simulated experiments. We tested our algorithm and bench-marked its performance as the number of samples and nodes increased. As future work, we plan to investigate algorithms to recover targets in such mixtures using a smaller number of samples. Another interesting direction is to use limited access to the underlying CBN while recovering the targets. This can be very useful in situations where sufficient data or prior knowledge might not be available to pin down the CBN. Solving the identifiability problem when the CBN has unobserved confounders might be a good first step in this direction. a fruitful and enjoyable research experience. Abhinav Kumar did this internship as part of his undergraduate thesis offered by his undergraduate institution BITS Pilani, Hyderabad. He would like to thank the institution for this opportunity. Gaurav Sinha would like to thank his mentees Aurghya Maiti, Pulkit Goel, Naman Poddar and Ayush Chauhan who were part of an older internship where the seed of this work was planted. The authors would like to thank anonymous reviewers for their very helpful comments which helped in greatly improving the presentation of this paper.

# A Proofs from Section 4

In this section, we provide missing proofs of the lemmas stated in Section 4.

# A.1 Proof of Lemma 4.1

Note that we have assumed a i > 0 for all i ∈ [k]. We iterate from i = 1 to k -1 and apply the following row transformations on our matrix.

This results in the following linear system.

where bi = (b i -a i a k b k ) for all i ∈ [k -1] and bk = b k . Since c > 0, this matrix is easily seen to have rank ≥ k -1. Using c = ∑ k i=1 a i we can easily check that the last row R k is -a k c (R 1 + . . . + R k-1 ), implying that it has rank k -1. Since the system is assumed to have at least one solution, it actually has infinitely many solutions. The null space of this matrix is the one dimensional space spanned by w = ( a 1 a k , . . . , a k a k ) T which has all positive entries since a i > 0, i ∈ [k]. Assume there are two distinct solutions u = (u 1 , . . . , u k ) T and v = (v 1 , . . . , v k ) T in R k ≥0 such that both have at least one of their co-ordinates 0, then uv belongs to the null space i.e. uv = λw for some non-zero scalar λ. If the same co-ordinate of u, v are 0 i.e. for some i ∈ [k], u i = v i = 0, then since a i a k is non-zero λ = 0 ⇒ u = v, a contradiction. If different co-ordinates of u, v are 0, say u 1 = v 2 = 0, then since u, v ∈ R k ≥0 , u 1v 1 is negative and u 2v 2 is positive. This is not possible since both these quantities should have the same sign as λ, as all co-ordinates of w are strictly positive. Therefore we arrive at a contradiction and there is a unique solution.

Having proved this uniqueness, finding the solution is easy. We perform the above-mentioned row transformations and obtain the general solution. Then for each i ∈ [k], we set x i = 0 and try to solve for the other variables x 1 , . . . , x i-1 , x i+1 , . . . , x k ∈ R ≥0 . By the above argument, we will get a valid solution for only one such i, which we return as the unique solution. Clearly it takes k O(1) time.

A.2 Proof of Lemma 4.2

2. Let T = {(π 1 , t 1 ), . . . , (π m , t m )} be a set of intervention tuples generating P mix (V ) and C V N+1 = {v 1 , . . . , v k }. Marginalizing with respect to V N+1 for a single target

Applying this marginalization to Equation 2, i.e., P mix (V ) = ∑ m i=1 π i P t i (V ), gives a convex linear combination of different P s (V N ), where s are values of some set of variables S ⊂ V N , implying that

3. This is straight-forward. To query P(v 1 , . . . , v N ), we query P(v 1 , . . . , v N , v N+1 ) for all v N+1 ∈ C V N+1

and sum them up. The same can be done to create access for P mix (V N ). Since we are summing at most k max terms, in O(k max ) time we can simulate access to both P(V N ), P mix (V N ).

# A.3 Proof of Lemma 4.3

This follows by the marginalization equation (Equation 6 in Appendix A.2).

# A.4 Proof of Lemma 4.5

Let s ∈ S r where r > i. This means that s is either s r or s r ∪ {v} for some v ∈ C V N+1 . We show that P s r (v i,l ) = P s r (s i ∪ s -i ∪ {v l }) = 0 for all v l ∈ C V N+1 . The proof for s = s r ∪ {v} is identical. Since i < r, we get that s r ⊆ s i . Now there are two cases, either the set of variables S r ⊆ S i or S r ⊆ S i . In the first case, since s r ⊆ s i we get that there is some variable V j ∈ S r , S i such that different values v r j and v i j belong to s r and s i respectively implying that P s r (s i ∪ s -i ∪ {v}) = 0. In the second case, there is some variable V j ∈ S r (j ∈ [N]) that is not in S i . Note that the "missing value" vj ∈ C V j (i.e. the one that is missing from all targets s j , j ∈ [q]) belongs to s -i (since V j / ∈ S i ) but it cannot belong to s r (since it is missing from all s 1 , . . . , s q ) ⇒ P s r (s i ∪ s -i ∪ {v}) = 0.

# A.5 Proof of Lemma 4.6

Let s ∈ S i . Note that s is either s i or s i ∪ {v} for some v ∈ C V N+1 . Using Equation 6 we get that for all s ∈ S i , marginalization of V N+1 in π s P s (V ) gives π s P s i (V N ). Marginalizing V N+1 in Equation 3, converts the left hand side to P mix (V N ) and right-hand side to ∑ q i=1 (∑ s∈S i π s )P s i (V N ) giving a set of intervention tuples that generates P mix (V N ). By the inductive hypothesis, P mix (V N ) is generated by the unique set of intervention tuples S satisfying Assumption 3.1. Since the intervention targets in S and the ones in the set of intervention tuples we just obtained are the same, using uniqueness of S we get that µ i = ∑ s∈S i π s .

# A.6 Proof of Lemma 4.7

Note that since V N+1 is the last node in the topological order, using the definition of interventions, we can conclude that,

. Now, on substituting for ∆ using Equation 4 into Equation 5, we obtain,

Note that all the unknown variables are on the right-hand side of this equation. Varying l ∈ [k], gives us a linear system of equations satisfied by scalars

In the above system, we have renamed the known values as follows. For l ∈ [k], denote

All a l 's are probabilities from interventional distributions and can be computed as product of conditional probabilities. Thus, by Assumption 3.2, a l > 0 for all l ∈ [k]. It's easy to see that c = ∑ l∈[k] a l , by the sum rule of probability. By statement of Lemma 4.3, for each i ∈ [q] and l ∈ [k], π s i ∪{v l } ≥ 0. Since we are only considering set of intervention tuples which satisfy Assumption 3.1, there is some l ∈ [k] such that π s i ∪{v l } = 0. On constraining the variables x 1 , . . . , x k in the above system to these conditions (i.e. x l ≥ 0 for all l ∈ [k] and x l = 0 for some l ∈ [k]), by Lemma 4.1 we are guaranteed a unique solution. Therefore there is a unique tuple (π s i ∪{v 1 } , . . . , π s i ∪{v k } ) satisfying these requirements ⇒ Equation 5 has a unique solution which is easily computed in k O(1) time using the technique described in proof of Lemma 4.1.

# B Non-Necessity of Assumption 3.2

With the help of an example we argue that Assumption 3.2 is not necessary in Theorem 1.

Example B.1. Consider a causal Bayesian Network V 1 → V 2 defined over two binary variable V = {V 1 , V 2 } with C V i = {0, 1}, i ∈ [2]. Further, define CPDs, P(V 1 = 1) = 0.5, P(V 2 = 1|V 1 = 0) = 0.5, and P(V 2 = 1|V 1 = 1) = 0. Clearly P(V 2 = 1, V 1 = 1) = 0 implying that this CBN doesn't satisfy Assumption 3.2.

Let P mix (V ) be a mixture distribution defined as

This mixture satisfies Assumption 3.1. Our algorithm first marginalizes on V 2 and tries to find the unique set of intervention targets for P mix (V 1 ). For this sub-problem, all steps of Algorithm 1 go through (since the distribution P(V 1 ) satisfies positivity), and the correct components get identified. Note that, for this sub-problem the algorithm identifies that P mix (V 1 ) = P(V 1 |do(V 1 = 0)). Now it tries to lift this computed target (V 1 = 0) to targets for the full mixture P mix (V ).

Since the algorithm does not try to lift the target (V 1 = 1) (as it was not found as a target for P mix (V 1 )), it does not require P(V 2 |V 1 = 1) to be non-zero. This can be easily checked in the lifting process described in Section 4.2.1. We do not repeat the steps of our algorithm here and encourage the reader to work through the lifting steps outlined in Section 4.2.1 and obtain unique solutions proving our point that Assumption 3.2 is not necessary and can be weakened.

# C Worked-Out Examples

In this section, we illustrate the workings of Algorithm 1 (in the main paper) using two worked-out examples. Example C.1 is simpler and uses a mixture distribution on a CBN with just two nodes. It does not really require all of the crucial ideas from the lifting procedure described in Section 4.2.1. However, we believe it is important since it gives a good broad understanding of the entire algorithm. Example C.2 is complicated enough (using a mixture distribution on a CBN with three nodes) to highlight some of the key novelties of our lifting procedure in Section 4.2.1. We urge the reader to first work through Example C.1 and then through Example C.2 to get a full understanding of the critical ideas that make our proof of Theorem 1 work.  

# F Evaluation Metrics

Let T denote the actual set of intervention targets and T denote the set of intervention targets computed by our algorithm. Let π t , π s denote mixing coefficients of target t, s in T and T respectively. We use the following evaluation metrics to evaluate the performance of our algorithm. 

# Acknowledgements

This work was done during an internship of the first author (Abhinav Kumar) under the guidance and mentorship of the second author (Gaurav Sinha), during the period January-August 2020. Abhinav Kumar would like to thank Adobe Research India for hosting him during this period and providing facilities for

# Example C.2. Consider a causal Bayesian Network defined over three binary variables

Let CPDs be such that Assumption 3.2 is satisfied. Consider a mixture distribution

Our inductive hypothesis assumes that this mixture on smaller number of nodes is generated by a unique set of intervention tuples that satisfies Assumption 3.1 and also that this set can be efficiently computed. This will give us access to the two scalars π 0 , π 1 and to the two targets (V 1 = 0) and (V 1 = 0, V 2 = 0) (we call them the currently computed targets). We need to lift these targets to targets for the original mixture distribution like we did in Example C.1. However, the situation is not as simple here. Note that (V 1 = 0) can be lifted to one of the three targets

So there are 6 possible targets in the original mixture and therefore a general solution for our mixture can be written using 6 new variables (say δ 0 , δ 1 , δ 2 , δ 3 , δ 4 , δ 5 ) such that,

where all δ i are non-negative. By marginalizing on V 3 , and using the solution we got from the inductive hypothesis (like we did in Example C.1), we can show that,

Now the two main non trivial ingredients needed from here are:

• Deciding the order in which the currently computed targets should be lifted, and

• Deciding the settings for V that would give linear systems where we can argue about unique solutions like in Example C.1.

For the first one, we lift the currently computed targets in an order which does not violate set inclusion for these targets, i.e. we first lift (V 1 = 0) and then lift (V 1 = 0, V 2 = 0). This can be done by considering any extension of the set inclusion partial order on these targets. Then for lifting the target (V 1 = 0), we choose to evaluate on the settings

Here, we pick the value of V 2 (i.e. V 2 = 1) that is missing from the currently computed target under consideration i.e. (V 1 = 0). There will always be one such missing value (it follows from Assumption 3.1). Evaluating on these settings simplifies our equation drastically. For l ∈ [2], we get,

Basically all possible lifts of the other currently computed target i.e. (V 1 = 0, V 2 = 0) vanish and we have a much simpler system of equations at hand. From here the solution follows exactly like the previous example. We substitute δ 0 = π 0δ 1δ 2 and rearrange to get a linear system in 2 equations and 2 variables δ 1 , δ 2 . Similar to the argument made in Example C.1, at least one of δ 1 , δ 2 will be 0 and therefore this system has a unique solution (using Lemma 4.1) giving values of δ 0 , δ 1 , δ 2 . These can then be substituted back in Equation 7 reducing the number of variables to 3 (i.e. δ 3 , δ 4 , δ 5 ). Again we substitute δ 3 = π 1δ 4δ 5 and reduce the equation to just two unknowns. Finally by

# D Finite Sample Algorithm

In a real world scenario, we will only have finitely many samples from the distributions P(V ) and P mix (V ).

In this situation, we modify Algorithm 1 slightly to make it work with finitely many samples. The resulting algorithm is presented in Algorithm 2. Let the sets containing the samples be B = {b 1 , . . . , b M } where b i ∼ P(V ) and B mix = {b mix 1 , . . . , b mix M } where b mix j ∼ P mix (V ). As a preprocessing step, we estimate the distributions P(V ) and P mix (V ) as P(V ) and Pmix (V ) (respectively) using samples in B and B mix respectively. P(V ) is estimated by estimating all the CPDs using maximum likelihood estimation (MLE). In our implementation, we use a function from the pgmpy library ( [AP15]), to compute these MLE estimates. We enforce Assumption 3.2 on P(V ), by enforcing it on all it's CPDs, using a small positive parameter δ (chosen by us). When P(v i |pa(v i )) = 0 for some v i and some setting of parents pa(v i ), we update,

for all values of V i , and then re-normalize to make it a probability distribution again. Marginal Pmix (V = v) is calculated using relative frequency of the occurence of V = v in the samples inside B mix . These estimated distributions are then used as inputs in Algorithm 2. We use another small positive parameter as input to Algorithm 2 which prunes each recovered set of intervention tuples computed during the algorithm, by only keeping mixing coefficients greater that . It's easy to see that the time complexity of Algorithm 2, including the estimation of probabilities from samples is:

Here N is number of nodes in the CBN G, d is the maximum in-degree of any node in G, k max is maximum number of values that any node in G can take and M is the number of samples present in B and B mix .

Remark D.1. Since our algorithm's run-time depends on , we need to carefully select it's value. Setting it too small could increase the run time whereas setting it too big could lead to wrongfully pruning intervention targets (with significant mixing proportions) present in the mixture.

# E.1 Effect of Graph Size

Figure 2 shows the variation of performance of Algorithm 2 keeping the number of samples fixed at ∼ 10 6 . We observe that recall decreases and root-mean-squared error in mixing coefficient increases very quickly as the number of nodes increases in the graph. Even though this is expected since error is accumulated as we successively add nodes and find new intervention targets, such performance for a very large sample size indicates bad dependence of sample complexity on the number of nodes. Improving this needs more exploration and is left for future work.

Algorithm 2: DISENTANGLE-FINITE input : V , G P(V ), Pmix (V ), output: Set of intervention tuples T 1. When |V | = 1, setup the linear system in Equation 1 (say Ax = b) using the estimated distributions. Similar to the technique described in Lemma 4.1, set one variable to 0 at a time giving solution (π 1 , . . . , π k ) corresponding to targets (t 1 , . . . , t k ) as described in Section 4.1. For every variable that is set to 0, create a set T = {(t i , π i ) : i ∈ [k]} containing the solution. For every such T , iterate through the tuples (t i , π i ) in it. If some π i < 0, set π i ← 0. Compute the score r(T ) = Aπb 2 , where π = (π 1 , . . . , π k ). Next, select T with the smallest value of r(T ). For this selected T , check if

If no, add the tuple (∅, 1 -∑ k i=1 π i ) to T . Only keep the tuples with strictly positive mixing coefficients i.e. T ← {(t i , π i ) ∈ T :

Recursively call this algorithm with inputs G N , P(V N ), Pmix (V N ), and obtain a set of intervention tuples S = {(s 1 , µ 1 ), . . . , (s q , µ q )}. Let s 1 , . . . , s q be ordered such that i ≤ j implies that s j ⊆ s i . For all i ∈ [N], by inspecting s j , identify vi ∈ C V i such that vi / ∈ s j for any j ∈ 

If no, add the tuple (s i , µ i -∑ k l =1 π s i ∪{v l } ) to T . At the end of this process, collect all the intervention tuples thus obtained (for all i ∈ [q]), in the set T . 4. Find the excluded value of node V N+1 , i.e. the value which is not present in any target in T . If no such value exists, find v ∈ C V N+1 which minimizes ∑ q i=1 π s i ∪{v} . For each i ∈ [q], set π s i ∪{v} ← 0. For each i ∈ [q], renormalize the mixing coefficients π s i ∪{v l } ← (π s i ∪{v l } × µ i )/(∑ k l =1 π s i ∪{v l } ). Only keep the tuples with strictly positive mixing coefficients in T i.e. T ← {(s, π s ) ∈ T : π s > 0}. return T

# E.2 Effect of Graph Type

In Figure 3, we demonstrate performance of Algorithm 2 for CBNs generated from two different family of random graphs (Erdös-Rényi (ER) and Scale-Free (SF)). We observe no significant difference in performance for these models and make a conjecture that only high level graph parameters (such as number of nodes, edges, in-degree etc.) might be having an impact on performance and the topology (given these parameters) might not be that crucial.

