====
Controls Team
====
.. toctree::
    :maxdepth: 2
    :caption: Learn about Controls
    :hidden:

    controls/command-and-declarative-programming

    controls/PID

    controls/motion-profiling

    controls/pathplanner
    
    controls/vision-systems

    controls/vision-photonvision-on-a-limelight

    controls/code-examples

    controls/style-guides
    
    controls/software-updates
    
If you are new to programming you might want to learn more about command based first.

A good place to start for new and veteran Controls Team is `FIRST Robotics Competition Control System <https://docs.wpilib.org/en/stable/index.html0>`_

Important Links
----
1. `Installing the FRC Game Tools <https://www.ni.com/en-us/support/downloads/drivers/download.frc-game-tools.html#473762>`_ (LabVIEW Update, FRC Driver Station, FRC roboRIO Imaging Tool and Images)
2. `WPILib 2023.1.1 Release <https://github.com/wpilibsuite/allwpilib/releases/tag/v2023.1.1>`_


A little history about our controls approaches.

2019 and Prior
----
* **Drivetrain**: Mecanum, tank drive, rhinotracks, or omni wheels combined with others depending on the game demands
* **Drive motors**: CIM motors mostly, switched to Falcons in 2019?
* **Gyro**: NavX
* **Programming**: *Iterative* Java

2022 Season Changes
----
* **Drivetrain**: MK3 swerve
* **Drive motors**: Falcon500 motors
* **Programming**: *Command based* Java adapted from SDS

2023 Season Changes
----
* **Drivetrain**: MK4 swerve
* **Gyro**: CTRE Pigeon
* **Programming**: *Command based* Java adapted from `BearSwerve <https://github.com/6391-Ursuline-Bearbotics/BearSwerve>`_ code base.
