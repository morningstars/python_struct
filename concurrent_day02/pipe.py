"""

    进程间通信

"""
from multiprocessing import Pipe, Process
import os, time

fd1, fd2 = Pipe()


def fun(name):
    time.sleep(3)
    # 向管道中写入内容
    fd1.send({name: os.getpid()})


jobs = []
for index in range(5):
    p = Process(target=fun, args=(index,))
    jobs.append(p)
    p.start()

for index in range(5):
    # 父进程读取管道
    data = fd2.recv()
    print(data)


for index in jobs:
    index.join()
