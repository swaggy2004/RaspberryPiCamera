'''
Taking multiple pictures at once
'''

from picamera import PiCamera
from time import sleep
import sys

cam = PiCamera()

#added the try except block of code so I can exist safely
try:
    #taking 3 pictures
    for i in range(3):
        cam.start_preview(alpha=200)
        sleep(5)
        print('Capturing...')
        #saving the pictures to the Pictures folder 
        cam.capture('/home/shaveen/Pictures/img%s.jpg'% i)
        cam.stop_preview()
        sleep(4)
except KeyboardInterrupt:
    #stopping the preview and the exsiting the code
    cam.stop_preview()
    print("Safley existed...")
    sys.exit(0)