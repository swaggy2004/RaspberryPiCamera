'''
Changing the brightness of the image to 70%
'''
from picamera import PiCamera, Color
from time import sleep

camera = PiCamera()

camera.start_preview()
camera.brightness = 70#changing the brightness of the image '0 - 100'
sleep(5)
camera.capture('/home/shaveen/Pictures/bright.jpg')
camera.stop_preview()
