# DESCRIPTION

## BACKGROUND OF INVENTION

The present invention generally relates to an electromagnetic rotary drive and more particularly, to an electromagnetic rotary drive that functions as a bearingless motor-generator. Most particularly, the invention relates to a control system for a bearingless motor-generator.

Electromagnetic rotary drives are commonly used in standard motors as well as bearingless motor-generators. A conventional electromagnetic rotary drive includes a rotating part and a stationary part. The rotary part is commonly referred to as a rotor and the stationary part is commonly referred to as a stator. The stationary part supports a set of windings. A conventional control system for an electromagnetic rotary drive for a standard motor is shown in FIG. 1. The control system, generally indicated at 10, includes six switches 12, which control the flow of phase currents into a set of windings to produce forces, which exert a torque on a rotating part. However, this control system produces no forces for levitating the rotating part, since poles carry the same flux, and balance their forces out.

Unlike the standard motor described above, a conventional bearingless motor-generator produces forces for levitating the rotating part. An example of a bearingless motor-generator is described in U.S. Pat. No. 6,559,567, issued May 6, 2003, to Schob, the description of which is incorporated herein by reference. This bearingless motor-generator has a control system for an electromagnetic rotary drive that includes control devices, which control the flow of phase currents into two windings. The phase currents have a mutual phase shift of about 120°. The control system produces forces transverse to the windings. These transverse forces can be repulsive forces or attractive forces. By orienting the windings as described by Schob, the forces may be directed at an angle greater than 0° and less than 90° relative to the axis of rotation of the rotor. In this way, the rotor can be axially or radially levitated.

It should be noted that the bearingless motor-generator described above includes a drive winding for producing a drive field and a separate control winding for producing a control field. The drive field exerts a torque on the rotating part to rotate the rotating part and the control field exerts a force on the rotating part to levitate the rotating part.

A control system is needed that permits both drive and control fields to be produced from the same set of windings, thus eliminating the need to separate drive and control windings.

## SUMMARY OF INVENTION

The present invention is directed toward a control system for an electromagnetic rotary drive for bearingless motor-generators that meets the foregoing needs. The control system comprises a winding configuration comprising a plurality of individual pole pairs through which phase currents flow, each phase current producing both a lateral force and a torque.

The present invention is also directed toward a bearingless motor-generator. The motor-generator comprises a stator, a rotor supported for movement relative to the stator, and a control system. The motor-generator comprises a winding configuration supported by the stator. The winding configuration comprises at least three pole pairs through which phase currents flow resulting in three three-phase systems. Each phase system has a first rotor reference frame axis current that produces a levitating force with no average torque and a second rotor reference frame axis current that produces torque.

Various objects and advantages of this invention will become apparent to those skilled in the art from the following detailed description of the preferred embodiment, when read in light of the accompanying drawings.

## DETAILED DESCRIPTION

Referring now to the drawings, there is illustrated in FIG. 2 a cylindrical motor control system 20 for an electromagnetic rotary drive for use in a cylindrical bearingless motor-generator (hereinafter “motor”). It should be noted that the standard motor drive control system described above has only six switches 12, while the control system 20 shown in FIG. 2 has eighteen switches 22. As a consequence, the control system 20 can stimulate three systems of three phases. Each of these systems comprises a pole pair system, generally indicated at 24, resulting in three pole pair systems. Although there are three times as many switches, the required power rating for each switch 22 is much smaller than that for the conventional control system 10 described above. For example, if the number of turns in the motor is kept constant, the voltage switches 22 would be required to block would be one third of the normal system voltage of the conventional control system 10. If the motor is required to have the same bus voltage as the conventional control system 10, the number of winding turns could be increased and the switches 22 would only carry one third the normal current of the conventional control system 10. In addition, the new control system 20 provides fault tolerance. If any of the coils in the new control system 20 or the power electronics for a pole pair system 24 fails, the other two three-phase systems will still be able to provide motor torque and magnetic bearing forces.

A winding configuration with individually stimulated pole pairs is shown in FIG. 3. In this winding configuration, phase currents ia1, ia2, ia3, ib1, ib2, ib3, ic1, ic2, ic3 are defined in the three pole pairs 24 shown in FIG. 2. These are essentially three three-phase systems. The first system contains phase currents ia1, ib1, and ic1. This system can be transformed into a rotor reference frame with known transformations, as follows:

\(\begin{matrix}
{\begin{bmatrix}
i_{{qs}\; 1}^{r} \\
i_{{ds}\; 1}^{r} \\
i_{01}
\end{bmatrix} = {\begin{bmatrix}
{\cos \mspace{14mu} \theta_{r}} & {\cos \left( {\theta_{r} - \frac{2\pi}{3}} \right)} & {\cos \left( {\theta_{r} + \frac{2\pi}{3}} \right)} \\
{\sin \mspace{14mu} \theta_{r}} & {\sin \left( {\theta_{r} - \frac{2\pi}{3}} \right)} & {\sin \left( {\theta_{r} + \frac{2\pi}{3}} \right)} \\
\frac{1}{2} & \frac{1}{2} & \frac{1}{2}
\end{bmatrix}\begin{bmatrix}
i_{a\; 1} \\
i_{b\; 1} \\
i_{c\; 1}
\end{bmatrix}}} & (1)
\end{matrix}\)

FIG. 4 shows fictional coils (illustrating the manner in which the three three-phase systems operate), generally indicated at 26, 28, which rotate with the rotor 30 representing the rotor reference frame q and d-axis currents. It should be noted that the rotor reference frame d-axis current produces no average torque and the rotor reference frame q-axis current produces torque.

Note that while the d-axis current produces no torque, it does produce a lateral force. It should be noted what happens if the rotor reference frame d-axis currents are permitted to be different in the three different three-phase pole pairs 24, while keeping the rotor reference frame q-axis currents the same. FIG. 5 shows the force produced on the rotor 30 when 10 amps (first positive, then negative) is applied individually to each of the pole pairs 24 of the rotor reference frame d-axes while the other pole pairs have zero rotor reference frame d-axis and q-axis currents. FIG. 6 shows the magnitude of the force on the rotor 30 with ids1r=+10 A, and the rest of the rotor reference frame d-axis and q-axis currents set to zero. This force has an average value of 1.8 lbs. This force has a strong fourth harmonic ripple, and also a much smaller second harmonic component. The rotor force components in the x and y directions, which are plotted in FIG. 7, each have second harmonic ripples, and combine to generate the fourth harmonic ripple in the force.

The above results demonstrate that the forces generated by the rotor reference frame d-axis current idsr have fairly constant magnitudes. The force phases generated on the rotor using constant d-axis currents are plotted in FIG. 8. Note that this Fig. plots the phases of the force in mechanical degrees versus the electrical angle of the motor. The phases of the rotor forces generated by exciting separate rotational reference frame d-axis currents are 120 mechanical degrees apart from each other, and vary 46 mechanical degrees (+/−23 mechanical degrees) over an electrical revolution.

FIG. 9 shows the force vectors PP1, −PP1, PP2, −PP2, PP3, −PP3 that are possible with the different pole pairs 24. There are six possible force directions, using the positive and negative rotational reference frame d-axis currents. These forces bound six distinct regions. A desired force within any region can be produced optimally by using the vectors bordering that region as the basis. From this, a control system can be developed.

First, the phases of the six force vectors PP1, −PP1, PP2, −PP2, PP3, −PP3 need to be determined. By fitting the results in FIG. 8, the force phase β is calculated for each of the six force vectors PP1, −PP1, PP2, −PP2, PP3, −PP3 as a function of electrical angle of the rotor θr:

\(\begin{matrix}
{\beta_{1} = {4.3050 + {23.155 \cdot {\cos \left( {{2 \cdot \left( {\theta_{r} + 105} \right)}\frac{\pi}{180}} \right)}}}} & (2) \\
{\beta_{1 - {negative}} = {\beta_{1} + 180}} & (3) \\
{\beta_{2} = {\beta_{1} - 120}} & (4) \\
{\beta_{2 - {negative}} = {\beta_{2} + 180}} & (5) \\
{\beta_{3} = {\beta_{1} + 120}} & (6) \\
{\beta_{3 - {negative}} = {\beta_{3} + 180}} & (7)
\end{matrix}\)

During rotor levitation, the phase of the desired force is calculated and compared with the six available force vectors PP1, −PP1, PP2, −PP2, PP3, −PP3, and the two force vectors that border the region containing the desired force are then chosen as the basis. Next, the desired force is transformed from the x, y basis to the basis containing the phase of the two vectors to be used, βboundry-1, and βboundary-2. The transformation is performed using the following matrix:

\(\begin{matrix}
{P = \begin{bmatrix}
{{real}\left( ^{{j \cdot \beta_{{boundary} - 1}}\frac{180}{\pi}} \right)} & {{real}\left( ^{{j \cdot \beta_{{boundary} - 2}}\frac{180}{\pi}} \right)} \\
{{imag}\left( ^{{j \cdot \beta_{{boundary} - 1}}\frac{180}{\pi}} \right)} & {{imag}\left( ^{{j \cdot \beta_{{boundary} - 2}}\frac{180}{\pi}} \right)}
\end{bmatrix}} & (8)
\end{matrix}\)

This allows the two currents that make up the boundary to the region, ids-boundary1r, Ids-boundary2r, to be defined as follows.

\(\begin{matrix}
{\begin{bmatrix}
i_{{ds} - {{boundary}\; 1}}^{r} \\
i_{{ds} - {{boundary}\; 2}}^{r}
\end{bmatrix} = {P^{- 1} \cdot \begin{bmatrix}
\frac{F_{x - {com}}}{currentstiffness} \\
\frac{f_{y - {com}}}{currentstiffness}
\end{bmatrix}}} & (9)
\end{matrix}\)

where Fx-com and Fy-com are magnetic force bearing commands and current stiffness is a constant that determines the amount of force delivered to the rotor for 1 amp of current, in this case it is 0.18 lbs/A (per FIG. 6). This technique is used to generate various force commands; the results can be seen in FIG. 10. It should be noted that there may be some ripple in the force. This may be expected, as no attempt is made to reduce the natural ripple inherent to constant d-axis rotor reference frame current.

Now, a mechanical model of the rotor 30 is generated, with motor torques and forces as inputs, and the rotor angle, speed, lateral position and lateral velocity as outputs. This motor rotor is a mass which is free to move in the x and y directions, and begin by defining the following complex quantities:

x1=Posx+i·Posy

x2=Velx+i·Vely

where x1 and x2 are system states defining rotor lateral position and velocity, i is imaginary number, Posx and Posy are x and y rotor positions in inches, and Velx and Vely are x and y rotor positions in meters per second.

From Newton's second law:

F=ma=m·{dot over (x)}2

where F is force in Newtons, m is mass in kilograms.

With this information, the system can be described as follows:

\(\begin{matrix}
{\begin{bmatrix}
{\overset{.}{x}}_{1} \\
{\overset{.}{x}}_{2}
\end{bmatrix} = {{{\begin{bmatrix}
0 & 1 \\
0 & 0
\end{bmatrix}\begin{bmatrix}
x_{1} \\
x_{2}
\end{bmatrix}} + {\begin{bmatrix}
0 \\
\frac{1}{m}
\end{bmatrix}F}} = {{A\begin{bmatrix}
x_{1} \\
x_{2}
\end{bmatrix}} + {BF}}}} & (10)
\end{matrix}\)

where A and B are linear state space description matrices.

Note that the controllability matrix C of this system is:

\(\begin{matrix}
{C = {\left\lbrack {B\mspace{14mu} {A \cdot B}} \right\rbrack = \begin{bmatrix}
0 & \frac{1}{m} \\
\frac{1}{m} & 0
\end{bmatrix}}} & (11)
\end{matrix}\)

This matrix has full rank so the system is controllable. Now, angular quantities are defined as follows:

x3=θmechanical

x4=ωmechanical

where x3 and x4 are angular position and velocity, θmechaninical mechanical is the mechanical angle of the rotor in radians, and ωmechanical is mechanical speed in radians per second.

With these quantities, the angular system can be described as:

\(\begin{matrix}
{\begin{bmatrix}
{\overset{.}{x}}_{3} \\
{\overset{.}{x}}_{4}
\end{bmatrix} = {{\begin{bmatrix}
0 & 1 \\
0 & 0
\end{bmatrix}\begin{bmatrix}
x_{3} \\
x_{4}
\end{bmatrix}} + {\begin{bmatrix}
0 \\
\frac{1}{J}
\end{bmatrix}T}}} & (12)
\end{matrix}\)

where J is rotational inertia and T is torque in newton-meters.

The controllability matrix C of this system is:

\(\begin{matrix}
{C = {\left\lbrack {B\mspace{14mu} {A \cdot B}} \right\rbrack = \begin{bmatrix}
0 & \frac{1}{J} \\
\frac{1}{J} & 0
\end{bmatrix}}} & (13)
\end{matrix}\)

The controllability matrix is again full rank, thus the system is controllable.

Now the position of the rotor can be described using the differential equations above along with the calculated torques and forces.

As was mentioned previously, motor torque will be controlled by enforcing the same appropriate rotor reference frame q-axis currents iqsr on all three pole pair systems. Also, it has been demonstrated that any desired radial force can be obtained by correctly controlling the rotational reference frame d-axis currents in the individual pole pairs 24. Using the results above, a rudimentary magnetic bearing controller can be designed to levitate the rotor 30; the position will be controlled with a proportional derivative (PD) controller (not shown). The controller has negative stiffness compensation, which essentially cancels the negative stiffness due to the motor permanent magnets (PMs). This controller outputs a force command, which is broken down into three pole pair rotor reference frame d-axis currents ids1r, ids2r, id3r. The motor may have mechanical touchdown bearings (not shown) which prevent the rotor 30 from contacting the lamination stacks of the stator 32 (see FIG. 4); they limit rotor motion to within 10 mils of center. On startup, the rotor 30 will be resting on these bearings, thus, the rotor will be levitated from the starting point on the touchdown bearing. Obviously these dimensions are dependent on the physical characteristics of the motor.

When the controller is implemented, the rotor 30 is levitated off of the touchdown bearing with an initial speed, such as 100 radians per second, and a torque command, which in this example is zero (thus iqsr=0 for all three systems). FIG. 11 shows the x, y plot of the rotor during this levitation, and FIG. 12 shows the x-component of position versus time during the levitation. FIG. 13 shows the PD force command separated into the negative stiffness compensation, proportional gain, and derivative components. The phase currents during this levitation period are seen in FIG. 14. The currents can be fairly high when the rotor 30 is being pulled off the back up bearings but the currents should decrease dramatically as time increases, and the rotor approaches the center. Rotor imbalance and sensor noise are present in the system, and some amount of current will be required to hold the rotor 30 in the center of the touchdown bearing. The rotor 30 may be intentionally rotated around its center of mass instead of its geometric center, which minimizes levitation currents, although in this case the position will not necessarily be forced to center.

In order to show that this control system provides simultaneous motor and magnetic bearing action, levitation is repeated, this time with 50 A of rotor reference frame q-axis current. The x position during this levitation is plotted in FIG. 15. This figure shows that the time response of levitation does not appreciably change with motoring current.

The phase currents present while levitating with 50 A Iqsr are shown in FIG. 16. The peak current of 95 A is achieved briefly during levitation in Ia2. The maximum current reached during the levitation period with no Iqsr is 61 A, also in Ia2. So, it is apparent that for a particular force level, the motor should be de-rated from its maximum power level. However, in this example, the magnetic bearing function needs a large force only during levitation, to overcome the negative stiffness while lifting the rotor 30 off of the back-up bearing. If this is the only time a large amount of current is required, temporarily exceeding the maximum phase limit of the motor will not be a problem, since the excess current will be present for such a brief period that no appreciable wire heating will occur. Actually, during most applications, levitation will occur before motoring starts, so the added current requirement may not exist at all.

The relevant factor to be considered when selecting ratings is the force needed to levitate the rotor. This involves factors that are not considered, including sensor noise, shaft runout, and rotor imbalance. In addition to compensating for these factors, if the motor is used as a flywheel in a satellite, it may be necessary to levitate the rotor on earth before sending it to orbit, which would require that the bearing system be able to support the weight of the rotor 30. Furthermore, the motor may be used to provide attitude control of the satellite in addition to energy storage. In this application, the magnetic bearing should be able to keep the rotor 30 levitated while the spacecraft is rotated.

Two conical motors, wound with three separated pole pairs, can be used together with the aforementioned control system to fully levitate and spin a rotor. An example of a machine 34 having two such conical motors is shown in FIGS. 17-19. In the illustrated embodiment of the machine 34, a rotor 36 rotates on the outside of stators 38, although a machine may be configured with rotors that rotate on the inside of the stators. Information on the position of the rotor 36 is received by a controller with eight radial eddy current sensors 40 and four axial eddy current sensors 42.

An exemplary control system 44 for driving the two conical motors is shown in FIG. 20. One conical motor comprises windings 46 comprised of three three-phase pole pair systems 24. The other conical motor comprises windings 48 also comprised of three three-phase pole systems 24. One advantage of this type of motor drive control system is that it provides fault tolerance; if any switch 22 or pole pair system 24 fails, the other two three-phase systems 24 will still provide rotation and levitation forces.

FIG. 21 shows the force vectors that are possible with the different pole pair systems 24. There are six force vectors that have an axial component as well as a radial component.

FIG. 22 shows a schematic force generation control code. Radial force control blocks 50, 52 use a radial control technique, as discussed above in connection with the cylindrical motor control system. The conical motor essentially reduces the current stiffness, as compared to that required by a similarly sized cylindrical motor, since all of the magnitude of force is no longer directed radially. The radial force control block 50 controls the radial force applied to Plane 1, while the radial force control block 52 controls the force applied to Plane 2. A new control block 53 is introduced to control the axial force. FIG. 23 shows a schematic of this control block 53. The inputs to this control block 53 are the axial force command at 56 and the rotor reference frame d-axis current commands, which were generated with the radial force control blocks 50 and 52, at 58. Axial force is created when the total force acting on Plane 1 is different than the total force acting on Plane 2. Thus, if one plane is creating a large radial force, it will have the effect of creating some axial force. However, the resultant axial force can be compensated for by adding equal parts of d-axis current to all of the pole pair systems 24 on the other motor. The axial force created by the radial controllers is calculated by taking the sum of the rotor reference frame d-axis current commands from the radial controller at Plane 1 minus the sum of the rotor reference frame d-axis current commands from the radial controller at Plane 2, then multiplying by the current stiffness at 60. This calculated axial force is then simply subtracted from the commanded axial force. This value, calculated at 62, is added to the rotor reference frame d-axis current commands of Motor I (shown in FIG. 21) and subtracted from the rotor reference frame d-axis current commands of Motor II. The final rotor reference frame d-axis current commands at 64 are sent out of this axial force control block 53 to the standard rotor reference frame current regulators 66 in FIG. 24.

A position controller 68 in FIG. 24 receives position information from the sensors 40, 42 and outputs force commands necessary to maintain levitation. FIG. 25 shows one implementation of the position controller as a proportional-integral-derivative (PID) controller. Note that while this specific example uses a PID controller, any other suitable controller type can be used, as well. The commanded position is input at 70, while measured position is input at 72. A standard PID control loop is executed at 74. Force commands at 76 are the output of this block 68.

The present invention is not intended to be limited to the control system described above. Similarly, the present invention is not intended to be limited to any particular winding configuration. It should be appreciated that any suitable winding configuration may be used for carrying out the invention.

The aforementioned invention is not intended to be limited to the motor described above but can be used on other motors with six or more poles. Motors with which the invention can be used include, but are not limited to, induction motors, synchronous reluctance motors, and permanent magnet motors. The motors may be configured as cylindrical or conical, interior rotor/exterior stator, or exterior rotor/interior stator.

The principle and mode of operation of this invention have been explained and illustrated in its preferred embodiment. However, it must be understood that this invention may be practiced otherwise than as specifically explained and illustrated without departing from its spirit or scope.

