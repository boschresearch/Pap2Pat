# Motivation

Many scientific and engineering datasets are multimodal, necessitating the fusion of disparate sources and datatypes for informed analysis. For example, in the realm of process optimization for materials manufacturing, processes ranging from microelectronic fabrication to metal additive manufacturing involve a myriad of process settings along with

## Relationship to prior literature

This work draws from several thematic bodies of literature. The non-exhaustive list below denotes those works which have most informed our approach as well as provide overviews for the recent state-of-the-art.

Gaussian mixture embeddings For deep unsupervised clustering, several works replace the standard normal prior from (Kingma & Welling, 2014;Rezende et al., 2014) with a Gaussian mixture model (GMM) to facilitate disentanglement and provide an explicit parameterization of clusters (Dilokthanakul et al., 2016;Jiang et al., 2017;Rao et al., 2019;Lee et al., 2020). Each modality in the multi-modal prior distribution is expected to provide disentangled latent representations of data which admit an explicit parameterization of class distributions. The current work is most similar to VaDE (Jiang et al., 2017) in its use of mean-field distributions to obtain a separable ELBO, and Bayesian estimator for q(c|X). This work builds upon VaDE by incorporating multimodal data inputs while maintaining computational tractability of the ELBO, as well as employing clusters to decode into physics-informed MoE models.

Disentanglement Another line of research is to extract latent disentangled representations into different factors of variations in data using VAEs. Earlier works such as β-VAE (Higgins et al., 2017) and Annealed VAE (Burgess et al., 2018) introduce additional weighting parameters to the KL divergence term of the original VAE ELBO loss. In Factor VAE (Kim & Mnih, 2018) and β-TCVAE (Chen et al., 2018) the ELBO is further decomposed to derive and penalize the total correlation to promote disentanglement in learned representations. For our purposes however, without an explicit parameterization of the cluster distributions to condition off of, it is not possible to introduce a physicsinformed expert MoE model.

# Multimodal inference

Generative modeling from multimodal data can be broadly categorized into either conditional generative models (Sohn et al., 2015;Pu et al., 2016) which directly learn conditional cross-modal distributions p(X i |X j ), or joint models (Suzuki et al., 2017;Vedantam et al., 2018;Wu & Goodman, 2018), which explicitly learn joint distributions that learn p(Z, X 1 , ..., X D ). We pursue the later as (Wu & Goodman, 2018) has been shown to provide better description of the underlying data distribution. We pursue the strategy used by works such as joint multimodal VAE (Suzuki et al., 2017) and joint VAE (Vedantam et al., 2018), where a a joint inference network q(Z|X 1 , X 2 ) is trained, followed by training of two additional unimodal inference networks q(Z|X 1 ) and q(Z|X 2 ) which handle missing data at test time. The unimodal inference networks are trained to either match the joint inference network or to maximize an ELBO derived to perform unimodal variational inference. More recently, MVAE (Wu & Goodman, 2018) and MMVAE (Shi et al., 2019) were proposed to model the joint posterior as a product of experts (PoEs) and a mixture of experts (MoEs). Most recently, MoPoE-VAE (Sutter et al., 2021) proposed a new ELBO formulation, which generalizes ELBO formulations derived from PoEs and MoEs. Our encoder bears similarities to MMVAE, MoPoE-VAE, and PoE, while preserving a computationally tractable closed form ELBO when combined with the GMM During training the posterior is sampled from a product of experts distribution fusing complementary information into a shared multimodal Gaussian distribution. A Gaussian mixture prior parameterizes clusters encoding cross-modal shared information. Sampling from mixture components provides generative models using either black-box decoders or expert physics models encoding prior physics knowledge. To facilitate cross-modal generative inference, unimodal embeddings are trained to reproduce the multimodal embedding, allowing inference of p(c|Xi). Shown here, an expert strain-hardening plasticity model allows two types of cross-modal inference: costly measurements of stress-strain response may be inferred from high-throughput imaging of lattice topology, or generative microstructural images can be provided to suggest microstructure which correlate with a given stress/strain measurement.

prior.

Physics-informed ML and fingerprinting Substantial works in recent years have focused on introducing physics into either solving partial differential equations (PDEs) or for building surrogates, typically introducing a PDE residual regularizer in physics-informed neural networks (Lagaris et al., 1998;Raissi et al., 2019) or by embedding physics directly into network architecture in structure-preserving ML (Trask et al., 2020). Such tools can be combined to provide parametric surrogates of simulations which can perform real-time inference over a database of parameterized PDE solutions (Lu et al., 2019;Wang et al., 2021;Mao et al., 2021). This paper provides a framework to fuse either these physics-informed surrogates or simpler empirical models together with experimental data. In contrast to traditional tools for fingerprinting which rely on purely data-driven techniques like PCA (Hasselmann, 1997;Hegerl et al., 2007), the current framework provides a means to incorporate domain expertise into fingerprints tailored toward a scientific task.

# Major contributions:

• Novel fusion of PoE w/ Gaussian mixture to obtain parameterized cluster "fingerprints" for downstream data analysis and high-throughput diagnostic tasks.

• Multimodal embedding allows cross-modal inference while preserving closed form expressions for expectations in ELBO.

• Mixture of experts decoding allows incorporation of interpretable inductive biases by assuming model form describing scientific processes. Potential for embedding physics-informed surrogates or simulators.

• Improvements over SotA unimodal unsupervised techniques.

• Disentanglement of clusters into structured latent space exposing relationships across modalities.

# Framework construction

Given individual modalities X i ⊂ R di , we partition the set of all modalities M = {X 1 , ..., X D } into M DD consisting of images/videos/audio amenable to purely data-driven modeling, and M S consisting of scientific modalities amenable to expert modeling. For each X i ∈ M we seek an embedding Z ∈ R l in latent dimension l << d i . Assuming a categorical variable c clustering data into C clusters in latent space, our variational autoencoder amounts to introducing parameterized prior p and posterior q distributions that maximize the following ELBO loss:

We further assume separability of both prior and posterior:

q(Z, c|X 1 , ..., X D ) = q(Z|X 1 , ..., X D )q(c|X 1 , ..., X D ).

(3)

Our framework consists of four components: 1. unimodal deep encodings with a product of experts (PoE) multimodal fusion, 2. a mixture of Gaussians prior, 3. a mixture of experts decoding of modalities X ∈ M S , and 4. unimodal encoders for cross-modal inference. We introduce each component sequentially, derive a closed form expression for the ELBO, and introduce an expectation maximization assignment of clusters and expert models.

## Multi-modal embedding

Assuming the unimodal embeddings may be modeled as multivariate Gaussians with diagonal covariance, we obtain posterior probabilities q(Z i |X i ) = N (Z i ; µ i , σ 2 i I), with mean and covariance provided by the set of neural networks

where θ i denotes trainable weights and biases. For this work we consider a simple class of 1D/2D convolutional encoders, whose architecture is provided in Appendix A.

To estimate q(Z|X 1 , ..., X D ) in the ELBO, it follows from Bayes' rule and pairwise independence that

so that the posterior is a scaled product of individual modalities. To obtain closed form expressions for the ELBO later, we assume

The product of Gaussian distributions is again Gaussian, yielding the multimodal distribution:

which may be sampled during training using the reparameterization trick: by sampling ∼ N (0, I) and calculating Z = µ + σ, we may back-propagate through the random node Z into the unimodal encoders, where denotes the Hadamard product.

## Gaussian mixture prior and expert decoding

We adopt a simple Gaussian mixture prior, modeling

To ensure a positive π that sums to unity, we parameterize it as the softmax of a trainable vector. To decode X i ∈ M DD , we employ a neural network with parameters θi

For X i ∈ M S , we assume an expert model p(X i |c) = N (E(t; θc ), σ2 c I), where t is an independent variable and θc denotes expert parameters associated with each cluster. The specific choice of E will be problem dependent and specified in the experiment section.

Because p(X i |Z, c) admits interpretation as a mixture of experts model (Jordan & Jacobs, 1994), we obtain closed form expressions for the mean and variance to facilitate postprocessing and uncertainty quantification:

In practice, E may take a variety of forms and its judicious selection imparts significant prior knowledge. We consider in this work simple generalized linear models and, for the mechanical data, an empirical linear strain-hardening model. In general, these could range from empirical engineering correlations obtained from e.g. dimensionless analysis or singular perturbation theory, to analytic parametric solutions to PDE based models, or to parametric physics-informed ML surrogates/reduce order models (see e.g. (Lu et al., 2019;Wang et al., 2021;Mao et al., 2021;Trask et al., 2020)).

## ELBO loss and EM minimizer

A modification of the derivation in (Jiang et al., 2017) to account for multimodality yields the closed form for the single sample ELBO:

where || • || denotes the 2 -norm, subscripts denote scalar components of tensors, γ c is the posterior distribution

we estimate q(c|X 1 , ..., X d ) = p(c|Z) = γ c following (Jiang et al., 2017), and we have taken σc = 1. The derivation may be found in Appendix B. We seek the minimizer of this loss over the entire data set:

In standard expectation-maximization fashion, we note that for fixed value of γ c , the variation of L with respect to the cluster centers µ c yields the global minimizer

where µ d and γ cd denote the encoded mean and posterior p(c|X 1 , ..., X D ) of the d th data point, respectively.

To facilitate batched access to large datasets, this may be calculated incrementally following the streaming algorithm outlined in Algorithm 1, alternating between an EM update for µ c followed by an Adam update (Kingma & Ba, 2014) of the remaining variables.

A weighted least squares problem for the optimal expert model parameters may be similarly obtained by taking the variation of the ELBO with respect to θc :

Efficient solution of this nonlinear least squares problem at each epoch will be dependent upon the problem-specific expert model and data stream, and to perform batching may require a streaming technique such as recursive least squares or Kalman filtering (Cioffi & Kailath, 1984). For simplicity, we update θc with Adam in this work but note that solving this at each epoch to ensure the expert model provides a best fit to the current partitions is likely to provide substantial improvement.

Algorithm 1 Training with streaming EM for cluster centers Input:

Calculate Adam update on ELBO end for end for

## Cross-modal inference

The primary objective of this work is to perform cross-modal inference: sampling from q(Z|X i ) allows: 1. generative modeling by decoding p(X j |Z) for i = j, and 2. an estimate of p(c|Z) via Eqn. (15). Unfortunately, sampling from the unimodal encoders q(Z|X i ) provides poor embeddings far from the multimodal embedding q(Z|X 1 , ..., X d ).

To remedy this, we introduce a second set of unimodal encoders q(Z|X i ) ∼ N (Z; μi , σ2 i I) with identical architecture to q(Z|X i ). After the multimodal network is trained, we minimize the KL-divergence between q(Z|X i ) and q(Z|X 1 , ..., X D ) so that the unimodal embeddings reproduce the multimodal one. In this sense, the unsupervised multimodal training provides labels which allows supervised training of unimodal embeddings. The KL loss admits the closed form expression

which may be sequentially optimized with Adam for each modality i after the multimodal model has been fit. An additional possibility not pursued here is to perform a Bayesian estimate to identify either the cluster most likely to generate the data

or the cluster centroid most likely to have generated the data

(20)

# Experiments

Hyper-parameters for both training and architecture were selected using the Weights and Biases experiment tracking tool (Biewald, 2020)   For the mechanical problem, a highthroughput compression test is performed on two populations of additively manufactured lattices corresponding to gyroid and octet microstructure (Garland et al., 2020). We supplement the resulting stress-strain curves X2 with images of the microstructure X1 to obtain low-and high-throughput modalities, respectively.

## Unsupervised multimodal MNIST

In the first experiment, we take the traditional MNIST dataset consisting of images X 1 and labels c ∈ {0, ..., 9} and manufacture a synthetic 1D modality X 2 = ct + , where t ∈ [0, 1] and ∼ N (0, 0.01) for a clean dataset or ∼ N (0, 0.5) for a noisy data set. We adopt the affine expert model E(t; θ c ) = θ c t, and perform unsupervised clustering of the multimodal dataset (X 1 , X 2 ), and additionally perform cross-modal inference. For this artificial problem, the labels are thinly veiled as the slope of second modality, and so we expect that if we successfully perform multimodal inference we should obtain accuracy comparable to a supervised MNIST benchmark.

We define unsupervised clustering accuracy (acc) as in (  

where N is the number of examples, M is the set of all possible mappings from a cluster to a label assignment, l i is the true label and c i is the cluster assignment by the model for example i. Calibration of the latent dimension (Figure 3) revealed l = 3 to be an optimal embedding dimension. In Table 1 we provide a comparison to classification accuracy against state of the art supervised and unsupervised models trained on images only. For multimodal inference with low noise we obtain perfect classification outperforming the current state-of-the-art in supervised classification and outperforming the state-of-the-art in unsupervised learning.

In addition to observing improved accuracy, we investigate in Figure 4 the disentangled representation of clusters and provide examples of generative models. Surprisingly, the sequential ordering of clusters in X 2 induces an sequential embedding of corresponding clusters in latent space. As noise is increased, the data in X 2 is sufficiently large to prevent distinct clustering into disentangled classes, however the ordering of digits is roughly preserved. When generative modeling is performed for X 2 , this is reflected by samples from the tail of the Gaussian mixture which generate images of adjacent digits. For example, the cluster of 2's contains images of 3's in its periphery. This suggests that the sequential ordering of data in X 2 may induce generative models for X 1 which reflect cross-modal ordering.  (An et al., 2020), (Jiang et al., 2017) and (Dilokthanakul et al., 2016) denoted by * , † and † †, respectively. If statistics were not provided we assume maximum accuracy was reported. While the data augmentation offered by X2 is not incorporated in comparisons to unimodal unsupervised benchmarks, a comparison to the supervised setting is valid. For all experiments we do not overparameterize and keep clusters equal to the number of digits. In this noisy case, this is reflected when sampling X1 from Zi ∈ {µc±3σc} i for clusters 1-9 (right): at the periphery of each cluster a digit ±1 is generated, reflecting the fuzzy class boundary of X2.

for multimodal and cross-modal classification in Figure 5 reveal an approximately banded structure, whereby misclassified modalities primarily occur between adjacent digits. While this single experiment is insufficient to remark on the generality of this result, it suggests the potential for learning generative models of images which reflect information from the expert model, a particularly exciting prospect for scientific datasets.

## Metal additive lattice fingerprinting

The lattice dataset consists of X 1 images of 3D printed lattices split between two types of printed metamaterials and corresponding X 2 stress/strain curves performed in a high-throughput uniaxial compression machine. Even with high-throughput testing, only 91 pairs of images were able to be generated, highlighting the utility of high-throughput photographs X 1 as surrogates to infer X 2 . We select as expert model a linear strain-hardening model partitioning the stress-strain response into two piecewise linear regions (Jones, 2009). Even a simple model like this succinctly encodes a large number of interpretable quantities of interest: a yield stress, together with elastic and plastic moduli. We gather in Figure 6 results from generative modeling and include in the appendix additional results demonstrating 94.74%/94.74%/94.74% classification accuracy of the two clusters for multimodal/X 1 /X 2 -cross-modal inferences, respectively. 

# Conclusions and future work

The present approach provides an abstract variational inference for discovering fingerprints in an unsupervised manner while incorporating physical model biases. This framework is widely applicable to a range of scientific disciplines where detection of fingerprints are crucial for tasks ranging from predicting and attributing climate change to designing biochemical pathways at a molecular level. In addition to the application focus on fingerprint generation, this framework may be used for a variety of general purpose downstream tasks based on multimodal processing of scientific data. For this work we have focused on a simple MNIST example to probe dynamics for an easily replicable and understandable dataset, along with a simple high-throughput manufacturing example to illustrate feasibility for facilitating high-throughput experimentation.

In future work, we will employ more sophisticated physics- informed surrogates as expert models for processes in additive manufacturing and semiconductor device design bridging multiscale and multifidelity information from data sources corresponding to both physical experiment (transmission electron microscopy, atom probe tomography, micro x-ray computerized tomography, or synchotron x-ray diffraction) and high-fidelity simulations (quantum density functional theory, molecular dynamics, crystal plasticity, and continuum mechanics). To date, these costly but rich sources of information are antagonistic to high-throughput testing and simulation. This framework provides an exciting platform for discovering data-driven scientific fingerprints which may be combined with advances in automated experimentation to accelerate scientific discovery.

# Software and Data

Pending acceptance, all data and code used to generate results will be hosted on a Github page. For now, we include a subset of the code to reproduce the MNIST examples through the anonymous Github1 ; unfortunately anonymous github does not offer enough storage to host the accompanying dataset.

we apply the separability assumptions p(X 1 , ..., X D , Z, c) = Π D i=1 p(X i |Z, c) p(Z|c)p(c), (23) q(Z, c|X 1 , ..., X D ) = q(Z|X 1 , ..., X D )q(c|X 1 , ..., X D ).

(24)

providing the additive decomposition L = E q(Z,c|X1,...,X D ) [log p(X 1 , ..., X D , Z)] -E q(Z,c|X1,...,X D ) [log q(Z, c|X 1 , ..., X D )] (25)

E q(Z,c|X1,...,X D ) [log p(X i |Z, c)] + E q(Z,c|X1,...,X D ) [log p(Z|c)] +E q(Z,c|X1,...,X D ) [log p(c)] -E q(Z,c|X1,...,X D ) [log q(Z|X 1 , ..., X D )]

-E q(Z,c|X1,...,X D ) [log q(c|X 1 , ..., X D )] .

For convenience we denote E q(Z,c|X1,...,X D ) = E q . The separability assumptions therefore decompose the ELBO into constituent expectations of the form

which may be integrated exactly for the Gaussian/categorical f and g appearing in the ELBO. The only term which may not be immediately computed is E q [log q(c|X 1 , ..., X D )]. The lack of a reparameterization trick for the categorical distribution precludes backpropagation into the encoder, forcing us to consider an encoder which only provides predictions for Z. While there are options to use e.g. a regularized Gumbel-softmax approximation to the categorical distribution (Jang et al., 2016), we would lose the tractability of the closed form expression for the ELBO. Instead we follow (Jiang et al., 2017) and approximate q(c|X 1 , ..., X D ) = p(c|Z) using the following justification.

Rewriting the ELBO L d = E q(Z,c|X1,...,X D ) log p(X 1 , ..., X D , Z) q(Z, c|X 1 , ..., X D )

= E q(Z,c|X1,...,X D ) log p(X 1 , ..., X D |Z)p(Z) q(Z|X 1 , ..., X D ) + log p(c|Z) q(c|X 1 , ..., X D ) = R l log p(X 1 , ..., X D |Z)p(Z) q(Z|X 1 , ..., X D ) dZ + D KL (q(c|X 1 , ..., X D )||p(c|Z)),

we seek extremal points with respect to c. The first term is independent of c, and the positive second term takes zero value when q(c|X 1 , ..., X D ) = p(c|Z), providing the desired maximum. We caution however that this holds only at local minima of the loss landscape, but empirically has been shown to perform well as an estimator.

Finally for completeness, we gather from (Jiang et al., 2017) the various integral formulas required to compute the expectations in closed form with modifications for our multimodal setting. 

where the integrand may be computed from Lemma B.1.

# Acknowledgements

The authors thank Warren Davis, Anthony Garland and Lekha Patel for providing guidance on the variational inference framework and review of the manuscript and Kat Reiner and Greg Geller for providing computing support. All authors acknowledge funding under the Beyond Fingerprinting Sandia Grand Challenge Laboratory Directed Research and Developement program. N. Trask acknowledges funding under the Collaboratory on Mathematics and Physics-Informed Learning Machines for Multiscale and Multiphysics Problems (PhILMs) project funded by DOE Office of Science (Grant number DE-SC001924) and the DOE Early Career program. Sandia National Laboratories is a multi-mission laboratory managed and operated by National Technology and Engineering Solutions of Sandia, LLC., a wholly owned subsidiary of Honeywell International, Inc., for the U.S. Department of Energy's National Nuclear Security Administration under contract DE-NA0003525. This paper describes objective technical results and analysis. Any subjective views or opinions that might be expressed in the paper do not necessarily represent the views of the U.S. Department of Energy or the United States Government. SAND number: SAND2022-1159 O

# Model Architectures

We employ relatively small convolutional architectures to serve as encoders for both modalities. The image modality encoder consists of 2 2D convolutional layers with 32 and 64 channels respectively, each with 3x3 kernels. We apply the exponential linear unit (ELU) activation function as well as batch normalization after each convolutional layer, then pass the output to a fully connected layer of size encoding d im × 2 to enable an embedding into a representation of the mean and standard deviation of the input in the latent space. For the 1D modality encoder, in place of 2D convolutional layers, we use 1D convolutions with 8 and 16 channels in the respective layers, but with an otherwise identical architecture.

The image decoder begins with a fully connected layer of appropriate size to be reshaped into 32 channels of 2D arrays, with each dimension having a length 1 4 of the length of the number of pixels per side of the original image. The reshaped output of the initial dense layer is passed into a series of 3 deconvolutional layers with 64, 32, and 1 channel respectively, each with a kernel size of 3. The first 2 deconvolutional layers use a stride of 3 and a Rectified Linear Unit (ReLU) activation function, and the final deconvolutional layer uses a stride of 1. Zero padding is used to retain the input shape while traversing these layers.

# Hyperparameters

We used the MNIST dataset along with the Weights and Biases tool (Biewald, 2020) to perform a hyperparameter search over learning rates and encoding dimension size. For the multimodal models, we found that a learning rate of 1.97e -5 gave the best result as measured by validation loss. For the MNIST dataset, an encoding dimension of size 3 gave the most consistent results, and we used a 2D encoding dimension for the lattice dataset. For the unimodal models, we found that a learning rate of 4.398e -5 for the image modality and a learning rate of 4.398e -3 for the 1D modality supported learning, but we leave a rigorous hyperparameter tuning for unimodal models for future work.

# Implementation details

Each of the input data modalities was normalized to have values in [0, 1]. The 1D data was sampled to generate an array of length 20 for MNIST and length 100 for the lattice stress-strain data. The lattice images were cropped and subsampled into quadrants resulting in images of dimension 152x152. We further augmented the dataset by flipping the images along each axis.

To train the MNIST multimodal models, we used 10% of the standard MNIST train set for validation, and selected the model with the lowest validation loss. We did not observe any indication of overfitting the multimodal model to the training data. All results reported are on the held out test dataset. For the MNIST unimodal models, we again did not observe overfitting when measuring model performance by accuracy to the cluster labels generated from the trained multimodal model, and we report results on the test set from the model resulting from the final training epoch.

We split the lattice dataset into a train/test 80/20 split. Since we did not observe overfitting during multimodal training, we selected the model with the lowest training loss and applied that model to the held out test set, and we report those results. We select the model resulting from the final training epoch for the unimodal tasks.

Our models are implemented in Python using Tensorflow (Abadi et al., 2016), and we leverage the Scikit-learn library (Pedregosa et al., 2011) for data preparation and accuracy metrics, Scipy (Virtanen et al., 2020) for data preparation and the linear sum assignment implementation of the Hungarian method (Kuhn, 1955) for efficient computation of the unsupervised cluster accuracy. We visualize our results using the Matplotlib (Hunter, 2007) and Seaborn (Waskom, 2021) libraries. Training was performed on NVIDIA DGX-1 and DGX-2 machines with each run executed on 1 GPU. A combination of P100 and V100 GPUs were used in this work. Training runs took on average approximately (machine dependent) 10-14 hours with our longest run on lattice data taking approximately one day. We made no attempt to optimize parallel training to improve run time or training efficiency.

# B. Derivation of ELBO

To derive a closed form expression for the single sample ELBO

= R l q(Z|X 1 , ..., X D ) log q(Z|X 1 , ..., X D )dZ,

where the integrand may be computed from Lemma B.1.

Lemma B.5.

E q(Z,c|X1,...,X D ) [log q(c|X 1 , ..., X D )] = R l q(Z|X 1 , ..., X D )dZ c q(c|X 1 , ..., X D ) log q(c|X 1 , ..., X D ),

= c q(c|X 1 , ..., X D ) log q(c|X 1 , ..., X D ).

For all terms, q(c|X 1 , ..., X D ) is calculated via the posterior estimator γ given in Equation ( 15).

