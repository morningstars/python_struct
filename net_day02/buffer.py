"""

缓冲区

"""

# fd = open("test", "w", buffering=0) # 不允许无缓冲
# fd = open("test", "w", buffering=1)  # 行缓冲 遇见换行就写入
fd = open("test", mode="w", buffering=12)  # > 1 表示指定缓冲区的大小 (不识别)

while True:
    s = input(">>")
    fd.write(s + "\n")
    fd.flush()  # 立即刷新缓冲区  将内容写入磁盘

# fd.close()
