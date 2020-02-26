import io
import socket
import struct
import time
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2

# Connect a client socket to my_server:8000
client_socket = socket.socket()
client_socket.connect(('192.168.0.5', 8200))

# Make a file-like object out of the connection
connection = client_socket.makefile('wb')
try:
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

    # Note the start time and construct a stream to hold image data
    # temporarily (we could write it directly to connection but in this
    # case we want to find out the size of each capture first to keep
    # our protocol simple)
    stream = io.BytesIO()
    for foo in camera.capture_continuous(stream, 'jpeg'):
        # Write the length of the capture to the stream and flush to
        # ensure it actually gets sent
        connection.write(struct.pack('<L', stream.tell()))
        connection.flush()
        # Rewind the stream and send the image data over the wire
        stream.seek(0)
        connection.write(stream.read())

        # Reset the stream for the next capture
        stream.seek(0)
        stream.truncate()
    # Write a length of zero to the stream to signal we're done
    connection.write(struct.pack('<L', 0))

    connection.close()
    client_socket.close()
finally:
    connection.close()
    client_socket.close()
