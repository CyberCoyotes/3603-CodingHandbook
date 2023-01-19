====
LEDs
====
There (seems to be) two approaches to controlling LEDs on a FRC robot. The REV Blinkin module or using the WPI Addressable with hooking up the LEDs directly to the Rio. The terms **individually addressable** is a reference to the ability of a program, app, or remote to make very specific changes to the LEDs themselves whereas WPI AddressableLED is program specific reference. 

Using a Blinkin
----
#. `Blinkin LED Driver page <https://www.revrobotics.com/rev-11-1105/>`_ and including the `PDF manual <https://www.revrobotics.com/content/docs/REV-11-1105-UM.pdf>`_
#. `REV Robotics Blinkin Overview - YouTube <https://youtu.be/wMdkM2rr1a4>`_
#. `Sonic Squirrels <https://github.com/FRC-Sonic-Squirrels/MinibotCode/blob/5b58f10ef78b79384b12a69ffbe3fcba4775bba1/src/main/java/frc/robot/subsystems/blinkin.java>`_
#. `Mechanical Advantage <https://github.com/Mechanical-Advantage/RobotCode2022/tree/main/src/main/java/frc/robot/subsystems/leds>`_ has blinkin and Addressable
#. Chief Delphi `blinkin-led-programming <https://www.chiefdelphi.com/t/blinkin-led-programming/339003>`_
#. Chief Delphi `rev-blinkin-led <https://www.chiefdelphi.com/t/rev-blinkin-led/396966>`_

Using WPI Addressable
----
#. `Addressable LEDs - WPILib <https://docs.wpilib.org/en/stable/docs/software/hardware-apis/misc/addressable-leds.html>`_
#. <https://github.com/Mechanical-Advantage/RobotCode2022/tree/main/src/main/java/frc/robot/subsystems/leds>
#. https://github.com/Yeti-Robotics/aurora-java-2022
#. https://github.com/6391-Ursuline-Bearbotics/2022_UARobotics_Rapid_React/blob/master/src/main/java/frc/robot/subsystems/LEDSubsystem.java
#. Chief Delphi post <https://www.chiefdelphi.com/t/addressableleds-and-rev-robotics-blinkin/375753>
