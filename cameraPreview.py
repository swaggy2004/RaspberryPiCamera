'''
Testing to get a small preview of my camera
'''

#importing the required moudles
from picamera import PiCamera
import time

#setting the camera object
cam = PiCamera()

#starting a preview for 6 seconds
cam.start_preview(alpha=200)
#cam.start_preview(alpha=200) -> this make the camera preview transparent. This fix all the future issues
time.sleep(10)
cam.stop_preview()