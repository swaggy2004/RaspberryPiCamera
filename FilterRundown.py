'''
Adding effects to the camera
'''

from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
for effect in camera.IMAGE_EFFECTS:#looping through all the effects
    camera.image_effect = effect#changing the effect
    camera.annotate_text = 'Effect: %s' %effect#chaning the title of the effect
    sleep(3)
    camera.capture('/home/shaveen/Pictures/%s_img.jpg' % effect)#saving the picture with the effect name
camera_stop_preview()