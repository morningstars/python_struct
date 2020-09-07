"""

    读取文件 发送

"""

from socket import *

f = open("timg.jpg", "rb")

s = socket()
s.connect(("0.0.0.0", 8888))

while True:
    data = f.read(1024)
    if not data:
        break
    s.send(data)

s.close()
f.close()
