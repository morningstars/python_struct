"""

打开文件

Character Meaning
    --------- ---------------------------------------------------------------
    'r'       读 必须有文件 （默认）
    'w'       写 没有文件则创建文件  有文件则清空文件内容
    'a'       写 没有文件则创建文件  追加文件内容

    'r+'       读写 必须有文件 （默认）
    'w+'       读写 没有文件则创建文件  有文件则清空文件内容
    'a+'       读写 没有文件则创建文件  追加文件内容

    'b'       二进制打开

    'x'       create a new file and open it for writing
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)

"""

# fd = open("file_write.py")
# fd2 = open("../day01/node.py")
#
# try:
#     fd3 = open("file_write.py")
# except FileNotFoundError as e:
#     print(e)
# else:
#     print("打开成功")



# fd4 = open("file_write.py", mode="r", buffering=0, encoding="utf-8")
fd = open("text2", mode="a")

# # 开始读写
# # fd.read()
# fd.write("world")

# 关闭文件
fd.close()


# 关键字 with
# with：在不再需要访问文件后将文件关闭
with open("text") as file_obj:
    contents = file_obj.read()
    print(contents)

