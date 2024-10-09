# Introduction

Layout, the structural and visual presentation of the contents within a document, is a key aspect for writers to compose documents and for readers to understand documents. Specifically, the planning and the arrangements of how the contents are spatially structured, as well as the use of multiple modalities (e.g. texts, graphics, tables), is highly * Work done during an internship at Google Research. influential in the choice of reading strategies from the readers. Hence, a well crafted layout can lead to better comprehension of the presented contents, and layout information is vital for document understanding (Wright, 1999;Hartley, 2013).

Learning a document-level representation with awareness of the layout has started to draw attention in the research community, especially in achieving better semantic document understanding (Katti et al., 2018;Denk and Reisswig, 2019;Xu et al., 2020). However, most prior works focus on rather surface forms of the layout, such as comprehending table hierarchy (Wang et al., 2020) and the claimed multimodality being referred to OCR detected features of the textual components (Hua et al., 2020;Zhang et al., 2020). Moreover, prior works mostly concern documents in the domain of scanned templated documents like receipts (Pramanik et al., 2020), not as content-rich and layoutflexible as articles such as Wikipedia pages.

In this paper, we propose Layout-Aware Multimodal PreTraining, dubbed LAMPRET, aiming for a more general-purposed pretraining methodology which exploits both the structure and the content of documents, and considers multimedia contents, such as images, to learn a comprehensive multimodal document representation. Specifically, we utilize an in-house document tokenizer to parse HTML formatted pages into several content blocks, where each block has the following features:

(1) spatial position, (2) semantic types, e.g. headers and tables, and (3) attributes like font-sizes.

Inspired by the inherent hierarchy in the contents, our LAMPRET framework is hierarchical, consisting of two cascaded transformers (Vaswani et al., 2017). The lower-level transformer takes as inputs the parsed multimodal content blocks serialized by their sorted spatial positions, and the output blocklevel representations are consumed by the higherlevel transformer. The lower-level model is trained with the Masked Language Modeling (MLM) ob-jective (Devlin et al., 2019) and an image-to-text matching prediction for grounding different input modalities. For training the higher-level model, we propose three novel block-level pretraining objectives aiming to exploit the structure of a document:

(1) block-ordering prediction requires the model to predict whether the input blocks are properly ordered, (2) masked-block predictions shares similar spirit with textual MLM but acts at the textual block-level, and (3) image fitting predictions requires the model to select the most suitable image for a missing image block.

We evaluate our proposed LAMPRET framework on two downstream document completion tasks: (1) Text block filling which aims to select the most appropriate textual block for a missing block to complete a document, and (2) Image content suggestion where the models are required to correctly retrieve the most suitable image at a layout position for a particular document, from a sizable set of candidates approximating realistic scenarios of composing documents. We show the effectiveness of our LAMPRET framework and the benefits of incorporating multimodality, as well as conduct extensive ablation studies on its components. Our main contributions are as follows:

• To our best knowledge, we are the first to consider layout multimodality in the context of the interactions between the actual image and the textual contents within a document.

• Propose a hierarchical framework with structureexploiting pretraining objectives to learn layoutaware document representations.

• Design novel downstream tasks to evaluate the layout-awareness of the learned document representations, with the hope to spur relevant future research in multimodal document understanding.

# Related Works

Document or Long-Text Learning. The recent advancements in NLP with the help of transformers (Vaswani et al., 2017), has encouraged research in transformer-based models that can go beyond the previous maximally allowed input length in models such as BERT (Devlin et al., 2019). Longformer (Beltagy et al., 2020), Reformer (Kitaev et al., 2020), and the recently proposed Big-Bird (Zaheer et al., 2020), are all capable of handling much longer input texts even to the whole document-level. The focus of this work, on one hand, is to design a framework that explicitly exploits the structure of the document contents, rather than modeling long document texts in the conventional way; on the other hand, we do not make any assumption of the base model used for LAM-PRET and hence any of these recent models can replace our current base model, which is BERT.

Document Layouts. Obtaining document layouts can be done by utilizing a conventional and rather rule-based technique, such as VIPS (Cai et al., 2003), and recent deep learning approaches (Yang et al., 2017;Soto and Yoo, 2019;Ling and Chen, 2020), where the computer vision models (Ren et al., 2015) is adopted. CharGrid (Katti et al., 2018) and its extensions (Denk and Reisswig, 2019;Kerroumi et al., 2020) assume the layout contents are visually interpreted via computer vision techniques such as OCR, and propose learning frameworks to semantically understand the documents from a 2D aspect. Other prior works utilize document layouts as an effective component for information extractions (Hua et al., 2020;Gorai and Nene, 2020;Yu et al., 2020b), and provide a benchmark for surface semantic understanding of documents (Li et al., 2020a). Our work aims to go beyond surface understanding and exploit the layout explicitly in a modeling perspective in combined with the fine-grained language and vision models.

Multimodality. Multimodal grounding is an important paradigm for training visual-linguistics models. In this work, we adapt the basic model configuration from recently proposed BERT-based visual-linguistics models (Li et al., 2019;Su et al., 2020;Lu et al., 2019;Chen et al., 2020;Li et al., 2020b;Yu et al., 2020a) to fuse the textual and image modalities. Specifically, we also adapt the image-to-text matching training objective inspired by these models as one of the components in LAM-PRET. Prior works concern multimodality in learning or extracting document layouts (Wang et al., 2020;Pramanik et al., 2020;Zhang et al., 2020;Xu et al., 2020) mostly by viewing a document as a structured imagery, while we model the actual multimodality in the contents such as how the texts should interact with the images within a document. which primarily handles HTML formatted webpage documents similarly to the aforementioned VIPS (Cai et al., 2003). Figure 1 illustrates how a document is tokenized (parsed) into several small content blocks, each is a small proportion of the document which shows a clear spatial boundary to the others. Each block has the following features:

• Block Position: The 2D real valued position of the bounding box which encompasses the block, represented by XY coordinate tuples of (top-left, bottom-right) corners as illustrated in Figure 1.

• Block Type: The semantic type of the content presented in the block. There are in total 13 different types defined by our document tokenizer, with the most popular ones being header, paragraph, image, list (bullet-items), and table, etc.

• Block Attributes: The visual presentations of the texts featured in a block. Two types of attributes are generated by our tokenizer: (1) scalar typed, such as font-size, which is normalized to ∈ [0, 1] with 1 indicating the largest possible font-size, and (2) binary-typed, such as indicating if the text is bold, italic, or underlined.

• Multimedia: There might be multimedia contents such as images, thumbnails, and videos in a block. In this work, we only consider images for our multimodal model. But our model can be easily extended to other multimedia contents. Note that multimedia content can be a block itself, as illustrated in Figure 1, the Image block is different from the Image & Text block.

Layout: We define layout as the structural presentation of the tokenized content blocks, i.e. their

# Expression Descriptions blki or blkij

The i-th content block in the serialized order, or the i and j-th in 2-dimension.

outi Final output representation of block i after the higher-level model.

blkhi Block-level representation of block i after the lower-level model, taken as input to the higher-level model.

# CLSi

CLS token for the i-th block, mainly for separating the input blocks and aggregating the i-th block-level representation.

# global-CLS

The global CLS token which is prepended at the beginning of the inputs, where the representation obtained at this position is regarded as the overall representation of the whole document. embdfeature The embedding for a particular feature. relative positions and orders, and the aforementioned attributional features of the textual contents within a block. In order to properly prepare the input representations for our models, we first sort the tokenized content blocks, with respect to the two dimensional coordinates of their top-left corners, as illustrated in Figure 2a. We sort the Y-axis first and then X-axis, with the intuition that for the documents this work focuses on, the vertical order is slightly more important than the horizontal. The sorted blocks are serialized in a zigzag fashion and then fed to the models. Note that our proposed way of sorting is not necessarily the optimal one, where our main focus here is to provide a meaningful ordering for the models to take inputs.

# LAMPreT

Our LAMPRET framework aims to: (1) model the inherent hierarchical formulation of layoutstructured documents, and (2) exploit the structure alongside the actual document contents to learn the representation. The frequently used terminologies throughout the paper are defined in Table 1.

## Model Overview

Hierarchical Architecture: In order to better comprehend a document structured with a particular layout, we consider two level of layout hierarchical formulation. Specifically, the lower-level of the hierarchy refers to the contents of a block such as text and/or images, while the higher-level concerns how these blocks are spatially structured. We design a framework consisting of two cascaded transformers taking different levels of inputs of a given document, as illustrated in Figure 2b. The Lower-Level Transformer  lower-level model takes as inputs the raw parsed contents, where each content block is placed at its serialized sorted position (represented by blocksegment-id, recall Figure 2a). Each block contains the textual contents and potentially also a few images (can be more than one), making the lowerlevel model inherently multimodal. Each block blk i is prepended with a CLS i 2 special token for indicating the boundary of block contents. We also prepend a global-CLS token at the beginning of the inputs for obtaining document-level representation. The higher-level model then takes as inputs the block-level representations blkh i , i.e. the outputs of the lower-level model at each CLS i position.

Input Representations: The textual contents are tokenized by the WordPiece (Wu et al., 2016) tokenizer. Each block is attached with a blocksegment-id indexed by its serialized sorted position, starting with 1 (0 is for the global-CLS position). We map and round each real-valued font-size to an integer ∈ [0, 10]. The boldness, underline, and italic are simply represented as binary values ∈ {0, 1}. We also supplement a binary embedding indicating the modality. The overall input representation for each token position is as follows:

where the embd attr denotes the element-wise 2 The CLS special token in Devlin et al. (2019) can be used for downstream tasks, we follow the similar formulation to prepend each block with its own CLS token so each of them can contribute to the training when required.

summed embedding from all the textual attributes. For each block, we leave a design choice to truncate its contents with a maximally allowed token length, as well as a maximally allowed number of images. More details are in the appendix Section B.1.

Visual Embedding: The image contents are first fed to a convolutional neural network (CNN), followed by a transformation MLP (multi-layer perceptron) layer to align the resulting visual embedding embd img to the same size of the textual token embedding. For documents without any image contents, we simply pad the inputs with zero-image tensors, and the attention mask in the lower-level model is adjusted not to attend to those input positions. For those standalone image blocks, we attach them to the closest text paragraph block (determined by the block positions) for a more straightforward block-level representation aggregation.

## Training Objectives

Figure 3 illustrates the training objectives on both the low-and the high-level of the LAM-PRET framework. The lower-level training objectives aim to capture the finer-grained linguistics, visual information and the ability to handle multimodal inputs, while the higher-level training objectives aim to exploit the structural interactions among the contents at the block-level.

Low-level objectives for the lower-level model:

• Masked Language Modeling (MLM): Following BERT and its multimodal variants (Lu et al., 2019;Li et al., 2019), we apply the MLM objec-  MLM and ITM stands for masked-language modeling and the image-text matching prediction for the low-level objectives. For each high-level objective, we illustrate: an exemplar block swapping for the block-ordering objective, an image masking for the image fitting objective, and a block masked at its block-level representation for the block-MLM objective, respectively.

tive on one hand to further finetune the linguistics ability on our dataset, on the other hand to finetune language modeling with image modality.

• Image-Text Matching (ITM): To further sharpen the model capability of handling multimodal inputs, we adapt the image-text matching (ITM) prediction used in (Lu et al., 2019) to our setups. Specifically, for a given document d containing one or more images, we sample a few candidate images from other documents {d ′ } within the same mini-batch during training, and swap them with some images in d with certain probabilities3 . The model is then required to predict whether the textual contents match the resulting image sequences as binary classification.

High-level objectives for the higher-level model:

• Block-Ordering Predictions (B-ORD): Two input blocks are randomly selected and swapped4 (with certain probability remained) in their serialized order when inputting to the the lower-level model. An MLP5 which takes as input the output representation at the global CLS position, out global-CLS , is trained to make the binary prediction on whether the input contents are following a proper order, i.e. whether the two selected blocks are swapped. The block-segment-ids for the two selected blocks are replaced by a padding value to prevent the leak of the original order.

• Block-MLM (B-MLM): One or more textual blocks are masked out at their block-level representations, blkh i , by replacing them with zerotensors. The objective requires the model to select the most suitable block for the masked position from a given set of candidate blocks, where the candidate set is constructed by collecting the blocks from all the documents (including self) within a mini-batch during training. An MLP layer then takes the concatenation of the output representations of the masked positions and the block-level representations of the candidate blocks, i.e. concat(out masked , blkh i , blkh j , ...), and outputs the classification result of the index to the most suitable block. Since this objective is performed as a classification task, which requires a fixed number of candidates, in practice we truncate the candidates to a fixed number of blocks (with ground truth blocks deliberately included).

• Image Fitting (IMG-FIT): One or more images are masked out by replacing them with a mask-image-token, which is a white image in our implementation. This objective requires the model to select the most suitable images from a set of candidate images for the masked-out images. Similar to Block-MLM, the candidate set is constructed by collecting the images from all the documents within a mini-batch during training, and a classification MLP layer is applied to predict the most suitable ones. The input to the MLP layer for the masked image in the i-th block is: concat(out global-CLS , out blk,i , embd img,1 , embd img,2 , ...), where embd img,j is the visual embedding of the j-th image candidate. We add the output representation at the global-CLS position to incorporate modeling the general trends of how the images are positioned within a document as it aggregates information from each block. In addition, a batch-level mask is applied to filter out the losses of those data entries (documents) without any image contents.

LAMPRET framework is jointly trained with a linear combination of the losses for the low-and high-level objectives:

where λ i s are tunable hyperparameters 6 , and all the losses L are of classification cross-entropy loss.

# Experiments

Our experiments aim to answer the following research questions: (1) Is the hierarchical formulation of LAMPRET effective? (2) Are the proposed layout-aware training objectives effective, and how are they complementing one another? (3) When and on what tasks does the multimodality help?

## Evaluation Tasks

We design two document completion tasks for evaluating the models: (1) text block filling aims to evaluate the model capability of interpreting the structure of the textual contents, and (2) image suggestion concerns the layout multimodality in addition to the structural aspect on texts.

Text Block Filling: Suppose the 2D sorted and then serialized content blocks are {blk 1 , blk 2 , ..., blk N }, we randomly select a block blk i to mask, and provide the context blk 1∶i-1 as inputs to the model, while leaving blk j∶j+K ∪ blk i as candidates, where j > i, blk j is spatially positioned after blk i by a certain margin (four rows in a common web-page document). The closest K (K = 5) blocks abide by the criteria are selected to make this task challenging. The task is then to predict the correct block blk i from the 6 We set all λis to 1 in our actual implementations.

candidate blocks. Note that this masked block blk i can be of any type of textual blocks, including header, an item from a list or table, etc. In this sense, the capability of prediction relies heavily on the understanding of the structure of the document.

Image Suggestion: The model takes as inputs all the content blocks of a document with an image masked-out (by replacing it with all-white-image), and is required to predict the correct image from a given set of candidate images (including the ground truth of the masked out one). We extract C (C = 1000 in this work ) candidate images from documents unseen from the ones used during the pretraining for evaluating the models. Note that since this task aims to simulate suggesting the image contents when composing a novel document, for a more realistic setting, we strip the textual blocks which encompass the direct captions to the images in the dataset used for this task.

Finetuning on Downstream Tasks: To allow better fusion of low and high-level information, we have: R doc = σ(α) ⋅ blkh global-CLS + (1 -σ(α)) ⋅ out global-CLS to represent a document, where α is a task-dependent learnable scalar and σ is the Sigmoid function. We train an MLP to embed the document representation R doc to retrieve from a set of candidate embeddings {R cand } with a contrastive loss (Hadsell et al., 2006), where R cand,i = blkh i for text block filling and R cand,i = embd img,i for image suggestion. Denote Y as equals to 1 if R doc is paired with the ground truth R gt , and 0 otherwise, and m a predefined margin, we have:

(3)

## Baselines

We compare our LAMPRET framework to the following baselines, more details are in Section B.3:

Single-Level LayoutLM: The single-level, nonhierarchical variant of LAMPRET framework consists of only the lower-level model, which resembles the base model of the prior work Lay-outLM (Xu et al., 2020). For training, both lowlevel objectives of LAMPRET, MLM and ITM, are utilized. We compare against this baseline for examining the effectiveness of the hierarchical formulation and the high-level objectives.

CNN-Grid: Inspired by prior work CharGrid and BERTGrid (Katti et al., 2018;Denk and Reisswig, 2019), we experiment replacing the transformerhigher-level model with a CNN module (the original Char(BERT)Grid is applied on OCR detected results which does not fit our setup). Each block-level representation blkh i is inserted to a position on a 2D map according to the sorted 2D coordinates of the block. This results in a 3D tensor, where the original 1D blkh i representation becomes the channel dimension, and hence can be the input to a CNN module. While the output representation out global-CLS of LAMPRET acts as the overall representation of the entire document, we apply an average pooling at the output of the CNN module to obtain the document-level representation of the same size. Since the CNN is viewed as a substitute of the higher-level model, we train this baseline with the same set of objectives of LAM-PRET, and hence the CNN-Grid baseline is the enhanced version of the prior works as we train it with additional layout-aware objectives.

# Unimodality (Text-Only):

We are also interested in examining how our framework performs particularly for the text block filling task, if the textual contents are the only model inputs. We experiment the text-only variant of models for both our LAMPRET and the single-level LayoutLM.

## Implementation Details

We initialize all the lower-level models (note that LayoutLM baseline is single-level) with BERTbase-uncased pretrained weights released from the original authors. A pretrained CNN module is adopted for all the models and baselines to encode the images, and then transformed to the same embedding size of the Wordpiece token embedding, 768, with an MLP layer. For both block-MLM and image fitting pretraining objectives, we empirically select 20 for the size of the candidate set, and hence the final output projection layers for these two objectives are 20-way classification. For block-ordering, the output projection MLP is simply performing binary classification. More implementation details are in the appendix Section B.

## Dataset

In this work, we scrape a collection of English Wikipedia pages (Wikipages) for training and evaluating the models. Our Wikipage dataset is uniformly sampled (scraped) from the entire Wikipedia, which makes it diverse and rich in the genres and the contents. Furthermore, the Wikipage dataset naturally features rich structures as well as different modalities of contents. We preprocess the collected Wikipages as described in section 3 to obtain content blocks. Table 2: General statistics of the dataset. Note that the Wikipages used in the downstream tasks are disjoint from the pretraining set. For the image suggestion task, we only retain pages with at least one image.

## Evaluation Metrics

Since the downstream tasks are trained with contrastive objective and performed in a retrieval fashion, we adopt two common ranking-based metrics to quantify the model performances:

Mean Reciprocal Rank (MRR): We compute the reciprocal (i.e. the multiplicative inverse) ranks of the ground truth items in the given candidates list, and average them across the whole test set.

Recall @ K: We compute the recall in the top-K ranked items by counting the number of the ground truth items in such a top-K candidate list. Since we only have one ground truth item for each example, the recall is binary existence divided by K.

## Experimental Results

Table 3 summarizes the model performances on the two proposed downstream tasks.

Text Block Filling. For the text block filling downstream task, our proposed LAMPRET model outperforms the baselines in both the precision and F-1 score metrics. It is worth noting that for both LAMPRET and the single-level LayoutLM, the unimodal text-only version performs slightly better than the multimodal version. We hypothesize that such results can be attributed to the suboptimal multimodal representation fusing, that it can be potentially alleviated with more sophisticated and finer-grained multimodal grounding paradigms. Among the models, CNN-Grid baselines performs the worst, of which the attention mechanism in transformers is hypothesized to capture the block-level interactions better. We examine the contribution of the high-level pretraining objectives on the multimodal version of LAMPRET. Each row denotes the pretraining is conducted with the indicated objective excluded. We also include an ablation on pretraining without the attributional features (last row), which is shown more effective on the text-based task.

Image Suggestion. We only conduct the image suggestion downstream task for multimodal models, as unimodal ones do not have access to image based features. Our LAMPRET achieves almost perfect performance for both metrics (99%), while all the baseline models suffer significant performance degradation. The hierarchical formulation and the accompanying high-level objectives are proven effective in LAMPRET as compared to single-level LayoutLM. The CNN-Grid baseline again generally performs the worst.

Model Ablation Studies. We are interested in analyzing the contributions of the high-level pretraining objectives for different downstream tasks. Table 4 shows an ablation analysis on the multimodal version of our LAMPRET framework. At each row, we deduct (1) one of the high-level pretraining objectives, or (2) the layout attributional features. In general, the block-ordering objective is empirically proven quite effective for both downstream tasks, judged by the performance degradation when it is excluded during the pretraining. It is worth noting as well that the exclusion of the layout attributes do not cause that much deterioration compared to other pretraining objectives, which hypothetically implies that the exploitation of the structural information of layout designed in the proposed LAM-PRET framework is relatively more effective.

Here we want to point out that we train for much more iterations during downstream finetuning for the image suggestion task (until performance convergence) when the model is not pretrained with the image fitting objective, otherwise with the same settings this downstream task does not work.

# Conclusions and Future Works

We propose a multimodal layout-aware document representation learning framework, LAMPRET. Once a document is parsed into several spatially structured content blocks, we sort and serialize them in a 2D formulation. LAMPRET aims to model the inherent hierarchical formulation of a document layout by two cascaded transformers.

The lower-level model is trained with MLM and ITM objectives, while the higher-level model is trained with three specifically designed layoutexploiting objectives. We evaluate LAMPRET on two downstream tasks: (1) text block filling, and

(2) image suggestion task.

For future works, we envision that (1) a more delicately designed training paradigm such as curriculum training for our hierarchical models can be beneficial, and (2) a more sophisticated multimodal grounding to the lower-level model can potentially alleviate the slightly worse performance in the textbased downstream tasks. Furthermore, we hope to expand the target domains from Wikipages to other content-rich documents such as news articles.

# A More Details of The

We hereby include more details that could help understanding the concept of layout defined in this work and how to process it, as well as its essential building component, the content blocks.

# A.1 Sorting The Blocks

In our dataset, the block positions are structured in the form of a standard bounding box coordinate tuple: (X left , Y top , X right , Y bottom ), where the pair (X left , Y top ) represents the coordinates of the top-left corner, while the pair (X right , Y bottom ) represents the bottom-right corner of the bounding box of a particular content block. In this formulation, even non-rectangular bounding regions for contents can be properly represented and bounded, and our sorting paradigm does not overlook those blocks.

We sort the blocks anchoring around the top-left corner of the box bounding the content block, in this way it is ensured their starting position is of the main consideration. Since even a semantically latter block can have earlier ending position if viewed from the document origin as illustrated in Figure 2a, we refrain from using the bottom-right corner for such a reason. We sort the two coordinates following the order: sort the Y top first and then X lef t , with a standard sequence sorting algorithm. We then perform a zigzag traversal to serialize the content blocks for the inputs to the models. Note that if the blocks are properly sorted (such as the aforementioned sorting), the serialization would reasonably preserve the relative orders in their original 2D formulations, and hence is a proper input sequence to a transformer-based model. The block-segment-ids defined after the serialization then acts similarly to the positional encoding of a transformer model, only that it is at the block-level.

# A.2 Block Features

Block Attributes: For the real-value-typed textual attributional features, i.e. font-size, our original data is prepared with a normalized value with the maximum indicating the H1 header size in a standard HTML web-page. We map this to a range of ∈ [0, 10], and round the results to obtain integer values, so that we can regard these integer-scalars as font-size ids and use the standard embedding technique, i.e. a linear layer (matrix) which retrieves the 1D embedding with the input ids.

Block Types: Each of the 13 block types is attached with an integer id which can then be used  for standard embedding technique, starting from 0. We use block type id = 13, which is the 14th id for indicating padding block, which is used in the block-ordering prediction objective for preventing leaking order information, as mentioned in section 4.2. We include Table 5 to summarize the ranges described above for all the discrete and/or discretized features of the inputs to our models.

# B More Implementations Details

We implement all of the models (including all the baselines) in TensorFlow 1 (Abadi et al., 2016). The BERT-base models which all the models based on, is adapted from the codes released in the original author code repository. We also use the provided pretrained weights to initialize all of the models, specifically the lower-level models for those hierarchically formulated models. The vocabulary size of the BERT-base model is 30522 according to the original configurations, where the input are tokenized by the WordPiece tokenizer.

# B.1 Input Representations

In section 4.2 in the main paper, we omit one of the obvious components used in the original BERT model, that is the token-level positional encoding, i.e. embd positional . Particularly for this positional embedding, we simply use a consecutive positional id scheme for all the inputs at their token-level, starting from the first content block to the last and viewing the entire document contents as a single piece sentence segment. The image contents are also attached with a positional id without breaking the consecutive nature, we do not use different positional encoding schemes for different modalities and view them as the same piece of input for this encoding. As a result, the overall input representa-  (50,50,768) in this work. We then apply a Llayered CNN module to encode this 3D tensor, with kernel size = 3 and L = 3 to match the N = 3 of the higher-level model of LAMPRET. We adjust the kernel strides and paddings in the CNN module to ensure that the height and width of the encoded tensor remains same as the input 3D tensor, in this way we can serialize back the encoded 3D tensor following the same zigzag fashion to perform the high-level pretraining objectives in LAMPRET. However, since the CNN module is fundamentally different from the transformer model, we do not have a global-CLS position, instead, we apply an average pooling to the outputs of the CNN module to reduce the height and width of the final encoded tensor to 1 × 1, a 1D representation as the We implement all of our MLP layers as one layered MLP and include the output dimension in this table.

higher-level document-level representation similar to out global-CLS . In combined with the aforementioned serialized back output representations, we can apply all the high-level objectives similar to our LAMPRET framework.

# B.3.2 Single-Level LayoutLM

Although we call this baseline as LayoutLM, it is still substantially different from the proposed model in (Xu et al., 2020). The original LayoutLM utilizes an OCR-based vision parser on scanned documents, and hence the attributional visual presentations of the textual contents, such as the fontsizes and boldness, are implicitly embedded in the OCR-parsed contents. On the contrary, in our version of Single-Level LayoutLM, the block information and attributes are directly extracted from HTML elements, where the visual presentations of those attributes are explicitly encoded as several discrete variables. Another noticeable difference is that the original LayoutLM adopts 2D scalarvalued positional encoding from the four coordinates of the bounding boxes, while we first properly define a 2D sorting scheme and then serialize the content blocks in our layout so we only need to encode single-scalar block-segment-ids as the blocklevel positional encoding, with the fine-grained token-level positional encoding kept. Differing from the original LayoutLM, the MLM applied to our version of Single-Level LayoutLM is the standard linguistics-based masked learning, and we additionally incorporate the image-to-text matching prediction for aligning multimodal inputs, which is not concerned by the original LayoutLM work.

# B.4 MLP Layers

Table 6 summarizes the configurations of all the MLP layers in this work. We list each MLP module mentioned in the main paper for better references on the implementation details.

All the models are trained with Adam optimizers (Kingma and Ba, 2015). We include number of parameters of each model in the last column, denoted as # params. We use the same set of hyperparameters for the models involving different versions when using different modality of inputs. Particularly for the image suggestion downstream tasks, the models without the corresponding image-fitting pretraining objectives in the ablation studies in Table 4, we train for 100K iterations, 10X the iterations used for those with the image-fitting pretraining objective, i.e. 10K iterations as shown above. For the learning rate decay, we follow the procedure provided by the original BERT implementation.  

# C More Training Details C.1 Hyperparameters

All the essential hyperparameters used throughout this work can be referred to in Table 7. We also include the search bounds as well as the number of trials in searching for our manually-tuned hyperparameter search procedures in Table 8.

# C.2 Hardware and Run-time

We train all of our models (including all the baselines) on a set of TPU computing hardwares, similarly to the configuration for the original BERT model, i.e. 4 Cloud TPUs in Pod configuration (16 TPU chips in total). The run-time for the pretraining phase on average takes 2-3 days, and the run-time for the two downstream tasks take roughly 4 hours each. 

