# Pap2Pat: Towards Automated Paper-to-Patent Drafting using Chunk-based Outline-guided Generation

> [!NOTE]
> Currently, this repository contains only the Pap2Pat dataset. All code for the dataset creation, outline-guided generation and evaluation will be added later.


## Abstract

> The patent domain is gaining attention in natural language processing research, offering practical applications in streamlining the patenting process and providing challenging benchmarks for large language models (LLMs). However, the generation of the description sections of patents, which constitute more than 90% of the patent document, has not been studied to date.
>
> We address this gap by introducing the task of outline-guided paper-to-patent generation, where an academic paper provides the technical specification of the invention and an outline conveys the desired patent structure.
We present Pap2Pat, a new challenging benchmark of 1.8k patent-paper pairs with document outlines, collected using heuristics that reflect typical research lab practices.
>
> Our experiments with current open-weight LLMs and outline-guided chunk-based
generation show that they can effectively use information from the paper but struggle with repetitions, likely due to the inherent repetitiveness of patent language. We release our data and code.



## Contents of this Repository

This repository comprises three main parts:

1. [Pap2Pat](Pap2Pat/): Dataset and evaluation code
2. [Outline_Guided_Generation](Outline_Guided_Generation/): Implementation of chunk-based outline-guided generation
3. [Pap2Pat_Dataset_Creation](Pap2Pat_Dataset_Creation/): Code for the creation of Pap2Pat


## License

The code is released under the MIT license, see [LICENSE](LICENSE).

The data is released under [CC-BY](https://creativecommons.org/licenses/by/4.0/).
