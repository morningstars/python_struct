import multiprocessing as mp
from time import sleep

a = 1


def fun():
    print("子进程执行开始")
    global a
    print("a = ", a)

    a = 10000
    sleep(3)

    print("子进程执行完毕")


# 创建进程对象
p = mp.Process(target=fun)

# 启动进程
p.start()

sleep(2)
print("父进程做事")

# 回收进程
# join()  阻塞进程 等待回收
p.join()

print("parent a:", a)
