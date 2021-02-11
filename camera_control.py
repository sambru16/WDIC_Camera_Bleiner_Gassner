from picamera import PiCamera 
from gpiozero import Button
import datetime as dt
import os

button1 = Button(17)
buttton2 = Button(27)
button3 = Button(22)
camera = PiCamera()

videostate = False

camera.start_preview()

def take_picture():
    try:
        os.remove('')
    except OSError:
        pass

    camera.capture('')

def control_video():
    if not videostate:
        try:
            os.remove('rpi_video.h264')
        except OSError:
            pass

        videostate = True
        camera.start_recording('rpi_video.h264')
        #camera.wait_recording(60)
    
    if videostate:
        videostate = False
        camera.stop_recording()

def picture_overlay():
    pass

while True:
    if button1.is_pressed:
        take_picture
    elif buttton2.is_pressed:
        control_video
    elif button3.is_pressed:
        picture_overlay
