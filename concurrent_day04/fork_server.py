"""
基于fork的多进程网络并发
"""

from socket import *
import os, sys
import signal

# 客户端处理函数
def handle(c):
    print("客户端：", c.getpeername())
    while True:
        data = conn.recv(2048)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()


addr = ('127.0.0.1', 8888)
s = socket(AF_INET, SOCK_STREAM)
# 设置套接字的地址重用
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(addr)
s.listen(5)

# 僵尸进程的处理
signal.signal(signal.SIGCHLD, signal.SIG_IGN)
print("监听端口：8888")

# 循环等待客户端连接
while True:
    try:
        conn, addr = s.accept()
    except KeyboardInterrupt:
        sys.exit("服务器退出")
    except Exception as e:
        print(e)
        continue

    # 创建子进程处理客户端请求
    pid = os.fork()
    if pid < 0:
        print("failure")
    elif pid == 0:
        s.close()
        handle(conn)
        os._exit(0)
    else:
        conn.close()
