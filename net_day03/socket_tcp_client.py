"""

    客户端

"""

from socket import *

# 创建套接字 socket
sockfd = socket()

# 发起连接
sockfd.connect(("0.0.0.0", 8888))

while True:

    data = input("请输入：")

    if not data:
        break

    # 发送消息 需要传字节串
    sockfd.send(data.encode())

    # 接收到消息
    data = sockfd.recv(1024)
    print("接收到服务器消息：", data.decode())

# 关闭连接
sockfd.close()
