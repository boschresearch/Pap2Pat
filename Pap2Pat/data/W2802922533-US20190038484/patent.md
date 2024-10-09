# DESCRIPTION

## FIELD OF THE INVENTION

This invention relates to wheelchairs having inertial sensors for providing information used to control neural stimulation of the wheelchair user.

## BACKGROUND

For people with spinal cord injuries who have lost the ability to control their trunk muscles, minor disturbances, such as a sharp turn or a collision with a curb, can destabilize the user and cause a loss of erect sitting posture, potentially leading to injurious falls. Falls are in fact the leading cause of injury for wheelchair users, and account for over 66,000 wheelchair related injuries per year. The injuries can be serious and include lacerations, contusions, abrasions, fractures and can result in death. According to at least one survey of people having spinal cord injuries, trunk stability is among the top functions they would like to see restored. There is clearly an opportunity to improve the safety of wheelchair users by increasing trunk stability.

Loss of control of trunk muscles also reduces the efficiency of manual propulsion of wheelchairs. Wheelchair users with poor trunk control due to paralysis of core thigh, hip and trunk muscles have limited trunk stability and may be unable to fully or safely lean backward and forward, resulting in inefficient pushing of the wheelchair. The inability to efficiently propel the wheelchair can make traversing challenging terrain, such as inclined ramps, difficult and can also lead to shoulder injuries. There is clearly an opportunity to improve the efficiency of wheelchair propulsion by increasing or restoring a degree of trunk control.

## SUMMARY

The invention concerns a wheelchair system providing neural stimulation to a user. In one example embodiment the system comprises a wheelchair. A sensor is positioned on the wheelchair for measuring a motion parameter thereof and generating one or more signals indicative of the motion parameter. A plurality of neural stimulating electrodes are attached to the user, each electrode attached to a respective muscle of the user for activating the respective muscle. A controller is in communication with the sensor and is adapted to receive the signals. The controller is also in communication with the plurality of electrodes for activating selected ones of the respective muscles in response to the signals.

The controller may be mounted on the wheelchair or the user. The motion parameter may comprise a linear motion parameter. The linear motion parameter is oriented in a direction of motion of the wheelchair and may be selected from the group consisting of linear velocity, linear acceleration and combinations thereof. The electrodes are attached to muscles selected from the group consisting of erector spinae, quadratus lumborum, gluteus maximus, posterior adductor and combinations thereof. The electrodes may be implanted beneath the user's skin or on a surface of the user's skin. The motion parameter may also comprise an angular motion parameter. The angular motion parameter is oriented about a turning axis of the wheelchair and may be selected from the group consisting of angular acceleration, angular velocity, and combinations thereof. The electrodes are attached to muscles selected from the group consisting of right erector spinae, right quadratus lumborum, right gluteus maximus, right posterior adductor, left erector spinae, left quadratus lumborum, left gluteus maximus, left posterior adductor and combinations thereof. The electrodes may be implanted beneath the user's skin or mounted on a surface of the user's skin.

In an example embodiment the sensor comprises an inertial measurement unit. Further by way of example, the sensor comprises at least one gyroscope and at least one accelerometer. In another example, the sensor comprises a radio frequency transmitter for wirelessly transmitting the signals to the controller. In an example embodiment the controller comprises a radio frequency receiver for receiving the signals and a microprocessor in communication with the receiver. In another example a seat belt controlled by a motor is mounted on the wheelchair. The controller controls the motor for tightening the belt. Further by way of example, a brake, controlled by an actuator, is mounted on the wheelchair, the controller controlling the actuator for applying the brake. In another example a distress indicator controlled by the controller for broadcasting a distress call.

The invention also encompasses a method of providing neural stimulation to a user of a wheelchair based upon motion of the wheelchair. In one example embodiment the method comprises:


- - measuring a motion parameter of the wheelchair;
  - generating a signal indicative of the motion parameter;
  - evaluating the signal;
  - activating at least one muscle of the user in response to the
    signal.

In one example, measuring the motion parameter comprises measuring a linear velocity of the wheelchair. By way of example, measuring the motion parameter comprises measuring a linear acceleration of the wheelchair or measuring an angular acceleration of the wheelchair or measuring an angular velocity of the wheelchair. By way of example, generating a signal comprises generating a signal indicative of at least one motion parameter selected from the group consisting of a linear velocity, a linear acceleration, an angular velocity, an angular acceleration, and combinations thereof. By way of example, evaluating the signal comprises converting the signal to a value indicative of a magnitude of the motion parameter and comparing the magnitude to a threshold magnitude of the motion parameter. In another example, evaluating the signal comprises converting the signal to a value indicative of a direction of the motion parameter and comparing the direction to a reference direction.

In an example embodiment, activating at least one muscle of the user in response to the signal comprises selecting one or more muscles of the user and applying a neural stimulus to activate the one or more muscles. By way of example, selecting one or more muscles of the user comprises selecting the erector spinae, quadratus lumborum, gluteus maximus, and posterior adductor muscles when the motion parameter is a linear acceleration which exceeds a threshold value. Further by way of example, selecting one or more muscles of the user comprises selecting right erector spinae, right quadratus lumborum, right gluteus maximus, and right posterior adductor muscles when the motion parameter is an angular acceleration or an angular velocity in a counterclockwise direction about a turning axis. Also by way of example, selecting one or more muscles of the user comprises selecting left erector spinae, left quadratus lumborum, left gluteus maximus, and left posterior adductor muscles when the motion parameter is an angular acceleration or an angular velocity in a clockwise direction about a turning axis.

The invention also encompasses method of providing neural stimulation to a user of a wheelchair based upon motion of the wheelchair during a collision. In an example embodiment the method comprises:


- - monitoring linear acceleration in a direction of motion of the
    wheelchair;
  - calculating a moving root mean square of the linear acceleration and
    comparing it against a first predetermined threshold value;
  - comparing a derivative of the root mean square linear acceleration
    against a second predetermined threshold value;
  - calculating a change in velocity using the linear acceleration and
    comparing the change in velocity to a third predetermined threshold
    value;
  - applying neuromuscular stimulation if the first, second and third
    predetermined threshold values are exceeded within a predetermined
    time period.

An example method of applying a restraint to a user of a wheelchair based upon motion of the wheelchair is also contemplated and comprises:


- - measuring a motion parameter of the wheelchair;
  - generating a signal indicative of the motion parameter;
  - evaluating the signal;
  - activating at least one the restraint in response to the signal.

By way of example, measuring the motion parameter comprises measuring a linear velocity of the wheelchair, measuring a linear acceleration of the wheelchair measuring an angular acceleration of the wheelchair or measuring an angular velocity of the wheelchair. In an example embodiment, generating a signal comprises generating a signal indicative of at least one the motion parameter selected from the group consisting of a linear velocity, a linear acceleration, an angular velocity, an angular acceleration, and combinations thereof.

In an example method, evaluating the signal comprises converting the signal to a value indicative of a magnitude of the motion parameter and comparing the magnitude to a threshold magnitude of the motion parameter. Also by way of example, evaluating the signal comprises converting the signal to a value indicative of a direction of the motion parameter and comparing the direction to a reference direction. Further by way of example, activating at least one restraint in response to the signal is selected from the group consisting of tightening a belt securing the user to the wheelchair, applying a brake to slow the wheelchair, broadcasting a distress signal and combinations thereof.

The invention further encompasses a system for providing assistance to a user for manual propulsion of a wheelchair. In one example embodiment the system comprises at least one sensor positioned on the user for measuring a motion parameter of the user while propelling the wheelchair. The at least one sensor generate one or more signals indicative of the motion parameter. A plurality of neural stimulating electrodes are positioned on the user, each electrode is attached to a respective muscle of the user for activating the respective muscle. A controller is in communication with the at least one sensor and adapted to receive the signals. The controller is also in communication with the plurality of electrodes for activating selected ones of the respective muscles in response to the signals. In one example embodiment the controller is mounted on either the wheelchair or the user. By way of examome, at least one sensor is mounted on the user in a position selected from the group consisting of an upper trunk of the user, a shoulder of the user, an arm of the user, a wrist of the user, a head of the user and combinations thereof. Further by way of example, the motion parameter is selected from the group consisting of a position of a part of the user, an acceleration of a part of the user, a rate of change of acceleration of a part of the user, an electrical potential of a muscle of the user, and combinations thereof. By way of example, the part of the user is selected from the group consisting of an upper trunk of the user, a shoulder of the user, an arm of the user, a wrist of the user, a head of the user and combinations thereof. In an example embodiment, the electrodes are attached to muscles selected from the group consisting of hip flexor muscles, hip extensor muscles, trunk flexor muscles, trunk extensor muscles, abdominal muscles and combinations thereof. By way of example, the electrodes are implanted beneath the user's skin or are mounted on a surface of the user's skin.

In an example embodiment, the at least one sensor comprises an inertial measurement unit. Further by way of example, the at least one sensor comprises at least one accelerometer. In another example, the at least one sensor comprises at least one electromyographic sensor. Also by way of example, the at least one sensor comprises a radio frequency transmitter for wirelessly transmitting the signals to the controller.

The invention also encompasses a method of providing assistance to a user for manually propelling a wheelchair. In one example embodiment, the method comprises:


- - detecting when the user has recovered from a previous push of the
    wheels of the wheelchair;
  - the user executing a next push of the wheels;
  - applying neural stimulation to trunk and hip flexor muscles of the
    user while the user executes the next push of the wheels;
  - detecting when the user has completed the next push of the wheels;
  - removing neural stimulation to the trunk and the hip flexor muscles
    of the user when the user has completed the next push of the wheels;
  - the user recovering from the next push of the wheels;
  - applying neural stimulation to trunk and hip extensor muscles of the
    user while the user is recovering from the next push of the wheels;
  - detecting when the user has recovered from the next push of the
    wheels;
  - removing neural stimulation from the trunk and the hip extensor
    muscles of the user when the user has recovered from the next push
    of the wheels.

In an example embodiment, detecting when the user has recovered comprises measuring a motion parameter of a part of the user while the user is recovering. In an example embodiment, the motion parameter is selected from the group consisting of a position of a part of the user, an acceleration of a part of the user, a rate of change of acceleration of a part of the user, an electrical potential of a muscle of the user and combinations thereof. In an example embodiment, the part of the user is selected from the group consisting of an upper trunk of the user, a shoulder of the user, an arm of the user, a wrist of the user, a head of the user, and combinations thereof.

By way of example, detecting when the user has completed the push of the wheels comprises measuring a motion parameter of the user while the user is pushing the wheels. In an example embodiment, the motion parameter is selected from the group consisting of a position of a part of the user, an acceleration of a part of the user, a rate of change of acceleration of a part of the user, an electrical potential of a muscle of the user and combinations thereof. Further by way of example, the part of the user is selected from the group consisting of an upper trunk of the user, a shoulder of the user, an arm of the user, a wrist of the user, a head of the user, and combinations thereof. In an example embodiment, detecting when the user has recovered comprises measuring anterior-posterior acceleration of a wrist of the user. Further by way of example, the method comprises measuring a rate of change of the anterior-posterior acceleration. Also by way of example, the method comprises measuring a rate of change of a medial-lateral acceleration of the wrist. In an example embodiment, detecting when the user has completed the push comprises measuring anterior-posterior acceleration of a wrist of the user. By way of example, the method may also comprise measuring a rate of change of the anterior-posterior acceleration. An example embodiment further comprises measuring a medial-lateral acceleration of the wrist.

In an example embodiment, detecting when a user has completed a push of the wheels comprises:


- - detecting an acceleration signal indicative of anterior-posterior
    acceleration of a part of the user greater than a predetermined
    threshold value;
  - detecting an increasing rate of change of the acceleration signal;
  - detecting a medial-lateral acceleration of the part of the user
    within a predetermined range of values.

By way of example, detecting when a user has recovered from a push of the wheels comprises:


- - detecting an acceleration signal indicative of anterior-posterior
    acceleration of a part of the user less than a predetermined
    threshold value;
  - detecting a decreasing rate of change of the acceleration signal;
  - detecting a medial-lateral acceleration of the part of the user
    having an increasing rate of change.

In an example embodiment, the part of the user comprises a wrist.

## DETAILED DESCRIPTION

FIGS. 1 and 2 show an example embodiment of a wheelchair system 10 according to the invention. System 10 comprises a wheelchair 12. A motion sensor 14 is positioned on the wheelchair 12. Motion sensor 14 measures one or more motion parameters of wheelchair 12 and generates signals indicative of the motion parameters. In an example embodiment the sensor 14 may be an inertial measurement unit (IMU) including accelerometers for measuring motion parameters such as acceleration of the wheelchair 12 in three mutually perpendicular axes (X, Y and Z as defined in FIG. 1) as well as one or more gyroscopes for measuring motion parameters such as angular velocity and angular acceleration of the wheelchair about the axes X, Y and Z. The sensor 14 also includes a radio frequency transmitter 16 used to transmit the signals wirelessly. A controller 18 is also part of system 10. In this example the controller 18 is also mounted on the wheelchair 12 but in another embodiment may be worn by (mounted on) the user 20. In the example embodiment shown controller 18 comprises a radio frequency receiver 22 for receiving signals from the sensor 14, and a microprocessor 24 in communication with receiver 22. The microprocessor may be, for example, a programmable logic controller. Software resident in the microprocessor 24 evaluates the signals from the sensor 14 and directs the microprocessor to issue commands to one or more of a plurality of neural stimulating electrodes 26, also part of system 10. Communication between controller 18 and electrodes 26 may be via wires or wirelessly.

Electrodes 26 are attached to respective muscles (detailed below) of the user 20 and selected ones are activated in response to the signals according to algorithms encoded in the software in the microprocessor 24. Electrodes 26 can be mounted on the surface skin of the user 20 using transcutaneous electrical nerve stimulation equipment (TENS) or implanted beneath the skin, using intramuscular implants or nerve cuff electrodes. In an experimental setting, an example system 10 used 8, 12 or 16 channel IPGs to deliver asymmetrical charged-balanced current controlled stimulus waveforms with pulse amplitudes (0-20 mA) selectable for each channel and variable pulse durations (0-250 μsec) and frequencies (0-20 Hz) set on a pulse by pulse basis.

The wheelchair system 10 according to the invention helps prevent user 20 from falling out of wheelchair 12 when unexpected destabilizing events, such as collisions or sharp turns, are encountered during everyday activities. This goal is accomplished by using the controller 18 to stimulate and thereby activate selected muscles and muscle groups (over which user 20 has lost control due to a spinal cord injury) in response to the motion parameters measured by sensor 14 and evaluated by algorithms in the software of the controller 18. When activated, the selected muscles restore trunk stability appropriately in response to the particular destabilizing event.

For collisions, such as when the wheelchair 12 encounters a curb, a linear motion parameter in the direction of wheelchair motion is used to determine muscle activation. Example linear motion parameters used by the controller 18 and measured by sensor 14 may be linear velocity, linear acceleration, or a combination of the two. The selected muscles to be activated by electrodes 26 in response to a collision are selected from knee, hip and trunk extensor muscles and include the erector spinae, the quadratus lumborum, the gluteus maximus, the posterior adductor and combinations thereof.

For sharp turns, an angular motion parameter oriented about a turning axis (axis Z in FIG. 1) of wheelchair 12 is used to determine muscle activation. Example angular motion parameters used by the controller and measured by sensor 14 include angular acceleration, angular velocity, and combinations of the two. The selected muscles to be activated by electrodes 26 in response to a sharp turn are again selected from knee, hip and trunk extensor muscles, but are separated laterally, with the right erector spinae, right quadratus lumborum, right gluteus maximus, and right posterior adductor muscles being selected when the motion parameter is an angular acceleration or an angular velocity in a counterclockwise direction about the Z axis, and the left erector spinae, left quadratus lumborum, left gluteus maximus, and left posterior adductor muscles being selected when the motion parameter is an angular acceleration or an angular velocity in a clockwise direction about the Z axis.

The invention also encompasses a method of providing neural stimulation to the user 20 of wheelchair 12. FIG. 3 shows a flowchart illustrating an example method, which comprises:


- - measuring a motion parameter of the wheelchair (**28**);
  - generating a signal indicative of the motion parameter (**30**);
  - evaluating the signal (**32**); and
  - activating at least one muscle of the user in response to the signal
    (**34**).

As noted above, measuring the motion parameter of the wheelchair 12 includes measuring a linear acceleration and/or linear velocity (for a collision for example) and measuring the angular velocity and/or angular acceleration of the wheelchair about a turning axis (for sharp turns for example). Generating a signal includes generating a signal, for example, a voltage signal, indicative of any of the motion parameters including a linear velocity, a linear acceleration, an angular velocity, an angular acceleration, and combinations thereof.

Evaluating the signal for a collision event comprises converting the signal to a value indicative of the magnitude of the motion parameter and then comparing that magnitude to a known threshold value at which muscle stimulus should be applied. Effective threshold values are known from experiment to vary with each wheelchair user, and in experimental applications of the method, collision acceleration thresholds ranging from 3.05 g to about 3.76 g were identified for determining when muscle stimulus should be applied to the extensor muscles to resist forward flexion to stabilize the user and assist return to upright sitting during the collision.

For a turning event, evaluating the signal required determining the direction of the turn as well as its magnitude. Determining the turn direction comprises comparing the measured direction to a reference direction to determine whether to activate the left or right muscle groups. Experimental angular motion parameter magnitude thresholds for determining when to apply the muscle stimulus ranged from about 97 degrees/sec to about 100 degrees/sec for applying muscle stimulation during turns.

The step of activating at least one muscle, the muscle or muscle group is selected based upon the measured motion parameters and the neural stimulus is applied to the selected muscles appropriate for the event (collision or turn). As noted above for an example embodiment, the erector spinae, quadratus lumborum, gluteus maximus, and posterior adductor muscles are selected when the measured motion parameter is a linear acceleration (indicating a collision) which exceeds a threshold value. For a measured angular motion parameter indicating a left turn and which exceeds a threshold value, one or more muscles comprises the right erector spinae, the right quadratus lumborum, the right gluteus maximus, and the right posterior adductor muscles are selected. For a measured angular motion parameter indicating a right turn and which exceeds a threshold value, one or more muscles comprising the left erector spinae, the left quadratus lumborum, the left gluteus maximus, and the left posterior adductor muscles are selected.

FIG. 4 illustrates a detailed example method according to the invention used during a collision. In this example, the linear acceleration in the direction of motion of the wheelchair (axis X, anterior/posterior acceleration) is monitored (36) using the sensor 14 and controller 18. Once motion is detected, algorithms 38, 40 and 42 within the controller 18 begin monitoring the signals from the sensor 14 to detect a collision. Algorithm 38 calculates the moving root mean square of the anterior/posterior acceleration continually and compares it against a threshold. Algorithm 40 compares the derivative of the RMS anterior/posterior acceleration against a threshold. Algorithm 42 calculates the change in velocity (integral of acceleration) and compares that to a threshold. If the thresholds are exceeded within a predetermined time period, T1, then a crash has occurred and the appropriate neuromuscular stimulation is applied by the controller 18 via electrodes 26.

FIG. 5 illustrates another example embodiment of the method according to the invention which comprises the steps of:


- - measuring a motion parameter of the wheelchair (**44**);
  - generating a signal indicative of the motion parameter (**46**);
  - evaluating the signal (**48**); and
  - activating at least one user restraint in response to the signal
    (**50**).

The method steps are similar to those for applying neuromuscular stimulation as described above, the difference being that a mechanical restraint is applied instead of muscular stimulation. As shown in FIG. 6 the restraints may include applying a brake 52, tightening a seat belt 54 to restrain user 20, and/or broadcasting a distress signal from a speaker 56 or over a radio frequency transmitter 58. Activation of the various restraints is effected by the controller 18 via appropriate interfaces, such as a servomotor 60 to tighten the seat belt, or an actuator 62, such as a solenoid, to apply the brake. The various mechanical devices used with the system 10 are advantageously electrical, to permit the system to be operated by a battery 64.

FIG. 7 shows another system 66 which improves the efficiency of manually propelled wheelchairs 68. System 66 is advantageous for users 70 with poor trunk control due to paralysis of core, thigh, hip and trunk muscles. Such users have limited trunk stability and are either unable to fully lean backward and forward when pushing the wheels 72 or are unsafe when doing so. This condition leads to inefficient pushing and thus difficulty in traversing challenging terrain such as inclined ramps.

System 66 comprises at least one sensor 74 positioned on user 70 for measuring a motion parameter of the user while the user is propelling the wheelchair 68. Motion parameters which are useful in system 66 include a position of a part of the user, an acceleration of a part of the user, a rate of change of acceleration of a part of the user as well as an electrical potential of a muscle of the user. One or more sensors 74 may be advantageously positioned on the user's upper trunk 76, shoulder 78, arm 80, in particular wrist 82, and head 84 for measuring the motion parameters of one or more of these parts of user 70. When it is desired to use electrical potential of a muscle as a motion parameter it is advantageous to use an electromyographic sensor mounted on the shoulder 78. Sensor 74 generates one or more signals indicative of the motion parameter while the user is propelling wheelchair 68.

In this example embodiment, one motion sensor 74 is used. Sensor 74 comprises a tri-axial accelerometer, such as a commercially available activity tracker, and is worn on the wrist 82. The wrist accelerometer 74 has a radiofrequency transmitter which transmit the signals indicative of the selected motion parameters wirelessly to a controller 86. Controller 86 may be worn by (mounted on) the user 70 or mounted on the wheelchair 68 (shown). In the example embodiment shown, controller 86 comprises a radiofrequency receiver 88 for receiving signals from the sensors 74, and a microprocessor 90 in communication with receiver 88. The microprocessor may be, for example, a programmable logic controller. Software resident in the microprocessor 90 evaluates the signals from the sensors 74 and directs the microprocessor to issue commands to one or more of a plurality of neural stimulating electrodes 92, also part of system 66.

Electrodes 92 are attached to respective muscles (detailed below) of the user 70 and selected ones are activated in response to the signals according to algorithms encoded in the software in the microprocessor 90. Electrodes 92 can be mounted on the surface skin of the user 70 using transcutaneous electrical nerve stimulation equipment (TENS) or implanted beneath the skin, using intramuscular implants or nerve cuff electrodes. Selected muscles on which electrodes 92 are to be attached for neuromuscular stimulation to improve propulsion efficiency include hip flexor muscles, hip extensor muscles, trunk flexor muscles, trunk extensor muscles, abdominal muscles and combinations thereof.

The invention further encompasses a method of providing assistance to user 70 for manually propelling wheelchair 68. An example method is illustrated in FIGS. 8-14, and comprises:


- - detecting when user **70** has recovered from a previous push of the
    wheels **72** of the wheelchair **68** (FIG. 8);
  - user **70** executing a next push of the wheels **72** (FIGS. 9-11);
  - applying neural stimulation to trunk and hip flexor muscles of user
    **70** while the user executes the next push of the wheels;
  - detecting when the user has completed the next push of the wheels
    (FIG. 11);
  - removing neural stimulation to the trunk and hip flexor muscles of
    user **70** when the user has completed the next push of said wheels
    (FIG. 11);
  - the user **70** recovering from the next push of said wheels (FIGS.
    12-14);
  - applying neural stimulation to trunk and hip extensor muscles of the
    user **70** while the user is recovering from the next push of the
    wheels (FIGS. 12-14);
  - detecting when the user **70** has recovered from the next push of
    the wheels (FIG. 8);
  - removing neural stimulation from the trunk and the hip extensor
    muscles of the user **70** when the user has recovered from the next
    push of the wheels (FIG. 8).

As illustrated in FIGS. 8-14, it is advantageous to apply neuromuscular stimulation to the trunk and hip flexor muscles while user 70 executes a push of wheels 72 because the pushing effort of the arms 80 is augmented by the force and weight of the trunk 76 as it bends forward in flexion (FIGS. 9-11) in response to the stimulation. Similarly, it is advantageous to remove the stimulation to the trunk and hip flexor muscles and apply stimulation to the trunk and hip extension muscles to cause extension of the trunk 76 (FIGS. 12-14) so that the user 70 may recover in preparation for the next push (FIG. 8). The timing of the application and removal of the neuromuscular stimulation depends upon detecting when user 70 has recovered and when the user has completed a push.

Detecting when user 70 has recovered from a push is effected by measuring a motion parameter of a part of the user while recovering. Practical motion parameters include a position of a part of the user, an acceleration of a part of the user, a rate of change of acceleration of a part of the user and an electrical potential of a muscle of the user, as well as combinations of these motion parameters. The parts of the user for which these motion parameters may be measured include the upper trunk 76, the shoulder 78, the arm 80, the wrist 82, the head 84 and combinations of these parts.

Detecting when user 70 has completed a push is effected by measuring a motion parameter of a part of the user while the user is pushing the wheels 72. Practical motion parameters include a position of a part of the user, an acceleration of a part of the user, a rate of change of acceleration of a part of the user and an electrical potential of a muscle of the user, as well as combinations of these motion parameters. The parts of the user for which these motion parameters may be measured include the upper trunk 76, the shoulder 78, the arm 80, the wrist 82, the head 84 and combinations of these parts.

Experimental evidence has shown that motion parameters of the wrist 82 of user 70, specifically the anterior-posterior acceleration and rate of change of acceleration, in combination with medial-lateral acceleration and rate of change of acceleration of the wrist, are useful in determining both the recovery from a push and the completion of a push by the user. FIGS. 15 and 16 illustrate an example embodiment of an algorithm using these wrist motion parameters.

As shown in FIG. 15, detecting when user 70 has completed a push of wheels 72 is effected by:


- - detecting an acceleration signal indicative of anterior-posterior
    acceleration of a part of the user (wrist **82**) greater than a
    predetermined threshold value (**94**);
  - detecting an increasing rate of change of the acceleration signal
    (**96**);
  - detecting a medial-lateral acceleration of the part of the user
    (wrist **82**) within a predetermined range of values (**98**).

As shown in FIG. 16, detecting when user 70 has recovered from a push is effected by:


- - detecting an acceleration signal indicative of anterior-posterior
    acceleration of a part of the user (wrist **82**) less than a
    predetermined threshold value (**100**);
  - detecting a decreasing rate of change of the acceleration signal
    (**102**);
  - detecting a medial-lateral acceleration of the part of the user
    (wrist **82**) having an increasing rate of change (**104**).

Although it is expected that the motion parameters of other parts of the user 70 may also be used to detect push completion and recovery, it has been found effective to use the motion of the wrist 82 of the user 70 to execute this algorithm.

It is expected that the systems and methods according to the invention will enhance a wheelchair user's experience, ability, efficiency and safety.

