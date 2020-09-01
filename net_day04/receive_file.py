"""

    收取文件 写入

"""

from socket import *

f = open("image.jpg", "wb")

s = socket()
s.bind(("127.0.0.1", 8888))
s.listen(5)

conn, addr = s.accept()

while True:
    data = conn.recv(1024)
    if not data:
        break
    f.write(data)

conn.close()
s.close()
f.close()