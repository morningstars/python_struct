from multiprocessing import Process, Array

# shm = Array('i', [1, 2, 3])

shm = Array('c', b'hello')

def func():
    for index in shm:
        print(index)
    # 修改共享内存
    shm[0] = b'H'


p = Process(target=func)
p.start()
p.join()

for item in shm:
    print(item, end=" ")

# value属性访问字节串
print(shm.value)
