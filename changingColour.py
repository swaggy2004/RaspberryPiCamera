'''
Changing the colour of th text and background
'''
from picamera import PiCamera, Color
from time import sleep

camera = PiCamera()

camera.start_preview()
camera.annotate_background = Color('blue')#changing the backgorund colour of the text
camera.annotate_foreground = Color('yellow')#changing the text colour of the text
camera.annotate_text = 'Hello, world!'
sleep(5)
camera.stop_preview()