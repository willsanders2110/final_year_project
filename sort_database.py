import sqlite3
import math
import os


def roundup(x):
    return int(math.ceil(x / 100.0)) * 100


conn = sqlite3.connect('sensor_data.db')
c = conn.cursor()

# c.execute('SELECT plant_1 FROM correct_moisture_data ORDER BY plant_1 DESC LIMIT 1')
# max_1 = c.fetchall()[0][0]
#
# c.execute('SELECT plant_2 FROM correct_moisture_data ORDER BY plant_2 DESC LIMIT 1')
# max_2 = c.fetchall()[0][0]
#
# c.execute('SELECT plant_3 FROM correct_moisture_data ORDER BY plant_3 DESC LIMIT 1')
# max_3 = c.fetchall()[0][0]
#
# c.execute('SELECT plant_4 FROM correct_moisture_data ORDER BY plant_4 DESC LIMIT 1')
# max_4 = c.fetchall()[0][0]
#
# max_sensor_val = int(max(max_1, max_2, max_3, max_4))
# sensor_bounds = roundup(max_sensor_val/5)


def get_timestamp_and_pos(image_name):
    image_name = image_name.split('.png')[0]

    pos = image_name.split('_')[4]

    month = image_name.split('_')[0]
    day = image_name.split('_')[1]
    hour = image_name.split('_')[2]
    minute = image_name.split('_')[3]
    ts = '{}_{}_{}_{}'.format(month, day, hour, minute)

    return pos, ts


for image in os.listdir('images'):
    plant_pos, timestamp = get_timestamp_and_pos(image)
    # print(plant_pos)
    # print(timestamp)
    sql_select_query = 'SELECT * FROM moisture_data WHERE time == ?'
    c.execute(sql_select_query, (timestamp, ))
    moisture_data = c.fetchall()
    if len(moisture_data) > 0:
        moisture_data = moisture_data[0][int(plant_pos)]
        moisture_data = int(moisture_data)
        if 0 <= moisture_data <= 200:
            os.rename("images/{}".format(image), "image_classes/0_200/{}".format(image))
        elif 201 <= moisture_data <= 400:
            os.rename("images/{}".format(image), "image_classes/201_400/{}".format(image))
        elif 401 <= moisture_data <= 600:
            os.rename("images/{}".format(image), "image_classes/401_600/{}".format(image))
        elif 601 <= moisture_data <= 800:
            os.rename("images/{}".format(image), "image_classes/601_800/{}".format(image))
        elif 801 <= moisture_data <= 1000:
            os.rename("images/{}".format(image), "image_classes/801_1000/{}".format(image))
        else:
            os.rename("images/{}".format(image), "image_classes/1000+/{}".format(image))
