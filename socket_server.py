import socket

image = "image.png"

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

    file = open(image, 'rb')
    image = file.read()
    size = str(len(image))
    connection.send(size.encode('utf-8'))

    data = connection.recv(4096)
    data = data.decode('utf-8')
    print(data)

    print(image)
    connection.send(image)

finally:
    server_socket.close()
