"""

    信号量

"""

from multiprocessing import Semaphore, Process
from _multiprocessing import SemLock
import os, time

sem = Semaphore(3)
semlock = SemLock(3)

def handle():
    print("%d 想执行" % os.getpid())
    semlock.acquire()
    # sem.acquire()
    print("%d 开始执行" % os.getpid())
    time.sleep(3)
    print("%d 结束执行" % os.getpid())
    # sem.release()
    semlock.release()

jobs = []
for i in range(5):
    p = Process(target=handle)
    jobs.append(p)
    p.start()

for i in jobs:
    i.join()

print(semlock._get_value())