import schedule
import serial as sl
from picamera import PiCamera
from picamera.array import PiRGBArray
import time
import cv2
from capture_soil_data import MoistureData
from move_gantry import GantryControls
import argparse
from led_setup import LED

ap = argparse.ArgumentParser()
ap.add_argument("-n", "--number", type=int, help="number of plants in set")
args = vars(ap.parse_args())


def job():
    for i in range(args['number']):
        capture_image()
        get_moisture_data(i+1)

        gantry.move_up_position(motor_connect)

    gantry.move_home(motor_connect)


def capture_image():
    local_time = time.localtime()

    minute = local_time.tm_min
    hr = local_time.tm_hour
    day = local_time.tm_mday
    month = local_time.tm_mon
    image_name = '{}/{}_{}_{}_{}'.format(directory_name, month, day, hr, minute)

    camera = PiCamera()
    raw_capture = PiRGBArray(camera)
    led.led_on()

    # allow the camera to warmup
    time.sleep(0.1)

    # grab an image from the camera
    camera.capture(raw_capture, format="bgr")
    image = raw_capture.array

    led.led_off()

    cv2.imwrite('{}.png'.format(image_name), image)

    camera.close()


def get_moisture_data(val):
    if val == 1:
        moisture_1 = moisture_data.position_1_data(moisture_connect)
        print(moisture_1)

    elif val == 2:
        moisture_2 = moisture_data.position_2_data(moisture_connect)
        print(moisture_2)

    elif val == 3:
        moisture_3 = moisture_data.position_3_data(moisture_connect)
        print(moisture_3)

    elif val == 4:
        moisture_4 = moisture_data.position_4_data(moisture_connect)
        print(moisture_4)


moisture_connect = sl.Serial('/dev/ttyACM0', 9600)
time.sleep(2)
motor_connect = sl.Serial('/dev/ttyUSB0', 9600)
time.sleep(2)

moisture_data = MoistureData()
gantry = GantryControls()
led = LED()

schedule.every().hour.do(job)

directory_name = 'images'

while True:
    schedule.run_pending()
    time.sleep(1)
