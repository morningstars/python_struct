from threading import Thread, Lock

lock = Lock()

a = b = 0


def func():
    while True:
        lock.acquire()
        if a != b:
            print("a = %d b = %d" % (a, b))
        lock.release()


t = Thread(target=func)
t.start()

while True:
    with lock: # with代码块结束后自动解锁
        a += 1
        b += 1

t.join()
