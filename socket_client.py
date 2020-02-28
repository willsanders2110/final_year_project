#!/usr/bin/env python

import random
import socket, select
from time import gmtime, strftime
from random import randint

image = "tux.png"

HOST = '192.168.0.29'
PORT = 8200

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)
sock.connect(server_address)

try:

    # open image
    myfile = open(image, 'rb')
    bytes = myfile.read()
    size = len(bytes)

    # send image size to server
    sock.sendall("SIZE %s" % size)
    answer = sock.recv(4096)

    print('answer = %s' % answer)

    # send image to server
    if answer == 'GOT SIZE':
        sock.sendall(bytes)

        # check what server send
        answer = sock.recv(4096)
        print('answer = %s' % answer)

        if answer == 'GOT IMAGE':
            sock.sendall("BYE BYE ")
            print('Image successfully send to server')

    myfile.close()

finally:
    sock.close()

# # initialize the camera and grab a reference to the raw camera capture
# camera = PiCamera()
# rawCapture = PiRGBArray(camera)
#
# # allow the camera to warmup
# time.sleep(0.1)
#
# # Read time, and take image every hour or so
# # Make sure that this can be updated by changing a variable!
#
# # grab an image from the camera
# camera.capture(rawCapture, format="bgr")
# image = rawCapture.array
#
# lt = time.localtime(time.time())
# time = "{}_{}_{}_{}_{}".format(lt.tm_year, lt.tm_mon, lt.tm_mday, lt.tm_hour, lt.tm_min)
#
# # Check every time an image is taken whether it can be sent to the PC or not
# # If not, then store the data
# # If it can, check whether there is additional data to send, then send all
#
# # PC just needs to be pinged, the PC itself doesn't need to actively send that it's ready
#
# cv2.imwrite("{}.jpg".format(time), image)
