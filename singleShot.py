'''
Taking a single picture with the camera
'''

#importing the required modules
from picamera import PiCamera
from time import sleep
import sys

#showing a preview from 6 seconds and then taking the picture
#if delay is lower than 6 the preview won't stop and the code won't stopping running
cam = PiCamera()

#use the try except just in case the preview woudln't go away
try:
    cam.start_preview()
    sleep(6)
    cam.capture('/home/shaveen/Pictures/test.jpg')
    cam.stop_preview()
except KeyboardInterrupt:
    cam.stop_preview()
    sys.exit(0)