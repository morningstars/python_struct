from threading import Thread
from time import sleep


def func():
    sleep(3)
    print("线程属性测试")


t = Thread(target=func)

t.setName("Hello")
print(t.getName())

t.start()

print(t.is_alive())
t.join()

print(t.is_alive())
