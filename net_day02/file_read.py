"""
文件读写操作
"""

fd = open("test", mode="r")

# 读操作
# read([size]) size为字节  默认到文件的末尾
# 如果不指定大小，则当文件过大时，会消耗大量内存，读取时间也很长

# 循环读取
# while True:
#     data = fd.read(8)
#     if not data:
#         break
#     print("读取到的内容：" + data)



# 读取一行内容 遇见换行则终止
# 如果指定size 则读取size大小的内容
# 再次调用则接着到一行结束
# data = fd.readline(3)
# data = fd.readline()  # 读取一行中剩余的内容
# print(data)


# 读取内容作为列表返回
# data = fd.readlines()
# print(data)



# fd 为可迭代对象 for循环获取每一行的内容
for line in fd:
    print(line)



fd.close()





