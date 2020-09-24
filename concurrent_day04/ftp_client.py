from threading import Thread
from socket import *
import os, sys
from time import sleep

HOST = '0.0.0.0'
PORT = 8088
ADDR = (HOST, PORT)


class FtpClient:

    def __init__(self, sockfd):
        self.sockfd = sockfd

    def do_list(self):
        self.sockfd.send(b'L')

        data = self.sockfd.recv(128).decode()

        if data == 'OK':
            data = self.sockfd.recv(2048).decode()
            print(data)

    def do_quit(self):
        self.sockfd.send(b'Q')
        self.sockfd.close()
        sys.exit("谢谢使用")

    def get_file(self, filename):
        self.sockfd.send(('G ' + filename).encode())
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            # 接受内容 写入文件
            with open(filename, 'wb') as f:
                while True:
                    data = self.sockfd.recv(1024)
                    if data == b'##':
                        break
                    f.write(data)
        else:
            print(data)

    # 上传文件
    def put_file(self, filename):
        try:
            f = open(filename, 'rb')
        except Exception as e:
            print(e)
            return

        filename = filename.split('/')[-1]
        self.sockfd.send(('P ' + filename).encode())
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            while True:
                data = f.read(1024)
                if not data:
                    sleep(0.1)
                    self.sockfd.send(b'##')
                    break
                self.sockfd.send(data)
            f.close()
        else:
            print(data)


def request(sockfd):
    ftp = FtpClient(sockfd)

    while True:
        print('\n==========命令选项===========')
        print('**********  list  **********')
        print('********  get file  ********')
        print('********  put file  ********')
        print('**********  quit  **********')
        print('============================')
        cmd = input('输入命令：')
        if cmd == 'list':
            ftp.do_list()
            # sockfd.send(cmd.encode())
        elif cmd == 'quit':
            ftp.do_quit()
        elif cmd[:3] == 'get':
            # strip() 去除首尾空格
            filename = cmd.strip().split(' ')[-1]
            ftp.get_file(filename)
        elif cmd[:3] == 'put':
            filename = cmd.strip().split(' ')[-1]
            ftp.put_file(filename)


def main():
    sockfd = socket()

    try:
        sockfd.connect(ADDR)
    except Exception as e:
        print(e)
        return
    else:

        print('\n==========文件种类===========')
        print('**********  file   image   data  **********')
        print('============================')

        msg = input("选择文件种类：")

        if msg not in ['data', 'image', 'file']:
            print('Error')
            return
        else:
            sockfd.send(msg.encode())
            request(sockfd)


if __name__ == '__main__':
    main()
