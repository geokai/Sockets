import socket
from time import sleep


HOST = '192.168.1.65'
PORT = 5000
INTERVAL = 25


message = b'Hello, from esp8266 client.\n\tBe of good cheer!'


def echo_client(msg):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, PORT))
            s.sendall(msg)
            # data = s.recv(1024)

            # print(repr(data))
            s.close()
        except Exception as e:
            pass
        sleep(INTERVAL)


if __name__ == "__main__":
    echo_client(message)
