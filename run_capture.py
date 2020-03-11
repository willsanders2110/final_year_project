from capture_image import Capture
import schedule
import time

capture = Capture()
local_time = time.localtime()

directory_name = 'images'


def job():
    hr = local_time.tm_hour
    day = local_time.tm_mday
    month = local_time.tm_mon
    image_name = '{}/{}_{}_{}'.format(directory_name, month, day, hr)

    capture.image(image_name)


schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
