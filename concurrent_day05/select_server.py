"""
IO多路复用

select方法使用
rs, ws, xs=select(rlist, wlist, xlist[, timeout])

功能: 监控IO事件，阻塞等待IO发生

参数：   rlist 列表 存放关注的等待发生的IO事件
        wlist 列表 存放关注的要主动处理的IO事件
        xlist 列表 存放关注的出现异常要处理的IO
        timeout 超时时间

"""

from select import *
from socket import *

s = socket()
s.bind(('0.0.0.0', 8088))
s.listen(5)

rlist = [s]
wlist = []
xlist = []

while True:
    # 监控IO的发生
    rs, ws, xs = select(rlist, wlist, xlist)
    # 遍历3个返回值列表 判断哪个IO发生
    for r in rs:
        if r is s:
            c, addr = r.accept()
            print(addr)
            rlist.append(c)  # 加入新的关注
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print(data)
            # r.send(b'OK')
            wlist.append(r)


    for w in ws:
        w.send(b'OK')
        wlist.remove(w)


    for x in xs:
        pass
