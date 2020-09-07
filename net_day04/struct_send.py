"""

    struct 模块

"""

import struct
from socket import *

ADDR = ("127.0.0.1", 8888)

s = socket(AF_INET, SOCK_DGRAM)

st = struct.Struct("i32sif")

while True:
    print("==============")
    id = int(input("ID:"))
    name = input("NAME:").encode()
    age = int(input("AGE:"))
    score = float(input("SCORE:"))

    # 数据打包
    data = st.pack(id, name, age, score)

    s.sendto(data, ADDR)
