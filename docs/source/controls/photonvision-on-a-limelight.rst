====
Using Photonvision on a Limelight
====

Download the `Limelight USB Driver <https://limelightvision.io/pages/downloads>`_ to see the Limeight in Windows Explorer. It's needed before Balena Etcher can flash the limelight.

`Installing PhotonLib <https://docs.photonvision.org/en/latest/docs/programming/photonlib/adding-vendordep.html>`_ in VS Code.

Check your vendordeps (.json files) if importing a previous project into a new year. For example, we have vendordeps

* BearSwerve.json
* PathplannerLib.json
* Pheonix.json
* photonlib.json
* REVlLin.json
* SdsSwerveLin.json

After installing the Pheonix Tuner, you need to manage the vendor libraries inside of VS Code.
https://docs.ctre-phoenix.com/en/stable/ch05a_CppJava.html

For the others, they were copied and imported into out project "vendordep" folder, then an "update online" was ran from the Manage Vendordep from within VS Code

Resources
----
* `PhotonVision discord <https://discord.gg/jWfxwqJK>`_
* `Full Robot Pose Estimation w/ PhotonVision - doc <https://docs.google.com/document/d/1i9y_xErWBRWlO6Ws0qoYoJbCUr-QSafhKVNoYOwd-ng/view>`_ doc shared via Discord (2022-12)
* `PhotonVision Beta 2023: AprilTags <https://www.chiefdelphi.com/t/photonvision-beta-2023-apriltags/415626>`_ Chief Delphi
* `PhotonVision beta 3D calibration lags on limelight camera <https://www.chiefdelphi.com/t/photonvision-beta-3d-calibration-lags-on-limelight-camera/416986/19>`_ Chief Delphi.
* `Vision Programming with AprilTags Jumpstart 2023 <https://youtu.be/TG9KAa2EGzQ?t=1104>`_.
