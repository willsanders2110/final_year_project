import socket

HOST = '192.168.0.29'
PORT = 8200

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(10)

while True:
    connection, address = server_socket.accept()
    try:
        print("got here")
        data = connection.recv(4096)
        print(data.decode('utf-8'))
        message = "Hi"
        connection.send(message.encode('utf-8'))
    finally:
        server_socket.close()
