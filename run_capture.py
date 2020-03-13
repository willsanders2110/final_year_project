import schedule
import serial as sl
from picamera import PiCamera
from picamera.array import PiRGBArray
import time
import cv2
from capture_soil_data import MoistureData

ser = sl.Serial('/dev/ttyACM0', 9600)
time.sleep(2)


def job():
    local_time = time.localtime()

    minute = local_time.tm_min
    hr = local_time.tm_hour
    day = local_time.tm_mday
    month = local_time.tm_mon
    image_name = '{}/{}_{}_{}_{}'.format(directory_name, month, day, hr, minute)

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

    pos_1 = MoistureData.position_1_data()
    print(pos_1)


schedule.every().hour.do(job)

directory_name = 'images'

while True:
    schedule.run_pending()
    time.sleep(1)
