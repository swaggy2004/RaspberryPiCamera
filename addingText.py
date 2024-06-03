'''
Adding text to a picture
'''
from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
camera.annotate_text = 'Hello, world!'#adding the text to the picture
camera.annotate_text_size = 50
sleep(5)
camera.capture('/home/shaveen/Pictures/pictureText.jpg')
camera.stop_preview()