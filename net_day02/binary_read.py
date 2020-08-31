"""
二进制
"""

fd = open("test", "rb")

data = fd.read()  # 得到字节串

print(data)
print(data.decode())

fd.close()

# with
# with生成的对象在代码块结束时会自动释放
with open("test", "rb") as f:
    data = f.read()
    print(data)

# 结束  f自动释放
