# WDIC_Camera_Bleiner_Gassner

Tasks:
1. Execute actions via Button press
2. Image Capture and Video Start & Stop
3. Add Text Overlay to Images (Date & Time)

Documentation:
To detect a pressed button, a while-loop repeatedly checks if one of the three buttons is pressed.
If yes, the needed function is called. In this functions, the actions for the different tasks get excecuted.

take_picture:
At first it will be checked if an old picture is already saved, and if yes it will be deleted to save space.
After that a simple picture is taken and saved.

control_video:
At first it will be checked if an old video is already saved, and if yes it will be deleted to save space.
Next, videostate is checked, which describes if a video is already shooting right now.
Depending on the value of videostate the video is either getting started or stopped.

picture_overlay:
Basically not much different from take_picture. Only big difference is that a text is added, which shows the actual date and time.

How to use:

To execute this project, the following things are needed:
- Raspberry Pi
- Raspberry Pi Camera Module
- 3 Buttons

The camera module and the buttons have to be connected with the Raspberry Pi. The camera module can be connected
via the camera slot and each button has to be connected with GND and either GPIO-Pin 17, 27 or 22.

The required libraries for the project should all be preinstalled on your Raspberry Pi.

After these few steps, the project should be ready to use.

The project itself is very easy to use: Simply execute the project and press one of the three buttons.
Each button has a unique functioning, which are described above. 

For further explanation you can watch our video: https://1drv.ms/v/s!AgtPPpg48bG1kH33SHQ3g94MVpdv?e=hzjZXH

If any other problem occurs you can also contact us via email:

samuel.brugger@student.htl-rankweil.at

lukas.gassner@student.htl-rankweil.at
