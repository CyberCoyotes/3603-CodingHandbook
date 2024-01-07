========================
Software Updates
========================
Every season there are a series of updates for your computer and the robot software. We've compiled a list of essential updates and some commmon ones that our team uses.

---------------------
Primary
---------------------
The NI Game Tools and WPILIB Suite must be updated every year after the game release. Most other programs will update on their own when they release updates.

- [ ] Install `NI Game Tools <https://packages.wpilib.workers.dev/game-tools/ni-frc-2024-game-tools_24.0.0_offline.iso>`_ .
    - [ ] Update the RIO Image (also needs `Balena Etcher <https://etcher.balena.io/>`_ if using RIO2 and an external SD card reader)
    - [ ] Radio (radio utility)
    - [ ] Driver's Station
- [ ] Install `WPI LIB Suite <https://packages.wpilib.workers.dev/installer/v2024.1.1/Win64/WPILib_Windows-2024.1.1.iso>`_.
    Including VS Code download for offline install option.  


------------------------
Secondary
------------------------
These are not needed by all teams, but we use them and probably used by many teams.
- [ ] Install or update `REV Hardware Client <https://docs.revrobotics.com/rev-hardware-client/>`_. 
    Needed to update REV firmware for motors (NEOs), controllers (Spark MAX), and Power Distribution Hub.
- [ ] `Tuner X <https://apps.microsoft.com/detail/9NVV4PWDW27Z?hl=en-us&gl=US>`_.
    Needed to update CTRE firmware for motors (Falcon, Kraken), controllers (Talon SRX), gyro (Pigeon), and the original Power Distribution Panel. See also `CTRE <https://store.ctr-electronics.com/software/>`_ website 
- [ ] `GitHub Desktop <https://desktop.github.com/>`_ client.
- [ ] `PathPlanner <https://github.com/mjansen4857/pathplanner/releases>`_ for for auton.
- [ ] `Limelight Docs <https://docs.limelightvision.io/en/latest/>`_ | `Downloads <https://limelightvision.io/pages/downloads>`_.

---------------
Updating Code
---------------
After downloading software and updating firmares, you need to import last year's code or start a new project. Part of this process will likely involve updating vendor libraries. The ones we use use have been listed below.

------------------
Vendor Libraries
------------------
- `Phoenix.json <https://maven.ctr-electronics.com/release/com/ctre/phoenix6/latest/Phoenix6-frc2024-beta-latest.json`_.
- `REVLib.json <https://software-metadata.revrobotics.com/REVLib.json>`_.
- `PathPlanner.json <https://3015rangerrobotics.github.io/pathplannerlib/PathplannerLib.json>`_ if using PathPlanner for auton

--------------------
Reference Document
--------------------
- `Reference Doc <https://docs.google.com/document/d/1pE3562a7Np4BVmMLlAgXqFzefXEp5hn-s_72Zkyl828/edit>`_.
