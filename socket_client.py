#!/usr/bin/env python

import socket
import cv2
import struct
import pickle

HOST = '192.168.0.29'
PORT = 8200

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)
sock.connect(server_address)

data = b""
payload_size = struct.calcsize(">L")

try:
    # send image size to server
    message = "Computer Ready"
    sock.send(message.encode('utf-8'))

    data = sock.recv(4096)
    data = data.decode('utf-8')
    print(data)

    # while len(data) < payload_size:
    #     print("Recv: {}".format(len(data)))
    #     data += sock.recv(4096)
    #
    # print("Done Recv: {}".format(len(data)))
    # packed_msg_size = data[:payload_size]
    # data = data[payload_size:]
    # msg_size = struct.unpack(">L", packed_msg_size)[0]


    print("msg_size: {}".format(msg_size))

    while len(data) < msg_size:
        data += sock.recv(4096)
    frame_data = data[:msg_size]
    data = data[msg_size:]

    frame = pickle.loads(frame_data, fix_imports=True, encoding="bytes")
    frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
    cv2.imshow('ImageWindow', frame)
    cv2.waitKey(1)

    # image = open('image.png', 'wb')
    # # image.write(image_len)
    # data = sock.recv(40960000)
    # # data.decode('utf-8')
    # image.write(data)
    # image.close()
    #
    # # image = open('image.png')
    # # print(image)
    # image = cv2.imread('image.png')
    # cv2.imshow('image', image)
    #
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
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
