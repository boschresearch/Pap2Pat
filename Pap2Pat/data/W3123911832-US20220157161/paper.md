# Introduction

The ability to simulate realistic traffic scenarios is an important milestone on the path towards safe and scalable self-driving. It enables us to build rich virtual environments in which we can improve our self-driving vehicles (SDVs) and verify their safety and performance [9,31,32,53]. This goal, however, is challenging to achieve. As a first step, most large-scale self-driving programs simulate prerecorded scenarios captured in the real world [32] or employ teams of test engineers to design new scenarios [9,31]. Although this approach can yield realistic simulations, it is ultimately not scalable. This motivates the search for a way to generate realistic traffic scenarios automatically.

More concretely, we are interested in generating the layout of actors in a traffic scene given the SDV's current state and a high definition map (HD map) of the surround-* Indicates equal contribution. Work done at Uber ATG. ing area. We call this task traffic scene generation (see Fig. 1). Here, each actor is parameterized by a class label, a bird's eye view bounding box, and a velocity vector. Our lightweight scene parameterization is popular among existing self-driving simulation stacks and can be readily used in downstream modules; e.g., to simulate LiDAR [9,10,32].

A popular approach to traffic scene generation is to use procedural models to insert actors into the scene according to a set of rules [55,31,9,37]. These rules encode reasonable heuristics such as "pedestrians should stay on the sidewalk" or "vehicles should drive along lane centerlines", and their parameters can be manually tuned to give reasonable results. Still, these simplistic heuristics cannot fully capture the complexity and diversity of real world traffic scenes, thus inducing a content gap between synthesized traffic scenes and real ones [26]. Moreover, this approach requires significant time and expertise to design good heuristics and tune their parameters.

To address these issues, recent methods use machine learning techniques to automatically tune model parameters [52,51,24,26,8]. These methods improve the realism and scalability of traffic scene generation. However, they remain limited by their underlying hand-crafted heuristics and priors; e.g., pre-defined scene grammars or assumptions about road topologies. As a result, they lack the capacity to model the true complexity and diversity of real traffic scenes and, by extension, the fidelity necessary to train and test SDVs in simulation. Alternatively, we can use a simple data-driven approach by sampling from map-specific empirical distributions [10]. But this cannot generalize to new maps and may yield scene-inconsistent samples.

In this paper, we propose SceneGen-a traffic scene generation model that eschews the need for hand-crafted rules and heuristics. Our approach is inspired by recent successes in deep generative modeling that have shown remarkable results in estimating distributions of a variety of data, without requiring complex rules and heuristics; e.g., handwriting [18], images [49], text [39], etc. Specifically, SceneGen is a neural autoregressive model that, given the SDV's current state and an HD map of the surrounding area, sequentially inserts actors into the scene-mimicking the process by which humans do this as well. As a result, we can sample realistic traffic scenes from SceneGen and compute the likelihood of existing ones as well.

We evaluate SceneGen on two large-scale self-driving datasets. The results show that SceneGen can better estimate the distribution over real traffic scenes than competing baselines and generate more realistic samples as well. Furthermore, we show that SceneGen coupled with sensor simulation can generate realistic labeled data to train perception models that generalize to the real world. With Sce-neGen, we take an important step towards developing SDVs safely and scalably through large-scale simulation. We hope our work here inspires more research along this direction so that one day this goal will become a reality.

# Related Work

Traffic simulation: The study of traffic simulation can be traced back to at least the 1950s with Gerlough's dissertation on simulating freeway traffic flow [16]. Since then, various traffic models have been used for simulation. Macroscopic models simulate entire populations of vehicles in the aggregate [30,40] to study "macroscopic" properties of traffic flow, such as traffic density and average velocity. In contrast, microscopic models simulate the behavior of each individual vehicle over time by assuming a car-following model [36,6,34,13,17,1,44]. These models improve simulation fidelity considerably but at the cost of computational efficiency. Microscopic traffic models have been included in popular software packages such as SUMO [31], CORSIM [35], VISSIM [11], and MITSIM [55].

Recently, traffic simulation has found new applications in testing and training the autonomy stack of SDVs. However, existing simulators do not satisfy the level of realism necessary to properly test SDVs [52]. For example, the CARLA simulator [9] spawns actors at pre-determined locations and uses a lane-following controller to simulate the vehicle behaviors over time. This approach is too simplistic and so it induces a sim2real content gap [26]. Therefore, in this paper, we study how to generate snapshots of traffic scenes that mimic the realism and diversity of real ones.

Traffic scene generation: While much of the research into microscopic traffic simulation have focused on modeling actors' behaviors, an equally important yet underexplored problem is how to generate realistic snapshots of traffic scenes. These snapshots have many applications; e.g., to initialize traffic simulations [52] or to generate labeled data for training perception models [26]. A popular approach is to procedurally insert actors into the scene according to a set of rules [55,31,9,37]. These rules encode reasonable heuristics such as "pedestrians should stay on the sidewalk" and "vehicles should drive along lane centerlines", and their parameters can be manually tuned to give reasonable results. For example, SUMO [31] inserts vehicles into lanes based on minimum headway requirements and initializes their speeds according to a Gaussian distribution [52]. Unfortunately, it is difficult to scale this approach to new environments since tuning these heuristics require significant time and expertise. An alternative approach is to learn a probabilistic distribution over traffic scenes from which we can sample new scenes [52,51,24,10,14,15,57]. For example, Wheeler et al. [52] propose a Bayesian network to model a joint distribution over traffic scenes in straight multi-lane highways. This approach was extended to model inter-lane dependencies [51] and generalized to handle a four-way intersection [24]. These models are trained to mimic a real distribution over traffic scenes. However, they consider a limited set of road topologies only and assume that actors follow reference paths in the map. As a result, they are difficult to generalize to real urban scenes, where road topologies and actor behaviors are considerably more complex; e.g., pedestrians do not follow reference paths in general.

Recent advances in deep learning have enabled a more flexible approach to learn a distribution over traffic scenes. In particular, MetaSim [26] augments the probabilistic scene graph of Prakash et al. [37] with a graph neural network. By modifying the scene graph's node attributes, MetaSim reduces the content gap between synthesized images versus real ones, without manual tuning. MetaSim2 [8] extends this idea by learning to sample the scene graph as well. Unfortunately, these approaches are still limited by their hand-crafted scene grammar which, for example, constrains vehicles to lane centerlines. We aim to develop a  more general method that avoids requiring these heuristics.

Autoregressive models: Autoregressive models factorize a joint distribution over n-dimensions into a product of conditional distributions p(x) = n i=1 p(x i |x <i ). Each conditional distribution is then approximated with a parameterized function [12,2,45,46,47]. Recently, neural autoregressive models have found tremendous success in modeling a variety of data, including handwriting [18], images [49], audio [48], text [39], sketches [20], graphs [29], 3D meshes [33], indoor scenes [50] and image scene layouts [25]. These models are particularly popular since they can factorize a complex joint distribution into a product of much simpler conditional distributions. Moreover, they generally admit a tractable likelihood, which can be used for likelihood-based training, uncovering interesting/outlier examples, etc. Inspired by these advances, we exploit autoregressive models for traffic scene generation as well.

# Traffic Scene Generation

Our goal is to learn a distribution over traffic scenes from which we can sample new examples and evaluate the likelihood of existing ones. In particular, given the SDV a 0 ∈ A and an HD map m ∈ M, we aim to estimate the joint distribution over other actors in the scene {a 1 , . . . , a n } ⊂ A,

The HD map m ∈ M is a collection of polygons and polylines that provide semantic priors for a region of interest around the SDV; e.g., lane boundaries, drivable areas, traffic light states. These priors provide important contextual information about the scene and allow us to generate actors that are consistent with the underlying road topology.

We parameterize each actor a i ∈ A with an eightdimensional random variable containing its class label c i ∈ C, its bird's eye view location (x i , y i ) ∈ R 2 , its bounding box b i ∈ B1 , and its velocity v i ∈ R 2 . Each bounding box b i ∈ B is a 3-tuple consisting of the bounding box's size (w i , l i ) ∈ R 2 >0 and heading angle θ i ∈ [0, 2π). In our experiments, C consists of three classes: vehicles, pedestrians, and bicyclists. See Fig. 1 for an example.

Modeling Eq. 1 is a challenging task since the actors in a given scene are highly correlated among themselves and with the map, and the number of actors in the scene is random as well. We aim to model Eq. 1 such that our model is easy to sample from and the resulting samples reflect the complexity and diversity of real traffic scenes. Our approach is to autoregressively factorize Eq. 1 into a product of conditional distributions. This yields a natural generation process that sequentially inserts actors into the scene one at a time. See Fig. 2 for an overview of our approach.

In the following, we first describe our autoregressive factorization of Eq. 1 and how we model this with a recurrent neural network (Sec. 3.1). Then, in Sec. 3.2, we describe how SceneGen generates a new actor at each step of the generation process. Finally, in Sec. 3.3, we discuss how we train and sample from SceneGen.

## The Autoregressive Generation Process

Given the SDV a 0 ∈ A and an HD map m ∈ M, our goal is to estimate a conditional distribution over the actors in the scene {a 1 , . . . , a n } ⊂ A. As we alluded to earlier, modeling this conditional distribution is challenging since the actors in a given scene are highly correlated among themselves and with the map, and the number of actors in the scene is random. Inspired by the recent successes of neural autoregressive models [18,49,39], we propose to autoregressively factorize p(a 1 , . . . , a n |m, a 0 ) into a product of simpler conditional distributions. This factorization simplifies the task of modeling the complex joint distribution p(a 1 , . . . , a n |m, a 0 ) and results in a model with a tractable likelihood. Moreover, it yields a natural generation process that mimics how a human might perform this task as well.

In order to perform this factorization, we assume a fixed canonical ordering over the sequence of actors a 1 , . . . , a n , p(a 1 , . . . , a n |m, a 0 ) = p(a 1 |m, a 0 )

where a <i = {a 1 , . . . , a i-1 } is the set of actors up to and including the i -1-th actor in canonical order. In our experiments, we choose a left-to-right, top-to-bottom order based on each actor's position in bird's eye view coordinates. We found that this intuitive ordering works well in practice.

Since the number of actors per scene is random, we introduce a stopping token ⊥ to indicate the end of our sequential generation process. In practice, we treat ⊥ as an auxillary actor that, when generated, ends the generation process. Therefore, for simplicity of notation, we assume that the last actor a n is always the stopping token ⊥.

Model architecture: Our model uses a recurrent neural network to capture the long-range dependencies across our autoregressive generation process. The basis of our model is the ConvLSTM architecture [42]-an extension of the classic LSTM architecture [22] to spatial data-and the input to our model at the i-th generation step is a bird's eye view multi-channel image encoding the SDV a 0 , the HD map m, and the actors generated so far {a 1 , . . . , a i-1 }.

For the i-th step of the generation process: Let x (i) ∈ R C×H×W denote the multi-channel image, where C is the number of feature channels and H × W is the size of the image grid. Given the previous hidden and cell states h (i-1) and c (i-1) , the new hidden and cell states are given by:

where ConvLSTM is a two-layer ConvLSTM, CNN b is a five-layer convolutional neural network (CNN) that extract backbone features, and w are the neural network parameters. The features f (i) summarize the generated scene so far a <i , a 0 , and m, and we use f (i) to predict the conditional distribution p(a i |a <i , m, a 0 ), which we describe next. See our appendix for details.

## A Probabilistic Model of Actors

Having specified the generation process, we now turn our attention to modeling each actor probabilistically. As discussed earlier, each actor a i ∈ A is parameterized by its class label

To capture the dependencies between these attributes, we factorize p(a i |a <i , m, a 0 ) as follows:

where we dropped the condition on a <i , m, and a 0 to simplify notation. Thus, the distribution over an actor's location is conditional on its class; its bounding box is conditional on its class and location; and its velocity is conditional on its class, location, and bounding box. Note that if a i is the stopping token ⊥, we do not model its location, bounding box, and velocity. Instead, we have p(a i ) = p(c i ), where c i is the auxillary class c ⊥ . 

# SceneGen M etaSim L ane Gr aph L ayoutVAE Ar gover se

where avg-pool : R C×H×W → R C is average pooling over the spatial dimensions and MLP c is a three-layer multilayer perceptron (MLP) with softmax activations.

Location: We apply uniform quantization to the actor's position and model the quantized values using a categorical distribution. The support of this distribution is the set of H × W quantized bins within our region of interest and its parameters π loc are predicted by a class-specific CNN. This approach allows the model to express highly multimodal distributions without making assumptions about the distribution's shape [49]. To recover continuous values, we assume a uniform distribution within each quantization bin. Let k denote an index into one of the H × W quantized bins, and suppose p k ∈ R 2 (resp., p k ∈ R 2 ) is the minimum (resp., maximum) continuous coordinates in the k-th bin. We model p(x i , y i |c i ) as follows:

where CNN loc (•; c i , w) is a CNN with softmax activations for the class c i . During inference, we mask and renormalize π loc such that quantized bins with invalid posi-tions according to our canonical ordering have zero probability mass. Note that we do not mask during training since this resulted in worse performance.

After sampling the actor's location (x i , y i ) ∈ R 2 , we extract a feature vector f

xi,yi ∈ R C by spatially indexing into the k-th bin of f (i) . This feature vector captures local information at (x i , y i ) and is used to subsequently predict the actor's bounding box and velocity.

Bounding box: An actor's bounding box b i ∈ B consists of its width and height (w i , l i ) ∈ R 2 >0 and its heading θ i ∈ [0, 2π). We model the distributions over each of these independently. For an actor's bounding box size, we use a mixture of K bivariate log-normal distributions:

where π box are mixture weights, each µ box,k ∈ R 2 and Σ box,k ∈ S 2 + parameterize a component log-normal distribution, and MLP box (•; c i , w) is a three-layer MLP for the class c i . This parameterization allows our model to naturally capture the multi-modality of actor sizes in real world data; e.g., the size of sedans versus trucks.

Similarly, we model an actor's heading angle with a mixture of K Von-Mises distributions:

where π θ are mixture weights, each µ θ,k ∈ [0, 2π) and κ θ,k > 0 parameterize a component Von-Mises distribu- 

where I 0 is the modified Bessel function of order 0. We use a mixture of Von-Mises distributions to capture the multimodality of headings in real world data; e.g., a vehicle can go straight or turn at an intersection. To sample from a mixture of Von-Mises distributions, we sample a component k from a categorical distribution and then sample θ from the Von-Mises distribution of the k-th component [3].

Velocity: We parameterize the actor's velocity v i ∈ R 2 as v i = (s i cos ω i , s i sin ω i ), where s i ∈ R ≥0 is its speed and ω i ∈ [0, 2π) is its direction. Note that this parameterization is not unique since ω i can take any value in [0, 2π) when v i = 0. Therefore, we model the actor's velocity as a mixture model where one of the K ≥ 2 components corresponds to v i = 0. More concretely, we have

where for k > 0, we have

and for k = 0, we have v i = 0. As before, we use threelayer MLPs to predict the parameters of each distribution.

For vehicles and bicyclists, we parameterize ω i ∈ [0, 2π) as an offset relative to the actor's heading θ i ∈ [0, 2π). This is equivalent to parameterizing their velocities with a bicycle model [43], which we found improves sample quality.

## Learning and Inference

Sampling: Pure sampling from deep autoregressive models can lead to degenerate examples due to their "unrealiable long tails" [23]. Therefore, we adopt a sampling strategy inspired by nucleus sampling [23]. Specifically, at each generation step, we sample from each of SceneGen's output distributions M times and keep the most likely sample. We found this to help avoid degenerate traffic scenes while maintaining sample diversity. Furthermore, we reject vehicles and bicyclists whose bounding boxes collide with those of the actors sampled so far.

Training: We train our model to maximize the loglikelihood of real traffic scenes in our training dataset:

log p(a i,1 , . . . , a i,n |m i , a i,0 ; w) (24) where w are the neural network parameters and N is the number of samples in our training set. In practice, we use the Adam optimizer [27] to minimize the average negative log-likelihood over mini-batches. We use teacher forcing and backpropagation-through-time to train through the generation process, up to a fixed window as memory allows.

# Experiments

We evaluate SceneGen on two self-driving datasets: Argoverse [7] and ATG4D [54]. Our results show that Sce-neGen can generate more realistic traffic scenes than the competing methods (Sec. 4.3). We also demonstrate how SceneGen with sensor simulation can be used to train perception models that generalize to the real world (Sec. 4.4). of 5500 25-seconds logs which we split into a training set of 5000 and an evaluation set of 500. Each log is subsampled at 10Hz to yield 250 traffic scenes, and each scene is annotated with bounding boxes for vehicles, pedestrians, and bicyclists. Each log also provides HD maps that encode lane boundaries, drivable areas, and crosswalks as polygons, and lane centerlines as polylines. Each lane segment is annotated with attributes such as its type (car vs. bike), turn direction, boundary colors, and traffic light state.

## Datasets

In our experiments, we subdivide the training set into two splits of 4000 and 1000 logs respectively. We use the first split to train the traffic scene generation models and the second split to train the perception models in Sec. 4.4.

Argoverse: Argoverse [7] consists of two datasets collected by a fleet of SDVs in Pittsburgh and Miami. We use the Argoverse 3D Tracking dataset which contains track annotations for 65 training logs and 24 validation logs. Each log is subsampled at 10Hz to yield 13,122 training scenes and 5015 validation scenes. As in ATG4D, Argoverse provides HD maps annotated with drivable areas and lane segment centerlines and their attributes; e.g., turn direction. However, Argoverse does not provide crosswalk polygons, lane types, lane boundary colors, and traffic lights.

## Experiment Setup

Baselines: Our first set of baselines is inspired by recent work on probabilistic scene grammars and graphs [37,26,8]. In particular, we design a probabilistic grammar of traffic scenes (Prob. Grammar) such that actors are randomly placed onto lane segments using a hand-crafted prior [37]. Sampling from this grammar yields a scene graph, and our next baseline (MetaSim) uses a graph neural network to transform the attributes of each actor in the scene graph. Our implementation follows Kar et al. [26], except we use a training algorithm that is supervised with heuristically generated ground truth scene graphs. 2Our next set of baselines is inspired by methods that reason directly about the road topology of the scene [52,51,24,32]. Given a lane graph of the scene, Procedural uses a set of rules to place actors such that they follow lane centerlines, maintain a minimum clearance to leading actors, etc. Each actor's bounding box is sampled from a Gaussian KDE fitted to the training dataset [5] and velocities are set to satisfy speed limits and a time gap between successive actors on the lane graph. Similar to MetaSim, we also consider a learning-based version of Procedural that uses a lane graph neural network [28] to transform each actor's position, bounding box, and velocity (Lane Graph).

Since the HD maps in ATG4D and Argoverse do not provide reference paths for pedestrians, the aforementioned baselines cannot generate pedestrians.3 Therefore, we also compare against LayoutVAE [25]-a variational autoencoder for image layouts that we adapt for traffic scene generation. We modify LayoutVAE to condition on HD maps and output oriented bounding boxes and velocities for actors of every class. Please see our appendix for details.

Metrics: Our first metric measures the negative loglikelihood (NLL) of real traffic scenes from the evaluation distribution, measured in nats. NLL is a standard metric to compare generative models with tractable likelihoods. However, as many of our baselines do not have likelihoods, we compute a sample-based metric as well: maximum mean discrepancy (MMD) [19]. For two distributions p and q, MMD measures a distance between p and q as

for some kernel k. Following [56,29], we compute MMD using Gaussian kernels with the total variation distance to compare distributions of scene statistics between generated and real traffic scenes. Our scene statistics measure the distribution of classes, bounding box sizes, speeds, and heading angles (relative to the SDV) in each scene. To peer into the global properties of the traffic scene, we also compute MMD in the feature space of a pre-trained motion forecasting model that takes a rasterized image of the scene as input [53]. This is akin to the popular IS [41], FID [21], and KID [4] metrics for evaluating generative models, except we use a feature extractor trained on traffic scenes. Please see our appendix for details. Additional details: Each traffic scene is a 80m × 80m region of interest centered on the ego SDV. By default, Sce-neGen uses K = 10 mixture components and conditions on all available map elements for each dataset. We train Sce-neGen using the Adam optimizer [27] with a learning rate of 1e-4 and a batch size of 16, until convergence. When sampling each actor's position, heading, and velocity, we sample M = 10 times and keep the most likely sample.

## Results

Quantitative results: Tab. 1 summarizes the NLL and MMD results for ATG4D and Argoverse. Overall, Scene-Gen achieves the best results across both datasets, demonstrating that it can better model real traffic scenes and synthesize realistic examples as well. Interestingly, all learning-based methods outperform the hand-tuned baselines with respect to MMD on deep features-a testament to the difficulty of designing good heuristics.

Qualitative results: Fig. 3 visualizes samples generated by SceneGen on ATG4D and Argoverse. Fig. 4 compares traffic scenes generated by SceneGen and various baselines. Although MetaSim and Lane Graph generate reasonable scenes, they are limited by their underlying heuristics; e.g., actors follow lane centerlines. LayoutVAE generates a greater variety of actors; however, the model does not position actors on the map accurately, rendering the overall scene unrealistic. In contrast, SceneGen's samples reflects the complexity of real traffic scenes much better. That said, SceneGen occassionally generates near-collision scenes that are plausible but unlikely; e.g., Fig. 3 top-right.

Ablation studies: In Tab. 2, we sweep over the number of mixture components used to parameterize distributions of bounding boxes and velocities. We see that increasing the number of components consistently lowers NLL, reflecting the need to model the multi-modality of real traffic scenes. We also ablate the input map to SceneGen: starting from an unconditional model, we progressively add lanes, drivable areas, crosswalks, and traffic light states. From Tab. 3, we see that using more map elements generally improves NLL. Surprisingly, incorporating traffic lights slightly degrades performance, which we conjecture is due to infrequent traffic light observations in ATG4D.  Discovering interesting scenes: We use SceneGen to find unlikely scenes in ATG4D by searching for scenes with the highest NLL, normalized by the number of actors. Fig. 5 shows an example of a traffic violation found via this procedure; the violating actor has an NLL of 21.28.

## Sim2Real Evaluation

Our next experiment demonstrates that SceneGen coupled with sensor simulation can generate realistic labeled data for training perception models. For each method under evaluation, we generate 250,000 traffic scenes conditioned on the SDV and HD map in each frame of the 1000 held-out logs in ATG4D. Next, we use LiDARsim [32] to simulate the LiDAR point cloud corresponding to each scene. Finally, we train a 3D object detector [54] using the simulated LiDAR and evaluate its performance on real scenes and Li-DAR in ATG4D.

From Tab. 4, we see that SceneGen's traffic scenes exhibit the lowest sim2real gap. Here, Real Scenes is simulated LiDAR from ground truth placements. This reaffirms our claim that the underlying rules and priors used in MetaSim and Lane Graph induce a content gap. By eschewing these heuristics altogether, SceneGen learns to generate significantly more realistic traffic scenes. Intriguingly, Lay-outVAE performs competitively despite struggling to position actors on the map. We conjecture that this is because LayoutVAE captures the diversity of actor classes, sizes, headings, etc. well. However, by accurately modeling actor positions as well, SceneGen further reduces the sim2real gap, as compared to ground truth traffic scenes.

# Conclusion

We have presented SceneGen-a neural autoregressive model of traffic scenes from which we can sample new examples as well as evaluate the likelihood of existing ones. Unlike prior methods, SceneGen eschews the need for rules or heuristics, making it a more flexible and scalable approach for modeling the complexity and diversity of real world traffic scenes. As a result, SceneGen is able to generate realistic traffic scenes, thus taking an important step towards safe and scalable self-driving.

At each step of the generation process, SceneGen takes a bird's eye view multi-channel image encoding the HD map m, the SDV a 0 , and the actors generated so far {a 1 , . . . , a i-1 }. The image emcompasses an 80m × 80m region of interest centered on the SDV a 0 and has a resolution of 0.25m per pixel, yielding a 320 × 320 image. The HD map is rasterized into a multi-channel image describing all available map elements in each dataset. For ATG4D, our multi-channel image consists of: lane polygons (straight vehicle lanes, dedicated right vehicle lanes, dedicated left vehicle lanes, dedicated bus lanes, and dedicated bike lanes); lane centerlines and dividers (allowed to cross, forbidden to cross, and maybe allowed to cross); lane segments (straight vehicle lanes, dedicated right vehicle lanes, and dedicated left vehicle lanes); drivable area and road polygons; and crosswalk polygons. In addition, we also encode each lane segment's traffic light state (green, yellow, red, flashing yellow, flashing red, and unknown), speed limit, and orientation as filled lane polygons. Note that orientation angles are encoded in their Biternion representations θ = (cos θ, sin θ) [16]. In aggregate, this yields a 24-channel image.

Argoverse provides a more limited set of map elements. Here, our multi-channel image consists of: lane polygons; lane centerlines (all lanes, left turn lanes, right turn lanes, intersection lanes, and traffic-controlled lanes); lane orientations (in Biternion representation); and drivable area polygons. In aggregate, this yields a 9-channel image.

To encode the actors a 0 , a 1 , . . ., we rasterize their bounding boxes onto a collection of binary occupancy images [1], one for each class; i.e., SDV, vehicles, pedestrians, and bicyclists. Furthermore, we encode their headings and velocities by rasterizing their bounding boxes onto a five-channel image, filled with their respective speed, direction, and heading. As before, direction and heading angles are encoded in their Biternion representations. See Fig. 1 for an example.

## Model Architecture

The basis of our model is the ConvLSTM architecture [19]. Let x (i) ∈ R C×H×W denote the input multi-channel image at the i-th step of the generation process. Given the previous hidden and cell states h (i-1) and c (i-1) , the new hidden states h (i) , cell states c (i) , and backbone features f (i) are given by:

correlation term ρ ∈ [-1, 1] (using tanh) such that:

Similarly, we model the distribution over heading angles with a mixture of K Von-Mises distributions whose parameters are predicted by another three-layer MLP:

where π θ ∈ ∆ K-1 are mixture weights and each µ θ,k ∈ [0, 2π) and κ θ,k > 0 parameterize a component Von-Mises distribution. Following Prokudin et al. [16], we parameterize each µ with its Biternion representation µ = (cos µ, sin µ) and each κ is predicted in log-scale. Note that we use separate MLP weights for each class in C whose actors are represented by bounding boxes; i.e., vehicles and bicyclists. Pedestrians are represented by their center of gravity only (i.e., location).

Velocity: Each of MLP v , MLP s , and MLP ω is a three-layer MLP with the same architecture as described above. We parameterize the mixture of K Von-Mises distributions for directions ω just as we parameterize the distribution of headings.

As before, we use separate MLP weights for each class in C.

## Training Details

We train our model to maximize the log-likelihood of real traffic scenes in our training dataset:

where w are the neural network parameters and N is the number of samples in our training set. We use teacher forcing and backpropagation-through-time to train through the generation process, up to a fixed window as memory allows. On a Nvidia Quadro RTX 5000 with 16GB of GPU memory, we train through 25 generation steps with batch size of 1 per GPU. We use PyTorch [14] and Horovod [18] to distribute the training process over 16 GPUs with a total batch size of 16. During training, we also randomly rotate each traffic scene with θ ∈ [0, 2π). Note that each summand log p(a 1 , . . . , a n |m; w) can be decomposed into a sum of the log-likelihoods for each actors; namely, we have

where ξ i encapsulates the conditions on a <i , m, and a 0 , to simplify notation. Therefore, the first summand log p(c i |ξ i ) is the (negative) cross-entropy loss between the predicted parameters π c and the ground truth class c i ∈ C ∪ {⊥}. We describe the remaining summands in detail next.

# Location:

The second summand log p(x i , y i |c i , ξ i ) measures the log-likelihood the actor's location (x i , y i ) ∈ R 2 . As discussed earlier, we uniformly quantize each actor's location and parameterize it with a categorical distribution. Therefore, log p(x i , y i |c i , ξ i ) is the (negative) cross-entropy loss between the predicted parameters π loc and the actor's ground truth quantized location. To address the significant imbalance of positive versus negative locations here, we use online negative hard mining. Specifically, we normalize π loc over the hardest 10,000 locations only (including the positive location), and compute log p(x i , y i |c i , ξ i ) based this restricted categorical distribution instead.

# Bounding box:

The third summand log p(b i |c i , x i , y i , ξ i ) is a sum of the log-likelihoods of the actor's bounding box size

Since we model bounding box size with a mixture of K bivariate log-normal distributions, we have

where π ∈ ∆ K-1 are mixture weights and each

Similarly, since we model heading angles with a mixture of K Von-Mises distributions, we have

where π ∈ ∆ K-1 are mixture weights and each µ k ∈ [0, 2π) and κ k > 0 parameterize a component Von-Mises distribution.

Velocity: The fourth summand log p(v i |c i , x i , y i , b i , ξ i ) is the log-likelihood of the actor's velocity v i ∈ R 2 , which we parameterize as v i = (s i cos ω i , s i sin ω i ) where s i ∈ R ≥0 is its speed and ω i ∈ [0, 2π) is its direction. Recall that we model the distribution over an actor's velocity as a mixture model where one of the K ≥ 2 components corresponds to v i = 0. Therefore, for v i = 0, we have

and for v i > 0, we have

where π ∈ ∆ K-1 are mixture weights, each µ s,k ∈ R and σ s,k > 0 parameterize a component log-normal distribution for speed s i , and each µ ω,k ∈ [0, 2π) and κ ω,k > 0 parameterize a component Von-Mises distribution for direction ω i .

# Additional Experiment Details

## Baselines

Prob. Grammar: Our Prob. Grammar baseline is inspired by recent work on probabilistic scene grammars [15,9,3].

Here, traffic scenes are composed by placing actors onto lane segments in the HD map, and initializing their classes, sizes, headings, velocities according to a hand-crafted prior. In our experiments, we use the following scene grammar:

Scene → Lanes ( 14)

Lane → Actors ( 16)

where Actor and are terminal symbols. Sampling from this scene grammar yields a scene graph, which defines the scene structure-where lane segments are and which actors are positioned on top of them-and scene parameters-the attributes of each lane segment and actor. In our setting, we are given the lane nodes (and the SDV actor's node) of the scene graph as a condition, and our goal is to insert/modify the actor nodes. Drawing inspiration from MetaSim's probabilistic scene grammar [9], we first uniformly sample the maximum number of actors per lane segment and then place them along the lane centerline, with a random clearance between successive actors drawn from the exponential distribution. The class of each actor is determined by the lane segment under consideration (i.e., car lane vs. bike lane); its lateral offset from the lane centerline is given by uniform noise; its bounding box size is sampled from a uniform distribution; its heading and the direction of its velocity is given by the direction of the lane segment plus some uniform noise; and its speed is the minimum of a sample from a uniform distribution and the lane segment's speed limit. The parameters of every distribution are tuned by hand. MetaSim: Our next baseline (MetaSim) uses a graph neural network (GNN) to transform the attributes of each actor node in the given scene graph. We use the implementation of Kar et al. [9] for this purpose. Specifically, given a scene graph drawn from Prob. Grammar, MetaSim deterministically modifies each actor's distance along its lane centerline, lateral offset, bounding box size, heading, and velocity. The inputs to MetaSim is a scene graph where each node's features are its attributes (normalized between 0 and 1 based on their respective minimum/maximum values under the prior), and the outputs of MetaSim are each node's new attributes (again normalized between 0 and 1). We use the GNN architecture of Kar et al. [9]: a three-layer GNN encoder with 32 → 64 → 128 features channels and a three-layer GNN decoder with 128 → 64 → 32 feature channels. Additionally, we use linear layers to encode and decode the per-node attributes. Note that we train MetaSim using a supervised algorithm with heuristically generated ground truth scene graphs. In particular, given a real traffic scene, we first associate each actor to a lane segment; if this is not possible, the actor is not included in the scene graph. Next, we modify the attributes of each actor according to Prob. Grammar's prior. Finally, this modified scene graph is given as input to MetaSim, and we train MetaSim to transform the modified attributes back to their original ones. In our setting, this training process was both faster and more stable than the original unsupervised algorithm.

Procedural: Our Procedural baseline is inspired by methods that operate directly on the road topology of the traffic scene [21,20,7,13]. Specifically, given a lane graph of the scene [10], Procedural uses a set of rules to place actors onto lane centerlines. First, we determine a set of valid routes traversing the entire lane graph. Each valid route is a sequence of successive lane centerlines along which actors can traverse without violating traffic rules; e.g., running red lights, merging onto an oncoming lane, etc. Next, we place actors onto each route such that successive actors maintain a random clearance (drawn from an exponential distribution) and no two actors collide. Each actor's bounding box size is sampled form a Gaussian KDE fitted to the training dataset, and its heading is determined by the tangent vector along its lane centerline at its location. Finally, we initialize the speed of each actor such that successive actors maintain a random time gap (drawn from an exponential distribution). Procedural is similar to the heuristics underlying [21,20,7] but generalized to handle arbitrary road topologies. Similar to Prob. Grammar, Procedural can generate only vehicles and bicyclists since existing HD maps do not provide sidewalks. We believe this limitation highlights the difficulty of using a heuristics-based approach.

Lane Graph: Inspired by MetaSim, we also consider a learning-based version of Procedural. Specifically, given a traffic scene generated by Procedural, we use a lane graph neural network to transform the attributes of each actor; i.e., location, bounding box size, heading, and velocity. Our lane graph neural network follows the design of the state-of-the-art motion forecasting model by Liang et al. [10]. It consists of MapNet for extracting map topology features and four fusion modules: actor-to-lane, lane-to-lane, lane-to-actor, and actor-to-actor. We train Lane Graph using heuristically generated ground truth, as in our MetaSim baseline. LayoutVAE: Our implementation of LayoutVAE largely follows that of Jyothi et al. [8]. To adapt LayoutVAE to traffic scene generation, we first augment the original model with an additional CNN to extract map features. In particular, given a bird's eye view multi-channel image of the HD map, we use the backbone architecture of Liang et al. [11] to extract multiscale map features, which we subsequently average-pool into a feature vector. This is then given to LayoutVAE as input in place of the label set encoding used in the original setting2 . Our second modification enables LayoutVAE to output oriented bounding boxes and velocities. Specifically, we replace the spherical quadrivariate Gaussian distribution of its BBoxVAE with a bivariate Gaussian distribution for location, a bivariate log-normal distribution for bounding box size, and a bivariate Gaussian distribution for velocity. To evaluate the log-likelihood of a scene, we use Monte-Carlo approximation with 1000 samples from the conditional prior [8].

## MMD Metrics

To complement our likelihood-based metric, we compute a sample-based metric as well: maximum mean discrepancy (MMD) [4]. As we discussed in the main text, MMD measures a distance between two distributions p and q as

for some kernel k. Following [24,12], we compute MMD using Gaussian kernels (with bandwidth σ = 1) with the total variation distance to compare scene statistics between generated and real traffic scenes. In particular, we first sample a set P of real traffic scenes from the evaluation dataset. Conditioned the SDV state and HD map of the scenes in P , we generate a set Q of synthetic scenes using the method under evaluation. Then, we approximate MMD as:

Our scene statistics measure the distribution of classes, bounding box sizes (in m 2 ), speeds (in m/s), and heading angles (relative to that of the SDV) for each scene. Empty scenes are discarded since these scene statistics are undefined. Since MMD is expensive to compute, in ATG4D, we form P by sampling the evaluation dataset by every 25th scene, yielding approximately 5000 scenes. We compute MMD over the full Argoverse validation set as it contains 5015 scenes only.

We also compute MMD in the feature space of a pre-trained motion forecasting model. This is similar to some popular metrics for evaluating generative models such IS [17], FID [5], and KID [2], except we use a motion forecasting model as our feature extractor. Here, our motion forecasting model takes a bird's eye view multi-channel image of the actors in the scene and regresses the future locations of each actor over the next 3 seconds in 0.5s increments. We use the actor rasterization procedure described in Sec. 1.1 and the model architecture from [22], and we train the model using 4000 training log from the ATG4D training set. To obtain a feature vector summarizing the scene, we average pool the model's backbone features along its spatial dimensions. Then, to compute MMD, we use the RBF kernel with bandwidth σ = 1. 

# Additional Experiment Results

## Vehicle MMD Metrics

In Tab. 1, we report vehicle-only MMD metrics for ATG4D and Argoverse. Specifically, we compute scene statistics for generated and real traffic scenes using vehicle actors only. As before, scenes with no vehicles are discarded during evaluation. This allows for an alternative comparison that controls for the class most easily handled by heuristics; i.e., vehicles. Overall, we see that SceneGen still achieves the best results among the competing methods. This result reaffirms our claim that heuristics-based methods are insufficient to model the full complexity and diversity of real world traffic scenes.

## Sampling Strategy Analysis

As discussed in the main text, SceneGen uses a sampling strategy inspired by nucleus sampling [6]. Specifically, at each generation step, we sample each of SceneGen's position, heading, and velocity distributions M times and return the most likely sample as output. In Tab. 2 and Fig. 2, we analyze the effects of using different numbers of sample proposals M = 1, 10, 20. We see that using M > 1 decreases MMD on deep features, indicating that scene-level realism is improved. This improvement is even more evident in Fig. 2, where we see vehicles disregarding the rules of traffic when M = 1. With more fine-grained tuning of M , we expect to see improvements in the actor-level statistics as well; i.e., class, size, and speed.

# Additional Qualitative Results

In Fig. 3 and4, we present an array of additional qualitative results for ATG4D and Argoverse respectively. Here, we compare traffic scenes generated by SceneGen, MetaSim, Lane Graph, and LayoutVAE. From these visualizations, we see that SceneGen generates traffic scenes that best reflect the complexity and diversity of real world traffic scenes. For example, in the second-to-last row of Fig. 3, we show a traffic scene generated by SceneGen in which a vehicle performs a three-point turn. In the bottom row of Fig. 3, we also show a scene in which two bicyclists perform an left turn using the car lane. These scenes highlight SceneGen's ability to model rare but plausible traffic scenes that could occur in the real world.

In Fig. 5 and 6, we also showcase the diversity of traffic scenes that SceneGen is able to generate. Each row in the figures show four samples from our model when given the same SDV state and HD map as inputs. From these visualizations, we see that SceneGen captures the multi-modality of real world traffic scenes well. For example, the top row of Fig. 5 shows four traffic scenes generated for a four-way intersection. Here, we see samples in which pedestrians cross the intersection, vehicles perform an unprotected left turn, and a large bus goes straight.

Finally, in Fig. 7, we visualize the quantized location heatmaps for steps t = 0, 5, 10, 15, 20 of the generation process. Each row shows the categorical distribution from which we sample the next actor's location. From these visualizations, we see that SceneGen is able to model the distribution over actor locations (and the corresponding uncertainties) quite precisely. For example, the distribution over vehicle locations are concentrated around lane centerlines and the distribution over pedestrian locations are diffused over crosswalks and sidewalks. 

# Gener ated Tr affic Scene

Step 20 

