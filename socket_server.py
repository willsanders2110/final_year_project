import socket
from picamera import PiCamera
from picamera.array import PiRGBArray
import time
import cv2
import struct
import pickle

HOST = '192.168.0.29'
PORT = 8200

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(10)


connection, address = server_socket.accept()
try:
    data = connection.recv(4096)
    data = data.decode('utf-8')
    print(data)

    message = "Raspberry Pi Ready"
    connection.send(message.encode('utf-8'))

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

    result, frame = cv2.imencode('.jpg', image, encode_param)

    data = pickle.dumps(frame, 0)
    size = len(data)

    # print("{}: {}".format(img_counter, size))
    connection.sendall(struct.pack(">L", size) + data)

    # cv2.imwrite("image.png", image)
    #
    # my_file = open(image, 'rb')
    # image_bytes = my_file.read()
    #
    # connection.send(image_bytes)

finally:
    server_socket.close()
