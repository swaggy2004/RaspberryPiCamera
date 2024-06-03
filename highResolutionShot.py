'''
Changing to the highest resolution of the camera
'''
from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.resolution = (1920, 1080)#changing to my camera's resolution
camera.framerate = 30#changing to my camera's framerate
camera.start_preview()
sleep(5)
camera.capture('/home/shaveen/Pictures/highRes.jpg')
camera.stop_preview()