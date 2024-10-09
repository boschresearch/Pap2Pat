# DESCRIPTION

## BACKGROUND

1. Statement of the Technical Field

The inventive arrangements relate to cryptographic systems. More particularly, the inventive arrangements concern cryptographic systems implementing a customizable encryption algorithm based on a sponge construction with authenticated and non-authenticated modes of operation.

2. Description of the Related Art

Sponge functions may be used in cryptographic applications. In this regard, the sponge functions can be used to implement symmetric cryptography functionalities (e.g., key derivation, message encryption, and authentication code computation). A detailed discussion of sponge functions is provided in a document entitled “Cryptographic Sponge Functions”, which was written by Bertoni et al. and published on Jan. 14, 2011 (“Bertoni”). As stated in Bertoni, a sponge function instantiates a sponge construction. The sponge construction is a simple iterated construction for building a function F based on a fixed length permutation. The function F has a variable-length input and an arbitrary output length. The fixed length permutation operates on a state of b=r+c bits, where r is the bitrate and c is the capacity. The capacity c determines the security level of the sponge construction.

During operation, each of the bits b is initialized to zero and an input message is cut into blocks of r bits. Thereafter, absorbing operations are performed in which: the r bits of each block are respectively XORed with the first r initialized bits; and a first permutation operation is performed using the results of the XOR operation as inputs. Next, squeezing operations are performed in which a second permutation operation is performed using the output bits of the first permutation operation as input bits. The output of the second permutation operation may then be truncated to the first l bits.

Duplex constructions are closely related to the sponge construction. Duplex constructions comprise a plurality of duplexing stages. During a first duplexing stage, all bits of the state are set to zero and a first input string τ0 is padded. The first input string τ0 is then XORed with the first r initialized bits. Then, a permutation function is applied to the results of the XOR operations so as to generate a set of first output bits. The first output bits are then truncated to the first l bits. In a next duplexing stage, a second input string τ1 is padded. The second input string τ1 is then XORed with the first output bits of the first duplexing stage. The permutation function is applied to the results of the XOR operations so as to generate a set of second output bits. The second output bits are then truncated to the first l bits.

## SUMMARY OF THE INVENTION

The invention concerns implementing systems and methods for generating encrypted data (e.g., ciphertext). The methods involve: combining a cryptographic key with state initialization bits to generate first combination bits; producing a first keystream by performing a permutation function ƒ using the first combination bits as inputs thereto; and using the first keystream to encrypt first data (e.g., authentication data or message body data) so as to produce first encrypted data (e.g., via modular arithmetic). The permutation function ƒ comprises a round function ƒround that is iterated R times. The round function ƒround consists of (1) a substitution layer in which the first combination bits are substituted with substitute bits, (2) a permutation layer in which the substitute bits are re-arranged, (3) a mixing layer in which at least two outputs of the permutation layer are combined together, and (4) an addition layer in which a constant is added to the output of the mixing layer.

The cryptographic key may be concatenated with a flag value prior to being combined with the state initialization bits. The first keystream may be truncated to a desired length prior to being used to encrypt the first data. The first data may be padded to make a total number of bits contained therein a multiple of the total number of state initialization bits prior to being encrypted. A multi-bit value for the state initialization bits may be selected that is unique for a given application.

In some scenarios, the present invention is implemented in a sponge framework. Accordingly, the method may additionally comprise: producing a second keystream by performing the permutation function ƒ using the first keystream as inputs thereto; and using the second keystream to encrypt second data (e.g., other message data) so as to produce second encrypted data.

In other scenarios, the present invention is implemented in a duplex framework. Accordingly, the first encrypted data is produced by: combining the first keystream with authentication data to generate the second combination bits; producing a second keystream by performing the permutation function ƒ using the second combination bits as inputs thereto; and combining the second keystream with the message body data so as to produce the first encrypted data. An authentication tag is generated by: combining the second keystream with the message body data to produce the third combination bits; producing a third keystream by performing the permutation function ƒ using the third combination bits as inputs thereto; and using at least a portion of the third keystream as the authentication tag.

## DETAILED DESCRIPTION

It will be readily understood that the components of the embodiments as generally described herein and illustrated in the appended figures could be arranged and designed in a wide variety of different configurations. Thus, the following more detailed description of various embodiments, as represented in the figures, is not intended to limit the scope of the present disclosure, but is merely representative of various embodiments. While the various aspects of the embodiments are presented in drawings, the drawings are not necessarily drawn to scale unless specifically indicated.

The present invention may be embodied in other specific forms without departing from its spirit or essential characteristics. The described embodiments are to be considered in all respects only as illustrative and not restrictive. The scope of the invention is, therefore, indicated by the appended claims rather than by this detailed description. All changes which come within the meaning and range of equivalency of the claims are to be embraced within their scope.

Reference throughout this specification to features, advantages, or similar language does not imply that all of the features and advantages that may be realized with the present invention should be or are in any single embodiment of the invention. Rather, language referring to the features and advantages is understood to mean that a specific feature, advantage, or characteristic described in connection with an embodiment is included in at least one embodiment of the present invention. Thus, discussions of the features and advantages, and similar language, throughout the specification may, but do not necessarily, refer to the same embodiment.

Furthermore, the described features, advantages and characteristics of the invention may be combined in any suitable manner in one or more embodiments. One skilled in the relevant art will recognize, in light of the description herein, that the invention can be practiced without one or more of the specific features or advantages of a particular embodiment. In other instances, additional features and advantages may be recognized in certain embodiments that may not be present in all embodiments of the invention.

Reference throughout this specification to “one embodiment”, “an embodiment”, or similar language means that a particular feature, structure, or characteristic described in connection with the indicated embodiment is included in at least one embodiment of the present invention. Thus, the phrases “in one embodiment”, “in an embodiment”, and similar language throughout this specification may, but do not necessarily, all refer to the same embodiment.

As used in this document, the singular form “a”, “an”, and “the” include plural references unless the context clearly dictates otherwise. Unless defined otherwise, all technical and scientific terms used herein have the same meanings as commonly understood by one of ordinary skill in the art. As used in this document, the term “comprising” means “including, but not limited to”.

Sponge and duplex constructions provide frameworks representing new cryptographic paradigms with many advantages including processing performance and provable computational cryptographic strength. A novel cryptographic algorithm design is described herein that is based on the sponge and duplex construction frameworks. More particularly, the novel cryptographic algorithm comprises a unique permutation function ƒ that is used with a sponge construction and/or a duplex construction. In this regard, the present invention provides the same advantages of conventional sponge and duplex constructions, as well as other additional advantages. These other additional advantages include, but are not limited to: the provision of a highly configurable and customizable cryptographic algorithm; the provision of a symmetric key algorithm that is designed against a military threat model; the provision of increased throughput suitable to support high-rate networked waveforms; and the provision of an algorithm that can be used with key lengths that are longer than the key lengths which can be used with conventional cryptographic algorithms. Longer key lengths result in a higher level of security.

Referring now to FIG. 1, there is provided a schematic illustration of an exemplary architecture for a sponge construction 100 implementing the present invention. Notably, the sponge construction 100 uses a unique permutation function ƒ (described below) to provide the traditional suite of cryptographic modes. This will become more evident as the discussion progresses.

As shown in FIG. 1, the sponge construction 100 is generally designed to implement symmetric cryptography functionalities, namely key derivation and message encryption. The sponge construction 100 is a simple iterated construction for building a function F based on a unique permutation function ƒ. The function F has a variable-length input and an arbitrary output length. The unique permutation function ƒ operates on a state of b=r+c bits, where r (e.g., 128 bits) is the bitrate and c (e.g., 384 bits) is the capacity. The capacity c determines the security level of the sponge construction.

Notably, the sponge construction 100 can be implemented in hardware, software or a combination of both hardware and software. As such, the operations of each functional block 102-106 may be implemented using hardware and/or software. The hardware can include, but is not limited to an electronic circuit. The electronic circuit can include passive components, active components and logical components.

The sponge construction 100 is divided into two phases. The first phase is an absorbing phase 120 in which the cryptographic key K or K∥N (i.e., a concatenation of the cryptographic key K and a flag N) is absorbed into a state of the sponge construction 100 while interleaving with applications of the underlying permutation function ƒ. Such absorption is achieved by combining K (or K∥N) with the first r bits of the initialized state bits b. In some scenarios, the bits b (e.g., 512 bits) are initialized to zero. The present invention is not limited in this regard. The bits b (e.g., 512 bits) may alternatively be initialized to any bit value (e.g., any 512 bit value). As such, each user could generate its own unique value to set during the initialization phase.

The combining of K (or K∥N) with the first r bits of the initialized state can be achieved via exclusive OR (“XOR”) operations 110, as shown in FIG. 1. XOR operations are well known in the art, and therefore will not be described in detail here. Still, it should be understood that the XOR operations are performed on a bit-by-bit basis. The result of each XOR operation is true whenever an odd number of inputs are true and false whenever an even number of inputs are true. The results of the XOR operations are then passed to permutation functional block 102 where the results are interleaved with applications of the unique permutation function ƒ.

The second phase is a squeezing phase 122 in which keystream blocks Z0, Z1, Z2 are produced by the performance of the unique permutation function ƒ in permutation functional blocks 102-106. Each keystream block Z0, Z1, Z2 comprises r bits. The unique permutation function ƒ will be described in detail below. Still, it should be understood that the permutation function ƒ maps each possible value of the bits input thereto into a particular unique value of the output bits. Notably, permutation functional block 102 takes the output of the absorbing phase 120 as an input. Permutation functional block 104 takes the output of permutation functional block 102 as an input. Permutation functional block 106 takes the output of permutation functional block 104 as an input.

Next, the keystream blocks Z0, Z1, Z2 are used to encrypt a message M. In this regard, the keystream blocks Z0, Z1, Z2 can be truncated to a desired length l. Additionally or alternatively, the message M may be padded to make it a multiple of r (if it is not a multiple of r). The message M is parsed into a plurality of message blocks M0, M1, M2. Each message block M0, M1, M2 comprises a plurality of bits of the message M. Each keystream block is then combined with a respective message block so as to produce an encrypted data block. The encrypted data block can include, but is not limited to, a ciphertext block C0, C1 or C2. The present invention is described herein in relation to ciphertext. The present invention is not limited in this regard. The present invention can be used to encrypt any type of data (e.g., text, audio, video, etc. . . . ).

In some scenarios, the combining of the keystream and message blocks is achieved using modular arithmetic. For example, each keystream block Z0, Z1, Z2 is combined with a respective block of message bits M0, M1, M2 via modulo 2 addition. The modulo 2 addition can be implemented using an XOR operation, as shown in FIG. 1. The XOR operation is performed on a bit-by-bit basis. As such, a first bit m0 of a message block M0, M1 or M2 is combined with a first bit z0 of a respective keystream block Z0, Z1 or Z2 via modulo 2 addition. Next, a second bit m1 of a message block M0, M1 or M2 is combined with a first bit z1 of a respective keystream block Z0, Z1 or Z2 via modulo 2 addition, and so on.

Referring now to FIG. 2, there is provided a schematic illustration of an exemplary architecture for a duplex construction 200 implementing the present invention. The duplex construction 200 is an adaptation of the sponge construction framework that, together with the unique permutation function ƒ (described below), provides an additional Authenticated Encryption (“AE”) cryptographic mode. This mode allows both source and integrity verification of encrypted traffic. This will become more evident as the discussion progresses.

Notably, the duplex construction 200 can be implemented in hardware, software or a combination of both hardware and software. As such, the operations of each component 202-232 may be implemented using hardware and/or software. The hardware can include, but is not limited to an electronic circuit. The electronic circuit can include passive components, active components and logical components.

In the duplex construction 200, the absorbing phase and squeezing phase are combined into each of a plurality of duplex operations. Accordingly, the duplex construction 200 comprises a plurality of duplex objects 202-206. The operations of each duplex object will be described separately below. Notably, the state of each duplex object call is preserved.

The input to duplex object 202 is a cryptographic key K (or optionally K∥1, i.e. a concatenation of the cryptographic key K and a flag 1). The cryptographic key K (or optionally K∥1) is padded in padding functional block 214 to make it a multiple of r (if it is not a multiple of r). The padding can involve appending bits to the beginning or end of the cryptographic key K (or optionally K∥1). Next, the output of padding functional block 214 is then combined with the first r bits of the initialized state bits b. In some scenarios, the bits b are initialized to zero, where b=r+c. The present invention is not limited in this regard. The bits b (e.g., 512 bits) may alternatively be initialized to any bit value (e.g., a 512 bit value). As such, each user could generate its own unique value to set during the initialization phase.

The combining of the padding functional block output and the first r bits of the initialized state can be achieved via XOR operations 110, as shown in FIG. 1. XOR operations are well known in the art, and therefore will not be described in detail here. Still, it should be understood that the XOR operations are performed on a bit-by-bit basis. The results of the XOR operations are then passed to permutation functional block 208. In permutation functional block 208, the unique permutation function ƒ is performed using the results of the XOR operations as inputs so as to generate a keystream block Z0. The keystream block Z0 is then truncated to a desired length l, as shown by truncate functional block 220. The value of l here can be less than r.

The input to duplex object 204 is authentication data A (or optionally A∥0, i.e. a concatenation of authentication data A and a flag 0). The authentication data A can include but is not limited to, authenticated packet headers. The authentication data A (or optionally A∥0) is padded in padding functional block 216 to make it a multiple of r (if it is not a multiple of r). The padding of padding functional block 216 is the same as or similar to that of padding functional block 214. Next, the output of padding functional block 216 is then combined with keystream block Z0. This combining can be achieved via XOR operations 228, as shown in FIG. 2. XOR operations are well known in the art, and therefore will not be described in detail here. Still, it should be understood that the XOR operations are performed on a bit-by-bit basis. The results of the XOR operations are then passed to permutation functional block 210. In permutation functional block 210, the unique permutation function ƒ is performed so as to generate a keystream block Z1. The keystream block Z1 is then optionally truncated to a desired length l, as shown by truncate functional block 222. The value of l here can be less than r. Truncation may be performed when the number of bits contained in the message body B is less than r. In this case, the value of l equals the number of bits contained in the message body B. The truncated keystream block Z1-Trunc is output from duplex object 204.

Thereafter, the truncated keystream block Z1-Trunc is combined with a message body B (or optionally B∥1, i.e. a concatenation of message body B and a flag 1). The message body B can include, but is not limited to, packet payload. This combining is achieved via XOR operations 232, which produces encrypted data (e.g., ciphertext) C. The XOR operations 232 are performed on a bit-by-bit basis.

The input to duplex object 206 is message body data B (or optionally B∥1). The message body data B can include but is not limited to, packet payload data. The message body data B (or optionally B∥1) is padded in padding functional block 218 to make it a multiple of r (if it is not a multiple of r). The padding of padding functional block 218 is the same as or similar to that of padding functional blocks 214 and 216. Next, the output of padding functional block 218 is then combined with keystream block Z1. This combining can be achieved via XOR operations 230, as shown in FIG. 2. XOR operations are well known in the art, and therefore will not be described in detail here. Still, it should be understood that the XOR operations are performed on a bit-by-bit basis. The results of the XOR operations are then passed to permutation functional block 212. In permutation functional block 212, the unique permutation function ƒ is performed so as to generate a keystream block Z2. The keystream block Z2 is then optionally truncated to a desired length l, as shown by truncate functional block 224. The value of here can be less than r. The truncated keystream block Z2-Trunc is output from duplex object 204. The truncated keystream block Z2-Trunc is then used as an authentication tag T.

In a communications scenario, the encrypted data (e.g., ciphertext) C and the authentication tag T would be transmitted from a source communication device to a destination communication device. The cryptographic key K would not be transmitted since it would be known by both devices.

The advantages of the duplex construction 200 are that: a single cryptographic key is required; encryption and authentication requires only a single pass; intermediate tags are supported thereby; additional authentication data (e.g., packet headers) is supported thereby; it is secure against generic attacks; and the ability to trade off speed and security by adjusting the value of r.

Referring now to FIG. 3, there is provided a schematic illustration that is useful for understanding the unique permutation function ƒ of the present invention which is employed in the sponge and duplex constructions described above in relation to FIGS. 1-2. The permutation function ƒ supports any key size (e.g., 128 bits or 256 bits) and is bijective. Since the permutation function ƒ is bijective, ƒ−−1 (inverse of ƒ) exists by definition. While ƒ1 is not used in practice, it may be helpful for crypto-analysis and verification purposes. Notably, the number of bits that are input and/or output from the permutation function ƒ is also customizable.

The permutation function ƒ comprises a round function ƒround that is iterated R times, depending on the key size. The round function ƒround consists of the following layers: a substitution layer 302; a permutation layer 304; a mixing layer 306; and a round constant addition layer 308. In the substitution layer 302, the bits input thereto are substituted with first substitute bits in accordance with a particular transformation and/or mapping algorithm. For example, input bits 010001 are substituted with bits 1010. The number of bits input/output to/from the substitution layer 302 can be the same or different. In the permutation layer 304, the bits input thereto are re-arranged. In the mixing layer 306, at least two outputs of the permutation layer are combined together. In the round constant addition layer 308, a constant is added to the output of the mixing layer. The manners in which the operations of each layer 302-308 are achieved will be discussed in detail below.

Notably, R is an integer which has a value large enough to resist differential attacks, linear attacks and other attacks depending on the cryptographic key size (e.g., R=10 for a 128 bit key or R=16 for a 256 bit key). In this regard, R is a customizable element of the permutation function ƒ. In some scenarios, R is determined by (1) calculating the number of rounds needed for linear and differential crypto-analysis and (2) adding some buffer to increase the security margin.

Referring now to FIG. 4, there is provided an expanded block diagram of the round function ƒround. The substitution layer 302 comprises a plurality of identical substitution boxes (or S-boxes) 4021, 4022, 4023, 4024, . . . , 40231, 40232 which collectively receive N input bits (e.g., 512 input bits) and individually receive X bits of the N input bits (e.g., 16 bits of 512 input bits). The value of N is selected to be large enough to keep a cryptographic key secure. For example, the value of N is selected to be 512 bits for a cryptographic key having a size of 128 bits or 256 bits.

The purpose of the S-boxes is to perform substitution so as to obscure the relationship between the cryptographic key and encrypted data (e.g., ciphertext). S-boxes are well known in the art, and therefore will not be described in detail herein. Any known or to be known S-box can be used herein without limitation provided that the following properties are satisfied thereby.

(1) The S-boxes have small differential probabilities.

(2) The S-boxes have small linear approximation biases.

(3) The S-boxes have a customizable number of input bits X.

(4) The S-boxes have customizable mapping functions.

For example, each S-box 4021, 4022, 4023, 4024, . . . , 40231, 40232 comprises an X-bit-to-X-bit S-box or an X-bit-by-Y-bit S-box, where X is a customizable integer and Y is a customizable integer different from X. The S-boxes can be implemented as look-up tables or in hardware using logical gates (e.g., XOR gates and AND gates). The look-up tables can be fixed or dynamically generated using the cryptographic key.

In some scenarios, each S-box comprises a bijective 16-bit-to-16-bit S-box. An exemplary architecture for such an S-box is described in Appendix C of a document entitled “Large Substitution Boxes with Efficient Combinational Implementations” which was written by Wood and published in August 2013. This S-box is based on a multiplicative inversion in GF(216)/<p(x)>, where p(x)=x16+x5+x3+x+1. An input to the S-box is represented as a 16-bit column vector x=(x15 x14 . . . x1 x0)T, x15 is the most significant bit. Using this notation, the forward S-box function is defined by the following mathematical equation.

\(Y = {{S(X)} = \left\lbrack {{\begin{pmatrix}
0 & 0 & 1 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 1 & 1 & 1 & 1 & 1 & 0 \\
1 & 1 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 1 & 1 & 0 & 1 & 0 & 1 & 0 \\
1 & 1 & 0 & 0 & 1 & 0 & 1 & 1 & 0 & 1 & 0 & 1 & 0 & 0 & 1 & 1 \\
1 & 1 & 1 & 0 & 0 & 0 & 1 & 0 & 0 & 1 & 1 & 0 & 0 & 0 & 0 & 0 \\
1 & 1 & 0 & 0 & 0 & 1 & 1 & 0 & 0 & 1 & 1 & 1 & 1 & 0 & 1 & 1 \\
0 & 1 & 0 & 0 & 0 & 0 & 1 & 1 & 0 & 1 & 1 & 1 & 1 & 1 & 0 & 1 \\
0 & 0 & 1 & 0 & 1 & 0 & 1 & 0 & 1 & 1 & 0 & 0 & 1 & 1 & 0 & 0 \\
1 & 0 & 1 & 1 & 1 & 0 & 1 & 1 & 0 & 0 & 0 & 1 & 0 & 1 & 1 & 1 \\
0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 1 & 1 & 1 & 0 & 1 \\
1 & 0 & 1 & 1 & 0 & 0 & 0 & 1 & 0 & 0 & 1 & 0 & 1 & 0 & 0 & 0 \\
1 & 0 & 1 & 0 & 0 & 1 & 1 & 1 & 0 & 0 & 1 & 1 & 0 & 1 & 0 & 0 \\
1 & 0 & 1 & 1 & 1 & 0 & 1 & 1 & 1 & 1 & 0 & 1 & 1 & 0 & 0 & 1 \\
1 & 0 & 1 & 0 & 0 & 1 & 0 & 1 & 1 & 0 & 0 & 1 & 0 & 0 & 0 & 1 \\
0 & 1 & 0 & 0 & 0 & 1 & 1 & 1 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \\
1 & 0 & 0 & 0 & 1 & 1 & 0 & 1 & 0 & 1 & 1 & 1 & 1 & 0 & 0 & 0 \\
1 & 1 & 0 & 1 & 0 & 1 & 1 & 0 & 1 & 0 & 0 & 1 & 1 & 0 & 0 & 0
\end{pmatrix}\begin{pmatrix}
x_{15} \\
x_{14} \\
x_{13} \\
x_{12} \\
x_{11} \\
x_{10} \\
x_{9} \\
x_{8} \\
x_{7} \\
x_{6} \\
x_{5} \\
x_{4} \\
x_{3} \\
x_{2} \\
x_{1} \\
x_{0}
\end{pmatrix}^{- 1}} \oplus \begin{pmatrix}
0 \\
1 \\
0 \\
0 \\
0 \\
1 \\
0 \\
1 \\
1 \\
0 \\
1 \\
1 \\
0 \\
1 \\
1 \\
1
\end{pmatrix}} \right\rbrack}\)

The inverse of the S-box function is defined by the following mathematical equation.

\(X = {{S^{- 1}(Y)} = \left\lbrack {\begin{pmatrix}
0 & 1 & 0 & 1 & 0 & 1 & 1 & 1 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 1 \\
1 & 1 & 0 & 1 & 0 & 0 & 1 & 0 & 1 & 0 & 1 & 1 & 1 & 1 & 0 & 1 \\
1 & 0 & 1 & 1 & 1 & 1 & 0 & 1 & 0 & 1 & 1 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 1 & 1 & 1 & 0 & 1 & 0 & 1 & 1 & 1 & 0 & 1 & 0 \\
1 & 1 & 1 & 1 & 1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 & 0 & 1 & 0 & 0 & 0 & 0 & 1 & 1 & 1 & 1 & 1 & 1 \\
1 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 & 0 & 1 & 0 & 1 & 1 \\
0 & 0 & 1 & 0 & 1 & 1 & 1 & 0 & 0 & 1 & 0 & 1 & 1 & 1 & 1 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 & 0 \\
1 & 1 & 1 & 0 & 0 & 1 & 1 & 1 & 1 & 0 & 1 & 1 & 1 & 0 & 0 & 0 \\
0 & 1 & 1 & 0 & 1 & 1 & 1 & 1 & 0 & 0 & 1 & 0 & 1 & 1 & 1 & 1 \\
1 & 0 & 0 & 1 & 1 & 0 & 0 & 0 & 1 & 0 & 0 & 1 & 1 & 0 & 1 & 1 \\
1 & 0 & 0 & 0 & 0 & 1 & 0 & 1 & 1 & 1 & 0 & 0 & 1 & 0 & 1 & 0 \\
1 & 0 & 0 & 0 & 0 & 1 & 1 & 1 & 1 & 1 & 0 & 1 & 1 & 1 & 1 & 1 \\
1 & 1 & 1 & 0 & 0 & 1 & 1 & 0 & 1 & 0 & 0 & 1 & 1 & 1 & 1 & 1 \\
0 & 1 & 0 & 0 & 1 & 0 & 1 & 0 & 1 & 0 & 0 & 1 & 0 & 0 & 0 & 1
\end{pmatrix}\begin{pmatrix}
y_{15} \\
{y_{14} \oplus 1} \\
y_{13} \\
y_{12} \\
y_{11} \\
{y_{10} \oplus 1} \\
y_{9} \\
{y_{8} \oplus 1} \\
{y_{7} \oplus 1} \\
y_{6} \\
{y_{5} \oplus 1} \\
{y_{4} \oplus 1} \\
y_{3} \\
{y_{2} \oplus 1} \\
{y_{1} \oplus 1} \\
{y_{0} \oplus 1}
\end{pmatrix}} \right\rbrack^{- 1}}\)

The above-described S-box can be implemented in hardware using 1238 XOR gates and 144 AND gates.

The permutation layer 304 comprises a bitwise permutation function 404. The purpose of the bitwise permutation function 404 is to permute or change a bit position of each bit 4101, 4102, 4103, 4104, . . . , 41031, 41032 input thereto relative to all other bits input thereto. Bitwise permutation functions are well known in the art, and therefore will not be described in detail herein. Any known or to be known bitwise permutation function can be used herein without limitation provided that the following properties are satisfied thereby.

(1) Each bit 4101, 4102, 4103, 4104, . . . , 41031, 41032 permutes to an output bit position different from its input bit position.

(2) All outputs of a given S-box go to X different mixers.

(3) The permutation period of the permutation function ƒ exceeds the number of rounds R.

For example, the bitwise permutation function includes a linear permutation function, an affine permutation function, or a random permutation function.

In some scenarios, the bitwise permutation function 404 comprises an affine function defined by the following mathematical equation.

π(x)=ax+β(mod 512)

where π(x) represents the output bit position, a is an integer constant (e.g., 31), x represents the input bit position and β is an integer constant (e.g., 15).

The mixing layer 306 comprises a mixing function that is implemented via a plurality of mixers 4061, 4062, . . . , 41016. In the scenario shown in FIG. 4, one mixer is provided for every two S-boxes. The present invention is not limited in this regard. The particular number of S-boxes per mixer is customizable. Also, the mixing function is a customizable element of the present invention. The purpose of the mixing function is to provide local diffusion (i.e., across two words) and increase the linear and differential branch numbers of a round from two to three. In this regard, mixers based on matrix multiplication in Galois Field GF(2M) may be employed because they satisfy all of the following constraints: the matrix is invertible in GF(216)/<p(x)>; the matrix has a differential and linear branch number equal to three; and the transformation is efficiently implementable in hardware.

In some scenarios, operations performed by each mixer 4061, 4062, . . . , 41016 is defined by the following mathematical equation.

p(x)=x16+x5+x3+x2+1

The mixer takes in two words W1 and W2 as input and produces outputs W′1 and W′2 as follows.

\(\begin{pmatrix}
W_{1}^{\prime} \\
W_{2}^{\prime}
\end{pmatrix} = {\begin{pmatrix}
1 & x \\
x & {x + 1}
\end{pmatrix}\begin{pmatrix}
W_{1} \\
W_{2}
\end{pmatrix}}\)

The mixer is implementable in hardware. An exemplary hardware implementation of the mixer is provided in FIG. 5. As shown in FIG. 5, the mixer comprises XOR gates 502, 506, 510 and Galois field multipliers 504, 508. The Galois field multipliers 504, 508 perform multiplication by x in Galois field GF(2X).

The round constant addition layer 308 comprises a plurality of addition operations represented by blocks 4081, 4082, 4083, 4084, . . . , 40831, 40832. The purpose of the addition operations is to add a constant N bit value to the state using bitwise XOR in order to disrupt symmetry and prevent slide attacks. Notably, the round constant must be fixed random N-bit values. Each round i must use a different round constant. The round constant is customizable, and should be unique for each round to prevent against slide attacks and be random, pseudorandom or highly asymmetric to reduce symmetry in the state.

In some scenarios, the round constant RCi for round i is given by the following mathematical equation.

RCi=SHA3−N(ASCII(i))

where ASCII(i) is a function that provides a one or two byte ASCII representation of round i and SHA3-512 is the SHA-3 hash function that outputs an N (e.g., 512) bit message digest. The following TABLE 1 provides the values of the round constant RCi up to i=16.

Notably, the present invention is suitable for implementation on Field Programmable Gate Arrays (“FPGAs”). Serial and fully parallel implementations can be used to meet area or performance constraints. The S-boxes may be implemented using composite field techniques and pipelined for higher performance. Also, the present invention can be integrated into Single Chip Crypto (“SCC”) systems.

Furthermore, the present invention anticipates future security requirements. Post Quantum Security (“PQS”) will become a requirement for radio product customers, as well as provable computational security and quantified theoretical security metrics and analysis processes. The present invention provides a security means that satisfies all of these requirements.

As evident from the above discussion, the present algorithm is highly customizable within a security margin. This customizability is useful in cases where different users want unique, proprietary algorithms. The following features of the present invention are customizable: (1) the state initialization; (2) the number of rounds R; (3) the permutation function ƒ; (4) the number of bits N input into the round function; (5) the type, number, parameters and mapping function of the S-boxes; (6) the bitwise permutation function; (7) the mixing function; and (8) the round constants.

Referring now to FIG. 6, there is provided a flow diagram of an exemplary method 600 for generating encrypted data (e.g., ciphertext) that is useful for understanding the present invention. Method 600 begins with step 602 and continues with optional step 604. In optional step 604, a cryptographic key is concatenated with a flag value. Next in step 606, the cryptographic key is combined with state initialization bits to generate the first combination bits. A multi-bit value for the state initialization bits may be selected such that it is unique for a given application.

The first combination bits are then used to produce a first keystream, as shown by step 608. The first keystream may optionally be truncated to a desired length, as shown by step 610. The first keystream is produced using a permutation function ƒ. The permutation function ƒ is performed using the first combination bits as inputs thereof. The permutation function ƒ comprises a round function ƒround that is iterated R times. The round function ƒround consists of (1) a substitution layer in which the first combination bits are substituted with substitute bits, (2) a permutation layer in which the substitute bits are re-arranged, (3) a mixing layer in which at least two outputs of the permutation layer are combined together, and (4) an addition layer in which a constant is added to the output of the mixing layer.

After completing optional step 610, method 600 continues with another optional step 612. Step 612 involves padding the first data to make a total number of bits contained therein a multiple of the total number of state initialization bits prior to being encrypted. The first data is then encrypted using the first keystream, as shown by step 614. In this regard, the first data may be combined with the first keystream using modular arithmetic (e.g., modulo 2 addition). The first data comprises, but is not limited to, authentication data and/or message body data.

If a sponge framework is employed [616: YES], then steps 618-620 are performed. Step 618 involves producing a second keystream by performing the permutation function ƒ using the first keystream as inputs thereto. Step 620 involves using the second keystream to encrypt the second data so as to produce the second encrypted data (e.g., ciphertext). Upon completing step 620, method 600 ends or other processing is performed (e.g., repeat steps 618-620 for a next block of message data), as shown by step 628.

If a duplex framework is employed [616: NO], then steps 622-626 are performed. Prior to discussing steps 622-626, it should be understood that in the duplex context the first encrypted data (e.g., ciphertext) is produced in previous step 614 by: combining the first keystream with authentication data to generate the second combination bits; producing a second keystream by performing the permutation function ƒ using the second combination bits as inputs thereto; and combining the second keystream with the message body data so as to produce the first encrypted data (e.g., ciphertext). The second keystream is also used in step 622 to produce the third combination bits. The third combination bits are input into the permutation function ƒ, as shown by step 624. As a result of performing the permutation function ƒ, a third keystream is produced. At least a portion of the third keystream is used as an authentication tag.

All of the apparatus, methods and algorithms disclosed and claimed herein can be made and executed without undue experimentation in light of the present disclosure. While the invention has been described in terms of preferred embodiments, it will be apparent to those of skill in the art that variations may be applied to the apparatus, methods and sequence of steps of the method without departing from the concept, spirit and scope of the invention. More specifically, it will be apparent that certain components may be added to, combined with, or substituted for the components described herein while the same or similar results would be achieved. All such similar substitutes and modifications apparent to those skilled in the art are deemed to be within the spirit, scope and concept of the invention as defined.

