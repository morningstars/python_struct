"""
match对象属性
"""

import re

pattern = r'(ab)cd(?P<pig>ef)'

regex = re.compile(pattern)

# 获取match对象
obj = regex.search('abcdefghi')

# 属性变量
print(obj.pos)
print(obj.endpos)
print(obj.re)
print(obj.string)
print(obj.lastgroup)  # 最后一组名称
print(obj.lastindex)  # 最后一组序号
print('================')

# 属性方法
print(obj.start())  # 开始位置
print(obj.end())  # 结束位置
print(obj.span())  # 起止位置

print(obj.groupdict())  # 获取捕获组字典，组名为键，对应内容为值
print(obj.groups())  # 获取子组对应内容

print(obj.group())  # 默认参数为0 获取整个内容
print(obj.group(1))  # 序号名
print(obj.group('pig'))  # 组名
