====
CTRE
====
In the past our team has used a lot of CTRE products (TalonSRX controllers, TalonFX with Falcons, Pigeon2). 
There are some big changes going from 2023 to 2024 with the release of the Kraken and Phoenix 5 to Phoenix 6 (Pro Licenses) frameworks.

--------------
2023 December
--------------
Mostly using this space to document my noticings and notes

------
Links
------
Assume all links are to official documentation unless otherwise noted

- Tuner X can be downloaded from the Microsoft store
- `Official Phoenix Pro Documentation <https://v6.docs.ctr-electronics.com/en/2023-pro/index.html>`_
- `Github Examples of Phoenix 6 <https://github.com/CrossTheRoadElec/Phoenix6-Examples>`_

See also `links on motion profiling <https://github.com/CyberCoyotes/Handbook/blob/main/docs/source/controls/motion-profiling.rst>`_.

-----------
Randomness
-----------

- `Package com.ctre.phoenix6.configs <https://api.ctr-electronics.com/phoenix6/release/java/com/ctre/phoenix6/configs/package-summary.html>`_.
- `API Migration <https://v6.docs.ctr-electronics.com/en/latest/docs/migration/migration-guide/index.html>`_. "Cheat Sheet"

.. list-table:: Control Request Changes
    :widths: 50 50
    :header-rows: 1

    *   - PREVIOUSLY
        - PHOENIX 6
    *   - Position
        - PositionDutyCycle
    *   - Velocity
        - VelocityDutyCycle
    *   - MotionMagic
        - MotionMagicDutyCycle
    *   - Closed-loop + Voltage Compensation
        - {ClosedLoop}Voltage
    *   -
        - {ClosedLoop}TorqueCurrentFOC (requires Pro)

*See API Migration <https://v6.docs.ctr-electronics.com/en/latest/docs/migration/migration-guide/index.html>`_ for more*

~ This is the way.