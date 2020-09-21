"""
基于threading的多进程网络并发
"""

from threading import Thread
import os, sys
from socket import *


def handle(conn):
    while True:
        data = conn.recv(2048)
        if not data:
            break
        print(data.decode())
        conn.send(b'OK')
    conn.close()


s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(5)

while True:
    try:
        conn, addr = s.accept()
    except KeyboardInterrupt:
        print("退出服务器")
        sys.exit()
    except Exception as e:
        print(e)
        continue

        # 创建新的线程处理客户端请求

    t = Thread(target=handle, args=(conn,))
    t.setDaemon(True)
    t.start()
