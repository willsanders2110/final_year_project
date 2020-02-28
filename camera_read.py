# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
rawCapture = PiRGBArray(camera)

# allow the camera to warmup
time.sleep(0.1)

# Read time, and take image every hour or so
# Make sure that this can be updated by changing a variable!

# grab an image from the camera
camera.capture(rawCapture, format="bgr")
image = rawCapture.array

lt = time.localtime(time.time())
time = "{}_{}_{}_{}_{}".format(lt.tm_year, lt.tm_mon, lt.tm_mday, lt.tm_hour, lt.tm_min)

# Check every time an image is taken whether it can be sent to the PC or not
# If not, then store the data
# If it can, check whether there is additional data to send, then send all

# PC just needs to be pinged, the PC itself doesn't need to actively send that it's ready

cv2.imwrite("{}.jpg".format(time), image)
