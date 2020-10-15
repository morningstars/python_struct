"""
给出端口号 获取ip
"""

import re

with open('1.txt', 'r') as f:
    content = f.read()

port = input("输入端口号：")

m = re.split(r'\n\n', content)
for i in m:
    try:
        result = re.match(r'\S+', i).group()
        # print(result)

        if port == result:
            pattern = r'[a-z0-9]{4}\.[a-z0-9]{4}\.[a-z0-9]{4}'
            ip_str = re.search(pattern, i).group()
            print(ip_str)

    except:
        continue




