from socket import *

sock_file = './sock'

s = socket(AF_UNIX, SOCK_STREAM)

s.connect(sock_file)

while True:
    msg = input("输入：")

    if not msg:
        break

    s.send(msg.encode())

s.close()
