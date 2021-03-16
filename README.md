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
