"""

线程示例

"""

from threading import Thread
from time import sleep
import os


def func2():
    for i in range(5):
        sleep(1)
        print(os.getpid(), "播放电影%d" % i)


def func():
    for i in range(5):
        sleep(2)
        print(os.getpid(), "播放歌曲%d" % i)


t = Thread(target=func)
t2 = Thread(target=func2)
t.start()
t2.start()

# 主线程任务
for i in range(3):
    sleep(3)
    print(os.getpid(), "看电视")

t.join()
t2.join()
