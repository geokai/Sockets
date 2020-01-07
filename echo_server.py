#!/usr/bin/env python3


import socket


HOST = ''
PORT = 65432


def echo_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        print("Listening on: ", s)    # bebug
        s.listen()
        client_conn, client_addr = s.accept()
        print("Reply via: ", client_conn)
        with client_conn:
            print('Connection from: ', client_addr)
            while True:
                data = client_conn.recv(255)
                print("data from {}: {}".format(client_addr, data.rstrip()))
                if not data:
                    print("Client {} has closed the connection.".format(client_addr))
                    break
                client_conn.sendall(b'echo: ' + data)


if __name__ == "__main__":
    echo_server()
