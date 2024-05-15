====
Controlling an Arm Mechanism
====

.. code-block:: java

 TalonFXConfiguration configuration = new TalonFXConfiguration();
 configuration.motionCruiseVelocity = FAST_MOTION_CONSTRAINTS.maxVelocity /
 SENSOR_VELOCITY_COEFFICIENT;
 configuration.motionAcceleration = FAST_MOTION_CONSTRAINTS.maxAcceleration /
 SENSOR_VELOCITY_COEFFICIENT;
 configuration.slot0.kP = 0.25;
 configuration.slot0.kI = 0.0;
 configuration.slot0.kD = 0.0;
 configuration.primaryPID.selectedFeedbackSensor =
 TalonFXFeedbackDevice.IntegratedSensor.toFeedbackDevice();
 configuration.voltageCompSaturation = 12.0;
 
`https://github.com/FRCTeam2910/2023CompetitionRobot-Public/blob/main/src/main/java/org/frcteam2910/c2023/subsystems/arm/ArmIOFalcon500.java`


====
REREFENCES
====
`https://github.com/CrossTheRoadElec/Phoenix6-Examples/blob/main/java/CommanddDrive/src/main/java/frc/robot/subsystems/DriveSubsystem.java`

See also
`https://github.com/FRCTeam2910/2023CompetitionRobot-Public/blob/main/src/main/java/org/frcteam2910/c2023/subsystems/intake/IntakeIOHardware.java`