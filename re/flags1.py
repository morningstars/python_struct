import re

s = """
Hello world
你好，世界
"""

# ASCII 只匹配ascii码字符
regex = re.compile(r'\w+', flags=re.A)

# I == IGNORECASE 匹配忽略字母大小写
regex2 = re.compile(r'[A-Z]+', flags=re.I)

# S == DOTALL 使 . 可以匹配换行
regex3 = re.compile(r'.+', flags=re.S)

# M == MULTILINE 使 ^ $可以匹配每一行的开头结尾位置
regex4 = re.compile(r'^你好', flags=re.M)

# X == VERBOSE 为正则添加注释
pattern = r"""\w+ # 第一部分
\s+ #第二部分
\w+ # 第三部分
"""
# 多个flag 用| 按位或连接
regex5 = re.compile(pattern, flags=re.X | re.I)

l1 = regex.findall(s)
l2 = regex2.findall(s)
l3 = regex3.findall(s)
l4 = regex4.findall(s)
l5 = regex5.findall(s)
print(l1)
print(l2)
print(l3)
print(l4)
print(l5)
