from picamera import PiCamera
from picamera.array import PiRGBArray
import time
import cv2

camera = PiCamera()
rawCapture = PiRGBArray(camera)

# allow the camera to warmup
time.sleep(0.1)

# Read time, and take image every hour or so
# Make sure that this can be updated by changing a variable!

# grab an image from the camera
camera.capture(rawCapture, format="bgr")
image = rawCapture.array

cv2.imwrite('test_image.png', image)

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
