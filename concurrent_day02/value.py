"""

    共享内存通信

"""

from multiprocessing import Value, Process
from random import randint
import time

money = Value('i', 5000)


def man():
    for i in range(30):
        time.sleep(0.1)
        money.value += randint(0, 5000)


def girl():
    for i in range(30):
        time.sleep(0.2)
        money.value -= randint(100, 3000)


m = Process(target=man)
g = Process(target=girl)

m.start()
g.start()

m.join()
g.join()

re = money.value
print(re)
