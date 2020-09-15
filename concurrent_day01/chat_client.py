from socket import *
import os, sys

HOST = '127.0.0.1'
PORT = 8888
ADDR = (HOST, PORT)

"""
    约定
        L ： 登录
        Q ： 退出
        C ： 聊天

"""


def main():
    s = socket(AF_INET, SOCK_DGRAM)

    while True:
        name = input("请输入姓名：")
        msg = "L " + name
        s.sendto(msg.encode(), ADDR)

        data, addr = s.recvfrom(1024)
        print(data.decode())

        # 如果不允许则重新输入
        if data.decode() == "OK":
            print("进入聊天室")
            break
        else:
            print(data.decode())

    pid = os.fork()

    if pid < 0:
        sys.exit("Fail")
    elif pid == 0:
        # 子进程 循环发送消息
        send_msg(s, name)
    else:
        # 父进程 循环接受消息
        recv_msg(s)


# 发送消息
def send_msg(s, name):
    while True:
        try:
            text = input("")
        except KeyboardInterrupt:
            text = "quit"

        if text == "quit":
            msg = "Q " + name
            s.sendto(msg.encode(), ADDR)
            sys.exit("退出聊天室")

        msg = "C %s %s" % (name, text)
        s.sendto(msg.encode(), ADDR)


# 接受消息
def recv_msg(s):
    while True:
        data, addr = s.recvfrom(2048)
        print(data.decode())
        # 服务端发送EXIT 让客户端退出
        if data.decode() == "EXIT":
            sys.exit()


if __name__ == '__main__':
    main()
