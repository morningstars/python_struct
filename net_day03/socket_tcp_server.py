"""

    socket 套接字
        字节流方式(SOCK_STREAM)：面向TCP
        数据报方式(SOCK_DGRAM)：面向UDP

"""

from socket import *

# AF_INET 表示ipv4
# SOCK_STREAM 表示 流
tcpSockServer = socket(family=AF_INET, type=SOCK_STREAM)

# 绑定地址
tcpSockServer.bind(('127.0.0.1', 8888))

# 设置监听 参数为监听队列的大小
tcpSockServer.listen(5)

while True:

    # 等待处理客户端连接
    # 返回两个参数 即返回一个元组
    print("waiting for connect...")

    try:
        connfd, addr = tcpSockServer.accept()
        print("connect from:", addr)
    except KeyboardInterrupt:
        print("out of connect")
        break

    while True:
        # 接受消息
        data = connfd.recv(1024)
        if not data:
            break

        print("接收到客户端消息：", data.decode())

        # 发送消息 需要传字节串
        n = connfd.send('Receive Msg'.encode())
        print("发送了%d个字节的数据" % n)

    connfd.close()

# 关闭socket
tcpSockServer.close()
