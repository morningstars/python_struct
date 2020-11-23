from socket import *
from getpass import getpass
import hashlib

socket = socket(AF_INET, SOCK_STREAM)
socket.connect(('0.0.0.0', 8088))


def do_register():
    while True:
        username = input("User:")
        password = getpass()
        password2 = getpass("Again:")

        if (' ' in username) or (' ' in password):
            print("用户名或密码不能有空格")
            continue

        if password != password2:
            print("两次密码不一致")
            continue

        msg = 'R %s %s' % (username, password)
        socket.send(msg.encode())

        data = socket.recv(128)
        print("receive from server:", data.decode())
        if data == 'OK':
            print("注册成功")
        else:
            print("注册失败")

        return


def do_login():
    pass


def do_logout():
    pass


def main():
    while True:
        print("""
        ===================welcome===================
        1.注册            2.登录              3.退出
        =============================================
        """)
        cmd = input("输入选项：")
        if cmd == '1':
            do_register()
        elif cmd == '2':
            do_login()
        elif cmd == '3':
            do_logout()
        else:
            print("请输入正确命令！")


if __name__ == '__main__':
    main()
