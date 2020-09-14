# 进程池

from multiprocessing import Pool
from time import sleep,ctime

def func(msg):
    sleep(2)
    print(msg)


# 创建进程池
pool = Pool(3)

# 往进程池添加事件
for i in range(20):
    msg = "hello %d"%i
    pool.apply_async(func=func, args=(msg,))


# 关闭进程池
# 即不往进程池再加入事件
pool.close()

# 回收进程池
# 阻塞等待现有进程池中进程执行完毕
pool.join()
