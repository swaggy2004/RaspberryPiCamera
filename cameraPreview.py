'''
Testing to get a small preview of my camera
'''

#importing the required moudles
from picamera import PiCamera
import time

#setting the camera object
cam = PiCamera()

#starting a preview for 6 seconds
cam.start_preview()
time.sleep(6)
cam.stop_preview()