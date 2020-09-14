from socket import *

import os

sock_file = './sock'

if os.path.exists(sock_file):
    os.remove(sock_file)

# 创建本地套接字
sockfd = socket(AF_UNIX, SOCK_STREAM)

# 绑定本地套接字
sockfd.bind(sock_file)

# 监听
sockfd.listen(5)
while True:
    c, addr = sockfd.accept()
    print(c)
    print(addr)
    while True:
        data = c.recv(2048)
        if not data:
            break
        print(data.decode())
    c.close()

sockfd.close()