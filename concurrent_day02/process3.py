from multiprocessing import Process
from time import sleep


# 带参数的进程函数
def work(sec, name):
    for index in range(3):
        sleep(sec)
        print("I'm %s" % name)
        print("I'm working...")


# p = Process(target=work, args=(2,'zhangsan'))
p = Process(target=work, kwargs={'name': "lisi", 'sec': 3})

# 子进程随父进程一起退出
# 设为True 则不使用join()
p.daemon = True

p.start()
print(p.name)
print(p.pid)
print(p.is_alive())

p.join()

print(p.name)
print(p.pid)
print(p.is_alive())
