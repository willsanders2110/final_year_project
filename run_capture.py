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
import sqlite3

ap = argparse.ArgumentParser()
ap.add_argument("-n", "--number", type=int, default=1, help="number of plants in set")
args = vars(ap.parse_args())


def job():
    local_time = time.localtime()

    minute = local_time.tm_min
    hr = local_time.tm_hour
    day = local_time.tm_mday
    month = local_time.tm_mon

    time_stamp = '{}_{}_{}_{}'.format(month, day, hr, minute)

    data = []
    data.append(time_stamp)
    for i in range(args['number']):
        image_name = '{}/{}_{}'.format(directory_name, time_stamp, i+1)

        capture_image(image_name)
        m_data = get_moisture_data(i+1)
        data.append(m_data)

        gantry.move_up_position(motor_connect)

    for i in range(4-args['number']):
        data.append(0)

    c.execute("""INSERT INTO moisture_data 
                 VALUES ('{}','{}','{}','{}','{}')""".format(data[0], data[1], data[2], data[3], data[4]))
    conn.commit()
    gantry.move_home(motor_connect)


def capture_image(image_name):

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
        return moisture_1.decode()

    elif val == 2:
        moisture_2 = moisture_data.position_2_data(moisture_connect)
        return moisture_2.decode()

    elif val == 3:
        moisture_3 = moisture_data.position_3_data(moisture_connect)
        return moisture_3.decode()

    elif val == 4:
        moisture_4 = moisture_data.position_4_data(moisture_connect)
        return moisture_4.decode()


moisture_connect = sl.Serial('/dev/ttyACM0', 9600)
time.sleep(2)
motor_connect = sl.Serial('/dev/ttyUSB0', 9600)
time.sleep(2)

conn = sqlite3.connect('sensor_data.db')
c = conn.cursor()

c.execute('''CREATE TABLE moisture_data
             (time, plant_1, plant_2, plant_3, plant_4)''')

moisture_data = MoistureData()
gantry = GantryControls()
led = LED()

schedule.every().minute.do(job)

directory_name = 'images'

while True:
    schedule.run_pending()
    time.sleep(1)
