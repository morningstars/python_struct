"""
ftp 文件服务器
"""

from threading import Thread
from socket import *
import os, sys
from time import sleep

HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)
FTP = '/Users/morningstar/Desktop/app/'  # 文件库路径


# 将客户端请求功能封装为类
class FtpServer:
    def __init__(self, conn, path):
        self.conn = conn
        self.path = path

    def do_list(self):
        # 获取文件列表
        files = os.listdir(self.path)
        print(files)
        if not files:
            self.conn.send('空'.encode())
            return
        else:
            self.conn.send(b'OK')
            sleep(0.1)

        # 循环发送
        fs = ''  # 大字符串拼接
        for file in files:
            if file[0] != '.' and os.path.isfile(self.path + file):
                fs += file + '\n'

        self.conn.send(fs.encode())

    def do_get(self, filename):
        try:
            f = open(self.path + filename, 'rb')
        except Exception as e:
            self.conn.send('文件不存在'.encode())
            return
        else:
            self.conn.send(b'OK')
            sleep(0.1)

        # 发送文件内容
        while True:
            data = f.read(1024)
            if not data:
                sleep(0.1)
                self.conn.send(b'##')
                break
            self.conn.send(data)

    def do_put(self, filename):
        if os.path.exists(self.path + filename):
            self.conn.send("文件已存在".encode())
            return
        self.conn.send(b'OK')

        with open(self.path + filename, 'wb') as f:
            while True:
                data = self.conn.recv(1024)
                if data == b'##':
                    break
                else:
                    f.write(data)


# 处理客户端请求
def handle(conn):
    cls = conn.recv(1024).decode()
    FTP_PATH = FTP + cls + '/'
    ftp = FtpServer(conn, FTP_PATH)

    while True:
        data = conn.recv(1024).decode()

        print(FTP_PATH, ':', data)
        if not data or data[0] == "Q":
            return
        elif data[0] == 'L':
            ftp.do_list()
        elif data[0] == 'G':
            filename = data.split(' ')[-1]
            ftp.do_get(filename)
        elif data[0] == 'P':
            filename = data.split(' ')[-1]
            ftp.do_put(filename)


def main():
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(5)

    while True:
        try:
            conn, addr = s.accept()
            print("addr", addr)
        except KeyboardInterrupt:
            return
        except Exception as e:
            print(e)
            continue

        # 多线程处理
        t = Thread(target=handle, args=(conn,))
        t.setDaemon(True)
        t.start()


if __name__ == '__main__':
    main()
