Motion Profiling
====

When controlling a mechanism, is often desirable to move it smoothly between two positions, rather than to abruptly change its setpoint. This is called “motion-profiling,” and is supported in WPILib through the TrapezoidProfile class 

WPI
----

For a description of the WPILib motion profiling features used by these command-based wrappers, see `Trapezoidal Motion Profiles in WPILib <https://docs.wpilib.org/en/stable/docs/software/advanced-controls/controllers/trapezoidal-profiles.html#trapezoidal-motion-profiles-in-wpilib>`_.
Note: The TrapezoidProfile command wrappers are generally intended for composition with custom or external controllers. For combining trapezoidal motion profiling with WPILib’s PIDController, see `Combining Motion Profiling and PID in Command-Based <https://docs.wpilib.org/en/stable/docs/software/commandbased/profilepid-subsystems-commands.html>`_.
To further help teams integrate motion profiling into their command-based robot projects, WPILib includes two convenience wrappers for the TrapezoidProfile class: TrapezoidProfileSubsystem, which automatically generates and executes motion profiles in its periodic() method, and the TrapezoidProfileCommand, which executes a single user-provided TrapezoidProfile.
`Motion Profiling through TrapezoidProfileSubsystems and TrapezoidProfileCommands <https://docs.wpilib.org/en/stable/docs/software/commandbased/profilepid-subsystems-commands.html>`_

CTRE
----

- `Motion Magic and other Motion Profiling <https://docs.ctre-phoenix.com/en/stable/ch16_ClosedLoop.html>`_ with CTRE.
- `254 <https://www.chiefdelphi.com/uploads/default/original/3X/a/b/ab808bbf5f212c6deba8565dac83852bbd9b4394.pdf>`_ PDF explaining motion planning
- `2019 Motion Magic <https://docs.google.com/presentation/d/1zzMI3DW-elButNH0QLFdYnDyaIapeI-zZnv9CAC6WY8/edit>`_ slide presentation. Video of Corey Applegate (FRC 3244) `CTRE Motion Magic <https://youtu.be/VQIgdLslU_E>`_

Come highly recommended `Team 195- FRC Motion Control: part 1 <https://youtu.be/4rbT-oscpx0>`_ BUT... its from 2018 AND its 4.5 hrs long for both parts

Resources
----

-  `Motion Profiling - wiki <https://github.com/CyberCoyotes/Handbook/wiki/Motion-Profiling>`_ page
-  `Telemetry docs <https://docs.wpilib.org/en/stable/docs/software/telemetry/index.html>`_ docs page.
-  `Control Modes Configuration for TalonFX and Falcon500 <https://www.chiefdelphi.com/t/control-modes-configuration-for-talonfx-and-falcon500/374704/12>`_ ChiefDelphi post.