from picamera import PiCamera
from picamera.array import PiRGBArray
import time
import cv2


class Capture:
    def __init__(self):
        self.camera = PiCamera()
        self.raw_capture = PiRGBArray(self.camera)

    def image(self, image_name):
        # allow the camera to warmup
        time.sleep(0.1)

        # Read time, and take image every hour or so
        # Make sure that this can be updated by changing a variable!

        # grab an image from the camera
        self.camera.capture(self.raw_capture, format="bgr")
        image = self.raw_capture.array

        cv2.imwrite('{}.png'.format(image_name), image)

        # cv2.imshow('image', image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
