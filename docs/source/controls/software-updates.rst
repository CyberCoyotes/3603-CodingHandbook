========================
Season Software Updates
========================
*Every season there are a series of updates for your computer and the robot software. We've compiled a list of essential updates and some commmon ones that our team uses.*

---------------------
Primary Updates
---------------------
*The NI Game Tools and WPILIB Suite must be updated every year after the game release. Most other programs will update on their own when they release updates.*

- [ ] Install `NI Game Tools <https://www.ni.com/en-us/support/downloads/drivers/download.frc-game-tools.html#473762>`_ .      

    - [ ] Update the RIO Image (also needs Balena Etcher if using RIO2)
    - [ ] Radio (radio utility)
    - [ ] Driver's Station

- [ ] Install `WPI LIB Suite <https://github.com/wpilibsuite/allwpilib/releases/tag/v2023.1.1>`_. Including VS Code download for offline install option.  
- [ ] Install `REV Hardware Client <https://docs.revrobotics.com/rev-hardware-client/>`_. Needed to update REV firmware for motors (NEOs), controllers (Spark MAX), and Power Distribution Hub.
- [ ] Install `Tuner X <https://apps.microsoft.com/detail/9NVV4PWDW27Z?hl=en-us&gl=US>`_. Needed to update CTRE firmware for motors (Falcon, Kraken), controllers (Talon SRX), gyro (Pigeon), and the original Power Distribution Panel. See also `CTRE <https://store.ctr-electronics.com/software/>`_ website 


------------------------
Other Updates
------------------------
- [ ] Download `GitHub Desktop <https://desktop.github.com/>`_ client.
- [ ] Official Limelight `Docs <https://docs.limelightvision.io/en/latest/>`_ | `Downloads <https://limelightvision.io/pages/downloads>`_.
- [ ] Install `PathPlanner <https://github.com/mjansen4857/pathplanner/releases>`_ if using for auton.

------------------
Vendor Libraries
------------------
*After the project is opened in the latest VS Code it will ask to be updated. The vendordeps will **break** and need to be reinstalled or copied over and updated *See below for vendor libraries we have used in the past*

#. `Phoenix.json <https://maven.ctr-electronics.com/release/com/ctre/phoenix/Phoenix5-frc2023-latest.json>`_.
#. `REVLib.json <https://software-metadata.revrobotics.com/REVLib.json>`_.
#. `PathPlanner.json <https://3015rangerrobotics.github.io/pathplannerlib/PathplannerLib.json>`_ if using PathPlanner for auton

Previously used `SdsSwerveLib.json <https://raw.githubusercontent.com/SwerveDriveSpecialties/swerve-lib/master/SdsSwerveLib.json>`_ & `BearSwerve.json <https://raw.githubusercontent.com/6391-Ursuline-Bearbotics/BearSwerve/master/BearSwerve.json>`_, but not implementing for 2024 for us.   

--------------------
Reference Document
--------------------
* `Reference Doc <https://docs.google.com/document/d/1pE3562a7Np4BVmMLlAgXqFzefXEp5hn-s_72Zkyl828/edit>`_.
