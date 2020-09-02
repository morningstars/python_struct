"""

    struct
    接收数据 写入文件

"""

from socket import *
import struct

# 创建套接字
s = socket(AF_INET, SOCK_DGRAM)
s.bind(("0.0.0.0", 8888))

# 确定数据结构
st = struct.Struct("i32sif")

# 打开文件
f = open("test.txt", "a")

while True:
    data, addr = s.recvfrom(1024)
    if not data:
        break
    data = st.unpack(data)

    info = "%d %s %d %.2f \n" % (data[0], data[1].decode(), data[2], data[3])

    f.write(info)
    f.flush()

f.close()
s.close()
