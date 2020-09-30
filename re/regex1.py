"""

"""

import re

s = 'Levi:1993,Sunny:1993'
pattern = r'(\w+):(\d+)'

# findall 如果有子组  只能获取子组的内容
l = re.findall(pattern, s)
print(l)

# compile对象调用
regex = re.compile(pattern)
l2 = regex.findall(s)
print(l2)

# split 分割
s3 = 'hello world how  arre you L-boby'
l3 = re.split(r'\W+', s3)
l32 = re.split(r'[^\w]+', s3)
print(l32)
print(l3)

# sub 替换 使用一个字符串替换正则表达式匹配到的内容
# 返回替换后的字符串
s4 = '时间：2020/09/29'
ns = re.sub(r'/', '-', s4, 0)

# subn返回替换后的字符串和替换了几处
ns2 = re.subn(r'/', '-', s4, 0)
print(ns)
print(ns2)

# finditer 返回迭代器
s5 = '2020年，建国71周年'
pattern = r'\d+'
it = re.finditer(pattern, s5)
for i in it:
    print(i.group())

# fullmatch 完全匹配
m = re.fullmatch(r'\w+', 'hello1973')
print(m.group())

# match 匹配开始位置
m = re.match(r'[A-Z]\w*', 'Hello_World')
print(m.group())

# search 匹配第一处
m = re.search(r'\S+', '好 \n 吗')
print(m.group())
