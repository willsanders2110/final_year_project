import socket
from picamera import PiCamera
import PiRGBArray
import time

HOST = '192.168.0.29'
PORT = 8200

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

    file = open(image, 'rb')
    image = file.read()
    size = str(len(image))
    connection.send(size.encode('utf-8'))

    data = connection.recv(4096)
    data = data.decode('utf-8')
    print(data)

    connection.send(image)

finally:
    server_socket.close()
