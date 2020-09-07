"""

    socket udp client

"""
from socket import *

HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)

s = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input("消息：")
    if not data:
        break

    s.sendto(data.encode(), ADDR)
    data, addr = s.recvfrom(1024)
    print("返回数据：", data.decode())

s.close()
