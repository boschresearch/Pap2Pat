# DESCRIPTION

## TECHNICAL FIELD

The present invention relates to a method for temperature compensation in a sensor, a computation program for the method for temperature compensation, a computation processing device carrying out a computation process of the computation program, and a sensor that is subjected to the temperature compensation.

## BACKGROUND ART

A semiconductor pressure sensor conventionally includes a micro-cavity and a thin diaphragm that covers a surface of the micro-cavity, and serves as a pressure gauge by measuring a change in a resistance formed on a surface of the diaphragm resulting from deformation of the diaphragm caused by external pressure, or with another electrode provided on the opposite pole, measuring a change in the capacitance between the diaphragm and the counter electrode.

In a pressure sensor configured as described above, in cases where the inside of the cavity is vacuumed and sealed, the deformation of the diaphragm is caused by a difference between outside pressure and vacuum pressure. That is, the pressure sensor corresponds to an absolute pressure sensor. On the other hand, in cases where a gas of a certain pressure is sealed in the cavity, the deformation of the diaphragm is caused by a difference between the outside pressure and the pressure of the gas in the cavity. That is, the pressure sensor is a relative pressure sensor. Even though it suffers from difficulty in keeping the inside of the cavity in vacuum, the absolute pressure sensor with the inside of the cavity vacuumed and sealed advantageously facilitates temperature compensation for a pressure sensor because the effect of the temperature-dependent contraction of the internal gas is negligible. On the other hand, since the inside of the cavity is sealed in vacuum, the diaphragm is already significantly deformed under an outside pressure of, for example, 1 atm. Thus, for the pressure sensor used at about 1 atm, it is disadvantageously difficult to use a thinner diaphragm to increase pressure sensitivity.

On the other hand, as an example of the relative pressure sensor, a capacitive pressure sensor is well-known which has a diaphragm portion that is deformable depending on pressure, which is a type of physical quantity, as typified by Patent Literature 1. Patent Literature 1 discloses a capacitive pressure sensor including a sensor chip having a first substrate with an electrode portion formed thereon and a second substrate with a diaphragm portion that is deformable depending on pressure formed thereon, a cavity portion formed in such a way that the diaphragm portion is associated with the electrode portion so as to face each other via a gap, and a sealing material externally sealing the cavity portion, the first substrate and the second substrate being bonded together, a gap width of the gap being changed depending on a difference between a pressure to be measured applied to the diaphragm portion and a pressure in the cavity portion so that the pressure difference is detected based on a change in the capacitance between the diaphragm portion and the electrode portion caused by the change in the gap width, wherein the capacitive pressure sensor further has a closure member that closes an inside of the cavity portion.

## SUMMARY OF INVENTION

### Technical Problem

The relative pressure sensor has an advantage in particular when outside air of about 1 atm is to be measured with a gas of about 1 atm sealed in the cavity. In this case, since the difference in pressure between the sealed gas and the outside air is small and the deformation of the diaphragm is insignificant, a thinner diaphragm can be provided, enabling an increase in sensitivity at about 1 atm. However, disadvantageously, since a gas is sealed in the cavity, a change in the temperature in the cavity varies the internal pressure, hindering deformation associated with the temperature of the diaphragm from being compensated for, as defined by the combined gas law.

Thus, an object of the present invention is to provide a method for temperature compensation in a sensor, a computation program for the method for temperature compensation, a computation processing device carrying out a computation process of the computation program, and a sensor in which optimum temperature compensation can be achieved by cancelling out deformation of a diaphragm caused by a change in pressure associated with the temperature of a gas in the cavity (thermal expansion of the gas sealed in the cavity) to suppress the deformation of the diaphragm within an intended temperature range.

### Solution to Problem

(1) The present invention provides a method for temperature compensation in a sensor including a substrate with a first electrode portion formed on one surface, a conductive portion formed on the one surface of the substrate via an insulator layer, a diaphragm portion formed on a surface of the conductive portion opposite to the surface of the conductive portion on which the insulator layer is formed, the diaphragm portion being deformable depending on pressure, and a temperature compensation member formed on a surface of the diaphragm portion opposite to the surface of the diaphragm portion on which the conductive portion is formed, the sensor internally having a closed space, a part of the closed space being formed along an inner circumferential surface of the conductive portion and the surface of the diaphragm portion on which the conductive portion is formed, wherein the temperature compensation member compensates for deformation of the diaphragm portion caused by thermal expansion of a gas sealed in the closed space.

The configuration in (1) can achieve optimum temperature compensation by cancelling out the deformation of the diaphragm portion caused by a change in pressure associated with the temperature of the gas in the closed space (thermal expansion of the gas sealed in the closed space) to suppress the deformation of the diaphragm portion within an intended temperature range.

Moreover, the configuration in (1) carries out effective temperature compensation to allow a sensor with a thin diaphragm to be designed and produced, thus enabling an increase in the sensitivity of the sensor.

The “compensation for the deformation of the diaphragm portion” in the present invention includes completely zeroing the amount of deformation of the diaphragm portion and approximating the amount of deformation of the diaphragm portion to zero.

(2) In the method for temperature compensation in the sensor in (1), preferably, the sensor is configured as a capacitive sensor including the substrate, the ring-like conductive portion having an inner diameter of 2R2 and an outer diameter of 2R3, the diaphragm portion formed on the surface of the conductive portion opposite to the surface of the conductive portion on which the insulator layer is formed, the diaphragm portion being shaped like a circular plate that is deformable depending on pressure and having an outer diameter of 2R3, the temperature compensation member being a ring-shaped temperature compensation ring that has an inner diameter of 2R1 and an outer diameter of 2R3, and a part of the closed space being formed by the inner circumferential surface of the conductive portion and the surface of the diaphragm portion on which the conductive portion is formed, and the method includes a computation step (1) of dividing, based on Timoshenko's symmetric circular plate theory, a composite circular plate configured such that center axes of the conductive portion, the diaphragm portion, and the temperature compensation ring align with one another into a first segment including a portion with a radius of 0 to R1 based on the center axis of the diaphragm portion, a second segment including a portion with a radius of R1 to R2 based on the center axes of the diaphragm portion and the temperature compensation ring, and a third segment including a portion with a radius of R2 to R3 based on the center axes of the conductive portion, the diaphragm portion, and the temperature compensation ring,

a computation step (2) of determining, based on Kirchhoff's circular plate theory, strains ∈0rr and ∈0θθ of a reference plane (z=0) in a stacking direction of the first to third segments (a direction of a Z axis) shown below in Formulae (5) and (6), using Formulae (1) to (4) shown below and representing relations between strains ∈rr and ∈θθ and displacements κr and κθ, in a radial direction (a direction of an r axis) and a circumferential direction (θ),

\(\begin{matrix}
\left\lbrack {{Formula}\mspace{14mu} 1} \right\rbrack & \; \\
{ɛ_{rr} = {ɛ_{rr}^{0} + {z\; \kappa_{r}}}} & (1) \\
\left\lbrack {{Formula}\mspace{14mu} 2} \right\rbrack & \; \\
{ɛ_{\theta\theta} = {ɛ_{\theta\theta}^{0} + {z\; \kappa_{\theta}}}} & (2) \\
\left\lbrack {{Formula}\mspace{14mu} 3} \right\rbrack & \; \\
{\kappa_{r} = {{{- {^{2}\omega}}\text{/}{r^{2}}} = {{- {\theta}}\text{/}{r}}}} & (3) \\
\left\lbrack {{Formula}\mspace{14mu} 4} \right\rbrack & \; \\
{\kappa_{\theta} = {{{- \left( {1/r} \right)}\left( {{\omega}\text{/}{r}} \right)} = {- \left( {\theta \text{/}r} \right)}}} & (4) \\
\left\lbrack {{Formula}\mspace{14mu} 5} \right\rbrack & \; \\
{ɛ_{rr}^{0} = \frac{u_{0}}{r}} & (5) \\
\left\lbrack {{Formula}\mspace{14mu} 6} \right\rbrack & \; \\
{ɛ_{\theta\theta}^{0} = \frac{u_{0}}{r}} & (6)
\end{matrix}\)

a computation step (3) of inputting Young's modulus E and Poisson's ratio ν to Formula (7) shown below to determine a matrix [Q],

\(\begin{matrix}
\left\lbrack {{Formula}\mspace{14mu} 7} \right\rbrack & \; \\
{\lbrack Q\rbrack = {\frac{E}{1 - v^{2}}\begin{Bmatrix}
1 & v \\
v & 1
\end{Bmatrix}}} & (7)
\end{matrix}\)

a computation step (4) of inputting the matrix [Q], the strains ∈0rr and ∈0θθ, the displacements κr and κθ, a coefficient of thermal expansion α, and a temperature difference ΔT (a difference between a reference temperature T0 in an initial state during compensation for deformation of the diaphragm portion and a temperature T1 resulting from a change) to a constitutive equation for stress on a linearly elastic symmetric circular plate with traverse isotropy shown below in Formula (8) to determine a stress σrr in the radial direction (the direction of the r axis) and a stress σθθ in the circumferential direction (θ),

\(\begin{matrix}
\left\lbrack {{Formula}\mspace{14mu} 8} \right\rbrack & \; \\
{\begin{Bmatrix}
\sigma_{rr} \\
\sigma_{\theta\theta}
\end{Bmatrix} = {\lbrack Q\rbrack \left( {\begin{Bmatrix}
ɛ_{rr}^{0} \\
ɛ_{\theta\theta}^{0}
\end{Bmatrix} + {Z\begin{Bmatrix}
\kappa_{r} \\
\kappa_{\theta}
\end{Bmatrix}} - \begin{Bmatrix}
{{\alpha\Delta}\; T} \\
{{\alpha\Delta}\; T}
\end{Bmatrix}} \right)}} & (8)
\end{matrix}\)

a computation step (5) of inputting the matrix [Q] to Formulae (9) to (11) shown below to compute matrixes [A], [B], and [D],

\(\begin{matrix}
\left\lbrack {{Formula}\mspace{14mu} 9} \right\rbrack & \; \\
{\lbrack A\rbrack = {\begin{bmatrix}
A_{11} & A_{12} \\
A_{21} & A_{22}
\end{bmatrix} = {\int_{z_{1}}^{z_{2}}{\lbrack Q\rbrack \ {z}}}}} & (9) \\
\left\lbrack {{Formula}\mspace{14mu} 10} \right\rbrack & \; \\
{\lbrack B\rbrack = {\begin{bmatrix}
B_{11} & B_{12} \\
B_{21} & B_{22}
\end{bmatrix} = {\int_{z_{1}}^{z_{2}}{\lbrack Q\rbrack z\ {z}}}}} & (10) \\
\left\lbrack {{Formula}\mspace{14mu} 11} \right\rbrack & \; \\
{\lbrack D\rbrack = {\begin{bmatrix}
D_{11} & D_{12} \\
D_{21} & D_{22}
\end{bmatrix} = {\int_{z_{1}}^{z_{2}}{\lbrack Q\rbrack z^{2}\ {z}}}}} & (11)
\end{matrix}\)

a computation step (6) of inputting the matrix [Q], the coefficient of thermal expansion α, and the temperature difference ΔT (the difference between the reference temperature T0 in the initial state during the compensation for the deformation of the diaphragm portion and the temperature T1 resulting from the change) to Formulae (12) and (13) shown below to compute matrices [NT] and [MT],

\(\begin{matrix}
\left\lbrack {{Formula}\mspace{14mu} 12} \right\rbrack & \; \\
{\begin{bmatrix}
N_{r}^{T} \\
N_{\theta}^{T}
\end{bmatrix} = {\int_{z_{1}}^{z_{2}}{{\lbrack Q\rbrack \begin{bmatrix}
{{\alpha\Delta}\; T} \\
{{\alpha\Delta}\; T}
\end{bmatrix}}\ {z}}}} & (12) \\
\left\lbrack {{Formula}\mspace{14mu} 13} \right\rbrack & \; \\
{\begin{bmatrix}
M_{r}^{T} \\
M_{\theta}^{T}
\end{bmatrix} = {\int_{z_{1}}^{z_{2}}{{\lbrack Q\rbrack \begin{bmatrix}
{{\alpha\Delta}\; T} \\
{{\alpha\Delta}\; T}
\end{bmatrix}}z\ {z}}}} & (13)
\end{matrix}\)

a computation step (7) of inputting, to Formula (14) shown below, the amount of initial deformation ω0′(r) of the diaphragm portion corresponding to the reference temperature T0 and the reference pressure P0 in the initial state during the compensation for the deformation of the diaphragm portion, and a distance g between the surface of the diaphragm portion on which the conductive portion is formed and an opposite surface of the substrate opposite to the surface of the diaphragm portion on which the conductive portion is formed, to compute a volume V0 in the closed space in the initial state,

[Formula 14]

V0=∫0R2πr(g+ω0′(r))dr  (14)

a computation step (8) of inputting a pressure PC in the closed space, the reference pressure P0, the volume V0 in the closed space in the initial state, the reference temperature T0, the temperature T1 resulting from the change, and a volume V1 (assumed value) in the closed space resulting from thermal expansion to Formula (15) shown below to compute a resultant pressure (a difference between the pressure PC in the closed space and the reference temperature P0 of an environment) P of the diaphragm portion,

\(\begin{matrix}
\left\lbrack {{Formula}\mspace{14mu} 15} \right\rbrack & \; \\
{P = {\frac{P_{c}V_{0}T_{1}}{T_{0}V_{1}} - P_{0}}} & (15)
\end{matrix}\)

a computation step (9) of inputting a dielectric constant ∈0 of vacuum, a relative dielectric constant (a ratio between a dielectric constant of a medium and the dielectric constant of vacuum) ∈r, the amount of initial deformation ω0′(r), and the distance g to Formula (16) shown below to compute a capacitance C0′ corresponding to the amount of initial deformation ω0′(r),

\(\begin{matrix}
\left\lbrack {{Formula}\mspace{14mu} 16} \right\rbrack & \; \\
{C_{0}^{\prime} = {\int_{0}^{R_{2}}{\frac{ɛ_{0}ɛ_{r}2\pi \; r}{\left( {g{\omega_{0}^{\prime}(r)}} \right)}\ {r}}}} & (16)
\end{matrix}\)

a computation step (10) of inputting Formulae (1) to (6) shown above to Formulae (17) and (18) shown below to obtain Formula (19) shown below and representing a resultant force Nr in the first to third segments in the radial direction (the direction of the r axis), Formula (20) shown below and representing a resultant force Nθ in the first to third segments in the circumferential direction (θ), Formula (21) shown below and representing a resultant moment Mr in the first to third segments in the radial direction (the direction of the r axis), and Formula (22) shown below and representing a resultant moment Mθ in the first to third segments in the circumferential direction (θ),

\(\begin{matrix}
\left\lbrack {{Formula}\mspace{14mu} 17} \right\rbrack & \; \\
{\begin{Bmatrix}
N_{r} \\
N_{0}
\end{Bmatrix} = {\lbrack A\rbrack \left( {\begin{Bmatrix}
ɛ_{rr}^{0} \\
ɛ_{\theta\theta}^{0}
\end{Bmatrix} + {\lbrack B\rbrack \begin{Bmatrix}
\kappa_{r} \\
\kappa_{0}
\end{Bmatrix}} - \begin{Bmatrix}
N_{r}^{T} \\
N_{\theta}^{T}
\end{Bmatrix}} \right)}} & (17) \\
\left\lbrack {{Formula}\mspace{14mu} 18} \right\rbrack & \; \\
{\begin{Bmatrix}
M_{r} \\
M_{\theta}
\end{Bmatrix} = {\lbrack B\rbrack \left( {\begin{Bmatrix}
ɛ_{rr}^{0} \\
ɛ_{\theta\theta}^{0}
\end{Bmatrix} + {\lbrack D\rbrack \begin{Bmatrix}
\kappa_{r} \\
\kappa_{\theta}
\end{Bmatrix}} - \begin{Bmatrix}
M_{r}^{T} \\
M_{\theta}^{T}
\end{Bmatrix}} \right)}} & (18) \\
\left\lbrack {{Formula}\mspace{14mu} 19} \right\rbrack & \; \\
{N_{r} = {{A_{11\;}\frac{{u_{0}(r)}}{r}} + {A_{12}\frac{u_{0}(r)}{r}} - {B_{11}\frac{{\theta (r)}}{r}} - {B_{12}\frac{\theta (r)}{r}} - N_{r}^{T}}} & (19) \\
\left\lbrack {{Formula}\mspace{14mu} 20} \right\rbrack & \; \\
{N_{\theta} = {{A_{21}\frac{{u_{0}(r)}}{r}} + {A_{22}\frac{u_{0}(r)}{r}} - {B_{21}\frac{{\theta (r)}}{r}} - {B_{22}\frac{\theta (r)}{r}} - N_{\theta}^{T}}} & (20) \\
\left\lbrack {{Formula}\mspace{14mu} 21} \right\rbrack & \; \\
{M_{r} = {{B_{11}\frac{{u_{0}(r)}}{r}} + {B_{12}\frac{u_{0}(r)}{r}} - {D_{11}\frac{{\theta (r)}}{r}} - {D_{12}\frac{\theta (r)}{r}} - M_{r}^{T}}} & (21) \\
\left\lbrack {{Formula}\mspace{14mu} 22} \right\rbrack & \; \\
{M_{\theta} = {{B_{21}\frac{{u_{0}(r)}}{r}} + {B_{22}\frac{u_{0}(r)}{r}} - {D_{21}\frac{{\theta (r)}}{r}} - {D_{22}\frac{\theta (r)}{r}} - M_{\theta}^{T}}} & (22)
\end{matrix}\)

a computation step (11) of inputting the resultant force Nr in the first to third segments in the radial direction (the direction of the r axis), the resultant force Nθ in the first to third segments in the circumferential direction (θ), the resultant moment Mr in the first to third segments in the radial direction (the direction of the r axis), the resultant moment Mθ in the first to third segments in the circumferential direction (θ), a transverse shear force Qr, and the resultant pressure (the difference between the pressure in the closed space and the reference pressure of the environment) P of the diaphragm portion to Formulae (23) to (25) shown below, to determine a balanced equation for an axial symmetric circular plate represented in Formula (26) shown below,

\(\begin{matrix}
\left\lbrack {{Formula}\mspace{14mu} 23} \right\rbrack & \; \\
{{\frac{N_{r}}{r} + \frac{N_{r} - N_{0}}{r}} = 0} & (23) \\
\left\lbrack {{Formula}\mspace{14mu} 24} \right\rbrack & \; \\
{Q_{r} = {\frac{M_{r}}{r} + \frac{M_{r} - M_{\theta}}{r}}} & (24) \\
\left\lbrack {{Formula}\mspace{14mu} 25} \right\rbrack & \; \\
{{\frac{Q_{r}}{r} + P + \frac{Q_{r}}{r}} = 0} & (25) \\
\left\lbrack {{Formula}\mspace{14mu} 26} \right\rbrack & \; \\
{{{\frac{1}{r}\frac{\;}{r}\left( {{r\frac{M_{r}}{r}} + M_{r} + M_{\theta}} \right)} + P} = 0} & (26)
\end{matrix}\)

a computation step (12) of inputting Formulae (19) to (22) shown above to Formulae (23) and (26) shown above to obtain relational expressions (27) and (28) shown below,

\(\begin{matrix}
\left\lbrack {{Formula}\mspace{14mu} 27} \right\rbrack & \; \\
{{\frac{^{2}{\theta (r)}}{r^{2}} + {\frac{1}{r}\frac{{\theta (r)}}{r}} - \frac{\theta (r)}{r^{2}}} = \frac{\Pr}{2D_{11}^{*}}} & (27) \\
\left\lbrack {{Formula}\mspace{14mu} 28} \right\rbrack & \; \\
{{\frac{^{2}{u_{0}(r)}}{r^{2}} + {\frac{1}{r}\frac{{u_{0}(r)}}{r}} - \frac{u_{0}(r)}{r^{2}}} = {\frac{\Pr \; \beta}{2D_{11}^{*}}\left( {\beta = {{B_{11}\text{/}A_{11}{and}D_{11}^{*}} = {D_{11} - {B_{11}^{2}\text{/}A_{11}}}}} \right)}} & (28)
\end{matrix}\)

a computation step (13) of carrying out two integration processes on Formulae (27) and (28) shown above to obtain Formulae (29) and (30) shown below,

\(\begin{matrix}
\left\lbrack {{Formula}\mspace{14mu} 29} \right\rbrack & \; \\
{{\theta (r)} = {{b_{1}r} + \frac{b_{2}}{r} + {\frac{1}{D_{11}^{*}}\left( \frac{\Pr^{3}}{16} \right)}}} & (29) \\
\left\lbrack {{Formula}\mspace{14mu} 30} \right\rbrack & \; \\
{{u_{0}(r)} = {{a_{1}r} + \frac{a_{2}}{r} + {\frac{\beta}{D_{11}^{*}}\left( \frac{\Pr^{3}}{16} \right)}}} & (30)
\end{matrix}\)

a computation step (14) of carrying out an integration process on Formula (29) shown above to compute an amount of deformation ω(1) of the diaphragm portion in the first segment shown below in Formula (31), an amount of deformation ω(2) of the diaphragm portion in the second segment shown below in Formula (32), and an amount of deformation ω(3) of the diaphragm portion in the third segment shown below in Formula (33),

\(\begin{matrix}
\left\lbrack {{Formula}\mspace{14mu} 31} \right\rbrack & \; \\
{{\omega^{(1)} = {\frac{\Pr^{4}}{64D_{11}^{*{(1)}}} + \frac{b_{1}^{(1)}r^{2}}{2} + c^{(1)}}},{0 \leq r \leq R_{1}}} & (31) \\
\left\lbrack {{Formula}\mspace{14mu} 32} \right\rbrack & \; \\
{{\omega^{(2)} = {\frac{\Pr^{4}}{64D_{11}^{*{(2)}}} + \frac{b_{1}^{(2)}r^{2}}{2} + {b_{2}^{(2)}{\ln (r)}} + c^{(2)}}},{R_{1} \leq r \leq R_{2}}} & (32) \\
\left\lbrack {{Formula}\mspace{14mu} 33} \right\rbrack & \; \\
{{\omega^{(3)} = 0},{R_{2} \leq r \leq R_{3}}} & (33)
\end{matrix}\)

a computation step (15) of inputting the amount of deformation ω(1) and ω(2) and the distance g to Formula (34) shown below to compute the volume V1 in the closed space resulting from the thermal expansion,

[Formula 34]

V1=∫0R2πr(g+ω(1))dr+∫0R2πr(g+ω(2))dr  (34)

a computation step (16) of inputting the volume V1 to Formulae (31) and (32) shown above to compute a capacitance C′ shown below in Formula (35) and corresponding to the amounts of deformation ω(1) and ω(2), and

\(\begin{matrix}
\left\lbrack {{Formula}\mspace{14mu} 35} \right\rbrack & \; \\
{C^{\prime} = {{\int_{0}^{R_{1}}{\frac{ɛ_{0}ɛ_{r}2\pi \; r}{\left( {g + {\omega^{(1)}(r)}} \right)}\ {r}}} + {\int_{R_{1}}^{R_{2}}{\frac{ɛ_{0}ɛ_{r}2\pi \; r}{\left( {g + {\omega^{(2)}(r)}} \right)}\ {r}}}}} & (35)
\end{matrix}\)

a computation step (17) of inputting the capacitances C0′ and C′ to Formula (36) shown below to determine an amount of change in capacitance ΔC′, the computation steps (1) to (17) being carried out in order.

[Formula 36]

ΔC′=C′−C′0  (6)

The configuration in (2) allows obtainment of the amount of change in capacitance ΔC′, more specifically, the parameter ΔC′ enabling determination of the degree of compensation for the deformation of the diaphragm portion caused by the thermal expansion of the gas sealed in the closed space. Thus, the deformation of the diaphragm portion can be compensated for more accurately than in the conventional art simply by applying the result of optimization of the parameter ΔC′ to the capacitive sensor. As a result, in detecting a change in the capacitance between the diaphragm portion and both the first electrode portion and the conductive portion based on the deformation of the diaphragm portion, the capacitive sensor can detect the change in capacitance more accurately than in the conventional art. Here, “optimization of the parameter ΔC′” includes completely zeroing the parameter ΔC′ and approximating the parameter ΔC′ to zero.

(3) In the method for temperature compensation in the sensor in (1) or (2), preferably, the conductive portion is a second electrode portion for detecting a change in the capacitance between the diaphragm portion and both the first electrode portion and the second electrode portion based on the deformation of the diaphragm portion.

The configuration in (3) allows the deformation of the diaphragm portion to be compensated for more accurately than in the conventional art simply by applying the result of optimization of the parameter ΔC′ to the capacitive sensor. As a result, in detecting a change in the capacitance between the diaphragm portion and both the first electrode portion and the second electrode portion based on the deformation of the diaphragm portion, the capacitive sensor can detect the change in capacitance more accurately than in the conventional art.

(4) In the method for temperature compensation in the sensor in (3), preferably, the sensor includes a barrier metal layer containing at least platinum and formed between the second electrode portion and the insulator layer, the barrier metal layer having an inner circumferential surface forming a part of the closed space. Here, the “barrier metal” refers to a material such as metal which exerts the following advantageous effects: the material (1) allows a dense film to be formed and produces a barrier effect against reaction between a wiring material and a silicon substrate, (2) is bonded well to metal and an insulating film, (3) can be micromachined by dry etching, and (4) offers reduced resistance.

The configuration in (4) applies the result of optimization of the parameter ΔC′ to the capacitive sensor. Thus, the capacitive sensor configured to enjoy the barrier metal effect of the barrier metal layer can also detect a change in the capacitance between the diaphragm portion and both the first electrode portion and the conductive portion more accurately than in the conventional art.

(5) In the method for temperature compensation in the sensor in (2), preferably, the conductive portion is a sealing ring portion formed on a surface of the diaphragm portion opposite to the surface of the diaphragm portion on which the temperature compensation ring is formed, and the sensor includes a ring-like second electrode portion formed between the sealing ring portion and the insulator layer to detect a change in the capacitance between the diaphragm portion and both the first electrode portion and the second electrode portion based on the deformation of the diaphragm portion.

The configuration in (5) applies the result of optimization of the parameter ΔC′ to the capacitive sensor. Thus, while configured to enjoy an effect enabling possible leakage of the gas in the closed space to be more reliably prevented by using the sealing ring to seal the portion between the diaphragm portion and the second electrode portion, the capacitive sensor can also detect a change in the capacitance between the diaphragm portion and both the first electrode portion and the second electrode portion more accurately than in the conventional art.

(6) In the method for temperature compensation in the sensor in (5), preferably, the second electrode portion and the sealing ring portion of the sensor are bonded together by a gold-gold bonding.

The configuration in (6) applies the result of optimization of the parameter ΔC′ to the capacitive sensor. Thus, while configured to enjoy an effect enabling reliability of an electric connection between the second electrode portion and the sealing ring portion to be improved, the capacitive sensor can also detect a change in the capacitance between the diaphragm portion and both the first electrode portion and the second electrode portion more accurately than in the conventional art.

(7) In the method for temperature compensation in the sensor in (2), preferably, the sensor includes a ring-like barrier metal layer containing at least platinum and formed on a surface of the diaphragm portion opposite to the surface of the diaphragm portion on which the temperature compensation ring is formed, and a ring-like second electrode portion formed between the barrier metal layer and the insulator layer to detect a change in the capacitance between the diaphragm portion and both the first electrode portion and the second electrode portion based on the deformation of the diaphragm portion, and when the barrier metal layer includes a single layer, the conductive portion is the barrier metal layer, and when the barrier metal layer includes a plurality of layers, the conductive portion is a layer included in the barrier metal layer and which is closest to the diaphragm portion.

The configuration in (7) applies the result of optimization of the parameter ΔC′ to the capacitive sensor. Thus, the capacitive sensor configured to enjoy the barrier metal effect of the barrier metal layer can also detect a change in the capacitance between the diaphragm portion and both the first electrode portion and the second electrode portion more accurately than in the conventional art.

(8) The present invention provides a computation program for carrying out a computation process for a method for temperature compensation in a sensor including a substrate with a first electrode portion formed on one surface, a conductive portion formed on the one surface of the substrate via an insulator layer, a diaphragm portion formed on a surface of the conductive portion opposite to the surface of the conductive portion on which the insulator layer is formed, the diaphragm portion being deformable depending on pressure, and a temperature compensation member formed on a surface of the diaphragm portion opposite to the surface of the diaphragm portion on which the conductive portion is formed, the sensor internally having a closed space, a part of the closed space being formed along an inner circumferential surface of the conductive portion and the surface of the diaphragm portion on which the conductive portion is formed, wherein the temperature compensation member compensates for deformation of the diaphragm portion caused by thermal expansion of a gas sealed in the closed space.

The configuration in (8) allows effects similar to the effects of the configuration in (1) to be enjoyed.

(9) A computation processing device according to the present invention carries out a computation process in accordance with the computation program according to claim 8.

The configuration in (9) allows effects similar to the effects of the configuration in (8) to be enjoyed.

(10) The present invention provides a sensor including a substrate with a first electrode portion formed on one surface, a conductive portion formed on the one surface of the substrate via an insulator layer, a diaphragm portion formed on a surface of the conductive portion opposite to the surface of the conductive portion on which the insulator layer is formed, the diaphragm portion being deformable depending on pressure, and a temperature compensation member formed on a surface of the diaphragm portion opposite to the surface of the diaphragm portion on which the conductive portion is formed, the sensor internally having a closed space, a part of the closed space being formed along an inner circumferential surface of the conductive portion and the surface of the diaphragm portion on which the conductive portion is formed, wherein the temperature compensation member compensates for deformation of the diaphragm portion caused by thermal expansion of a gas sealed in the closed space.

The configuration in (10) allows effects similar to the effects of the configuration in (1) to be enjoyed.

## DESCRIPTION OF EMBODIMENTS

### First Embodiment

A method for temperature compensation in a sensor according to a first embodiment of the present invention will be described below with reference to FIG. 1 to FIG. 6.

(Configuration of a Capacitive Sensor 100)

As shown in FIG. 1(a) and FIG. 1(b), a capacitive sensor (a sensor) 100 to which the results of computations in a method for temperature compensation in the capacitive sensor are applied includes a substrate 1, an insulator layer 2, a first electrode portion 3, a second electrode portion (conductive portion) 4, a diaphragm portion 5, a temperature compensation ring (temperature compensation member) 6, and a closed space 7.

The substrate 1 is formed of a semiconductor such as silicon and has a circular recess 1a in a substantially central portion of the substrate 1.

The insulator layer 2 is a layer formed of an insulator such as silicon dioxide and is formed on one surface of the substrate 1. The insulator layer 2 also has a circular penetration portion 2a formed in a substantially central portion thereof so as to align with the recess 1a in the substrate 1 and such a generally rectangular penetration portion 2b as shown in FIG. 1(a).

The first electrode portion 3 is formed as a barrier metal layer containing at least platinum and includes three layers, that is, a layer located closest to the substrate 1 and formed of titanium, a layer located furthest from the substrate 1 and formed of gold, and a layer located between these two layers and formed of platinum.

The second electrode portion 4 is formed of gold and shaped like a ring on a surface of the insulator layer 2 opposite to a surface of the insulator layer 2 on which the substrate 1 is formed. In a variation, the second electrode portion 4 may be formed of a metal material such as silver or copper.

The diaphragm portion 5 is formed of silicon and is deformable under a pressure applied by atmospheric pressure. In a variation, the diaphragm portion 5 may be formed of a semiconductor material other than silicon.

The temperature compensation ring 6 is formed of aluminum and shaped like a ring on a surface of the diaphragm portion 5 opposite to a surface of the diaphragm portion 5 on which the second electrode portion 4 is formed. In a variation, the temperature compensation ring 6 may be a metal material with a high coefficient of thermal expansion instead of aluminum.

The closed space 7 forms an atmospheric environment suitable for detection of the pressure applied to the diaphragm portion 5. The closed space 7 is formed by being surrounded by an inner surface of the recess 1a, an inner circumferential surface of the penetration portion 2a, an inner circumferential surface of the second electrode portion 4, and the surface of the diaphragm portion 5 on which the second electrode portion 4 is formed.

(Operation of the Capacitive Sensor 100)

Now, operation of the capacitive sensor 100 will be described. When a pressure based on atmospheric pressure is applied to the diaphragm portion 5 of the capacitive sensor 100, the diaphragm portion 5 is deformable depending on the pressure. The pressure is measured by detecting a change in the capacitance between the diaphragm portion 5 and both the first electrode portion 3 and the second electrode portion 4.

(Principle for Compensation for the Amount of Deformation of the Diaphragm Portion 5)

Now, a general principle for compensation for the amount of deformation of the diaphragm portion 5 will be described with reference to FIG. 2. A distance g in FIG. 2(a) to FIG. 2(c) indicates the distance between the surface of the diaphragm portion 5 on which the second electrode portion 4 is formed and an opposite surface of the recess 1a opposite to the surface of the diaphragm portion 5 on which the second electrode portion 4 is formed.

First, in a state before compensation shown in FIG. 2(a) and in an initial state in an environment with a reference temperature T0 and a reference pressure P0, the diaphragm portion 5 is deformed to a state shown by a solid line in FIG. 5. The amount of initial deformation of the diaphragm portion 5 is ω0(r). A capacitance C0 is generated between the diaphragm portion 5 and both the first electrode portion 3 and the second electrode portion 4 in association with the amount of initial deformation ω0(r). Then, the following are assumed. When the reference pressure remains the initial pressure P0 and only the reference temperature changes from the initial temperature T0 to a temperature T, the diaphragm portion 5 is deformed to a state shown by a dotted line in FIG. 2(a), the amount of deformation of the diaphragm portion 5 changes from the amount of initial deformation ω0(r) to an amount of deformation ω(r), and the capacitance generated between the diaphragm portion 5 and both the first electrode portion 3 and the second electrode portion 4 changes from the initial capacitance C0 to C. Under these assumptions, the amount of change ΔC in capacitance can be expressed by Formula (37) shown below. In Formula (37), a coefficient ∈0 represents the dielectric constant of vacuum and a coefficient ∈r represents a relative dielectric constant (the ratio between the dielectric constant of a medium and the dielectric constant of vacuum).

\(\begin{matrix}
\left\lbrack {{Formula}\mspace{14mu} 37} \right\rbrack & \; \\
{{\Delta \; C} = {{C - C_{0}} = {\int_{0}^{R_{2}}{\frac{ɛ_{0}ɛ_{r}2\pi \; {r\left( {{\omega_{0}(r)} - {\omega (r)}} \right)}}{\left( {g + {\omega_{0}(r)}} \right)\left( {g + {\omega (r)}} \right)}\ {r}}}}} & (37)
\end{matrix}\)

Then, in a state after compensation shown in FIG. 2(b) and in an initial state in an environment with the reference temperature T0 and the reference pressure P0, the diaphragm portion 5 is deformed to a state shown by a solid line in FIG. 2(b). The amount of initial deformation of the diaphragm portion 5 is ω0′(r). A capacitance C′0 is generated between the diaphragm portion 5 and both the first electrode portion 3 and the second electrode portion 4 in association with the amount of initial deformation ω0′(r). Then, the following are assumed. When the reference pressure remains the initial pressure P0 and only the reference temperature changes from the initial temperature T0 to a temperature T, the diaphragm portion 5 is deformed to a state shown by a dotted line in FIG. 2(b), the amount of deformation of the diaphragm portion 5 changes from the amount of initial deformation ω0′(r) to an amount of deformation ω′(r), and the capacitance generated between the diaphragm portion 5 and both the first electrode portion 3 and the second electrode portion 4 changes from the initial capacitance C′0 to C′. Under these assumptions, the amount of change ΔC′ in capacitance can be expressed by Formula (38) shown below. In Formula (38), the coefficient ∈0 represents the dielectric constant of vacuum and the coefficient ∈r represents the relative dielectric constant (the ratio between the dielectric constant of a medium and the dielectric constant of vacuum).

\(\begin{matrix}
\left\lbrack {{Formula}\mspace{14mu} 38} \right\rbrack & \; \\
{{\Delta \; C^{\prime}} = {{C^{\prime} - C_{0}^{\prime}} = {\int_{0}^{R_{2}}{\frac{ɛ_{0}ɛ_{r}2\pi \; {r\left( {{\omega_{0}^{\prime}(r)} - {\omega^{\prime}(r)}} \right)}}{\left( {g + {\omega_{0}^{\prime}(r)}} \right)\left( {g + {\omega^{\prime}(r)}} \right)}\ {r}}}}} & (38)
\end{matrix}\)

Formula 38 indicates that the parameter ΔC′ may be set to zero in order to completely compensate for deformation of the diaphragm portion 5, that is, to completely zero a difference in the amount of deformation of the diaphragm portion 5 (=the amount of initial deformation ω0′(r)−the amount of deformation ω′(r)). This in turn indicates that the parameter ΔC′ enables the degree of compensation for the deformation of the diaphragm portion 5 to be determined.

FIG. 2(c) shows a comparative example for the general principle for compensation shown in FIG. 2(a) and FIG. 2(b) and shows the result of optimization of the parameter ΔC′ obtained by computations in the method for temperature compensation according to the first embodiment, more specifically, the result of setting the parameter ΔC′ to zero, and thus, the result of completely zeroing the amount of deformation of the diaphragm portion 5. In this state, the distance g is maintained between the surface of the diaphragm portion 5 on which the second electrode portion 4 is formed and an inner surface of the recess 1a opposite to the surface of the diaphragm portion 5 on which the second electrode portion 4 is formed. In a variation, the amount of deformation of the diaphragm portion 5 may be approximated to zero by setting the parameter ΔC′ to a value approximate to zero.

(Computation Steps of the Method for Temperature Compensation in the Sensor According to the First Embodiment)

Now, the computation steps of the method for temperature compensation in the capacitive sensor will be described with reference to FIG. 3 to FIG. 6. The purpose of each of the computation steps is to compute the deformation of the diaphragm portion 5 associated with temperature. The pressure in the closed space 7 varies depending on temperature, and thus, the deformation of the diaphragm portion 5 is calculated based on the relation between temperature and pressure.

First, in a computation step S1 shown in FIG. 3, based on the Timoshenko's symmetric circular plate theory, a composite circular plate configured such that center axes of the second electrode portion 4, the diaphragm portion 5, and the temperature compensation ring 6 align with one another (see FIG. 6(a)) is divided into a first segment (1) including a portion with a radius of 0 to R1 based on the center axis of the diaphragm portion 5, a second segment (2) including a portion with a radius of R1 to R2 based on the center axes of the diaphragm portion 5 and the temperature compensation ring 6, and a third segment (3) including a portion with a radius of R2 to R3 based on the center axes of the second electrode portion 4, the diaphragm portion 5, and the temperature compensation ring 6 (see FIG. 6(b)), as shown in FIG. 6.

An alternate long and short dash line in FIG. 6(a) and FIG. 6(b) shows an axis passing through the center axis P (the position of a radius of 0) of the second electrode portion 4, the diaphragm portion 5, and the temperature compensation ring 6 and extending along a stacking direction of the second electrode portion 4, the diaphragm portion 5, and the temperature compensation ring 6. Thicknesses tg, ts, and to in FIG. 6(a) and FIG. 6(b) represent the respective thicknesses of the second electrode portion 4, the diaphragm portion 5, and the temperature compensation ring 6. A temperature difference ΔT in FIG. 6(a) and FIG. 6(b) represents a difference between the reference temperature T0 and the temperature T. A resultant pressure P in FIG. 6(a) and FIG. 6(b) represents a difference between the pressure PC in the closed space 7 and the reference pressure P0 of the environment. R1 in FIG. 6(a) and FIG. 6(b) denotes the radius of the inner diameter (2R1) of the temperature compensation ring 6. Similarly, R2 in FIG. 6(a) and FIG. 6(b) denotes the radius of the inner diameter (2R2) of the second electrode portion 4. Similarly, R3 in FIG. 6(a) and FIG. 6(b) denotes the radius of the outer diameter (2R3) of the second electrode portion 4, the diaphragm portion 5, and the temperature compensation ring 6. In this case, the second electrode portion 4, the diaphragm portion 5, and the temperature compensation ring 6 are formed using gold, silicon, and aluminum, respectively, as a material.

Then, in a computation step S2, based on Kirchhoff's circular plate theory, strains ∈0rr and ∈0θθ of a reference plane (z=0), shown in Formulae (5) and (6) shown above, in the stacking direction of the first to third segments (1) to (3) are determined using Formulae (1) to (4) shown above and representing the relations between strains ∈rr and ∈θθ and displacements κr and κθ in a radial direction (the direction of an r axis) and a circumferential direction (θ).

Then, in a computation step S3, Young's modulus E and Poisson's ratio ν are input to Formula (7) shown above to determine a matrix [Q].

Then, in a computation step S4, a stress σrr in the radial direction (the direction of the r axis) and a stress σθθ in the circumferential direction (θ) are determined by inputting the matrix [Q], the strains ∈0rr and ∈0θθ, the displacements κr and κθ, a coefficient of thermal expansion α, and a temperature difference ΔT (a difference between a reference temperature T0 in an initial state during compensation for deformation of the diaphragm portion 5 and a temperature T1 resulting from a change) to a constitutive equation for stress on a linearly elastic symmetric circular plate with traverse isotropy shown in Formula (8) shown above.

Then, in a computation step S5, the matrix [Q] is input to Formulae (9) to (11) shown above to compute matrices [A], [B], and [D].

Then, in a computation step S6, matrices [NT] and [MT] are respectively computed by inputting the matrix [Q], the coefficient of thermal expansion α, and the temperature difference ΔT (the difference between the reference temperature T0 in the initial state during the compensation for the deformation of the diaphragm portion and the temperature T1 resulting from the change) to Formulae (12) and (13) shown above.

Then, in a computation step S7, a volume V0 in the closed space 7 in the initial state is computed by inputting, to Formula (14) shown above, the amount of initial deformation ω0′(r) of the diaphragm portion 5 corresponding to the reference temperature T0 and the reference pressure P0 in the initial state during the compensation for the deformation of the diaphragm portion 5, and the distance g between the surface of the diaphragm portion 5 on which the second electrode portion 4 is formed and an opposite surface of the recess 1a opposite to the surface of the diaphragm portion 5 on which the second electrode portion 4 is formed.

Then, in a computation step S8, a resultant pressure of the diaphragm portion 5 (the difference between the pressure PC in the closed space 7 and the reference pressure P0 of the environment) P is computed by inputting the pressure PC in the closed space, the reference pressure P0, the volume V0 in the closed space 7 in the initial state, the reference temperature T0, the temperature T1 resulting from the change, and a volume V1 (assumed value) in the closed space resulting from thermal expansion to Formula (15) shown above.

Then, in a computation step S9, a capacitance C0′ corresponding to the amount of initial deformation ω0′(r) is computed by inputting the dielectric constant ∈0 of vacuum, the relative dielectric constant (the ratio between the dielectric constant of a medium and the dielectric constant of vacuum) ∈r, the amount of initial deformation ω0′(r), and the distance g to Formula (16) shown above.

Then, in a computation step S10, Formulae (1) to (6) shown above are input to Formulae (17) and (18) shown above to obtain Formula (19) shown above representing a resultant force Nr in the first segment (1) to the third segment (3) in the radial direction (the direction of the r axis), Formula (20) shown above representing a resultant force Nθ in the first segment (1) to the third segment (3) in the circumferential direction (θ), Formula (21) shown above representing a resultant moment Mr in the first segment (1) to the third segment (3) in the radial direction (the direction of the r axis), and Formula (22) shown below representing a resultant moment Mθ in the first segment (1) to the third segment (3) in the circumferential direction (θ). Here, reference characters A11, A12, B11, and B12 in Formula (19) represent components of the matrices [A] and [B] shown in Formulae (9) and (10) shown above. Reference character NrT represents a resultant force exerted in the radial direction (the direction of the r axis) at the temperature T. Reference characters A21, A22, B21, and B22 in Formula (20) represent components of the matrices [A] and [B] shown in Formulae (9) and (10) shown above. Reference character NθT represents a resultant force exerted in the circumferential direction (θ) at the temperature T. Reference characters B11, B12, D11, and D12 in Formula (21) represent components of the matrices [B] and [D] shown in Formulae (10) and (11) shown above. Reference character MrT represents a resultant moment exerted in the radial direction (the direction of the r axis) at the temperature T. Reference characters B21, B22, D21, and D22 in Formula (22) represent components of the matrices [B] and [D] shown in Formulae (10) and (11) shown above. Reference character MθT represents a resultant moment exerted in the circumferential direction (θ) at the temperature T.

Then, in a computation step S11, a balanced equation for an axial symmetric circular plate represented in Formula (26) shown above is determined by inputting the resultant force Nr in the first segment (1) to the third segment (3) in the radial direction (the direction of the r axis), the resultant force Nθ in the first segment (1) to the third segment (3) in the circumferential direction (θ), the resultant moment Mr in the radial direction (the direction of the r axis), the resultant moment Mθ in the circumferential direction (θ), a transverse shear force Qr, and the resultant pressure (the difference between the pressure PC in the closed space 7 and the reference temperature P0 of the environment) P of the diaphragm portion 5 to Formulae (23) to (25) shown above.

Then, in a computation step S12, Formulae (19) to (22) shown above are input to Formulae (23) and (26) shown above to obtain relational expressions (27) and (28) shown above. Here, reference character D*11 in Formulae (27) and (28) represents a parameter acquired using the respective components A11, B11, and D11 of the matrices [A], [B], and [D] as shown in Formula (28). Similarly, reference numeral β in Formula (28) represents a parameter acquired using the respective components A11 and B11 of the matrices [A] and [B] as shown in Formula (28) shown above.

Then, in a computation step S13, two integration processes are carried out on Formulae (27) and (28) shown above to obtain common solutions for a gradient θ(r) of a normal direction displacement shown in FIG. 29) shown above and a displacement u0(r) shown in Formula 30 shown above. Here, reference characters a1 and a2 in Formula (30) and reference characters b1 and b2 shown in Formula (29) represent coefficients.

Then, in a computation step S14, an integration step is carried out on Formula (29) shown above to compute the amount of deformation ω(1) of the diaphragm portion 5 in the first segment (1) shown above in Formula (31), the amount of deformation ω(2) of the diaphragm portion 5 in the second segment (2) shown above in Formula (32), and the amount of deformation ω(3) of the diaphragm portion 5 in the third segment (3) shown above in Formula (33). Reference characters D*11(1), b1(1), and c(1) in Formula (31) represent coefficients resulting from the integration process. Similarly, reference characters D*11(2), b1(2), b2(2), and c(2) in Formula (32) represent coefficients resulting from the integration process. Thus, the coefficients b1(1), c(1), b1(2), b2(2), and c(2) are calculated based on a condition of continuity and a condition of constraint for each of the segments of the composite circular plate.

Then, in a computation step S15, the amount of deformation ω(1) and ω(2) of the diaphragm portion 5 and the distance g are input to Formula (34) shown above to compute the volume V1 in the closed space 7 resulting from the thermal expansion.

Then, in a computation step S16, the volume V1 in the closed space 7 resulting from the thermal expansion is input to Formulae (31) and (32) shown above to compute a capacitance C′ shown in Formula (35) shown above and corresponding to the amounts of deformation ω(1) and ω(2) of the diaphragm portion 5.

Then, in a computation step S17, the capacitances C0′ and C′ are input to Formula (36) shown above to determine an amount of change in capacitance ΔC′.

The above-described configuration can achieve the optimum temperature compensation by cancelling out the deformation of the diaphragm portion 5 caused by a change in pressure associated with the temperature of the gas in the closed space 7 (the thermal expansion of the gas sealed in the closed space 7) to suppress the deformation of the diaphragm portion 5 within an intended temperature range.

Moreover, the above-described configuration carries out effective temperature compensation to allow the capacitive sensor 100 with the thin diaphragm portion 5 to be designed and produced, thus enabling an increase in the sensitivity of the capacitive sensor 100.

Moreover, the above-described configuration can provide the parameter ΔC′, which enables determination of the degree of compensation for the deformation of the diaphragm portion 5 caused by the thermal expansion of the gas sealed in the closed space 7. Thus, the deformation of the diaphragm portion 5 can be compensated for more accurately than in the conventional art simply by applying the result of optimization of the parameter ΔC′ to the capacitive sensor. As a result, in detecting a change in the capacitance between the diaphragm portion 5 and both the first electrode portion 3 and the second electrode portion 4 based on the deformation of the diaphragm portion 5, the capacitive sensor 100 can detect the change in capacitance more accurately than in the conventional art. Here, “optimization of the parameter ΔC′” includes completely zeroing the parameter ΔC′ and approximating the parameter ΔC′ to zero. Furthermore, the “compensation for the deformation of the diaphragm portion 5” includes completely zeroing the amount of deformation of the diaphragm portion 5 by setting zero for the parameter ΔC′, and approximating the amount of deformation of the diaphragm portion 5 to zero by setting a value approximate to zero for the parameter ΔC′.

### Second Embodiment

Now, a method for temperature compensation in a sensor according to a second embodiment of the present invention will be described with reference to FIG. 7 to FIG. 10. Portions 21 to 27 (some of the portions are not shown in the drawings) of a capacitive sensor 200 to which the results of computations in the method for temperature compensation according to the second embodiment are applied are similar to the portions 1 to 7, respectively, of the capacitive sensor 100 to which the results of computations in the method for temperature compensation according to the first embodiment are applied. Thus, description of the portions 21 to 27 may be omitted.

(Configuration of the Capacitive Sensor 200)

As shown in FIG. 7, the capacitive sensor (the sensor) 200 includes a substrate 21, an insulator layer 22, a first electrode portion 23, a second electrode portion (conductive portion) 24, a diaphragm portion 25, a temperature compensation ring (temperature compensation member) 26, and a closed space 27 which are similar to the corresponding portions of the capacitive sensor 100, as well as a first barrier metal layer 28.

The first barrier metal layer 28 contains at least platinum and is formed between the second electrode portion 24 and the insulator layer 22 like a ring similar to the second electrode portion 24. The first barrier metal layer 28 includes two layers, a layer 28a located closest to the insulator layer 22 and formed of titanium and a layer 28b located closest to the second electrode portion 24 and formed of platinum. An inner circumferential surface of the first barrier metal layer 28 forms the closed space 27 along with an inner surface of a recess 21a, an inner circumferential surface of a penetration portion 22a, an inner circumferential surface of the second electrode portion 24, and a surface of the diaphragm portion 25 on which the second electrode portion 24 is formed.

(Operation of the Capacitive Sensor 200)

Now, operation of the capacitive sensor 200 will be described. When a pressure based on atmospheric pressure is applied to the diaphragm portion 25 of the capacitive sensor 200, the diaphragm portion 25 is deformable depending on the pressure. The pressure is measured by detecting a change in the capacitance between the diaphragm portion 25 and both the first electrode portion 23 and the second electrode portion 24, the change being caused by the deformation.

(Computation Steps of the Method for Temperature Compensation in the Sensor According to the Second Embodiment)

Now, computation steps of the method for temperature compensation in the capacitive sensor will be described with reference to FIG. 8 to FIG. 10. The second embodiment carries out steps S201 to S217 in order which are similar to the computation steps S1 to S17 of the method for temperature compensation according to the first embodiment.

This configuration applies the result of optimization of the parameter ΔC′ to the capacitive sensor 200. Thus, the capacitive sensor 200, configured to enjoy the barrier metal effect of the first barrier metal layer 28, can also detect a change in the capacitance between the diaphragm portion 25 and both the first electrode portion 23 and the second electrode portion 24 more accurately than in the conventional art.

### Third Embodiment

Now, a method for temperature compensation in a sensor according to a third embodiment of the present invention will be described with reference to FIG. 11 to FIG. 14. Portions 31 to 37 (some of the portions are not shown in the drawings) of a capacitive sensor 300 to which the results of computations in the method for temperature compensation according to the third embodiment are applied are similar to the portions 1 to 7, respectively, of the capacitive sensor 100 to which the results of computations in the method for temperature compensation according to the first embodiment are applied. Thus, description of the portions 31 to 37 may be omitted.

(Configuration of the Capacitive Sensor 300)

As shown in FIG. 11, the capacitive sensor (the sensor) 300 includes a substrate 31, an insulator layer 32, a first electrode portion 33, a second electrode portion 34, a diaphragm portion 35, a temperature compensation ring (temperature compensation member) 36, and a closed space 37 which are similar to the corresponding portions of the capacitive sensor 100, as well as a sealing ring portion (conductive portion) 38.

The sealing ring portion 38 is formed of a metal material such as gold, platinum, or titanium, has an inner diameter of 2R2 and an outer diameter of 2R3, and is formed between the diaphragm portion 35 and the second electrode portion 34 to prevent a gas sealed in the closed space 37 from leaking. In this case, the second electrode portion 34 and the sealing ring portion 38 are preferably bonded together by a gold-gold bonding. An inner circumferential surface of the sealing ring portion 38 forms the closed space 37 along with an inner surface of a recess 31a, an inner circumferential surface of a penetration portion 32a, an inner circumferential surface of the second electrode portion 34, and a surface of the diaphragm portion 35 on which the sealing ring portion 38 is formed.

(Operation of the Capacitive Sensor 300)

Now, operation of the capacitive sensor 300 will be described. When a pressure based on atmospheric pressure is applied to the diaphragm portion 35 of the capacitive sensor 300, the diaphragm portion 35 is deformable depending on the pressure. The pressure is measured by detecting a change in the capacitance between the diaphragm portion 35 and both the first electrode portion 33 and the second electrode portion 34, the change being caused by the deformation.

(Computation Steps of the Method for Temperature Compensation in the Sensor According to the Third Embodiment)

Now, computation steps of the method for temperature compensation in the capacitive sensor will be described with reference to FIG. 12 to FIG. 14. Computation steps S302 to S317 of the method for temperature compensation according to the third embodiment are similar to the computation steps S2 to S17, respectively, of the method for temperature compensation according to the first embodiment. Thus, only the computation step S301 will be described in detail.

First, in the computation step S301, based on the Timoshenko's symmetric circular plate theory, a composite circular plate configured such that center axes of the sealing ring portion 38, the diaphragm portion 35, and the temperature compensation ring 36 align with one another is divided into a first segment (1) including a portion with a radius of 0 to R1 based on the center axis of the diaphragm portion 35, a second segment (2) including a portion with a radius of R1 to R2 based on the center axes of the diaphragm portion 35 and the temperature compensation ring 36, and a third segment (3) including a portion with a radius of R2 to R3 based on the center axes of the sealing ring portion 38, the diaphragm portion 35, and the temperature compensation ring 36.

Then, the computation steps S302 to S317 are sequentially carried out to finish the computation steps of the method for temperature compensation in the capacitive sensor.

The above-described configuration applies the result of optimization of the parameter ΔC′ to the capacitive sensor 300. Thus, while configured to enjoy an effect enabling possible leakage of the gas in the closed space 37 to be more reliably prevented by using the sealing ring portion 38 to seal the portion between the diaphragm portion 35 and the second electrode portion 34, the capacitive sensor 300 can also detect a change in the capacitance between the diaphragm portion 35 and both the first electrode portion 33 and the second electrode portion 34 more accurately than in the conventional art.

Moreover, the above-described configuration applies the result of optimization of the parameter ΔC′ to the capacitive sensor 300. Thus, while configured to enjoy an effect enabling reliability of an electric connection between the second electrode portion 34 and the sealing ring portion 38 to be improved when the second electrode portion 34 and the sealing ring portion 38 are bonded together by a gold-gold bonding, the capacitive sensor 300 can also detect a change in the capacitance between the diaphragm portion 35 and both the first electrode portion 33 and the second electrode portion 34 more accurately than in the conventional art.

### Fourth Embodiment

Now, a method for temperature compensation in a sensor according to a fourth embodiment of the present invention will be described with reference to FIG. 15 to FIG. 18. Portions 41 to 47 (some of the portions are not shown in the drawings) of a capacitive sensor 400 to which the results of computations in the method for temperature compensation according to the fourth embodiment are applied are similar to the portions 1 to 7, respectively, of the capacitive sensor 100 to which the results of computations in the method for temperature compensation according to the first embodiment are applied. Thus, description of the portions 41 to 47 may be omitted.

(Configuration of the Capacitive Sensor 400)

As shown in FIG. 15, the capacitive sensor (the sensor) 400 includes a substrate 41, an insulator layer 42, a first electrode portion 43, a second electrode portion 44, a diaphragm portion 45, a temperature compensation ring (temperature compensation member) 46, and a closed space 47 which are similar to the corresponding portions of the capacitive sensor 100, as well as a sealing ring portion 48 and a second barrier metal layer 49.

The sealing ring portion 48 is formed of gold and provided between the diaphragm portion 45 and the second electrode portion 44, more specifically, on a surface of the second electrode portion 44 opposite to a surface of the second electrode portion 44 on which the insulator layer 42 is formed, thus preventing a gas sealed in the closed space 47 from leaking.

The second barrier metal layer 49 contains at least platinum, has an inner diameter of 2R2 and an outer diameter of 2R3, and is formed between the diaphragm portion 45 and the sealing ring 48 like a ring similar to the sealing ring 48. The second barrier metal layer 49 includes two layers, a layer 49a located closest to the sealing ring 48 and formed of platinum and a layer (conductive portion) 49b located closest to the diaphragm portion 45 and formed of titanium. An inner circumferential surface of the second barrier metal layer 49 forms the closed space 47 along with an inner circumferential surface of the sealing ring portion 48, an inner surface of a recess 41a, an inner circumferential surface of a penetration portion 42a, an inner circumferential surface of the second electrode portion 44, and a surface of the diaphragm portion 45 on which the second barrier metal layer 49 is formed.

(Operation of the Capacitive Sensor 400)

Now, operation of the capacitive sensor 400 will be described. When a pressure based on atmospheric pressure is applied to the diaphragm portion 45 of the capacitive sensor 400, the diaphragm portion 45 is deformable depending on the pressure. The pressure is measured by detecting a change in the capacitance between the diaphragm portion 45 and both the first electrode portion 43 and the second electrode portion 44, the change being caused by the deformation.

(Computation Steps of the Method for Temperature Compensation in the Sensor According to the Fourth Embodiment)

Now, computation steps of the method for temperature compensation in the capacitive sensor will be described with reference to FIG. 16 to FIG. 18. Computation steps S402 to S417 of the method for temperature compensation according to the fourth embodiment are similar to the computation steps S2 to S17, respectively, of the method for temperature compensation according to the first embodiment. Thus, only the computation step S401 will be described in detail.

First, in the computation step S401, based on the Timoshenko's symmetric circular plate theory, a composite circular plate configured such that center axes of a layer 49b of the second barrier metal layer 49 which is closest to the diaphragm portion 45, the diaphragm portion 45, and the temperature compensation ring 46 align with one another is divided into a first segment (1) including a portion with a radius of 0 to R1 based on the center axis of the diaphragm portion 45, a second segment (2) including a portion with a radius of R1 to R2 based on the center axes of the diaphragm portion 45 and the temperature compensation ring 46, and a third segment (3) including a portion with a radius of R2 to R3 based on the center axes of the layer 49b of the second barrier metal layer 49 which is closest to the diaphragm portion 45, the diaphragm portion 45, and the temperature compensation ring 46.

Then, the computation steps S402 to S417 are sequentially carried out to finish the computation steps of the method for temperature compensation member in the capacitive sensor.

The above-described configuration applies the result of optimization of the parameter ΔC′ to the capacitive sensor 400. Thus, the capacitive sensor 400, configured to enjoy the barrier metal effect of the second barrier metal layer 49, can also detect a change in the capacitance between the diaphragm portion 45 and both the first electrode portion 43 and the second electrode portion 44 more accurately than in the conventional art.

Moreover, the above-described configuration applies the result of optimization of the parameter ΔC′ to the capacitive sensor. Thus, while configured to enjoy an effect enabling reliability of an electric connection between the second electrode portion 44 and the sealing ring portion 48 to be improved when the second electrode portion 44 and the sealing ring portion 48 are bonded together by a gold-gold bonding, the capacitive sensor 400 can also detect a change in the capacitance between the diaphragm portion 45 and both the first electrode portion 43 and the second electrode portion 44 more accurately than in the conventional art.

### Fifth Embodiment

Now, with reference to FIG. 19 to FIG. 22, a description will be given which concerns a computation program for a method for temperature compensation in a sensor and a computation processing device carrying out a computation process of the computation program, according to a fifth embodiment of the present invention.

(Configuration of a Computation Processing Device 500)

As shown in FIG. 19, a personal computer (computation processing device) 500 includes a display 51 that displays images, a keyboard 52 via which commands, numerical values, and the like are input, and a control device 53.

The control device 53 has a CPU 54 that controls devices in the personal computer 500, a hard disk 55, and a drive device 56. A CD-ROM 57 is removably installed in the drive device 56.

(Operation of the Computation Processing Device 500)

After the CD-ROM 57 is installed in the drive device 56, a program stored in the CD-ROM 57 (a computation program according to the fifth embodiment) is downloaded into the hard disk 55 in response to an instruction input via the keyboard 52.

(Computation Steps of the Computation Processing Device According to the Fifth Embodiment)

Now, computation steps of the computation processing device according to the fifth embodiment will be described with reference to FIG. 20 to FIG. 22. The computation steps shown in FIG. 20 to FIG. 22 are implemented by the CPU 54 by executing the program stored in the hard disk 55. The fifth embodiment carries out steps S501 to S507 in order which are similar to the computation steps S1 to S17 of the method for temperature compensation according to the first embodiment.

According to the above-described configuration, the personal computer 500 specifically executes the computation program according to the fifth embodiment to enjoy effects similar to the effects of the first embodiment.

The present invention is not limited to the above-described embodiments. The embodiments may be varied based on the spirits of the present invention without departing from the scope of the present invention. For example, as shown in FIG. 23, in a capacitive sensor 600 including a substrate 61, an insulator layer 62, a first electrode portion 63, a second electrode portion 64, a diaphragm portion 65, a temperature compensation ring 66, a sealing ring portion 68, and a second barrier metal layer 69 (69a and 69b) which are similar to the corresponding components of the capacitive sensor 400, a first barrier metal layer 60 may be formed which contains at least platinum and includes two layers, a layer 60a formed between the second electrode portion 64 and the insulator layer 62 like a ring similar to the second electrode portion 64, the layer 60a formed of titanium being located closest to the insulator layer 62, and a layer 60b formed of platinum and located closest to the second electrode portion 64. In this case, an inner circumferential surface of the first barrier metal layer 60 forms a closed space 67 along with an inner circumferential surface of the second barrier metal layer 69, an inner circumferential surface of the sealing ring portion 68, an inner surface of a recess 61a, an inner circumferential surface of a penetration portion 62a, an inner circumferential surface of the second electrode portion 64, and a surface of the diaphragm portion 65 on which the second barrier metal layer 69 is formed. Thus, the result of optimization of the parameter ΔC′ is applied to the capacitive sensor 600. Therefore, the capacitive sensor 600, configured to enjoy the barrier metal effect of the first barrier metal layer 60, can also detect a change in the capacitance between the diaphragm portion 65 and both the first electrode portion 63 and the second electrode portion 64 more accurately than in the conventional art.

In the example described above in the first to fifth embodiments, the Timoshenko's symmetric circular plate theory is applied to a composite circular plate with three layers including a layer closest to a diaphragm portion, the diaphragm portion, and a temperature compensation ring to obtain the parameter ΔC′, which enables determination of the degree of compensation for deformation of the diaphragm portion. However, the embodiments are not limited to this. The Timoshenko's symmetric circular plate theory may be applied to a composite circular plate with four or more layers including the three layers, the layer closest to the diaphragm portion, the diaphragm portion, and the temperature compensation ring, and an additional layer other than the layer closest to the diaphragm portion, the diaphragm portion, and the temperature compensation ring, to obtain the parameter ΔC′, which enables determination of the degree of compensation for the deformation of the diaphragm portion.

In the example described above in the fourth embodiment, the second barrier metal layer 49 includes a plurality of layers, that is, the layer 49a formed of platinum and located closest to the sealing ring 48 and the layer 49b formed of titanium and located closest to the diaphragm portion 45. However, the embodiments are not limited to this. As shown in FIG. 24, in a capacitive sensor 700 including a substrate 71, an insulator layer 72, a first electrode portion 73, a second electrode portion 74, a diaphragm portion 75, a temperature compensation ring 76, a closed space 77, and a sealing ring portion 78 which are similar to the corresponding portions of the capacitive sensor 400, the second barrier metal layer may have a single layer configuration including only a layer 79a formed of platinum. In this case, in the above-described computation step S401 (see FIG. 16), a composite circular plate configured such that the center axes of the layer 79a, the diaphragm portion 75, and the temperature compensation ring 76 align with one another is divided into a first segment (1) including a portion with a radius of 0 to R1 based on the center axis of the diaphragm portion 75 (the position where the radius r is zero), a second segment (2) including a portion with a radius of R1 to R2 based on the center axes of the diaphragm portion 75 and the temperature compensation ring 76, and a third segment (3) including a portion with a radius of R2 to R3 based on the center axes of the layer 79a, the diaphragm portion 75, and the temperature compensation ring 76, based on the Timoshenko's symmetric circular plate theory as is the case with the fourth embodiment.

In the example described above in the first embodiment, the temperature compensation ring 6 is shaped like a ring on the surface of the diaphragm portion 5 opposite to the surface of the diaphragm portion 5 on which the second electrode portion 4 is formed. However, the embodiments are not limited to this. By way of example, as shown in FIG. 25(a) and FIG. 25(b), in a capacitive sensor 800 including a substrate 81, an insulator layer 82, a first electrode portion 83, a second electrode portion 84, a diaphragm portion 85, and a closed space 87 which are similar to the corresponding portions of the capacitive sensor 100, temperature compensation members 86 each shaped generally like a rectangular parallelepiped may be arranged at every 90° along a circumferential direction of the diaphragm portion 85, on the surface of the diaphragm portion 85 opposite to the surface of the diaphragm portion 85 on which the second electrode portion 84 is formed. In this example, as shown in FIG. 25(a), a radially outward end surface of the temperature compensation member 86 is shaped identically to an outer circumferential surface of the diaphragm portion 85 (a thick line portion in FIG. 25(a)) as viewed in a stacking direction of the substrate 81 and the insulator layer 82. The temperature compensation member 86 may be disposed at any position and have any shape provided that the temperature compensation member 86 is in a condition optimum for temperature compensation. This also applies to the capacitive sensors 200 to 400 according to the other embodiments (the second to fourth embodiments).

In the example described above in the first embodiment, the temperature compensation ring 6 is formed on the surface of the diaphragm portion 5 opposite to the surface of the diaphragm portion 5 on which the second electrode portion 4 is formed. However, the embodiments are not limited to this. By way of example, as shown in FIG. 26(a) and FIG. 26(b), in a piezo-resistive physical quantity sensor (a sensor) 900 including a substrate 91, an insulator layer 92, a first electrode portion 93, a second electrode portion 94, a diaphragm portion 95, and a closed space 97 which are similar to the corresponding portions of the capacitive sensor 100, sets of a temperature compensation member 96 and a piezo element 98 shaped generally like rectangular parallelepipeds may be arranged at every 90° along a circumferential direction of the diaphragm portion 95, on the surface of the diaphragm portion 95 opposite to the surface of the diaphragm portion 95 on which the second electrode portion 94 is formed. In this example, as shown in FIG. 26(a), radially outward end surfaces of the temperature compensation member 96 and the piezo element 98 are shaped identically to an outer circumferential surface of the diaphragm portion 95 (a thick line portion in FIG. 26(a)) as viewed in a stacking direction of the substrate 91 and the insulator layer 92. The piezo-resistive physical quantity sensor 900 uses the piezo element 98, having a resistance value varying depending on strain of the diaphragm portion 95, to detect the value of a pressure applied to the diaphragm portion 95. Changes in the resistance value can be detected based on outputs from the first electrode portion 93 and the second electrode portion 94. A material for the piezo element 98 may be a piezoelectric material such as PZT (lead zirconate titanate). This also applies to the other embodiments (the second to fourth embodiments).

Furthermore, in the first to fifth embodiments described above, the conductive portion (electrode portion) is shaped like a circular ring, the diaphragm portion is shaped like a circle, and the temperature compensation member is a temperature compensation ring so that the shapes of the conductive portion, the diaphragm portion, and the temperature compensation member correspond to one another. However, the present invention is not limited to this combination. For example, for compensation for the deformation of the diaphragm portion caused by thermal expansion of a gas sealed in the closed space, the conductive portion (electrode portion) and the temperature compensation member may be shaped like rectangular rings and the diaphragm portion may be shaped like a rectangle so that the shapes of the conductive portion, the temperature compensation member, and the diaphragm portion correspond to one another. Of course, the conductive portion, the diaphragm portion, and the temperature compensation member may have any shapes provided that the conductive portion, the diaphragm portion, and the temperature compensation member are formed to compensate for the deformation of the diaphragm portion caused by thermal expansion of the gas sealed in the closed space.

