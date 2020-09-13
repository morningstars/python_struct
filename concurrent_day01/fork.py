"""

fork()会生成一个子线程，子线程会拷贝父线程开辟的空间中的内容
子线程从fork（）的下一句代码开始执行
子线程fork()返回的是0 即表示新进程
父线程fork()返回的不是0

孤儿进程与僵尸进程
孤儿：父进程先于子进程退出
僵尸：子进程先于父进程退出 父进程没有处理子进程的退出状态


"""

import os

import sys

pid = os.fork()

if pid < 0:
    print("Success")
elif pid == 0:
    print("New")
else:
    print("Old")

print("Fork test over")

print("进程号：", os.getpid())
print("父进程：", os.getppid())

# os._exit(0)

# 进程结束 打印文字
sys.exit("hhello wwol")
