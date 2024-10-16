# Introduction

Learning semantically meaningful representations has been a vital step in numerous computer vision applications such as representation learning [60,68], contentbased visual retrieval [26,25,36,53], person or vehicle re-identification [69,56,34], and face verification [30,18]. Deep Convolutional Neural Networks (CNNs) have proven repeatedly their effectiveness in the large spectrum of applications [11,10,14,58,6,13,12] including Deep Metric Learning (DML). The neural networks in DML are trained to map the data to a lower-dimensional embedding space in which similar data (data in the same class) are pulled to-R@1 Epochs Figure 1. Accuracy in Recall@1 versus epochs on the Cars-196 [29] dataset. Note that all methods were trained on a single Quadro p5000 GPU with a batch size of 100. Our method achieves the highest accuracy while converging at the same order as the proxy-based baselines in terms of the number of epochs.

gether and the dissimilar data (data in different classes) are pushed away [53,61]. For such an embedding space, rich representations and special loss functions are inevitable.

High image retrieval often requires global and local representations [7]. The global features [47,1], or "global descriptors" compactly summarize the contents of an image. Often global descriptors are taken from the deepest layers in CNNs; therefore, they only involve the most abstract information, and the vital identifiers such as geometry and spatial information are lost. On the other hand, local features [4,33], involve information about the geometry and spatial information of the input image. Generally speaking, global features lead to better recall, while local features are essential in better precision [7]. A typical retrieval system setup takes advantage of both global and local features in its final embeddings to obtain the best of both worlds.

Recently, self-attention or Second-Order Attention (SOA) in feature space has received a significant attraction [55,59,38,54,65]. The SOA can be considered as a spatial enhancement technique that reflects the correlation among spatial locations and enhances the highly correlated parts of the feature map. Although recent deep-learningbased global descriptors provide effective ways to aggregate features into a compact global vector, they have not explored the correlations of low-level and high-level features within feature maps simultaneously. The other vital factor in DML is the loss function. The loss functions are essential to provide a powerful supervisory signal based on the problem objectives [25,61]. The loss functions in the DML problems are classified into pairwisebased [61,48,57,50,41], and proxy-based [36,25,53] models. The pairwise-based losses are built based on comparing the pairwise distances between data in the batch. While the pairwise-based losses provide a strong supervisory signal for training the model by considering data-todata relations [50,61], they suffer from sample mining and slow convergence [25].

The proxy-based losses address the above issues by introducing a limited number of proxies [36,25,53]. A proxy is a representative of a subset of training data (for instance, a proxy per class) and learned along with network parameters. Since the number of proxies is substantially smaller than the data-points, the proxy-based models benefit from faster convergence rates than the pairwise-based losses. Note the proxy-based models are associated with data-to-proxy relations and they miss the rich supervisory information of data-to-data relations.

In this paper, we propose a multi-head network that benefits from the fast convergence of the proxy-based loss functions and rich data-to-data relation of the pairwisebased models. Although we are using a hybrid of both proxy-based and pairwise-based loss functions in our multihead network, our approach does not introduce any hyperparameter tuning for tuple sampling. Our framework also involves an SOA mechanism to exploit the correlation between features at different spatial locations to further enhance the deep local and global features. Also, we combine both global and local descriptors to produce the final descriptor that holds the content information as well as geometry and spatial information to efficiently select the most similar images. With the above advantages, our proposed method achieves state-of-the-art performance in terms of Recall@1 and quickly converges as exhibited in Figure 1.

The contribution of this paper unfolds as follows: (a) We propose a multi-head network that takes advantage of both pairwise-based and proxy-based methods; it leverages rich data-to-data relations and enables fast and reliable convergence. (b) We explore the SOA for further enhancement of both local and global features based on higher-order information. (c) We demonstrate the impact of using local and global descriptors, proxy-based and pairwise-based, SOA, and the embedding dimensions via a thorough ablation study on their effects. (d) An embedding neural network trained with our approach achieves state-of-the-art performance on four publicly available benchmarks for metric learning [29,63,42,31].

# Related Work

In this section, we categorize the DML approaches based on their use of descriptors and loss functions into two broad categories, then we review relevant papers in each category.

## Loss Functions

Loss functions in DML can be divided into two groups, pairwise-based and proxy-based.

Pairwise-based Losses. Contrastive loss [8,19] and Triplet loss [48,57] are influential examples of loss functions for pairwise-based DML. Contrastive loss takes a pair of embedding vectors as input and aims to push them apart if they are of different classes or pull them together if they are of the same class. Triplet loss considers a data point as an anchor. Each anchor is associated with a positive (an embedding with an identical class label to the anchor) and a negative data point (an embedding with different class labels) and involves the distance of the anchor-positive pair to be smaller than that of the anchor-negative pair in the embedding space.

One potential issue with pairwise-based models is that a large number of tuples have a limited contribution to the learning algorithm and sometimes even diminish the quality of the learned embedding space [64]. To address this issue, most pairwise-based losses [50,43,62] employ hard sample mining techniques [64,20]. However, these techniques involve tuning hyper-parameters and consequently increases the risk of over-fitting. Pairwise-based losses are rich in data-to-data relations. However, the number of tuples increases polynomially with regard to the number of training data, resulting in prohibitive complexity and significantly slow convergence [25].

Proxy-based Losses. Proxy-based metric learning endeavors to address the complexity and slow convergence issue of the pairwise-based losses. The proxy-based methods require a small set of proxies to capture the global structure of an embedding space and assign each data point to relevant proxies instead of the other data points during training. Since the number of proxies is significantly smaller than the training data, the training complexity reduces substantially. For instance, Proxy-NCA [36] loss assigns a single proxy to each class and associates data points to each proxy and encourages positive pairs to be close together and negative pairs to be far apart. Proxy-NCA++ [53] is an extension of the Proxy-NCA and aims to enhance the limitations of the Proxy-NCA in terms of temperature factor and pooling layer.

SoftTriple loss [46], inspired by the Proxy-NCA yet assigns multiple proxies to each class instead of one to improve the likelihood of capturing the intra-class variance. Proxy-Anchor loss [25] assigns a proxy to each class and treats each proxy as an anchor and assigns positive and negative pairs to each anchor. Although introducing proxies in proxy-based losses significantly improves the convergence in model training, it has an inherent limitation of data-toproxy relation instead of data-to-data relation that results in limited supervisory information. Our multi-head network overcomes this limitation by proposing a hybrid approach involves in both pairwise-based and proxy-based methods to benefit data-to-data relations as well as high convergence rates.

## Descriptors

DML algorithms can be divided into three groups based on their use of descriptors: local descriptors, global descriptors, and joint local and global descriptors.

Local Descriptors. Hand-engineered features such as SIFT [33] and SURF [4] have been widely used and adopted for retrieval systems especially before the deep learning era.

The key advantage of local features over global ones for image retrieval is their capacity to perform spatial matching, often by utilizing RANSAC [15]. Due to the efficiency of local features, recently, several deep learning-based local features have been proposed [66,39,35,44].

Global Descriptors. Global descriptors are often involved the most abstract information about the input, leading to high-performance image retrieval. Before the deep learning era, most global descriptors were obtained using the combination of local descriptors [23,24]. However, recently Joint Local and Global Descriptors. Global descriptors are essential for high recalls yet local descriptors are necessary for better precision; therefore, researchers develop hybrid methods to take advantage of both descriptors. For instance, Taira et al. [52] used NetVLAD [2] to extract global features for candidate pose retrieval, followed by dense local feature matching using feature maps from the same network for indoor localization. Simeoni et al. 's DSM [49] detected key points in activation maps from global feature models. Activation channels are interpreted as visual words, to propose correspondences between a pair of images. Cao et al. [7] extracted global and local features from the same network. They utilize the global descriptors to retrieve the most similar images and then re-rank the retrieved images by local descriptors to increase the precision.

# Proposed Algorithm

Our proposed algorithm involves two essential components: Refined deep local and global representations along with a multi-head loss function that enables the data-to-data relation as well as fast convergence. Our model design is illustrated in Figure 2.

## Deep Global and Local Representations

We propose to leverage hierarchical representations from a CNN to represent different types of descriptors. While deep layers are associated with the most abstract representations and representing higher-level features, the intermediate layers are more informative in terms of local representations and lower-level features.

Given an image, from the backbone we obtain two feature maps: f l ∈ R H l ×W l ×C l and f g ∈ R Hg×Wg×Cg , representing local (l) and global (g) feature maps where H, W, C indicate the height, width, and number of channels respectively. For off-the-shelf convolutional networks, H g ≤ H l , W g ≤ W l , and C g ≥ C l ; indicating that deeper layers have larger number of channels and spatially smaller feature maps.

## Second-Order Attention (SOA)

Let (i I , j I ) in the input image (I) correspond to location (i, j) in feature map f . To incorporate higher-order spatial information into the feature map, we adopt the second-order attention block [55,38]. A computational flow of the SOA concept is shown in Figure 3. For each feature map, we produce two projections of feature map f named query q, and key k, each obtained through 1 × 1 2d-convolutions with possible reduction of number of channels (d). Then, by flattening both tensors, we obtain both q and k in R d×hw . The second-order attention map A is computed as follows:

where ζ is a scaling factor and a ∈ R hw×hw , indicating the correlation of each f i,j to the whole map f . A third projection of f and value v is then obtained by 1 × 1 2dconvolution, and after flattening, results in R hw×d shape. Then, the second-order attention map f soa is obtained from linear combination of the first-order features f and the second-order attention map:

where ϕ is yet another 1 × 1 convolution to manage the effect of the obtained attention map. Thus, a new feature f soa i,j in the second-order map f soa ∈ R h×w×d , is a function of features from all locations in f :

where h denotes the combination of all convolutional operations within the non-local block.

## Pooling

To aggregate deep activations in both global and local features, we adopt the combination of Global Max Pooling (GMP) and Global Average Pooling (GAP) as follows:

After the aggregation, we whiten the aggregated representation for both refined local and global representations; we integrate this into our model with two separated fullyconnected layers. The fully connected layer associated with enhanced local representations

indicates the number of channels in the f soa l and D 2 is the dimension of the local embedding space. Similarly, we have a fully connected layer associated with enhanced global representations

indicates the number of channels in the f soa g and D 2 is the dimension of the global embedding space. After computing F l ∈ R D/2 and F g ∈ R D/2 , the final embedding F ∈ R D computes by concatenation of the F l and F g .

## A Hybrid Loss Function

Our loss is designed to overcome the limitation of both proxy-based and pairwise-based models by introducing a hybrid loss involving the proxy-anchor [25] loss from the proxy-based category and the MS [61] loss from the pairwise-based class.

Proxy-based Loss. Proxy-anchor loss [25] assigns a proxy to each class. Proxy-anchor approach considers each proxy as an anchor and associate it with entire data in a batch to find positive and negative samples. The proxy-anchor loss defined as follows:

where δ > 0 is a margin, α > 0 is a scaling factor, P is the set of all proxies, s(., .) measures the similarity among its arguments ,and P + indicates the set of positive proxies of data in the batch. Also, for each proxy p, a batch of embedding vectors X is divided into the set of positive X + p and negative X - p = X -X + p embedding vectors. By utilizing the proxy-anchor loss we incorporate datato-proxy relations as well as fast convergence. For incorporating the data-to-data relation, we integrate the MS loss.

Pairwise-based Loss. We employ the MS loss [61] as a pairwise-based loss since it considers the self, negative, and positive similarities. Self-similarity ensures that the instances belonging to a positive class remains closer to the anchor than the instances associated with negative classes. The positive similarity exclusively deals with positive pairs. σ represents the similarity margin that controls the closeness of positive pairs by heavily penalizing those pairs whose cosine similarities are less or equal to σ. The negative similarity ensures that negative samples have similarity with the anchor as low as possible. The MS loss function is formulated as follows:

Table 1. Recall@K (%) on the Cars-196 [29] and CUB-200-2011 [63] datasets. Superscripts indicate embedding sizes. Backbone networks of the models are denoted by abbreviations: G-GoogleNet [51], BN-Inception with batch normalization [22], R50-ResNet50 [21]. For each group of methods, the best performance is bolded and the second best is underlined.

# Algorithms BackBone

Cars-196 CUB-200-2011 R@1 R@2 R@4 R@8 R@1 R@2 R@4 R@8 Clustering 64 [ where γ, β, and σ are hyper-parameters. m is the number of samples, P i ,N i represents positive and negative samples, and S i,j denotes the pairwise similarity between x i and x j .

Our Objective Function. Our hybrid objective function is a combination of proxy-anchor and MS losses balanced by normalization factor λ:

# Experimental Results

In this section, our method is compared with current state-of-the-art methods on four public benchmark datasets employed for deep metric learning [29,63,42,31]. We also perform a thorough investigation of local and global features, the SOA, the MS loss and proxy-anchor loss, and embedding dimensionality to study their effects on the proposed method.

## Dataset

We evaluated our model on the CUB-200-2011 [63], Cars-196 [29], Stanford Online Product (SOP) [42] and In-Shop Clothes Retrieval (In-Shop) [31] datasets. For CUB-200-2011, we set aside 5,864 images of its first 100 classes as a training set and 5,924 images of the other classes as a test set. For Cars-196, 8,054 images of its first 98 classes are set aside as a training set and 8,131 images of the other classes are used as a test set. For SOP, we follow the standard dataset split in [43,25,53] using 59,551 images of  

## Implementation Setup

Backbone: For a fair comparison [37] to recent works, the Resnet50 [21] pre-trained on ImageNet classification [9] is adopted as our backbone network.

# Global and Local Features:

For all experiments on all datasets, we obtained the global features from resnet50-conv5-x∈ R 7×7×2084 layer and local features are extracted from resnet50-conv4-x∈ R 14×14×1024 .

Training: In all of the experiments, AdamW algorithm [32] has been adopted and used as our optimizer. AdamW has the same update step as Adam [28] with separate decays of weights. In all experiments, our model is trained only for 20 epochs and the initial learning rate is fixed to 10 -4 . Note that the learning rate for proxies is set to 10 -2 for faster convergence.

Proxy Setting: We assign a single proxy to each class as suggested in Proxy-NCA [36] and Proxy-Anchor [25]. The proxies are initialized with a normal distribution.

Input Setting: To have a fair comparison with state-of-theart methods, the input is re-scaled to 256 × 256 and then center-cropped to 224 × 224. We used random cropping and horizontal flipping during training as the data augmentation strategy, as suggested in [25,36]. During the test, the images are only center-cropped. The default size of cropped images is fixed to 224 × 224 [37].

Hyperparameter Setting: ζ in Eq. 1 is set to 1. α and δ in Eq. 5 is set to 32 and 10 -1 respectively. γ, β, and σ in Eq. 6 are set to 2, 50, 1. Finally, λ in Eq. 7 is set to 3 × 10 -2 , for all experiments.

## Comparison to Other Methods

We demonstrate the strength of our proposed method quantitatively by evaluating its image retrieval performance on four public benchmark datasets. For a fair comparison to the previous arts [37], the accuracy of our model is computed in three different settings: we used 64 1, our model outperforms all the previous stateof-the-art methods including the proxy-based [25,36,53], pairwise-based [62,61,46] and ensemble methods [27] in all three settings often with a large margin on top 1 recall. In particular, on the challenging Cars-196 dataset, our method improves the previous best score by a large margin, 2.3%, 5.3%, and 2.4% in Recall@1 in embedding size of 64, 128, and 512 respectively. As reported in Table 2, our model also achieves state-of-the-art performance on the SOP dataset. It outperforms previous methods in all cases except for Recall@10 and Recall@100 in 64-dimensional embedding, but even in these cases, it achieves the second best. Finally, on the In-Shop dataset, it obtains the best scores in all two settings as shown in Table 3. On the In-Shop dataset, our model outperforms the state-of-the-art by a large margin of 2.7% in Recall@1. In our experimental results, we noted that our model outperforms numerous stateof-the-art methods even with low-dimensional embedding vectors while they have higher embedding dimensions. This observation suggests that our model is capable of learning a more compact and effective embedding space. Last but not least, our hybrid method converges in the same order as the proxy-based method as results are summarized in Figure 1.

## Qualitative Results

To further exhibiting the visual performance of our method, we illustrate the qualitative retrieval results of our model on four datasets in Figure 4. Note that these datasets are challenging especially due to their large intra-class variations. For instance, the CUB200-2011 has a variety of poses and background clutter, the Cars-196 has various colors and shapes, and SOP and In-Shop datasets have challenging view-points of objects that make the retrieval tasks even harder. In contrast to all of these challenges, our proposed method performs robust retrieval.

## Ablation Study

Local and Global Features. To investigate the impact of the local and global features on the performance of our proposed method, we examined the Recall@1 while training than the global descriptors but neither of these descriptors individually achieved the performance as the combination of these descriptors obtained on both datasets based on Recall@1 performance (see Table 1).

Second-order Attention. One of the vital components of our proposed method is SOA. We employ this attention mechanism to further enhance deep features based on their correlation. To evaluate the impact of the SOA, we trained our model with and without having the SOA, and the results are summarized in Figure 5 (b). According to this figure, the performance of the model significantly improves in terms of Recall@1 when the model is trained with SOA especially on critical datasets like CUB-200-2011. This observation confirms our assumption on the essence of higher-order attention for further enhancements of the representations. We visualize the effects of second-order attention in Figure 9. This figure exhibits the attention map of samples from Cars-196 and CUB-200-2011 datasets. For each image, four parts have been selected with different stars and different colors. The attention map associated with each star has a border with identical colors. For locations in the background, interestingly, the attention from that feature is distributed within the main object in the image. It confirms the second-order attention has learned to focus on the main object in the image to accurately retrieve the most similar images to the query. On the other hand, when the star is located within the main object, the attention is on highly distinctive regions.

A Single Head Attention. Our proposed method requires two attention heads for local and global descriptors. We are interested in probing a test case with having only a single attentional head for both local and global descriptors. After extracting local descriptor f l ∈ R 14×14×1024 and global descriptor f g ∈ R 7×7×2048 from backbone, we use a focus layer [5] to reshape the local descriptor f new l ∈ R 7×7×4096 to spatially match the global descriptor. Then, we concatenate the global and local descriptors resulting in a combined feature map f ∈ R ∈7×7×6144 . Then, we apply the SOA for further enhancement of this feature map. We evaluated this approach on Cars-196 and CUB-200-2011 datasets. The single head attention obtained 86.6% and 66.6% in terms of Recall@1 on Cars-196 and CUB-200-2011, respectively. Note the obtained results are slightly degraded from the multi-head approach 90.1% on Cars-196 and 70.6% on CUB-200-2011 (see Table 1), that suggests the multi-head SOA is necessary.

Multisimilarity and Proxy-anchor Loss. The other crucial component of our architecture is the combination of pairwise-based and proxy-based loss functions. To study the impact of each loss function on our proposed method, we trained our model separately with MS loss and proxy anchor loss and we evaluated the performance based on Recall@1 on Cars-196 and CUB-200-2011 datasets. The results is exhibited in Figure 7. This Figure demonstrates that the combination of these two losses are crucial in our design since none of them individually achieves our performance (see Table 1).

Embedding Dimension. The dimension of embedding vectors is a vital factor that controls the trade-off between speed and accuracy in image retrieval systems. We thus investigate the effect of embedding dimensions on the retrieval accuracy in our method. We evaluated our model with embedding dimensions varying from 64 to 2048 following the experiment in [61,25]. The result of the analysis is illustrated in Figure 8, in which the retrieval performance of our model is reported on both Cars-196 and CUB-200-2011 dataset. The performance of our loss is fairly stable when the dimension is equal to or larger than 128. The performance of our model on the Cars-196 dataset improves until reach-ing 1024 dimensional embedding and after that slightly degrades. On the other hand, the performance consistently increases with the embedding dimension on the CUB-200-2011 dataset showing that more information on that dataset helps the retrieval performance.

# Conclusion

We have proposed a novel metric learning algorithm that takes the best of both proxy-based and pairwise-based losses. Also, it leverages enhanced local and global descriptors to improve the recall and precision simultaneously. Our method benefits from having a reach data-to-data relation as well as fast and reliable convergence. We extensively evaluated our model on 4 public benchmarks and our model has achieved state-of-the-art performance on all datasets in terms of Recall@1 accuracy. Also, our model converged quickly without any careful data sampling technique. 

# Additional Experimental Results

This supplementary material exhibits additional experimental results excluded from the main paper due to space limitation. Section 6.1 analyzes the impact of the batch size in our framework. Section 6.2 visualizes attention maps generated from Cars-196 [29] and CUB-200-2011 [63]. Section 6.3 provides additional qualitative results including, image retrieval results of our model compared with MS [61] and Proxy-Anchor [25] losses, and t-SNE visualization of the learned embedding space on four benchmark datasets [29,63,42,31].

## Impact of Batch size

To investigate the impact of the batch size on the performance of our proposed method, we examined the Recall@1 by training our model on both Cars-196 and CUB-200-2011 datasets by varying batch sizes from 30 to 120. The result of the analysis is summarized in Table 4 where it reveals our model is robust in terms of batch sizes, especially for batch sizes larger or equal to 60.

## Second-Order Attention

We visualize the effects of second-order attention in Fig- ure 9. This Figure exhibits the attention map of samples from Cars-196 and CUB-200-2011 datasets. For each image, four parts have been selected with different stars and different colors. The attention map associated with each star has a border with identical colors. For locations in the background (row 2, col 2 or row 4, col 3), interestingly, the attention from that feature is distributed within the main object in the image. It confirms the second-order attention has learned to focus on the main object in the image to accurately retrieve the most similar images to the query. On the other hand, when the star is located within the main object, the attention is on highly distinctive regions(row 1, col 3 or row 2, col 4).

## Additional Qualitative Results

More qualitative examples for image retrieval on Cars-196 and CUB-200-2011 datasets are exhibited in Figure 10 and Figure 11, respectively. The results of our model are compared with the MS loss -from the pairwise-based classand Proxy-Anchor -from the proxy-based category-using the same backbone network. The overall results demonstrate that our model learned better embedding space than our baselines. In the examples in the 2nd, 3rd, 5th and 6th rows of Figure 10, the MS loss and proxy anchor loss picked wrongful images while our hybrid loss retrieved the most similar cars to the query. Also, in Figure 11 MS and Proxy-Anchor loss missed several images, but our approach was able to retrieve the most similar images to the query. Even in Figure 11, row 1 that our model wrongfully retrieved the first image, but as one can see, the image is significantly similar to the query image in terms of appearance.

Based on the qualitative results given in Figures 10 and11, one can see that our model produces accurate results. Also, the example in the first row of Figure 11 shows successful retrievals despite different view-point and color changes. Figures 12, 13 , 14 and 15 exhibit t-SNE visualizations of the embedding spaces learned by our hybrid loss on the test sets of the four benchmark datasets. The results demonstrate that all data points in the embedding space have relevant nearest neighbors, which suggests that our model learns a semantic similarity that can be generalized even in the test set.       

# Acknowledgements

This research work was sponsored by the Office of Naval Research (ONR) via contract N00014-17-C-2007.

Disclaimer: The views and conclusions contained herein are those of the authors and should not be interpreted as necessarily representing the official positions, policies or endorsements, either expressed or implied, of ONR or the U.S. Government.

