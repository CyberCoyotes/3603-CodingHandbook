  -----------------------------------
  Using Photonvision on a Limelight
  -----------------------------------

Download the [Limelight USB
Driver](https://limelightvision.io/pages/downloads) to see the Limeight
in Windows Explorer. It\'s needed before Balena Etcher can flash the
limelight.

[Installing
PhotonLib](https://docs.photonvision.org/en/latest/docs/programming/photonlib/adding-vendordep.html)
in VS Code.

Check your vendordeps (.json files) if importing a previous project into
a new year. For example, we have vendordeps

-   BearSwerve.json
-   PathplannerLib.json
-   Pheonix.json
-   photonlib.json
-   REVlLin.json
-   SdsSwerveLin.json

After installing the Pheonix Tuner, you need to manage the vendor
libraries inside of VS Code.
<https://docs.ctre-phoenix.com/en/stable/ch05a_CppJava.html>

For the others, they were copied and imported into out project
\"vendordep\" folder, then an \"update online\" was ran from the Manage
Vendordep from within VS Code

Resources \-\-\--\* [PhotonVision discord](https://discord.gg/jWfxwqJK)
\* [Full Robot Pose Estimation w/ PhotonVision -
doc](https://docs.google.com/document/d/1i9y_xErWBRWlO6Ws0qoYoJbCUr-QSafhKVNoYOwd-ng/view)
doc shared via Discord (2022-12) \* [PhotonVision Beta 2023:
AprilTags](https://www.chiefdelphi.com/t/photonvision-beta-2023-apriltags/415626)
Chief Delphi \* [PhotonVision beta 3D calibration lags on limelight
camera](https://www.chiefdelphi.com/t/photonvision-beta-3d-calibration-lags-on-limelight-camera/416986/19)
Chief Delphi. \* [Vision Programming with AprilTags Jumpstart
2023](https://youtu.be/TG9KAa2EGzQ?t=1104).
