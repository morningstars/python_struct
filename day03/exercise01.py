"""

循环 每个一秒输入

"""
import time

fd = open("text.txt", "a+")

fd.seek(0)

n = 1
for line in fd:
    n += 1

while True:
    time.sleep(1)
    fd.write("%d. %s\n" % (n, time.ctime()))
    fd.flush()
    n += 1
# fd.close()
