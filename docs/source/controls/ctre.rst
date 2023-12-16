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
- `API Migration <https://v6.docs.ctr-electronics.com/en/latest/docs/migration/migration-guide/index.html>`_.
- `Control Requests <https://v6.docs.ctr-electronics.com/en/latest/docs/migration/migration-guide/control-requests-guide.html>`_.
- `Closed-Loop Control including Motion Magic <https://v6.docs.ctr-electronics.com/en/latest/docs/migration/migration-guide/closed-loop-guide.html>`_.

-----------------     
Control Requests
-----------------

v5

.. code-block:: Java
// robot init, set voltage compensation to 12 V
m_motor.configVoltageComSaturation(12);
m_motor.enableVoltageCompensation(true);

// main robot code, command 12 V output
m_motor.set(ControlMode.PercentOutput, 1.0);


v6

.. code-block:: Java
// class member variable
final VoltageOut m_request = new VoltageOut(0);

// main robot code, command 12 V output
m_motor.setControl(m_request.withOutput(12.0));


.. list-table:: Control Requests
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


~ This is the way.