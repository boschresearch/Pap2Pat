# Introduction

The rapid growth of nanotechnology has led to the development of new sensing devices of micrometer size coined as microsensors. These devices can be used to detect, measure, analyze, and economically monitor low concentrations of chemical and biological agents. The monitoring of a specific substance is pivotal in many applications, especially for clinical purposes in order to screen a patient for the presence of a disease at an early stage [1]. Microcantilever-based microsensors have been proven to be very sensitive and accurate [1]. The changes in the physical properties of the microcantilever are considered to indicate or detect changes in the environment surrounding it [2,3]. These changes can for example be measured using electric signals with piezoressitive microcantilevers [2–4]. They can also be gauged by monitoring the tip deflection of the microcantilevers [5–7]. The deflection of the microcantilever was first used for atomic force microscopy [5]. Moreover, the changes in the physical properties of the microcantilever are widely used to indicate the presence or absence of a certain analyte [8–11].

The magnitude of microcantilever deflection is of the order of nanomenters and it is usually measured using optical methods. The performance of the microcantilever as a sensing device is affected by the noise level in the surrounding environment. For example, Fritz et al. [12] reported that the microcantilever deflection due to flow disturbances and due to thermal effects could reach 5–10 times that due to analyte sensing. Accordingly, further developments in microcantilever technology are necessary in order to magnify the deflection signal due to the sensing effect so that its signal can be easily distinguished from the noise signal [13–16]. As such, Khaled et al. [2] pointed out the necessity of establishing special microcantilevers assemblies for this purpose. Many of these assemblies were patented [14,17]. It should be noted that additional novel methods for magnifying the deflection signal due to analyte sensing were proposed [18–21]. Some of these methods are based on controlling both the geometry of the fluidic cell incubating the microcantilevers and their geometrical distribution. An interesting assembly among the assemblies described in the work of Khaled et al. [2] is the ɛ-microcantilever assembly. The deflection due to analyte sensing of ɛ-microcantilever assembly is estimated to be double that of the rectangular microcantilever [2]. As such, this assembly is considered to be highly important for the present work.

In this work, the advantage of utilizing microcantilever assemblies including the ɛ-assembly established by Khaled et al. [2] in microsensing applications is explored theoretically. Various force loading conditions that can produce noticeable deflections such as the concentrated force, moment and constant surface stress which can be due to analyte adhesion are considered. The linear elasticity theory for thin beams [22] is used to obtain the deflections. Different deflection indicators are defined and various controlling variables are identified. The performance of different microcantilever assemblies is compared with the performance of rectangular microcantilevers in order to map out conditions that produce magnification of the sensing deflection relative to the noise deflection.

# Theoretical Analysis

## Microcantilevers With One Piece (Rectangular Microcantilevers)

The geometry of the rectangular microcantilever considered in this section is shown in Figure 1(a). The properties of the rectangular microcantilever can be summarized by specifying the extension length L, width W, thickness t, Young’s modulus E and Poisson’s ratio ν. When the length of the microcantilever is much larger than its width, Hooks law for small deflections can be used to relate the microcantilever deflections to the effective elastic modulus Y and the bending moment M [22]. It is given by: \(\frac{d^{2}z}{dx^{2}} = \frac{M}{\text{YI}}\) where z is the deflection the microcantilever at any section located at a position x from the base surface. I is the area moment of inertia of the microcantilever cross-section about its neutral axis. For a rectangular cross-section with its neutral axis coinciding with its centroidal axis, I is given by: \(I = \frac{1}{12}\mathit{Wt}^{3}\)

The boundary conditions for Equation (1) are given by: \(z{({x = 0})} = \left. \frac{\mathit{dz}}{\mathit{dx}} \right|_{x = 0} = 0\)

For a concentrated force exerted on the rectangular microcantilever tip (x = L), the solution of Equation (1), denoted by zaF(x), subject to boundary conditions given by Equation 3(a,b) can be expressed as: \(z_{\mathit{aF}}~{(x)} = \left( \frac{6\mathit{FL}^{3}}{\mathit{EWt}^{3}} \right)\left\lbrack {\left( \frac{x}{L} \right)^{2} - \frac{1}{3}\left( \frac{x}{L} \right)^{3}} \right\rbrack\)

The above result is based on a realistic linearly increasing bending moment from the base prescribed by: \(M = \mathit{FL}\left( {1 - \frac{x}{L}} \right)\)

For thin cross-sections, the surface stress, σ, can be calculated from the following equation: \(\sigma = \frac{M}{I}\left( \frac{t}{2} \right)\)

The surface stress at x = 0 (base surface) denoted by σaFo is equal to: \(\sigma_{\mathit{aFo}} = \frac{6\mathit{FL}}{\mathit{Wt}^{2}}\)

The maximum deflection which occurs at the microcantilever tip (x = L) can be expressed as: \(z_{\mathit{aF}~\mathit{\max}} = \frac{4\mathit{FL}^{3}}{\mathit{EWt}^{3}}\)

For a bending moment M exerted on the rectangular microcantilever tip (x = L), the solution of Equation (1), denoted by zaM(x), subject to boundary conditions given by Equation 3(a,b) is the following: \(z_{\mathit{aM}}~{(x)} = \left( \frac{6\mathit{ML}^{2}}{\mathit{EWt}^{3}} \right)\left( \frac{x}{L} \right)^{2}\)

The surface stress at the base section which is denoted by σaMo is equal to: \(\sigma_{\mathit{aMo}} = \frac{6M}{\mathit{Wt}^{2}}\)

The maximum deflection which is the deflection at the microcantilever tip is equal to: \(z_{\mathit{aM}~\mathit{\max}} = \frac{6\mathit{ML}^{2}}{\mathit{EWt}^{3}}\)

When the microcantilever is coated on one side with a thin film of receptor, it is usually bent due to analyte adhesion on that layer. This adhesion causes a differential in the surface stress across the microcantilever section yielding a bending moment at each section. The bending moment M [2,22] is given by: \(M = \frac{\Delta\sigma\mathit{Wt}}{2}\) where Δσ is the difference between the surface stresses of the top and bottom sides of the microcantilever. The solution of Equation (1), denoted by zaΔσ(x), subject to boundary conditions given by Equation 3(a,b) can then be expressed as: \(z_{a\Delta\sigma}~{(x)} = \frac{6{({1 - \nu})}\Delta\sigma_{o}L^{2}}{\mathit{Et}^{2}{({n + 1})}{({n + 2})}}\left( \frac{x}{L} \right)^{n + 2}\)

This is because the effective elastic modulus for this case is given by Y = E/(1−v). Also, Δσ is considered to vary along the microcantilever length according to the following relationship: \(\Delta\sigma = {\Delta\sigma}_{o}\left( \frac{x}{L} \right)^{n}\) where n is the model index. This variation is expected as analyte concentration in the surrounding environment is expected to increase as the distance from the microcantilever base increases. The maximum deflection due to analyte adhesion is obtained from Equation (13) by substituting x = L. It is equal to: \(z_{a\Delta\sigma~\mathit{\max}}~{(x)} = \frac{6{({1 - \nu})}{\Delta\sigma}_{o}L^{2}}{\mathit{Et}^{2}{({n + 1})}{({n + 2})}}\)

Equation (15) is reducible to Stoney’s equation when n is set to be equal to zero.

## Microcantilevers With More Than One Piece (Mc Assemblies)

### The Microcantilever Assembly (B)

The geometry of the microcantilever assembly (b) is shown in Figure 1(b). Equation (1) is changeable to the following when the center line of the free end (x = L) is loaded by a normal concentrated force of magnitude F: \(\frac{d^{2}z_{\mathit{bF}}}{\mathit{dx}^{2}} = \left( \frac{3\mathit{FL}}{\mathit{EWt}^{3}} \right) \times {{2{({1 - {x/L}})}}/{\mathit{\cos}^{3}{(\theta)}}}\)

Note that I for each beam is I = Wt3/12. Note that θ is half the triangular tip angle. The cosine of the angle θ is given by: \(\mathit{\cos}{(\theta)} = \left\lbrack {1 + 0.25\left\lbrack \frac{B/L}{1 - 0.5{({W/L})}} \right\rbrack^{2}} \right\rbrack^{- 1/2}\)

The boundary conditions for Equation (16) are given by: \(z_{b}~{({x = 0})} = \left. \frac{\mathit{dz}_{b}}{\mathit{dx}} \right|_{x = 0} = 0\)

The solution of Equation (16), denoted by zbF(x), subject to the above boundary conditions is the following: \(z_{\mathit{bF}}~{(x)} = \left( \frac{3\mathit{FL}^{3}}{\mathit{EWt}^{3}} \right)\left\lbrack {\left( \frac{x}{L} \right)^{2} - \frac{1}{3}\left( \frac{x}{L} \right)^{3}} \right\rbrack\left( \frac{1}{\mathit{\cos}^{3}{(\theta)}} \right)\)

Using Equation (6), the surface stress at x = 0, σbFo, is equal to: \(\sigma_{\mathit{bFo}} = \left( \frac{3\mathit{FL}}{\mathit{Wt}^{2}} \right)\left\lbrack \frac{1}{\mathit{\cos}{(\theta)}} \right\rbrack\)

The maximum deflection occurs at the tip (x = L). It is equal to: \(z_{\mathit{bF}~\mathit{\max}} = \left( \frac{3\mathit{FL}^{3}}{\mathit{EWt}^{3}} \right)\left\{ \frac{2}{3~\mathit{\cos}^{3}{(\theta)}} \right\}\)

For a bending moment M about x-axis exerted on the center line of the free end of the assembly (b) (at x = L), Equation (1) is changeable to the following form: \(\frac{d^{2}z_{\mathit{bM}}}{\mathit{dx}^{2}} = \left( \frac{3M}{\mathit{EWt}^{3}} \right) \times {2/{\mathit{\cos}{(\theta)}}}\)

The solution of Equation (22), subject to boundary conditions given by Equation 18(a,b) is the following: \(z_{\mathit{bM}}~{(x)} = \left( \frac{3\mathit{ML}^{2}}{\mathit{EWt}^{3}} \right)\left( \frac{x}{L} \right)^{2}\left\lbrack \frac{1}{\mathit{\cos}{(\theta)}} \right\rbrack\)

As such, the maximum deflection is expected to be equal to: \(z_{\mathit{bM}~\mathit{\max}} = \left( \frac{3\mathit{ML}^{2}}{\mathit{EWt}^{3}} \right)\left\{ \frac{1}{\mathit{\cos}{(\theta)}} \right\}\)

Using Equation (6), the surface stress at x = 0, σcMo, is equal to: \(\sigma_{\mathit{bMo}} = \frac{3M}{\mathit{Wt}^{2}}\mathit{\cos}{(\theta)}\)

When a receptor layer is coated on one side of assembly (b)-side beams (SB), Equation (1) changes to the following form after the analyte adhesion on these coatings: \(\frac{d^{2}z_{b\Delta\sigma}}{\mathit{dx}^{2}} = \left\{ \frac{6{({1 - \nu})}{\Delta\sigma}_{o}}{\mathit{Et}^{2}} \right\} \times {\left( {x/L} \right)^{n}/{\mathit{\cos}^{2}{(\theta)}}}\)

The solution of Equation (26), subject to boundary conditions given by Equation 18(a,b) is the following: \(z_{b\Delta\sigma}~{(x)} = \left\{ \frac{6{({1 - \nu})}{\Delta\sigma}_{o}L^{2}}{\mathit{Et}^{2}{({n + 1})}{({n + 2})}} \right\}\left( \frac{x}{L} \right)^{n + 2}\left\lbrack \frac{1}{\mathit{\cos}^{2}{(\theta)}} \right\rbrack\)

The maximum deflection due to analyte adhesion is then equal to: \(z_{b\Delta\sigma~\mathit{\max}} = \left\{ \frac{6{({1 - \nu})}{\Delta\sigma}_{o}L^{2}}{\mathit{Et}^{2}} \right\}\left\{ \frac{1/{\mathit{\cos}^{2}{(\theta)}}}{{({n + 1})}{({n + 2})}} \right\}\)

Define the first deflection indicator γpU as the ratio of the microcantilever deflection at the tip (x = L) per surface stress at the base for the microcantliever of type (p) due to force loading of type U to the corresponding value for the rectangular microcantilever. The type (p) can be either the microcantilever of type (b) and (c) as shown in Figure 1. The force loading of type U can be either concentrated force loading (F), external bending moment (M) or constant surface stress (Δσo). As such, γbF, γbM and γbΔσo are equal to: \(\gamma_{\mathit{bF}} = {1/{\mathit{\cos}^{3}~{(\theta)}}}\)  \(\gamma_{\mathit{bM}} = \frac{1}{\mathit{\cos}^{2}~{(\theta)}}\)  \(\gamma_{{b\Delta\sigma}_{o}} = {1/{\mathit{\cos}^{2}~{(\theta)}}}\)

### The Microcantilever Ɛ-Assembly (Assembly C)

The geometry of the microcantilever assembly (c) is shown in Figure 1(c). Let the centerline of the assembly free end (x = L) to be loaded by a normal concentrated force of magnitude F. And Let the free end of the intermediate beam (IB) be loaded by the negative of the previous load (−F). Accordingly, Equation (1) changes to the following: \(\frac{d^{2}z_{\text{cF}}}{\text{dx}^{2}} = \left( \frac{3FL}{\text{EWt}^{3}} \right) \times \left\lbrack \begin{matrix} {{2/{\text{cos}\left( \theta \right)}},~{(\text{for SB})}} \\ {- 4{({x/L})},~{(\text{for IB})}} \end{matrix} \right.\) where SB stands for the side beams of the assembly. The boundary conditions of Equation (30) are given by: \(z_{\mathit{cSB}}~{({x = 0})} = \left. \frac{\mathit{dz}_{\mathit{cSB}}}{\mathit{dx}} \right|_{x = 0} = 0\)  \(z_{\mathit{cSB}}~{({x = L})} = z_{\mathit{cIB}}~{({x = L})}\)  \(\left. \frac{\mathit{dz}_{\mathit{cSB}}}{\mathit{dx}} \right|_{x = L} = \left. \frac{\mathit{dz}_{\mathit{cIB}}}{\mathit{dx}} \right|_{x = L}\)

The solution of Equation (30), denoted by zcF (x), is equal to: \(z_{\mathit{cSBF}}~{(x)} = \left( \frac{3\mathit{FL}^{3}}{\mathit{EWt}^{3}} \right)\left( \frac{x}{L} \right)^{2}\left\lbrack \frac{1}{\mathit{\cos}{(\theta)}} \right\rbrack\)  \(z_{\mathit{cIBF}}~{(x)} = \left( \frac{3\mathit{FL}^{3}}{\mathit{EWt}^{3}} \right)\left\{ {- \left( \frac{2}{3} \right)\left( \frac{x}{L} \right)^{3} + 2\left( {\frac{1}{\mathit{\cos}{(\theta)}} + 1} \right)\left( \frac{x}{L} \right) + D_{1}} \right\}\) where D1 is equal to: \(D_{1} = - \left\{ {\frac{1}{\mathit{\cos}{(\theta)}} + \frac{4}{3}} \right\}\)

The surface stress at the base section σcFo is equal to: \(\sigma_{\mathit{cFo}} = \left( \frac{3\mathit{FL}}{\mathit{Wt}^{2}} \right)\mathit{\cos}{(\theta)}\)

Define the second deflection indicator λcU as the ratio of the IB-free end deflection zcIBU (x = 0) to that at the assembly free end zcU (x = L) due to force loading of type U. The force loading of type U can be either the current described force loading (F), external bending moment loading (M) or the constant surface stress (Δσo) loading. The last two types of force loadings will be described later on. As such, λcF is equal to: \(\lambda_{\mathit{cF}} = \frac{\mathit{zc}_{\mathit{cIBF}}~{({x = 0})}}{z_{\mathit{cF}}~{({x = L})}} = - \left\{ {1 + \frac{4}{3}\mathit{\cos}{(\theta)}} \right\}\)

Now, let a bending moment M be exerted on the assembly (c) free end centerline. And let another bending moment of same magnitude be exerted on the IB-free end at x = 0. The deflection equations for this assembly under the current moments loading is given by the following: \(\frac{d^{2}z_{\text{cM}}}{\text{dx}^{2}} = \left( \frac{6M}{\text{EWt}^{3}} \right) \times \left\lbrack \begin{matrix} {{2/{\text{cos}\left( \theta \right)}},\quad\left( \text{for SB} \right)} \\ {- 2,\quad\quad\quad\left( \text{for IB} \right)} \end{matrix} \right.\)

The boundary conditions are given by Equations 31(a–c). The solution of Equation (35) is given by: \(z_{\mathit{cSBM}}~{(x)} = \frac{1}{\mathit{\cos}{(\theta)}}\left( \frac{6\mathit{ML}^{2}}{\mathit{EWt}^{3}} \right)\left( \frac{x}{L} \right)^{2}\)  \(z_{\mathit{cIBM}}~{(x)} = \left( \frac{6\mathit{ML}^{2}}{\mathit{EWt}^{3}} \right)\left\{ {- \left( \frac{x}{L} \right)^{2} + 2\left( {\frac{1}{\mathit{\cos}{(\theta)}} + 1} \right)\left( \frac{x}{L} \right) + D_{2}} \right\}\) where D2 is equal to: \(D_{2} = - \left\lbrack {\frac{1}{\mathit{\cos}{(\theta)}} + 1} \right\rbrack\)

The surface stress at x = 0, σcMo, is equal to: \(\sigma_{\mathit{cMo}} = \frac{6M}{\mathit{Wt}^{2}}\mathit{\cos}{(\theta)}\)

The second deflection indicator for assembly (c) for the current moments loading λcM is equal to: \(\lambda_{\mathit{cM}} = \frac{z_{\mathit{cIBM}}~{({x = 0})}}{z_{\mathit{cM}}~{({x = L})}} = - \left\lbrack {\mathit{\cos}{(\theta)} + 1} \right\rbrack\)

If the top surfaces of the side beams of assembly (c) are coated with a receptor while the receptor coating on the intermediate beam is on its bottom surface, then the deflection equations of assembly (c) changes to: \(\mathit{\cos}^{2}{(\theta)} \times \frac{d^{2}z_{\mathit{cSB}\Delta\sigma}}{\mathit{dx}^{2}} = - \frac{d^{2}z_{\mathit{cIB}\Delta\sigma}}{\mathit{dx}^{2}} = \frac{6{({1 - \nu})}{\Delta\sigma}_{o}}{\mathit{Et}^{2}}\left( \frac{x}{L} \right)^{n}\)

The solution for Equation (39) subject to boundary conditions given by Equation 31(a–c) is equal to: \(z_{\mathit{cSB}\Delta\sigma}~{(x)} = \left\{ \frac{6{({1 - \nu})}{\Delta\sigma}_{o}L^{2}}{E{({n + 1})}t^{2}} \right\}\left( \frac{x}{L} \right)^{n + 2}\left\{ \frac{1/{\mathit{\cos}^{2}{(\theta)}}}{n + 2} \right\}\)  \(z_{\mathit{cIB}\Delta\sigma}~{(x)} = \left\{ \frac{6{({1 - \nu})}{\Delta\sigma}_{o}L^{2}}{E{({n + 1})}t^{2}} \right\}\left\{ {\frac{- 1}{({n + 2})}\left( \frac{x}{L} \right)^{n + 2} + \left\lbrack {1 + \frac{1}{\mathit{\cos}^{2}{(\theta)}}} \right\rbrack\left\lbrack {\frac{x}{L} - \frac{n + 1}{n + 2}} \right\rbrack} \right\}\)

The deflection indicator for assembly (c) due to the alternating analyte adhesion on the surfaces λcΔσ is equal to: \(\lambda_{c\Delta\sigma} = \frac{z_{\text{cIB}\Delta\sigma}~{({x = 0})}}{z_{\text{cSB}\Delta\sigma}~{({x = L})}} = - {({n + 1})}\left\lbrack {\text{cos}^{2}{(\theta)} + 1} \right\rbrack\)

The deflection indicators γcF, γcM and γcΔσo can be shown to be equal to the following: \(\gamma_{\mathit{cF}} = {1.5/{\mathit{\cos}^{2}{(\theta)}}}\)  \(\gamma_{\mathit{cM}} = {1/{\mathit{\cos}^{2}{(\theta)}}}\)  \(\gamma_{{c\Delta\sigma}_{o}} = {1/{\mathit{\cos}^{2}{(\theta)}}}\)

# Results And Discussion

## Validation Of The Results

The present analytical methods were tested against an accurate numerical solution using finite element methods and accounting for all mechanical constraints induced by the assemblies. Among these constraints is restraining the wrapping of the side beams due to the presence of the small connecting beam at x = L. The deflection contours for assembly (c) with L = 385 μm, W = 30 μm and t = 20 nm under concentrated moment condition described in section 2.2.2 with M = 10−12 Nμm is shown in Figure 2. The microcantilever material was taken to be silicon with E = 0.185 Nμm−2 and a poisons ratio of ν = 0.33. The assembly deflection at x = L is equal to zcM (x = L) = 0.028 μm using Equation (36b). Also, the deflection at the intermediate beam’s free end can be shown to be equal to zcIBM (x = 0) = 0.048 μm. As can be seen from Figure 2, the corresponding numerical values of those deflections are equal to 0.026 μm and 0.045 μm, respectively. Notice that the maximum error between the numerical and the derived analytical solutions is less than 10 percent. Also, notice that the numerical values of deflections are smaller than those predicated by the analytical methods. This is because the geometrical constraints imposed on the assemblies impede the deflections. (Legand)

## Discussion Of The Results

### Discussion Of The Results Of First Performance Indicators

Figure 3 shows the variation of the performance indicators γbF and γcF with the relative dimensions of assemblies (b) and (c). It is noticed that all the values of γbF and γcF are larger than one which indicates that assemblies (b) and (c) produce larger deflections than rectangular microcantilevers under same surface stress at the base and same extension length L. Moreover, both indicators increase as both the microcantilever width W and the assembly width B increase. Similar findings are noticed for the performance indicators γbM, γcM, γbΔσ and γcΔσ as can be seen from Figures 4 and 5. On the other hand, an increase in B causes the effective free length of the assembly to increase, which makes the assembly more sensitive to external noises.

### Discussion Of The Results Of Second Performance Indicators

Figure 6 shows the variation of the second performance indicator λcF with the relative dimensions of assembly (c). It is noticed that all values of λcF are smaller than minus one. This indicates that IB-free end deflection is always larger than that of the assembly tip deflection. Moreover, the absolute value of λcF is noticed to increases as both W and B decreases. Similar findings are noticed for the performance indicators λcM and λcΔσ as can be seen from Figures 7 and 8. As a result, assembly (c) can provide larger deflections than assembly (b) while it is less affected by external noise. This is because its deflection increase as B decreases which results in a reduction of the assembly’s free length. Moreover, the absolute values of λcΔσ increases as n increases as can be shown using Equation (41). This indicates the advantage of assembly (c) in microsensing applications as compared to rectangular cantilevers or triangular cantilevers.

# Conclusions

A theoretical investigation on improving deflections of microcantilevers sensors is presented in this work based on analytical solutions. Three different mcirocantilevers were analyzed. These are: (a) the rectangular microcantilever, (b) the modified triangular microcantilever assembly, and (c) the ɛ-microcantilever assembly. The deflection theory of thin beams is utilized to obtain the deflection profile for each microcantilever. Different force loadings were considered including concentrated force, concentrated moment and constant surface stress. Different deflection indicators were defined and computed. It was found that both the modified triangular microcantilever assembly and the ɛ-microcantilever assembly produce larger deflections than the rectangular microcantilever under the same base surface stress and same extension length. The deflection of the former microcantilevers can be 280% and 425% above that of the rectangular microcantilever for concentrated moment and constant surface stress cases, respectively. In addition, the ɛ-microcantilever assembly was found to produce larger deflection than the triangular microcantilever assembly. The deflection of the ɛ-microcantilever intermediate free end may reach 200% above that of the triangular microcantilever assembly. It was found that deflection enhancement due to ɛ-microcantilever increases as the assembly free length decreases. The cited conclusions were found to be valid for the different force loading conditions. The analytical results were validated against an accurate numerical solution utilizing a finite element method. The analytical and numerical solutions were found to be in good agreement. Based on our analysis, the ɛ-microcantilever assembly was found to provide a superior and the best favorable high detection capability with the least susceptibility to external noise in microsensing applications. As such, it is recommended to experimentally test it to show whether detective potential of microsensors can be increased.

