from threading import Event, Thread
from time import sleep

s = None # 共享操作

e = Event()


def func():
    print("----------------")
    global s
    s = ";"
    e.set()  # 共享资源操作结束


t = Thread(target=func)
t.start()
print("说对口令就是自己人")

e.wait(3)  # 阻塞等待

if s == ";":
    print("对")
else:
    print("错")

t.join()
