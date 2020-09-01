"""

    socket udp server

"""

from socket import *

# 创建SOCK_DGRAM类型socket
s = socket(AF_INET, SOCK_DGRAM)

s.bind(("0.0.0.0", 8888))

while True:

    data, addr = s.recvfrom(1024)
    print("receive from :", addr)
    print(data)

    s.sendto("收到".encode(), addr)

s.close()
