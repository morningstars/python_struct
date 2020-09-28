import re

str = "001hello world hella 你好 世界 ！！ abcdefg 张三丰 张四丰 张丰"

# 普通字符
print(re.findall('ab', str))  # ['ab']
print(re.findall('你好', str))  # ['你好']

# |
# 或关系
print(re.findall('你好 | abcd', str))  # ['你好 ', ' abcd']

# .
# 匹配单个字符
print(re.findall('张.丰', str))  # ['张三丰', '张四丰']

# [...]
# 匹配字符集
# [abc#] 表示[]中任意一个字符
# [0-9][a-z][A-Z] 表示区间内任意一个字符
# [_#?0-9a-zA-Z] 混合书写 区间写在后面
print(re.findall('[abcd]', str))  # ['d', 'a', 'a', 'b', 'c', 'd']
print(re.findall('[a-z]',
                 str))  # ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd', 'h', 'e', 'l', 'l', 'a', 'a', 'b', 'c', 'd', 'e', 'f', 'g']

# [^...]
# 匹配字符集反集
print(
    re.findall('[^ a-z]', str))  # ['0', '0', '1', '你', '好', '世', '界', '！', '！', '张', '三', '丰', '张', '四', '丰', '张', '丰']

# ^
# 匹配字符集开始位置
print(re.findall('Jame', "Hi Jame"))  # ['Jame']
print(re.findall('^Jame', "Hi Jame"))  # []

# $
# 匹配字符集结束位置
print(re.findall('Jame$', "Hi Jame"))  # ['Jame']

# 注： ^和$ 必然出现在正则表达式的开头和结尾   如果同时出现，则中间部分必须完全匹配
print(re.findall('^Jame$', "Jame"))  # ['Jame']

#  *
#  匹配前面的字符出现0次或多次
print(re.findall('wo*', "woooooo~~w!"))  # ['woooooo', 'w']

# 匹配出以大写字母开头的单词
print(re.findall('[A-Z][a-z]*', "Hello World,Hi Tom hello kitty"))  # ['Hello', 'World', 'Hi', 'Tom']

#  +
#  匹配前面的字符出现1次或多次
print(re.findall('[A-Z][a-z]+', "A Boy"))  # ['Boy']
print(re.findall('[A-Z][a-z]*', "A Boy"))  # ['A', 'Boy']

#  ？
#  匹配前面的字符出现0次或1次
print(re.findall('[A-Z][a-z]?', "A Boy"))  # ['A', 'Bo']

print(re.findall('-?[0-9]+', "工资：1800，小刚：-500"))  # ['1800', '-500']

# {n}
# 匹配前面的字符出现n次
print(re.findall('1[0-9]{10}', 'jame:19000009919'))

# {m,n}
# 匹配前面的字符出现m-n次
print(re.findall('[1-9][0-9]{5,10}', 'jame:19000009919, 19999'))

# \d \D
# 匹配任意数字/非数字字符
print(re.findall(r'\d{1,5}', 'mysql: 3306, http: 80'))
print(re.findall(r'\D+', 'mysql: 3306, http: 80'))

# 匹配数字 整数小数正数负数
print(re.findall(r'-?\d+\.?\d*', str))

# \w \W
# 匹配任意普通/非普通字符  普通字符：数字 字母 下划线 汉字
print(re.findall(r'\w+', 'mysql: !3306, ~哈http: __80'))
print(re.findall(r'\W+', 'mysql: !3306, ~http: __80'))

# \s \S
# 匹配任意空/非空字符 空字符：\r \n \t \v \f
print(re.findall(r'\s+', "hello world !!"))
print(re.findall(r'\S+', "hello world !!"))

# \A \Z 匹配开头结尾位置

# \b \B
# 匹配单词/非单词边界位置
print(re.findall(r'\Bis\B', 'This is a aisa test'))

# 前面加r 表示转义

# 贪婪/非贪婪模式
# 后面加? 转为非贪婪模式
# * : *?
# + : +?
# ? : ??
# {m,n} : {m,n}?
print(re.findall(r'ab*', 'abbbbbbb'))
print(re.findall(r'ab*?', 'abbbbbbb'))
print(re.findall(r'ab+', 'abbbbbbb'))
print(re.findall(r'ab+?', 'abbbbbbb'))
print(re.findall(r'ab?', 'abbbbbbb'))
print(re.findall(r'ab??', 'abbbbbbb'))
print(re.findall(r'ab{3,5}?', 'abbbbbbb'))

print(re.findall(r'\(.+?\)', "(hello world),zha(Tom)"))

# ()内部分组
# 表达式分组
print(re.search(r'(ab)+', 'abababab').group())
print(re.search(r'(王|李)\w{1,3}', '王者荣耀').group())


# 匹配身份证号
print(re.search(r'^[1-9]\d{5}(18|19|20)\d{2}((0[1-9])|10|11|12)(([0-2][1-9])|10|20|30|31)\d{3}[xX0-9]$', '320481199112140418').group())
# print(re.findall('^[1-9]\\d{5}(18|19|([23]\\d))\\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\\d{3}[0-9Xx]$', '320481199112140418'))
# print(re.findall('^[1-9]\\d{5}\\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\\d{3}$', '320481199112140418'))

print(re.findall(r'ab|cd', 'abcd'))
