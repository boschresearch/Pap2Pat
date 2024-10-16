# Introduction

Describing an image with its detailed, distinguishing aspects is crucial for many applications, such as creating text keys for image search engine and accessibility for the visual impaired. The standard deep learning approaches train an imageconditioned language model by maximizing the textual similarity between generated and reference captions (Vinyals et al., 2015;Xu et al., 2015;Rennie et al., 2017;Anderson et al., 2018). However, the reference captions of public datasets often describe only the most salient objects in images. This makes models trained to maximize textual similarity with reference captions tend to generate less distinctive captions that ignore the fine detailed aspects of an image that distinguishes it from others.

To alleviate the problem, we propose to use CLIP (Radford et al., 2021), a multi-modal encoder model trained on large image-text data (mostly English) collected from the web, by using its similarity scores (Hessel et al., 2021) as rewards (Sec. 3.1).

In addition, we propose a CLIP text encoder finetuning strategy with synthetic negative caption augmentation to improve the grammar of captioning model, without any extra text annotations (Sec. 3.2). Note that our approach completely eliminates the need for reference captions during reward computation. To comprehensively evaluate descriptive captions, we also introduce FineCapEval, a new dataset that measures captioning in diverse aspects: overall, background, object, and relation between objects (Sec. 4).

In our experiments on MS COCO (Lin et al., 2014) dataset, we show that the captions from models trained with CLIP reward are more distinctive and contain more detailed information compared to the captions from CIDEr (Vedantam et al., 2015)optimized models. The CLIP-guided captions even achieve the higher text-to-image retrieval performance than reference captions that are originally paired with images. We also show that our text encoder finetuning significantly improves caption grammars by removing degeneration artifacts such as word repetition. In fine-grained caption evaluation with FineCapEval and human analysis, we show our CLIP based rewards outperform text similarity objectives by a large margin on all categories.

# Related Works

Image Captioning Metrics. Traditionally, captions have been evaluated with n-gram or scenegraph based similarity metrics such as BLEU (Papineni et al., 2002), ROUGE (Lin, 2004), ME-TEOR (Banerjee and Lavie, 2005), CIDEr (Vedantam et al., 2015), and SPICE (Anderson et al., 2016). However, such metrics often fail to capture paraphrased expressions due to the limited number of reference captions or scene-graphs. To tackle the problem, recent works including BERTScore (Zhang et al., 2019), ViLBERTScore (Lee et al., 2020a), UMIC (Lee et al., 2021), and CLIPScore (Hessel et al., 2021) propose to use relevance scores computed by language or multi-modal models pretrained on large data.

Objectives for Image Captioning. Standard deep learning based image captioning approaches train models with maximum likelihood estimation (MLE) objective. Ranzato et al. (2016) point that MLE suffers from exposure bias problem. 2 To tackle exposure bias, Bengio et al. (2015) propose a curriculum learning strategy called scheduled sampling. Ranzato et al. (2016) propose to train models by directly maximizing the textual similarity between generated and reference captions with RE-INFORCE (Williams, 1992). Rennie et al. (2017); Luo (2020) propose self-critical sequence training (SCST) approach by normalizing rewards to stabilize its high variance.

Recent studies have observed that referencetrained captioning models often neglect important information from images (Dai et al., 2017;Wang et al., 2017). Lee et al. (2020b) use an visual question answering model's accuracy as a reward, encouraging models to generate captions that in-clude information sufficient to answer a visual question. Dai and Lin (2017); Luo et al. (2018); Liu et al. (2018) use image-text retrieval model's self-retrieval score as a reward and combine them with n-gram based metrics, encouraging captioning models to generate captions that are distinctive to each input image.

Note that these works require careful balancing between self-retrieval and text similarity objectives for stable training. In contrast, by finetuning CLIP text encoder (Sec. 3.2), our approach removes the need of reference caption and text similarity metrics for reward computation.

# Methods

## CLIP-guided Image Captioning

We propose to use the relevance score between image and text calculated by CLIP (Radford et al., 2021). Following Hessel et al. (2021), we use CLIP-S as our reward:

where I, c are image and caption, f I , f T are CLIP's image and text encoders, and w is set to 2.5. By maximizing the multimodal similarity of CLIP, which is a contrastively trained model, image captioning models are encouraged to generate captions that contain more distinctive information about the input image. Fig. 1 (a) illustrates this training strategy.

Following Rennie et al. (2017), we optimize our captioning model P θ (c|I) with RE-INFORCE (Williams, 1992) with self-critical baseline.

We approximate the gradient of the expected reward for generated caption ĉ, where rewards from beam search are normalized with the baseline rewards b from the greedy decoding ĉgreedy :

where R(I, c) = CLIP-S(I, c).

## Improving Grammar with CLIP Text

Encoder Finetuning

Since CLIP is not trained with a language modeling objective, the captioning model trained with CLIP-S reward often generates grammatically incorrect (e.g., repeated words) captions (See Table 3). We inject grammatical knowledge to CLIP's text encoder with synthetic negative captions, generated by randomly repeating/removing/inserting/swapping/shuffling tokens of the reference captions. We provide the implementation details of such operations in appendix. We introduce a 2-layer per-Image Criteria Annotations (a)

Background white house, truck digging soil in front of the house, trees and bushes, house surrounded by a small garden, Mini excavator, houses, white and grey building, greenery, two houses, blue and white colored machine Object a blue car, a blue car, black car, car, dozer, white and grey building, greenery, black car, green bushes Relation parked in the front yard, in front, parked in front of, Parked, car standing on the road Overall A blue car parked in the front yard of an off white house with a truck digging soil in front of the house. A blue car in front of a house surrounded by a small garden with trees and bushes in the background.

A black car parked in front of a house with a mini excavator behind it with other houses in the background.

A car and a dozer parked in front of two white and grey buildings and greenery on both sides.

A black car standing on the road surrounded by green bushes on both sides and two houses and a blue and white colored machine in the background.   4 FineCapEval: Fine-grained Caption Evaluation Dataset

We introduce FineCapEval, a new dataset for caption evaluation in four different aspects. To construct FineCapEval, we collect 500 images from the MS COCO (Lin et al., 2014) test2015 split and Conceptual Caption (Sharma et al., 2018) val split, respectively. Then, for each image, we ask 5 human annotators to write phrases of 1) background, 2) objects (and their attributes; i.e., color, shape, etc.), 3) relation between objects (i.e., spatial relation), and 4) a detailed caption that includes all three aspects. See details of data collection process in appendix. In total, FineCapEval consists of 1,000 images with 5,000 annotations for each of the 4 criteria. In Table 1, we show samples of FineCapEval dataset.

# Experiments

We train CLIP-Res50 Transformer captioning model (Shen et al., 2022) with different rewards: MLE, CIDEr, CLIP-S, CIDER+CLIP-S, CLIP-S+Grammar. Following previous works, we conduct experiment on MS COCO (Lin et al., 2014) English captioning dataset with Karpathy split (Karpathy and Fei-Fei, 2015). We evaluate the model with n-gram based metrics, embedding based metrics, text-to-image retrieval scores, and FineCapEval. We also conduct human evaluation with five criteria to understand the human preference of the generated captions in diverse aspects.

Model Architecture and Training. We use the CLIP-Res50 Transformer (Shen et al., 2022)  Text-to-Image Retrieval. We report the recall of the reference image using a text-to-image retrieval model, to measure the distinctiveness of the generated captions. For the retrieval model, we use pretrained CLIP ViT-B/32 (Radford et al., 2021).

FineCapEval. For background, object, and relation criteria, we measure the captioning performance with word-level recall, R word ∈ [0, 1]. See details of R word calculation in appendix. For overall caption, we measure the performance with CIDEr.

Human Evaluation. To evaluate captions in terms of human preference, we show a pair of captions from CLIP-S+grammar reward (ours) with CIDEr reward and with MLE baseline to human annotators from Amazon Mechanical Turk 5 . Then we ask them to select a better caption on 5 criteria (overall, background, object, attribute, relation).

For each of the 5 criteria, we ask 10 annotators with 50 pairwise selection questions. We use 50 images from FineCapEval for caption generation.

6 Results and Discussions

## CLIP Guides Distinctive Captions

In Table 2, the models with CLIP-S and CLIP-S+Grammar rewards achieve higher image-text metrics (CLIP-S / RefCLIP-S) and text-to-image retrieval scores than baselines. Interestingly, their 4 Following the default settings of original papers, BERT-S and CLIP-S/RefCLIP-S are based on RoBERTa-Large (Liu et al., 2019) and CLIP ViT-B/32 (Radford et al., 2021) respectively.

5 https://www.mturk.com/ retrieval scores are even higher than the retrieval score with reference captions. This shows the distinctiveness of their generated captions. For image (a) in Table 3, our model with CLIP-S+Grammar reward describes the rainy weather with 'wet', while the model with CIDEr reward does not describe it.

Our models with CLIP-S and CLIP-S+Grammar rewards score lower text similarity metrics (n-gram based metrics and BERT-S) than the model with CIDEr reward. However, the low scores on these reference-based metrics can be addressed by that the models with CLIP-S and CLIP-S+Grammar rewards often generate captions that include finegrained information that are not even present in the reference captions. For example, for image (b) in Table 3, CLIP-S+Grammar model describes 'blue sign' of the restaurant, whereas none of the reference captions mentions them.

## Finetuning CLIP Text Encoder Improves Grammar

Table 3 shows that the degeneration (e.g., repeating words) of CLIP-S reward is successfully mitigated by adding the grammar reward (CLIP-S+Grammar). Table 2 shows that adding grammar reward significantly increases all text similarity metrics (e.g., +60 for CIDEr).

## Fine-grained Caption Evaluation

FineCapEval. The rightmost four columns of Table 2 show that the captions with CLIP-S and CLIP-S+Grammar significantly outperforms the captions with CIDEr on all four criteria of FineCapEval: overall, background, object, relation. The gap is smallest in object criterion, which implies MS COCO reference captions describe more object information than background or relation between objects.

Human Evaluation. Table 4 shows human evaluation results on five criteria: overall, background,   (Sharma et al., 2018) val split. For each of the 5 criteria, we ask 10 human annotators to select a better caption between ours and another method. On all criteria, the human annotators strongly prefer the captions with CLIP-S+Grammar rewards over CIDEr and MLE baseline.

# Conclusion and Future Directions

We introduce a novel training strategy for image captioning models by maximizing multimodal similarity score of CLIP and finetuning its text encoder to improve grammar. The use of CLIP reward eliminates the need for reference captions and their bias for reward computation. We also introduce FineCapEval, a dataset for fine-grained caption evaluation. We demonstrate the effectiveness of our proposed method based on improvements in text-to-image retrieval, FineCapEval, and human evaluation on fine-grained criteria along with quali-tative examples. Future works involve finetuning CLIP reward models with desired writing styles for different applications and improving the synthetic augmentation process by using external data suitable for grammars with advanced linguistics expertise.

# Ethical Considerations

The CLIP models we used are trained on millions of image-text pairs collected from the web. Birhane et al. (2021) shows that such large-scale datasets often contain problematic and explicit image-text pairs. As the CLIP model card6 suggests, using CLIP reward for training image captioning models is intended as a research output, and any deployed use case of the models is out of scope.

Our captioning models and CLIP models are trained on English datasets; its use should be limited to English language use cases. As our proposed method is not limited to English and easily extended to other languages, future work will explore the extensions in various languages.

In this appendix, we first show more example image captioning with different rewards (Sec. A). Then we explain the implementation details (Sec. B), and the details of FineCapEval (Sec. C). We also explain the details of human evaluation (Sec. D). Lastly, we provide the license for the datasets and models used in the project (Sec. E).

# A More Image Captioning Examples

We provide more image captioning examples using different reward functions in Table 5. Overall, the captions from the model with CLIP-S+Grammar reward provide 1) more descriptive than the captions from the CIDEr model and reference captions, and 2) more grammatically correct than the captions from the model with CLIP-S reward.

# B Implementation Details

Negative Caption Generation. In Alg. 1, we show Python implementation of the negative text generation (Sec. 3.2) for grammar finetuning. In summary, we generate negative captions using one of the operations: repeat, remove, insert, swap, shuffle on the original captions.

Evaluation Scripts. We use pycocoevalcap7 for MS COCO caption evaluation metrics such as CIDEr. We use BERTScore official repo8 with roberta-large model to calculate BERT-S. We report the evaluation script number from single run (single weight initialization), as we did not observe meaningful score fluctuation across multiple runs in our initial experiments.

# C FineCapEval Details

Data Collection. To create a fine-grained description of the image, we ask annotators to write a caption that should describe target images' 1) background, 2) objects and their attributes (i.e., color, shape, etc.), and 3) the relationship between the objects if any (i.e., spatial relation). Furthermore, we ask the annotators to write metadata containing which words/phrases in their writing belong to the three criteria. We also provide annotators with guidelines in writing a caption as follows: 1) There should be a single sentence describing the image. 2) The image may be a photo, an illustration or a pure background. 3) Pay close attention to local and global events in the image. 4) Descriptions should be at least ten words for each image. 5) Avoid the subject description of the image (i.e., a dog runs "very fast", a man feels "successful"). 6) Avoid known entities such as specific locations (i.e. Eifel Tower), time (i.e., 4 pm), event (i.e., Halloween), proper name. 7) In describing people, use only man/woman/boy/girl if clear; otherwise, use person/child. All annotators are hired by a professional crowdsourcing platform TELUS9 . The crowdsourcing company obtained consents from the crowdworkers before the annotation process and conducted the ethical reviews. We collect English captions and all the annotators are native English speakers living in the US. We pay 5,400 USD, including 1) caption creation (5k samples) and 2) quality assurance process that manually examines 50% of the created caption by different workers.

Word-level Recall R word . In Alg. 2, we show Python implementation of word-level recall R word . In summary, R word measures how many words from each of the reference phrases are included in a generated caption on average.

# D Human Evaluation Details

We conduct pairwise evaluation of human preference, as shown in the Sec. 5. For each image, we show two captions generated from two models: ours (CLIP-S + Grammar) and the baseline (MLE/CIDEr). A human worker selects a caption that better describes the image in terms of five criteria: overall, background, object, attribute, and relation. For each criterion, we use 50 images from FineCapEval, and the two options are randomly and evenly shuffled. We also provide 'Tie' option  to choose when the two captions are equally good or bad. For each criterion, we recruit 10 annotators 1) who are located in the Great Britain or the United States 2) HIT approval rate above 80% and 3) Number of HITs approved greater than 1000, from Amazon Mechanical Turk. We pay the annotators 0.03 USD per selection, which roughly corresponds to 11 USD/hour. In Fig. 2, we provide the screenshot for 'object' criterion for example.

# E Licenses

For all artifacts, we remain within their respective license agreements. Here, we list the licenses:

• MS COCO -CC 4.0https: //cocodataset.org/#termsofuse 

# Acknowledgements

We thank the reviewers for their valuable comments. This work was partially done while JC was interning at Adobe Research and later extended at UNC, where it was supported by ARO Award W911NF2110220, DARPA MCS Grant N66001-19-2-4031, and NSF-CAREER Award 1846185. The views contained in this article are those of the authors and not of the funding agency.

