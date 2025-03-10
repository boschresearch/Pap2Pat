# Introduction

Transformers [14,68], first designed for Natural Language Processing (NLP), have achieved great success in a number of other areas as well [5,11], including the vision (e.g., Selfie [66], DETR [6], ViT [34], and PVT [69]) and vision-language (ViLBERT [45], VL-BERT [60], OS-CAR [42]) communities. However, for VL Pre-Training Model (PTM), current approaches, such as VL-BERT [60] and UNITER [9] focus on learning text and image representation of a general domain (i.e., coarse matching). As such, these techniques will benefit for general cross-modality representation learning. However, in the various e-commercial situations (e.g., accessories, clothing, toys), the main goal is to learn the fine-grained representation (e.g. short sleeve, cotton and jersey) rather than only the coarse representation (what, where) in the general domain. In this case, the current general VL models [9,60] are sub-optimal for fashion-based tasks [1,26,67], and could be unfavorable when deploying global features based models to attribute-aware tasks, such as searching for a specific fashion captioning [75] and fashion catalog/object [15], where it is essential to extract finegrained features or similarities [65] from image and text.

In this paper, we propose a novel framework (see Fig. 1) for the fashion-based tasks. The core idea is to focus on fine-grained representation learning and to bridge the semantic gaps between text and image. To achieve this goal, we first introduce an efficient "kaleido" strategy, which extracts a series of multi-grained image patches for the imagemodality. As a result, our model is named as Kaleido-BERT. This strategy is scalable and largely alleviates the aforementioned coarse presentation issue by introducing the patch-variant pre-training scheme. Furthermore, to bridge the semantic gap between different modalities, attention mechanism is employed to build pre-alignments between kaleido patches and text tokens. This pre-alignment information further guides the masking strategy for pre-training. Kaleido-BERT 1 is forced to explicitly learn semantic information across modalities. In summary, our contributions are as follows:

• Kaleido Patch Generator: We propose the kaleido strategy to generate a kaleido of multi-grained features. With the related pre-training tasks, i.e. rotation, 1 https://github.com/mczhuge/Kaleido-BERT/.

jigsaw, camouflage, grey-to-color, and blank-to-color, Kaleido-BERT learns fine-grained cross-modality information and outperforms the fixed-patch or RoIbased VL models in the fashion domain.

• Attention-based Alignment Generator: Kaleido-BERT introduces the pre-alignment strategy to infer a cross-modality mapping between kaleido patches and text tokens. These pre-alignment pairs largely fill the semantic gaps between modalities.

• Alignment Guided Masking:

We present an alignment-guided masking strategy to explicitly force Kaleido-BERT to learn the semantic connections between vision and language. Experiments show the importance of the attention-based pre-alignment and the alignment masking strategy.

# Related Work

There is a large body of VL modeling literature [3,4,23,28,31,54,62,77,79], and we briefly introduce the transformer-based methods in this section. More detailed summary can be found in Tab. 1.

## Vision-Language Pre-training

Recent transformer-based pre-training frameworks, such as BERT [14], GPT2 [57], XLNet [76], and GPT3 [5], have revolutionized NLP tasks. Motivated by these studies, many cross-modal pre-training models for vision-language (e.g., video/image and text pairs) have been designed. For videotext pair models, CBT [63] and VideoBERT [64] are pioneering work that study the capability of pre-training learning. ActBERT [83] and HERO [39] focus more on down- stream applications, while UniVL [47] focuses on both video-language understanding and generation tasks.

For image-text pair models, they can be categorized into single-stream [2, 9, 10, 21, 27, 38, 40-43, 55, 61, 70, 73, 82] and two-stream [13,15,24,38,45,48,50,78] or even threestream [32] according to the network architecture of the single-modal input. In single-stream models, the features of different modalities are directly fed into a Transformer. In contrast, in two-stream models, they are first processed by two single-modal networks before fed into a Transformer, and so forth in three-stream models. ViLBERT [45] claims that the two-stream structure is superior to the singlestream, while VL-BERT [61] finds that the single-stream models achieve more promising results, as these models have more cross-modality information interactions. Vi-sualBERT [40] and B2T2 [2] are single-stream models and derive a unified VL understanding network. With the same spirit of focusing on generic VL tasks, many concurrent models, e.g., Unicoder-VL [38], VLP [82], ViL-BERT [45], VL-BERT [61], have been proposed under the BERT framework. In contrast to the boom in generic tasks (e.g., VCR [9,43,78], VQA [32,38]), other tasks such as visual relationship detection (RVL-BERT [10]), visual navigation (i.e., PERVALENT [24] and VLN-BERT [48]), and visual dialog (e.g., VisualD [50], VD-BERT [70]) are still in their infancy. More recently, Lu et al. [46] shows that multi-task VL learning can lead to a significant improvement over isolated task learning. Similarly, OSCAR [42] achieves new state-of-the-art performance on many representative VL tasks (e.g., image captioning like XGPT [73], image-text retrieval like Image-BERT [55]).

Advances have also been made by the VirTex [13] model in image classification, object detection, and instance segmentation filed, by using semantically dense captions to learn visual representations. Another notable study is the recent ACL work [41] in which the authors creatively demonstrate that the attention head of the VL model can perform entity grounding and syntactic grounding. Unlike all the above-mentioned works, Pixel-BERT [27] considers align-ing vision-language features at a pixel level instead of using region-based image features.

As shown in Fig. 2, our Kaleido-BERT focuses on a masking strategy at the embedding level rather than at the task level (e.g., LXMERT [38] and UNITER [9]) or input level such as OSCAR [42]. Kaleido-BERT explicitly align the embedding features between image and text so that it can learn fine-grain representations for fashion tasks.

## Fashion-Based Task

As described in §. 2.1, existing VL models mainly focus on relatively coarse representations, while less attention has been paid to fine-grained representation learning for the fashion-based task. There are two concurrent studies [15,21] resembling our work. FashionBERT [21] was the first published work in the fashion domain. The concurrent work, MAAF [15], aims to derive a modality-agnostic attention fusion strategy to address the undifferentiated text and image query task. Unlike FashionBERT, which utilizes a patch-fixed masking strategy, the MAAF adopts an image-level attention mechanism. We argue that these two schemes restrict the power of the pre-trained representation learning, especially for the fine-grained fashion task. As a consequence, a more flexible solution with patch-variant is urgently required.

To the best of our knowledge, the proposed Kaleido-BERT is the first to present the effectiveness of alignment guided masking by jointly focusing more on image-text coherence for the fashion domain.

## Model Overview

The architecture of our Kaleido-BERT is illustrated in Fig. 1. There are five stages: (1) Kaleido-BERT takes two inputs: a text (e.g., image caption or description) and corresponding image patches generated by our Kaleido Patches Generator (KPG). Similar to LXMERT [38], each text is represented as a sequence of tokens and each image is represented as a sequence of kaleido patches. ( 2) At the embedding stage, we propose the Attention-based Alignment Generator (AAG) to generate pre-alignments between text tokens and kaleido patches so that the image and text are explicitly aligned semantically. (3) Different from existing random masking strategy, we proposed to adopt an Alignment Guided Masking (AGM) strategy to relieve the difficulty of cross-modality modeling. (4) Text tokens and kaleido patches fully interact in Kaleido-BERT, which gradually learns VL semantic information and produces the cross-modality fine-grained representations. ( 5) Finally, we adopt five new kaleido tasks (i.e., rotation, jigsaw, camouflaged, grey-to-color and blank-to-color tasks) besides the masked language modeling and image-text matching tasks to supervise the network. Our implementation is based on the EasyTransfer 2 /Huggingface 3 library. We refer the readers to this de facto standard library for details.

## Kaleido Patch Generator

Given an image as input, we obtain the multi-grained patches by the proposed Kaleido Patch Generator (KPG). As shown in Fig. 3, we can introduce a saliency detection network 4 (e.g., BAS [56], EGNet [81], ICON [84] or other SOTAs in the recent paper [17]) to obtain the foreground mask and then lock (e.g., bounding box proposal) the domain object. Motivated by the spatial envelope [52] and the block-level strategy [18,19], we then split the image into different scales (i.e., 1×1, 2×2, . . . , 5×5). These image patches are just like "kaleido" patches, and more detailed divisions (e.g., 6×6 or N×N like Pixel-BERT [27]) can be considered according to the difficulty of the specific task. Finally, we obtain 55 kaleido patches from each input image. To generate the embeddings of these patches, we utilize the standard ResNet-50 [25] as our backbone.

## Attention-based Alignment Generator

Attention-based Alignment Generator (AAG) aims to find the coarse alignments between text tokens and kaleido patches. As shown in Fig. 4, we directly adopt the famous SAT network [74] as our text generator, which automatically learns to describe the content of images. At the same time, the SAT network generates the attention heat-map for Tensorflow: https://github.com/alibaba/EasyTransfer Pytorch: https://github.com/huggingface/transformers For simplicity, we just utilize a very simple UNet-like architecture as our foreground segmentation net.  each token, from which we infer the relation between generated tokens and image regions. With the co-occurrence of the generated tokens and the raw text tokens, as well as the overlap area of image regions and kaleido patches, we further build the alignments between raw text tokens and kaleido patches.

## Alignment Guided Masking

The main idea that inspires us to modify the vanilla random masking strategy is that the pre-aligned token, patch pair provides explicit semantic relations between two modalities. This alignment can be used in the pretraining stage, which further forces Kaleido-BERT to explicitly explore cross-modality semantic information. As shown in Fig. 2 (Left), unlike the random masking strategy, Alignment Guided Masking (AGM) gives high priority to masking the pre-alignment pairs. Meanwhile, for each selected pre-aligned token, patch pair, we randomly mask either the token part or the patch part, which stimulates Kaleido-BERT to learn the missing information in one modality by providing the information of the other. When all pre-alignment pairs are traversed and not-enough tokens or patches are selected, a random masking strategy is adopted to mask the unaligned tokens and patches independently. In this way, we obtain the token and patch masking candidates. AGM strategy works on level-3, level-4, level-5 of kaleido patches. We do not apply this strategy on level-1 & -2 since masking larger patches will increase the difficulty of modeling. Empirically, we mask one patch in level-3, two patches in level-4, and three patches in level-5.

## Cross-Modality Transformer

We adopt the original BERT [14] as our cross-modality transformer so that our Kaleido-BERT can be easily extended. Specifically, for the text side, we follow Fashion-BERT [21] to encode the order of the token (i.e., generated via WordPieces [72]) position as 0, 1, 2, 3, . . . , N . Our final training corpus for each sub-word token is obtained by summing up its embedding with the segment and position embeddings, followed by another layer normalization (LN) layer. For the image side, we encode the position information by re-organizing it as 5D features ([x 1 , x 2 , y 1 , y 2 , w * h]) for each patch. After that, both patches and location features are fed into a fully-connected (FC) layer in order to project them into the same embedding space. We obtain visual embeddings for each patch by summing up three FC outputs (i.e., FC (seg id), FC (img feature), FC (pos emb)) 5  and then passing them through an LN layer.

## Pre-training Kaleido-BERT

To alleviate the VL semantic gap and boost feature representation, we design three pre-training tasks, i.e., Aligned Masked Language Modeling (AMLM), Image and Text Matching (ITM) and the proposed Aligned Kaleido Patch Modeling (AKPM) (which includes five kaleido sub-tasks) to supervise our Kaleido-BERT.

Task #1: AMLM. Derived from our alignment guided masking strategy, we can obtain the mask candidates including both token and patch candidates. When masking indices are determined, we decompose masking words into 10% random words, 10% unchanged, and 80% [MSK]. The masked-out token sequence is denoted by T i = {t 1 , ...[M SK], ..., t T }, where token t i is masked out. We feed the hidden output of the last layer of the masked-out token into a classifier over the standard BERT vocabularies. The AMLM goal is to predict the masked words based on the observation of their surrounding tokens and image patches. The objective of the AMLM task is mathemati- 5 Similar to 'segment embeddings' in BERT, we conduct a special modality embedding ('T' for text, 'I' for image) to help the model distinguish the different modalities.

cally written as:

where CE denotes the cross-entropy loss. F is the Kaleido-BERT function. F(•) M SK hidden denotes the hidden output of masked-out tokens. K denotes the masked-out kaleido patch sequence.

Task #2: ITM. The ITM task is transferred by Next Sentence Prediction (NSP) on the vanilla BERT. In this task,

[CLS] is used to indicate the beginning of the fused representation. The hidden output of [CLS] is fed into an FC layer and we use the sigmoid function to predict a score between 0 and 1. The text and image of one positive example are extracted from the same fashion product, while those of one negative sample are randomly extracted from different fashion products. The objective of the ITM task is written as:

where y m denotes the text and image match label.

Task #3: AKPM. The kaleidoscope patch sequence is composed of a collection of kaleidoscope patches as {K 1 , K 2 , ..., K N }, in which N is the kaleidoscope level (N = 5 in our experiment). As shown in Fig. 5, our AKPM includes a single sub-task for each kaleidoscope level, respectively.

Sub-Task #I: Rotation Recognition (RR). Recent works [22,29] have compared various self-supervised learning strategies concluding that predicting image rotations is among the most effective. Motivated by this, we introduce RR in our pre-training. Specifically, we force the 1×1 patch of the level-1 kaleido to randomly rotate by an angle θ ∈ {0 

where y r denotes the rotation angle.

Sub-Task #II: Jigsaw Puzzle Solving (JPS). JPS [29,51] has been demonstrated to be suitable for self-supervised representation learning. Such a pretext task (also called surrogate task) can mine the spatial relations among image patches. Based on this insight, we borrow the notion of jigsaw puzzle to stimulate Kaleido-BERT to learn the potential association from unordered 2×2 patch lists. For simplicity, we treat the JPS problem as a classification of the jigsaw permutations (4! = 24 classes). The network architecture is similar to RR. The objective of the JPS task is written as:

where y j denotes the jigsaw permutation.

Sub-Task #III: Camouflage Prediction (CP). To increase the discernment ability of the model, we introduce another camouflage prediction task to judge which patch has been replaced 6 . With the help of image and text clues, this task encourages the training process to observe the diversity among 3×3 patches. We name this task Camouflage Prediction (CP) because its essence is to camouflage one patch then let the model detect it. By pre-training our Kaleido-BERT with CP, the framework achieves a strong capacity to screen out the imparity with varied products. The CP prediction is also treated as a classification problem and its objective is denoted by:

where y c denotes the index of a camouflaged patch.

Sub-Task #IV: Grey-to-Color Modeling (G2CM). Different from the masking strategy in existing models, which simply exchanges image embeddings with zero paddings, we introduce a smoother G2CM strategy that greys the image patches. Then we reconstruct the grey patch to a color patch by regression, supervised by KL-divergence, which better caters to self-supervised learning. The objective of G2CM is to minimize the G2CM loss:

where KLD denotes the KL-divergence, which aims to minimize the distance of the reconstructed distribution to the target distribution and k 4i is the masked-out patch(es) of K 4 kaleido patches.

Sub-Task #V: Blank-to-Color Modeling (B2CM). The last sub-task is B2CM. Similar to other pre-training methods that replace image feature embeddings with the samedimension zeros sequence, we also adopt this kind of patch masking scheme. This strongly tests the learning ability of a model that captures the contextual information. The objective of B2CM is to minimize the B2CM loss:

where k 5i is the masked-out patch of K 5 . 6 The camouflaged patch is the same scale as the patch randomly selected selecting from the other product randomly. All in all, we introduce the aligned kaleido patch modeling to enhance the ability of the model for spatial context structure (i.e., RR and JPS), classification (i.e., CP), and image generation (i.e., G2CM and B2CM). Finally, Kaleido-BERT should minimize the overall loss function as:

The evaluations of different Kaleido tasks on the validation set are shown in Fig. 6. As can be seen, the losses decay smoothly, which proves that the pre-training process carries on as normal, and the designed tasks can be learned well with Kaleido-BERT.

# Experiments

We evaluate our Kaleido-BERT on four VL tasks by transferring the pre-trained model to each target task and fine-tuning through end-to-end training.

## Pre-training Settings

Dataset. For a fair comparison, we follow the same settings as the Top-1 FashionBERT [21] and pre-train the proposed Kaleido-BERT on the Fashion-Gen7 dataset. It contains 67,666 fashion products accompanied with text descriptions. Each product includes one to six images from different angles. Among all the image-text pairs, like [21], we use 260,480 for training, and 35,528 for testing.

Implementation Details. Our Kaleido-BERT has: L=12, H=768, A=12. L is number of stacked Transformer blocks. H denotes the hidden activation, and A means the number of attention heads. We implement our model with Tensorflow and use 8*Tesla V100 for pre-training. The Adam optimizer is applied with a learning rate of 2e -5 and weight decay 1e -4. We adopt a warming-up strategy for the first 5K steps. 

## Downstream Tasks

We evaluate our model for four downstream VL tasks, including Image-Text Retrieval, Text-Image Retrieval, Category Recognition, and Fashion Captioning. The four tasks strongly cater to industrial applications in the fashion field.

1. Image-Text Retrieval (ITR). Text retrieval is a downstream task that requires the model to distinguish whether a sentence can effectively describe an image. We sample the product images and titles as image-sentences pairs provided by the Fashion-Gen [58] and consider the original product information as positive samples. At the same time, we shuffle the dataset and consider the unmatched image-sentence pairs as negative samples. To increase the difficulty, the positive and negative pairs are selected from the same sub-category, which is hard for PTM to differentiate. We use Rank@1, Rank@5, Rank@10 to evaluate the retrieval performance.

2. Text-Image Retrieval (TIR). The image retrieval task aims to rank product images according to their title. Similar to text retrieval, we use the ground-truth image in the pair as the positive sample and randomly sample 100 unrelated captions from other products in the same subcategory. By predicting the matching score, Rank@1, @5, @10 are used as metrics.

3. Category/SubCategory Recognition (CR & SUB). The category is a vital attribute for describing a product, and is especially useful in many real-life applications. We consider a classification task that judges the category and subcategory of a product, such as {HOODIES, SWEATERS}, {TROUSERS, PANTS}. We directly use a FC layer after [CLS] for these tasks.

4. Fashion Captioning (FC). Image captioning has emerged as an important research topic with a rich literature in computer vision, and the accuracy on FC can evaluate the generation ability of cross-modality models.

## Competing Models

Detailed comparisons for each downstream task are shown in Tab. 2 & Tab. 3. (i) Our Kaleido-BERT achieves significant improvement on nearly all evaluations, which demonstrates its excellent understanding and generation ability in fashion domain. (ii) We observe that the Fashion- BERT approach outperforms ViLBERT and VLBERT. The main difference between them is that FashionBERT adopts patches as image features, while ViLBERT and VLBERT extract RoIs as features. This indicates that in the fashion domain, the patch method is better for extracting image features. (iii) ImageBERT and Oscar perform better than VLBERT and ViLBERT by adding RoI object classification and RoI tags. These two methods provide more information about the image modality. This, to a certain degree, hints that more image semantic information (e.g. image features, image supervision tasks) is required to guide model learning. In our Kaleido-BERT, the kaleido strategy extends from the patch method of FashionBERT [21].

The attention-based alignment masking and the kaleido pretraining task provide more semantic information from the image modality. These factors together explain the superiority of Kaleido-BERT in VL understanding and generation in the fashion domain.

## Ablation Study

Three main factors may influence the performance of Kaleido-BERT, including Input-level: Kaleido Patch Generator (KPG); Embedding-level: Alignment Guided Masking (AGM); and Task-level: Aligned Kaleido Patch Modeling (AKPM). We thus perform three main ablation studies to further analyze these components/strategies of our model. The results are shown in Tab. 4 and Fig. 7.  patches. Scheme-1: Similar to [21,34], the first attempt is to split the fashion images with a fixed-scale setting. Training with such patches, we obtain 276.97 Sum R, 313.43 Sum CLS and 76.6 Sum CAP scores. Scheme-2: We carry out a kaleido (patch-invariant) scheme to generate patches and achieves +9.7%, +0.5% and +4.0% relative improvement on each metric. Compared with scheme-1, scheme-2 is capable of capturing fine-grained representation better. Scheme-3: We further introduce the salient object detection (SOD) algorithm [81] to avoid a huge number of patches with blank regions (tabula rasa). We observed 16.2%, +1.5% and +9.7% relative improvement compared with Scheme-1.

# KPG. Three attempts we have tried to generate our kaleido

AGM. The majority of existing masking methods independently mask visual and text features with a pre-set probability. Such kind masking methods are usually named as random masking. In this experiment, we compare AGM to random masking (Random). Not surprisingly, AGM obtains +6.7%, +1.2%, 6.9% improvements. Compared to random masking, AGM generates more semantic related masking, which benefits our Kaleido-BERT to better understand multi-modality information.

AKPM. To verify the efficiency of the proposed AKPM, we conduct 7 ablation studies (see Fig. 7). The baseline (B) merely consists of the basic ITM and AMLM. Then we add five sub-task to pre-train the model step by step. For example, "B + I ∼ IV" equals to "B + I + II + III + IV". Note that existing models [21] usually use the combination of "ITM + AMLM + B2CM" (B + V) as the pre-training supervision. As shown in Tab. 4, the improvement is limited (+0.9%) in terms of Sum CLS score, even cause negative effect (-2.7%) in SumR metric. Interestingly, we naively replace V (B2CM) with I (RR) will obtains improvement on all downstream tasks (+0.5%, +0.4% and +1.4%, respectively). Gradually, we observed that the performance continue improve when we adding the corresponding subtasks sequentially. Meanwhile the negative affect of V has been alleviated, we argue that V plays the true value when Kaleido-BERT has learned the comprehensive representations of image embeddings from I∼IV.

# Conclusion

We presented a novel pre-trained vision-language understanding architecture Kaleido-BERT for fashion-based task. It consists of a kaleido patches generator, attentionbased alignment generator, and alignment guided masking strategy. These components are easy to implement and cooperate closely to learn both intra-modal and inter-modal image-text feature embeddings. The designed Kaleido-BERT is much more efficient than existing models, attains the new SOTA performance, and largely boosts the accuracy of many downstream tasks such as Image-Text Retrieval, Category Recognition, and Fashion Captioning.

