

from socket import *

s = socket(AF_INET, SOCK_DGRAM)

s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
s.bind(("0.0.0.0", 8080))

while True:
    try:
        msg, addr = s.recvfrom(1024)
    except KeyboardInterrupt:
        break
    else:
        print("从 %s 接收到消息：%s" % (addr, msg.decode()))

s.close()
