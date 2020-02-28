import socket
import select

HOST = '192.168.0.29'
PORT = 8200

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(10)

while True:
    server_socket.accept()
    try:
        data = server_socket.recv(4096)
        print(data.decode('utf-8'))
        message = "Hi"
        server_socket.send(message.encode('utf-8'))
    finally:
        server_socket.close()
