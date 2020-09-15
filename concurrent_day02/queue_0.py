"""

    消息队列

"""


from multiprocessing import Queue, Process
import os, time
import random

q = Queue(5)


def request():
    for i in range(20):
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        q.put((x, y))


def handle():
    while True:
        time.sleep(0.5)
        try:
            x, y = q.get(timeout=3)
        except:
            break
        else:
            print("%d + %d = %d" % (x, y, x + y))


p1 = Process(target=request)
p2 = Process(target=handle)
p1.start()
p2.start()
p1.join()
p2.join()
