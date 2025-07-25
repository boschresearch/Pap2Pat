# Pap2Pat: Benchmarking Outline-Guided Long-Text Patent Generation with Patent-Paper Pairs

[![arXiv](https://img.shields.io/badge/arXiv-2410.07009-b31b1b.svg?style=for-the-badge)](https://arxiv.org/abs/2410.07009)
[![hf](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Paper%20page-ffc107?color=ffc107&logoColor=white&style=for-the-badge)](https://huggingface.co/papers/2410.07009)
[![acl](https://img.shields.io/badge/ACL-ACL%202025%20Findings-ffc107?color=ffc107&logoColor=white&style=for-the-badge)](https://aclanthology.org/2025.findings-acl.496/)

## Abstract

> Dealing with long and highly complex technical text is a challenge for Large Language Models (LLMs), which still have to unfold their potential in supporting expensive and timeintensive processes like patent drafting. Within patents, the description constitutes more than 90% of the document on average. Yet, its automatic generation remains understudied. When drafting patent applications, patent attorneys typically receive invention reports (IRs), which are usually confidential, hindering research on LLM-supported patent drafting. Often, prepublication research papers serve as IRs. We leverage this duality to build PAP2PAT, an open and realistic benchmark for patent drafting consisting of 1.8k patent-paper pairs describing the same inventions. To address the complex longdocument patent generation task, we propose chunk-based outline-guided generation using the research paper as invention specification. Our extensive evaluation using PAP2PAT and a human case study show that LLMs can effectively leverage information from the paper, but still struggle to provide the necessary level of detail. Fine-tuning leads to more patent-style language, but also to more hallucination. We release our data and code.



## Contents of this Repository

This repository comprises three main parts:

1. [Pap2Pat](Pap2Pat/): Dataset and evaluation code
2. [Outline_Guided_Generation](Outline_Guided_Generation/): Implementation of chunk-based outline-guided generation
3. [Pap2Pat_Dataset_Creation](Pap2Pat_Dataset_Creation/): Code for the creation of Pap2Pat


## License

The code is released under the MIT license, see [LICENSE](LICENSE).

The data is released under [CC-BY](https://creativecommons.org/licenses/by/4.0/).
