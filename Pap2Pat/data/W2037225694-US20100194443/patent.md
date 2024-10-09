# DESCRIPTION

## BACKGROUND OF THE INVENTION

1. Field of the Invention

The present invention relates to electronics and, more specifically, to voltage-to-current (V/I) converters having an exponential transfer function.

2. Description of the Related Art

This section introduces aspects that may help facilitate a better understanding of the invention(s). Accordingly, the statements of this section are to be read in this light and are not to be understood as admissions about what is in the prior art or what is not in the prior art.

An exponential (or dB-linear) voltage-to-current (V/I) converter is a key component for the design of automatic gain-control (AGC) circuits, which are used in a variety of applications, such as wireless communications devices, hearing aids, and disk drives. A representative AGC circuit employs an exponential V/I converter in the feedback loop that controls the gain of a variable-gain amplifier (VGA). The exponential characteristic of the V/I converter enables the AGC circuit to advantageously have a substantially constant settling time for a variety of initial input-signal conditions, which is very desirable for the above-specified applications. Additional details on the use of exponential V/I converters in AGC circuits can be found, e.g., in U.S. Pat. No. 6,369,618, which is incorporated herein by reference in its entirety.

One problem with exponential V/I converters is that they are not straightforwardly amenable to implementation in CMOS technology. More specifically, unlike bipolar transistors, which have an inherent exponential transfer characteristic, MOSFET transistors have a square-law transfer characteristic in strong inversion. As a result, designing a CMOS V/I converter that exhibits an exponential transfer characteristic and has other desirable properties is relatively difficult.

## SUMMARY OF THE INVENTION

Problems in the prior art are addressed by various embodiments of an exponential (or dB-linear) voltage-to-current (V/I) converter that is amenable to implementation in CMOS technology. In a representative embodiment, the exponential V/I converter has a voltage scaler, a current multiplier, and an exponential current converter serially connected to one another. The voltage scaler supplies an input current to the current multiplier based on an input voltage. The current multiplier multiplies the input current and a current proportional to absolute temperature and supplies the resulting current to the exponential current converter. The exponential current converter has a differential MOSFET pair operating in a sub-threshold mode and generating an output current that is proportional to a temperature-independent, exponential function of the input voltage. Advantageously, the exponential V/I converter can be implemented to have a dB-linear operation range as wide as about 40 dB.

According to one embodiment, provided is a device having (A) a current multiplier that multiplies a first current and a current proportional to absolute temperature to generate a second current; and (B) an exponential converter that applies an exponential transfer function to the second current to generate an output current. The exponential transfer function depends on a thermal voltage. Temperature dependence of the current proportional to absolute temperature counteracts temperature dependence of the thermal voltage to cause the output current to be proportional to a temperature-independent, exponential function of the first current over an operating range of the device.

According to another embodiment, provided is a method having the steps of: (A) multiplying a first current and a current proportional to absolute temperature to generate a second current; and (B) applying an exponential transfer function to the second current to generate an output current. The exponential transfer function depends on a thermal voltage. Temperature dependence of the current proportional to absolute temperature counteracts temperature dependence of the thermal voltage to cause the output current to be proportional to a temperature-independent, exponential function of the first current over a specified operating range.

According to yet another embodiment, provided is a device having (A) means for multiplying a first current and a current proportional to absolute temperature to generate a second current; and (B) means for applying an exponential transfer function to the second current to generate an output current. The exponential transfer function depends on a thermal voltage. Temperature dependence of the current proportional to absolute temperature counteracts temperature dependence of the thermal voltage to cause the output current to be proportional to a temperature-independent, exponential function of the first current over an operating range of the device.

## DETAILED DESCRIPTION

FIG. 1 shows a block diagram of an exponential (or dB-linear) voltage-to-current (V/I) converter 100 according to one embodiment of the invention. Converter 100 receives input voltage Vin and converts it into output current Iout so that there is an exponential relationship between the input voltage and the output current. As further described below, converter 100 is amenable to implementation in CMOS technology and is advantageously capable of maintaining the exponential transfer characteristic over a relatively wide (e.g., about 40 dB) output-current range.

Converter 100 has a voltage scaler 110 that conditions input voltage Vin for further processing in the subsequent circuit blocks of the converter. More specifically, voltage scaler 110 scales input voltage Vin and adds bias voltage Vbias to the scaled voltage according to Eq. (1):

V110=Vbias+γVin   (1)

where V110 is the output voltage of the voltage scaler, and γ is a scaling factor. In one embodiment, one or both of bias voltage Vbias and scaling factor γ are programmable so that output voltage V110 remains in an optimal range for the entire variability range of input voltage Vin. In a representative embodiment, |Vbias|≈0.2V and γ≈0.5.

Converter 100 applies output voltage V110 to resistive load R0, which drives current I1 through that load. In effect, the combination of voltage scaler 110 and resistive load R0 serves as a voltage-to-current converter that converts input voltage Vin into current I1. The subsequent signal processing in converter 100 is current-based and converts current I1 into output current Iout.

Converter 100 further has a current multiplier 120 whose output current I2 is expressed according to Eq. (2):

I2=ηI1IPTAT   (2)

where η is a constant, and IPTAT is a current proportional to absolute temperature (PTAT). In effect, current multiplier 120 generates output current I2 by multiplying the input current (i.e., current I1) and current IPTAT As further described below, the temperature proportionality of current IPTAT is utilized to make the exponential transfer characteristic of converter 100 substantially temperature independent and enable the converter to operate accurately and reliably in a variety of ambient conditions without a thermostat.

Output current I2 produced by current multiplier 120 is applied to an exponential current converter 130 that converts output current I2 into output current I3 according to Eq. (3):

\(\begin{matrix}
{I_{3} = {A\; {\exp \left( {\sigma \frac{I_{2}}{V_{T}}} \right)}}} & (3)
\end{matrix}\)

where A and σ are constants, and VT is the thermal voltage (=kBT/q, where kB is the Boltzmann constant, T is temperature in Kelvin, and q is the electron charge). Eqs. (2) and (3), taken together, indicate that current multiplier 120 and exponential current converter 130 work together to provide a substantially temperature-independent, exponential transfer function between currents I1 and I3. More specifically, according to Eqs. (2) and (3), the argument of the exponent in Eq. (3) contains current IPTAT and thermal voltage VT in the nominator and denominator, respectively. Since both current IPTAT and thermal voltage VT are linear functions of temperature, their temperature dependencies cancel each other, thereby causing the exponential transfer function between currents I1 and I3 to be substantially temperature independent.

Exponential current converter 130 applies output current I3 to a current limiter 140, where it is processed to generate output current Iout. More specifically, current limiter 140 imposes lower limit Imin and upper limit Imax onto current I3. If the magnitude of current I3 is smaller than lower limit Imin, then current limiter 140 forces Iout≧Imin. If the magnitude of current I3 is larger than upper limit Imax, then current limiter 140 forces Iout≈Imax. If the magnitude of current I3 is between lower limit Imin and upper limit Imax, then current limiter 140 forces Iout≈I3.

FIG. 2 shows a circuit diagram of a voltage scaler 200 that can be used as voltage scaler 110 according to one embodiment of the invention. Voltage scaler 200 has a reference current source 202, an operational amplifier 204, and four resistors R1-R4 interconnected as shown in FIG. 2. If R1>>R2, then voltage scaler 200 implements the transfer function defined by Eq. (1), wherein:

\(\begin{matrix}
{V_{bias} \approx {I_{ref}\frac{R_{2}\left( {R_{3} + R_{4}} \right)}{R_{3}}}} & \left( {4a} \right) \\
{\gamma \approx \frac{R_{2}\left( {R_{3} + R_{4}} \right)}{R_{1}R_{3}}} & \left( {4b} \right)
\end{matrix}\)

where Iref is the current generated by reference current source 202. Note that resistor R1 is a programmably variable resistor, which enables programmability of scaling factor γ. In one embodiment, reference current source 202 is a programmably variable current source, which enables programmability of bias voltage Vbias.

FIG. 3 shows a circuit diagram of a current multiplier 300 that can be used as current multiplier 120 according to one embodiment of the invention. Current multiplier 300 has two nested differential amplifiers, each having an active current-mirror load. The active devices of the first (outer) differential amplifier are MOSFET transistors M5 and M6, and the load of that differential amplifier is the current mirror formed by transistors MOSFET M1 and M2. Similarly, the active devices of the second (inner) differential amplifier are transistors MOSFET M7 and M8, and the load of that differential amplifier is the current mirror formed by MOSFET transistors M3 and M4. The gates of transistors M5 and M7 are both electrically connected to a common node having floating voltage Vx. The gates of transistors M6 and M8 are both electrically connected to a common node that receives reference voltage Vref.

In one embodiment, reference voltage Vref is supplied by a programmable reference-voltage source (not explicitly shown in FIG. 3). The voltage source is programmed to set a value of Vref so that there is a desired relationship between output current I2 and input voltage Vin. In particular, Vref is selected from a voltage range, wherein, if Vref changes, then the transfer function between output current I2 and input voltage Vin is translated along the voltage axis without changing its slope.

Current multiplier 300 further has reference current sources 302 and 304 that function as tail supplies of the outer and inner differential amplifiers, respectively. Current source 302 is designed to generate reference current Ibgap that does not depend on the technological process used in the fabrication of current multiplier 300 or on the temperature of the current multiplier. In one embodiment, current source 302 can be implemented, as known in the art, using a conventional bandgap circuit. Current source 304 is designed to generate temperature-dependent PTAT current IPTAT (see also Eq. (2)). In one embodiment, current source 304 can be a PTAT current source disclosed, e.g., in U.S. Patent Application Publication No. 2008/0284493, which is incorporated herein by reference in its entirety. In one configuration, current source 304 generates current IPTAT so that, at room temperature (T0=298 K), IPTAT=Ibgap.

Operation of transistors M5-M8 in current multiplier 300 is described by Eqs. (5a)-(5d), respectively:

\(\begin{matrix}
{\frac{I_{bgap} + I_{1}}{2} = {\frac{1}{2}\mu_{n}C_{ox}\frac{W_{1}}{l_{1}}\left( {V_{x} - V_{a} - V_{th}} \right)^{2}}} & \left( {5a} \right) \\
{\frac{I_{PTAT} + I_{2}}{2} = {\frac{1}{2}\mu_{n}C_{ox}\frac{W_{2}}{l_{2}}\left( {V_{x} - V_{b} - V_{th}} \right)^{2}}} & \left( {5b} \right) \\
{\frac{I_{bgap} - I_{1}}{2} = {\frac{1}{2}\mu_{n}C_{ox}\frac{W_{1}}{l_{1}}\left( {V_{ref} - V_{a} - V_{th}} \right)^{2}}} & \left( {5c} \right) \\
{\frac{I_{PTAT} - I_{2}}{2} = {\frac{1}{2}\mu_{n}C_{ox}\frac{W_{2}}{l_{2}}\left( {V_{ref} - V_{b} - V_{th}} \right)^{2}}} & \left( {5d} \right)
\end{matrix}\)

where μn is the mobility of electrons; Cox is the capacitance of the oxide layer; W1 and l1 are the width and length, respectively, of transistors M5 and M6; W2 and l2 are the width and length, respectively, of transistors M7 and M8; Va and Vb are the voltages indicated in FIG. 3; and Vth is the threshold voltage. If transistors M5-M8 are implemented so that

\({\frac{\left( {W_{1}/l_{1}} \right)}{\left( {W_{2}/l_{2}} \right)} = 1},\)

then Vx≈Vref and Eqs. (5a)-(5d) reduce to Eq. (2), wherein η=(Ibgap)−1.

If current multiplier 300 is used in V/I converter 100 to implement current multiplier 120, then the following relationship exists between input voltage Vin and current I1:

I1=αVin+ic   (6)

where α=γ/R0 and ic=(Vbias−Vref)/R0. Note that, for a given configuration of V/I converter 100, α and ic are constants.

FIG. 4 shows a circuit diagram of an exponential current converter 400 that can be used as exponential current converter 130 according to one embodiment of the invention. Exponential current converter 400 has a differential pair of MOSFET transistors M1 and M2 that are configured to operate in a sub-threshold mode (also referred to as a cut-off or weak-inversion mode). The gates of transistors M1 and M2 are electrically connected through resistor R12. The gate of transistor M2 receives bias voltage Vbias1 from a bias-voltage generator 410. Transistor M3 serves as a tail supply for the differential pair. A current source 402 drives reference current Iref1 through transistor M2. A current source 404 and transistor M4 are used to appropriately bias transistors M2 and M3.

As known in the art, drain-to-source current Ids in a MOSFET transistor operating in a sub-threshold mode varies exponentially with gate-to-source voltage Vgs, as expressed by Eq. (7):

\(\begin{matrix}
{I_{ds} \approx {I_{0}{\exp \left( \frac{V_{gs} - V_{th}}{{nV}_{T}} \right)}}} & (7)
\end{matrix}\)

where I0 is a constant; and n=1+CD/Cox, where CD is the capacitance of the depletion layer. Applying Eq. (7) to transistor M2, one finds that:

\(\begin{matrix}
{I_{{ref}\; 1} \approx {I_{0}{\exp \left( \frac{V_{{bias}\; 1} - V_{s} - V_{th}}{{nV}_{T}} \right)}}} & (8)
\end{matrix}\)

where Vs is the voltage indicated in FIG. 4. Further applying Eq. (7) to transistor M1 and then using Eq. (8), one finds that:

\(\begin{matrix}
{{I_{3} \approx {I_{0}{\exp \left( \frac{V_{{bias}\; 1} + {I_{2}R_{12}} - V_{s} - V_{th}}{{nV}_{T}} \right)}}} = {I_{{ref}\; 1}{\exp \left( \frac{I_{2}R_{12}}{{nV}_{T}} \right)}}} & (9)
\end{matrix}\)

Note that Eq. (9) is equivalent to Eq. (3), wherein A=Iref1 and σ=R12/n.

If current multiplier 300 and exponential current converter 400 are used in V/I converter 100 to implement current multiplier 120 and exponential converter 130, respectively, then the following relationship exists between input voltage Vin and current I3:

\(\begin{matrix}
{{I_{3} = {B\; {\exp \left( {\beta \; V_{i\; n}} \right)}}}{where}{B = {{I_{{ref}\; 1}{\exp \left( \frac{R_{12}I_{PTAT}i_{c}}{{nV}_{T}I_{bgap}} \right)}\mspace{14mu} {and}\mspace{14mu} \beta} = {\frac{\alpha \; R_{12}I_{PTAT}}{{nV}_{T}I_{bgap}}.}}}} & (10)
\end{matrix}\)

Note that, for a given configuration of V/I converter 100, B and β are constants that do not depend on the temperature because the temperature dependencies of current IPTAT and thermal voltage VT substantially cancel each other. Thus, Eq. (10) indicates that V/I converter 100 employing current multiplier 300 and exponential current converter 400 provides a temperature-independent, exponential transfer function between input voltage Vin and current I3. In addition, current multiplier 300 and exponential current converter 400 are advantageously capable of exhibiting a dB-linear transfer function over a relatively wide (e.g., about 40 dB) operation range because the exponential current converter invokes the inherent exponential characteristic of MOSFET transistors in the sub-threshold operating mode.

FIG. 5 shows a circuit diagram of a current limiter 500 that can be used as current limiter 140 according to one embodiment of the invention. Current limiter 500 has reference current sources 502 and 504, an operational amplifier 506 with a feedback network, and two current mirrors formed by transistors M1, M4, M5, and M6. Reference current Iref3 generated by current source 502 sets the minimum output current for current limiter 500. Reference current Iref2 generated by current source 504 sets the maximum output current for current limiter 500.

Current source 502 sets the minimum output current for current limiter 500 because it is directly connected to an output terminal 508 of the current limiter. As a result, output current Iout has at least a current component corresponding to reference current Iref3. Hence, output current Iout does not drop below the value of Iref3 even if current I3 becomes zero.

Current source 504 sets the maximum output current for current limiter 500 in the following manner. Transistors M1 and M2 have substantially the same size, which causes the value of Iref2 to set the ON/OFF level for transistor M3. More specifically, if current I3 is smaller than Iref2, then operational amplifier 506 holds transistor M3 in the OFF state. As a result, the two current mirrors formed by transistors M1, M4, M5, and M6 force output current Iout to mirror current I3. However, if current I3 is greater than Iref2, then operational amplifier 506 turns ON transistor M3, which sinks the excess current and causes the current flowing through transistor M1 to remain at the value of Iref2. The two current mirrors then mirror the current flowing through transistor M1 onto output terminal 508, thereby substantially forcing output current Iout not to exceed the value of Iref3.

While this invention has been described with reference to illustrative embodiments, this description is not intended to be construed in a limiting sense. Although certain embodiments of the invention have been described in reference to NMOS technology, the invention is not so limited. Various circuits of the inventions can also be implemented using the PMOS technology, the bipolar CMOS technology, and various non-MOS technologies, including implementations in an integrated circuit. Various modifications of the described embodiments, as well as other embodiments of the invention, which are apparent to persons skilled in the art to which the invention pertains are deemed to lie within the principle and scope of the invention as expressed in the following claims.

As used herein, the term dB-linear means that, when plotted on a logarithmic scale over an operation range, the output current is a substantially linear function of the input voltage (or current), wherein slope of the linear function does not deviate from a specified value by more than about ±5%.

Unless explicitly stated otherwise, each numerical value and range should be interpreted as being approximate as if the word “about” or “approximately” preceded the value of the value or range.

It will be further understood that various changes in the details, materials, and arrangements of the parts which have been described and illustrated in order to explain the nature of this invention may be made by those skilled in the art without departing from the scope of the invention as expressed in the following claims.

Although the elements in the following method claims, if any, are recited in a particular sequence with corresponding labeling, unless the claim recitations otherwise imply a particular sequence for implementing some or all of those elements, those elements are not necessarily intended to be limited to being implemented in that particular sequence.

Reference herein to “one embodiment” or “an embodiment” means that a particular feature, structure, or characteristic described in connection with the embodiment can be included in at least one embodiment of the invention. The appearances of the phrase “in one embodiment” in various places in the specification are not necessarily all referring to the same embodiment, nor are separate or alternative embodiments necessarily mutually exclusive of other embodiments. The same applies to the term “implementation.”

Also for purposes of this description, the terms “couple,” “coupling,” “coupled,” “connect,” “connecting,” or “connected” refer to any manner known in the art or later developed in which energy is allowed to be transferred between two or more elements, and the interposition of one or more additional elements is contemplated, although not required. Conversely, the terms “directly coupled,” “directly connected,” etc., imply the absence of such additional elements.

Transistors are typically shown as single devices for illustrative purposes. However, it is understood by those with skill in the art that transistors will have various sizes (e.g., gate width and length) and characteristics (e.g., threshold voltage, gain, etc.) and may consist of multiple transistors coupled in parallel to get desired electrical characteristics from the combination. Further, the illustrated transistors may be composite transistors.

As used in the claims, the terms “source,” “drain,” and “gate” should be understood to refer either to the source, drain, and gate of a MOSFET or to the emitter, collector, and base of a bi-polar device when the present invention is implemented using bi-polar transistor technology.

