import socket
import select

HOST = '192.168.0.29'
PORT = 8200

connected_clients_sockets = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(10)


while True:
    read_sockets, write_sockets, error_sockets = select.select(connected_clients_sockets, [], [])

    for sock in read_sockets:
        if sock == server_socket:
            sockfd, client_address = server_socket.accept()
            connected_clients_sockets.append(sockfd)
        else:
            try:
                data = sock.recv(4096)
                txt = str(data)
                if data:
                    print(txt)
                    sock.sendall("Hi")
            finally:
                sock.close()
                connected_clients_sockets.remove(sock)
    server_socket.close()
