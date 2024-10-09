# DESCRIPTION

The present application relates to a method for assessing the efficacy of a disease-modifying antirheumatic drug (DMARD) for use in the treatment of an inflammatory condition. The application also relates to a method for predicting which rheumatoid arthritis pathotype a patient having, suspected of having, or at risk of developing rheumatoid arthritis will develop. The application also relates to a method of predicting whether a patient having, suspected of having, or at risk of developing an inflammatory condition will respond to treatment with a DMARD.

It is widely believed that a precision medicines approach is likely to be more effective in the treatment of patients with chronic inflammatory disorders, including those with rheumatoid arthritis (RA), than the current process where patients are treated in a prescriptive manner using a one size fits all approach. Unfortunately, the lack of robust biomarkers to determine treatment responsiveness in many chronic inflammatory conditions, including rheumatoid arthritis, has hindered the development of this approach in clinical settings.

Results described herein demonstrate that plasma lipid mediator concentrations prior to the initiation of treatment are different in patients that respond to DMARDs when compared with those that do not. Using machine learning methodologies, the inventors found that the concentrations of a group of mediators known as specialized pro-resolving mediators (SPMs) were predictive of treatment responsiveness in two RA cohorts, with prediction accuracy for response to treatment of up to ˜95%. Furthermore, plasma SPM concentrations prior to DMARD treatment initiation were also found to reflect the distinct joint disease pathotypes. Of note, while the patients enrolled in this study were DMARD naïve, most of the patients in both cohorts were on a wide range of other medications for a number of co-morbidities. Therefore, the identification of a specific lipid mediator signature that is predictive of DMARD responsiveness suggest that changes in these lipid mediators are specific for this group of therapeutics. Given that SPM regulate host innate and adaptive immune responses and that SPM production is reflective of leukocyte activation status (Dalli, J. & Serhan, C. N. “Specific lipid mediator signatures of human phagocytes: microparticles stimulate macrophage efferocytosis and pro-resolving mediators.” Blood 120, e60-72 (2012), Gao, Y., et al. “Female-Specific Downregulation of Tissue Polymorphonuclear Neutrophils Drives Impaired Regulatory T Cell and Amplified Effector T Cell Responses in Autoimmune Dry Eye Disease.” J Immunol 195, 3086-3099 (2015), and Serhan, C. N. & Levy, B. D. “Resolvins in inflammation: emergence of the pro-resolving superfamily of mediators.” J Clin Invest 128, 2657-2669 (2018), the contents of all of which are incorporated herein by reference), the present findings indicate that peripheral blood SPM concentrations may be used as functional biomarkers for patient stratification and predicting treatment responsiveness to DMARDs.

The biosynthesis of SPM involves the stereoselective conversion of essential fatty acids by distinct enzymes, with the successful formation of the bioactive product relying on the expression and activity of the enzyme as well as their appropriate subcellular localization. Chiral chromatographic analysis of plasma 6-months post treatment demonstrated a predominance of the S-isomers of the monohydroxylated fatty acids. While this observation does not exclude the contribution of enzymes such as cytochrome P450 enzymes in the formation of the monohydroxylated fatty acids measured, it suggests that ALOX activity is sustained in DMARD-non-responders despite peripheral blood SPM concentrations being overall reduced in this patient group. Thus, suggesting that the SPM biosynthetic pathways become uncoupled post DMARD treatment initiation.

## SUMMARY OF THE INVENTION

According to a first aspect, the invention provides a method of assessing the efficacy of a disease-modifying antirheumatic drug (DMARD) for use in the treatment of an inflammatory condition in a patient, which comprises measuring the levels of at least one specialized pro-resolving mediator (SPM) in samples obtained from the patient before and after administration of the DMARD, wherein an increase in the level of the at least one SPM after administration of the DMARD is indicative of efficacy of the DMARD.

According to a second aspect, the invention provides a method for predicting which rheumatoid arthritis pathotype a patient having, suspected of having, or at risk of developing rheumatoid arthritis will develop comprising measuring the level of at least one specialized pro-resolving mediator (SPM) in a disease-modifying antirheumatic drug (DMARD) naïve patient sample and classifying the rheumatoid arthritis pathotype a patient will develop as Lympho-myeloid, Diffuse-myeloid and Pauci-immune-fibroid.

According to a third aspect, the invention provides a method for predicting whether a patient having, suspected of having, or at risk of developing an inflammatory condition will respond to treatment with a disease-modifying antirheumatic drug (DMARD) comprising measuring the level of at least one specialized pro-resolving mediator (SPM) in a DMARD naïve patient sample and classifying the patient as a predicted DMARD responder or a predicted DMARD non-responder.

## DETAILED DESCRIPTION OF THE INVENTION

According to a first aspect, the invention provides a method of assessing the efficacy of a disease-modifying antirheumatic drug (DMARD) for use in the treatment of an inflammatory condition in a patient, which comprises measuring the levels of at least one specialized pro-resolving mediator (SPM) in samples obtained from the patient before and after administration of the DMARD, wherein an increase in the level of the at least one SPM after administration of the DMARD is indicative of efficacy of the DMARD.

Patients and Diseases

As used herein, the terms “subject” and “patient” are used interchangeably to refer to a human or a non-human mammal. The subject may be a companion non-human mammal (i.e. a pet, such as a dog, a cat, a guinea pig, or a non-human primate, such as a monkey or a chimpanzee), an agricultural farm animal mammal, e.g. an ungulate mammal (such as a horse, a cow, a pig, or a goat) or a laboratory non-human mammal (e.g., a mouse and a rat). The invention may find greatest application in connection with the treatment of human subjects.

The inflammatory condition may be rheumatoid arthritis, arthritis associated with ankylosing spondylitis, cardiovascular disease (CVD), periodontal disease, asthma, diabetes and inflammatory bowel disease (IBD), ulcerative colitis, Crohn disease or a neurological disorder such as Alzheimer's disease. The inflammatory condition may be cardiovascular disease (CVD) or rheumatoid arthritis. Preferably, the inflammatory condition is rheumatoid arthritis. In any of the embodiments herein, the subject may be a human. The subject may be a subject diagnosed with an inflammatory condition, for example Rheumatoid Arthritis. The subject may be a subject undergoing treatment for an inflammatory condition, for example Rheumatoid Arthritis.

The method advantageously allows personalisation of medicine. Because each patient will have differences in the genetics and their environment when compared to any other patient, they may respond differently to drugs, including DMARDs. If a patient is not responding to a DMARD then an alternative therapy may be needed. The method of the invention therefore allows better clinical decision making for an individual patient. The patient may be described as an “individual patent” accordingly.

Disease Modifying Anti-Rheumatic Drugs (DMARDs)

Disease modifying anti-rheumatic drugs (DMARDs) are a category of drugs. The members of this category of drugs are known to the person skilled in the art. The skilled person also knows what drugs are not DMARDs, for example, statins are not DMARDs. Statins include atorvastatin, cerivastatin, fluvastatin, lovastatin, mevastatin, pitavastatin, pravastatin, rosuvastatin and simvastatin, none of which are DMARDs. DMARDs include both biological (or “biologic”) and non-biological (or “non-biologic”) drugs.

Biological DMARDs include etanercept, adalimumab, infliximab, certolizumab pegol, and golimumab, which are all part of a class of drugs called tumor necrosis factor (TNF) inhibitors, and a variety of other agents with different targets, including anakinra, abatacept, rituximab, and tocilizumab.

Non-biological DMARDs include methotrexate, aspirin, hydroxychloroquine and leflunomide. Another common non-biological DMARDs is sulfasalazine. Less frequently used non-biological DMARDs include gold salts, azathioprine, and cyclosporine. The DMARD may therefore be selected from the group consisting of methotrexate, aspirin, hydroxychloroquine, leflunomide, sulfasalazine, gold salts, azathioprine, and cyclosporine. The DMARD may be selected from the group consisting of methotrexate, aspirin, hydroxychloroquine, leflunomide and sulfasalazine. The DMARD may be selected from the group consisting of methotrexate, aspirin, hydroxychloroquine and leflunomide. The DMARD may be methotrexate.

Known details concerning some frequently used non-biological DMARDs are provided below. In each case, a problem with non-biological DMARD treatment may be the need for patient monitoring, toxicity and side effects.

Methotrexate

Methotrexate was originally used as a chemotherapy treatment for cancer. When used in much lower doses for rheumatoid arthritis and other rheumatic diseases, methotrexate works to reduce inflammation and to decrease joint damage. It is taken weekly (on the same day each week) as a pill, liquid, or injection. Methotrexate may be combined with other DMARDs or with a biologic agent if methotrexate alone does not adequately control disease.

Common side effects include upset stomach and mouth sores. Methotrexate can rarely interfere with the bone marrow's production of blood cells. Low blood cell counts can cause fever, infections, swollen lymph nodes, and easy bruisability and bleeding. Liver function problems can occur, even with low doses, and therefore regular blood tests are necessary for anyone taking methotrexate. People using methotrexate should also limit alcohol use because of the increased risk of liver injury with this combination. Rare injury to the lung can occur, and methotrexate should be stopped if the person develops a new cough and shortness of breath. Women should not become pregnant while taking methotrexate.

Proper monitoring is critical to identify drug toxicity in people taking methotrexate. Testing is performed prior to starting treatment to evaluate baseline blood counts and check kidney and liver function. These tests are repeated every 4 to 6 weeks for the first few months then every 8 to 12 weeks thereafter. The dose of methotrexate can be modified if problems are noted. Anyone taking methotrexate should take folic acid (1 mg daily) or folinic acid (5 mg weekly) to reduce the risk of certain side effects, such as upset stomach, mouth sores, low blood cell counts, and abnormal liver function.

Sulfasalazine

Sulfasalazine is used in the treatment of rheumatoid arthritis and of arthritis associated with ankylosing spondylitis and inflammatory bowel disease (ulcerative colitis and Crohn disease). It is not clear how sulfasalazine works. It may be combined with other DMARDs if a person does not respond adequately to one medication. It is taken as a pill two times per day, and it is usually started at a low dose and is increased slowly to minimize side effects.

Side effects of sulfasalazine include changes in blood counts, nausea or vomiting, sensitivity to sunlight, skin rash, and headaches. People who are allergic to sulfonamide medications, such as sulfamethoxazole-trimethoprim (sample brand names: Bactrim, Septra), may have a cross-reaction to sulfasalazine and should therefore not take it. Periodic blood tests are recommended to monitor the blood count on a regular basis.

Sulfasalazine is a yellow-orange colour; people who take it may notice that their urine, tears, and sweat develop an orange tinge, which can stain clothing and contact lenses. Its important to drink plenty of fluids while taking sulfasalazine and to avoid taking it on an empty stomach or with antacids.

Hydroxychloroquine

Hydroxychloroquine, originally developed as a treatment for malaria, was later found to improve symptoms of arthritis. It can be used early in the course of rheumatoid arthritis and is often used in combination with other DMARDs. It is also very frequently used for treatment of systemic lupus erythematosus. It can be combined with steroid medications to reduce the amount of steroid needed. It is usually taken in pill form once or twice per day.

Taking a high dose of hydroxychloroquine for prolonged periods of time may increase the risk of damage to the retina of the eye, although high doses are not usually required for treatment of rheumatic conditions. An eye examination by an ophthalmologist is recommended before starting treatment and periodically thereafter. It is common to have an eye check-up done once each year.

Leflunomide

Leflunomide inhibits production of inflammatory cells to reduce inflammation. It is often used alone but may be used in combination with methotrexate for people who have not responded adequately to methotrexate alone or together with a biologic agent. It is taken by mouth once daily.

Side effects include rash, temporary hair loss, abnormal liver function tests, nausea, diarrhea, weight loss, abdominal pain, and neuropathy (nerve damage). High blood pressure can occur in up to 10 percent of people. Testing for prior exposure to hepatitis and regular blood testing while on therapy are needed to monitor for liver damage and other toxicities. Women should not become pregnant while taking leflunomide or while it is still detectable in the body.

Azathioprine

Azathioprine has been used in the treatment of cancer, rheumatoid arthritis, lupus, and a variety of other inflammatory illnesses since the 1950s. It has also been used in organ transplantation to prevent rejection of the transplanted organ.

The most common side effects of azathioprine include nausea, vomiting, decreased appetite, liver function abnormalities, low white blood cell counts, and infection. It is usually taken by mouth once daily. Regular blood testing is recommended during treatment with azathioprine.

Typically, the invention relates to non-biological DMARDs, for example the invention may be defined as a method of assessing the efficacy of a non-biological DMARD. An advantage of the invention is that it may inform and improve clinical decision making, in particular, it may provide a more rapid determination that a non-biological DMARD is not effective and therefore permit an early and efficient change of treatment to a different non-biological DMARD or to a biological DMARD.

Specialized Pro-Resolving Mediators (SPMs)

SPM are molecules produced by enzymes primarily carried in leukocytes for the essential fatty acids arachidonic acids (AA), eicosapentaenoic acid (EPA), n-3 docosapentaenoic acid (n-3 DPA) and docosahexaenoic acids (DHA). These molecules are central in the regulation of innate and adaptive immune responses during inflammation to facilitate its termination. SPM may also be referred to as “lipid mediators”.

Without being bound by theory, an increase in the levels of at least one SPM are thought to indicate efficacy because SPM are protective mediators.

As used herein, the terms “level” and “levels” are used interchangeably with the terms “concentration” and “concentrations”.

The SPM may be a DHA metabolite, n-3 DPA metabolite, AA metabolite and/or an EPA metabolite. The method may comprise measuring the levels of at least one DHA metabolite, at least one n-3 DPA metabolite, at least one AA metabolite and/or at least one EPA metabolite.

The SPM may be a DHA metabolite and/or an EPA metabolite. The method may comprise measuring the levels of at least one DHA metabolite, and/or at least one EPA metabolite.

The invention may alternatively be characterised as comprising measuring the levels of at least one DHA metabolite, at least one n-3 DPA metabolite, at least one AA metabolite and/or at least one EPA metabolite, without reference to the term plasma specialized pro-resolving mediator (SPM). Likewise, the invention may be characterised as comprising measuring the levels of at least one DHA metabolite and/or at least one EPA metabolite, without reference to the term plasma specialized pro-resolving mediator (SPM). Similarly, the invention may be characterised by reference to any one or more of the specific EPA, n-3 DPA, AA and/or DHA metabolites defined below.

EPA Metabolites

EPA metabolites include the “E-series resolvins” and EPA-derived monohydroxylated fatty acids.

EPA metabolites are listed in Table 1 below:

n-3 DPA Metabolites

These include the 13-series resolvins—RvT1, RvT2, RvT3 and RvT4, D-series resolvins-RvD1n-3 DPA, RvD2n-3 DPA and RvD5n-3 DPA, Protectins PD1n-3 DPA PD2n-3 DPA and 10S, 17S-diHDPA and Maresins—MaR1n-3 DPA MaR2n-3 DPA and 7S, 14S-diHDPA together with the respective monohydroxylated fatty acids.

n-3 DPA metabolites are listed in Table 2 below:

AA Metabolites

AA metabolites include Lipoxins—LXA4, LXB4, 5S, 15S-diHETE, 15R-LXA4 and 15R-LXB4 Leukotrienes: LTB4, 5S, 12S-diHETE, 12-epi-LTB4, 6-trans, 12-epi-LTB4 and 20-OH-LTB4, LTC4, LTD4 and LTE4 and Prostanoids: PGD2, PGE2 and PGF2□ TxB2

AA metabolites are listed in Table 3 below:

DHA Metabolites

DHA metabolites include the “D-series resolvins—RvD1, RvD2, RvD3, RvD4, RvD5, RvD6, 17R-RvD1 and 17R-RvD3, Protectins—PD1, 10S,17S-diHDHA, 17R-PD1 and 22-OH-PD1, PCTR1, PCTR2 and PCTR3 and Maresins—MaR1, 7S, 14S-diHDHA, MaR2, 4S, 14S-diHDHA and 22-OH-MaR1, MCTR1, MCTR2 and MCTR3”.

DHA metabolites are listed in Table 4 below:

Measuring SPM

The method may comprise measuring a D-series resolvin and/or an E-series resolvin. The D-series reslovin may be selected from the group consisting of RvD1, RvD2, RvD3, RvD4, RvD5, RvD6, 17R-RvD1 and 17R-RvD3. Any combination of the D-series resolvins may be measured. The E-series resolving may be selected from the group consisting of RvE1, RvE2 and RvE3. Any combination of the E-series resolvins may be measured.

The method may comprise measuring the levels of RvT3; RvT4; RvD1; MaR1n-3 DPA; RvT4; RvE2;14-oxo-MaR1; 17R-RvD3; 15R-LXB4; RvD3; RvD4; TxB2; LTB4; 20-COOH-LTB4; LTE4; 10S, 17S,diHDHA (PDX); 17R-PD1; 15R-LXA4; PGE2; PGD2; MaR1n-3 DPA, 10S, 17S-diHDPA; 4S, 14S-diHDHA; 5S, 12S-diHETE; and/or 5S, 15S-diHETE.

The method may comprise measuring the levels of RvD4, 10S,17S-diHDPA, 15R-LXA4 and/or MaR1n-3 DPA. The method may comprise measuring the levels of RvD4, 5S,12S-diHETE, 4S, 14S-diHDHA, 10S,17S-diHDPA, 15R-LXA4 and/or MaR1n-3 DPA. The method may comprise measuring the levels of RvD4, 10S,17S-diHDPA, 15R-LXA4 and MaR1n-3 DPA. The method may comprise measuring the levels of RvD4, 5S,12S-diHETE, 4S, 14S-diHDHA, 10S,17S-diHDPA, 15R-LXA4 and MaR1n-3 DPA.

The method may comprise measuring the levels of RvD4, 10S,17S-diHDPA, 15R-LXA4 and/or 5S,12S-diHETE. The method may comprise measuring the levels of RvD4, 10S,17S-diHDPA, 15R-LXA4 and 5S,12S-diHETE.

The method may comprise measuring the levels of at least one SPM. The method may comprise measuring the levels of at least two, at least three or at least four SPM. Accordingly, the at least one SPM may be at least four SPM. The at least four SPM may comprise RvD4, 10S,17S-diHDPA, 15R-LXA4 and MaR1n-3 DPA. The at least two or at least three SPM may comprise any two or three SPM selected from RvD4, 5S,12S-diHETE, 4S, 14S-diHDHA, 10S,17S-diHDPA, 15R-LXA4 and MaR1n-3 DPA The method may comprise measuring the levels of at least six SPM. Accordingly, the at least one SPM may be at least six SPM. The at least six SPM may comprise RvD4, 5S,12S-diHETE, 4S, 14S-diHDHA, 10S,17S-diHDPA, 15R-LXA4 and MaR1n-3 DPA. The method may comprise measuring the levels of at least five SPM. The at least five SPM may comprise any five selected from RvD4, 5S,12S-diHETE, 4S, 14S-diHDHA, 10S,17S-diHDPA, 15R-LXA4 and MaR1n-3 DPA.

The method may comprise measuring the levels of RvT3; RvT4; RvD1; MaR1n-3 DPA; RvT4; 14-oxo-MaR1; 17R-RvD3; 15-epi-LXB4; RvD3; RvD4; TxB2; LTB4; 20-COOH-LTB4; LTE4; 10S, 17S,diHDHA (PDX); 17R-PD1; 15-epiLXA4; PGE2; PGD2; 10S, 17S-diHDPA; and/or 5S, 15S-diHETE.

The method may comprise measuring the levels of RvT3; RvT4; RvD1; MaR1n-3 DPA; RvT4; RvE2; 14-oxo-MaR1; 17R-RvD3; 15-epi-LXB4; RvD3; RvD4; TxB2; LTB4; 20-COOH-LTB4; LTE4; 10S, 17S,diHDHA (PDX); 17R-PD1; 15-epiLXA4; PGE2; PGD2; 10S, 17S-diHDPA; and/or 5S, 15S-diHETE.

The method may comprise measuring the levels of 14-oxo-MaR1, RvD4, RvT3 and/or RvE2. The method may comprise measuring the levels of 14-oxo-MaR1 and RvD4. The method may comprise measuring the levels of 14-oxo-MaR1, RvD4, RvT3 and RvE2.

The method may comprise measuring the levels of at least one SPM. The method may comprise measuring the levels of at least four SPM. Accordingly, the at least one SPM may be at least four SPM. The at least four SPM may comprise 14-oxo-MaR1, RvD4, RvT3 and RvE2.

The method may comprise measuring the levels of at least one SPM, for example at least two, at least three, at least four, at least five or at least six SPM selected from the top 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53 or 54 SPMs shown in FIG. 1 F.

The method may comprise measuring the levels of SPM that are involved in coordinating the host response during ongoing inflammation. The method may therefore include measuring levels of PCTR2, RvD2 and/or RvD3.

The method may comprise measuring the levels of SPM that are mediators linked with pain modulation. The method may therefore include measuring levels of RvE1 and/or RvE2.

The method may comprise measuring the levels of SPM that are mediators linked with pain modulation and SPM that are involved in coordinating the host response during ongoing inflammation. The method may therefore include measuring levels of PCTR2, RvD2, RvD3, RvE1 and/or RvE2. Any combination of these SPM mediators may be measured. Any two or any three or any four of these SPM mediators may be measured. All five of these SPM mediators may be measured.

DMARD Responders and Non-Responders

The method may further comprise classifying the patient as a DMARD responder or a DMARD non-responder based on the efficacy of the DMARD. Where an increase in the level of the at least one SPM after administration of the DMARD indicates that the DMARD is effective, the patient will be classified as a DMARD responder. Conversely, where no increase in the level of the at least one SPM after administration of the DMARD is detected, the patient will be classified as a DMARD responder.

As used herein, the term “DMARD responder” typically refers to a non-biological DMARD responder; that is a patient who is responding or will respond to treatment with a non-biological DMARD. Likewise, the term “DMARD non-responder” typically refers to a non-biological DMARD non-responder; that is a patient who is not responding or will not respond to treatment with a non-biological DMARD. Both DMARD responders and DMARD non-responders may respond to biological DMARDs.

A responder is clinically defined as a patient who after treatment have a low disease activity score-28 (DAS28)<3.2

The method may comprise measuring the levels of ALOX5 and/or ALOX15-derived mediators from both the n-3 DPA and DHA metabolomes. ALOX5 and ALOX15-derived mediators from both the n-3 DPA and DHA metabolomes include RvD1, RvD4, RvD1n-3 DPA and RvD2n-3 DPA ALOX5 and ALOX15-derived mediators from both the n-3 DPA and DHA metabolomes may be reduced in non-responders.

The method may comprise measuring the levels of ALOX5 derived products of EPA. ALOX5-derived mediators from the EPA metabolomes include RvE1 and RvE2. ALOX5—derived mediators from the EPA metabolome may be reduced in non-responders.

The method may comprise measuring the levels of ALOX5 derived products of AA. ALOX5 derived products of AA include the leukocyte chemoattractant LTB4 and the ionotropic cysteinyl leukotrienes. AA-derived ALOX5 products may be increased in plasma from non-responders when compared with responders.

Samples

Each sample may be defined as a “patient sample” or a “biological sample”.

Samples are typically obtained prior to the methods of the invention being performed. The methods of the invention are in vitro methods accordingly. In some alternative embodiments, the method may further comprise a step or steps of sample collection.

The sample may be a plasma or whole blood sample. Preferably, the sample is a plasma sample. When the sample is a plasma sample, the SPM may be described as a plasma specialized pro-resolving mediator (SPM).

The sample obtained before treatment with a DMARD may have been obtained at any within 24 h prior to commencement of treatment.

The sample obtained after treatment with a DMARD may have been obtained around six months after commencement of treatment with the DMARD. However, changes may even be observed as soon as 1 month after treatment. The sample after treatment with a DMARD may have been obtained around 1 month, around 2 months, around 3 months, around 4 months or around 5 months after commencement of treatment with the DMARD.

The samples may be treated immediately after collection with an anticoagulant such, for example, as heparin to prevent clotting.

If the samples—for example human plasma samples—are required to be stored prior to analysis, they may be placed in an organic solvent and stored at a temperature of −75° C. or below, e.g., −80° C. Suitably, the organic solvent may comprise or consist of methanol. Although lipid mediators have been found to be unstable in frozen samples during the term-long-term storage, with the levels of some of the mediators being significantly (>50%) reduced following three-month storage, it has been surprisingly found that by using methanol, and optionally other organic solvents, the stability of these molecules may be improved when they are stored for an extended period at temperatures of −75° C. and below. Suitably, the samples may be stored at temperatures of about −80° C. or less. The samples may be stored for at least about 1 month, and in some embodiments at least about 3 months, up to about 9 months or longer.

Deuterium labelled standards of the kind described below may be added to the samples prior to freezing.

Measuring SPM Levels

Methods for measuring the levels of SPM in biological samples such as blood and tissue are available to those skilled in the art and need not be described herein in detail. Suitable methods are disclosed, for example, in Yang R, Chiang N, Oh SF and Serhan C N. 2011. “Metabolomics-Lipidomics of Eicosanoids and Docosanoids Generated by Phagocytes”. Curr Protoc Immunol. 95:14.26:14.26.1-14.26.26 and Dalli J and Serhan C N. 2012. “Specific lipid mediator signatures of human phagocytes: microparticles stimulate macrophage efferocytosis and pro-resolving mediators”. Blood. 2012; 120:e60-e72, the contents of both of which are incorporated herein by reference.

Briefly, in some embodiments, the levels of the at least one SPM in the samples may be measured using liquid chromatography tandem mass spectrometry (LC-MS/MS) after extracting the SPMs from the samples.

The SPMs may be extracted from the samples using solid-phase extraction, for instance using C18 columns. Suitable methods are disclosed by Colas R A, Shinohara M, Dalli J, Chiang N and Serhan C N. “Identification and signature profiles for pro-resolving and inflammatory lipid mediators in human tissue”. Am J Physiol Cell Physiol. 2014; 307:C39-54, the contents of which are incorporated herein by reference.

One or more internal labelled standards may be added to the samples prior to extraction of the SPMs to facilitate quantitation of the SPM in the samples. Suitable labelled standards are deuterium-labelled 5S-HETE (5S-HETE-da), deuterium-labelled leukotriene B4 (LTB4-d4), deuterium-labelled lipoxin A4 (LXA4-d5), deuterium-labelled resolvin D2 (RvD2-d5) and deuterium-labelled prostaglandin E2 (PGE2-d4).

The identity of a SPM in a sample may be confirmed by matching its retention time (RT) and at least 6 diagnostic ions from its MS-MS spectrum with those of a synthetic or authentic standard for the SPM. Retention times for molecules measured using liquid chromatography are often instrument specific, but in some embodiments for example, the retention times of the above-mentioned 13-series resolvins may be as shown in Table 5 below:

Quantitation may be achieved using linear regression curves that are constructed using a synthetic or authentic standard for the mediator.

LC-MS/MS may be suitable for use in situations where there is access to the equipment required such, for example, in hospital laboratories. However, more conveniently, the levels of the at least one SPM in the samples may be measured using an immunoassay. Immunoassays have the potential to be miniaturised to run on a microfluidics device or test-strip and may be more suited for clinical point-of-care applications. Embodiments of the invention which incorporate an immunoassay may therefore be used in situ by a primary healthcare provider for assistance in prescribing a statin for an individual patient.

The levels of the at least one SPM may be measured using a homogeneous or heterogeneous immunoassay.

Thus, in some embodiments, the levels of the or each SPM may be measured in solution by binding to labelled antibodies that are present in excess, whereby binding alters detectable properties of the label. The amount of a specific SPM present will therefore affect the amount of the label with a particular detectable property. As is well known in the art, the label may comprise a radioactive label, a fluorescent label or an enzyme having a chromogenic or chemiluminescent substrate that is coloured or caused or allowed to fluoresce when acted on by the enzyme.

The antibodies may be polyclonal or monoclonal with specificity for the SPM. In some embodiments, monoclonal antibodies may be used.

Alternatively, a heterogeneous format may be used in which the at least one SPM is captured by surface-bound antibodies for separation and quantification. In some embodiments, a sandwich assay may be used in which a surface-bound SPM is quantified by binding a labelled secondary antibody.

Suitably, the immunoassay may comprise an enzyme immunoassay (EIA) in which the label is an enzyme such, for example, as horseradish peroxidase (HRP). Suitable substrates for HRP are well known in the art and include, for example, ABTS, OPD, AmplexRed, DAB, AEC, TMB, homovanillic acid and luminol. In some embodiments, an ELISA immunoassay may be used; a sandwich ELISA assay may be particularly preferred.

The immunoassay may be competitive or non-competitive. Thus, in some embodiments, the amounts of the at least one SPM may be measured directly by a homogeneous or heterogeneous method, as described above. Alternatively, the SPM in the samples may be sequestered in solution with a known amount of antibody which is present in excess, and the amount of antibody remaining then determined by binding to surface-bound SPM to give an indirect read-out of the amount of SPM in the original sample. In another variant, the at least one SPM may be caused to compete for binding to a surface bound antibody with a known amount of a labelled SPM.

The surface bound antibodies or SPM may be immobilised on any suitable surface of the kind known in the art. For instance, the antibodies or SPM may be immobilised on a surface of a well or plate or on the surface of a plurality of magnetic or non-magnetic beads.

In some embodiments, the immunoassay may be a competitive assay, further comprising a known amount of the SPM, which is the same as the one to be quantitated in the sample, but tagged with a detectable label. The labelled SPM may be affinity-bound to a suitable surface by an antibody to the SPM. Upon adding the sample a proportion of the labelled SPM may be displaced from the surface-bound antibodies, thereby providing a measure of the level of SPM in the sample.

In some embodiments, the immunoassay may comprise surface-bound SPM, which is the same as the SPM that is to be quantitated in the sample, and a known amount of antibodies to the SPM in solution in excess. The sample is first mixed with the antibodies in solution such that a proportion of the antibodies bind with the SPM in the sample. The amount of unbound antibodies remaining can then be measured by binding to the surface-bound SPM.

In some embodiments, the immunoassay may comprise a labelled secondary antibody to the SPM or to a primary antibody to the SPM for quantifying the amount of the SPM bound to surface-bound antibodies or the amount of primary antibody bound to the SPM immobilised on a surface.

Measuring SPM levels may be by equipment for measuring the level of a specific SPM in a sample comprising a sample collection device and an immunoassay. The equipment may further comprise a detector for detecting labelled SPM or labelled antibodies to the SPM in the immunoassay. Suitable labels are mentioned above, but in a preferred embodiment, the label may be an enzyme having a chromogenic or chemiluminescent substrate that is coloured or caused or allowed to fluoresce when acted on by the enzyme.

The immunoassay or equipment may be incorporated into a miniaturised device for measuring the level of at least one SPM in a biological sample. Suitably, the device may comprise a lab-on-a-chip.

Measuring SPM levels may be by a device for measuring the level of at least one SPM in a sample obtained from a patient, the device comprising one or more parts defining an internal channel having an inlet port and a reaction zone, in which a SPM in a sample may be reacted with an immobilised primary antibody for the SPM for capturing the SPM, or a primary antibody for the SPM in excess in solution after mixing with the sample upstream of the reaction zone may be reacted with SPM, which is the same as the one to be measured in the sample, but immobilised on a surface within the reaction zone, for quantifying directly or indirectly the amount of the SPM in the sample.

The captured SPM or primary antibody may then be detected using a secondary antibody to the SPM or primary antibody, which is tagged with an enzyme.

As described above, the enzyme may have a chromogenic or chemiluminescent substrate that is coloured or caused or allowed to fluoresce when acted on by the enzyme. Suitably, the one or more parts of the device defining the channel, at least adjacent the reaction zone, may be transparent to light, at least in a range of wavelengths encompassing the colour or fluorescence of the substrate to allow detection of a reaction between the SPM or primary antibody and the secondary antibody using a suitable detector such, for example, as a photodiode, positioned outside the channel or further channel.

In some embodiments, the device may comprise a plurality of channels, each with its own inlet port, for measuring the levels of a plurality of different SPMs in the sample in parallel. Therefore, each channel may include a different respective immobilised primary antibody or SPM. Suitably, the device may comprise one or more selectively operable valves associated with the one or more inlet ports for controlling the admission of a sequence of different reagents into to the channels such, for example, as the sample, wash solutions, primary antibody, secondary antibody and enzyme substrate.

The device therefore may comprise a microfluidics device. The channel may include a reaction zone. Microfluidics devices are known to those skilled in the art. A review of microfluidic immunoassays or protein diagnostic chip microarrays is provided by Chin et al. 2012. Lab on a Chip. 2012; 12:2118-2134. A microfluidics device suitable for carrying out an ELISA immunoassay at a point-of-care is disclosed by Chan C D, Laksanasopin T, Cheung Y K, Steinmiller D et al. “Microfluidics-based diagnostics of infectious diseases in the developing world”. Nature Medicine. 2011; 17(8):1015-1019, the contents of which are incorporated herein by reference.

Assessing Efficacy

Assessing the efficacy of a DMARD may comprise comparing levels of the at least one SPM in the samples obtained from the patient before and after administration of the DMARD. Where the comparison indicates that the level of the at least one SPM is higher in the sample obtained from the patient after administration of the DMARD than in the sample obtained from the patient before administration of the DMARD then the comparison shows there is an increase in the level of the at least one SPM after administration of the DMARD is indicative of efficacy of the DMARD. It will be appreciated that the converse comparison is equivalent; a decrease in the level of the at least one SPM before administration of the DMARD is indicative of efficacy of the DMARD. Likewise, a decrease in the level of the at least one SPM after administration of the DMARD is indicative of DMARD ineffectiveness. DMARD ineffectiveness may be observed in a patient resistant to DMARD therapy.

An increase is a difference compared to pre-treatment values. The increase may for example be an increase of at least about 5%, at least about 10%, at least about 15%, at least about 20%, at least about 25%, at least about 30%, at least about 35%, at least about 40%, at least about 45%, at least about 50%, at least about 55%, at least about 60%, at least about 65%, at least about 70%, at least about 75%, at least about 80%, at least about 85%, at least about 90%, at least about 95% or at least about 100%. The increase may be an increase of at least about 20%.

Alternatively, an increase may be expressed as a fold change. The skilled person will appreciate that any percentage increase may be converted to a fold change and vice versa.

The terms “indicates” and “indicative” are used because, without being bound by theory, a method may determine that a DMARD is ineffective under particular circumstances, but this is not an absolute determination, for instance a different treatment regimen or an increased dose may yet be effective in some cases. However, the terms may “indicates” and “indicative” be replaced with “determine” and “determines” as appropriate, for instance when a maximum recommended dose of a DMARD is used, the method can determine that the DMARD is ineffective. Any of the above terms may be replaced with the terms “predict” or “predictive”. Where discreet groups are involved, the word “classify” and its variants may be used, such as “wherein an increase in the level of the at least one SPM after administration of the DMARD classifies the DMARD as effective”.

Where multiple SPM are measured, the increase that indicates efficacy of the DMARD may be the same or may be different for each SPM.

Assessing the efficacy of a DMARD may comprise a comparison with a control, such as a control database. A control database may be particularly beneficial when the levels of multiple SPM are be assessed.

The method may therefore comprise a further step of comparing the levels of the at least on SPM in samples obtained from the patient before administration of the DMARD with the levels of the at least on SPM in samples obtained from the patient after administration of the DMARD. Such a comparison may be performed by any method known in the art, including by a statistical method.

The method may comprise a further step of finding a difference between the levels of the at least on SPM in samples obtained from the patient before administration of the DMARD and the levels of the at least on SPM in samples obtained from the patient after administration of the DMARD. This step may be performed by any method known in the art, including by a statistical method. The method may therefore comprise a further step of determining whether the DMARD is effective or ineffective based on the levels of the at least on SPM in samples obtained from the patient before administration of the DMARD and the levels of the at least on SPM in samples obtained from the patient after administration of the DMARD. For instance, the method may comprise determining whether the DMARD is effective or ineffective based on a comparison of and/or finding a difference between the levels of the at least on SPM in samples obtained from the patient before administration of the DMARD and the levels of the at least on SPM in samples obtained from the patient after administration of the DMARD.

The method may comprise a further step of determining the DMARD is ineffective and optionally changing the patient's treatment.

The method may comprise assessing the efficacy of a DMARD using a multivariate analysis. The multivariate analysis may be orthogonal partial least squares-discrimination analysis (oPLS-DA).

oPLS-DA generates a regression model based on concentrations of lipid mediators differently expressed between two groups (Chong, J., Yamamoto, M. & Xia, J. MetaboAnalystR 2.0: “From Raw Spectra to Biological Insights.” Metabolites 9 (2019). oPLS-DA may be performed using the MetaboAnalyst web-based application (https://www.metaboanalyst.ca/faces/ModuleView.xhtml).

The method may comprise assessing the efficacy of a DMARD using a trained machine learning model. Such a machine learning model may be used to predict the response to DMARD treatment based on data such as one or more of: SPM profiles (including individual concentrations for each SPM for each patient), clinical scores and specific SPM families. The data may be separated based on the specific pathotype of the patient.

The machine learning model may be created using various scripts, such as R scripts, to create Support Vector Machine (SVM) models and/or random forest prediction models, for example. The machine learning model may therefore comprise at least one of an SVM model and a random forest prediction model. The skilled person is familiar with SVM models and random forest prediction models, and as such a specific implementation of SVM models and random forest prediction models will now be briefly described.

The SVM models may be created using the known and freely-accessible package ClassyFire developed by the Wishart Research Group (http://classyfire.wishartlab.com/), and described in the publication: Djoumbou Feunang Y, Eisner R, Knox C, Chepelev L, Hastings J, Owen G, Fahy E, Steinbeck C, Subramanian S, Bolton E, Greiner R, and Wishart DS. ClassyFire: Automated Chemical Classification With A Comprehensive, Computable Taxonomy. Journal of Cheminformatics, 2016, 8:61. As the skilled person would understand, ClassyFire is a web-based application for automated structural classification of chemical entities. ClassyFire uses an SVM to create the machine learning models. As would be understood, SVM classifies, makes a regression, and creates a novelty detection for the creation of the model. Several such models may be created until the most accurate model is found. Validation of the models is achieved using a validation cohort to estimate the Matthews Correlation Coefficient (MCC) value and assess the accuracy of the prediction, as would be understood. These SVM models output accuracy percentages and MCC values after validation.

The SVM models are trained based on training data. Such data includes “explanatory” data and “response” data for patients in which the treatment outcome is already knows. The explanatory data comprises all the data that is used to determine why a patent is or isn't a responder. For example, the explanatory data may be lipid mediator profiles for a particular patient, including the individual concentrations of lipid mediators as obtained from plasma. The response data comprises data indicating whether or not the particular patient actually is or isn't a responder. The training data may therefore comprise a tab-delimited table with a training dataset of patients as columns and lipid mediators as rows, and a tab-delimited table with a validation dataset of patients as columns and lipid mediators as rows.

The random forest models may be created using the known package randomForest as described in the publication: A. Liaw and M. Wiener (2002). Classification and Regression by randomForest. R News 2(3), 18-22. As the skilled person would understand, this package creates a random forest model based on classification and regression of random forests. The random forest models may be created using random forests and bootstrapping in order to decorrelate the multiple trees generated on different bootstrapped samples from the training data, and then reduce the variance in the trees by averaging. The use of averaging improves the performance of decision trees and avoids overfitting. The randomForest package creates several trees, each one using different variables to create a best version.

The mtry parameter, which is the number of variables available for splitting at each tree node, can be used to define how many variables the data is split into to create different trees. Specifically in this use, the importance of each lipid mediator in the improvement of the model's accuracy is estimated by defining the lipid mediators to create a loop, monitoring for a change in accuracy of the model, and defining the best mtry based on the lipid mediator's effect on the accuracy of the model. The model may then be re-run based on the defined best mtry value. As for the SVM models, a validation cohort is used to estimate the MCC value. These random forest models output accuracy percentages and MCC values after validation, and may also output one or more plots associated with the performance of the model and the importance of each lipid mediator in the construction of the model.

The random forest models, like the SVM models, are trained using training data. The training data used to train the random forest models may be the same as that used to train the SVM models.

The method may therefore comprise measuring the levels of at least two SPM and determining whether the DMARD is effective, the method comprising inputting the levels of at least two SPM into a trained machine learning algorithm, the trained machine learning algorithm being arranged to:


- - i. Compare the levels of the at least two SPM from the sample
    obtained from the patient before administration of the DMARD with
    the levels of the same at least two SPM in the sample obtained from
    the patient after administration of the DMARD, and
  - ii. Output whether the DMARD is effective or ineffective;  
    optionally wherein the trained machine learning model is a Support
    Vector Machine (SVM) model and/or a random forests model.

The trained machine learning algorithm may be trained based on training data, the training data comprising:


- - First data including lipid mediator profiles for a plurality of
    patients before and after administration of the DMARD, optionally
    including concentrations of lipid mediators; and
  - Second data identifying whether for each of the plurality of
    patients the DMARD was effective or ineffective.

Treatment of Inflammatory Conditions Including Rheumatoid Arthritis

DMARDS (including biologicals) are the main types of treatment for rheumatoid arthritis. Patients are also prescribed NSAIDs, Usually patients are given NSAIDs at early stages to manage symptoms and usually prior to diagnosis. Upon diagnosis patients are usually prescribed Methotrexate (˜80-90%) if within the first weeks there is no improvement, this may be combined with another non-biological DMARD such as hydrochloroquinone and if after 6 months there is no improvement other drugs, usually biologicals, are administered.

The prescription of biological DMARDs is restricted under current guidelines until after non-biological treatment has been attempted. One reason for this is that non-biological DMARDs are much cheaper than biologicals.

Patient treatment may be modified on the basis of the present invention. The method of the invention may allow:


- - Terminating treatment with an ineffective DMARD and starting
    treatment with an alternative DMARD instead.
  - Terminating treatment with an ineffective DMARD and starting
    treatment with a biologic instead.
  - Changing the dose of an ineffective DMARD.
  - Combining the ineffective DMARD with a different DMARD.

The advantageous outcome is that a patient will not need to wait 6 months to determine whether they are getting an effective drug or not, and so the clinician can explore different combinations or doses of the drug, or switch to a different drug.

The method may therefore further comprise modifying treatment of the patient. For example, the method may further comprise a subsequent step of selected from the group consisting of:


- - a) terminating treatment with an ineffective DMARD and starting
    treatment with an alternative DMARD,
  - b) terminating treatment with an ineffective DMARD and starting
    treatment with a biological DMARD instead,
  - c) changing the dose of an ineffective DMARD, typically increasing
    the dose of an ineffective DMARD, and/or
  - d) combining the ineffective DMARD with a different DMARD.

The method may comprise selecting a treatment for the patient wherein:


- - (a) if the DMARD is effective then the same DMARD is selected, and
  - (b) if the DMARD is ineffective then a different DMARD, optionally a
    biological DMARD, is selected;
  - and optionally further comprising administering the selected
    treatment to the patient.

According to a second aspect, the invention provides a method for predicting which rheumatoid arthritis pathotype a patient having, suspected of having, or at risk of developing rheumatoid arthritis will develop comprising measuring the level of at least one specialized pro-resolving mediator (SPM) in a disease-modifying antirheumatic drug (DMARD) naïve patient sample and classifying the rheumatoid arthritis pathotype a patient will develop as Lympho-myeloid, Diffuse-myeloid and Pauci-immune-fibroid.

The term “DMARD naïve” refers to a patient who has never taken a DMARD, or has never been prescribed a DMARD. The patient may have never taken and/or been prescribed a DMARD for treatment of rheumatoid arthritis.

Patients with RA can be classified into three categories or pathotypes: Lympho-myeloid, Diffuse-myeloid and Pauci-immune-fibroid. These classifications are typically performed based on based on synovial molecular and histological features. Each category of RA is associated with distinct disease evolution and responses to DMARD treatment.

In one embodiment, an upregulation of pro-resolving mediators identifies that the patient has the Pauci-immune-fibroid pathotype. An upregulation of 15R-LXA4 and/or MCTR2 may identify that the patient has the Pauci-immune-fibroid pathotype.

In one embodiment, an upregulation of pro-inflammatory and immunosuppressive mediators identifies that the patient has the Pauci-immune-fibroid pathotype. An upregulation of PGD2, TxA2 and/or TxB2, may identify that the patient has the Pauci-immune-fibroid pathotype. Levels of TxA2 may be measured indirectly via its stable further metabolite TxB2.

The term “classifying” is used interchangeably with the terms, “diagnosing” and “predicting”. The method may be considered a method for diagnosing which rheumatoid arthritis pathotype a patient having, suspected of having, or at risk of developing rheumatoid arthritis will develop, accordingly.

Classifying may comprise comparing levels of the at least one SPM in the sample obtained from the patient with a control. Where the comparison indicates that the level of the at least one SPM is higher in the sample obtained from the patient than the control then the comparison shows there is an increase in the level of the at least one SPM in the patient sample.

An increase is a difference compared to control values. The increase may for example be an increase of at least about 5%, at least about 10%, at least about 15%, at least about 20%, at least about 25%, at least about 30%, at least about 35%, at least about 40%, at least about 45%, at least about 50%, at least about 55%, at least about 60%, at least about 65%, at least about 70%, at least about 75%, at least about 80%, at least about 85%, at least about 90%, at least about 95% or at least about 100%. The increase may be an increase of at least about 20%.

Alternatively, an increase may be expressed as a fold change. The skilled person will appreciate that any percentage increase may be converted to a fold change and vice versa.

Where multiple SPM are measured, the increase that indicates efficacy of the DMARD may be the same or may be different for each SPM.

Classifying the rheumatoid arthritis pathotype a patient will develop may comprise a comparison with a control, such as a control database. A control database may be particularly beneficial when the levels of multiple SPM are be assessed.

The method may comprise classifying the rheumatoid arthritis pathotype a patient will develop using a multivariate analysis. The multivariate analysis may be orthogonal partial least squares-discrimination analysis (oPLS-DA).

The method may comprise classifying the rheumatoid arthritis pathotype a patient will develop using a trained machine learning model. The trained machine learning model may be an SVM model and/or a random forests model.

The method may comprise measuring the levels of at least two SPM and predicting which rheumatoid arthritis pathotype a patient will develop, the method comprising inputting the levels of at least two SPM into a trained machine learning algorithm, the trained machine learning algorithm being arranged to:


- - i. Compare the levels of the at least two SPM from the sample with
    the levels of the same at least two SPM in a database, and
  - iii. Output whether the patient will develop the Lympho-myeloid,
    Diffuse-myeloid or Pauci-immune-fibroid pathotype;  
    optionally wherein the trained machine learning model is a Support
    Vector Machine (SVM) model and/or a random forests model.

The trained machine learning algorithm may be trained based on training data, the training data comprising:


- - First data including lipid mediator profiles for a plurality of
    patients, optionally including concentrations of lipid mediators;
    and
  - Second data identifying whether each of the plurality of patients
    developed the Lympho-myeloid, Diffuse-myeloid or
    Pauci-immune-fibroid pathotype.

In one embodiment, the method comprises comparing the level of the at least one SPM in the patient sample to one or more controls. An “increase” or “upregulation” may be determined by comparison with the one or more controls.

The one or more controls may be one or more control samples. The one or more control samples may be analysed in parallel to the patient sample. The level of the one or more SPM may be compared to the level of the corresponding one or more SPM in the control sample. An “increase” or “upregulation” may be determined by comparison with the control sample. Comparison may be to an average SPM level between a plurality of control samples.

The one or more controls may be a database comprising levels previously obtained from one or more control samples. The level of the one or more SPM may be compared to the level of the corresponding one or more SPM in the database. An “increase” or “upregulation” may be determined by comparison with the database.

The control may be an average level of the one or more SPM in rheumatoid arthritis patient samples.

Where a clinician may treat one pathotype differently from another pathotype, classifying the rheumatoid arthritis pathotype a patient will develop may allow the adoption of a particular, or an alternative, treatment regime more suited to the patient.

For instance, without being bound by theory, the evidence so far suggests that patients with the Pauci-immune-fibroid pathotype are more resistant to DMARDs. These patients may therefore benefit more from their treatment being biologicals rather that non-biological DMARDs such as Methotrexate for example.

The method may further comprise selecting a treatment for the patient. The treatment for the patient may be selected on the basis of the classification of the rheumatoid arthritis pathotype the patient will develop.

The method may further comprise administering the treatment selected for the patient.

In one embodiment, wherein the method classifies the rheumatoid arthritis pathotype as the Pauci-immune-fibroid pathotype, a treatment with a biological DMARD is selected and optionally administered to the patient.

According to a third aspect, the invention provides a method for predicting whether a patient having, suspected of having, or at risk of developing an inflammatory condition will respond to treatment with a disease-modifying antirheumatic drug (DMARD) comprising measuring the level of at least one specialized pro-resolving mediator (SPM) in a DMARD naïve patient sample and classifying the patient as a predicted DMARD responder or a predicted DMARD non-responder.

An advantage of this aspect is instead of waiting for the disease to progress a patient would give a sample in which the levels SPMs may be measured in order to determine if they are likely to respond or not. If not, they could be immediately prescribed alternative treatments such as biologicals.

The method may comprise measuring RvD4, 10S,17S-diHDPA, 15R-LXA4 and/or MaR1n-3 DPA. The method may comprise measuring RvD4, 10S,17S-diHDPA, 15R-LXA4 and MaR1n-3 DPA. The method may comprise measuring RvD4, 5S,12S-diHETE, 4S, 14S-diHDHA, 10S,17S-diHDPA, 15R-LXA4 and/or MaR1n-3 DPA. The method may comprise measuring RvD4, 5S,12S-diHETE, 4S, 14S-diHDHA, 10S,17S-diHDPA, 15R-LXA4 and MaR1n-3 DPA.

The method may comprise measuring 14-oxo-MaR1, RvD4, RvT3 and/or RvE2. The method may comprise measuring 14-oxo-MaR1 and RvD4. The method may comprise measuring 14-oxo-MaR1, RvD4, RvT3 and RvE2.

The method may comprise measuring RvD5 and/or RvT3.

The method may further comprise measuring the level of at least one pro-inflammatory eicosanoid. The pro-inflammatory eicosanoid(s) may be PGD2 and/or PGE2. PGD2 and/or PGE2 are AA-derived mediators but are not SPM. An increase in the level of at least one pro-inflammatory eicosanoid may predict that the patient is a DMARD non-responder.

The method may further comprise measuring a marker of ALOX5 activity; a marker of ALOX12 activity and/or a marker of ALOX15 activity. The marker of ALOX5 activity; a marker of ALOX12 activity and/or a marker of ALOX15 activity may be an S-isomer of a monohyrdoxylated fatty acid. The method may comprise chiral analysis of the marker of ALOX5 activity; a marker of ALOX12 activity and/or a marker of ALOX15 activity.

The marker of ALOX5 activity may be selected from the group consisting of 5-HETE, 5HEPE, 7-HDPA and 7-HDHA. Any combination of ALOX5 markers may be measured. Any two or any three ALOX5 marker may be measured. All four ALOX5 markers may be measured. The method may therefore comprise measuring 5-HETE, 5HEPE, 7-HDPA and/or 7-HDHA. Preferably, the method comprises measuring 7-HDHA, 5-HEPE and 5-HETE.

The marker of ALOX12 activity may be selected from the group consisting of 14-HDPA and 14-HDHA. Any combination of ALOX12 markers may be measured. The method may therefore comprise measuring 14-HDPA and/or 14-HDHA.

The marker of ALOX15 activity may be selected from the group consisting of 17-HDPA, 17-HDHA, 15-HEPE and 15-HETE. Any combination of ALOX15 markers may be measured. Any two or any three ALOX15 marker may be measured. All four ALOX5 markers may be measured. The method may therefore comprise measuring 17-HDPA, 17-HDHA, 15-HEPE and/or 15-HETE.

In an alternative aspect, the invention provides a method for predicting whether a patient with rheumatoid arthritis will respond to treatment with a DMARD comprising measuring a marker of ALOX5 activity; a marker of ALOX12 activity and/or a marker of ALOX15 activity in a DMARD naïve patient sample and classifying the patient as a predicted DMARD responder or a predicted DMARD non-responder.

The term “classifying” is used interchangeably with the terms, “diagnosing” and “predicting”. The method may be considered a method for diagnosing whether a patient having, suspected of having, or at risk of developing an inflammatory condition will respond to treatment with a DMARD, accordingly.

The method may comprise classifying a patient as a predicted DMARD non-responder when the level of the at least one SPM is increased.

Classifying may comprise comparing levels of the at least one SPM in the sample obtained from the patient with a control. Where the comparison indicates that the level of the at least one SPM is higher in the sample obtained from the patient than the control then the comparison shows there is an increase in the level of the at least one SPM in the patient sample.

An increase is a difference compared to control values. The increase may for example be an increase of at least about 5%, at least about 10%, at least about 15%, at least about 20%, at least about 25%, at least about 30%, at least about 35%, at least about 40%, at least about 45%, at least about 50%, at least about 55%, at least about 60%, at least about 65%, at least about 70%, at least about 75%, at least about 80%, at least about 85%, at least about 90%, at least about 95% or at least about 100%. The increase may be an increase of at least about 20%.

Alternatively, an increase may be expressed as a fold change. The skilled person will appreciate that any percentage increase may be converted to a fold change and vice versa.

Where multiple SPM are measured, the increase that indicates efficacy of the DMARD may be the same or may be different for each SPM.

Classifying the patient as a predicted DMARD non-responder or as a predicted DMARD responder may comprise a comparison with a control, such as a control database. A control database may be particularly beneficial when the levels of multiple SPM are be assessed.

The method may comprise classifying a patient as a predicted DMARD non-responder using a multivariate analysis. The multivariate analysis may be orthogonal partial least squares-discrimination analysis (oPLS-DA).

The method may comprise a patient as a predicted DMARD non-responder using a trained machine learning model. The trained machine learning model may be an SVM model and/or a random forests model.

The method may comprise measuring the levels of at least two SPM and determining whether the patient is a DMARD responder or a DMARD non-responder, the method comprising inputting the levels of at least two SPM into a trained machine learning algorithm, the trained machine learning algorithm being arranged to:


- - i. Compare the levels of the at least two SPM from the sample with
    the levels of the same at least two SPM in a database, and
  - ii. Output whether the patient is a DMARD responder or a DMARD
    non-responder;  
    optionally wherein the trained machine learning model is a Support
    Vector Machine (SVM) model and/or a random forests model.

The trained machine learning algorithm may be trained based on training data, the training data comprising:


- - First data including lipid mediator profiles for a plurality of
    patients, optionally including concentrations of lipid mediators;
    and
  - Second data identifying whether each of the plurality of patients is
    a DMARD responder or a DMARD non-responder.

In addition to the machine learning models, another script may be used to perform differential gene expression analysis of the ALOX12, ALOX5, ALOX15 and ALOX15B enzymes. This script may be created using the known and freely-accessible package edgeR as described in the publications: Robinson M D, McCarthy D J, Smyth G K (2010). “edgeR: a Bioconductor package for differential expression analysis of digital gene expression data.” Bioinformatics, 26(1), 139-140 and McCarthy D J, Chen Y, Smyth G K (2012). “Differential expression analysis of multifactor RNA-Seq experiments with respect to biological variation.” Nucleic Acids Research, 40(10), 4288-4297. This script uses the quasi-likelihood method to identify differences in the expression levels of specific genes between a DMARD responder and a DMARD non-responder. It also provides a violin plots to visualize the different gene expression levels.

In one embodiment, the method comprises comparing the level of the at least one SPM in the patient sample to one or more controls. An “increase” or “upregulation” may be determined by comparison with the one or more controls.

The one or more controls may be one or more control samples. The one or more control samples may be analysed in parallel to the patient sample. The level of the one or more SPM may be compared to the level of the corresponding one or more SPM in the control sample. An “increase” or “upregulation” may be determined by comparison with the control sample. Comparison may be to an average SPM level between a plurality of control samples.

The one or more controls may be a database comprising levels previously obtained from one or more control samples. The level of the one or more SPM may be compared to the level of the corresponding one or more SPM in the database. An “increase” or “upregulation” may be determined by comparison with the database.

The control may be an average level of the one or more SPM in a plurality of DMARD naïve patient samples.

If a patient is classified ahead of treatment as a predicted DMARD non-responder then a clinician may treat that patient differently to a patient classified as a predicted DMARD responder. Classifying the patient as a predicted DMARD non-responder or as a predicted DMARD responder may allow the adoption of a particular, or an alternative, treatment regime more suited to the patient.

For instance, a predicted DMARD non-responder may be more resistant to DMARDs. These patients may therefore benefit more from their treatment being biologicals rather that non-biological DMARDs such as Methotrexate for example.

The method may further comprise selecting a treatment for the patient. The treatment for the patient may be selected on the basis of the classification of the patient as a predicted DMARD non-responder or as a predicted DMARD responder.

The method may further comprise selecting a treatment for the patient wherein:


- - (a) if the patient is a predicted DMARD responder then a
    non-biological DMARD is selected, and
  - (b) if the patient is a predicted DMARD non-responder then a
    biological DMARD is selected;  
    and optionally further comprising administering the selected
    treatment to the patient.

The method may further comprise administering the treatment selected for the patient.

In one embodiment, wherein the method classifies the patient as a predicted DMARD non-responder, a treatment with a biological DMARD is selected and optionally administered to the patient.

In another embodiment, wherein the method classifies the patient as a predicted DMARD responder, a treatment with a non-biological DMARD is selected and optionally administered to the patient.

In one embodiment, the method comprises comparing the level of the at least one SPM in the patient sample to one or more controls. An “increase” or “upregulation” may be determined by comparison with the one or more controls.

The one or more controls may be one or more control samples. The one or more control samples may be analysed in parallel to the patient sample. The level of the one or more SPM may be compared to the level of the corresponding one or more SPM in the control sample. An “increase” or “upregulation” may be determined by comparison with the control sample. Comparison may be to an average SPM level between a plurality of control samples.

The one or more controls may be a database comprising levels previously obtained from one or more control samples. The level of the one or more SPM may be compared to the level of the corresponding one or more SPM in the database. An “increase” or “upregulation” may be determined by comparison with the database.

The control may be an average level of the one or more SPM in samples from patients having, suspected of having, or at risk of developing the same inflammatory condition.

The method of the second aspect may be combined with the method of the third aspect. Without being bound by theory, integrating a predication of which rheumatoid arthritis pathotype a patient having, suspected of having, or at risk of developing rheumatoid arthritis will develop with a prediction of whether the patient is a DMARD responder or a DMARD non-responder may:


- - a) Provide an improved prediction of whether the patient is a DMARD
    responder or a DMARD non-responder, and/or
  - b) provide an improved selection of a treatment for the patient.

Accordingly, the invention also provides a method for predicting whether a patient having, suspected of having, or at risk of developing rheumatoid arthritis will respond to treatment with a disease-modifying antirheumatic drug (DMARD) comprising classifying the rheumatoid arthritis pathotype a patient will develop as Lympho-myeloid, Diffuse-myeloid and Pauci-immune-fibroid in accordance with the method of the second aspect, measuring the level of at least one specialized pro-resolving mediator (SPM) in a DMARD naïve patient sample and classifying the patient as a predicted DMARD responder or a predicted DMARD non-responder.

The method of the third aspect may therefore further comprise classifying the rheumatoid arthritis pathotype a patient will develop as Lympho-myeloid, Diffuse-myeloid and Pauci-immune-fibroid in accordance with the method of the second aspect.

In some embodiments, where the patient is classified as a patient that will develop the Pauci-immune-fibroid pathotype and as a predicted DMARD non-responder, a treatment with a biological DMARD is selected and optionally administered to the patient.

Computer Implementation

The methods of the present invention may be performed by a computer and equipment controlled by the computer. The step of measuring the level of at least one specialized pro-resolving mediator (SPM) may be performed by equipment controlled by the computer.

The invention also provides a computer-implemented method of assessing the efficacy of a DMARD for use in the treatment of an inflammatory condition in a patient, which comprises receiving in a computer sample data representing the levels of at least one SPM in samples obtained from the patient before and after administration of the DMARD and executing software on the computer to compare the levels of the at least one SPM in the samples, an increase in the level of the at least one SPM after administration of the DMARD being indicative of efficacy of the DMARD, and to output efficacy data representing the efficacy of the DMARD on the basis of the comparison.

The invention also provides a computer program comprising instructions which, when executed by a computer, cause the computer to carry out a computer implemented method of the invention.

It will be appreciated that the step of comparing the levels of the at least one SPM in the samples may be carried out on a different computer from a computer that initially receives data representing the levels of the SPM in the samples.

The invention also provides a computer apparatus for assessing the efficacy of a DMARD for use in the treatment of an inflammatory condition in a patient, which comprises a first device incorporating a computer, a second computer and a communication channel between the first device and second computer for the transmission of data therebetween; wherein the first device is arranged to receive sample data representing the levels of at least one SPM in samples obtained from the patient before and after administration of the DMARD and to transmit the sample data to the second computer via the communication channel, and the second computer is arranged to execute software to compare the levels of the at least one SPM in the samples to determine the efficacy of the DMARD for the patient, an increase in the level of the at least one SPM after administration of the DMARD being indicative of efficacy, and output efficacy data representing the efficacy of the DMARD.

The second computer may be arranged to transmit the efficacy data to the first device via the communication channel, or to a third computer.

In some embodiments, the first device may incorporate an immunoassay, equipment or device for measuring the level of at least one SPM in a sample.

The invention also provides a computer implemented method and computer apparatus for predicting which rheumatoid arthritis pathotype a patient having, suspected of having, or at risk of developing rheumatoid arthritis will develop in accordance with the second aspect of the invention, the features of which correspond to those given above for a computer implemented method and computer apparatus in accordance with the first aspect of the invention mutatis mutandis.

The invention also provides a computer implemented method and computer apparatus for predicting whether a patient having, suspected of having, or at risk of developing an inflammatory condition will respond to treatment with a disease-modifying antirheumatic drug (DMARD) in accordance with the third aspect of the invention, the features of which correspond to those given above for a computer implemented method and computer apparatus in accordance with the first aspect of the invention mutatis mutandis.

Further Advantages

Using samples from deeply phenotyped patients diagnosed with rheumathoid arthritis that had not yet received treatment for their conditions the inventors assessed the levels of bioactive mediators in their plasma and assessed the correlation of these lipid mediators with outcome of treatment with DMARDs. Results from these studies demonstrated identified four specific molecules that were prognostic for treatment outcome. In addition, these studies also demonstrated that peripheral mediator concentrations may be related to disease subsets which in turn are linked with disease severity and treatment responsiveness.

Thus, these results indicate that comparing the levels of bioactive lipid mediators in plasma from patients upon diagnosis will provide an indication on which therapeutic they may respond best to. In addition, measuring the plasma levels of these molecules after initiation of treatment will also provide an indication of whether the patient is responding to the given treatment or not.

This methodology can predict whether a patient with Rheumatoid Arthritis will respond to treatment with DMARDs.

An advantage provided by the invention is the ability of a clinician to tell at the outset whether DMARD treatment will be effective. Currently, whilst it can become apparent quite quickly whether a specific treatment regime is working or not, it may well take a cycle of six months of dose escalation, combination with pain killers etc. before a clinician may try, first a different DMARD, and then ultimately a different class of drug. That second cycle can take another six months, totaling a year of disease progression and potentially irreversible damage, before an effective treatment (likely a biological) is used. This is debilitating to the patient and brings not only health consequences, in the form of secondary disease complications, for example cardiovascular disease, and MTX side-effects, but also economic consequences. To these can be added the side effects of DMARDs which can be quite unpleasant.

An advantage provided by the invention in relation to determination of the disease pathotype is that, as well as having a relationship to the potential responsiveness of the patient, different pathotypes require different levels of treatment aggression. Determination of a patient's disease pathotype therefore allows personalisation of their treatment.

The invention finds use in both clinical laboratories to aid in patient stratification as well as to in pharmaceuticals as an aid to drug development.

Preferred features for the second and subsequent aspects of the invention are as for the first aspect of the invention mutatis mutandis.

The present invention will now be described by way of reference to the following Examples and accompanying Drawings which are present for the purposes of illustration only and are not to be construed as being limiting on the invention.

### Example 1—Plasma SPM Concentrations are Predictive of Responsiveness to DMARD Treatment in RA Patients

In order to determine whether peripheral blood SPM concentrations are predictive of DMARD responsiveness in patients with RA, we investigated plasma lipid mediator profiles in deeply phenotyped early RA patients prior to treatment initiation (see table 6 for patient information). Plasma lipid mediators were identified in accordance with published criteria (Dalli, J., Colas, R. A., Walker, M. E. & Serhan, C. N. “Lipid Mediator Metabolomics Via LC-MS/MS Profiling and Analysis.” Methods Mol Biol 1730, 59-72 (2018), the contents of which are incorporated by reference). In RA patient plasma we identified mediators from all four major essential fatty acid metabolomes, i.e. arachidonic acid (AA), EPA, n-3 DPA and DHA (Table 7). These included the EPA, n-3 DPA and DHA-derived resolvins and the n-3 DPA and DHA-derived protectins and maresins. We next used Orthogonal Projections to Latent Structures Discriminant Analysis (OPLS-DA), which generates a regression model based on concentrations of lipid mediators differently expressed between two groups (Chong, J., Yamamoto, M. & Xia, J. MetaboAnalystR 2.0: “From Raw Spectra to Biological Insights.” Metabolites 9 (2019), the contents of which are incorporated by reference), to assess the concentrations of identified mediators between DMARD-responders and DMARD-non-responders. Here we observed two distinct clusters representing DMARD-responders and DMARD-non-responders (FIG. 1A, B). We next used the machine learning method random forests to build models based on plasma lipid mediator concentrations to further evaluate whether pre-treatment levels of these mediators were linked with DMARD responsiveness. Using this approach, we found that cumulative concentrations of the DHA (that includes the D-series resolvins, protectins and maresins) and EPA (that includes the E-series resolvins) metabolomes were the most accurate at predicting whether a patient would respond to treatment or not. The accuracy for the DHA metabolome at predicting outcome was of ˜81% and that of the n-3 DPA metabolome was of ˜69% (FIG. 1C and Table 8). Of note, these values were also higher than those obtained using a combination of clinical parameters that included the DAS28-ESR and rheumatoid factor concentrations (FIG. 1C).

In order to validate the robustness of our model we obtained peripheral blood lipid mediator profiles from a second cohort of DMARD naive patients composed of 36 responders and 22 non-responders, and tested whether the models generated using the different mediator metabolomes predicted outcome for patients in this cohort (see Tables 9 and 10 for patient clinical parameters and lipid mediator concentrations). For this purpose, we assessed the receiver operating characteristic (ROC) curve, which evaluates the diagnostic potential of a classifier by varying its discrimination threshold. Assessment of the area under the curve for the generated plots demonstrated that the DHA metabolome gave an AUC of 0.44, whereas the n-3 DPA metabolome gave an AUC of 0.58 (FIG. 1D, FIG. 13 and Table 8). Similar findings were made using support vector machines, a different machine learning strategy. Here, the DHA metabolome gave the highest accuracy score of ˜62%, an AUC of 0.54, whilst the n-3 DPA metabolome gave an accuracy score of 61%, an AUC of 0.66 (Table 1). We further evaluated the ability of the n-3 DPA metabolome-based model to accurately categorize patients using the resulting confusion matrix of the model. Here we found that the model based on concentrations of n-3 DPA derived mediators was able to correctly classify ˜83% of responders in the appropriate category (FIG. 1E). Thus, these results indicate that baseline peripheral blood lipid mediator profiles are linked with DMARD treatment outcome.

Increased eicosanoid and SPM concentrations in peripheral blood from DMARD non-responders

To gain insights into mechanisms determining the responsiveness of patients to DMARD treatment, we conducted lipid mediator pathway analysis to identify which pathways were differentially regulated between the two patient groups. This demonstrated that there was an upregulation of SPM biosynthetic pathways, including the DHA derived RvD5 and the n-3 DPA derived RvT3 as well as the pro-inflammatory eicosanoids, including the nociceptive mediators PGD2 and PGE2, in DMARD non-responders when compared with responders (FIG. 2). To determine whether the differences in SPM expression were linked with a distinct transcriptional regulation of enzymes involved in SPM biosynthesis we assessed the transcript expression of ALOX enzymes in peripheral blood from these two patient groups. ALOX5, ALOX12, ALOX15 and ALOX15B transcript levels were similar between the DMARD-responders and DMARD-non-responders (FIG. 3). These results suggest that regulation of SPM biosynthetic pathways may be via either the regulation of protein translation or posttranslational modification of the enzymes to regulate their activity (Dalli, J., Chiang, N. & Serhan, C. N. “Elucidation of novel 13-series resolvins that increase with atorvastatin and clear infections.” Nat Med 21, 1071-1075 (2015) and Fredman, G., et al. Resolvin “D1 limits 5-lipoxygenase nuclear localization and leukotriene 84 synthesis by inhibiting a calcium-activated kinase pathway.” Proc Natl Acad Sci USA 111, 14530-14535 (2014). The contents of both of which are incorporated herein by reference). Thus, we next tested whether the activity of these enzymes was altered. For this purpose, we measured plasma levels of monohydroxylated fatty acids from all four fatty acid metabolomes to gain insights into their activity in the two patient groups. Assessment of plasma concentrations of 5-HETE, 5HEPE, 7-HDPA and 7-HDHA, markers of ALOX5 activity, revealed a significant upregulation of 7-HDHA, 5-HEPE and 5-HETE in DMARD-non-responders when compared with responders. Concentrations of markers for ALOX12 (14-HDPA and 14-HDHA) and ALOX15 (17-HDPA, 17-HDHA, 15-HEPE and 15-HETE) also demonstrated an increased in activity for these enzymes in non-responders (FIG. 4). Thus, these findings indicate that the observed increases in plasma SPM in non-responders was due to increased ALOX activity. To further evaluate the origin of these proposed pathway markers we conducted chiral liquid chromatography tandem mass spectrometry which permits the separation the R and S isomers of a given hydroxylated fatty acid. Here we found that in plasma of both DMARD responders and DMARD non-responders the most abundant isomer for all the monohydroxylated fatty acids tested was that carrying the alcohol in the S conformation (FIG. 14). Given that all four ALOX enzymes involved in SPM biosynthesis preferentially oxygenate fatty acids in the S conformation, these results indicate an increased ALOX activity in non-responders.

### Example 2—Baseline RvD4, 10S, 17S-diHDPA, 15R-LXA4, MaR1n-3 DPA Concentrations are Predictive of DMARD-Treatment Outcome in RA Patients

Having found that lipid mediator profiles are predictive of responsiveness to DMARD treatment in RA patients we next investigated whether we could identify specific lipid mediators that may be useful as biomarkers for treatment responsiveness. For this purpose, we conducted a random forest “importance” analysis that identifies the relevance of every mediator in the performance of the model based on the prediction accuracy. Here we found that the DHA-derived RvD4 (4S,5R,17S-trihydroxy-6E,8E,10Z,13Z,15E,19Z-docosahexaenoic acid) and 10S, 17S-diHDPA (10S,17S-dihydroxy-7Z,11E,13Z,15E,19Z-docosapentaenoic acid) were the most important mediators in predicting treatment responsiveness, with 15R-LXA4 (5S,6R,15R-trihydroxy-7E,9E,11Z,13E-eicosatetraenoic acid), 5S,12S-diHETE (5S,12S-dihydroxy-6E,8Z,10E,14Z-eicosatetraenoic acid), 4S, 14S-diHDHA (4S,14S-dihydroxy-5E,7Z,10Z,12E,16Z,19Z-docosahexaenoic acid) and n-3 DPA derived Maresin 1 (MaR1n-3 DPA) (7R,14S-dihydroxy-8E,10E,12Z,16Z,19Z-docosapentaenoic acid) also displaying a marked contribution although to a lesser extent than the RvD4 and 10S, 17S-diHDPA (FIG. 1F). Having identified potential candidate biomarkers, we next built machine-learning models using the random forest methodology and concentrations of either RvD4, 10S, 17S-diHDPA, 15R-LXA4 and MaR1n-3 DPA or RvD4, 10S, 17S-diHDPA, 15R-LXA4, 5S,12S-diHETE, 4S,14S-diHDHA, MaR1n-3 DPA using a second group of DMARD naive patients (see Table 9 and 10 for patient clinical parameters and lipid mediator concentrations) and tested the ability of this model to assign patients to the correct outcome group. Here we found that the combination of the two mediators alone predicted treatment outcome in ˜86% of the cases while the model build using the four mediators gave a better prediction score of ˜83% (FIG. 1G). We next validated the accuracy of these two models using mediator concentrations from a different group of DMARD naive patients. Results from these experiments demonstrated that the model build using the four mediators gave an AUC of 0.80, whereas the model built with the six mediators gave an AUC score of 0.79 (FIG. 1H). Of note, the AUC for these mediators were markedly better than those obtained using mediator concentrations from the n-3 DPA metabolome and disease scores (FIG. 1D).

### Example 3— Pre-Treatment Lipid Mediator Profiles Identify Distinct Disease Pathotypes

Recent studies demonstrate that based on synovial molecular and histological features patients with RA can be classified into three categories Lympho-myeloid, Diffuse-myeloid and Pauci-immune-fibroid that are associated with distinct disease evolution and responses to DMARD treatment (Humby, F., et al. “Synovial cellular and molecular signatures stratify clinical response to csDMARD therapy and predict radiographic progression in early rheumatoid arthritis patients.” Ann Rheum Dis (2019), the contents of which are incorporated herein by reference). Therefore, we next questioned whether immune-related features in each of these groups extended beyond the synovium into the systemic circulation. To address this question, we conducted lipid mediator profiling to assess whether peripheral blood lipid mediator concentrations in RA patients from each of these three groups were distinct prior to the initiation of DMARD therapy. Using PLS-DA we found that plasma lipid mediators were indeed characteristic for different disease pathotypes i.e. distinct lipid mediator profiles clustered with each category (FIG. 5A). Assessment of the variable importance in projection (VIP) scores, which identify the contribution of each mediator in the observed separation between groups demonstrated an upregulation of pro-resolving mediators, including 15R-LXA4 and MCTR2, in peripheral blood from patients with the Pauci-immune-fibroid pathotype. In plasma from these patients we also found an upregulation of pro-inflammatory and immunosuppressive mediators including PGD2 and TxA2, measured as its stable the further metabolite TxB2 (FIG. 5B).

We next investigated the differential regulation of lipid mediator profiles between DMARD-responders and non-responders for each of these three pathotypes. Here we found an increase in ALOX5 products from both the n-3 DPA and DHA metabolomes in non-responders with Lympho-myeloid and those with a Pauci-immune-fibroid pathotype when compared with responders with the respective pathotypes. These included significant increases in the DHA-derived RvD4, and PDX. Assessment of mediators from the AA and EPA metabolomes demonstrated an increase in ALOX5 products in non-responders with Lympho-myeloid and Pauci-immune-fibroid pathotypes that reached statistical significance in patients with a Pauci-immune-fibroid pathotype for the leukotriene (LT) B4 pathway including its further metabolite 20-COOH-LTB4. In these patients we also found a statistically significant increase of the pro-inflammatory and nociceptive mediator PGE2 (FIG. 6). These results demonstrate that differences in peripheral blood lipid mediator profiles between DMARD-responders and non-responders are common to different RA pathotypes.

Having found that lipid mediator concentrations were different between these patient groups, we next assessed whether combining disease pathotypes with the biomarkers identified above would further enhance the predictiveness of our machine learning model. Results from this analysis demonstrate a marked increase in the predictiveness of RvD4, 10S, 17S-diHDPA, 15R-LXA4 and MaR1n-3 DPA at identifying responders, when separate machine learning models were built for each of the RA pathotypes, with the ability of the model to correctly classify responders increasing to ˜89% (FIG. 5D).

### Example 4—Increased SPM in DMARD-Responders when Compared to Non-Responders 6 Months after Treatment

Having observed a differential regulation in peripheral blood SPM concentrations between DMARD-responders and DMARD-non-responders prior to treatment initiation we next investigated whether differences in peripheral blood lipid mediator concentrations were also present in patients 6 months after treatment initiation. OPLS-DA analysis demonstrated that plasma lipid mediator profiles from DMARD responders 6 months after the initiation of treatment were distinct from those of DMARD-non-responders, as demonstrated by a separation between the two patient clusters (FIG. 7A, Table 11). Assessment of VIP scores identified 21 mediators and SPM pathway markers that were differentially expressed between the two patient groups (FIG. 7B). Amongst these mediators we found SPM that are involved in coordinating the host response during ongoing inflammation such as PCTR2, RvD2 and RvD3 (Arnardottir, H. H., et al. Resolvin “D3 Is Dysregulated in Arthritis and Reduces Arthritic Inflammation.” J Immunol 197, 2362-2368 (2016), Chiang, N., Dalli, J., Colas, R. A. & Serhan, C. N. “Identification of resolvin D2 receptor mediating resolution of infections and organ protection”. J Exp Med 212, 1203-1217 (2015), and Dalli, J., Ramon, S., Norris, P. C., Colas, R. A. & Serhan, C. N. Novel proresolving and tissue-regenerative resolvin and protectin sulfido-conjugated pathways. FASEB J 29, 2120-2136 (2015), the contents of all of which are incorporated by reference) as well as mediators linked with pain modulation e.g. RvE1 and RvE2 (Barden, A. E., et al. “Specialised pro-resolving mediators of inflammation in inflammatory arthritis”. Prostaglandins Leukot Essent Fatty Acids 107, 24-29 (2016) and Xu, Z. Z., et al. “Resolvins RvE1 and RvD1 attenuate inflammatory pain via central and peripheral actions.” Nat Med 16, 592-597, 591p following 597 (2010), the contents of both of which are incorporated by reference) (FIG. 7B).

In order to gain further insights into the mediator pathways that were differentially regulated between these patient groups we interrogated the biosynthetic pathways for each of the essential fatty acid metabolomes. This analysis demonstrated that the concentrations of ALOX5 and ALOX15-derived mediators from both the n-3 DPA and DHA metabolomes were reduced in the plasma of non-responders when compared to responders (FIG. 7C). Pathway analysis of EPA and AA-derived lipid mediator concentrations demonstrated that while ALOX5 derived products of EPA were also reduced, AA-derived ALOX5 products, including those of the potent leukocyte chemoattractant LTB4 and the ionotropic cysteinyl leukotrienes (Radmark, O., Werz, O., Steinhilber, D. & Samuelsson, B. “5-Lipoxygenase, a key enzyme for leukotriene biosynthesis in health and disease”. Biochim Biophys Acta 1851, 331-339 (2015), the contents of which are incorporated herein by reference), were markedly increased in plasma from non-responders when compared with responders (FIG. 7D).

Having observed significant decreases in SPM concentrations we next investigated whether the activity of ALOX enzymes and the conversion of DHA and n-3 DPA was altered in peripheral blood cells from the two patient groups. For this purpose, we measured plasma levels of monohydroxylated fatty acids from the DHA and n-3 DPA metabolomes to gain insights into both enzyme activity and substrate conversion. Plasma concentrations of the ALOX5 products 7-HDPA and 7-HDHA were either similar (7-HDPA) between the two patient groups, or upregulated (7-HDHA) in DMARD-non-responders. Concentrations of the ALOX12 (14-HDPA and 14-HDHA) and ALOX15 (17-HDHA and 17-HDPA) products were increased in non-responders (FIG. 8). Of note, as observed in baseline plasma, chiral analysis of monohydroxylated fatty acids demonstrated that the predominant isomer for each of these products was the S-isomer (FIG. 15). These findings indicate that the observed reduction in plasma DHA and n-3 DPA derived SPM in DMARD non-responders was not due to a decrease in ALOX activity and/or substrate availability/conversion in peripheral blood cells from these patients. Together these observations demonstrate that 6 months after treatment initiation plasma SPM concentrations in DMARD responders were higher than those measured in DMARD non-responders. Given that enzyme activity was elevated in non-responders when compared with responders, this suggests that uncoupling of the SPM biosynthetic pathways may be responsible for the reductions in plasma SPM concentrations.

### Example 5—SPM Mediate the Protective Actions of MTX in Experimental Inflammatory Arthritis

Since SPM were elevated after treatment initiation in responders when compared with non-responders, and given that MTX is the anchor drug in the treatment of these patients, we next questioned whether MTX regulated SPM production. Incubation of human whole blood with MTX at a clinically relevant and comparable concentration (Edno, L., et al. “Total and free methotrexate pharmacokinetics in rheumatoid arthritis patients”. Ther Drug Monit 18, 128-134 (1996), the contents of which are incorporated herein by reference) led to an increase in plasma SPM concentrations as demonstrated by rightward shift in the SPM cluster in the OPLS-DA analysis. This shift was linked with an upregulation of mediators from the DHA, n-3 DPA and EPA bioactive metabolomes including DHA-derived PDX and RvD1 as well as the EPA-derived RvE3 (FIG. 9A-C and Table 12).

In order to test whether findings made with human cells in vitro were also translatable to the in vivo scenario we next assessed whether MTX also upregulated SPM levels in mice. Administration of MTX to mice led to a dose-dependent shift in the peripheral blood SPM profile. Of note this shift was linked with an upregulation of several ALOX15-derived SPM including RvT1, RvT4 and RvD5n-3 DPA (FIG. 9D-E and Table 13). We next tested whether the regulation of SPM was central to the joint protective actions of MTX in experimental inflammatory arthritis. For this purpose, we administered MTX to wild type (WT) mice and mice that lack ALOX15 (Alox151 and assessed joint disease activity. As anticipated, administration of MTX to WT mice led to a significant reduction in clinical scores, an improvement in weight loss and a decrease in paw edema (FIG. 10A-C). In these studies, we also found a decrease in the number of eosinophils, neutrophils, monocytes and macrophages that were recruited to the joint as well as a reduction in inflammatory eicosanoid concentrations (FIGS. 10D and 11). Of note the protective actions of MTX were lost in mice lacking the ALOX15 enzyme. In these mice, MTX no longer regulated disease activity, weight loss (FIG. 10A-C), leukocyte trafficking (FIG. 10D) as well as peripheral blood and circulating eicosanoid concentrations (FIG. 11). Therefore, these findings indicate that MTX upregulates SPM production and loss of these endogenous pathways reverses the joint protective actions of this DMARD.

Human whole blood was incubated with MTX (100 nM, 37° C., 45 min). Incubations were quenched and SPM were identified and quantified using LC-MS/MS-based lipid mediator profiling. Results are mean±SEM. n=6 volunteers per group.

### Example 6— Activation of p-300 and MAPK by MTX Increases SPM Production and Protects During Experimental Inflammatory Arthritis

Distinct signalling pathways, including those downstream of CREB-binding protein and its homologue p300 (CBP/p300) as well as p38 mitogen-activated protein kinase (MAPK), are implicated in mediating the cellular actions of MTX in target cells, including leukocytes (Thornton, C. C., et al. “Methotrexate-mediated activation of an AMPK-CREB-dependent pathway: a novel mechanism for vascular protection in chronic systemic inflammation”. Ann Rheum Dis 75, 439-448 (2016) and Wu, C. W., et al. “Combined treatment with vitamin C and methotrexate inhibits triple-negative breast cancer cell growth by increasing H2O2 accumulation and activating caspase-3 and p38 pathways”. Oncol Rep 37, 2177-2184 (2017), the contents of both of which are incorporated herein by reference). Given that these two pathways are also implicated in the regulation of ALOX15 expression (Shankaranarayanan, P., Chaitidis, P., Kuhn, H. & Nigam, S. “Acetylation by histone acetyltransferase CREB-binding protein/p300 of STAT6 is required for transcriptional activation of the 15-lipoxygenase-1 gene”. J Biol Chem 276, 42753-42760 (2001), Xu, B., et al. “Interleukin-13 induction of 15-lipoxygenase gene expression requires p38 mitogen-activated protein kinase-mediated serine 727 phosphorylation of Stat1 and Stat3.” Mol Cell Biol 23, 3918-3928 (2003) and Fredman, G., et al. “An imbalance between specialized pro-resolving lipid mediators and pro-inflammatory leukotrienes promotes instability of atherosclerotic plaques”. Nat Commun 7, 12859 (2016) the contents of all of which are incorporated by reference) we next questioned whether they were involved in the observed increases in SPM production by MTX. For this purpose, we employed a pharmacological approach to assess whether inhibitors to these pathways blocked MTX-induced upregulation of SPM in human peripheral blood. Here we found that incubation of whole blood with inhibitors to both CBP/p300 (L002) and MAPK (SB202190) markedly shifted the plasma lipid mediator profile blocking the MTX-induced upregulation of SPM, decreasing the concentrations of several mediators including PD1, MaR2n-3 DPA and in the anti-arthritic RvD1 (Norling, L. V., et al. “Proresolving and cartilage-protective actions of resolvin D1 in inflammatory arthritis”. JCI Insight 1, e85922 (2016), the contents of which are incorporated by reference) (FIG. 12A, B). We next tested whether inhibition of these pathways also reversed the anti-arthritic actions of MTX in experimental inflammatory arthritis. Here we found that administration of either L002 or SB202190 reversed the anti-arthritic actions of MTX, as measured by an increase in joint inflammation, an increase in joint damage, and an increase in weight loss, a marker of disease activity (FIG. 12C-E). Administration of these inhibitors also reversed the ability of MTX to regulate neutrophil trafficking to the inflamed joint, an observation that was linked with an increase in the joint concentrations of the potent leukocyte chemoattractant LTB4 (FIG. 12F, G). Thus, pharmacological inhibition of CBP/p300 or MAPK abrogates the beneficial effects of MTX on ALOX15 activity and the downstream beneficial effects on joint disease. These findings suggest that via the activation of CBP/p300 and MAPK, MTX regulates the activity of ALOX15 upregulating SPM production, dampening joint inflammation and joint damage during inflammatory arthritis.

### Example 7— Summary of Suitable Sample Processing Method

Plasma samples will be collected placed in methanol containing deuterium labelled internal standards (d4_LTB4, da-5S-HETE, d4-PGE2, d5-LXA4 and d5-RvD2, 500 pg each). These were then kept at −20° C. for 45 minutes to allow for protein precipitation and subjected to solid phase extraction as per previous publication (Dalli et al 2018). Methyl formate fractions were then brought to dryness using a TurboVap LP (Biotage) and products suspended in water-methanol (50:50 vol:vol) for LC-MS-MS. A Shimadzu LC-20AD HPLC and a Shimadzu SIL-20AC autoinjector (Shimadzu, Kyoto, Japan), paired with a QTrap 5500 (ABSciex, Warrington, UK) were utilised and operated as described (Dalli et al 2018). To monitor each lipid mediator and respective pathways, a Multiple Reaction Monitoring (MRM) method was developed with diagnostic ion fragments and identification using recently published criteria (Dalli et al 2018), including matching retention time (RT) to synthetic and authentic materials and at least six diagnostic ions for each lipid mediator. Calibration curves were obtained for each using authentic compound mixtures and deuterium labeled lipid mediator at 0.78, 1.56, 3.12, 6.25, 12.5, 25, 50, 100, and 200 μg. Linear calibration curves were obtained for each lipid mediator, which gave r2 values of 0.98-0.99. All analyses were conducted blind.

Levels of the mediators levels for the following lipid mediator families:

Lipoxins, leukotrienes, prostaglandins and thromboxane from Arachidonic acid; E-series resolvins from eciosapentaenoic acid; resolvins, protectins and maresins from n-3 docosapentanoic acid and resolvins, protectins and maresins from docosahexaenoic acid as well as their pathway markers and further metabolites will be measured in plasma from these patients and compared to an established database compiled using deeply phenotyped patient samples from patients that were responsive and non-responsive to the treatments of interest.

Materials & Methods

The following materials and methods relate to all of the Examples above.

Liquid chromatography (LC)-grade solvents were purchased from Fisher Scientific (Pittsburgh, Pa., USA); Poroshell 120 EC-C18 column (100 mm×4.6 mm×2.7 μm) was obtained from Agilent (Cheshire, UK); C18 SPE columns were from Biotage (Uppsala, SE); synthetic standards for LC-tandem mass spectrometry (MS-MS) quantitation and deuterated (d) internal standards (da-5S-HETE, d5-RvD2, d5-LXA4, d4-PGE2, and d4-LTB4) were purchased from Cambridge Bioscience (Cambridge, UK) or provided by Charles N. Serhan (Harvard Medical School, Boston, Mass., USA; supported by NIH-funded P01GM095467); Methotrexate (MTX, Sigma); Dulbecco's Phosphate-Buffered Saline (DPBS, without calcium and magnesium, Sigma); Whole Blood Lysing Reagent Kit (Beckman Coulter, Inc.). L002 and SC202190 (Cayman Chemicals).

Pathobiology of Early Arthritis Cohort

Baseline and 6 months post treatment plasma samples were obtained from the Pathobiology of Early Arthritis Cohort (PEAC). The PEAC cohort study was approved by the King's College Hospital Research Ethics Committee (REC 05/Q0703/198). Following written informed consent, peripheral blood samples and synovial tissue were obtained from patients recruited at Barts Health NHS Trust into the Pathobiology of Early Arthritis Cohort (PEAC, http://www.peac-mrc.mds.qmul.ac.uk) undergoing ultrasound (US)-guided synovial biopsy of the most inflamed joint (knee, wrist or small joints of hands or feet)5. All patients were disease modifying anti-rheumatic drugs (DMARDs) and steroid-naïve, had symptoms duration less than 12 months and fulfilled the ACR/EULAR 2010 classification criteria for RA. RA individuals were categorised into three pathotypes based on histological classification of synovial tissue: Lympho-myeloid, Diffuse-Myeloid and pauci-immune Fibroid (for more details see Humby, F., et al. “Synovial cellular and molecular signatures stratify clinical response to csDMARD therapy and predict radiographic progression in early rheumatoid arthritis patients.” Ann Rheum Dis (2019), the contents of which are incorporated herein by reference). Patients were treated with methotrexate. Response status after 6 months of mixed DMARD therapy was determined by EULAR response criteria based on DAS28-ESR.

Chiral LC-MS/MS Analysis

For chiral lipidomic analysis, a Chiralpak AD-RH column (150 mm×2.1 mm×5 μm) was used with isocratic methanol/water/acetic acid 95:5:0.01 (v/v/v) at 0.15 ml/min. To monitor isobaric monohydroxy docosapentaenoic acid levels, a multiple reaction monitoring (MRM) method was developed using signature ion fragments for each molecule as in Dalli J, Chiang N, Serhan C N. Elucidation of novel 13-series resolvins that increase with atorvastatin and clear infections. Nat Med 21, 1071-1075 (2015).

Data

The data used for the machine learning models and network analyses consisted of the lipid mediator profiles of patients with RA who responded (n=30) or did not (n=24) to the treatment with DMARDs for the first PEAC-derived patient cohort. The lipid mediator profile included DHA-derived resolvins (RvD1, RvD2, RvD3, RvD4, RvD5, RvD6, 17-RvD1 and 17-RvD3), protectins (PD1, 17-PD1, 10S,17S-diHDAH and 22-OH-PD1), PCTRs (PCTR1, PCTR2 and PCTR3), maresins (MaR1, MaR2, 7S,14S-diHDHA, 4,14-diHDHA, 14-oxo-MaR1 and 22-OH-MaR1), MCTRs (MCTR1, MCTR2 and MCTR3), 13-series resolvins (RvT1, RvT2, RvT3 and RvT4), n-3 DPA-derived resolvins (RvD1n-3 DPA, RvD2n-3 DPA and RvD5n-3 DPA), n-3-DPA derived protectins (PD1n-3 DPA and 10S, 17S-diHDPA), n-3 DPA-derived maresins (MaR1n-3 DPA), E-series resolvins (RvE1, RvE2 and RvE3), leukotrienes (LXA4, LXB4, 5S,15S-diHETE, 20-OH-LTB4, 20-COOH-LTB4, 6-trans-LTB4 and 12-epi-6-trans-LTB4), cysteinyl leukotrienes (LTC4, LTD4 and LTE4), prostaglandins (PGD2, PGE2, PGF2a) and thromboxane (TXB2). A Clinical Score model was obtained using the following clinical parameters: disease duration, erythrocyte sedimentation rate (ESR), rheumatoid factor (RF titre), tiredness visual analogue scale (VAS), pain VAS, patient global health VAS, physician global assessment VAS, swollen joints number, disease activity score-28 (DAS28) and 12 max US Synovial Thickness and US Power Doppler scores. A second patient cohort of 45 patients (37 responders and 8 non-responders) was obtained from the PEAC study and was used as the validation dataset for the lipid mediator profiling and Clinical Score models, and also as the training dataset for improved models based on specific biomarkers. Age, sex and clinical parameters not mentioned before were not considered for this first approximation of creating a model able to classify the response of RA patients to DMARD treatment.

Model Building

Data were preprocessed and analysed using R Software (version 3.5.1; https://www.r-project.org/) and RStudio environment (version 1.1.456; https://www.rstudio.com/).

From the exploratory analysis, two samples were removed for showing outlier concentrations of TXB2, which likely reflected coagulation during sample collection and an additional sample was removed due to lack of clinical records. Although no normalization was required since all the lipid mediator concentrations were calculated based on the same amount of standard, the concentrations were scaled by subtracting the mean and dividing by the standard deviation of each feature.

Two supervised machine learning methodologies were used to create the classifier models: classyfire (Chatzimichali, E. A. & Bessant, C. “Novel application of heuristic optimisation enables the creation and thorough evaluation of robust support vector machine ensembles for machine learning applications”. Metabolomics 12, 16 (2016), the contents of which are incorporated herein by reference) and randomForest (Breiman, L. Classification and Regression Trees, (Routledge, 2017), the contents of which are incorporated herein by reference). Classyfire uses Support Vector Machine (SVM) to separate groups by organizing the samples in two spaces divided by a hyperplane in a way that the distances between the samples in the same group are not too wide and the distance between the groups is as large as possible (Bennett, K. P. & Campbell, C. “Support vector machines.” ACM SIGKDD Explorations Newsletter 2, 1-13 (2000), the contents of which are incorporated herein by reference). Besides that, it uses bootstrapping (new datasets created by iteratively resampling of the original data with replacement) to improve and validate the models. In this study, classyfire was implemented using the R Package “classyfire” (https://crans-project.org/src/contrib/Archive/classyfire/), with 70 bootstrap iterations and 70 individual classifiers in each ensemble. We also used the inbuilt automatic optimization step that includes minimization of the bootstrapping error 36 in the R Package “classyfire” to improve and validate the models (see FIG. 13 for representative outcomes).

Random forests operates by getting the consensus of weak decision tree classifiers (Han, T., Jiang, D., Zhao, Q., Wang, L. & Yin, K. “Comparison of random forest, artificial neural networks and support vector machine for intelligent diagnosis of rotating machinery.” Transactions of the Institute of Measurement and Control 40, 2681-2693 (2018), the contents of which are incorporated herein by reference). The decision trees are created using the features as vertices and classes as leaves; each tree is designed using a different set of randomly chosen features (Lötsch, J., et al. “Machine-learning based lipid mediator serum concentration patterns allow identification of multiple sclerosis patients with high accuracy.” Sci. Rep. 8, 14884 (2018), the contents of which are incorporated herein by reference). In this case, the R package “randomForest” (https://crans-project.org/package=randomForest) (which also uses bootstrapping as the validation method) was used with a parameters setting of 10,000 trees per run and the design of a small loop to define the best number of variables randomly sampled as candidates at each split. Increasing the number of ntrees beyond this value did not markedly improve the outcomes (see FIG. 13 for representative outcomes).

Model Testing

Receiver operating characteristic curves (ROC curves) were built to evaluate the prediction accuracy of the models when predicting between DMARDs responder and DMARDs non-responder in a test dataset. ROC curves are created by plotting the true positive rate against the false positive rate, showing the sensitivity and specificity of the model, when the discrimination threshold changes. The area under the curve (AUC) is calculated as the prediction performance of the models. ROC curves were created using the R package “pROC” (https://cran.r-project.org/web/packages/pROC/index.html). AUC values close to 1 (AUC>0.8) refer to good classifier models.

Receiver operating characteristic curves (ROC curves) were built to evaluate the prediction accuracy of the models when predicting between DMARDs responder and DMARDs non-responder in a test dataset. ROC curves are created by plotting the true positive rate against the false positive rate, showing the sensitivity and specificity of the model, when the discrimination threshold changes. The area under the curve (AUC) is calculated as the prediction performance of the models. ROC curves were created using the R package “pROC” (https://cran.r-project.org/web/packages/pROC/index.html). AUC values close to 1 (AUC>0.8) refer to good classifier models. Alongside ROC curves, other statistics such as the percentage of correctly classified samples (% accuracy score), specificity and sensitivity were also calculated.

Feature Selection and Model Improvement

As random forests showed the best validation scores during the testing step, the model improvement was based on the random forests methodology. The lipid mediators were separated in groups based on their precursors (DHA, n-3 DPA, EPA and AA) or the distinct clusters of mediators. Besides that, and using the “importance” function of randomForest, which organizes the model's features by relevance based on the decrease of the mean accuracy of the model when the specific feature is not present, different models were created using only the most relevant lipid mediators. The % accuracy score and MCC were calculated for all the models and, according to the results, the best models and the most relevant biomarkers for the classification of the DMARD-responder and DMARD-non-responder patients were selected.

Pathotypes Analyses

All the data (training and validation cohorts) was separated based on the specific pathotype shown for the patients: pauci-immune/fibroid (n=28), lympho-myeloid (n=27) and diffuse-myeloid (n=31). This was made with the purpose of seeking better classification models and seeing if specific lipid mediators were responsible for the different manifestation of the disease. The models were build using randomForest and different statistic scores were calculated for the validation of each model.

Network Analyses

Statistical differences between the normalised concentrations (expressed as the fold change) of the lipid mediators from the DMARD-non-responder and DMARD-responder groups were determined using a student t-test followed by a multiple comparison correction using Benjamini-Hochberg procedure. Based on these differences, lipid mediator biosynthesis networks were constructed using Cytoscape 3.7.1. The different pathways were illustrated using different colours and line shapes, while up or down regulated mediators were denoted with diamond or triangle shapes, respectively, and on changes of the node's size. Bolded mediators represent statistical differences between the two groups. The comparison between DMARD-non-responders and DMARD-responders were made with pre and post-treatment data.

Targeted Lipid Mediator Profiling

Plasma was obtained from peripheral blood of healthy volunteers, patients and mouse following centrifugation at 1500×g for 10 min at room temperature. Paws were collected and immediately transferred to liquid nitrogen prior to homogenization in 1 ml ice cold MeOH and homogenized using a glass dounce. All samples for LC-MS/MS-based profiling were extracted using solid-phase extraction columns as in Walker, M. E., Souza, P. R., Colas, R. A. & Dalli, J. “13-Series resolvins mediate the leukocyte-platelet actions of atorvastatin and pravastatin in inflammatory arthritis.” FASEB J 31, 3636-3648 (2017), the contents of which are incorporated herein by reference. Prior to sample extraction, deuterated internal standards, representing each region in the chromatographic analysis (500 pg each) were added to facilitate quantification. Samples were kept at −20° C. for a minimum of 45 min to allow protein precipitation. Supernatants were subjected to solid phase extraction, methyl formate fraction collected, brought to dryness and suspended in phase (methanol/water, 1:1, vol/vol) for injection on a Shimadzu LC-20AD HPLC and a Shimadzu SIL-20AC autoinjector, paired with a QTrap 5500 or QTrap 6500 plus (Sciex). An Agilent Poroshell 120 EC-C18 column (100 mm×4.6 mm×2.7 μm) was kept at 50° C. and mediators eluted using a mobile phase consisting of methanol/water/acetic acid of 20:80:0.01 (vol/vol/vol) that was ramped to 50:50:0.01 (vol/vol/vol) over 0.5 min and then to 80:20:0.01 (vol/vol/vol) from 2 min to 11 min, maintained till 14.5 min and then rapidly ramped to 98:2:0.01 (vol/vol/vol) for the next 0.1 min. This was subsequently maintained at 98:2:0.01 (vol/vol/vol) for 5.4 min, and the flow rate was maintained at 0.5 ml/min. QTrap 5500 or QTrap 6500 plus were operated using a multiple reaction monitoring method as in Walker, M. E., Souza, P. R., Colas, R. A. & Dalli, J. “13-Series resolvins mediate the leukocyte-platelet actions of atorvastatin and pravastatin in inflammatory arthritis.” FASEB J 31, 3636-3648 (2017), the contents of which are incorporated herein by reference. Each lipid mediator was identified using established criteria including matching retention time to synthetic or authentic standards and at least 6 diagnostic ions (Walker, M. E., Souza, P. R., Colas, R. A. & Dalli, J. “13-Series resolvins mediate the leukocyte-platelet actions of atorvastatin and pravastatin in inflammatory arthritis.” FASEB J 31, 3636-3648 (2017), the contents of which are incorporated herein by reference). Calibration curves were obtained for each mediator using lipid mediator mixtures at 0.78, 1.56, 3.12, 6.25, 12.5, 25, 50, 100, and 200 μg that gave linear calibration curves with an r2 values of 0.98— 0.99.

Healthy Volunteer's Blood Collection

Venous peripheral blood was collected at indicated intervals in sodium citrate (3.2%) from fasting volunteers that declared not taking NSAIDS for at least 14 days, caffeine and alcohol for at least 24 h and fatty fish for 48 h. Volunteers gave written consent in accordance with a Queen Mary Research Ethics Committee (QMREC 2014:61) and the Helsinki declaration.

Human Whole Blood Incubations

In select experiments, whole blood was incubated with L002 (2 μM) or SB202190 (5 μM) or vehicle (0.1% DMSO) for 45 min (37° C.). Blood was then incubated with MTX (100 nM) for 45 min (37° C.). Plasma was then separated by centrifugation at 1,500×g for 10 min for lipid mediators profiling.

Animals

Male C57BL/6 mice and Alox15−/− (11-week-old) were procured from Charles River Laboratories (Kent, United Kingdom). Experiments strictly adhered to United Kingdom Home Office regulations (Guidance on the Operation of Animals, Scientific Procedures Act) and Laboratory Animal Science Association Guidelines (Guiding Principles on Good Practice for Animal Welfare and Ethical Review Bodies). All animals were provided with standard laboratory diet and water ad libitum and kept on a 12-h light/dark cycle.

Inflammatory Arthritis

Male C57BL/6 mice and Alox15−/− (11-week-old) were administered K/BxN serum (100 μl, i.p.) on day 0 and day 2 to initiate inflammatory arthritis. Mice were then given MTX (25 mg/kg each), or vehicle (DPBS−/− that contained 1% DMSO) via intraperitoneal injection on days 3, 5, and 7. Clinical scores were monitored daily by using a 26-point arthritic scoring system. Swelling and redness of mouse ankles/wrists, pads, and digits were inspected daily. Blood and paws were collected on day 8.

In select experiments, male C57BL/6 mice (11-week-old) were given L002 (20 mg/kg each) or SB202190 (20 mg/kg each) before MTX injections. Clinical scores were monitored daily by using a 26-point arthritic scoring system. Swelling and redness of mouse ankles/wrists, pads, and digits were inspected daily. Blood and paws were collected on day 8 after arthritis onset.

Enzyme Transcript Expression

RNA was extracted from whole blood samples in RNALater solution using the Ambion Ribo-Pure Blood kit (ThermoFisher Scientific). Total RNA-Sequencing (RNA-seq) was performed on an IIlumina HiSeq2500 platform. Raw data were quality-controlled using FastQC, trimmed or removed with Cutadapt. Transcript abundance was derived from paired sample FASTQ files over GENCODE v24/GRCh38 transcripts using Kallisto v0.43.0. Normalization of the raw data and differential gene expression analysis between DMARD-responder and DMARD-non-responder were performed using the quasi-likelihood method of the Bioconductor R package “edgeR” (https://bioconductor.org/packages/release/bioc/html/edgeR.html). Results are expressed as the log counts per million of each gene. RNA-Seq data are uploaded to ArrayExpress and are accessible via accession E-MTAB-6141.

Flow Cytometry

Paws were harvested and leukocytes were isolated as previously described (Norling, L. V., et al. “Proresolving and cartilage-protective actions of resolvin D1 in inflammatory arthritis.” JCI Insight 1, e85922 (2016), the contents of which are incorporated herein by reference). In brief, paws were incubated in RPMI-1640 that contained 0.5 μg/ml collagenase D and 40 μg/ml DNaseI at 37° C. for 30 min with vigorous agitation. Isolated cells were passed through a 70-μM strainer and suspended in RPMI-1640 that contained 2 U/ml penicillin, 100 mg/ml streptomycin, and 10% fetal bovine serum, then centrifugated at 400 g for 10 min. Isolated cells were suspended in DPBS−/− that contained 0.02% bovine serum albumin and 1% Fc-blocking IgG (v/v) and were incubated with 0.1% live/dead stain for 20 min on ice. Cells were washed using DPBS−/− and incubated with the following antibodies: PE CD64 (FcγRI, clone X54-5/7.1, host mouse, Biolegend), Alexa Fluor 700 Ly-6G (clone 1A, host rat, Biolegend), Brilliant Violet 785 Ly-6C (clone HK1.4, host rat, Biolegend), APC/Cyanine7 CD45 (clone 30-F11, host rat, Biolegend), Alexa Fluor 488 CD11 b (clone M1/70, host rat, Biolegend), APC Siglec F (clone ES22-10D8, host rat, Miltenyi Biotec), Brilliant Violet 711 CD115 (CSF-1R) (clone AFS98, host rat, Biolegend) and Brilliant Violet 510 CD43 (clone 1G10, host mouse, BD Biosciences) for 45 min on ice. These were then washed and fixed using 1% paraformaldehyde. CountBright Absolute Counting Beads were used for leukocyte enumeration. Staining was evaluated using LSRFortessa cell analyzer and analyzed using FlowJo software.

Histology

Paws were placed in 10% formaldehyde (v/v; in water that contained 0.65% Na2HPO4 and 0.4% NaH2PO4) for 48 h. These were then placed in 10% EDTA in DPBS for 2 wk. When decalcified, paws were embedded in wax as previously described (Walker, M. E., Souza, P. R., Colas, R. A. & Dalli, J. “13-Series resolvins mediate the leukocyte-platelet actions of atorvastatin and pravastatin in inflammatory arthritis.” FASEB J 31, 3636-3648 (2017), the contents of which are incorporated herein by reference). Four-micron sections were obtained and hematoxylin and eosin staining was carried out by the Barts Cancer Institute Pathology Core as described in Walker, M. E., Souza, P. R., Colas, R. A. & Dalli, J. “13-Series resolvins mediate the leukocyte-platelet actions of atorvastatin and pravastatin in inflammatory arthritis.” FASEB J 31, 3636-3648 (2017), the contents of which are incorporated herein by reference.

Statistical Analysis

We performed all statistical analyses and data derivation using R (R Development Core Team. R: A language and environment for statistical computing. (2016), the contents of which are incorporated herein by reference), MetaboAnalyst 4.0 (Chong, J., Yamamoto, M. & Xia, J. MetaboAnalystR 2.0: “From Raw Spectra to Biological Insights.” Metabolites 9 (2019), the contents of which are incorporated herein by reference), Prism 8 and Microsoft Excel. Results presented in the figures are expressed as means and those displayed in the tables are displayed as mean±sem. Differences between groups were determined using one-sample T test (normalized data) or Mann Whitney test (2 groups) or one-way ANOVA (more than 2 groups). Sample sizes for each experiment were determined on the variability observed in prior experiments. Partial least squares-discrimination analysis (PLS-DA) and Orthogonal Partial least squares-discrimination analysis (OPLS-DA) were performed using MetaboAnalyst 4.0 Chong, J., Yamamoto, M. & Xia, J. MetaboAnalystR 2.0: “From Raw Spectra to Biological Insights.” Metabolites 9 (2019), the contents of which are incorporated herein by reference) or SIMCA 14.1 software (Umetrics, Umea, Sweden) after mean centering and unit variance scaling of lipid mediator concentrations. PLS-DA is based on a linear multivariate model that identifies variables that contribute to class separation of observations (e.g. treatment response) on the basis of their variables (lipid mediator concentrations). During classification, observations were projected onto their respective class model. The score plot illustrates the systematic clusters among the observations (closer plots presenting higher similarity in the data matrix).

