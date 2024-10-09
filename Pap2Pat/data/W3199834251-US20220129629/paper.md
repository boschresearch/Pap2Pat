# Introduction

Paraphrase generation restates text input in a different surface form while preserving its semantics. It has various applications on downstream NLP tasks including text summarization (Cao et al., 2016), semantic parsing (Berant and Liang, 2014), as well as diversifying text generation for user-facing systems such as chatbots. To evaluate model robustness, a paraphraser can be used to generate adversarial examples, which also serve as augmented data to train the target neural networks (Iyyer et al., 2018a). Besides, paraphrasing queries makes Question Answering systems more likely to match with keywords in a knowledge base (Fader et al., 2014;Yin et al., 2015).  We first train a task-adapted model with a denoising objective so that it is able to reconstruct input text. We then use Dynamic Blocking (DB) to generate pseudopairs of paraphrasing data. Finally, the generated data is used to train the self-supervised model.

However, it is expensive to annotate paraphrases, resulting in only a few human-labeled datasets. The existing ones are either small-scale like MRPC (Dolan and Brockett, 2005), or of closed domains like QQP1 which consists entirely of questions. Consequently, previous work explored automatically (hence noisily) annotated datasets such as PIT-2015 (Xu et al., 2013), Twitter URL Paraphrase Corpus (Lan et al., 2017), ParaNMT (Wieting and Gimpel, 2018), and Para-Bank (Hu et al., 2019), or re-purposed datasets including MSCOCO (Lin et al., 2014) and WikiAnswers (Fader et al., 2013). The scarcity of highquality datasets motivates us to consider unsupervised alternatives. In this work, we explore a transfer learning approach, which leverages unsupervised large-scale pretrained models like T5 (Raffel et al., 2019) and BART (Lewis et al., 2019).

The effectiveness of BERT-score (Zhang et al., 2019) in identifying text similarity hints that pretrained language models are equipped with extensive knowledge in paraphrasing. This knowledge may be attributed to the fact that text spans shar-ing similar context usually stay semantically close together -word embedding (Mikolov et al., 2013) being a classic example. In other words, the paraphrasing capability of language models stems from the strong correlation between context and semantic similarity. In this work, we use pre-trained autoregressive LMs to leverage such implicit knowledge for paraphrasing in an unsupervised setting. 2  For paraphrasing, decoder-only LMs merely output a continuation of the input, while Sequenceto-Sequence models like BART tend to copy the input through even when paired with popular decoding algorithms such as greedy decoding, beam search or top-k/p sampling (Holtzman et al., 2020) because the probabilities of the input tokens during generation are all peaked. To address this issue, we propose Dynamic Blocking (DB), a decoding algorithm that effortlessly transforms pre-trained autoregressive language models into natural paraphrasers with the help of task-adaption and selfsupervision (Figure 1). To obtain a surface form different from the input, whenever we emit a token that is present in the source sequence, this algorithm prevents the model from outputting its immediate successor for the next generation step. The algorithm is based on the intuition that during inference, although the top candidate at each generation step corresponds to a peaked probability, the rest of the distribution still contains rich linguistic knowledge suitable for paraphrasing. This is in similar spirit with using soft targets for model distillation (Hinton et al., 2015).

Through automatic and human evaluations, we demonstrate that our approach outperforms previous models (including supervised, in-domain models and the ground-truth targets) on both QQP and ParaNMT datasets and incurs no performance loss under domain shifts (i.e., finetuned on QQP and evaluated on ParaNMT, and vice versa). For automatic evaluations, we propose a reference-independent automatic metric named BERT-iBLEU, which is a harmonic mean of BERTscore and one minus self -BLEU. We show that this new metric correlates significantly better with human evaluation than traditional metrics. On the qualitative side, we illustrate with concrete examples that our model generates paraphrases that exhibit diverse syntactic structures. Finally, we observe that our model can generate paraphrases in other languages without any additional training. 2 We will release all codes.

Our contributions are: (1) a training pipeline that leads to a strong, unsupervised paraphrasing model; (2) a novel decoding algorithm that effectively diversifies paraphrase generation; (3) a new automatic metric that evaluates paraphrasing quality more accurately.

# Model

Figure 1 shows the training pipeline of our paraphrasing model, which consists of three key components, namely task-adaptation, self-supervision and Dynamic Blocking. Overall we decode the taskadapted model with Dynamic Blocking to generate self-supervision data, which is in turn used to train the final model.

## Task-Adaptation

Inspired by Gururangan et al. (2020), we apply task-adaptive training on the target dataset, treating its training set as a non-parallel collection of sentences. We perform task-adaptation by reconstructing the original sequence from its corrupted version with a denoising auto-encoder objective. Unlike previous work (Devlin et al., 2019;Lewis et al., 2019), we do not corrupt inputs with masks, but rather directly remove the corrupted tokens. This is to avoid pretrain-finetune discrepancy in denoising autoencoding models (Yang et al., 2019). After the deletions, we randomly shuffle all remaining tokens to encourage the model to learn different alignments for better syntactic diversity. 3 Note that we perform both deletions and shuffling on the word-level. This is similar to whole-word masking introduced in later versions of BERT (Devlin et al., 2019). To demonstrate the benefit of our corruption strategy, we present ablation study results in Section 4.3 by either adding masks or not shuffling.

## Dynamic Blocking

Unlike previous diversity-promoting work which mainly focuses on the target side and encourages dissimilarity among beams (Vijayakumar et al., 2018;Kumar et al., 2019;Holtzman et al., 2020), Dynamic Blocking takes the source input into account to guide the model toward generating in a different surface form (Figure 2). As illustrated in Algorithm 1, we represent the source sequence S as a list of tokens S = (S 0 , S 1 , ..., S M ) and similarly 

# Blocked

In Dictionary In Dictionary < s > t h e c h a r t .

# Active Block Dictionary

Sample each entry with probability p

Figure 2: Illustration of the Dynamic Blocking algorithm on real outputs. The algorithm first constructs a full block dictionary based on the input, which maps each token to its immediate successor to be blocked, and then samples from this dictionary to build multiple active block dictionaries, each used for generating a distinct paraphrase.

When establishing an active dictionary, each entry in the full dictionary has a probability of p to be sampled. During generation, the blocking takes place whenever an item in the active dictionary is triggered.

the generated sequence as G = (G 0 , G 1 , ..., G N ). Suppose that during generation, the model emits G j that is identical to some S i (it is not necessary that i = j). Then for the next generation step G j+1 , the algorithm forbids the model to generate S i+1 . Note that we block S i+1 for only one step. After G j+1 is generated, we perform a different blocking for G j+2 iff G j+1 ∈ S.

Algorithm 1: Dynamic Blocking input :A source sequence S consisting of a list of tokens S = (S0, S1, ..., SM ), and a G0 = BOS to start the decoding process 1 Initialize j ← 0 2 while Gj = EOS do 3 if Gj = Si ∈ S for some i then 4 P (Gj+1 = Si+1|S, (G0, G1, ..., Gj) ← 0

The motivation to block for only one generation step is to allow the possibility of pure syntactic variation of the original sequence, meaning that all tokens are kept but their order is permuted. For example, let us consider a decoding algorithm that completely prevents the model from generating a source token at all generation steps -a popular n-gram blocking strategy we call Static Blocking. Suppose that we intend to paraphrase "I like apples and oranges." as "I like oranges and apples.". This is a valid paraphrase, but if we completely block the word "apples" at all generation steps, it will be impossible to arrive at this paraphrase. However, with Dynamic Blocking the model will still be able to generate the word "apples" later on even though this word has been temporarily blocked for one step after "and" is generated. As shown in Figure 2, Dynamic Blocking builds a block dictionary which maps each token in the source sequence to its immediate successor. We then sample from this dictionary with a probability p for each entry. This hyperparameter controls how different we want the paraphrase to be from the source input. In two extreme cases: when p = 0.0, the model does not block any tokens and most likely copies through the source sequence; when p = 1.0, the model always blocks the immediate next token, leading to a drastically different surface form. In this work, we take the middle ground and set p = 0.5 so that for each blocking action, there will be half of the candidates taking that path. Note that if a word is tokenized into several subwords, only the first subword is allowed to be blocked.

We sample multiple block dictionaries to ensure diversity among candidates, while leveraging beam search to ensure coherence. For each sampled block dictionary, we use beam search to generate four candidates and keep the top-ranked two. It is beneficial to combine the two decoding methods because beam search helps to weed out ungrammatical or semantically invalid candidates. 4Note that we only adopt bi-gram blocking because it is a superset of all higher-gram blockings. Consider, e.g., a tri-gram blocking entry ab → c in the block dictionary. If this entry is triggered, then the bi-gram blocking entry b → c will also have been triggered. Hence we found it unnecessary to include higher-order n-grams.

## Self-Supervision

To help the model internalize patterns learned from task-adaption, we pseudo-label the training set (Siddhant et al., 2020) by decoding the taskadapted model with Dynamic Blocking. Having obtained the self-supervision data, we discard the task-adapted model and start from the pretrained language model to avoid catastrophic forgetting (Chronopoulou et al., 2019;Chen et al., 2020). We also include reversed data (i.e., swapping source and target) because during task-adaptation the target is always longer than the input, and including reversed data helps to offset this bias of sequence length.

# Experimental Setup

## BERT-iBLEU

To evaluate paraphrasing quality, we propose a new metric named BERT-iBLEU which encourages semantic closeness while penalizing surface-form similarity. For semantic closeness we use the unsupervised metric BERT-score (Zhang et al., 2019), which leverages a pretrained language model to compute the cosine similarity between each token in the candidate and that in the reference using contextual embeddings. 5 To ensure that the key information (often conveyed through relatively rare words) is retained in the paraphrase, we apply IDF-reweighing on each token. 6 To measure the surface-form dissimilarity, we use one minus self -BLEU, where self -BLEU is the BLEU score between the source and the candidate. Hence BERT-iBLEU (where i stands for inverse) is a weighted harmonic mean of the BERT-score and one minus self -BLEU.

As an extreme case, though copying through the input leads to a perfect BERT-score, 1self -BLEU = 0; hence BERT-iBLEU = 0. This is the reason that we do not use the BERTscore directly to evaluate paraphrases. β is used to control the relative importance between semantic similarity and surface-form dissimilarity. In our experiments we set β = 4.0 to scale up BERT-score so that it has a similar range with self -BLEU. Note that because BERT-iBLEU is reference-independent, it serves both as a metric to evaluate paraphrasing quality and as a criterion to re-rank generated candidates during task-adaptation and self-supervision.

## Dataset

We evaluate on the Quora Question Pair (QQP) and the ParaNMT datasets. QQP contains 140K question pairs that are marked as a duplicate to each other and 640K non-parallel questions. The sizes of dev and test sets are 3K and 20K, respectively. The ParaNMT dataset was constructed by back-translating sentences in Czech in the CzEng dataset (Bojar et al., 2016). We directly obtained the test set of SOW-REAP from the authors of Goyal and Durrett (2020). To match the size of their training set, for task-adaptation we sample 350K non-parallel sentences from ParaNMT-5M, while to generate self-supervision data we sample 350K sentences from the same corpus as inputs.

We filter out any sentences in SOW-REAP's test set to avoid training on test examples.

## Reproduction of Previous Models

For the experiments on QQP we reproduce the supervised Transformer with the pre-trained T5-base model, which is stronger than the usual setting where the paraphraser trains from scratch. We also reproduce the model from Hegde and Patil (2020), which we refer to as CorruptLM. This model is similar to our task-adaptive phase (Section 2.1), except that they corrupt the inputs by removing all stop words rather than a fixed percentage of arbi-trary words.7 Instead of GPT-2 as used by their work, we use BART which shows stronger results on downstream tasks. The rest of the settings remain the same. 8 For the experiments on ParaNMT we use the SOW-REAP model released by Goyal and Durrett (2020).9 

## Automatic Evaluation

To evaluate paraphrasing quality, we follow Li et al. (2019) to report iBLEU (Sun and Zhou, 2012), BLEU (Papineni et al., 2002) and ROUGE (Lin, 2004) on QQP, and report BLEU and ROUGE on ParaNMT. Follwing Goyal and Durrett (2020), for ParaNMT both BLEU and ROUGE are calculated by first selecting the candidate that achieves the best sentence-level score with the ground-truth, and then compute the corpus-level score of all these candidates. We use py-rouge10 to compute ROUGE and the Datasets library from HuggingFace11 to compute BLEU. We also report BERT-iBLEU for the models we reproduced.

## Human Evaluation

We conduct human evaluations on MTurk. 12 For each experiment, we compare our model with the strongest models reported in both supervised and unsupervised settings. On QQP, we compare with supervised Transformer, unsupervised CorruptLM, and the ground-truth. On ParaNMT, we compare with SOW-REAP and the ground-truth. To construct holistic human studies, we opt for both headto-head binary comparison and Likert-scale scoring. The former provides straightforward results on which model is stronger, while the latter is used to consolidate their relative positions. We only worked with annotators who had completed more than 10K assignments, had an approval rate of > 98%, and resided in the US. We also required that the annotators be native English speakers. When comparing between two model outputs based on the same input, we asked the annotators to identify which paraphrase they prefer in terms of overall quality. 13 For each experiment, we randomly sampled 200 examples from the QQP's or ParaNMT's test set and shuffled the order of each example to anonymize the model identities. Each assignment was scored by two annotators.

# Results

## Human Evaluation

Table 1 and 2 present human evaluation results on our final model compared with other baselines. On QQP our model outperforms both Transformer and CorruptLM. Recall that CorruptLM also leverages a pre-trained language model. This indicates the effectiveness of our training pipeline when holding the LM factor as a constant. On ParaNMT our model outperforms SOW-REAP in both headto-head and Likert-based evaluations. Moreover, our model outperforms the ground-truth on both datasets. For ParaNMT, the result indicates that our approach also outperforms a supervised roundtrip translation baseline since that is how ParaNMT data was generated in the first place. For QQP, we note two reasons why these scores do not indicate that our model can generate paraphrases with human-level quality. First, QQP is humanlabeled, not human-generated. Second, QQP annotates duplicate questions rather than paraphrases. Questions referring to the same topic but are not semantically equivalent may still be marked as duplicates. 14We use Cohen's Kappa to evaluate the interannotator agreement. For head-to-head evaluations, we obtained kappa = 0.35, indicating fair agreement. Note that when calculating kappa, we leave out all cases where either of the two annotators gives a "tie" because this usually signifies that they are unsure about which paraphrase is better.

## Advantage of the Proposed Metric

To facilitate a better understanding of the automatic evaluation results, we investigate how each of the automatic metrics correlates with human evaluation.  nificantly better with human perceptions. The reason that BLEU does not correlate well with human evaluation is that there are two conflicting objectives. The first comes from keeping the important information, such as named entities, which should be copied verbatim, while the second comes from using different wordings to express the same semantics -the better the model is at this, the lower the BLEU becomes. For a model good at both, the gain in BLEU for matching key entities and the loss for using different wordings cancel each other out, preventing BLEU from faithfully evaluating the paraphrasing quality. Consequently, BLEU is only useful for checking extreme cases: very low or high BLEU usually signals bad paraphrases, but for the middle-ground cases BLEU alone is less indicative. A similar argument holds for ROUGE.

In contrast, BERT-score encourages the first objective and is not penalized by the second. However, parroting the input will still fool BERT-score alone.

Hence we pair it with self -BLEU to encourage surface-form diversity.

## Automatic Evaluation

On QQP, our model outperforms both the supervised Transformer and the unsupervised Cor-ruptLM on BERT-iBLEU (Table 4). 15 Recall that BERT-iBLEU iBLEU BLEU ROUGE-1/2/L Agree % 68.9 39.4 45.3 21.8/5.4/21.4

Table 3: The percentage of times where the ranking given by each metric agrees with that given by human evaluation in the head-to-head studies. Only cases where two annotators agree are counted.

both Transformer and CorruptLM leverage a strong pretrained language model, indicating that the performance gain stems mainly from our proposed pipeline rather than the language model itself. On ParaNMT, our model outperforms the supervised SOW-REAP (Table 5). 16 As ablation studies on task-adaptation and self-supervision, we can see in Table 4 and 5 that our model (TA+SS+DB) beats the one that is either task-adapted only (TA) or self-supervised but decoded without DB (TA+SS), showing that both self-supervision and Dynamic Blocking are crucial to paraphrasing quality. On the traditional metrics in Table 4, our models also obtain competitive results with the supervised models. However, as we move down to the last row, we see that Copy-input achieves state-of-theart results on all metrics except BERT-iBLEU, indicating that iBLEU, BLEU, and ROUGE scores are not reliable for evaluating paraphrasing quality. 17 In contrast, our best model on BERT-iBLEU (TA+SS+DB) achieves much lower iBLEU and BLEU scores as compared to other models, showing the inconsistency between these traditional metrics and human evaluation. We also note one special aspect of Table 5 to make it easier to interpret. Unlike on QQP, the performance of Copy-input on ParaNMT is the lowest among all models. However, we need to take this comparison with a grain of salt because all the other results are based on 10 candidates where only the ones with the highest sentence-level scores are retained. In contrast, Copy-input only has one candidate. Thus Copyinput and the other results are not directly comparable. Plus, SOW-REAP filters the dataset to only include syntactically diverse targets and then splits it into the train, dev and test sets, which makes Copy-input less effective.

## Robustness to Domain Shift

On the ParaNMT dataset, we notice that Cor-ruptLM, when finetuned on non-parallel QQP, achieves much worse results than the other models (CorruptLM (QQP) row in Table 5), indicating that it is less robust to domain shift. In contrast, our model achieves similar results compared to the indomain one under the same setting (TA+SS+DB (QQP) row). Conversely, we also finetune our model on non-parallel ParaNMT and evaluate on QQP (TA+SS+DB (ParaNMT) row in Table 4). We observe that this model again achieves performance similar to that of the in-domain model. These results show that our model may be able to perform task-adaptation using an arbitrary out-of-domain corpus and still work well on the target domain.

## Ablation Studies on Corruption Strategies

During task-adaptation, our corruption strategies involve both deletions and shuffling. In Table 6 we provide ablation study results where we either replace words with masks instead of deleting them or delete words without shuffling. We can see that our delete-and-shuffle strategy achieves the best BERT-iBLEU score among the three settings. 

# Analysis

## Syntactic Diversity

In Table 7, we qualitatively demonstrate paraphrases generated by our model that exhibit syntactic structure variance. Unlike previous work relying on explicit syntactic scaffolding (Goyal and Durrett, 2020), our model achieves syntactic diversity "for free" from shuffling during task-adaptation.18 

## Generalization to Other Languages

Dynamic Blocking on BART without Finetuning Though we focus on T5 throughout the paper, we do note a unique ability of BART: it can Input Generated paraphrase We got to spend the rest of the weekend at the track. yeah.

We got to stay at the track for the rest of the weekend. yeah. Are predictions of the future based on the present too much? Are future predictions too much based on the present? What is the best way to reduce belly and arm fat?

What is the easiest way to reduce arm and belly fat? You can seduce enemy soldiers, though.

You can, though, seduce enemy troops. Well, why would your buddy be in the shower with you?! Okay, why would you be in the shower with your friend?! directly work with Dynamic Blocking to generate paraphrases (i.e., without domain-adaptation and self-supervision), though of lower quality than the self-supervised model. We demonstrate such examples in Appendix D.

Paraphrasing in Other Languages We observe that although BART is trained almost exclusively on English text, it is able to paraphrase in multiple other languages. We adopt the aforementioned BART setting and present an example in German (Table 13 in Appendix E). To our best knowledge, this is the first unsupervised model that can paraphrase in a non-English language. The reasoning behind this observation is twofold. First, although BART was trained on English corpora, there is a small portion of the content in German due to mislabeled language identification, allowing the model to observe German data; second, previous work has shown that large-scale language models are able to perform zero-shot cross-lingual transfer on a variety of downstream classification tasks, such as Named Entity Recognition (Moon et al., 2019), Natural Language Inference, and Document Classification (Artetxe and Schwenk, 2019). Our work hence demonstrates that it is possible to perform such a transfer even for generative tasks like paraphrasing. We also hypothesize that the paraphrasing quality should improve if we apply our training pipeline to mBART or mT5 (Xue et al., 2020). We leave this as future work.

# Related Work

Paraphrase generation has been a long-standing task that has several applications on downstream NLP tasks including text summarization (Cao et al., 2016), semantic parsing (Berant and Liang, 2014), and question answering (Yu et al., 2018). Early works on paraphrase generation mostly rely on rule-based or statistical machine translation systems (McKeown, 1980;Meteer and Shaked, 1988;Bannard and Callison-Burch, 2005).

Supervised Approaches Neural sequence-tosequence (Seq2Seq) models have been used to address this task (Prakash et al., 2016;Li et al., 2017;See et al., 2017;Vaswani et al., 2017;Gupta et al., 2018); sometimes such models are also used to evaluate paraphrasing quality (Thompson and Post, 2020). Round-trip translation between two languages (i.e., back-translation) with strong neural machine translation (NMT) models has also become a widely used approach for paraphrase generation (Yu et al., 2018). Consequently, supervised models using datasets like ParaNMT obtain their performance mainly from sequence-level distillation (Kim and Rush, 2016), where the data comes from the underlying supervised translation models. There have been several previous works (Iyyer et al., 2018b;Chen et al., 2019;Li et al., 2019;Kumar et al., 2019;Goyal and Durrett, 2020) that make use of syntactic structures to produce more diverse paraphrases. More recently, Qian et al. (2019) employ distinct generators to produce diverse paraphrases. Retrieval-augmented generation methods have also been investigated (Kazemnejad et al., 2020;Lewis et al., 2020). However, most of these approaches require parallel data.

Unsupervised Approaches Unsupervised paraphrasing, on the other hand, is a rather less explored and more challenging problem in NLP. Bowman et al. ( 2016) train a variational autoencoder (VAE) to maximize the lower bounds for the reconstruction log-likelihood of the input sentence without requiring any parallel corpora. Sampling from the trained VAE's decoder leads to sentences that can practically be considered as paraphrases as the decoder aims to reconstruct the input sentence by its training objective. Miao et al. (2018) introduce a constrained sentence generation approach by using Metropolis-Hastings sampling, which allows for decoding with complicated discrete constraints such as the occurrence of multiple keywords, hence not requiring any parallel corpora. Roy and Grangier (2019) introduce a model that allows interpo-lation from continuous auto-encoders to vectorquantized auto-encoders. Liu et al. (2020) cast the paraphrasing as an optimization problem, where it searches the sentence space to find the optimal point for an objective function that takes semantic similarity, expression diversity, and language fluency into account. Siddique et al. ( 2020) optimize a similar objective with deep reinforcement learning.

Transfer Learning There have been few works leveraging pre-trained language models for paraphrasing, either in a supervised (Witteveen and Andrews, 2019) or an unsupervised (Hegde and Patil, 2020) setting. Both works employ GPT-2 as their backbone generation model. Similarly, we opt for more recent large-scale pre-trained models like BART and T5.

# Conclusion

We design an effective training pipeline that enables large-scale pre-trained models to generate high-quality paraphrases in an unsupervised setting through task-adaptation, self-supervision, and a novel decoding algorithm named Dynamic Blocking. We demonstrate with automatic and human evaluations that our model achieves state-of-theart results on benchmark datasets. We also show that our model generates paraphrases that exhibit syntactic diversity, as well as generalizes to other languages without any additional training. Overall our work motivates a deeper investigation into self-supervised techniques for paraphrase generation as well as extensions such as context-aware paraphrasing, where the output conditions not only on the sentences to be paraphrased, but also on the context around them. We leave this as future work. 

# A Automatic Metric Results

We present automatic evaluation results on the previous metrics for QQP in Table 8 and for ParaNMT in Table 9. We can see that for QQP our task-adaptation model without Dynamic Blocking during inference achieves state-of-the-art results among unsupervised approaches. Had we based our judgments on Table 8, we would have mistakenly selected this one as our final model.

# B Robustness to Grammar Errors

During the task-adaptation phase, our model in most cases has a grammatically correct sentence as the target sequence. Additionally, shuffling during that phase encourages the model to attend to the context during generation. These setups make our model reasonably robust to grammar errors so that it can paraphrase and normalize the input at the same time. Table 10 shows a case where we intentionally introduce grammar errors on subject-verb agreement, singular vs. plural, and verb inflections.

Input Our approach are data-driven and can be apply across various situation.

# Output

Our approach is data-driven and can be applied across various situations. Our approach is data-driven and can be applied across different situations.

Our approach is data-driven and can be applied across diverse situations. Our approaches are data-driven and can be applied across various situations.

Our data-driven approach can be applied across different situations.

Our approaches are data-driven and can be applied across different situations.

Our data-driven approach can be applied across diverse situations. Our approaches are data-driven and can be applied across diverse situations. Table 10: Selected example of output candidates produced by our model where we intentionally introduce grammar errors (marked with underlines). We observe that all paraphrase candidates have these errors corrected.

We find that our model is in most cases robust to such errors. This trait is desired because we may face noisy inputs from users. Through early ablation studies, we observed that without shuffling during task-adaptation, the model was much less robust to grammar errors. Hence shuffling does more than just improving on the BERT-iBLEU metric (Table 6).

# C Failure Modes

Though only occurring occasionally, our model exhibits multiple failure patterns. Hence we perform "anti-cherry-picking" and present in Table 11 some of such examples and the respective modes we outline. We hypothesize that the Antonym mode can be partially addressed by a lookup in the dictionary to additionally block the antonyms. Grammar errors are harder to resolve because they are usually apparent only after the whole sentence is generated.

A grammar checker on the candidates may improve the situation. The swapping of subject and object shows that unsupervised approaches based on pretrained language models could only carry us so far till the syntactic-level. In its current form, it cannot handle semantic mistakes. For missing named entities, an NER tagger can help filter candidates that miss important entities. We leave addressing these failure modes as future work.

# D Details of Dynamic Blocking

Block surface-form variations In our early experiments, we observed that when blocking a word (e.g. "give"), the model usually tries to generate its capitalized ("Give") or upper ("GIVE") version.

From we human's perspective, these are usually not good paraphrases -intuitively we would prefer a different word. Similar to whole-word masking introduced in later versions of BERT, 19 we only block the beginning of the word rather than any subword.

Block Closed-Class Words We also leverage linguistic knowledge to help boost the quality of the paraphrases by avoiding blocking closed-class words, or functional words. 20 The closed classes in English include pronouns, determiners, conjunctions, and prepositions while open-class words correspond to nouns, lexical verbs, adjectives, and adverbs. There are two justifications for blocking these words. First, because they are closed-class, there are fewer synonyms available; second, blocking such words is error-prone. For example, changing determiners (e.g. from "you" to "I") may lead to syntactic or semantic errors, while modifying conjunctions (e.g. from "and" to "or") may lead to change in logical relationships.

Block Inflections In Section 5.2, we mentioned that BART can directly work with Dynamic Blocking without task-adaptation or self-supervision, but that results in lower quality, especially lacking syntactic variance because it is not trained with the shuffling strategy during task-adaptation. In addition, we found that without finetuning, BART tries to generate inflections of a word when it is blocked. To partially remedy this drawback, we use the pattern library 21 to enumerate all inflections of a word to block (e.g. for "give" we should also block "gives", "gave", "giving" and "given") in addition to all the other blocking schemes introduced in Section 3. This is available for most languages that involve inflections. We show in Table 12 the output candidates of a selected example with and without blocking inflections.

Retain Named Entities We also explore a variation of the system where we employ a separate Named Entity Recognition model to identify the named entities in the source sequence and prevent 20 https://mailman.uib.no/public/ corpora/attachments/20111124/6c58cb02/ attachment.txt 21 https://github.com/clips/pattern any tokens in these entities from appearing in the full block dictionary. This change ensures that all named entities are copied verbatim.

# E Paraphrasing in German

We pair BART directly with Dynamic Blocking to generate paraphrases in German. In Table 13, we can see that all candidates (left column) have different surface forms, while all translations in English (right column)22 share similar meanings.

# F MTurk Instructions

To facilitate reproducibility, we include our MTurk instructions for the head-to-head and the Likertbased human studies (Figure 3 and 4). As mentioned in Section 3.5, we only provide guidelines on which paraphrases are better in general and leave the rest to the annotator's intuition.

# Input

The random selection of pages must be performed by someone other than the player.

# Output Blocking inflections

The random choice of the pages must be performed by someone else than the player. The random selection of the pages must be performed by someone else than the user. The random selection of the pages must be executed by someone other than the user.

The random collection of these pages must be performed by someone else than the player. The random selection of these pages must be executed by someone other than the user.

# No blocking inflections

The randomly selection of page must be perform by someone else than the players. The random choice of page must be performed by someone else than the player.

The randomly selection of page must be perform by someone rather than the players.

The random choice of page must be performed by someone rather than the player.

The random collection of pages must be performed by someone else than the players. Candidates Warum lieen keine Geschutzbelehrungen statt? Why were there no protection instructions? Warum finden keine Geschutzbelehrungen statt?

Why are there no protection instructions? Warum lieen keine Brandschutzbelehrungen statt?

Why weren't there any fire safety instructions? Warum finden keine Geschutzbelehrungen statt?

Why are there no protection instructions? Warum finden wir keine Brandschutzbelehrungen statt? Why are we not giving fire safety instructions?

Table 13: Paraphrasing German input by directly applying Dynamic Blocking to BART. Translations on the right are given by the Google Translator, except that the first one is the ground-truth translation. Note that the candidates are ranked by multi-lingual BERT rather than RoBERTa-base which is only used to rank English outputs.  

