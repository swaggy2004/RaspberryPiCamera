'''
Changing the brightness in steps
'''
from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
for i in range(100):
    camera.annotate_text = 'Brightness: %s' % i#showing the current brightness level
    camera.brightness = i#changing the camera brightness
    sleep(0.1)
camera.stop_preview()