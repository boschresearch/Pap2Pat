# Introduction

Entity resolution (ER) is the process of identifying similar entities in several datasets, where the datasets may belong to different organizations. While these organizations would like to join hands and analyzes the behavior of matching customers, they may be restricted by law from sharing sensitive client-data such as medical, criminal, or financial information. The problem of matching records in two or more datasets without revealing additional information is called privacypreserving record linkage (PPRL) [11] or blind data linkage (BDL) [10] and is the focus of this paper. A survey of PPRL methods is available in [18]. The importance of finding efficient and accurate PPRL solutions can be observed, for example, in the establishment of a special task team by the Interdisciplinary Committee of the International Rare Diseases Research Consortium (IRDiRC) to explore different PPRL approaches [1].

The PPRL problem is a generalization of the well-studied private set intersection (PSI) problem in which two parties with different datasets would like to

The work for this paper was done while Michael Mirkin was with IBM Research.

# arXiv:2203.14284v1 [cs.CR] 27 Mar 2022

know the intersection or the size of the intersection of these datasets without revealing anything else about their data to the other party. Examples for PSI solutions include [5,6,12,20,30,32]. With PSI, the two parties compute the intersection of their respective sets, which can be used to identify matches by looking for records that share the same identifying field e.g., PSI over social security numbers (SSNs). However, in reality, such identifying fields do not always exist, and even when they do exist, their content may be entered incorrectly or differently. For example, consider two parties that perform PSI on entity names. A single user may register himself in different systems under the names: 'John doe', 'John P Doe', 'john doe', just 'John', or even 'Jon ode' by mistake. A general PPRL solution may attempt to consider all of the above names as matching.

In some cases, more than one data field is used to match two records, e.g., first name, last name, addresses, and dates of birth. These fields are known as quasi-identifiers (QIDs), which may hold private information. In this paper, we assume that the parties are allowed to learn data by matching QIDs. In other cases, one can use a masking method e.g., as in [25] to maintain the users' privacy.

Non-exact matching is commonly performed using ER solutions that employ a local sensitive hash (LSH) function. Unlike cryptographic hash functions, this technique permits collisions by deliberately hashing similar inputs to a single digest. For example, consider a hash function that hashes all the above names to a single digest value or to lists of digests with non-empty intersection. Different LSH functions with different parameters allow us to fine-tune the results in different ways. We provide more details in Section 2.2.

Unfortunately, few practical protocols exist that can securely perform such "fuzzy" record linkage without revealing some private data of the parties, and do so in a linear time frame. See Section 1.1 for a review of the different approaches. Many involve a third-party (e.g., [23]), which we aim to avoid, while other works do not provide a thorough leakage analysis that would help evaluate the security of the solution. To this end, we constructed a new and efficient PPRL solution that runs in O(n). We describe its performance and discuss its security characteristics.

The goal of our solution is to compose a PSI with an LSH function. The dataset fields are first locally hashed by both parties using the LSH and then checked for matches using PSI. The choice of PSI algorithm can only affect the performance (latency and bandwidth) of our solution but does not affect the amount of leaked information that can be tuned using the different parameters of the LSH. Figure 1 illustrates a high-level view of our solution.

Our contribution. Our contributions can be summarized as follows:

-We introduce a novel and efficient PPRL protocol that combines LSH and PSI, and analyze its security against semi-honest adversaries. It does not involve third parties. Specifically, due to the use of LSH, our protocol has a low probability of revealing the data of non-matched records and thereby provides better privacy guarantees.

-We implemented the model and suggest several lower-level and higher-level optimizations. -We evaluated our implementation over a dataset with 2 20 records and demonstrated its practical advantage when the execution took 11 -45 minutes, depending on network settings. -Our program is freely available for testing at [35]. Fig. 1: A high level illustration of our PPRL protocol. The parties P s and P r hold datasets D s and D r . They preprocess the data for every record and then feed the results into an LSH that outputs an ordered list of digest vectors L s and L r , respectively. These are fed into a PSI black box. Finally, P s translates the PSI output to the matching record IDs.

## Related work

To demonstrate our solution, we use a PSI instantiation that uses public-key cryptography; specifically, we use one that leverages the commutative properties of the Diffie-Hellmann (DH) key agreement scheme. This PSI construction was introduced in [20] with a similar construction even before that in [30]. Subsequent PSI works consider other, more complex cryptographic primitives such as homomorphic encryption (HE) [6] and oblivious transfer (OT) [32]. While the latter solutions may offer an interesting tradeoff in terms of performance and security, we decided to stick with the basic DH-style protocol due to its simplicity and the fact that its primitives were already standardized [2]. Because we use PSI as a blackbox, we can also benefit from most of the advantages that the other methods provide such as performance and security guarantees.

Our solution follows previous works in considering a balanced case, where the two datasets are roughly equal in size. An example, for a PSI over unbalanced sets was studied in [5]. In fact, there were attempts to use PSI for PPRL before this paper. However, they were either noted to be inefficient [38] or relied on a different techniques such as term frequency-inverse document frequency (TF-IDF) [34], which is more appropriate for comparing documents, rather than short record fields (such as names or addresses). Furthermore, the protocol of [34] can only compare given record pairs. This implies the need for O(n 2 ) operations, in contrast to our method, which requires O(n) operations.

A complete survey of PPRL techniques and challenges is available at [18,38], in which we observed solutions that use different cryptographic primitives. For example, [14,39] relies on HE, which is known for its high computational cost. For example, [14] reports that it took somewhat less than two hours to evaluate 20, 000 patient records, which is less records than in our evaluations by several orders of magnitude. Other works [4,36] use garbled circuits, which can still be inefficient, while other multi-party computation solutions such as [26] can incur high communication costs [7]. Another example is the fuzzy volts approach, which uses secure polynomial interpolations [31], but only reports results for around 1, 000 records. Other solutions [19,33] overcome the leakage issue by using differential privacy, which anonymizes the data to maintain privacy. We see it as an orthogonal approach to ours.

Many PPRL works use Bloom filter encodings [37], which use a locality preserving hash (LPH) function over the data. The main advantage of the Bloom filter is speed. The difference between LPH and LSH is that LPH is datadependent, i.e., for three records p, q, r, a metric d, and an LPH function l p d(p, q) < d(q, r) =⇒ d(l p (p), l p (q)) < d(l p (q), l p (r))

This relation complicates the evaluation of the protocol leakage. The lack of a formal analysis for Bloom filter based solutions caused several attacks on them [8,9,27,28]. A survey of attacks and countermeasures for this method can be found in [15]. Our solution's use of LSH has an advantage over Bloom filters as it is data-independent and more robust against the above attacks. A method that combines Bloom filters and LSH was presented in [16,24]. In contrast to this one, our solution only uses LSH, which simplifies the privacy analysis. Moreover, our use of PSI hides the LSH output and thus prevents offline attacks. In addition, [24] requires use of a third-party and demonstrates a solution that took more than an hour to match 300K records. Another recent example is [26], which runs in O(n•polylog(n)) and proved to be cryptographically secure in the semi-honest security model. However, the method analyzed 4, 096 records in 88 minutes and it is not clear whether this method can scale to handle more than 100K records.

Organization. The paper is organized as follows. Section 2 provides some background notation and describes the required preliminaries for this work. In Section 3 we present and discuss several possible definitions of PPRL protocols. We provide a high level description of our solution in Section 4 and provide further details about our implementation in Appendix D. We report our experimental setup and results in Section 5 and conclude in Section 6.

# Preliminaries and notation

We denote the concatenation of two strings by s 1 | s 2 . The function Eq(s, r) returns 1 when two strings are equal and 0 otherwise. An ordered list of elements A is marked with square brackets, e.g., A = [5,3,8] and we access its ith element by A[i]. A permutation π can either return a permuted list when operating on an ordered list, or the index of a permuted element within that list when the input is another index. For example, let π : x → x + 1 (mod 4) be a permutation, then π( [5,6,7,8]) = [8,5,6,7], π(2) = 3, and π(3) = 0. Uniform random sampling from a set U is denoted by u $ ← -U .

## Entity resolution (ER)

An ER method gets as input two datasets of N s and N r records from record spaces R: D s = {s 1 , s 2 , . . . , s Ns } and D r = {r 1 , r 2 , . . . , r Nr }, respectively. It evaluates the similarity of every two records using a similarity measure µ : R × R → [0, 1] and an associated similarity indicator

The ER method uses the similarity indicator to facilitate a bipartite graph G = (U, V, E), where the nodes of U , V are the records of D s , D r , respectively, and for every two nodes (u ∈ U , v ∈ V ), an edge exists in E if I µ t (u, v) =1. PPRL. Informally, a PPRL protocol is an ER method executed by two parties: a sender P s and a receiver P r , who privately hold D s and D r , respectively. At the end of the protocol, P r learns the similarity edges E while P s learns nothing. We provide a formal definition in Section 3. Specifically, our PPRL solution uses the LSH and PSI primitives, described next.

## Local sensitive hash (LSH)

An LSH [29] is a hash function that deliberately hashes similar inputs to the same output hash value. We are interested in the similarity of strings i.e., the content of the record fields. Therefore, we use the LSH from [29], which is based on the Jaccard index and on Min-Hashes, as demonstrated in Figure 2.

Jaccard index (a.k.a. the Jaccard similarity coefficient) is a similarity measure for strings. The procedure for computing the Jaccard index of two inputs strings (s, r) splits each normalized string into the set of all overlapping sub-strings of given lengths, termed k-shingles (or k-grams), where k is the length of the substrings. We use small letters to denote strings or the corresponding records, and capital letters to denote their associated sets of k-shingles. The Jaccard index for records s, r is

Fig. 2: Computing the LSH for a string: shingles are extracted from the normalized string, and then min-hashes are evaluated and grouped into bands that are hashed to a list of signatures.

when the context is clear we use J instead of J(s, r). It is possible to instantiate a PPRL solution that relies on the Jaccard index. The drawback of such a protocol is that it has quadratic complexity in the size of the datasets. For linear complexity, we use Min-Hash.

Definition 1 (Min-Hash [29]). For a collision-resistant hash function H with an integer output digest and an integer k, a Min-Hash function receives a string s as input, converts it to a k-shingles set S, and returns

When the context is clear we write MinH instead of MinH H k .

Observation 1 ( [29]) For two normalized records s and r, a collision resistant hash function H, and k > 0, it follows that

An LSH involves applying P different Min-Hash functions to a string s. The outputs are split into B bands of R digests (P = BR). The concatenation of the R digests of each band is again hashed to produce the signature of the band, where the same signature hash function is used for all bands. An LSH output is a tuple with these band signatures.

and the LSH output over a string s is the ordered list

Two LSH tuples are considered to be a match if they share at least one common signature. We denote this by the indicator function

Example 2. Figure 2 demonstrates an LSH with P = 100, B = 25, R = 4, where MinH H1 5 (s 1 ) = 17, MinH H2 5 (s 1 ) = 43, etc. Subsequently, every sequence of R digests is concatenated and hashed to produce a band signature, with a total of B band signatures, which form the LSH of s 1 , LSH(s 1 ) = (865, 1082, . . . , 172). Repeating the process for s 2 , we observe a match in the signature of the second band for the two compared strings; this means that the two LSHs match and the strings match with a high probability.

## Private set intersection (PSI)

PSI is a cryptographic protocol that allows two parties to compute the intersection of their private sets without revealing anything beyond this fact or beyond the size of the intersected sets to the other party. PSI is a special case of PPRL, which considers only exact matches. Some variations of PSI allow the parties to learn just the cardinality of the intersection.

Many PSI solutions exist (see Section 1). In this work, we use a unidirectional variant of the DH-PSI [30], as presented in Figure 3. The two parties P s and P r first agree on a group G and a collision-resistant hash function H, and each party generates its own secret key sk s and sk r , respectively. Subsequently, both parties hash and encrypt their records using their private keys and send them to the other party. In addition, P r encrypts the output of P s using its secret key and sends the results back to P s . Finally, P s learns the intersection of the two datasets.

# Ps (sks)

Pr ( skr)

Informally, the security of these protocols against semi-honest adversaries is guaranteed by the one-way property of the hash function, the computational hardness of the decisional DH, and the one-more-DH [17] assumptions (see definitions in Appendix A). The decisional DH is used to hide the data in transit from eavesdroppers, while the one-more-DH assumption is used to prevent P s from generating new records in the name of P r .

One DH-PSI variant is the mutual DH-PSI, which includes one extra round: P s sends D r to P r so that P r can also compute the intersection. However, here an eavesdropper learns both D s and D r and can therefore learn the cardinality of the intersection D s ∩ D r .

One issue with DH-PSI is that it is susceptible to man-in-the-middle attacks [13]. To mitigate this attack and the leakage of the mutual DH-PSI's intersection cardinality,we assume that the transportation is encrypted and authenticated using TLS 1.3.

# PPRL

PPRL is an ER protocol between two parties P s and P r , with private datasets D s and D r of sizes N s and N r , respectively; these records have a similarity measure µ(•, •), and some additional privacy requirements. These requirements may lead to several security models and several formal definitions of PPRL.

The most intuitive way to define privacy for PPRL is by following the PSI privacy notion: P s only learns N r and the intersection D s ∩ D r , i.e., all records that exactly match in all fields while P r only learns N s . Note that in both PSI and PPRL, P s and P r need to share the nature of the information contained in their datasets with each other to decide which QIDs they can validly compare.

The difference between PSI and PPRL is that PSI only returns exact matches according to some uniquely identifying QIDs, while PPRL returns matching records up to some similarity indicator and according to non-unique QIDs. For example, a PSI protocol may rely on users' SSNs, while a PPRL protocol may compare first and last names. Thus, a PPRL may inadvertently match "David Doe" with "Davy Don" even if they represent different entities (users). Figure 4 shows a Venn diagram for the output of different ER solutions on D s and D r datasets. With the exact matching method (D s ∩ D r ) no privacy risks occur since it only reveals the agreed-upon intersection 3 . In contrast, when using the Jaccard similarity to compute the matches, the parties learn: a) records in D s ∩ D r , which is ok; b) records outside D s ∩ D r that represent the same entity (true-positive), which is also ok; c) records outside D s ∩ D r that represent different entities (false-positive), which may break the privacy of the parties. In general, any PPRL protocol must assume this kind of leakage, and should do its best to quantify it, e.g., by assuming the existence of a bound τ on the similarity false-positive rate.

# Definition 3 (PPRL).

A PPRL protocol P between two parties P s , P r with datasets D s , D r , respectively, a similarity measure µ, a measure indicator I µ t for a fixed threshold t with a false-positive rate bounded by τ , has the following properties.

-Correctness: P is correct if it outputs to P s the set

where Enc(r) is an encryption of r under a secret key of P r . -Privacy: P maintains privacy if P s only learns res and N r , and P r only learns N s .

Corollary 1. The leaked information of P r in P is bounded by τ • |res| Nr .

Definition 3 assumes the existence of τ but only implicitly uses it. The reason is that τ does not always exist. In many cases, it can be empirically estimated based on prior data or based on perturbed synthetic data. However, relying solely on empirical estimates increases the ambiguity of the privacy definition for such protocols. Moreover, in many cases, τ depends on data from the two datasets that have different distributions, which none of the parties know in advance. Another reason for only implicitly relying on τ is that the leaked information in Cor. 1 depends on res and can only be computed after running the protocol.

While τ bounds the privacy leak from above, there is still the issue of quantifying the exact leakage after the protocol ends. It is not clear how the parties can verify the number of false-positive cases without revealing private data. Usually, an ER protocol is used when the compared records do not include uniquely identifying fields (such as an SSN) and thus the parties cannot compute the exact matches using PSI. Consequently, their only way to verify matches is by revealing their private data. To assist in this task, we define a protocol called a revealing PPRL. Definition 4 (Revealing PPRL). A revealing PPRL protocol P is a PPRL protocol P , where P r also learns u = {Enc(r) | (s, Enc(r)) ∈ P .res} and P s also learns res = {(r, Enc(r)) | (s, Enc(r)) ∈ P .res},

In words, P r learns which of its own records are matched, and P s learns the field content of the matched records of the other party. The simplest way to achieve a revealing PPRL is for P s to send u to P r , who will then decrypt its values and hand them back to P s . The difference between Definitions 3 and 4 is that in the latter, P s learns the values of P r 's records instead of just their encryption. While this definition leaks more data from P r to P s , it is easier to analyze because now P s can verify the matches with some probability and learn the estimated number of false-positives. We also consider the definitions of the associated mutual PPRL and the mutual revealing PPRL.

# Definition 5 (Mutual PPRL).

A PPRL protocol P between two parties P s , P r with datasets D s , D r , respectively, a similarity measure µ, a measure indicator I µ t for a fixed threshold t with a false-positive rate bounded by τ , has the following properties.

-Correctness: P is correct if it outputs res s (resp. res r ) to P s (resp. P r ),

where

, and Enc(r) (resp. Enc(s)) is an encryption of r (resp. s) under a secret key of P r (resp. P s ).

-Privacy: P maintains privacy if P s only learns res s and N r , and P r only learns res r and N s .

The mutual revealing PPRL is similarly defined. The difference between the mutual PPRL and the revealing PPRL in terms of privacy is that in the mutual PPRL, P r can match the encryption of P s records to its records and therefore gains more information while P s only learns the encryption of P r records.

In the PPRL protocols described above, the two parties learn the intersection of their datasets. However, in some scenarios, the parties merely need to learn the number of matches and do not wish to reveal the identity of the matched records to the other party. To this end, we define an N-PPRL protocol.

# Definition 6 (N-PPRL).

A PPRL protocol P between two parties P s , P r with datasets D s , D r , respectively, a similarity measure µ, a measure indicator I µ t for a fixed threshold t with a false-positive rate bounded by τ , has the following properties.

-Correctness: P is correct if it outputs to P s the value

-Privacy: P maintains privacy if P s , (resp. P r ) only learns N s∩r , N r (resp. N s ).

The mutual N-PPRL protocol is similarly defined.

# Our solution

Our PPRL solution (hereafter: LSH-PSI PPRL) is an ER protocol that uses LSHMatch as its similarity indicator, where for privacy reasons, the parties cannot directly share the LSH results. The reason depends on whether the LSH is a preimage-resistant hash function or not. When it is not, P r and P s can simply inverse the LSH results for records that are not in the intersection and reveal private information of P s , P r , respectively. But even when it is, the solution's privacy depends on the LSH input entropy, where the parties can maintain an offline brute force attack against the LSH records of the other party. To mitigate the privacy issue, we use a PSI protocol. The two parties first compute the LSH band signatures of all their records and then apply a PSI protocol over these signatures. Finally, P s maps back the intersected signatures to the original records to learn the set of similar records. The concrete properties of LSHMatch can be tuned using the B and R LSH parameters. Figure 6 presents the LSH-PSI protocol, and Figure 5 illustrates it schematically.

Our protocol is defined against semi-honest (honest-but-curious) adversaries, where all parties do not deviate from the protocol, and their inputs are genuine. Nevertheless, they may record and analyze all the intermediate computations and messages from the other parties to get more information.

Remark 1. The two parties must use the same preprocessing techniques to increase the efficiency of the underlying ER method. In addition, the LSH-PSI protocol assumes that the pre-processing phase runs some deduplication protocol on the dataset of every party. Otherwise, P s can extract information from pairs of matching records s 1 , s 2 ∈ D s , where s 1 matches a record in D r but s 2 does not.

Remark 2. The PSI protocol is executed for all records at once and not per record, therefore it is critical to preserve the order of the signatures exchanged between the parties, i.e., of L s and L s in Figure 5. Otherwise, it will be impossible to match the records in Step 4 of Figure 6. In Section 4.1, we discuss the case where P r does not preserve the order of P s encrypted signatures.

The purpose of using the permutation π p in Step 1b is to avoid the case where the other party learns information about "missing" records. For example, suppose that the records in D r are ordered alphabetically according to a first name QID, and that P s learns that Jerry and Joseph are in the intersection. If Jerry and Joseph happen to belong to adjacent records in D r , then an honest 

The two parties run a DH-PSI protocol over their respective band signatures so that Pr only learns Ns, and Ps only learns Nr and

Ps generates the array

Ps returns the matching records

Fig. 6: The LSH-PSI PPRL protocol. but curious P s learns that P r has no record for John. When using a permutation, the only way for P s to deduce the same information is by learning all the records in D r . A concrete example of Steps 1.b -3 is given in Appendix B.

Theorem 1. The LSH-PSI PPRL protocol is a PPRL protocol according to Definition 3 where the similarity indicator is LSHMatch. This protocol is secure against semi-honest adversaries.

Proof. Correctness. The correctness of the protocol follows from the fact that the intersection L s ∩ L r has a one-to-one correlation with the encrypted band signatures L s ∩ L r . Privacy of P s . By the discrete-log assumption, P r only gets to see N s elements that are indistinguishable from random values. Thus, P r only learns N s .

Privacy of P r . P s gets from P r the values of L s and L r raised to the power of P r 's secret key. By the discrete-log assumption, these values are indistinguishable from random to P s . Except that P s can raise L r values to the power of its own secret key and then intersect the results with L s . This intersection of random values is used by P s to identify matching signatures, which is expected by Definition 3. Because P s learns nothing from values outside the intersection, we say that it only learns res and N r as expected.

Remark 3. Similar to the DH-PSI case, the use of TLS 1.3 allows the parties to mutually authenticate themselves and to avoid the attack presented in [13]. Still, as a defense-in-depth mechanism, the parties in every PPRL session should avoid reusing secret keys to avoid man-in-the-middle attacks.

## PPRL variants

Based on the above protocol, we construct three other protocols: a mutual PPRL protocol, an N-PPRL protocol, and a revealing PPRL protocol, where the latter immediately follows the definition. A mutual PPRL protocol. To establish a mutual PPRL protocol, we modify Step 2 of Figure 6 to use the mutual DH-PSI protocol of Section 2.3. The security of the protocol follows from either the security of the mutual DH-PSI, or from the fact that the mutual protocol is equivalent to running the original PPRL protocol twice: first between P s and P r , and subsequently between P r and P s . Note that P s cannot reduce the communication by sending only records that are in the intersection because then an eavesdropper can learn the intersection size. This claim is valid even when using a secure communication channel (e.g., TLS 1.3). An N-PPRL protocol. To achieve an N-PPRL protocol, we could have simply counted the number of elements in the intersection set res, but this would reveal to P s more information beyond N s∩r . Instead, we suggest reordering the encrypted band signatures during the DH-PSI in a way that hides the identity of the matched records but still enables them to be counted. Specifically, we ask P r to apply a secret permutation to L s before sending it to P s . This permutation has a special property that permutes together the groups of adjacent B signatures that originate from the same record, otherwise, P s will not be able to distinguish between the cases

We call the above permutation an intra-permutation of records. In addition, we apply an inter-permutation of records, where we separately permute the B signatures in each group of signatures in L s that originate from the same record.

# Experiments

Experimental setup. We carried out the experiments on two machines that are located in different local area networks (LANs). We measured an average of 65 ms round-trip latency between them. -Machine A has an Intel ® Xeon ® CPU E5-2620 v3 @ 2.40GHz, with 12 physical cores and 377 GB of RAM.

-Machine B has an Intel ® Xeon ® CPU E5-2699 v4 @ 2.20GHz, with 44 physical cores and 744 GB of RAM.

We set machine A to run P s and machine B to run P r with N s ≈ N r .

Our code is written in C++ and runs on Ubuntu 20.04. It uses OpenSSL version 1.1.1f to establish secure TLS 1.3 connections between the two parties. In addition, it uses OpenSSL hash function implementation (concretely, H=SHA256) and DH operations (concretely, elliptic curve DH operations over the NIST P-256 curve). We report communications in KB and running time in seconds. We also provide a breakdown of the different running time phases: communication and computations per party. For the measurements, we separated the communication phases from the computation phases, which in a real scenario can be pipelined to run in parallel.

For the evaluations, we considered two dataset cases: a) The North Carolina voter register (NCVR) dataset 4 , which is commonly used for PPRL evaluations; b) a synthetic dataset that we generated and made available in [35]. NCVR datasets. We used the November 2014 and November 2017 snapshots of the NCVR datasets. Prior to running the PPRL protocol, we deduplicated the snapshots by eliminating duplicate records with identical "NCID" or with identical values in the 'first name', 'last name', 'midl name', 'birth place' and 'age' fields. Subsequently, we removed the NCID field from the two snapshots, and ran our PPRL protocol on the two snapshots. A reported matching pair was considered to be a true-positive event if the two reported records share the same NCID value. Table 1 shows the accuracy breakdown of the LSH we used by reporting the number of false-negative (FN), false-positive (FP), and true-positive (TP) events, together with the precision, recall, and F1 results when sampling sets of fixed sizes from the above snapshots. Note that while the precision is high, the absolute number of false-positives may be regarded as too high for some users. See Section C.1 for ways to tune the process and balance the number of false positive and false negative cases while considering the protocol performance. Synthetic dataset. We generated two synthetic datasets using IBM InfoSphere ® Optim T M Test Data Fabrication [21] with the following fields: 'first name', 'last name', 'email', 'email domain', 'address number', 'address location', 'address line', 'city', 'state', 'country', 'zip base', 'zip ext', 'phone area code', 'phone exchange code' and 'phone line number', where N s ≈ N r ≈ 1, 000, 000. We generated the datasets in a way that only 100 records in the two datasets represent identical entities. The pairs of records that describe these shared entities sometimes have identical fields and sometimes fields with minor typos, different styles, and other types of minor differences, which are still small enough to warrant the assumption that the similar records in fact describe the same entity. Our PPRL protocol identified all the matching records. The performance evaluation of the protocol is given in Table 2.

# Conclusion

We presented a novel PPRL solution that relies on LSH to identify similar records while using PSI to ensure privacy. We formally defined the privacy guarantees that such a protocol provides and evaluated its efficiency. Our results show that it takes 11 -45 minutes (depending on the network settings) to perform a PPRL solution comparing two large datasets with 2 20 records per dataset. Note that none of the results presented in Section 1.1 reported comparable speeds for such large datasets. This makes our solution practical and attractive for companies and organizations. We made our implementation available for testing at [35]. We proposed a PPRL framework that can use different PSI protocols as long as they provide the same security guarantees defined above. We demonstrated our solution using an ECDH PSI protocol. It may be an interesting direction to implement and test the protocol using other solutions that can further improve its performance and overall bandwidth.

where the probability is taken over (g, a, b). Definition 9 (One-more-DH (OMDH) [17]). Let G be a cyclic group. The one-more-DH problem is hard, if for every PPT adversary A that gets a generator g ∈ G together with some power g a and who has access to two oracles: h a = CDH g,g a (h) for some h ∈ G, and r $ ← -C() a challenge oracle that returns a random challenge point r ∈ G and can only be invoked after all calls to the CDH g,g a , it follows that

where the probability is taken over (g, a).

# B Example of the LSH-PSI protocol

A concrete example of Steps 1.b -3 of the LSH-PSI PPRL protocol (Figure 6) is given in Figure 7. Suppose that v = H(455) sksskr then P s learns via the PSI process that P r also has a band signature with the same value 455. P r took care to preserve the order of P s 's encrypted band signatures during the PSI, so P s can map the shared value v back to the band signature for Band 1 of record N s , and deduce that P r has some unknown record that is similar to her own record N s . 

# C Using the Jaccard indicator

Theorem 1 shows that the LSH-PSI PPRL protocol follows Definition 3 when considering the LSH as the similarity indicator. This means that security reviewers need to accept the privacy leakage that occurs when using an LSH, something that is already done by many organizations that perform RL. However, some reviewers may instead prefer to trust the Jaccard index due to its wide acceptance.

Figure 4 shows two ways to define LSH false-positive events: in relation to exact matches of entire records as in the LSH-PSI PPRL, or in relation to the method of matching pairs of records with a high enough Jaccard index. Thus according to the latter definition an LSH false-positive happens only when a pair of records are matched due to having at least one shared LSH band, and yet they do not have a high enough Jaccard index to justify a claim of similarity. Bounding the false-positive events rate τ based on the latter definition will allow us to define an LSH-PSI PPRL related to the Jaccard index metric but with a different bound τ • τ , where τ is the Jaccard original false-positive bound. In this section, we further discuss the relation between the LSH and the Jaccard index.

For two records s, r with Jaccard index J, Figure 8 shows the probability for an LSHMatch = 1 event according to Equation 2 with R = 200 and B = 20. In standard ER solutions, it is the role of the domain expert to decide the specific Jaccard index that would indicate enough similarity between the two records. For example, in the figure the targeted Jaccard index is 0.78. The figure shows the cumulative probability of getting true-positives (J(s, r) > 0.78 and LSHMatch(s, r) = 1), true-negatives (J(s, r) ≤ 0.78 and LSHMatch(s, r) = 0), and the corresponding false-positive and false-negative cumulative probabilities.

The above example shows that when B = 20 and R = 200, it is possible to close the gap between the Jaccard index and the LSH by choosing the Jaccard threshold to be below 0.5. In that case, the probability for a false-positive event is less than 0.0001, which means that one in every ten-thousand records leaks. However, using such a Jaccard threshold will yield many false-positive cases relative to exact record matching, which is less desirable in terms of privacy.

It turns out that it is possible to tune the slope of the accumulated probability function. Figure 9 compares the probability functions in four different setups B = 20, R = 200 (setup 1) B = 100, R = 100 (setup 2) B = 14, R = 30 (setup 3) and B = 120, R = 18 (setup 4). Here, we see that replacing setup 1 with setup 2 allows us to set the Jaccard threshold at 0.78 while reducing the LSH false-positive rate to as low as 10 -8 . However, setup 2 dramatically increases the LSH false-negative rate. Note however that false negatives affect the security less than false-positives, and in addition, users are often much more reluctant to report false positives than to miss reports due to false negatives. Setup 2 may also increase the overall performance of the protocol relative to setup 1 because there are many more bands to encrypt and communicate, as described in the following section. 

# C.1 Optimizing the protocol

Setup 4 in Figure 9 probably results in more false-positive and false-negative cases than setup 1, and the low slope of the curve implies a larger region of uncertainty. However, the PSI for setup 4 runs more than 6 times faster than the PSI for setup 1, because there are just 20 rather than 180 band signatures that need to be encrypted and communicated. The change in the R parameter does not affect the performance as much, since it merely determines the number of Min-Hashes that need to be computed locally. It turns out that computing a Min-Hash (like the highly optimized SHA-256 operation) is much faster than computing the power in the underlying groups of the DH protocol. Moreover, there are known methods for quickly producing R different permutations out of a single SHA-256 call such as the Mersenne twister [3]. Finally, the value of R does not affect the size of the communication.

We use the B and R parameters to control the curve, which in turn affects the protocol's accuracy and performance. Reducing B makes it less likely to find a matching band signature, thus increasing the false-negative probability, but improving performance. The rate of false-negatives can be reduced by decreasing R, thus making it more probable for two bands to match. Conversely, if the falsepositive rate is too high, then one can increase R with little performance penalty. We therefore optimize the process by searching for values of B and R that have the minimal B value (for best performance) while more or less preserving the targeted curve shape.

Suppose for example that setup 1 has the targeted probability function 

# C.2 Scoring the reported matches

When a PPRL protocol relies on the Jaccard index but its implementation uses LSH, it may be in the users' interest to quantify the number of false-positive events. To this end, we present a way to estimate the Jaccard index based on the LSH results.

Estimating the Jaccard index for matching pairs When using LSH with B band signatures, it is possible to estimate the actual Jaccard index J by using a binomial confidence interval. By observation 1, the probability for a matching band (i.e. the probability for a match in all R Min-Hashes of the band) is p = J R . Suppose that P s learns that there are h matching band signatures and t = B -h non-matching band signatures. Using a 95% confidence interval, the Jaccard index lies in the range

In some cases this interval is too wide, and the users may prefer using a different approach, such as a revealing PPRL. In a revealing PPRL, the two parties learn the intersection of their datasets as in a standard PPRL but they also learn the records of the other parties that are involved in of the intersection. Thus, the leaked information in a revealing PPRL is higher than in a PPRL.

Below, we propose an approach with privacy leakage that lies between the leakage of a revealing PPRL and a PPRL, where we compute the Jaccard index only for matching pairs, without revealing the exact shingles.

Computing the precise Jaccard index for matching pairs Suppose that at the end of the LSH-PSI PPRL protocol, P s learns the matching pair (s, Enc(r)). P s can ask P r to participate in another PSI process over the set of shingles of (s, r), where P s knows s and P r knows r. In this PSI, P s only learns the intersection size of the associated shingles |S ∩ R| and the size |R|, so it can compute J(s, r) = |S∩R| |S|+|R|-|S∩R| . Note that learning only the intersection size and not the intersection itself makes it harder for P s to guess P r 's record.

These additional PSIs are relatively expensive in terms of performance, but we only need to carry them out for the reported matches, which are presumably only a very small fraction of all possible pairs of records. P s and P r can decide to perform such PSIs for every matching pair or for selected pairs of special interest, or for pairs selected after estimating the Jaccard index as described above. As mentioned in Section 3 performing a selective PSIs leaks the size of the selection to an eavesdropper and this should be taken into account in the application threats model.

# D Our implementation

For reproducibility, we provide concrete details about our LSH implementation. We start by explaining the concept of relative weighting of the record fields.

# D.1 Relative weighting of the record fields

Some record fields may be more indicative of identity than other fields. For example, an SSN field is very indicative (though it may also include typos), and a similarity of the full names is more indicative of identity than the similarity of zip codes. A simple method of weighting the effect of the different fields on the matching process is to duplicate the shingles originating from a field for a predefined number of times. We call this number the field weight. For example, consider a PPRL that operates over records with two fields: name and zip code. We use k=6 and k=7 shingles for these fields and set their weights to be 3 and 1, respectively. Then, the 6-shingle 'John S' extracted from the name field 'John Smith' will be duplicated into three separate shingles 'John S1', 'John S2', 'John S3', whereas the zip-code 7-shingle '2304170' will not be duplicated. This causes shingles originating from the name to be three times more likely than zip-code shingles to be the minimum value used by the Min-Hashes of the LSH (see Section 2.2). This will make the band signatures more likely to match if name shingles are identical than if zip-code shingles are identical.

The problem with this shingle duplication weighting method is that the extra shingles slow down the PPRL process because more shingles need to be hashed by the many Min-Hashes. To this end, we present a novel method for weighting the shingles, which yields the same results as the shingle duplication method but is much faster. The idea is to reduce the hash value of a shingle according to the shingle's weight, to directly increase its chance of being the shingle that receives the minimal value by the Min-Hashes.

We view the hash code h of a shingle as a discrete random variable with uniform distribution over some integer range [0, maxV al]. Thus, x = h/maxV al is approximately a random variable with a continuous uniform distribution over [0, 1]. Our method relies on this being a good approximation.

Our method is as follows: instead of duplicating a shingle w times, we compute the shingle's hash-code h, normalize it x = h/maxV al, then apply the transformation y = 1 -(1 -x) 1/w , and finally return back to the original scale h = y * maxV al . Lemma 1 shows that this results with a variable h whose distribution is the same as the minimum of w independent hashes. Y (H 1 ). The CDF of X is therefore

Since H 1 is a uniform variable over [0, 1], this means F X (x) = F Y (x).

We observed a 9% speedup when comparing the computation time (ignoring communications) of our PPRL solution using the shingle duplication method versus the above hash-dropping method.

Remark 4. The work in [22] also describes a method of computing a 'Weighted MinHash' over multisets with duplicated elements, but the universe of all possible items (or dimension for vectors) is assumed to be known in advance.

# E LSH description

We are now ready to describe our LSH implementation. The algorithms below use a data structure that we call the field-group data structure F G, which is a list of tuples (s, k, w), where s is a string, k ∈ N is the shingles length, and w ∈ N is a vector with the shingles' weights, respectively. Algorithm 1 computes the LSH for a given record record. First, it concatenates together strings from fields that belong to the same group according to the configuration variable conf (Lines 5-6). Then, it attaches to every concatenated string the k, w values of its group as defined by conf (Line 7). The algorithm returns the output of the LshFG function on the generated field-group data structure F G (Line 8).

The LshFG algorithm uses the auxiliary functions getWeigthedShingles, which we describe in Algorithm 2. Its input is a field-group data structure and its output is a list of pairs of k-shingles and their respective weights. return L

