from socket import *
import os, sys

ADDR = ("127.0.0.1", 8888)
FileName = "names.txt"

# 存储用户信息
user = {}


# 网络请求
def do_request(s):
    while True:
        data, addr = s.recvfrom(1024)

        # 接收到姓名 判断是否允许进入  通知其他客户
        print(data.decode())
        msg = data.decode().split(" ")

        # 区分请求类型
        if msg[0] == "L":
            do_login(s, msg[1], addr)
        elif msg[0] == "C":
            text = " ".join(msg[2:])
            do_chat(s, msg[1], text)
        elif msg[0] == "Q":
            if msg[1] not in user:
                s.sendto(b"EXIT", addr)
                continue
            do_quit(s, msg[1])


# 登录
def do_login(s, name, addr):
    if name in user or "管理员" in name:
        s.sendto("用户已存在".encode(), addr)
        return

    s.sendto(b"OK", addr)

    msg = "欢迎%s进入聊天室" % name

    # 通知其他人
    for key in user:
        print("addr", user[key])
        s.sendto(msg.encode(), user[key])

    # 将用户加入
    user[name] = addr


def do_chat(s, name, text):
    msg = "%s : %s" % (name, text)
    for key in user:
        if key != name:
            s.sendto(msg.encode(), user[key])


def do_quit(s, name):
    msg = "%s退出聊天室" % name
    for key in user:
        if key != name:
            s.sendto(msg.encode(), user[key])
        else:
            s.sendto(b"EXIT", user[key])

    try:
        del user[name]
    except:
        print("")


# 创建网络连接
def main():
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(ADDR)

    pid = os.fork()
    if pid < 0:
        return
    # 子进程发送管理员消息
    elif pid == 0:
        while True:
            text = input("管理员消息：")
            msg = "C %s %s" % ("管理员", text)
            s.sendto(msg.encode(), ADDR)
    else:
        # 网络请求
        do_request(s)


if __name__ == "__main__":
    main()
