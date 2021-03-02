from picamera import PiCamera 
from gpiozero import Button
import datetime as dt
import os

button1 = Button(17)
buttton2 = Button(27)
button3 = Button(22)
camera = PiCamera()

videostate = False

camera.start_preview(alpha=220)

def take_picture():
    try:
        os.remove('/home/pi/Documents/Camera_Project/rpi_image.jpg')
    except OSError:
        pass

    camera.capture('/home/pi/Documents/Camera_Project/rpi_image.jpg')

def control_video():
    global videostate
    if not videostate:
        try:
            os.remove('/home/pi/Documents/Camera_Project/rpi_image.jpg')
        except OSError:
            pass

        videostate = True
        camera.start_recording('/home/pi/Documents/Camera_Project/rpi_image.jpg')
        camera.wait_recording(60)
    
    if videostate:
        videostate = False
        camera.stop_recording()

def picture_overlay():
    try:
        os.remove('/home/pi/Documents/Camera_Project/rpi_image.jpg')
    except OSError:
        pass

    camera.annotate_text_size = 110
    camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    camera.capture('/home/pi/Documents/Camera_Project/rpi_image.jpg')

while True:
    if button1.is_pressed:
        take_picture
    elif buttton2.is_pressed:
        control_video
    elif button3.is_pressed:
        picture_overlay