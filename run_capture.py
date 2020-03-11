import schedule
from picamera import PiCamera
from picamera.array import PiRGBArray
import time
import cv2


def job():
    hr = local_time.tm_hour
    day = local_time.tm_mday
    month = local_time.tm_mon
    image_name = '{}/{}_{}_{}'.format(directory_name, month, day, hr)

    capture(image_name)


def capture(image_name):
    camera = PiCamera()
    raw_capture = PiRGBArray(camera)

    # allow the camera to warmup
    time.sleep(0.1)

    # Read time, and take image every hour or so
    # Make sure that this can be updated by changing a variable!

    # grab an image from the camera
    camera.capture(raw_capture, format="bgr")
    image = raw_capture.array

    cv2.imwrite('{}.png'.format(image_name), image)

    camera.close()


schedule.every(1).minutes.do(job)

local_time = time.localtime()

directory_name = 'images'

while True:
    schedule.run_pending()
    time.sleep(1)
