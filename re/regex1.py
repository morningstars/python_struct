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
