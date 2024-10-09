# INTRODUCTION

The organization and grouping of products is important for ecommerce and retail companies to streamline the shopping experience and showcase product authority. Identifying product variants is one of the important tasks within the domain of product grouping and recommendation. Product variants are groups of products that share many similarities except for a few differences. For example, the same faucet may be sold in a number of different finishes, as shown in Figure 1. Product variants are particularly useful to customers for a number of reasons.

• They help users find alternative products easily and without the hassle of searching or browsing through the massive product catalog. • They save consumers time in comparing alternative products by ensuring that key product features remain the same across product variants. • They simplify search results and product lists by grouping similar products together.

On e-commerce websites, product variant information is often prominently displayed on product detail and product listing pages, and receives extraordinarily high user views, clicks, and purchases. Figure 2 shows how product variant options may be shown to the user.

Due to the importance of product variant identification, the execution requirements for the algorithm are very high. In addition to high performance, the algorithm must have a high degree of interpretability and transparency to receive support from business stakeholders and enable collaboration with various domain experts. 1.1 Algorithm Requirements 1.1.1 Precision. Product variant information is highly visible to end customers, and mistakes can significantly impact customer experience and site performance. As a result, there is a very high requirement for the precision of product variant identification.

1.1.2 Recall. High recall is also highly desired. Showing the complete product offerings not only helps customers find the right products quicker, but also projects the right image of product authority and increases customer loyalty.

1.1.3 Leverage Domain Knowledge. When working with a wide variety of product categories, it is important to define product variants in different ways. For example, while faucets may vary by color, it does not make sense to define lumber variants based on color. For many types of products, there are existing business rules for how variants in each product category should be defined. In order to achieve the highest level of customer satisfaction, our algorithm must respect this domain knowledge.

1.1.4 Interpretability. Identifying product variants is a high priority task that involves many business stakeholders. In order to effectively collaborate with them, we need a business friendly justification for why certain products were grouped together. When business users have a clear understanding of why the algorithm is grouping certain products, they are more likely to adopt the algorithm on their set of products or contribute their subject matter expertise towards improving the algorithm.

Based on the above requirements, we frame the problem of identifying product variants into a constrained clustering problem, where we incorporate business rules and human knowledge into the algorithm as constraints. In order to improve recall, we use Natural Language Processing (NLP) techniques to perform sensible fuzzy matching on the constraints to overcome the noise in the textual data. First, we extract product family name from unstructured product title. Then, we measure the similarity between model numbers of two product variant candidates using edit distance. Beside several business constraints, there are cluster level constraints that the product variants must have the same family name and the model number difference must be within a certain range. We will discuss the details in the Section 3.

# RELATED WORK

In this section, we discuss three types of strategies that are relevant to our application, including product deduplication, classification, and constrained clustering.

## Product Deduplication

Product duplication broadly involves detecting duplicates or similar products in databases. Several methods address this problem as it is extremely important in retail applications. [1] provides a comprehensive overview of database duplicates detection. Product similarity can be computed in various ways.

Character-based methods: These methods match strings character by character. Popular methods that do character-wise matching include edit distance or Levenshtein Distance [6] and Hamming Distance.

Token-based methods: Character-based methods may not work well if the order of words get changed (but they mean the same). Hence token-based methods are useful where raw strings are not matched but are converted to tokens first (by splitting them using a delimiter). Jaccard index is a popular token-based similarity metric.

Besides databases, product duplicate detection is addressed for Web data obtained from e-commerce websites. The key difference between finding similar products from a relational database and from the Web is that Web data is very noisy whereas databases are structured. [10] propose a hierarchical clustering method to cluster products from multiple websites and apply it to detect similar products in a dataset of TVs. Their approach builds upon the Title Model Words Method (TMWM) [12] which extracts entities from product titles and matches them using cosine similarity. Then additional rules are applied to detect product duplicates. Another method that their approach uses is the Hybrid Similarity Method (HSM) [2] which adds product attributes to compute similarities (beyond just product titles).

Another relevant line of work [8] uses the term product resolution and heuristic methods (or rules) to extract structure from unstructured data and find product duplicates. [5] is also a rulebased filtering approach that does pairwise comparison between punctuation-delimited textual chunks and determines if the chunks are similar or not. Pairwise computations save time especially if the dataset is large. Another method that builds upon this idea is [4] where the authors propose to use Locality Sensitive Hashing (LSH) [3] to detect candidates for pairwise comparison and compare model words from product titles (proposed by [11]) as well as descriptions.

Despite of the large body of work on product deduplication, these methods do not directly address our application. Rather than identifying the most similar products, our task is to group items together conditional on variable attributes defined by domain experts for each specific category. This uncompromisable condition makes the task more challenging and interesting.

## Classification

A recent blog post [7] proposed a classification based approach to find product variants. They predict whether a pair of products belong to the same product variant family based on a limited set of generic product attributes. These attributes are the same across all categories and include dimensions, price, weight, manufacturer, supplier, and model number. For each of these attributes, a distance metric is computed between each pair of items. These distance metrics are used as features to train a random forest model, which gives a probability of product similarity.

One drawback of this classification method is that it uses the same standard attributes for all categories. When the product catalog is very diverse, we found that classification algorithms using these standard attributes do not perform well. In particular, the attributes may be unavailable or not relevant to certain types of products.

Many categories may not have standard attributes like Product Width or Product Length defined. These missing values degrade the performance of the model. We used standard techniques (e.g. average or dominant values of similar products) to fill in missing values. In addition, some products, such as windows, are designed to vary on these standard dimension attributes. Therefore, it often does not make sense to group based on similarity within these attributes. Figure 3 shows two faucets that should be classified as within the same product variant family. The distance features used in the model are shown in the table. In this example, many of the standard product dimensions have missing values and the faucets are not correctly identified as being product variants.

In contrast, our algorithm only uses two basic product attributes, product title and model number. Because they are required to make a product sellable, we rarely suffer from the missing value issue. In addition, our algorithm considers variable attributes defined by domain experts for each category in the process of extracting the product family name (will be discussed in Section 3.2). Therefore, our algorithm generated better results that satisfy the categoryspecific conditions.

## Constrained Clustering

Constrained clustering [9] is a type of clustering algorithm that considers the user's background knowledge or constraints in the processing of grouping objects into clusters. This special property makes it more desirable than its unconstrained counterpart in many applications. The standard definition of constrained clustering is similar to typical unconstrained clustering models with the addition of a set of constraints imposed on each cluster, as shown below: 𝑑𝑖𝑠𝑝 (𝐶𝑙 𝑖 , 𝑟𝑒𝑝 𝑖 ) = 𝑂 ∈𝐶𝑙 𝑖 𝑑 (𝑂, 𝑟𝑒𝑝 𝑖 ) represents the dispersion of the cluster 𝐶𝑙 𝑖 or the total distance between every member of the cluster and a representative element 𝑟𝑒𝑝 𝑖 ∈ 𝐶𝑙 𝑖 of the cluster.

A type of constrained clustering is based on SQL aggregate constraints, defined as: Definition 2.2. SQL Aggregate Constraints: Consider the aggregate functions 𝑎𝑔𝑔 ∈ {𝑚𝑎𝑥 (), 𝑚𝑖𝑛(), 𝑎𝑣𝑔(), 𝑠𝑢𝑚()}. Let 𝜃 be a comparator function, i.e., 𝜃 ∈ {<, ≤, ≠, =, ≥, >} and 𝑐 represent a numeric constant. Let 𝑂 𝑖 ∈ 𝐷 be associated with attributes {𝐴 𝑗 } where 𝑂 𝑖 [𝐴 𝑗 ] represents the value of attribute 𝐴 𝑗 for object 𝑂 𝑖 . Given the cluster 𝐶𝑙, a SQL aggregate constraint on 𝐶𝑙 is a constraint in one of the following forms:

i

In a sense, this paper is about how to use NLP approaches to create proper SQL aggregate constraints (i.e. satisfying business rules, sharing the same product family name, and model numbers within a certain edit distance) to perform constrained clustering. Because this approach respects the business requirements and uses easily interpretable features, it achieves satisfactory results and accelerates its adoption in the business. However, it is worth noting that our algorithm is different from the traditional constrained clustering approach. From the definition, constrained clustering requires a pre-defined parameter k for the number of clusters. In contrast, our algorithm does not limit on the number of product variant groups, and can allow the formation of product variant groups to adapt to the properties of each category. This is the most sensible approach given the business use case.

# APPROACH

In this section, we describe our approach to identifying product variants using the framework of constrained clustering. A summary of this approach can be found in Algorithm 1. We describe in detail the three main constraints that we impose on our constrained clustering algorithm.

• Business rule constraints -We require an exact match on several business mandated attributes. For each product variant group or cluster 𝐶𝑙,

for all 𝑂 𝑖 , 𝑂 𝑘 ∈ 𝐶𝑙 and 𝐴 𝑗 ∈ {𝑏𝑟𝑎𝑛𝑑, 𝑐𝑎𝑡𝑒𝑔𝑜𝑟𝑦}. • Same product family name constraint -For each cluster 𝐶𝑙, 𝑂 𝑖 [𝐴 𝑗 ] = 𝑂 𝑘 [𝐴 𝑗 ] for all 𝑂 𝑖 , 𝑂 𝑘 ∈ 𝐶𝑙, where 𝐴 𝑗 represents the attribute of product family name. In the next section, we will talk about the NLP process to extract the attribute of product family name from the product title. This is conditional on the variant attributes set by domain experts.

• Model number constraint -The model number for each product must be similar to the model number of another product in the cluster. For each cluster 𝐶𝑙,

for all 𝑂 𝑖 ∈ 𝐶𝑙 where 𝐴 𝑗 represents the model number attribute and 𝑑 represents the Levenshtein distance function. These constraints are further described in the sections below and a summary of our algorithm is given in Algorithm 1.

## Rule Based Constraints

Product variants must be grouped from within the same brand and category due to business constraints.

## Extraction of Family Name from Product Title Conditional on Category-specific Variant Attributes

Our algorithm extracts a product family name for each product. The family name consists of a sequence of important tokens from the product title that should be found in all products within a product variant family. This family name allows us to easily explain to business partners how the products were grouped. We use the following steps to extract the product family name from the product title.

• Standardize terms with a synonyms dictionary.

• Remove punctuation and other non-standard characters.

• Remove numbers and units of measurement as these are often noisy and inconsistent.

• Remove brand information as this is inconsistently available in the title. • Remove noisy tokens from a manually created blacklist, including tokens from noisy attributes. • Remove tokens that are already included in the category data. • Remove tokens related to the variant attributes that are defined by domain experts for each category. For example, the color of the faucet should be removed from the title. Figure 4 shows an example of how a product family name is extracted from a unstructured product title. If product candidates have the same sequence of tokens after the cleaning process, these products may belong to the same product variant group. 

## Model Number

Another strong signal that products belong to the same product variant family is the model number. Product variants are often assigned similar model numbers by the manufacturer. The core part of the model number is often constant for all product variants, while a few characters may be changed or added to represent the available attributes. In Figure 5, we see that the faucet color is represented by the two final letters in the model number. All other characters in the model number remain constant.

We use the standard Levenshtein or edit distance to measure how similar two model numbers are. The following operations are included with equal weights:

• Insertion • Deletion • Substitution This distance measure helps us determine if a small change or addition was made between product variants. In general, product variants tend to have much smaller edit distances than pairs of products that are from a similar category but are not product variants. Figure 6 shows the distribution of edit distances for product variants compared to different products from within the same category. Product variants tend to have lower model number edit distances.

How model numbers are created tends to vary by category and manufacturer. In particular, different categories may have different standards in how similar model numbers are. We used a grid search  to determine the optimal model number distance threshold for each of our major categories.

# EXPERIMENTS

In addition to the required business constraints, brand and category, we test the following two combination of constraints:

• Model Number Only -Items are grouped together as product variants if the edit distance of their model numbers is sufficiently small. • Extracted Product Family Name and Model Number -Important tokens are extracted from each product title. Items that have the same product title tokens and also have a sufficiently small edit distance for the model number are grouped together as product variants. We compare the performance of constrained clustering under these constraints to a baseline of vanilla classification.

We test these methods using a manually curated dataset of product variants owned by a large retailer. We include a wide variety of product categories such as window treatments, faucets, PVC pipes, tools, hardwood flooring, and many other products. This dataset consists of about 1 million items.

Precision is measured by comparing items grouped by the algorithm to items with known product variant information. True positives are when our algorithm groups together items that are known to be variants of the same product. False positives occur when our algorithm groups together items that are known to be variants of different products. Products with no known variant information are ignored in this validation process. Recall is measured by looking at items with known product variant groupings, and determining how many of these items are correctly identified. Model performance is shown in Table 2.

The model number constraint is not sufficient to correctly identify product variants. This method performs poorly compared to the classification baseline. However, when the product family name constraint is added, we see a significant increase in recall resulting in a much higher F1 score than the baseline.

In addition to overall precision and recall, we review the performance of our model across different categories. Algorithm results are released into production on a category by category basis. Due to business requirements, we can only put the model into production for categories that have very high precision (>=90%). Using both the same product family name and similar model number constraints resulted in a much higher number of categories reaching the precision threshold than the classification model, as shown in Figure 7. This results in the largest number of groupings being implemented on the site.

# CONCLUSION

While there are many techniques for identifying similar or duplicate products, not all of these methods are appropriate for grouping product variants within a diverse catalog. A constrained clustering approach gives us the flexibility to group items from a wide variety of product types while still maintaining high accuracy. Constrained clustering also provides an easy to understand explanation for why products are grouped together. The most effective constraints are based on explicitly incorporating business rules, extracting  Applying these constraints to our product catalog gives us high quality product variant groupings.

