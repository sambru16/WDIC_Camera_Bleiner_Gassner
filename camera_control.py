from picamera import PiCamera 
from gpiozero import Button
import datetime as dt

button1 = Button(17)
buttton2 = Button(27)
button3 = Button(22)
camera = PiCamera()

camera.start_preview()

def take_picture():
    pass

def control_video():
    pass

def picture_overlay():
    pass

while True:
    if button1.is_pressed:
        take_picture
    elif buttton2.is_pressed:
        control_video
    elif button3.is_pressed:
        picture_overlay
