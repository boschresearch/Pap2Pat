# Introduction

In fact, when working with user data, maintaining user privacy is absolutely essential. In this work we study a situation where we intend to share an entire (manipulated) dataset, without violating user privacy. Then the dataset might be used by the public for several different purposes. Hence, to measure the accuracy regardless of the downstream task, we use a general purpose metric to measure the similarity of the initial dataset with the shared dataset. To measure the privacy there are a large body of work that attempt to provide formal privacy measures. At a high level, there are two distinct approaches to quantifying privacy, differential privacy and k-anonymity.

Differential privacy is a property of a data processing algorithm and it ensures that small changes in input (typically the presence or absence of any individual user) lead to minimal changes in the output. All differentially private algorithms are randomized, and the uncertainty introduced by the randomization provides a layer of protection. On the other hand, k-anonymity is a property of the dataset. To make a dataset k-anonymous one either generalizes or removes data that is identifiable, so that in the final dataset any information is shared by at least k distinct users. Both approaches have their own pros and cons, which we briefly discuss next. (We defer the formal definitions to Section 3.)

The main advantage of differential privacy is that the output of a differentially private algorithm remains such even in the face of arbitrary post-processing by an adversary armed with additional side information about the users. This is one reason why it has emerged as the gold standard of privacy. However, as we share more information the differential privacy measure gets weaker. In this work we prove that sharing sparse binary matrices with differential privacy guarantees is infeasible (See Theorem 4.3). Roughly speaking, we prove that any differentially private algorithm either provides a very weak privacy guarantee, or significantly changes the dataset, destroying the underlying signal.

On the other hand, k-anonymity Sweeney [2002] is a popular pre-processing technique that can be used to provide some level of privacy. While k-anonymity can be vulnerable to certain attacks Ranjit et al. [2008],

it still provides meaningful guarantees when adversaries have limited access to side information Bassily et al. [2013]. Moreover, in cases where a data analyst cannot withstand noise, it still represents a formal way to give privacy protections. Making a dataset k-anonymous while best preserving utility is an NP-hard problem Aggarwal et al. [2005]. Current approximation algorithms offer the guarantee of removing at most O(log(k)) times more elements than that of an optimal solution, however, such a bound is vacuous when the optimal solution has to remove a constant fraction of the dataset (or anything smaller than a 1 -O 1 log(k) fraction). In those cases the algorithm that just returns a null dataset achieves the same guarantee.

In this work, we strive to design an approach for sharing a binary matrix, while respecting the privacy of the users. In order to do this we study a variant of k-anonymity (called smooth-k-anonymity). Then we provide a polynomial-time approximation algorithm for smooth-k-anonymity in binary matrices and in theory improve the approximation guarantees of the state of the art results for k-anonymization.

In the binary matrix representation, each row represents the data of one user and each column corresponds to a feature, and if the user u has the feature f , element (u, f ) in the matrix is 1. This representation captures the following common setups: Bipartite Graphs: The nodes of one side correspond to the users and the nodes of the other side corresponds to the features. If user u has feature f , there is an edge between u and f . User Lists: We have a collection of lists of users, and each list is associated with a feature. If user u has feature f , user u exists in the list associated with f . Points in a Binary Space: Each user is associated with a point. The coordinates of the point are equivalent to the respective row in the matrix representation.

# Related work

The problem of anonymizing data is very well studied. One of the first techniques for anonymizing data sets was k-anonymity Sweeney [2002]. This notion was intended for tabular data where each row corresponds to a user and each column corresponds to a particular feature. The authors define k-anonymity in terms of quasi-identifiers. That is, columns in the data set that, combined, could single out a user. A k-anonymous dataset is one where every user is indistinguishable from k-other users with respect to the quasi-identifier set only (that means that the columns not corresponding to quasi-identifiers are not anonymized). Other works have improved upon this definition by enforcing other restrictions such as requiring l-diversity Machanavajjhala et al. [2007] or t-closeness Li et al. [2007] for non quasi-identifiers, on top of k-anonymity for quasi-identifiers. The choice of quasi-identifiers is crucial since an attacker with just a small amount of information about a user could de-anonymize a dataset Narayanan and Shmatikov [2008].

The majority of work on k-anonymity has been focused on finding the optimal k-anonymous dataset. That is, one that approximates the original data the best. Meyerson and Williams [2004] showed that this task is in fact NP-hard, although it admits a O(k log k) approximation with running time exponential in k. Later on, Aggarwal et al. [2005] obtained a polynomial time approximation of O(k) which was improved by Kenig and Tassa [2012], Park and Shim [2010] to a O(log k) approximation. Several variants of these algorithms including using set cover approximations Wang et al. [2010]. In addition to these algorithms with provable guarantees, other work has provided heuristics for different notions of anonymization. For instance LeFevre et al. [2006] has defined a heuristic algorithm for k-anonymization of quasi-identifiers based on the construction similar to that of kd-trees Friedman et al. [1977]. Other authors have defined heuristics based on clustering Byun et al. [2007], Zheng et al. [2018]. None of those methods have provable guarantees in our context.

Another related work to ours is that of Cheng et al. [2010], which defines the notion of k-isomorphism in social network graphs. Essentially, a graph is k-isomorphic if it can be decomposed into a union of k distinct isomorphic sub-graphs. This notion of anonymity is limited to social network graphs as the goal is to prevent an attacker from identifying a user based on the structure of their neighborhood.

A different framework for achieving anonymity is differential privacy Dwork and Roth [2014]. Unlike k-anonymity, differential privacy provides mathematical guarantees on the amount of information that can be gained by an attacker that observes a differentially private dataset. Differential privacy has been effectively applied for statistics release Dwork and Smith [2010] and empirical risk minimization Chaudhuri et al. [2011] among many other scenarios. The vast majority of differential privacy examples require the mechanism to output a summarized version of the data: a statistic or a model in the case of risk minimization. To release a full dataset in a differentially private manner, Kasiviswanathan et al. [2011] introduces the notion of local differential privacy. Local differential privacy allows us to release a full dataset while protecting the information of all users.

Methods from differential privacy have also been used for the release of private graph information. For instance, Nissim et al. [2007] shows how to compute the minimum spanning trees and the number of triangles in a graph. Eliáš et al. [2020] recently showed how to preserve cuts in graphs with differential privacy. Kasiviswanathan et al. [2013] introduce the notions of edge and node differential privacy in graph settings and show how to calculate functions over graphs under node differential privacy by capping the number of edges per node. Arguably the work most related to this paper is that of Nguyen et al. [2016]. The authors propose edge-differential privacy in order to release an anonymous graph. Similar to our results in Corollary 4.2, the authors show that a value of in Ω(log n) is needed in order to achieve non-trivial utility guarantees, where n is the number of nodes in the graph.

We observe that some work has been devoted to combining differential privacy with k-anonymity guarantees. Li et al. [2011] show that enforcing k-anonymity in certain data-oblivious ways on a sub-sampled dataset, is sufficient to show differential privacy guarantees.

Our algorithmic techniques are related to the lower bounded facility location problem Ahmadian and Swamy [2012], Guha et al. [2000], Svitkina [2010]. This problem has been first introduced and studied independently by Karget and Minkoff [2000] and Guha et al. [2000]. Lower bounded clustering problems have been motivated by privacy purposes Motwani and Nabar [2008]. They both provide bicriteria approximation algorithms for this problem. Later, Svitkina [2010] provided a 448-approximation algorithm for this problem. This is the first constant approximation algorithm for this problem. Ahmadian and Swamy [2012] improved Svitkina's result and give an 82.6 approximation algorithm for this problem. To the best of our knowledge the latter is the best approximation algorithm for the lower bounded facility location problem.

# Setup

Given the equivalence of binary matrices and bipartite graphs, for ease of notation we mostly use graph theoretical terminology to describe our work. We assume we are given a bipartite graph, where one set of nodes corresponds to users and another set of nodes corresponds to features. This is a common modeling step, for instance in location analysis applications the features may represent places visited; in social network modeling, the features may represent interests shared by different users; and so on.

Let U = {u 1 , . . . , u n } denote a set of users and F = {f 1 , . . . , f m } a set of features. Throughout the paper we use n and m as the |U | and |F |, respectively. The edge set E of the graph is defined as follows, given u ∈ U and f ∈ F , we say e = (u, f ) ∈ E if user u is associated with item f . We denote this graph by G = (U ∪ F, E). Let G denote the space of all bipartite graphs over U ∪ F , a mechanism M : G → G is a (possibly randomized) function that maps G = (U ∪ F, E) to another graph G = (U ∪ F, E ) with the same set of nodes but with possibly different edges. Throughout the paper given two sets A and B we denote their symmetric difference by A ⊕ B.

We now introduce the different notions of privacy we will be using throughout the paper.

Definition 3.1. Edge differential privacy. We say a randomized mechanism M preserves -edge differential privacy if for any two graphs G = (U ∪ F, E) and G = (U ∪ F, E ) such that |E ⊕ E | = 1 the following holds for all A ⊂ G:

Edge differential privacy implies that the output of a mechanism does not change too much if a single edge of the input graph is changed. Thus an adversary that observes the output of M(G) may not be able to infer if a single edge was present or not in the graph.

However, if a user has a high degree in G, then the output of an edge-differentially private algorithm may still leak information about the presence or absence of that user in the graph. This leads to a definition of node-differential privacy which we detail below. Definition 3.2. We say that two graphs G

That is, two graphs are node neighboring if one can be obtained from the other by replacing all the edges of a single user. Definition 3.3 (Node differential privacy). We say a mechanism M preserves node differential privacy if for any two node neighboring graphs G and G and for all A ⊂ G

Under this notion of anonymity, it is very unlikely for an adversary to identify a user in a particular dataset. While the above notions of differential privacy provide quantifiable protection against an attacker, as we will see, they also require adding a non-trivial amount of noise.

For this reason we revisit an older notion of privacy: k-anonymity. While the original definition of k-anonymity Sweeney [2002] requires defining quasi-identifiers, in this work we assume that every feature can be used as a quasi-identifier.

We first introduce some notation. We will consider graphs in G with fixed node sets U ∪ F , and varying edge sets. Let G = (U ∪ F, E) ∈ G be one such graph, notice that the graph is identified by E. For a given edge set E, let F u (E) = {f ∈ F : (u, f ) ∈ E} be the items associated with u in the set edge set E. Notice we can then partition users into equivalence classes. Formally, let

Now we are ready to formally define k-anonymity by suppression.

# Definition 3.4 (k-anonymization and k-anonymization by suppression

The mechanism M is k-anonymous by suppression if it also satisfies 1. E ⊂ E That is the set of items associated with each user in the output graph, is the same of that of at least k users. Moreover, in k-anonymity with suppression the output set of edges E needs to be a subset of E. Notice that with a k-anonymous output an adversary can only distinguish a user up to a set of k different people.

Finally, we introduce our variant of the above definition.

2. For every u ∈ U , and every

This definition is very similar to Definition 3.4. The main difference between the definitions is that a smooth-k-anonymous mechanism is only allowed to add edges to the output if, for each equivalence class of users and each item connected to them, the majority of such edges belong to the original graph. Figure 1 we depict the difference between our smooth-k-anonymous and k-anonymity with suppression.

We conclude this section by defining the utility measure of a mechanism. In order for a mechanism to be useful it should preserve as much as possible of the graph structure. In this paper we measure this by the Jaccard similarity of two graphs.  Algorithm 1 Randomized response

# Comparison of privacy notions

In this paper we introduce the new algorithmic problem of finding the best smooth-k-anonymization of a graph. For this reason, in this section, we provide some comparison between smooth-k-anonymity and alternative privacy notions that can be used for data release.

## Comparison with differential privacy

Node differential privacy As we have briefly discussed, node-differential privacy provides the best theoretical guarantees for privacy protection. In the specifics of our setup, node-differential privacy is equivalent to the so-called local differential privacy Kasiviswanathan et al. [2011], where every user is acting separately without coordination from some global authority. Let G = (U ∪ F, E), borrowing from local differential privacy ideas, one way of achieving node differential privacy is by releasing M(G) = (U ∪ F, E ) built according to Algorithm 1. The algorithm is parameterized by a randomized response probability p. It is not hard to show that in order to achieve -node differential privacy p = . Notice that this value converges to 1 exponentially fast as a function of the size of the feature set F . That is, even for relatively small graphs, in order to achieve any meaningful privacy guarantee, the probability of returning a completely random graph is very close to 1. For this reason, this notion is not amenable to be used with good utility in our setting.

Edge differential privacy Algorithm 1 can also be used to define a mechanism M that is edge differential privacy. In that case one can achieve -edge differential privacy by setting p = 2 1+e (see Appendix B.1). In this section fist we consider Algorithm 1 as a natural way to provide differential privacy and upper bound the Jaccard similarity of the input and the output graphs of this algorithm. Later in this section we show that a similar bound holds for all differential privacy algorithms.

We now upper bound the similarity of the output of the algorithm with -edge differential privacy. The bound depends on the density λ of the graph G defined as:

Q , then with probability at least 1 -δ: Using Theorem 4.1, we can plot in Figure 2 a lower bound for the needed to achieve a certain level of Jaccard similarity utility, given a density factor λ. Notice that for reasonably sparse datasets, say graphs with density around 1/10,000, one needs an higher than 10 to obtain a Jaccard Similarity of more than 50%. This result will be confirmed in Section 6 in our empirical analysis.

The previous Theorem allows us to derive the following. This means that, when the average user-degree is poly-logarithmic (or even m 0.99 ) we need ∈ Ω(log m) to achieve a constant Jaccard similarity with -edge differential privacy. It is well-known that many realworld matrix datasets are sparse. For instance in the context of real-world networks, classical theoretical models Albert and Barabási [2002] as well as empirical studies Backstrom et al. [2012], Leskovec et al. [2007] postulate constant average degree or degrees growing slower than the size of the graph.

The above results show that using randomized response, any differentially private approximation to a graph with high utility requires an exceptionally large value of , thus rendering void any privacy guarantees. Later in Theorem 4.3 we show a similar bound on for all differentially private algorithms. In fact, for such a high , the algorithm likely maintains the graph G unmodified thus exposing users to re-identification risks. For this reason we believe k-anonymity might in fact provide better protection in practice, especially in scenarios where our goal is to produce a private version of the input graph with high utility.

Unfortunately, however, all of the previous work Aggarwal et al. [2005], Kenig and Tassa [2012] provide non-trivial guarantees on the quality of a k-anonymous mechanism only when J(E, E Opt ) ≥ 1 -O( 1 log k ), in other words when very few edges need to be removed, as the similarity between the graph and the optimal k-anonymous graph is very high. By contrast, we show in Section 5 one can achieve a constant approximation to the optimal smooth-k-anonymous solution in less restrictive scenarios.

Hardness of Differential Privacy So far in this section we analyzed randomized response and show that this mechanism requires an unacceptably large . One may ask if there is any other -differential privacy mechanism with a small that guarantees the output to be similar to the input. The following theorem rules out the existence of such a mechanism. The proof of this theorem is presented in Appendix B.3. Theorem 4.3. Let M be an arbitrary mechanism that satisfies -edge differential privacy. Let α be a parameter such that for any input graph

## Comparison with k-anonymity by suppression

In this section we compare k-anonymity by suppression with smooth-k-anonymity. First, in terms of privacy, we notice that both smooth-k-anonymity and k-anonymity by suppression guarantee that every user in the output is indistinguishable from at least k-users. Moreover, observe that since smooth-k-anonymity is allowed to add edges to the output graph, an attacker would not be certain whether an edge was in the original graph or not.

We now show formally that the optimum solution of smooth-k-anonymity may preserve a significantly larger fraction of the input data than regular k-anonymity. To show this separation rigorously, we adopt the bipartite stochastic block model (SBM), which is commonly used in modeling applications, for instance in clustering and community detection Abbe [2017].

Bipartite Stochastic Block Model. To define the bipartite SBM, consider the following random process. We have two sets of n vertices, and each set is further decomposed into r blocks of size s, where r • s = n. Each block in the first part corresponds to one block of the second part. There is an edge between each pair of vertices in two corresponding blocks independently with probability q, and between every other pair of vertices with probability p. We let α = qs denote the expected number of edges that one node has to its corresponding block, a.k.a. internal edges. We let β = p(n -s) denote the expected number of edges that one node has to vertices other than its corresponding block, a.k.a. external edges. We refer to this as the stochastic block model with parameters r, s, α, β.

The result that we provide in this section is of particular interest when the blocks are not very sparse, i.e., α ∈ ω( log n log 1/q ) and α ∈ Ω(β + s). The next theorem upper bounds the number of edges in a (non-smooth) k-anonymous subgraph of a graph generated by the stochastic block model by O(n log n log 1/q ). Therefore, since α ∈ ω( log n log 1/q ), the fraction of remaining edges tends to zero. The proof of this theorem is presented in Appendix B.4.

Theorem 4.4. Let G be a graph generated by the stochastic block model with parameters r, s, α, β. Let k ≥ 2 log n log 1/q . With probability 99%, any k-anonymous subgraph of G contains at most 2 log n+10 log 1/q n ∈ Õ(n) edges. This allows us to show a gap with smooth-k-anonymization. In fact, a natural solution that puts the vertices of each block in a cluster leads to a solution for smooth-k-anonymity that in expectation keeps αn edges, adds (s -α)n edges, and removes βn edges. Since α ∈ Ω(β + s), the number of remaining edges αn is not less than a constant factor of the changed edges. This result concerns the optimum solution, but in the next section we provide an algorithm for computing smooth-k-anonymization of a graph.

# Algorithms and Analysis

In this section we develop algorithms that find a smooth-k-anonymization of G. We say an algorithm alg is α-approximation if J(E, E alg )/J(E, E Opt ) ≥ α, where E alg is the output of alg, E Opt is the optimal solution, and J(•, •) is the Jaccard similarity function. Our main contribution is captured by the following theorem.

Theorem 5.1. Assume J(E, E Opt ) ≥ 0.75. There exists an algorithm that finds a constant approximate smooth-k-anonymization of G in polynomial time.

At a high level, our algorithm will decompose users into clusters, each of size at least k. Then in each cluster c, for each item f , if the majority of the vertices in c have an edge to f , we add edges to f from all nodes in c; otherwise we remove edges to f from all nodes in c.

## Preliminaries

Let us start with some preliminary notions and lemmas. We will abuse notation slightly, and for a user u and item f , say u ∈ f if there is a (u, f ) edge in the graph.

Note that we can represent each user u with a point in a m dimensional space. For an item f i , we set the i-th dimension of u's representation to 1 if u ∈ f i and to 0 otherwise. In this space we define the distance of two points, u and v to be the number of positions where u and v differ (i.e. their Hamming distance).

Let ∆ Alg u be the number of positions that the algorithm Alg changes in the binary vector corresponding to the user u. Intuitively, u ∆ Opt u should be related to J(E, E Opt ). The following lemma formalizes this intuition.

All proofs from this section are in Appendix C.

To complement Lemma 5.2, the following lemma lower bounds J(E, E Alg ) given an upper bound on

## Initial algorithm

We now provide an approximation algorithm using a reduction to lower-bounded r-median1 . In the next subsection we improve it using a slightly more complicated algorithm.

In the lower-bounded r-median problem we are asked to select at most r centers from n points and assign each point to one center such that (i) the number of points assigned to each center is at least k, (ii) the total distance of the points from their assigned centers is minimized. We refer to each set of the points that are assigned to the same center as a cluster. In this paper we let r = n/k, which means that the algorithm may use as many centers as it needs, however, it must assign at least k points to each center2 . Here we use a 82.6 approximation algorithm for lower-bounded r-median Ahmadian and Swamy [2012], which is the best known result to the best of our knowledge. We refer to this algorithm as Alg 1 .

1. Embed each user in R m as described at the beginning of this section.

2. Approximately solve the lower-bounded r-median on the points (for r = n /k).

3. For each cluster c, for each item f , if most vertices in c have an edge to f , add all edges from nodes in c to f , otherwise remove all edges from nodes in c to f . Note that by definition of lower-bounded r-median, each cluster contains at least k points. Moreover, the data that we output for users that belong to the same cluster are the same. Hence, the output satisfies the anonymity part of the smooth-k-anonymity condition. Moreover, the output satisfies the majority part of the smooth-k-anonymity assumptions. Next we bound J(E, E Alg 1 ) assuming J(E, E Opt ) ≥ 1 -φ.

For analysis sake, we introduce the relaxed lower-bounded r-median problem in which we are allowed to select any possible discrete point in the space as a center (as opposed to being restricted to select centers only from the points that appear in the input). Note that, if we take a solution to relaxed lower-bounded r-median and move each center to its closest point (that appears in the input), by triangle inequality the cost of the solution increases by at most a factor 2. Therefore the cost of lower-bounded r-median is at most twice that of relaxed lower-bounded r-median.

By Lemma 5.2 we have u ∆ Opt u ≤ 2φ 1-φ |E|. We now prove there exists a solution to relaxed lower-bounded r-median with cost at most 2φ 1-φ |E|. Take an optimal anonymous solution and consider the equivalence classes of nodes with the same neighborhood. This induces a clustering of the nodes with clusters of size at least k. Now, observe that the total number of entries changed is equal to the sum of distances from the output neighborhood (of each class) and the original nodes. So this shows that there exists a clustering with sizes at least k with total cost u ∆ Opt u . Therefore, there exists a solution to lower-bounded r-median with cost at most 4φ 1-φ |E|. Note that we are using an 82.6-approximation algorithm to find lower-bounded r-median. Hence, the total cost of our solution is at most 330.4φ  1-φ |E|. The last line of the algorithm does not increase the total cost (since it selects the best center for each cluster). Hence we have u ∆

1-φ |E|. By applying this to Lemma 5.3 we have J(E, E Alg 1 ) ≥ 1 - 165.2φ  1-φ . This is a positive constant for any φ ≤ 0.006. This implies the following theorem.

Theorem 5.4. Assume J(E, E Opt ) ≥ 0.994. There exists an algorithm that finds a constant approximation smooth-k-anonymization of G in polynomial time.

Of course, having J(E, E Opt ) ≥ 0.994 is a very strong assumption. Next we substantially relax this requirement. .

## Improved algorithm

To prove a better algorithm we will use the 1.488 approximation algorithm for the metric facility location problem Li [2013] as a subroutine. In the metric facility location problem we are given a set of points and a set of facilities in a metric space, with an opening cost for each facility. The objective is to select a set of facilities and assign each point to a facility such that the total cost of the selected facilities plus the total distance of the points from their assigned facilities is minimized. Again here, we refer to the set of points assigned to each facility as a cluster. Below is our algorithm Alg 2 . This algorithm depends on a parameter α that we set later. 1. Embed each user in R m as before.

2. For each user u i define a facility with the same coordinates and opening cost 2α

where U k i is the set of k closest points to i. 3. Approximately solve the facility location instance. 4. Iteratively, remove each cluster with fewer than αk points and assign its points to their second closest facility.

5. Arbitrarily merge clusters with size less than k to reach size k, but do not let the clusters grow larger than 2k.3 6. For each cluster c, for each item f , if most vertices in c have an edge to f , add all edges from nodes in c to f , otherwise remove all edges from nodes in c to f . Theorem 5.5. Assume J(E, E Opt ) ≥ 0.75. Algorithm Alg 2 run with an α ∈ O(1) finds a constant approximation to smooth-k-anonymization of E in polynomial time.

The proof of the theorem is in Appendix 5.5.

# Experimental results

We give a brief overview of the empirical performance of our algorithms. We give the full details of the setup as well as additional empirical results in Appendix D. We will release an open-source version of our code by the camera-ready deadline.

Datasets We used representative examples of sparse binary matrices (and bipartite graphs) of different origins and structural properties. The scales of the datasets are up to > 1B rows, > 100k columns, > 10B entries (for our largest dataset) and the densities of the matrices range from 10 -5 to 0.1. We used one synthetic dataset, four publicly-available real-world datasets as well as one large-scale proprietary dataset from a major internet company. These are as follows: stochastic is generated from the stochastic block Metrics We measure utility using the Jaccard similarity between the set of the edges as defined in the paper as well as the number of suppressed entries and created entries.

Experimental infrastructure Our algorithm is implemented as a single-threaded C++ problem and is run on standard commodity hardware, with the exception of runs on the large-scale user-list dataset. For this dataset, we evaluated a simple heuristic to parallelize our algorithm. (See Appendix D for more details.)

Baselines and Algorithms As baselines we use the Mondrian anonymization algorithm LeFevre et al. [2006] implementation6 which enforces k-anonymity by suppression, as well as the randomized response algorithm of Section 4 which enforces edge-or node-differential privacy. We also compare our algorithm for smooth k-anonymization with an additional baseline non-smooth (which uses a simple heuristic to obtain (standard) k-anonymity by suppression using the clusters obtained by our algorithm). Our algorithm is always run with α = 1/2, which in practice gives good results for all datasets (we observe that values of α in [1/8, 1/2] have similar results).

Jaccard similarity vs k First, we evaluate the quality of our algorithm for smooth k-anonymity for different k values and we compare it with that of the (non-smooth) k-anonymity solution and mondrian. In Figures 3(a) and 3(b) we show a sample of plots of the mean Jaccard similarity for a given setting of the k parameter for smooth k-anonymity (solid line), non-smooth anonymity (dashed line) and mondrian (dotted). We were not able to run the mondrian algorithm on the larger datasets because, contrary to our algorithm, it scales with the size of the full n × m matrix size (m number of columns) and it does not exploit the sparsity of the matrix. As expected, the Jaccard similarity decreases with increasing k, but at every k level smooth k-anonymity allows to obtain significantly better results than all baselines (in some cases even twice better). We report more detailed results in Table 1 for k = 8. Notice that our smooth algorithm allows significantly higher jaccard similarity (and lower suppressed entries) for a small increase in created entries. For instance, in adult, the number of suppressed entries is decreased by ∼ 26% with just a ∼ 7% increase in added entries.

Differential privacy We now evaluate the Jaccard similarity obtained by the -differentially private method. We report the results in Figure 3(c). Here we report results for the lower protection level of -edge differential privacy, as -node differential privacy protection generates results close to random outputs. As expected (see Section 4) the sparser the dataset the worse the performance of differential privacy at parity of . Notice how to get Jaccard similarity above 0.5 in stanford or dblp, must be 10 which is too large to provide strong guarantees. We can use these results to compare k-anonymity and -differential from their a standpoint. We observe that depending on the dataset an anonymity of k = 16 might require an as large as 11 to obtain the same utility. Learning from anonymous data Finally, we report results on using the anonymized datasets in a downstream machine learning task. We use the anonymized version of the adult dataset to learn a classifier for the standard classification task of predicting whether an adult's income is ≥ $50k per year. The results are reported in Figure 4. Notice our algorithm performs better (or on par) with the best baseline (mondrian). We observe (see Appendix D) that smooth performs significantly better than the -node differentially private algorithm with = 10 even for k = 200, mirroring the degradation seen in the Jaccard similarity metric.

# Conclusion

We presented a new notion of anonymity which relaxes standard k-anonymity and allows us to obtain better guarantees and improved results in downstream machine learning tasks. Our algorithms reduce the anonymization problem to clustering with lower bounds and require non-trivial analysis to prove approximation guarantees. Many interesting questions remain, including strengthening our bounds for smooth k-anonymity and better understanding the interplay between the various notions of privacy.

# A Technical lemma

Proof. From the condition on x it follows that b -x > 0. Therefore rearranging terms in (1) yields the equivalent inequality:

This inequality holds if and only if x < b-a 2 .

B Omitted proofs from Section 4

# B.1 Randomized response is -differentially private

Consider the following procedure. For each element, with probability 1 -2 e +1 we report the true value, otherwise with probability 1 e +1 we report 0 and with probability 1 e +1 we report 1. We refer to this procedure as -DP. Next theorem shows that this procedure is -differentially private.

Theorem B.1. -DP preserves edge differential privacy.

Proof. Let G and G be two arbitrary graphs that only differ in one edge e, and let G and G be the outcomes of -DP on G and G respectively. Let S be a collection of graphs, and let H be an arbitrary graph in S.First we consider the case that e ∈ G and e ∈ H. Then, we consider the case that e / ∈ G and e ∈ H. The same argument holds for the other two possibilities.

Let P -e (G , H) be the probability that G -{e} = H -{e}, i.e., ignoring edge e all of their other edges match. Similarly, let P -e (G , H) be the probability that G -{e} = H -{e}. Note that G and G only defer on edge e. Hence, we have P -e (G , H) = P -e (G , H). We have If p 4 ≥ C(δ) Q , then with probability at least 1 -δ:

where λ := λ(G).

Proof. Let E denote the edge set of the output graph. By definition of the mechanism, each edge on E is preserved with probability 1 -p + 1 2 p = 1 -p 2 . Thus, we have

. By Hoeffding's inequality we know with probability at least 1 -δ 2 :

Similarly an edge not in E is added to E with probability p 2 . Thus we have

Z j where Z j ∼ Bin p 2 . Thus, by Hoeffding's inequality we have that with probability at least 1 -

By the union bound, and rearranging terms we thus have that with probability at least 1 -δ

where we have used Lemma A.1 in the Appendix for the last inequality. The results follow by dividing the numerator and denominator by λ and using the definition of p.

# B.3 Hardness of differential privacy

Theorem B.3 (Restatement of Theorem 4.3). Let M be an arbitrary mechanism that satisfies -edge differential privacy. Let α be a parameter such that for any input graph

Proof. To prove this first we define a policy M(G) based on M(G), such that M(G) is

• an -differentially private mechanism,

• E[J(G, M(G))] ≥ α 2 , when |G| ≥ l = (nm) 0.9 , and

The third property bounds the range of |M(G)| and allows us to analyze M(G) and bound . We define policy M(G) based on M(G) as follows:

Note that M(G) can be exactly calculated given M(G), hence M(G) is an -differentially private policy as well. Moreover, note that when

Hence, for a graph G with |G| ≤ l + 1 we have

Consider the following two equivalent random processes to construct random graphs G = (U ∪ F, E) and G = (U ∪ F, E ).

• Select l pairs of nodes from U × F uniformly at random without replacement. Add an edge between each selected pair in both D and D . Select one other pair of nodes from U × F uniformly at random without replacement, denote it as (u, f ), and add an edge between u and f in D .

• Select l + 1 pairs of nodes from U × F uniformly at random without replacement. Add an edge between each selected pair in both D and D . Select one of the edges in D uniformly at random, denote it as (u, f ), and remove it from D.

Note that, G is a graph chosen uniformly at random from all graphs on U × F with l edges, and G is a graph chosen uniformly at random from all graphs on U × F with l + 1 edges. Moreover, (u, f ) is both an edge selected uniformly at random from the edges inside G and it is an edge selected uniformly at random from the edges that are not in G.

Recall that, by definition, we have

Note that, if we select one of the edges of G uniformly at random, it exists in M(G ) with probability at least

Hence, we have (u, f ) ∈ M(G ) with probability at least α 2 . Let S be the set of all possible outputs of M(G ) where the (u, f ) ∈ M(G ). By the definition of differential privacy we have

This means that (u, f ) ∈ M(G) with probability at least αe - 2 . Recall that, by definition (u, f ) is an edge chosen uniformly at random from the edges that do not exist in G. Hence, if we select one of the edges that do not exist in G, it exists in M(G) with probability at least αe - 2 . On the other hand, similar to G , if we select one of the edges of G uniformly at random, it exists in M(G) with probability at least α 2 . Hence, we have

Recall that by construction we have |M(G)| ≤ 2(l+1) α . This together with the above inequality gives us nmαe - 2 ≤ 2(l+1) α . This implies ≥ log α 2 nm 4(l+1) ∈ Ω log(α 2 nm) , as claimed.

# B.4 Utility of k-anonymity by suppression in the stochastic block model

Theorem B.4 (Restatement of Theorem 4.4). Let G be a graph generated by the stochastic block model with parameters r, s, α, β. Let k ≥ 2 log n log 1/q . With probability 99%, any k-anonymous subgraph of G contains at most

. Fix a subset of size k of vertices in the first part and a subset of size t in the second part. Recall that the probability that we have an edge between a pair of vertices is either p or q, where p ≤ q, and each edge exists independently. Hence, the probability that all of the edges between a certain set of vertices of size k and a certain set of vertices of size t exist is at most q kt . On the other hand there are k n • t n such a pair of sets. Therefore, by union bound, the probability that there exists a set of vertices of Proof. Svitkina Svitkina [2010] showed that Lines 2 to 5 gives solution in which (i) the size of each cluster is at least αk, and (ii) the cost of the solution is at most 1.488 • 1+α 1-α times that of lower-bounded r-median. Similar to our previous algorithm, since the size of each cluster is at least k, the last line of the algorithm guarantees smooth-k-anonymity. Next we bound J(E, E Alg 2 ) assuming J(E, E Opt ) ≤ 1 -φ. We refer to the first four lines of algorithm Alg 2 as Alg 2 . Similar to the previous subsection we know that there exists a solution to lower-bounded r-median with cost at most 4φ 1-φ |E|. Therefore the cost of the solution to the facility location problem is at most

Again similar to the previous subsection and by applying Lemma 5.3 we have

Later we show that Line 5 decreases the Jaccard similarity by at most a factor α 2 8 . Hence we have

which is a positive constant for φ ≤ 0.25 and α = 0.004. This implies Theorem 5.5. New we show that Line 5 decreases the Jaccard similarity by a factor of at least α 2 8 . To prove this, we use the probabilistic method. For each cluster we show a random point such that if we move the points in each cluster to its corresponding random point, the expected Jaccard similarity is at least α 2 8 times that of the initial Jaccard similarity. This implies that there exists a fixed (i.e., deterministic) set of points such that if we move the points in each cluster to its corresponding fixed point, the expected Jaccard similarity is at least α 2 8 times that of the initial Jaccard similarity. Note that, for each cluster, we are selecting the optimum center, and hence this statement holds for our selected centers as well.

Let E init be the edge set corresponding to the clustering prior to Line 5. For each merged cluster we select the center of one of its initial clusters uniformly at random. Note that each merged cluster contains at most 2/α initial clusters. we select the center of each initial cluster with probability at least α/2. This means that each edge that exists in E ∩ E init exists after merging the clusters with probability at least α/2. Hence, the expected number edges that exists after merging is at least α 2 |E ∩ E init |. Moreover, the number of nodes in each initial cluster is at most αk 2k fraction of that of the merged cluster. Hence, the total number of edges increases by a factor of at most 2/α after merging and moving the point to the random centers. Hence, the expected Jaccard similarity after the merge is at least

as claimed. This completes the proof of Theorem 5.5.

# D Additional material from the experimental section

Description of the datasets We now report a more detailed description of the datasets used. Some key properties of the datasets are shown in Table 2. stochastic is generated from the stochastic block model described in Section 4.2 with n = 1024 rows and columns, and parameters s = 64, q = 0.8, p = 0.01. adult is a dataset from UCI7 from the US census used in many anonymization and differential privacy papers LeFevre et al. [2006]. We use all categorical features represented as a binary vector. playstore8 consists of a bipartite graph representing features of user's devices  [2015] consists of a co-authorship graph. In graph adjacency form, rows and columns represent authors in computer science and an entry (i, j) is 1 iff i and j co-authored a paper. stanford Leskovec et al. [2009] consists of a directed web graph, where rows and columns represent web pages crawled from the Stanford website. An entry (i, j) is 1 iff page i has a hyperlink to page j. user-lists is a proprietary dataset from a major internet company containing user-interest relationships. Each row represents a user, and the columns represent the inclusion in a given marketing interest list.

Metrics Our utility goal is to preserve as accurately as possible the input, to do so we use the Jaccard similarity between the set of the edges as utility metric as defined in the paper. To measure the distortion incurred by the data we also use other standard anonymity quality metrics, including the number of suppressed entries and created entries. We note that for binary data other metrics such as the normalized certainty penalty LeFevre et al. [2006] used for hierarchical features are not relevant.

Experimental infrastructure We implemented our algorithm using C++. For all execution of an experiment (except for the large-scale user-list dataset) we use a single-thread program run on standard commodity hardware. All experiments terminated within 3 hours. We repeat each run of an algorithm with a given setting 10 times and report mean and deviation metrics. For our user-list dataset with more than a billion rows, we evaluated a simple heuristic to parallelize the computation of our algorithm. We split the dataset in chunks of order of 10 5 rows by using a Locality Sentitive Hashing technique (LSH) Wang et al. [2014]. More precisely, for each row we compute 8 independent min hash LSHs (over the set of columns with 1) and sort the rows of the dataset by the lexicographical order of their min hashes. This is similar to the shingle sorting technique Chierichetti et al. [2009]. We then obtain the chunks by approximately dividing this sequence of elements in consecutive intervals of size 10 5 . Then we ran our algorithm independently on each chunk of the dataset and combined the solution. Our results (reported in Fig 3 (b)) show that this simple heuristic is quite effective.

Baselines We compare our algorithm with the well-known mondrian anonymization algorithm LeFevre et al. [2006], using an open source implementation 9 which enforces k-anonymity by suppression. The algorithm doesn't have parameters to tune (expect k).

Our algorithm has theoretical guarantees for smooth k-anonymization, but it can be easily used as an heuristic for (standard) k-anonymity by suppression (in the last step, the clusters are simply anonymized by computing the intersection of all binary vectors), so we report results for non-smooth k-anonymity using our algorithm as an additional baseline.

Implementation details For efficiency we made small changes to the implementation of the algorithm in Section 5.3 that we now summarize. In step (2) we slightly modify the formula for obtaining the best empirical results. Similarly to the bicriteria algorithm of Svitkina [2010], we add a parameter β > 1, set α = 1/β, and define for a point u i the cost of the facility as  βk closest point to i. In our experiments, β = 2 (i.e. α = 1/2) was the best performing setting and we report experiments with that value only (results with 2 ≤ β ≤ 8 are very similar). In step 3, we solve the facility location problem efficiently by running the well-known Meyerson's algorithm Meyerson [2001] 10 different times on a random ordering of the data points and selecting the best solution (in this setting the algorithm is known to be a constant factor approximation Fotakis [2011] in expectation). Finally, in steps 4 and 5, we replace the procedure described in the paper, with a simpler one where we simply close facilities that have fewer than k clients in arbitrary order and reassign all clients to the nearest open one until all clusters are large enough.

Jaccard similarity vs k First, we evaluate the quality of our algorithm for smooth k-anonymity for different k values and we compare it with that of the (non-smooth) k-anonymity solution and mondrian. In Figures 5(a), 5(b), 5(c), 5(d) as well as Figures 3(a) and 3(b) we plot the mean Jaccard similarity for a given setting of the k parameter for our datasets for both smooth k-anonymity (solid line), non-smooth anonymity (dashed line) and mondrian (dotted). We were not able to run the mondrian algorithm on the larger datasets (dblp, stanford, user-list) as this algorithm (contrary to ours) scales with the size of the full n × m matrix where m is the number of columns of the dataset (while our algorithm can exploit the sparsity of the matrix).

From the pictures, it is possible to observe that, as expected, the Jaccard similarity decreases with increasing k, but at every k level smooth k-anonymity allows to obtain significantly better results than all baselines. For instance, for playstore we observe 2× higher Jaccard similarity for k = 32 than with the best baseline. Among the baselines, interestingly we see that non-smooth anonymity despite using our algorithm which is not optimized for anonymity by suppression can perform better than mondrian which is optimize for that task, in particular for lower k values. For large k values in Figure 3(a) mondrian performs better but still is outperformed by smooth anonymity.

The level of Jaccard similarity at a given k is, as expected, dependent on the structure of the graph. We observe for instance higher similarity at large k values for stochastic, adult, playstore dataset than dblp. This can be easily explained by the nature of the datasets: for adult, stochastic, playstore, the rows represent comparably dense features; while for dblp each row represent a quite sparse and somewhat unique feature set (i.e., the co-authors of a researcher). Interestingly, the algorithm performs much better on the stanford dataset than the dblp one, this can be explained with previous observations on social networks showing higher  . entropy than web graphs Chierichetti et al. [2009]. Notice also how our heuristic algorithm for the large-scale dataset obtains performances (Figure 3(b)) comparable to the best datasets. We observe that the results are very concentrated, in fact, the maximum standard deviation observed for any k value in [2,64] for our smooth (non-smooth) k-anonymity algorithm is 0.7%, 1.3%, 0.5%, 1.3% (1.8%, 2.2%, 0.2%, 0.8%) for adult, playstore, dblp, stanford, respectively.

Trade-off between suppressed entries and created entries We report an extended version of Table 1 in Table 3.

Additional results for differential privacy All results in our experiments with differential privacy in Figure 3(c) are very concentrated around the mean with maximum standard deviation for any of 1.02%, 0.09%, 0.15%, 0.05%, 0.04% for stochastic, adult, playstore, dblp and stanford, respectively.    Comparison between k-anonymity and differential privacy We can use the results of the previous evaluation to compare the two approaches. Notice that k-anonymity and -differential privacy provide mathematically incomparable privacy guarantees; but we can compare the utility of both for different settings of their parameters k or . This is what we do in Figure 6 where we report for each dataset and value of k for smooth k-anonymity and parameter than will result in the same average Jaccard similarity for edge differential privacy protection. Notice how, depending on the dataset, an anonymity level of k = 16 might require an as large as 11 to obtain the same utility even for the lower level of guarantee of edge differential privacy. For the denser datasets like adult and playstore, values of anonymity between k = 4 and k = 64 correspond to the performance of ∼ 4 ≤ ≤∼ 5.

Learning from anonymous data Finally, we report results on using the anonymized datasets in a downstream machine learning task. For the adult dataset we train a neural net classifier for the standard classification task for this dataset of predicting whether the income of the entry point is >= $50k per year. For all methods, we only anonymize the features not the labels and we train the model on the anonymized features in output from the algorithms and report the prediction on the original test dataset. We use a 1-layer, 10-hidden unit network with RELU activation nodes.

The results are reported in Figure 4 for the anonymization methods and in Figure 7(a) for the -node differentially private method. The shades represent the 95% confidence interval. Notice that our algorithm reports results better (or on par) with the best baseline (mondrian) and significantly better than the -node differentially private algorithm with = 10 even for k = 200. We also observe that our smooth algorithm has lower variance in the output than the mondrian one. This confirms that our algorithm outperforms all baselines also in producing outputs useful for machine learning analysis.

# C.3 Proof of the main theorem

Theorem C.3 (Restatement of Theorem 5.5). Assume J(E, E Opt ) ≥ 0.75. There exists an algorithm that finds a constant approximation to smooth-k-anonymization of E in polynomial time.

