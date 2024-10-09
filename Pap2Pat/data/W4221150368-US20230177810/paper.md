# Introduction

Visual scenes are naturally composed of semanticallyrelated groups of pixels. The relationship between grouping and recognition has been studied extensively in visual understanding even before the deep learning era [56,57]. In bottom-up grouping, the idea is to first re-organize pixels into candidate groups and then to process each group with a recognition module. This pipeline has been successfully applied in image segmentation from superpixels [64], constructing region proposals for object detection [80,102] and semantic segmentation [3]. Beyond bottom-up inference, top-down feedback from recognition can also provide signals to perform better visual grouping [79,101].

* Jiarui Xu was an intern at NVIDIA during the project.

# GroupViT

Text Encoder However, on moving to the deep learning era, the ideas of explicit grouping and recognition have been much less separated and more tightly coupled in end-to-end training systems. Semantic segmentation, e.g., is commonly achieved via a Fully Convolutional Network [51], where pixel grouping is only revealed at the output by recognizing each pixel's label. This approach eliminates the need to perform explicit grouping. While this method is very powerful and still delivers state-of-the-art performance, there are two major limitations that come with it: (i) learning is limited by the high cost of per-pixel human labels; and (ii) the learned model is restricted only to a few labeled categories and cannot generalize to unseen ones.

Recent developments in learning visual representations from text supervision have shown tremendous success on transferring to downstream tasks [63]. The learned model can not only be transferred to ImageNet classification in a zero-shot manner and achieve state-of-the-art performance, but can also perform recognition on object categories beyond ImageNet. Inspired by this line of research, we ask the question: Can we also learn a semantic segmentation model purely with text supervision, and without any perpixel annotations, capable of generalizing to different sets of objects categories, or vocabularies, in a zero-shot manner?

To accomplish this, we propose to bring back the grouping mechanism into deep networks, which allows semantic segments to emerge automatically with only text supervision. An overview of our approach is illustrated in Fig. 1. By training on large-scale paired image-text data with contrastive losses, we enable the model to be zero-shot transferred to several semantic segmentation vocabularies, without requiring any further annotation or fine-tuning. Our key idea is to leverage the Vision Transformer (ViT) [24] and incorporate a new visual grouping module into it.

We call our model GroupViT (Grouping Vision Transformer). Compared to convolutional neural networks (Con-vNets), which operate on regular grids, the global selfattention mechanism of Transformers naturally provides the flexibility to combine visual tokens into non-grid-like segments. Thus, instead of organizing visual tokens into grids, as recent ViT-based applications [17,25,48,86] do, we propose to perform hierarchical grouping of visual tokens into irregular-shaped segments. Specifically, our GroupViT model is organized in different stages through a hierarchy of Transformer layers, where each stage contains multiple Transformers to perform information propagation among the group segments, and a grouping module that merges smaller segments into larger ones. With different input images, our model dynamically forms different visual segments, each intuitively representing a semantic concept.

We train GroupViT with text supervision only. To perform learning, we merge visual segment outputs in the final stage of GroupViT using average pooling. We then compare this image-level embedding to those derived from textual sentences via contrastive learning. We construct positive training pairs by using corresponding image and text pairs, and negative ones by using text from other images. We extract the text embedding with a Transformer model, trained jointly along with GroupViT from scratch. Interestingly, even though we only provide textual training supervision at the image level, we find that semantically meaningful segments automatically emerge using our grouping architecture.

During inference, for the task of semantic segmentation, given an input image, we extract its visual groups using GroupViT (Fig. 1). Each final group's output represents a segment of the image. Given a vocabulary of label names for segmentation, we use the text Transformer to extract each label's textual embedding. To perform semantic segmentation, we then assign the category labels to image segments according to their mutual similarity in the embedding space. In our experiments, we show that GrouViT trained on the Conceptual Caption [11,68] and Yahoo Flickr Creative Commons [74] datasets with text supervision alone, can transfer to semantic segmentation tasks on the PASCAL VOC [26] and PASCAL Context [58] datasets in a zero-shot manner. Without any fine-tuning, we achieve a mean intersection over union (mIoU) of 52.3% on PASCAL VOC 2012 and an mIoU of 22.4% on PASCAL Context, performing competitively to state-of-the-art transfer-learning methods requiring greater levels of supervision. To our knowledge, our work is the first to perform semantic segmentation on different label vocabularies in a zero-shot manner with text supervision alone, without requiring any pixel-wise labels.

Our contributions are the following:

• Moving beyond regular-shaped image grids in deep networks, we introduce a novel GroupViT architecture to perform hierarchical bottom-up grouping of visual concepts into irregular-shaped groups. • Without any pixel-level labels and training and with only image-level text supervision using contrastive losses, GroupViT successfully learns to group image regions together and transfers to several semantic segmentation vocabularies in a zero-shot manner. • To our knowledge, ours is the first work to explore zero-shot transfer from text supervision alone to several semantic segmentation tasks without using any pixel-wise labels and establishes a strong baseline for this new task.

# Related Work

Vision Transformer. Inspired by the success of Transformers in NLP [22,81], the Vision Transformer (ViT) [24] was recently proposed and has been successfully applied to multiple computer vision tasks, including image classification [48,77,78,92], object detection [48,84,95], semantic segmentation [48,87,98]  Genome [38]. To scale up learning, weakly-supervised visual grounding has been introduced where the bounding box and text correspondence is not available during training [12,31,45,46,83,91]. However, to localize object bounding boxes these approaches still rely on pre-trained object detectors [83,91], which, in turn, utilize box annotations from other datasets. While related, we emphasize there are two main differences between our problem setting and that of visual grounding: (i) We train our model on millions of noisy image-text pairs from the web, while visual grounding requires human curated and annotated data at a relatively smaller scale; (ii) Our GroupViT provides a bottom-up mechanism for progressive visual grouping where object segments automatically emerge with text supervision, while visual grounding needs bounding box annotations borrowed from other datasets. Semantic Segmentation with Less Supervision. Multiple research directions have been proposed to learn to segment with less supervision than dense per-pixel labels. For example, few-shot learning [23,47,54,59,75,82,90] and active learning [9,67,71,72,88] are proposed to perform segmentation with as few pixel-wise labels as possible. Going further, zero-shot approaches [7,41] are proposed to learn segmentation models for unseen categories without using pixel-wise labels for them. However, it still requires learning with segmentation labels on seen categories as the initial step. Another line of re-lated research is of weakly-supervised semantic segmentation [1,10,28,34,39,43,70,73,85], which aims to learn semantic segmentation with only image-level object category supervision. While it largely reduces supervision, it still requires manual labeling using a finite vocabulary on a carefully-curated image dataset. Different from all previous work, our approach completely gets rid of human annotations and GroupViT is trained with large-scale noisy text supervision. Instead of a fixed vocabulary, we show that GroupViT can be generalized to any set of categories in a zero-shot manner for semantic segmentation.

The concurrently developed unpublished text-supervised semantic segmentation methods [30,89,93,99] also show promising results. One major difference between these methods and GroupViT is that, they exploit vision-language model [33,63] pre-trained on well-prepared large-scale private dataset with 400M-1.8B image-text pairs, while our GroupViT is trained from scratch with much noisier public datasets (30M images in total) to learn grouping and segmentation and yet achieves competitive performance. Among these works, OpenSeg [30] also learns with class agnostic mask annotations to generate mask proposals, while our method does not require any mask annotations.

# Method

We propose the GroupViT architecture for zero-shot transfer to semantic segmentation with text supervision only. GroupViT introduces a new hierarchical grouping Transformer architecture that exploits the global selfattention mechanism of Transformers to partition input images into progressively larger arbitrary-shaped groups. We first describe GroupViT's architecture in detail in Sec. 3.1.

To train it, we employ carefully-designed contrastive losses between image-text pairs, which we describe in Sec. 3.2. Lastly, we transfer the trained GroupViT model, without further fine-tuning, to the task of zero-shot semantic segmentation as described in Sec. 3.3.

## Grouping Vision Transformer

We introduce the GroupViT image encoder (Fig. 2), which performs hierarchical progressive grouping of visual concepts via a Transformer-based architecture. In GroupViT, we separate Transformer layers into multiple grouping stages. In each stage, we learn a number of group tokens (as learnable parameters) via self-attention that aggregate information globally from all image tokens (segments). We then use the learned group tokens to merge similar image tokens together via a Grouping Block. Through a hierarchy of grouping stages, we group smaller image segments into larger ones. We describe each component next.

Architecture Following the design of ViT [24], we first split an input image into N non-overlapping patches and

Two elephants in the jungle this morning  linearly project each into a latent space. We treat each projected patch as an input image token and denote the set of all of them as {p i } N i=1 . In each grouping stage, besides the image tokens, we concatenate a set of learnable group tokens and input them into the Transformer for that stage.

Multi-stage Grouping As Fig. 2(a) shows, instead of forwarding all the N input image tokens through all the layers of the Transformer, we separate its layers into a hierarchy of grouping stages. Each stage incorporates a Grouping Block at its end to merge the smaller groups into larger ones.

Formally, suppose there are L grouping stages, each indexed by l and with a set of learnable group tokens {g i } M l i=1 . For simplicity, we treat the image patches {p i } N i=1 input to the first grouping stage as the set of starting segments

i=1 to {s l i } and similarly {g l i } M l i=1 to {g l i }. Starting with l=1, for each grouping stage, we first concatenate {s l i } and {g l i } together and then input them into a number of Transformer layers, each of which performs information propagation between them via

where [ ; ] denotes the concatenation operator. Then we group the updated M l-1 image segment tokens {ŝ l i } into M l new segment tokens {s l+1 i } i=1 via a Grouping Block as

In each grouping stage M l < M l-1 , i.e., there are progressively fewer group tokens, resulting in progressively larger and fewer image segments. After the final grouping stage, L, we apply Transformer layers on all segment tokens and finally average their outputs to obtain the final global image representation z I as

As shown in Fig. 2(a), GroupViT re-organizes visual information into arbitrary image segments after the first stage itself and thus is not confined to a regular-grid structure.

Grouping Block As shown in Fig. 2(b), the Grouping Block at the end of each grouping stage takes the learned group tokens and image segment tokens as inputs. It merges all the segment tokens that are assigned to the same group token into a single new image segment, based on similarity in the embedding space. Formally, we compute the similarity matrix A l between the group tokens {ĝ l i } and segment tokens {ŝ l i } via a Gumbel-Softmax [32, 55] operation computed over the group tokens as

where W q and W k are the weights of the learned linear projections for the group and segment tokens, respectively, and {γ i } are i.i.d random samples drawn from the Gumbel(0, 1) distribution. We compute the group to assign a segment token to by taking the one-hot operation of it argmax over all the groups. Since the one-hot assignment operation via argmax is not differentiable, we instead use the straight through trick in [60] to compute the assignment matrix as

where sg is the stop gradient operator. With the straight through trick, Âl has the one-hot value of assignment to a single group, but its gradient is equal to the gradient of A l , which makes the Grouping Block differentiable and endto-end trainable. We call this one-hot assignment strategy as hard assignment. After assigning the segment tokens to the different learned groups, we merge the embedding of all the tokens belonging to the same group to form a new segment token s l+1 i . For each group, the output of the Grouping Block is a weighted sum of the segment tokens assigned to that group and computed as

where W v and W o are the learned weights to project the merged features. An alternative to hard assignment is soft assignment, which uses A l instead of Âl for computing Eqn. 5. Empirically, we found that hard assignment results in more effective grouping versus soft assignment (Table 1).

The Grouping Block works similarly to a single iteration of the previously proposed Slot Attention mechanism [50]. While Slot Attention learns instance-level grouping from self-supervision, our Grouping Block groups similar semantic regions with weak text supervision. For example, in the second row of Fig. 6, the two horses are grouped together.

## Learning from Image-Text Pairs

To train GroupViT to perform hierarchical grouping, we employ carefully-designed contrastive losses between image-text pairs. We describe these next.

# Image-Text Contrastive Loss

To learn visual representations via text supervision, following [33,63], we train a dual-encoder architecture via an image-text contrastive loss. In our case, GroupViT acts as the image encoder and a Transformer [81] as the text encoder. The final image embedding from GroupViT (Eqn. 2) is the average embedding of all its output segment tokens. The text embedding is the embedding of the last output token (end-of-sentence token) from the text Transformer. We forward the input image and A picture of a jungle text in a pair through their respective encoders, project them into a common embedding space and compute a similarity measure between them. We consider all matched imagetext pairs as positive pairs, and all other unmatched ones as negative ones. Our training objective is to pull the representations of the positive pairs closer to each other, while pushing those of the unmatched ones far away from each other.

Formally, assume a batch of B image-text pairs

, where x I i and x T i are the image and text inputs, respectively, of the i-th pair. We encode each of them, via their respective encoders, into embedding vectors z I i and z T i and l 2 -normalize each. We then measure their similarity by computing their dot product. The total image-text contrastive loss is defined as

which is composed of an image-to-text contrastive loss defined as

and a text-to-image contrastive loss defined as

where τ is a learnable temperature parameter to scale the logits.

# Multi-Label Image-Text Contrastive Loss

To enable effective visual grouping, besides the image-text loss in Eqn. 6, we propose a multi-label contrastive loss with text prompting. As illustrated in Fig. 3, we use the "prompting engineering" mechanism proposed in [63] to generate additional text labels for each image besides its originally provided sentence label. Specifically, we randomly select K noun words from a sentence x T i , and prompt each of them with a set of handcrafted sentence templates, e.g., "A photo of a {noun}". The motivation to select nouns is that objects in images are more likely to be described by them. Besides training with the original imagetext pairs {(x I i , x T i )} B i=1 , we employ additional contrastive losses between the new sets of image-"prompted text" pairs {(x

, where {x T k i } K k=1 are all prompted sentences generated from the nouns sampled from x T i . As shown in Fig. 3, compared to the standard contrastive loss (Eqn. 6), which results in only one positive pair among the batch B, in our case, each image x I i has K positive text pairs and B(K -1) negative ones.

Similarly to the standard image-text contrastive loss (Eqn. 6), our multi-label contrastive loss is defined as

which is a sum of two two-way contrastive losses

.

Finally, the total image-text contrastive loss for training GroupVIT is defined as

## Zero-Shot Transfer to Semantic Segmentation

Since GroupViT automatically groups images into semantically-similar segments, its output can be easily zeroshot transferred to semantic segmentation without any further fine-tuning. This zero-shot transfer pipeline is illustrated in Fig. 4. To infer the segments of an image belonging to a finite vocabulary of object classes, we forward a test image through GroupVIT without applying AvgPool to its final L output segments, and obtain the embedding of each of them as {z I i } M L i=1 . Each segment token corresponds to an arbitrarily-shaped region of the input image. We then compute the similarity between the embedding of each segment token and the text embedding of all the semantic classes present in the dataset. We assign each image segment to the semantic class with the highest image-text embedding similarity.

Specifically, let Âl be the assignment matrix of the lth grouping stage described in Sec. 3  the mapping between the input and output segments of lth stage. Multiplying all the stage-level assignment matrices

Âl yields the final assignment between the input patches {p i } N i=1 and the final-stage output tokens {z I i } M L i=1 . We use the same "prompting engineering" as described in Sec. 3.2 to transform all the semantic segmentation label names into sentences. The embedding of label names in the dataset is {z T i } C i=1 , where C is the number of classes. As shown in Fig. 4, to classify an image segment z I i to one of C classes, we compute the dot product between l 2 -normalized class name embedding vectors {z T i } C i=1 and z I i , and assign it to the class with the highest similarity.

# Experiments

## Implementation Details

Architecture The architecture of GroupViT is based on ViT-S [24,77] with 12 Transformer layers, each with a hidden dimension of 384. We use input images of size 224 × 224 and a patch size of 16 × 16. We add a learnable positional embedding to each patch after linearly projecting it. We experiment with 1-stage and 2-stage architectures for GroupViT. Both architectures output 8 tokens after the final grouping stage. In 1-stage GroupViT, we learn 64 group tokens and insert the grouping block after the sixth Transformer layer. Before the grouping block, we project the 64 group tokens into 8 tokens using an MLP-Mixer layer [76] and output 8 segment tokens. In 2-stage GroupViT, there are 64 and 8 group tokens in the first and second grouping stages, respectively. We insert grouping blocks after the sixth and ninth Transformer layers. Our text-encoder is the same as [63]. We use a 2-layer MLP to project the visual and text embedding vectors into the same latent space.

Training We use the CC12M [11] and the filtered YFCC [74] datasets for training, containing 12M and 14M image-text pairs, respectively. Our batch size is 4096 with a learning rate initialized to 0.0016 and decayed via the cosine schedule [52]. We use the Adam [37] optimizer with a weight decay of 0.05. We train GroupVIT for 30 epochs with the 5 initial epochs containing linear warm-up. For the multi-label contrastive loss, we set K = 3. We use the same text templates as in [63] for generating text prompts.

Zero-shot Transfer to Semantic Segmentation We evaluate GroupViT for the task of zero-shot transfer to semantic segmentation on the validation splits of the PASCAL VOC 2012 [26] and PASCAL Context [58] datasets. They each contain 20 and 59 foreground classes, respectively, with an additional background class. During inference, GroupViT predicts only the foreground classes by thresholding the softmax-normalized-similarity between the embedding of the output image segments and the text segmentation labels, where we set the threshold to 0.9 and 0.5 for PASCAL VOC 2012 and PASCAL Context, respectively. We resize each input image to have a shorter side length of 448.

## Ablation Study

To discern the contribution of each component of GroupViT, we conduct an ablation study. For all experiments, we train a 1-stage GoupViT with the CC12M dataset, unless otherwise specified. We report mIoU (mean intersection over union) of the predicted and ground truth segmentation masks on the PASCAL VOC 2012 validation set.

# Hard vs. Soft Assignment

In each Grouping Block, we assign image segment tokens to group tokens via hard or soft assignment (Sec. 3.1). For soft assignment, we use the original A l matrix instead of Âl used for hard assignment to compute Eqn. 5. The impact of this is shown in the first column of Table 1. We find that hard assignment improves over soft assignment by a large margin, >10% mIoU. We conjecture that with soft assignment, the features of new segment tokens {s l+1 i } are likely to be more correlated with each other due to absence of zero values in A l . Hence, each group may contain information from the same image patches increasing ambiguity while assigning text labels to image segments. With hard assignment, however, the affinity matrix Âl assigns image segments to groups in a mutually exclusive manner, making groups more differentiated and their assignment to text labels less ambiguous.

# Multi Label Contrastive Loss

We investigate the effect of adding the multi-label contrastive loss in the second column of Table 1. Adding the multi-label contrastive loss to the standard one (Eqn. 8) improves performance both with hard and soft assignment, by 13.1% and 2.6%, respectively. With the multi-label contrastive loss, the input text during  training and inference is in a similar prompted format. We conjecture that this consistency helps GroupViT better classify the learned image segments into label categories. group tokens is much less than the number of classes in the real world, each group token is a feature vector in a 384-D embedding space, which can represent many more concepts than just 1. We also experiment with different output tokens and find 8 to be optimal, similar to findings in [66].

# Group Tokens In

Multi Stage Grouping In Table 3, we compare the 1-stage and 2-stage GroupViT architectures. We also compare their visual zero-shot semantic segmentation results in Fig. 5. We find that the 2-stage GroupViT generates smoother segmentation maps compared to its 1-stage counterpart. To quantify the smoothness of the segmentation maps, we also report the boundary mIoU [16] in Table 3, which computes the IoU of boundaries only. The 2-stage GroupViT improves the mask mIoU of the 1-stage variant by 1.8% and the boundary mIoU by 1.9%. We also train both models on a combination of the CC [11] and YFCC [74] datasets.

While the 1-stage model does not benefit as much from the expanded dataset, the 2-stage model improves significantly both in terms of the mask and boundary mIoU values by ∼7%. These results demonstrate that our hierarchical grouping mechanism is effective, especially when training with larger datasets. We adopt the 2-stage GroupViT in the following experiments.

## Visualization

Qualitative Results on PASCAL VOC 2012 We show selected qualitatively segmentation results of GroupViT in Fig. 6. We select examples with a single object (row 1), multiple object of the same class (row 2), and multiple objects from different classes (row 3). GroupViT could generate plausible segmentation. We provide more qualitative results in the supplement Sec. B.

# Concepts Learnt by Group Tokens

We visualize what the group tokens learn in Fig. 7. We select some group tokens and highlight the attention regions across images in the PASCAL VOC 2012. We found different group tokens are learning different semantic concepts. In the first stage, group tokens usually focus on mid-level concepts such as "eyes" (row 1) and "limbs"(row 2). Interestingly, the group token 36 attends to "hands" if people are in the image, while focusing on "feet" if animals like bird and dog are present. Group tokens in the second stage are more associated with high-level concepts, e.g., "grass", "body" and "face". The figure also shows that the learnt concepts in the first stage    could be aggregated into higher level concepts in the second stage.

## Comparisons with Existing Methods

We compare the zero-shot semantic segmentation performance of GroupViT with other zero-shot baselines and with methods for fully supervised transfer, based on ViT-S.

Comparison with Zero-Shot Baselines We train ViT and a text encoder with the image-text contrastive loss defined in CLIP [63], for comparison. To zero-shot transfer CLIP to semantic segmentation, during inference, we first apply non-parametric grouping on its output features. We then compute the similarity between the average feature of each group and the text embedding of the segmentation labels of the dataset. In this way, any non-parametric grouping method for ViT combined with CLIP can be considered as a zero-shot semantic segmentation baseline. We also report a "pixel-wise" baseline, which treats each pixel as a group and performs classification independently. As by a large margin. This demonstrates that, compared to ViT trained with CLIP, our GroupViT is more effective at zeroshot transfer to semantic segmentation. In the Table C.1, we also show that GroupViT's ImageNet classification performance is comparable to that of ViT.

Comparison with Fully-Supervised Transfer We compare the performance of GroupViT with fully-supervised transfer to semantic segmentation. For fully-supervised transfer, we fine-tune a semantic segmentation head jointly with a pre-trained representation [13,97] on the training sets of the PASCAL VOC 2012 and PASCAL Context datasets separately and report their performances in Table 5. For a fair comparison, we employ a ViT architecture comparable to GroupViT's for all baselines. Specifically, we append a 1×1 convolution layer to a pre-trained ViT, trained with images of size 224 × 224 and fine-tune the whole network with ground truth masks for 4k iterations. During inference, we resize the input images to have a shorter side length of 448 pixels. For fully-supervised transfer, we compare both supervised and self-supervised pre-training methods against GroupViT (Table 5). GroupViT (without fine-tuning) outperforms all variants of ViT pre-trained with self-supervision (with supervised fine-tuning) by a large margin on PASCAL VOC 2012 and is comparable to them on PASCAL Context. This implies that GroupViT, without any pixel-level annotations is able to transfer to several semantic segmentation datasets and can outperform existing state-of-the-art transfer-learning methods requiring more supervision (i.e., pixel-level labels for supervised transfer). Interestingly, on PASCAL VOC 2012, the zero-shot performance of GroupViT (mIoU of 52.3%) approaches that of fully-supervised ViT (mIoU of 53%) trained with both image classification and segmentation labels, which is significant.

# Discussion

Conclusion We take the first step towards learning semantic segmentation with text alone and without any explicit human supervision. We show that, with GroupViT, the representation learned from large-scale noisy image-text pairs can be transferred to semantic segmentation in a zero-shot manner. This work also demonstrates that besides image    2012. This could be attributed to the presence of background classes in PASCAL Context, e.g., ground, road and wall that result in low IoU (∼1.5) on zero-shot transferring GroupViT to semantic segmentation on PASCAL Context. Through visual inspection, we found that while the pixels belonging to these background classes are typically correctly grouped into a single group by GroupViT, the group as a whole may be miss-classified into the wrong class on being compared to the text embedding of the various class labels. We hypothesize that this, in turn, happens due to the low probability of the background classes being described in textual sentences used during training. We show examples of such failure case in Fig. C.5. We further conduct an oracle experiment to verify this finding. In the oracle experiment, for each output group from GroupViT, we compute its IoU with all ground truth masks and assign to each group the class label that results in the the maximum IoU. This represents the upper bound of GroupViT's performance since here we leverage ground truth masks to predict each group's class label. We use our 2-stage GroupViT trained on CC12M and YFCC datasets for this oracle experiment, which is the same model labeled "Ours" in Table 5 of the main paper. We report the oracle experiment's results on PASCAL Context in Table C.3. The large gap between the performance of the original and oracle mIoU values on the PASCAL Context dataset, shows that while GroupViT's grouping results are reasonably good, there is room to further improve the groups' classification to segmentation class labels via image-text embedding similarity. 

# C.4. COCO Dataset

We evaluate the performance of GroupViT on the COCO dataset [44], which contains 80 object classes. We combine the instance masks of the same category to get the semantic segmentation mask for each image. We report semantic segmentation mIoU on COCO in Table C.3. It demonstrates that GroupViT is able to transfer to complex datasets with various number of classes. 

# C.5. Training on RedCaps

To show that our approach is generalizable to other training datasets, besides CC [11,68] and filtered YFCC [74], we also train GroupViT on the recently released RedCaps dataset [21], which contains 12 millions image-text pairs from Reddit, of similar size as filtered YFCC. We report mIoU for zero-shot transfer to various image segmentation benchmarks datasets in Table C 

# A. Implementation Details

A. 1

# . Architecture

The architecture of GroupViT is based on ViT-S [24,77] with 12 Transformer layers. Each layer consists of a multihead self-attention and an MLP block. The input to each block is normalized by layer normalization [5]. We connect the group tokens in the different grouping stages via MLP-Mixer layers [76]. Our text-encoder consists of 12 Transformer layers, each with a hidden dimension of 256. Following [63], the Transformer operates on a lower-cased byte pair encoding (BPE) representation of the text with a vocabulary of 49,152 words.

# A.2. Fully-Supervised Transfer to Semantic Segmentation

To implement the baselines for fully-supervised transfer to semantic segmentation, we fine-tune the pre-trained ViT model jointly with a 1×1 convolutional layer appended to it for pixel-wise classification. We scale each input image by a randomly selected factor in the range of 2] and then crop random 224×224 patches from each image during training. We use the Adam [37] optimizer with a weight decay of 0.05 and a learning rate 0.001. We train all models for 4k iterations with a batch size of 16. During inference, we resize each input image to have a shorter side of size 448 pixels. We open-source our code at https://github.com/NVlabs/GroupViT. 

# C.1. Image Classification

We compare the performance of the GroupViT and ViT architectures for the task of object classification on Ima-geNet. Following CLIP [63], here we train both architectures using supervision from text only via an image-text contrastive loss. In Table C.1, we report both the zeroshot and the linear probing accuracy on the ImageNet [19] validation split. The zero-shot and linear probing evaluation follow the same setting as CLIP [63]. GroupViT's ImageNet classification performance is comparable to (if not better than) that of ViT, thus demonstrating that our proposed grouping mechanism enhances the baseline ViT architecture with the capability to perform semantic pixel grouping and zero-shot transfer to semantic segmentation, without affecting its object classification performance. 

# C.2. Mask Probing

We follow the procedure outlined in DINO [8] to evaluate the quality of the masks generated by GroupViT and by the baseline ViT model pre-trained using prior methods in a fully supervised [77], self-supervised [8,14] or textsupervised [63] manner. For the ViT models, similar to DINO [8] for each final attention head, we compute its similarity to the [CLS] token and derive an attention mask for the pixels with the highest attention values. We then compute the Jaccard similarity of each head's attention mask to the ground truth mask and retain the attention mask with the highest similarity. As for GroupViT, it does not have a multi-head design in the Grouping Block. Thus, we directly select the group most similar, as measured by the Jaccard index, to the ground truth mask for each image. As Table C.2 shows, the mask probing result of GroupViT is significantly better than that of all variants of the baseline ViT architecture. Hence, compared to ViT, our GroupViT more effectively groups semantically-related visual inputs together.

# C.3. Limitations

We found that the mIoU of GroupViT on PASCAL Context is significantly lower than that on PASCAL VOC 

