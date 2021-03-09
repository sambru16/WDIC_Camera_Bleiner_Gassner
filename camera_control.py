from picamera import PiCamera           #Kamera 
from gpiozero import Button             #GPIO Button
import datetime as dt                   #Datum und Uhrzeit
import os                               #Verzeichnis und Dateiverwaltung

button1 = Button(17)                    #Button Zuweisung
buttton2 = Button(27)           
button3 = Button(22)
camera = PiCamera()                     #Kamera Zuweisung

videostate = False                      #Status der Videoaufnahme

camera.start_preview(alpha=220)         #Kameravorschau aktivieren

def take_picture():                     #Erste Routine(Bild aufnehmen)
    try:
        os.remove('/home/pi/Documents/Camera_Project/rpi_image.jpg')                 #Wenn Bild vorhanden --> löschen
    except OSError:
        pass

    camera.capture('/home/pi/Documents/Camera_Project/rpi_image.jpg')                #Bild aufnehmen und abspeichern

def control_video():                    #Zweite Routine(Video aufnehmen)
    global videostate           
    if not videostate:                  #Falls Videoaufnahme nicht aktiv ist --> starten der Aufnahme
        try:
            os.remove('/home/pi/Documents/Camera_Project/rpi_image.jpg')    #Wenn Video vorhanden --> löschen
        except OSError:
            pass

        videostate = True       
        camera.start_recording('/home/pi/Documents/Camera_Project/rpi_image.jpg')     #Starten der Aufnahme
        camera.wait_recording(60)
    
    if videostate:                      #Falls Videoaufnahme aktiv --> Aufnahme beenden
        videostate = False      
        camera.stop_recording()

def picture_overlay():                  #Dritte Routine(Bildbeschriftung)
    try:
        os.remove('/home/pi/Documents/Camera_Project/rpi_image.jpg')                  #Wenn Bild vorhanden --> löschen
    except OSError:
        pass

    camera.annotate_text_size = 110     #Textgröße ändern
    camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')            #Datum und Uhrzeit hinzufügen
    camera.capture('/home/pi/Documents/Camera_Project/rpi_image.jpg')                 #Bild aufnehmen

while True:                             #GPIO Button Abfrage
    if button1.is_pressed:
        take_picture
    elif buttton2.is_pressed:
        control_video
    elif button3.is_pressed:
        picture_overlay
