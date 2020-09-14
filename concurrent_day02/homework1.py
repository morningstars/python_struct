"""
multiprocess 创建两个进程
同时复制一个文件里的上下两部分内容到一个新的文件里
"""

from multiprocessing import Process
import os

file_name = "homework_target.txt"
file_size = os.path.getsize(file_name)
print(file_size)

file_head_name = "homework_head.txt"
file_rear_name = "homework_rear.txt"


def copy_head():
    with open(file_name, 'r') as f:
        with open(file_head_name, 'w') as fh:
            fh.write(f.read(int(file_size/2)))


def copy_rear():
    with open(file_name, 'r') as f:
        f.seek(int(file_size / 2), 0)
        with open(file_rear_name, 'w') as fr:
            fr.write(f.read())


p1 = Process(target=copy_head)
p2 = Process(target=copy_rear)

p1.start()
p2.start()

p1.join()
p2.join()
