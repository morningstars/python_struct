"""

    udp的广播  一端发送 多端接收

"""
from socket import *

s = socket(AF_INET, SOCK_DGRAM)

s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

ADDR = ("192.168.2.255", 8080)

# data, addr = s.recvfrom(1024)

while True:
    data = input("消息：")
    if not data:
        s.sendto(data.encode(), ADDR)
    else:
        break

s.close()
