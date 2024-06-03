'''
Takes a short video clip
'''
from picamera import PiCamera
from time import sleep

cam = PiCamera()

cam.start_preview(alpha=200)
sleep(4)
cam.start_recording('/home/shaveen/Videos/vid.h264')#starts taking a video
sleep(10) #goes on for 10 seconds
cam.stop_recording()#stops taking the video
cam.stop_preview()