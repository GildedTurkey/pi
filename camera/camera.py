from picamera import PiCamera
from time import sleep
import time

camera = PiCamera()
camera.rotation = 180
camera.resolution = (640, 480)

camera.start_preview()
sleep(3)
camera.capture('/home/pi/Desktop/image' + time.time() + '.jpg')
camera.stop_preview()