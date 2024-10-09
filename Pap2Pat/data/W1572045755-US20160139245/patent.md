# DESCRIPTION

## FEDERALLY-SPONSORED RESEARCH AND DEVELOPMENT

This invention is assigned to the United States Government and is available for licensing for commercial purposes. Licensing and technical inquiries may be directed to the Office of Research and Technical Applications, Space and Naval Warfare Systems Center, Pacific, Code 72120, San Diego, Calif., 92152; voice (619) 553-5118; email ssc_pac_T2@navy.mil; reference Navy Case Number 103844.

## BACKGROUND

Tracking acoustic sources via passive sonar is a challenging task common to several underwater monitoring and surveillance systems. Classical tracking approaches based on matched-field tracking and Kalman filtering techniques are impractical due to their large computational and storage requirements.

## DETAILED DESCRIPTION OF SOME EMBODIMENTS

Reference in the specification to “one embodiment” or to “an embodiment” means that a particular element, feature, structure, or characteristic described in connection with the embodiments is included in at least one embodiment. The appearances of the phrases “in one embodiment”, “in some embodiments”, and “in other embodiments” in various places in the specification are not necessarily all referring to the same embodiment or the same set of embodiments.

Some embodiments may be described using the expression “coupled” and “connected” along with their derivatives. For example, some embodiments may be described using the term “coupled” to indicate that two or more elements are in direct physical or electrical contact. The term “coupled,” however, may also mean that two or more elements are not in direct contact with each other, but yet still co-operate or interact with each other. The embodiments are not limited in this context.

As used herein, the terms “comprises,” “comprising,” “includes,” “including,” “has,” “having” or any other variation thereof, are intended to cover a non-exclusive inclusion. For example, a process, method, article, or apparatus that comprises a list of elements is not necessarily limited to only those elements but may include other elements not expressly listed or inherent to such process, method, article, or apparatus. Further, unless expressly stated to the contrary, “or” refers to an inclusive or and not to an exclusive or.

Additionally, use of the “a” or “an” are employed to describe elements and components of the embodiments herein. This is done merely for convenience and to give a general sense of the invention. This detailed description should be read to include one or at least one and the singular also includes the plural unless it is obviously meant otherwise.

The embodiments disclosed herein involve a sparsity-driven approach for tracking broadband acoustic sources. Source location maps (SLMs), one per frequency, are sequentially estimated while capturing the temporal dependence between successive SLMs. Coherence across the SLMs' support is enforced to guarantee that the source-location estimates are independent of frequency. An iterative solver based on the proximal gradient (PG) method may be used to construct the SLMs.

Localization and tracking of acoustic sources, such as in the underwater environment, is an important task for applications such as environmental monitoring and surveillance. Passive sonar enables monitoring and surveillance systems to operate without radiating sound into the water; hence, it is often employed in applications where concealment and low environmental impact are desired.

Underwater source localization via passive sonar is, nevertheless, difficult due to the complex interactions that sound undertakes as it propagates underwater. In shallow-water propagation environments, multi-path propagation leads to constructive and destructive acoustic interactions at the hydrophones that further exacerbate the localization problem. However, it is the same multi-path propagation that creates enough diversity in the set of received acoustic signals at the hydrophone array to enable localization in range, depth, and azimuth.

Acoustic data collected over time can be used for sketching source tracks by, for example, plotting source-location estimates over time. Tracking capitalizes on the temporal structure inherent to source tracks, which are always constrained by the kinematic features of the source, to improve source-location estimates. However, using classical tracking methods, such as Kalman filtering, to develop a passive acoustic tracker poses significant computational challenges.

Matched-field processing (MFP) refers to classical underwater source-localization techniques that rely on an acoustic model for characterizing the acoustic propagation in the environment. It uses the adopted model to predict acoustic pressures, also known as replicas, at the hydrophones for sources located on a grid of tentative source locations. Then, it “matches” the replicas to the acoustic measurements gathered by the array in order to obtain acoustic-power estimates at all grid locations. The resulting power estimates are subsumed within the so-called ambiguity surface (or ambiguity volume if the sources' azimuths are also unknown). Source localization, thus, becomes a peak-picking problem where source-location estimates are mapped to grid points having high acoustic-power estimates. Despite the merits of MFP, the quality of its location estimates continues to be challenged by the presence of multiple sources and mismatch between the true propagation environment and the acoustic model used. These challenges can cause artifacts on the ambiguity surfaces that conceal the true source locations.

Tracking of underwater acoustic sources using passive sonar has traditionally been relegated to a post-processing task under the name of matched-field tracking (MFT). MFT algorithms construct a sequence of ambiguity surfaces to enable source localization at each point of the acoustic sources' trajectories.

Tracks are obtained by knitting peaks of consecutive ambiguity surfaces together. A directed graph constructed by connecting the largest peaks on neighboring ambiguity surfaces is used to construct the family of allowed tracks. The number of tracks grows combinatorially with the number of peaks used, quickly rendering this approach as computationally intractable.

Assumptions on the kinematics of the acoustic sources, e.g., maximum source velocity, constant source-speed and constant depth-trajectories, are used to reduce the number of tracks to be considered. The surviving tracks are scored based on their average acoustic-power estimates. When tracking a single source, the track with the largest score is chosen to be the true trajectory. This approach has been extended to enable coherent processing of broadband data. Weighted approaches for scoring the tracks obtained from the graph have also been proposed. A limitation common to all these approaches is that they do not use prior information when generating the ambiguity surfaces. Thus, these approaches are not well suited to process data in real time since they are required to construct a batch of ambiguity surfaces for generating tracks.

More recently, Bayesian approaches for joint tracking and parameter inversion in the context of underwater source localization have been proposed. Due to the nonlinear relationship between source locations and replicas, they use computationally-taxing Markov Chain Monte Carlo methods for estimating posterior probability distributions and are, thus, prohibited in the context of real-time underwater tracking.

Sparsity-driven Kalman-filter approaches can be used for tracking acoustic sources over a grid. These approaches use the entire localization grid postulated in MFP to define their state variable. They presume that only those grid entries corresponding to the locations of the sources take non-zero values. Hence, the state variable has a sparse structure. Direct application of these methods for underwater source localization is impractical due to the high dimensionality of the grid, and hence that of the state variable. Bayesian methods for tracking a sparse signal that build on the relevance vector machine have also been proposed. However, their associated computational cost is also high due to the size of their state-space variable and their need to maintain a covariance-matrix estimate for it.

The embodiments discussed herein relate to a sparsity-driven framework for broadband source localization via passive sonar. Per time instant, SLMs, one per frequency, are constructed. Only those points on the map that correspond to source locations take nonzero values. All other points in the SLMs are set to zero. Motivated by the fact that the source locations are presumed to be independent of frequency, coherence across SLMs is enforced to guarantee that their support coincides. SLMs can be combined to construct a broadband SLM. Different from previous approaches to construct SLMs, the disclosed approach considers a regularizer that forces the SLM estimator to use both the previous SLM obtained and the new measurement available. An iterative solver based on PG may be used for constructing the SLMs.

FIG. 1 shows a block diagram of an embodiment of the operational concept of a system 10 in accordance with the Sparsity-Driven Passive Tracking of Acoustic Sources. System 10 includes K acoustic sources 20, 30, and 40, each radiating sound underwater. Although the acoustic sources are presumed to be mobile, thus justifying the dependence of their locations {rk (τ)}k=1K, on the time τ∈, no assumptions about their kinematics are made. Each rk(τ)∈ d is given in cylindrical coordinates comprising the source's range, depth (with respect to the sea surface), and azimuth, with d∈{1,2,3}.

An acoustic sensor array 50 detects acoustic signals 22, 32, and 42 from sources 20, 30, and 40, respectively. As an example, an acoustic sensor array 50 is an array of N hydrophones with known and arbitrary geometry, where N>0. Array 50 is used to collect a time series of acoustic pressure vectors {y(τ) ∈N:τ∈} with entries [y(τ)]n ∈ denoting the acoustic pressure measured by the n-th hydrophone in the array at time τ. Note that although the framework is agnostic to the specific geometry of the array, its geometry affects the definition of source location. For instance, data gathered with an array that features horizontal aperture but no vertical aperture primarily provides information about the sources' azimuth only (d=1), although source range and depth can be determined depending on the closeness of the source to the end fire direction, the length of the array, and the bandwidth considered. On the other hand, data collected on a vertical array with no horizontal aperture provide information on the source range and depth only (d=2), unless the bathymetry is not flat. Data gathered with an array featuring vertical and horizontal aperture provides information about the sources' range, depth, and azimuth (d=3).

The acoustic time-series data is transformed to the frequency domain via a discrete-time Fourier transform. Fourier coefficients at F frequencies {ωf}f=1F across the N hydrophones are collected per frequency to vectors yf (t):=[yf1(t), . . . , yfN(t)]′∈N, where yfN(t) denotes the Fourier coefficient estimate corresponding to ωf at time t obtained from data gathered by the n-th hydrophone and ′ denotes the transpose operator.

It is presumed that a model characterizing the acoustic propagation in the environment is available. If {rk (t)∈d}k=1K were known, one could use it to compute model-predicted Fourier coefficients at the array for each source location, i.e., replicas. Let {hacek over (p)}k,f denote the normalized replica for a source located at rk (t) transmitting at ωf, where the normalization implies that |{hacek over (p)}k,f∥2. Each yf(t) can be modeled as

yf(t)=Σk=1Ksk,f(t){hacek over (p)}k,f+εf(t),f=1, . . . F  (Eq. 1)

where εf(t)∈N denotes a zero-mean additive noise component, and sk,f denotes the Fourier coefficient at ωf of the acoustic signature of the spectrum corresponding to the k-th source acoustic signature at time t. The replicas {hacek over (p)}k,f 's are obtained using a model that characterizes the acoustic propagation environment and the geometry of the array. Although replicas have been defined as time invariant, (Eq. 1) can be adapted to capture spatiotemporal changes in the model used to generate the replicas.

Given K and {yf ({tilde over (t)}),∀f}{tilde over (t)}=0t, the goal of the spectral passive-acoustic tracking problem is to recursively estimate the locations {rk(t)}k=1K of the acoustic sources 20, 30, and 40. Even if all sk,f(t) in (Eq. 1) were known, finding estimates for the source locations is difficult due to the non-linear relationship between rk(t) and {hacek over (p)}k,f, which in most cases of interest is not available in closed form.

In some embodiments, the estimation of the locations of the acoustic sources is performed by a processor 52 embedded within acoustic sensor array 50, with the results being transmitted, via signal 54, to receiver 60. In some embodiments, acoustic sensor array sends, via signal 54, the signal measurements to receiver 60, which performs the required processing.

As shown in diagram 100 of FIG. 2, acoustic sources 110 generate acoustic signals 120 that propagate through the propagation environment towards an acoustic sensor array 140, which in this case is a hydrophone array. Acoustic signals are collected by the hydrophone array 140 as a time series 130 of acoustic pressures. The time-series data captured by each hydrophone in array 140 is transformed to the Fourier domain via a short-time Fourier transform (STFT) processing step 150 yielding Fourier coefficients. The Fourier coefficients obtained across hydrophones for a set of F frequencies {ω1, . . . , ωF} are grouped to construct Fourier coefficient vectors yf(t)∈N at the end of processing step 160.

Referring to FIG. 3, diagram 200 shows an embodiment of a model-based prediction component, where a postulated source location 210 is input 212 into a model-based predictor 220. Based upon an acoustic model, such as an underwater acoustic model characterizing the true propagation environment, predictor 220 yields a replica vector 222. Replicas are model-based predicted vectors of Fourier coefficients that are used by the Passive Tracking of Acoustic Sources with Sparse Innovations to model the yf(t)'s and determine the source localizations.

FIG. 4 shows a diagram 300 illustrating an example of an operational environment and the desired SLM. As shown, an underwater environment 310 includes a sensor array 320 mounted to the seafloor, a ship 330 on the surface of the water, and submarines 340 and 350 located underwater. An SLM 360 includes a marker 362 representing the location of sensor array 320, a marker 364 representing the estimated location of ship 330, a marker 366 representing the estimated location of submarine 340, and a marker 368 representing the estimated location of submarine 350.

A model that alleviates the challenges associated with the nonlinearities inherent to (Eq. 1) is proposed next. A possible approach is to introduce a grid of tentative source locations :={rg}g=1G with G>>max{KF, N}. Now the yf(t)'s at time t can be modeled as

yf(t)=Σg=1Gsg,f(t)pg,f+εf(t),f=1, . . . ,F  (Eq. 2)

where pg,f denotes the normalized replica corresponding to a source located at rg ∈, and sg,f(t) the Fourier coefficient at ωf of the spectrum corresponding to the acoustic signature of the source located at rg ∈ at time t.

Since G>>KF most of the sg,f(t)'s are expected to be zero. Only those few sg,f (t)'s that correspond to the true source locations should take non-zero values. Let sf (t):=[s1,f(t), . . . ,sG,f(t)]′ ∈G and S(t):=[s1(t), . . . ,sF(t)]∈G×F Once an estimate for S(t) is available, a broadband SLM can be obtained by plotting the pairs (rg,∥g(t)∥2) for all rg ∈, wheres g(t):=[sg,1(t), . . . , sg,F (t)]′∈F comprises the entries of the g-th row of S(t). Source location estimates {{circumflex over (r)}k(t)} correspond to the location of the K-largest peaks in the broadband SLM, that is

\(\begin{matrix}
{\in {{ϛ_{k}}_{q}}} & \left( {{Eq}.\mspace{14mu} 3} \right)
\end{matrix}\)

Discussed below is an estimator for S(t) that captures the group sparsity inherent to the rows of S(t) and the temporal dependency between SLMs corresponding to consecutive time instances.

An iterative estimator for S(t) is proposed that uses the previously estimated S(t−1) to capture the temporal dependency between source locations at consecutive time instances. Per time t, an estimate Ŝ(t)=[ŝ1(t), . . . , ŝF(t)] for S(t) is obtained as

\(\begin{matrix}
{{\hat{S}(t)} = {{\frac{1}{2}{\sum\limits_{f = 1}^{F}{{{y_{f}(t)} - {P_{f}s_{f}}}}_{2}^{2}}} + {\frac{\lambda}{2}{\overset{F}{\sum\limits_{f = 1}}{{s_{f} - {{\hat{s}}_{f}\left( {t - 1} \right)}}}_{2}^{2}}} + {\mu {\sum\limits_{g = 1}^{G}{ϛ_{g}}_{2}}}}} & \left( {{Eq}.\mspace{14mu} 4} \right)
\end{matrix}\)

where S:=[s1, . . . , SF], g′ is the g-th row of S, Pf:=[p1,f, . . . , pG,f]∈N×G is the matrix of replicas for ωf, and μ, λ>0 are tuning parameters. Equation (Eq. 4) represents a regularized least-squares regression problem. The regularization term in (Eq. 4) scaled by μ encourages group sparsity on the rows of Ŝ(t), with μ controlling the number of non-zero rows in Ŝ(t). The regularization term scaled by λ encourages estimates ŝf(t) to be close to ŝf(t−1), ∀f, with λ controlling the emphasis place on ŝf(t−1) when estimating sf(t), ∀f.

FIG. 5 shows a diagram 400 of an embodiment of a grid 410 comprising a plurality of tentative locations, which can be used to construct an SLM, and an estimated source location 420. Location 420 corresponds to a point (rg,∥g∥q). Although only one estimated source location 420 is shown for SLM 410, other SLMs may contain additional estimated source locations 420.

FIG. 6 shows a diagram 500 of the structure of the regression coefficient matrix S 510. Once an estimate for S has been obtained, its columns can be used to construct SLMs over  per ωf. Furthermore, a broadband SLM can be constructed using whole rows of S for each rg ∈. For instance, after defining 9:=[sg,1, . . . , sg,F]′∈F as the vector corresponding to the g-th row of S 520, an SLM can be constructed by plotting the pairs (rg,∥g∥q) for all rg ∈ and q>1.

Equation 4 may be written as a real-valued convex optimization problem after representing all complex-valued variables by the direct sum of their real and imaginary parts. To this end, the following notation is introduced: {hacek over (y)}f (t):=[Re{yf(t)}′, Im{yf (t)}′]′, {hacek over (s)}f:=[Re{sf}′, Im{sf}′]′, {hacek over (S)}:=[{hacek over (s)}1, . . . , {hacek over (s)}F], and

\(\begin{matrix}
{{\overset{\Cup}{P}}_{f}:=\begin{bmatrix}
{{Re}\left\{ P_{f} \right\}} & {{- {Im}}\left\{ P_{f} \right\}} \\
{{Im}\left\{ P_{f} \right\}} & {{Re}\left\{ P_{f} \right\}}
\end{bmatrix}} & \left( {{Eq}.\mspace{14mu} 5} \right)
\end{matrix}\)

where Re{•}(Im{•}) denotes the real-part (imaginary-part) operator. Matrix {hacek over (S)} can be alternatively viewed in terms of its rows as {hacek over (S)}=[1′, . . . , 2G′]′ where the first (last) G rows correspond to the real (imaginary) parts of the rows of S.

Equation (Eq. 4) is equivalent to the following convex optimization problem:

\(\begin{matrix}
{{\overset{\Cup}{S}(t)} = {{\underset{\overset{\Cup}{S} \in {\mathbb{R}}^{2G \times F}}{\arg \; \min}\frac{1}{2}{\sum\limits_{f = 1}^{F}\; {{{{\overset{\Cup}{y}}_{f}(t)} - {{\overset{\Cup}{P}}_{f}{\overset{\Cup}{s}}_{f}}}}_{2}^{2}}} + {\frac{\lambda}{2}{\sum\limits_{g = 1}^{G}\; {{{\overset{\Cup}{v}}_{g} - {{\overset{\Cup}{v}}_{g}\left( {t - 1} \right)}}}_{2}^{2}}} + {\mu {\sum\limits_{g = 1}^{G}\; {{\overset{\Cup}{v}}_{g}}_{2}}}}} & \left( {{Eq}.\mspace{14mu} 6} \right)
\end{matrix}\)

where {hacek over (v)}g:=[1′, . . . , 2G′]′∈2F, {hacek over (v)}g(t−1) corresponds to the direct sum of the real and imaginary parts of g(g(t−1)). FIG. 7 shows a diagram 600 illustrating the structure of {hacek over (S)}. It comprises two blocks that correspond to the real part 610 of matrix S and the imaginary part 620 of matrix S. Note that the minimizer Ŝ(t) of (Eq. 4) can be obtained as a function of {hacek over (S)}(t) as Ŝ(t)={hacek over (S)}1:G(t)+j{hacek over (S)}G+1:2G (t), where j:=√{square root over (−1)} and {hacek over (S)}g1:g2(t) is a matrix which comprises rows g1 to g2 from {hacek over (S)}(t), 1≦g1≦g2≦G.

Although (Eq. 6) is a convex optimization problem that can be solved via interior point methods, such a solver would entail high computational complexity due to the high dimensionality of {hacek over (S)} and fail to exploit the sparse structure of {hacek over (S)}. The ensuing section presents a PG solver for (Eq. 6) that capitalizes its structure to obtain closed-form updates.

Equation (Eq. 4) may also be written as

\(\begin{matrix}
{{\min\limits_{\overset{\Cup}{S} \in {\mathbb{R}}^{2G \times F}}\frac{1}{2}{\sum\limits_{f = 1}^{F}\; {{{{\overset{\Cup}{y}}_{f}(t)} - {{\overset{\Cup}{P}}_{f}{\overset{\Cup}{s}}_{f}}}}_{2}^{2}}} + {\frac{\lambda}{2}{\sum\limits_{f = 1}^{F}\; {{\overset{\Cup}{s}}_{f}}_{2}^{2}}} - {\lambda {\sum\limits_{g = 1}^{G}\; {{\overset{\Cup}{v}}_{g}^{\prime}{{\overset{\Cup}{v}}_{g}\left( {t - 1} \right)}}}} + {\mu {\sum\limits_{g = 1}^{G}\; {{\overset{\Cup}{v}}_{g}}_{2}}}} & \left( {{Eq}.\mspace{14mu} 7} \right)
\end{matrix}\)

where all terms independent of {hacek over (S)} have been removed from the cost. The terms

\({\frac{\lambda}{2} \cdot {{\overset{\Cup}{s}}_{f}}_{2}^{2}},{f = 1},\)

in the regularizer are known to induce resilience to model mismatch into the estimate {hacek over (S)}(t). From this vantage point, λ>0 corresponds to the variance of a random perturbation affecting each replica, which depends on the mismatch between the true propagation environment and the model used to generate the replicas. The linear terms −λvg′vg(t−1) encourage estimates {hacek over (v)}g (t) to be close to {hacek over (v)}g(t−1). In particular, as the model mismatch increases, and thus the reliability of the replicas decreases, (Eq. 7) naturally steers its attention towards the prior SLM estimates subsumed by the {hacek over (v)}g(t−1)'s.

A PG algorithm for solving (Eq. 6) that capitalizes on its sparse structure is discussed below. Equation 6 may be written as min{hacek over (s)} h({hacek over (S)})+μΣg−1G∥{hacek over (v)}g∥2′ where h({hacek over (S)}):=1/2Σf=1F[∥{hacek over (y)}f(t)−{hacek over (P)}f{hacek over (s)}f∥22+λ∥{hacek over (s)}f∥22−2λ{hacek over (s)}f′{hacek over (s)}f(t−1)] denotes the continuously-differentiable portion of the cost. Note that the gradient of h({hacek over (S)}) is Lipschitz continuous with Lipschitz constant Lh:=maxf=1, . . . ,F σmax Pf′Pf+λI2G), where σmax(Pf′Pf) denotes the largest singular value of Pf′Pf. That is, ∥∇h({hacek over (S)}1)−∇h({hacek over (S)}2)∥2≦Lh∥{hacek over (S)}1−{hacek over (S)}2∥F, where ∇h({hacek over (S)}l) denotes the gradient of h with respect to {hacek over (S)} evaluated at {hacek over (S)}l. It should also be noted that Lh can be obtained at a reduced computational cost by using the singular values of the Pf's as

Lh=maxf[σmax(Pf)]2+λ.

The PG method can be interpreted as a majorization-minimization method relying on a majorizer H({hacek over (S)}; Z) for h, where Z:=[z1, . . . , zF]∈2G×F is an auxiliary matrix. The majorizer H satisfies: (i)H({hacek over (S)}; Z)≧h({hacek over (S)}), ∀({hacek over (S)}); and, (ii) H({hacek over (S)}; Z)=h({hacek over (S)}) for Z={hacek over (S)}. The specific H used by the PG method is

\(\begin{matrix}
{{H\left( {\overset{\Cup}{S};Z} \right)}:={{h(Z)} + {\sum\limits_{f = 1}^{F}\; {{\nabla{h_{f}\left( z_{f} \right)}^{\prime}}\left( {{\overset{\Cup}{s}}_{f} - z_{f}} \right)}} + {\frac{L_{h}}{2}{{\overset{\Cup}{S} - Z}}_{F}^{2}}}} & \left( {{Eq}.\mspace{14mu} 8} \right)
\end{matrix}\)

where hf({hacek over (s)}f):=1/2∥f(t)−{hacek over (P)}f{hacek over (s)}f∥22+λ∥{hacek over (s)}f∥22−2λ{hacek over (s)}f′{hacek over (s)}f(t−1), and ∇hf(zf) denotes the gradient of hf with respect to {hacek over (s)}f evaluated at zf. That the majorizer in (Eq. 7) satisfies conditions (i) follows from the fact that the gradient of h is Lipschitz continuous, and that it satisfies (ii) follows after setting Z={hacek over (S)} in (Eq. 8). FIG. 8 shows a graph 700 illustrating a majorizer H 710 for the smooth function h 720. Note that the line intersection 730 illustrates condition (ii) above, that is, H must touch at the point Z={hacek over (S)}. With i denoting the PG iteration index, the PG algorithm iteratively solves

\(\begin{matrix}
{{{\overset{\Cup}{S}}^{i}(t)} = {\min\limits_{\overset{\Cup}{S}}\left\lbrack {{H\left( {\overset{\Cup}{S};{{\overset{\Cup}{S}}^{({i - 1})}(t)}} \right)} + {\mu {\sum\limits_{g = 1}^{G}\; {{\overset{\Cup}{v}}_{g}}_{2}}}} \right\rbrack}} & \left( {{Eq}.\mspace{14mu} 9} \right)
\end{matrix}\)

where {hacek over (S)}i(t) denotes the PG estimate for {hacek over (S)}(t) at iteration i.

From an algorithmic point of view, it is convenient to write H as a function of the {hacek over (v)}g's. After performing some algebraic manipulations on H and dropping all terms independent of {hacek over (S)}, (Eq. 9) can be written as

\(\begin{matrix}
{{{{\overset{\Cup}{S}}^{\lbrack i\rbrack}(t)} = {\min\limits_{\overset{\Cup}{S}}{\sum\limits_{g = 1}^{G}\; \left( {{\frac{L_{h}}{2}{{{\overset{\Cup}{v}}_{g} - {w_{g}^{\lbrack{i - 1}\rbrack}(t)}}}_{2}^{2}} + {\mu {{\overset{\Cup}{v}}_{g}}_{2}}} \right)}}}{where}} & \left( {{Eq}.\mspace{14mu} 10} \right) \\
{{w_{g}^{\lbrack{i - 1}\rbrack}(t)}:={{{\overset{\Cup}{v}}_{g}^{\lbrack{i - 1}\rbrack}(t)} - {\left( \frac{1}{L_{h}} \right){d_{g}^{\lbrack{i - 1}\rbrack}(t)}}}} & \left( {{Eq}.\mspace{14mu} 11} \right)
\end{matrix}\)

is a gradient-descent step, with step-size

\(\frac{1}{L_{h}},\)

for the g-th row of {hacek over (S)}, and the entries of dg[i−1](t), which correspond to those of the gradient of hf with respect to {hacek over (v)}g, are

\(\begin{matrix}
{\left\lbrack {d_{g}^{\lbrack{i - 1}\rbrack}(t)} \right\rbrack_{f} = \left\{ \begin{matrix}
{{{{- {\overset{\Cup}{p}}_{g,f}^{\prime}}{r_{f}^{\lbrack{i - 1}\rbrack}(t)}} + {\Delta \; {s_{f,g}^{\lbrack{i - 1}\rbrack}(t)}}},} & {{f = 1},\ldots \mspace{14mu},F} \\
{{{{- {\overset{\Cup}{p}}_{{g + G},f}^{\prime}}{r_{f}^{\lbrack{i - 1}\rbrack}(t)}} + {\Delta \; {s_{f,{g + G}}^{\lbrack{i - 1}\rbrack}(t)}}},} & {{f = {F + 1}},\ldots \mspace{14mu},{2F}}
\end{matrix} \right.} & \left( {{Eq}.\mspace{14mu} 12} \right)
\end{matrix}\)

where rf[i−1](t):={hacek over (y)}f(t)−{hacek over (P)}f{hacek over (s)}f[i−1](t) and Δsf,g+G[i−1](t):=λ({hacek over (s)}f,g[i−1](t)−sf, g(t−1)). Equation (Eq. 9) is often called the proximal operator μ∥{hacek over (v)}g∥2 with parameter

\(\frac{1}{L_{h}}.\)

Equation (Eq. 9) is decomposable across {hacek over (v)}g's. Per iteration i, the PG update in (Eq. 8) can be performed in parallel for every pair of rows of {hacek over (S)} comprised in each {hacek over (v)}g via

\(\begin{matrix}
{{{\overset{\Cup}{v}}_{g}^{i}(t)} = {{\min\limits_{{\overset{\Cup}{v}}_{g}}{\frac{L_{h}}{2}{{{\overset{\Cup}{v}}_{g} - {w_{g}^{\lbrack{i - 1}\rbrack}(t)}}}_{2}^{2}}} + {\mu {{{\overset{\Cup}{v}}_{g}}_{2}.}}}} & \left( {{Eq}.\mspace{14mu} 13} \right)
\end{matrix}\)

The cost in (Eq. 13) is convex; however, it is non-differentiable due to ∥{hacek over (v)}g∥2. Despite the non-differentiability of its cost, (Eq. 13) can be solved in closed form and its solution in this case is

\(\begin{matrix}
{{{\overset{\Cup}{v}}_{g}^{i}(t)} = {{w_{g}^{\lbrack{i - 1}\rbrack}(t)}\left( {1 - \frac{\mu}{L_{h}{{w_{g}^{\lbrack{i - 1}\rbrack}(t)}}_{2}}} \right)_{+}}} & \left( {{Eq}.\mspace{14mu} 14} \right)
\end{matrix}\)

where (•)+=max{0,•}. Equation (Eq. 14) follows readily from the Karush-Kuhn-Tucker (KKT) conditions for (Eq. 13) where the notion of sub-differential is used to characterize {hacek over (v)}g[i](t).

The resulting PG algorithm is summarized as Algorithm 1 shown in diagram 800 of FIG. 9. Per iteration, the PG update entails 0 (NGF) scalar operations required for computing dg[i−1](t) in (Eq. 11). The algorithm terminates when ∥{hacek over (S)}[i](t)−{hacek over (S)}[i−1](t)∥2/∥{hacek over (S)}[i](t)∥2≦εs, where ∥•∥ denotes the Frobenius norm and εs is a small positive threshold, e.g., εs=10−5. Algorithm 1 can be shown to converge to the solution of (Eq. 5) while featuring a worst-case convergence rate of 0(1/i). Thus its convergence may be slow in practice, requiring up to several hundreds of iterations to achieve a highly accurate solution. Nevertheless, it has been observed that the support of {hacek over (S)}[i](t) can be correctly identified using fewer iterations (in the order of 50 iterations). Moreover, it is possible to develop an accelerated version of Algorithm 1 featuring a worst-case convergence rate of

\({O\left( \frac{1}{j^{2}} \right)}.\)

The updates involved in the resulting accelerated PG algorithm are outlined in diagram 900 shown in FIG. 10.

FIG. 11 shows a flowchart of an embodiment of a method 1000 in accordance with the Passive Tracking of Underwater Acoustic Sources with Sparse Innovations. As an example, method 1000 may be performed by system 10, 100, and 200 as shown in FIGS. 1-3. Also, while FIG. 11 shows one embodiment of method 1000 to include steps 1010-1080, other embodiments of method 1000 may contain fewer or more steps. Further, while in some embodiments the steps of method 1000 may be performed as shown in FIG. 11, in other embodiments the steps may be performed in a different order, or certain steps may occur simultaneously with one or more other steps. Additionally, some or all of the steps of method 1000 may be performed by processor 52 embedded within acoustic sensor array 50, by receiver 60, or by other processing means operatively connected to acoustic sensor array 50.

Method 1000 may begin with step 1010, which involves defining a grid  of G tentative locations rg, to localize more than one acoustic sources, based on the location of an acoustic sensor array 50, where up to K acoustic sources 20, 30, and 40 are presumed to be located. In some embodiments step 1010 includes the step of estimating the number of acoustic sources, while in other embodiments the number of acoustic sources is predetermined.

Step 1020 involves using an acoustic model to compute, via the model-based predictor 220, replicas that correspond to simulated acoustic sources at locations in , wherein the replicas are model-predicted Fourier coefficient vectors at F frequencies {ωf}f=1F corresponding to the acoustic pressure field 120 as sampled by an acoustic sensor array 140 having N sensors. Step 1030 involves collecting, using acoustic sensor array 140, time series data 130 of actual acoustic measurements at each sensor of the acoustic sensor array caused by the acoustic sources 110.

Method 1000 may proceed to step 1040, which involves using a short-time Fourier transform (STFT) 150 on the collected time-series data 130 partitioned to m blocks to compute Fourier coefficient estimates at frequencies {ωf}f=1F for all N sensors. Step 1050 involves constructing a set of Fourier coefficient vectors Y (t):=[y1(t), . . . , yF (t)]∈N×F, where [Y(t)]n,f ∈ denotes the Fourier coefficient corresponding to ωf for the n-th sensor in the t-th STFT block, at step 160 using the Fourier coefficients previously obtained via the STFT.

Step 1060 involves modeling Fourier coefficient vectors at ωf for the m-th measurement block of the collected time series data as yf(t)=Σg=1Gsg,f(t)pg,f+εf(t), ∀f, where sg,f(t) denotes the unknown Fourier coefficient associated to the acoustic signature at frequency ωf for a source located at rg, pg,f ∈N is the replica for ωf corresponding to a source located at rg normalized so that ∥pg,f∥2=1, and εf(t) denotes the Fourier coefficients at ωf corresponding to the noise in the t-th block.

Step 1070 involves setting to zero all values of sg,f(t) associated to tentative locations rg where acoustic sources are presumed to be absent. Step 1070 is an optional step that may or may not appear in all embodiments of the methods disclosed herein. It relays on so-called predictor screening rules that can identify with certainty points in  where acoustic sources are absent. A specific embodiment of a predictor-screening rule is described in the commonly-assigned U.S. patent application Ser. No. 14/285,400, entitled “Multitask Learning Method for Broadband Source-Location Mapping of Acoustic Sources.”

Step 1080 involves obtaining, at time t an estimate S(t) as the solution to

\({{\min_{S \in {\mathbb{C}}^{G \times F}}{\frac{1}{2}{\sum\limits_{f = 1}^{F}\; {{{y_{F}(t)} - {P_{f}s_{f}}}}_{2}^{2}}}} + {\frac{\lambda}{2}{\sum\limits_{f = 1}^{F}\; {{s_{g} - {{\hat{s}}_{g}\left( {t - 1} \right)}}}_{2}^{2}}} + {\mu {\sum\limits_{g = 1}^{G}\; {ϛ_{g}}_{2}}}},\)

where S:=[s1, . . . , sF]∈G×F, g′ is the g-th row of S, Pf:=[p1,f, . . . , pG,f]∈N×G is the matrix of replicas for ωf, and μ, λ>0 are tuning parameters. Step 1080 also involves generating one or more SLMs over  per frequency ωf using S(t), wherein each location on a particular SLM is associated with the magnitude of its corresponding acoustic gain estimate |ŝg,f(t)|, wherein estimates of the actual locations of the K acoustic sources, {{circumflex over (r)}k(t)}k∈κ, correspond to the locations of the K-largest coefficients |ŝg,f (t)| depicted in the SLM. In some embodiments of step 1080, the SLMs are generated using an iterative problem solver based upon the PG method.

In some embodiments, step 1080 involves generating SLMs over  per frequency ωf using each column sf (t) of S(t) to construct the SLMs per frequency ωf. In some embodiments, step 1080 involves generating a broadband SLM over comprising all frequencies ωf used to compute S(t) using a whole row of S(t) for each rg ∈. In some embodiments of step 1080, generating SLMs over  per frequency ωf involves generating a broadband SLM over  using S(t) by plotting the pairs (rg, ∥g(t)∥2) for all rg ∈, where g(t):=[sg,1(t), . . . , Sg,F (t)]′∈F comprises the entries of the g-th row of S(t).

Method 1000 may be implemented as a series of modules, either functioning alone or in concert, with physical electronic and computer hardware devices. Method 1000 may be computer-implemented as a program product comprising a plurality of such modules, which may be displayed for a user.

Various storage media, such as magnetic computer disks, optical disks, and electronic memories, as well as non-transitory computer-readable storage media and computer program products, can be prepared that can contain information that can direct a device, such as a micro-controller, to implement the above-described systems and/or methods. Once an appropriate device has access to the information and programs contained on the storage media, the storage media can provide the information and programs to the device, enabling the device to perform the above-described systems and/or methods.

For example, if a computer disk containing appropriate materials, such as a source file, an object file, or an executable file, were provided to a computer, the computer could receive the information, appropriately configure itself and perform the functions of the various systems and methods outlined in the diagrams and flowcharts above to implement the various functions. That is, the computer could receive various portions of information from the disk relating to different elements of the above-described systems and/or methods, implement the individual systems and/or methods, and coordinate the functions of the individual systems and/or methods.

The performance of the proposed broadband tracking algorithm is illustrated on the third Shallow-Water Evaluation Cell Experiment (SWellEX-3) dataset. The environment considered corresponds to that in the third Shallow-Water Evaluation Cell Experiment (SWellEX-3), see diagram 1100 shown in FIG. 12. In SWellEX-3, a towed source transmitting at frequencies {53+16 k}k=09 Hertz and a vertical line array 1110 collecting acoustic data were used. In this analysis, only 9 hydrophones, out of 64 hydrophones available, were used. These hydrophones were 11.25 m apart, having a total aperture of 90 m with the bottom element 6 m above the seafloor (water depth was 198 m).

A grid with G=20,000 locations spanning radial distances 0-10 km and depths 0-198 m was used, as shown by the top portion of the diagram 1120 ending at a depth of 198 m at line 1130. Depths between 198 m-228 m are represented by portion 1140, depths between 228 m-1028 m are represented by portion 1150, and depths below 1028 m are represented by portion 1160. The grid's radial and vertical spacing were 50 m and 2 m, respectively. All replicas were computed with the KRAKEN normal-mode propagation model using the environmental model as shown in FIG. 12.

Sample parameter values used in the model are: ν1=1; 520 m/s, ν2=1; 498 m/s, ν3=1; 490 m/s, ν4=1; 490 m/s, ν5=1; 572 m/s, ν6=1; 593 m/s, ν7=1; 881 m/s, ν8=3; 246 m/s, ν9=5; 200 m/s, αb=0.2 dB/m/kHz, αb=0.06 dB/m/kHz, αb=0.02 dB/m/kHz, ρb=1.76 g/cm3, ρb=2.06 g/cm3, and ρb=2.66 g/cm3.

The top portion the diagram 1200 shown in FIG. 13 illustrates the bathymetry 1210 along the range trajectory of a towed acoustic source used during SWellEX-3, while the bottom portion of FIG. 13 shows the range trajectory 1220 of the towed acoustic source. Note that the model used reflects the initial portion of the bathymetry (up to time 60 min). After time 60 min., there is increasing mismatch between the model used and the true propagation environment whose effect will be seen in the final portions of the tracks to be described next. An embodiment of the methods disclosed herein can alleviate this mismatch by dynamically updating the acoustic propagation model used according to the appropriate bathymetric data along the direction on which the source is located. This embodiment will use source location estimates (Eq. 3) to dynamically modify the model-based predictor based on the current source locations.

Referring to FIGS. 14 and 16, FIG. 14 shows a diagram 1300 illustrating depth tracks obtained for the source using matched-field tracking and FIG. 16 shows a diagram 1500 illustrating range tracks obtained for the source using matched-field tracking. MFT was used as a baseline for comparison. Despite its high computational complexity, MFT yields accurate track estimates for the single source case. Ambiguity surfaces obtained via Bartlett MFP, were used to construct partial linear trajectories, also known as tracklets. A total of 8 ambiguity surfaces were used to construct each tracklet. Each ambiguity surface accounts for 13.65 seconds of recorded data, and thus each tracklet corresponds to 109 seconds of recorded data. Note that there is a 50% overlap between consecutive tracklets.

Per time t, the ranges and depths of all peaks are plotted in diagram 1400 shown in FIG. 15 and diagram 1600 shown in FIG. 17. In these particular tests, the trajectory was broken into three different intervals for which different (λ, μ) pairs were chosen. Although the tracks obtained give a coarse approximation to those followed by the source, it was expected that by dynamically adjusting the selection of, e.g., μ, the gaps in the tracks could be removed. Note that these gaps appear because the choice of μ at those particular time instances was too high. Note also that both MFT and the proposed method fail to track the source after t=65 min. due to the severe mismatch between the environment and the model used to generate the replicas.

FIG. 18 shows a diagram 1700 illustrating a Source Location Map (SLM) obtained using a PG solver. As shown, reference 1710 represents the estimated source location, which in this case matches the true source location, while reference 1720 representing an artifact, i.e., non-zero entry in the SLM that does not correspond to a source location. The color bar on the right illustrates the intensity of each point on the map in a decibel (dB) scale. Note that the magnitude of the artifact is more than 10 dB below the magnitude of the point associated to the true source location.

FIG. 19 shows a graph 1800 illustrating faster convergence using the accelerated PG (APG) solver outlined in FIG. 10 versus the PG solver outlined in FIG. 9, where line 1810 represents the cost versus iterations for the accelerated PG solver and line 1820 represents the cost versus iterations for the PG solver. In practice, only a few iterations of either algorithm were needed to correctly identify the support of the SLMs (up to 40 iterations in this case). The dashed line 1830 illustrates the iteration value at which both algorithms were stopped, and the cost function value achieved by the PG and APG algorithms.

In order to simulate the presence of two sources using the SWellEX-3 dataset, data corresponding to the portions of the trajectory illustrated in FIG. 13 between 0-25 mins. and 40-65 mins. (first and second colored panels from left to right) were combined after being rescaled to compensate for the signal-to-noise ratio difference between the two portions of the trajectory. In this case, the computational complexity of MFT, and correspondingly its execution time, increased dramatically since the algorithm connected all combinations of pairs of peaks across ambiguity surfaces. MFT was not able to distinguish the two sources possibly due to the width of the peaks on the ambiguity surfaces.

FIG. 20 shows a diagram 1900 illustrating range tracks obtained for two sources using an embodiment of a method in accordance with the Sparsity-Driven Tracking of Acoustic Sources. Similarly to the one source case, μ was adapted via grid search so as to obtain approximately 15 non-zero entries per SLM. The top portion of diagram 1900 in FIG. 20 illustrates the number of nonzero entries S0 obtained per SLM. The bottom portion of diagram 1900 in FIG. 20 illustrates the estimated trajectories for the two sources, which as expected match portions of the one source trajectory shown in FIG. 13.

FIG. 20 illustrates the performance of an embodiment of the method disclosed herein when used to track the location of the two sources. Similarly to the one-source case, different (λ, μ) pairs were chosen for different intervals of the trajectory. Although the trajectories of the two sources can be observed in range, it is difficult to separate the two sources in depth. As in the one source case, dynamic adjustment of the parameters is expected to help improve on the quality of the tracks obtained.

Although some embodiments of the method were discussed herein with regard to underwater source localization, some embodiments of the method may apply to other acoustic source localization environments, such as above water, where accurate in-air acoustic propagation models are available. Another possible extension involves using spatially distributed arrays for localization as a way to exploit spatial diversity to counteract multipath affects in the localization performance and to reduce the presence of surveillance gaps.

Many modifications and variations of the Sparsity-Driven Passive Tracking of Acoustic Sources are possible in light of the above description. Within the scope of the appended claims, the embodiments of the systems described herein may be practiced otherwise than as specifically described. The scope of the claims is not limited to the implementations and the embodiments disclosed herein, but extends to other implementations and embodiments as may be contemplated by those having ordinary skill in the art.

