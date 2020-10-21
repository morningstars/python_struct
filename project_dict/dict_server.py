from socket import *
from sql_method import *

sql_method = Sql_method()

socket = socket(AF_INET, SOCK_STREAM)

socket.bind(('0.0.0.0', 8088))
socket.listen(5)

while True:
    try:
        conn, addr = socket.accept()
    except KeyboardInterrupt as e:
        print(e)
        break

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break

        msgs = data.split(' ')
        print("接收到：", msgs)

        msg_back = None
        if msgs[0] == 'L':
            if sql_method.login(msgs[1], msgs[2]):
                msg_back = "Login Success!"
            else:
                msg_back = "Login Failure!"
        elif msgs[0] == 'R':
            if sql_method.register(msgs[1], msgs[2]):
                msg_back = "Register Success!"
            else:
                msg_back = "Register Failure!"
        conn.send(msg_back.encode())

    conn.close()

socket.close()
