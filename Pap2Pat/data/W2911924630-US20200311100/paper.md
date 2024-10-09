# I. INTRODUCTION

Real-world data is often very high dimensional and hence not visualizable. The Mapper algorithm, developed in [Singh et al., 2007], is a method to visualize such data in low dimensions while trying to remain true to the topological structure of data in the higher dimension. The algorithm returns a simplicial complex 1 which is a representation of data via a far less number of nodes than the number of data points. Through this visualization, it becomes convenient to gain insights from data.

The Mapper algorithm begins by applying a function f : X → Z on the input space X. The resulting lower dimensional image space Z is covered by a set of bins that overlap each other, with every part of Z included in at least one bin. Then, a clustering algorithm is applied within the f -1 of each bin. *This work was completed during internship at Adobe Systems, Noida. This paper was accepted at ICDMW 1 [Hatcher, 2002] provides a rigorous mathematical treatment of simplicial complexes.

The nerve of these set of clusters, computed as in II, is called Mapper. The Mapper restricted to only its nodes and edges is called the Mapper graph. Although the Mapper algorithm has been highly successful, it is difficult to work with due to a large number of parameters involved in the choices of lens function, type of cover and clustering algorithm. [Carriere et al., 2018] have studied parameter selection in the case where Z = R. They prove that in the 1dimensional setup, the Mapper graph statistically converges to a geometric structure called the Reeb graph, which encodes the topological information of the original space. This, in turn, gives a method to tune its parameters to best approximate the Reeb graph. Even with best parameters Mapper provides a visualization of data at a fixed scale at which the cover was constructed. Since our input space is a high dimensional discrete point cloud and not a continuous space, the best parameters still provide an approximation to its topology and it is possible that more insights are available when data is viewed at different scales. [Dey et al., 2016] address this issue by proposing Multiscale Mapper, where data is seen along a tower of covers. But still, each cover in the tower is at a scale which views all parts of the data through the same lens irrespective of the data distribution being different in different regions. In this paper, we propose an algorithm which allows us to view denser and sparser parts of the data at separate scales in the same visualization. This, unlike the current Mapper algorithm, is not restricted to one global scale; hence, it prevents the shattering of sparser data subsets under finer scales that are suitable for denser data subsets. Further taking inspiration from [Munch and Wang, 2016], [Carriere et al., 2018] we can characterize the output of Mapper (with lens function f ) as good when it approximates the Reeb space (a generalisation of the Reeb graph in higher dimensions) under f .

## A. Contributions

The main contributions of this paper are as follows: In II, we first briefly introduce the mathematical notions behind Mapper and then discuss our contributions towards improvement on Mapper algorithm. We have implemented all our experiments using 2-dimensional lens function; however, a vast majority of it is generalizable to higher dimensions. Since R-valued lens functions limit the topological information to only edges; it is more informative to use higher dimensional lens function. But in dimensions greater than 3, we get higher-order simplices that are hard to visualize, so we restrict ourselves to 2 dimensions. In this paper, we shall refer to the individual elements of open cover as bins. We can conceptualize covering as putting each element in one or more of these bins.

### II. THEORETICAL BACKGROUND

Definition 2. A k-simplex is the smallest convex set containing a given set of k + 1 affinely independent points, where u 0 , u 1 , . . . , u k are called affinely independent if u 1 -u 0 , u 2u 0 , . . . , u k -u 0 are linearly independent. Definition 3. An m-simplex σ is said to be an m-face of a k-simplex σ if m < k and the vertices of σ are a proper subset of the vertices of σ. Definition 4. A simplicial complex K is a set of simplices such that:

• A face of a simplex from K is also in K • ∀σ 1 , σ 2 ∈ K, σ 1 ∩ σ 2 is a face of both σ 1 and σ 2

For an example, 1-simplex is a line segment, 2-simplex a triangle, 3 simplex a tetrahedron and so on. And for a 3simplex (tetrahedron), 0-faces are its vertices, 1-faces are its edges, and 2-faces are its triangular sides.

Definition 5. Given a cover U of a space X, the nerve N (U) is a simplicial complex constructed as follows:

• The vertices (nodes) of N (U) correspond to bins of U • For each k + 1 bins of U that have mutual non-empty intersection in X, N (U) contains a k-simplex with the corresponding nodes as its vertices.

The Mapper algorithm is motivated by the Nerve Theorem [Hatcher, 2002, Corollary 4G.3], originally proposed by Pavel Alexandrov.

Theorem 1 (Nerve Theorem). If U is an open cover of a paracompact space X such that every non-empty intersection of finitely many sets in U is contractible, then X is homotopy equivalent to the nerve N (U).

An intersection being contractible intuitively means that we should be able to continuously shrink it to a point in X. Finally, homotopy equivalent is a mathematical notion of the shape being similar -which tells us that if the required conditions are satisfied, then the nerve would give us the shape of X itself.

In the context of data analysis, we work with a point cloud lying in R n n ∈ N , which is a metric space. Every metric space is paracompact as proved in [Steen et al., 1978], hence the assumption of paracompact space is satisfied in our case. We can compute topological properties of point cloud by assuming that it is sampled from a paracompact space in R n which we refer to as X.

Mapper Algorithm: based on these ideas, the algorithm works as follows:

1) Given a point cloud X, we project it onto a lower dimension space Z by a lens function f . We create a cover U on the image. The pre-image of each bin under f then gives us a cover f -1 (U) of X:

2) We obtain a modified pullback cover f * (U) of X from the bins of f -1 (U). The pullback of U under f is defined as

where P(V ) is the set of path connected components of V . In the discrete setting, path connected components are approximated by clusters. Hence in practice, we obtain f * (U) by clustering within each bin of f -1 (U).

3) We compute the nerve of f * (U) in X. This nerve is the Mapper M (X, U, f ) of X.

# Thus

Definition 6. Given a space X, a lens function f , and a cover U of f (X), the Mapper is defined as

The 1-skeleton of Mapper is a graph consisting of simplices till 1 dimension from Mapper. Hereafter we shall omit X, U, f wherever they are clear from context.

Mapper has been applied in a wide range of usecases to get useful insights. The data analytics company Ayasdi have extensively used TDA to provide solutions in various fields [Ayasdi, 2018], like finance [Ayasdi, 2016], healthcare [Ayasdi, 2015], sports [Beckham, 2012] and machine learning [Ayasdi, 2017]. [Kamruzzaman et al., 2016] have used Mapper to study environmental stressors on plant phenotypes. [Vejdemo-Johansson et al., 2012] have used Mapper to identify voting patterns in the US House of Representatives, and have comparatively presented a marked improvement on the classification possible compared to Principal Component Analysis [Pearson, 1901]. However, the parameters in Mapper, i.e. f (lens function), r (bin diameter) and g (bin overlap) require tuning by trial and error, and hence involve some implicit knowledge of the data. Moreover, once the Mapper graph is obtained, insight mining is primarily done by human intervention. These are significant roadblocks in the goal of using Mapper to gain insights from truly unsupervised big data. We have made progress in automating these processes. Our work results from [Dey et al., 2016], who introduced and significantly developed the notion of Multiscale Mapper. This technique is based on building a tower of covers of various scales, and studying the variations in the resulting tower of nerves. Below, we define Multiscale Mapper and related terminology as presented in [Dey et al., 2016].

. By abuse of notation, ξ also represents the induced map U → V. Definition 9. A tower W where the objects W ε are covers and the maps w ε,ε are maps of covers, W is called a tower of covers.

Definition 10. Given two simplicial complexes K, L, a simplicial map from K to L is a map ξ : K → L such that:

Note that if ξ is not injective on vertices, then a k-simplex might map to a k -simplex, k < k. Definition 11. A tower W where the objects W ε are simplical complexes and the maps w ε,ε are simplicial maps, W is called a tower of simplicial complexes.

Definition 12. Given a space X, lens function f , and a tower of covers

As in the case of Mapper, we omit X, U, f from notation wherever it is clear from context. The following facts establish that the successive relationship between covers of f (X) in U naturally corresponds to a successive relationship of Mappers within MM(U).

. Thus a tower of covers induces a corresponding tower of simplicial complexes i.e. the nerves of each cover.

• A map of covers ξ : U → V induces a map of covers between their respective pullbacks under a function f

Definition 13. The pullback under f : X → Z of a tower of covers U = {U ε } ε of Z is defined as

and is itself a valid tower of covers via the induced maps.

## III. A SELECTIVE MAGNIFICATION SCHEME -MULTIMAPPER

It is possible, and we have seen in experiments, that the same cover might not be ideal for every part of the data. For example, in Fig. 1, the coarsest refinement hides local structure that appears at finer scales, but the graph also begins to break into more components, which obscures global relationships between the data in each component. To solve this issue, we have developed a technique which takes the locally best scale for each region of the data, and glues them together to represent the entire data more accurately than a single global scale. For scale selection, we use the notion of Multiscale Mapper. However, the varying scales in Multiscale Mapper is applied globally, which means that two regions with different density would not be appropriately represented at any one level. Therefore we propose a Mapper graph which is an amalgamation of Mapper graphs computed on various regions of interest. We apply Multiscale Mapper on each region of interest as a way of selecting scales. It is a different question to identify these regions and the appropriate scale of its cover in the first place -we discuss a possible approach in IV using the idea of Multiscale Mapper.

To consistently combine the locally suitable Mappers, we implement our idea as a repeated rescaling of selected regions.

Intuitively it can be understood as magnification/compression of a Mapper in relatively sparser/denser regions respectively. Our first approach slices relevant bins of the cover to obtain smaller bins; our second approach is more sophisticated and uses a nerve-like computation to glue together various locally suitable Mappers. The latter has the advantage of being compatible with all covering schemes, including the brick-like cover proposed in V.

## A. Local Refinement via Cover Slicing

The covering process can be broken into two parts, deciding the type of partition and then overlap percentage. Our aim in this section is to modify the underlying partition in a manner that the required regions are covered by smaller bins than before. Once we have identified regions in the Mapper M that are to be magnified, we perform the steps below. It is specifically illustrated using cuboidal bins, but can be generalized to other shapes by redefining the chopping in Step 3.

1) Let S be the set of nodes we wish to magnify; X be the region of the original data corresponding to these nodes, i.e.

where C w is the cluster corresponding to a node w. 2) Now we look at the image of X under the original lens function f , i.e. Z = f ( X) (8)

3) P be the partition of the image, Z = f (X), that gave rise to the Mapper M . Then define a subset:

i.e. those parts of the partition which contain some part of Z. 

M thus shows the data corresponding to Z M , and the remaining parts of the data at the same scale as M . This process can be repeated at various regions of the data to view each region at a suitable scale.

## B. Handling Degeneracy via Multimapper

A major drawback of the previous approach is degeneracy of f i.e. f may map distant parts of X very closely, in the image Z. Hence, if we magnify a region X in the above method, since we go via its image Z, we would actually magnify f -1 ( Z) = f -1 (f ( X)), which is potentially a larger region and having other parts distant from X. Hence undesirable parts of the Mapper would be magnified as well. We wish to avoid this effect of f ; but we want to retain the convenience of constructing the cover via pullback under f . Moreover, we Fig. 2: Original bins sliced to obtain smaller bins. As shown here, the process can be repeated. would want to not only zoom in on denser parts, but zoom out on sparser parts that might have shattered. Our one-shot solution to these requirements is the notion of Multimapper. Multimapper is constructed as follows:

1) As before, given a Mapper graph M , with nodes V and some nodes S to be magnified, we identify the corresponding data subset and image subset:

where C w is the cluster corresponding to a node w. 2) Let C be the set of clusters corresponding to the nodes of M . The region we want to 'preserve at original scale', i.e. not magnify, is:

From this we discard those clusters which lie entirely in X to obtain:

3) We define a new cover on Z as per our choice and requirement. Unlike in III-A, this need not be a restriction of the old cover of Z. 4) We cluster within the inverse images of each new bin, to obtain a new set of clusters C, such that:

Effectively, it is again a Mapper construction restricted on X with a new cover on Z. 5) Now we have obtained an overall set of clusters

We compute a new nerve M according to Ĉ: the nodes correspond to clusters in Ĉ, and a k-simplex is added for every k + 1 clusters of Ĉ that have a simultaneous intersection. This nerve-like computation ensures that M :

• matches M on V \ S, via nerve computation on C

• replaces the induced sub-complex on S with a copy of M , via nerve computation on C

• glues these two parts in a manner faithful to the topology of X, by imitating the nerve construction on simultaneous intersections involving both C and C

The above process can be repeated at various regions, with locally suitable choices of covering scheme, bin size, and clustering algorithm. The resulting structure is a Mapper-like simplicial complex which we call Multimapper.

Conceptually, Multimapper breaks up the original point cloud into subsets that may or may not intersect. For each region, it computes the Mapper that is of a suitable scale for that region.

Definition 14 (Multimapper). Given a finite collection of subsets X ⊂ 2 X such that ∪ Y ∈X Y = X and covers {U Y } Y ∈X such that ∀Y ∈ X , U Y ⊇ Y , we can define the corresponding Multimapper:

This piecewise approach makes Multimapper quite flexible, we can freely choose different local Mappers for different regions, while retaining the global relationships between them. Fig. 3(b) shows an example of applying Multimapper on a specific region of dataset. Fig. 3(c) shows the graph obtained by applying Multimapper repeatedly on separate regions and creating a single visualization by gluing them all. We can see it reveals new structure in the magnified regions as well as prevents the shattering of graph which was happening in case of Mapper with similar bin size as can be seen in Fig. 1(c). Via the stability results in [Dey et al., 2016], we further know that Multimapper is locally as stable as Multiscale Mapper; and of course, since it after all arises from a cover, it is globally as stable as Mapper.

IV. DETECTING A BAD MAPPER [Singh et al., 2007] refer to the Reeb graph as a geometric representation suitable for obtaining information directly, and introduce Mapper as a generalization of Reeb graph. Later, [Carriere et al., 2018] have shown that in the ideal setup, Mapper with a 1-dimensional lens function statistically converges to the Reeb graph of the original space under the lens function. A general convergence result of Mapper to a generalization of Reeb graph called the Reeb space has been conjectured, and [Munch and Wang, 2016] have studied a category-theoretic version of this relationship. The ideal convergence would not occur in case of real data since real data is a discrete point cloud. However, we can measure the correctness of a Mapper via its closeness to the Reeb space. We can thus reasonably demand that a good enough Mapper of a discrete point cloud, under a particular lens function f , should be similar in shape to the Reeb space (under f ) of the connected paracompact space it approximates.

Definition 15 (Reeb space). Given a continuous map f : X → Y between topological spaces X and Y , the Reeb space R f (X) of X with respect to f is X/ ∼ where the equivalence relation ∼ on X is defined as p ∼ q iff p and q lie in the same connected component of f -1 (c) for some c ∈ Y .

When Y = R n , the connected components are same as path connected components [Sutherland, 2009], and this is sufficient for our real-world setting. When Y = R, the Reeb space is called the Reeb graph.

The Mapper algorithm is constructed using the Nerve Theorem, and we have characterized its goodness by its closeness to the Reeb space. Thus, to partially characterize bad Mappers i.e. Mappers far from the Reeb space, we can try to find regions of the Mapper where the contractibility hypotheses of Nerve Theorem is violated. Checking for contractibility, however, is complicated in a real  world setting, especially since our actual space is a point cloud. To adapt our method to the real world, let us recall the association between the continuous and discrete ideas:

We know that if a space has more than one path connected component, it cannot be contractible -shrinking two separate pieces to the same point would require shrinking across the gap between them, which violates continuity. Translated to the point cloud setting, this means that if a data subset has multiple clusters, the corresponding space cannot be contractible. Hence, a sufficient condition for non-contractibility can be checked using the following general characterization: Given a Mapper on a set of nodes

where:

• σ(S) is the simplex on the vertices S • For some topological space A, β 0 (A) is the number of connected components in A • C v is the cluster corresponding to the node v of the nerve. This motivates our approach, which we illustrate via 1simplices (edges). However, the same technique can be iterated over all simplices in M . The most naive approach of identifying components in discrete setting is via any known clustering algorithms. We propose such a method next, followed by a modification on it that is independent of clustering algorithms.

## Clustering-Dependent Version

Procedure: Given a Mapper M , for each edge (u, v), C u ∩ C v = ∅, we cluster within C u ∩ C v using a clustering algorithm like DBSCAN which does not fix the number of clusters a priori. If more than one cluster is obtained, we report it as a violation. Finding even a single violation is sufficient for the Mapper to be classified as bad. A. Our Algorithm: Clustering-Independent Version

In the above naive approach, we depend on clustering to approximate path connected components. Thus we are constrained by the choice of clustering algorithm and its parameters, and must optimize this on a case-by-case basis as these are not generalizable to any dataset. To remove this dependency, we propose a method of approximating path connected components that is independent of clustering. The well-known TDA method of persistence, which is usually applied directly on the point cloud [Ghrist, 2008], can be translated to the Mapper setting via Multiscale Mapper - [Dey et al., 2016] have given an algorithm that, given a tower of covers, computes the persistence diagram of the resulting Multiscale Mapper. They have also provided an approximate computation suitable for the discrete point cloud setting. Hence, given U = {U ε } ε , a Multiscale Mapper MM(U) and a void H that appears in some M (U ε ) ∈ MM(U)

Hence, for every 0-void, i.e. connected component, 1-void, i.e. circular hole and so on, that appears in MM(U), we get a birth-death pair, a range of scales at which it is visible in the corresponding Mappers. We consider a topological feature, e.g. a void, to be truly present in the shape of the data if it remains, or is persistent, for a large range of scales. If has cuboidal 2 bins of diameter ε 0 and U must be finite, we define covers of the form U ε of f (X) to have the same partition rule as U, but with bin size ε. Thus the tower of covers of f (C u ∩ C v ) is:

From this we obtain the pullback tower f * (U ) of covers of C u ∩ C v . On this, using persistence via Multiscale Mapper as illustrated in [Dey et al., 2016], we can compute β 0 , the persistence and hence true number of components. If β 0 > 1, we report a violation. To increase efficiency in implementation, we will compute only zeroth dimension persistence diagram.

V. REDUCING OBSCURED INFORMATION VIA BRICK-LIKE COVER Construction of a cover from the implementation perspective for the Mapper algorithm can be conceptualized in two steps:

1) Construction of a partition 2) Growing each piece of the partition to introduce overlap, hence obtaining bins. The most well-known, standard box-like cover partitions the image space into n-cuboids, where n is the projected dimension. Hence with a 1-dimensional lens, we get line segments; with a 2-dimensional lens, we get rectangular boxes; and so on. In such a setup, 2 n bins can intersect where 2 n pieces of the partition meet; hence simplices in the nerve can have dimension up to 2 n . However, simplices of dimension > 2 are difficult to visualize. Because of this, the visualization we create will be truncated at 2or 3-simplices, and not represent the complete information contained in the Mapper. Hence, it would be desirable to build covers such that the visualization represents all the topological information contained in Mapper through simplices of visualizable dimensions. This requires us to explore non-cuboidal lattices for the partition. As suggested in [Singh et al., 2007], hexagonal lattices are a natural choice -in 2D, for example, hexagonal bins can intersect only 3 at a time; hence the Mapper would have at most 2-simplices.

2 Cuboidal bins may be arranged in the standard way or as suggested in V. 

## The Brick Cover

Constructing bins over a hexagonal lattice is computationally difficult even in 2 dimensions. Our proposed 2D covering is more efficient and achieves the same goal with a few realistic constraints. Our partition of the 2D plane uses offset rectangles, as in a brick wall. The underlying vertices are still a hexagonal lattice, which gives us an advantage over the usual rectangles: at most 3 bricks can meet at a vertex. At overlap below 50%, this translates to a maximum of 3-fold intersection of bins. Given the sparse nature of high-dimensional data, overlap below 50% is a reasonable notion of nearness. The idea of using non-cuboidal bins can be extended to higher dimensions: for example, cuboidal lattice in 3D gives up to 8fold intersections, while hexagonal lattice in 3D gives only up to 6-fold intersections. We claim that our proposed bricklike cover gives the lowest possible maximum simultaneous intersections among all 2D covers that use cuboidal bins. This is because:

1) For the underlying partition of a cuboidal cover, let a 'mesh point' be a point at which some pieces of the partition meet, and at least one piece has that point as a vertex. At a mesh point:

• The total angle contributed by pieces incident on it must equal 2π. • A piece having the mesh point as its own vertex, contributes π/2, other surrounding pieces contribute π. Hence 2 pieces cannot form a mesh point, since neither piece could have the said point as its own vertex.

• Thus, at a minimum, we are forced to build 2π as π + π/2 + π/2, as in a brick-like mesh.

2) We are left to choose the 'offset', i.e. by how much the successive rows of pieces are shifted from each other. We assume that the overlap is added to the top right of the underlying pieces. Then, between two successive rows:

• If the top row is shifted to the right by p%, then an overlap greater than p% would lead to 4intersections. So we must maximize p. But this is the same as the bottom row being shifted to the left by (100 -p)%, so an overlap greater than (100 -p)% would also cause 4-intersections. So we must maximize (100 -p). • Symmetrically, when the top row is shifted to the left by p, we again need a simultaneous maximization of p and (100 -p). • Hence we must choose p = (100 -p) = 50, which gives us the proposed cover.

### VI. CONCLUSION

In this paper, we proposed improvements upon the existing Mapper algorithm solving many of its shortcomings partially. We have given a partial characterization of undesirable outputs of the Mapper algorithm and proposed a flexible method that corrects the choice of scale locally in a manner sensitive to the density of various data subsets. In all these methods, we have retained the unsupervised nature and stability of Mapper. Moreover, replacing the standard covering scheme with our brick-like cover reveals more topological information in a visualizable way. Our methods produce a visualization that is more true to the actual shape of data, via the Reeb space characterization, than the standard Mapper. Our contributions pave the path towards an automatic one-shot Mapper output which is the best visualization in terms of being close to the topological structure of data without any need of manual parameter optimization. This improves the efficacy of its applications in analysis and visualization of high dimensional big data. An interesting direction of future work that we mean to pursue is to study the relationship between successive applications of the Multimapper algorithm. Moreover, our method to detect deviations from Reeb space in Mapper via violations of Nerve Theorem hypothesis can be more powerfully implemented if a discrete analog of contractibility was reasonably defined, similar to how clusters are used to approximate connected components. Finally, a characterization of the best cover possible in any given dimension for the given data would be useful.

