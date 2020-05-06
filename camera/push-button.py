from picamera import PiCamera
from time import sleep
from gpiozero import Button

button = Button(17)
camera = PiCamera()
camera.rotation = 180
camera.resolution = (640, 480)

camera.start_preview()
frame = 0

while True:
    try:
        button.wait_for_press()
        camera.capture('/home/pi/projects/camera/push-button/img-%03d.jpg' % frame)
        frame += 1
    except KeyboardInterrupt:
        camera.stop_preview()
        break