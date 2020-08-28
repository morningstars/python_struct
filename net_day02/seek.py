"""

    文件偏移量

"""
import os

fd = open("test", "r")

# data = fd.read()
print(fd.tell())  # 获取偏移量

# 设置偏移量
fd.seek(5, 0)
print(fd.read())

print(fd.fileno())

fd.close()

# 系统对于文件的操作  一些方法


print(os.path.getsize("test"))  # 获取文件大小
print(os.listdir())  # 获取文件列表
print(os.path.exists("buffer.py"))  # 判断文件是否存在
print(os.path.isfile("test"))  # 判断文件类型

# os.makedirs()
