"""

    浏览器中http访问

"""

from socket import *

s = socket()
s.bind(("0.0.0.0", 8800))
s.listen(6)

c, addr = s.accept()
msg = c.recv(1024)
print(msg)

# c.send(b"404 not found")

# http响应格式
data = """HTTP/1.1 200 OK
Content-Type:text/html

<h1>hello world</h>
"""

c.send(data.encode())

c.close()
s.close()
