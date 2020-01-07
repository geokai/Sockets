#!/usr/bin/env python3


import socket
from time import sleep


HOST = ''
PORT = 5000
INTERVAL = 25


message = b'Hello, from local client.\n\tHave a great day!'


def echo_client(msg):
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                s.sendall(msg)
                # data = s.recv(1024)
                # print(repr(data))

        except Exception as e:
            pass

        sleep(INTERVAL)


if __name__ == "__main__":
    try:
        echo_client(message)
    except KeyboardInterrupt:
        print(" :Quitting!")
    finally:
        exit()
