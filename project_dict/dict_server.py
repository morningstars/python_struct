from socket import *
from sql_method import *
from multiprocessing import Process
import signal
import sys


def do_login(conn, msgs, sql_method):
    if sql_method.login(msgs[1], msgs[2]):
        conn.send(b'OK')
    else:
        conn.send(b'Failure')


def do_register(conn, msgs, sql_method):
    if sql_method.register(msgs[1], msgs[2]):
        conn.send(b'OK')
    else:
        conn.send(b'Failure')


def handle_request(conn, sql_method):
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break

        msgs = data.split(' ')
        print("接收到：", msgs)

        if msgs[0] == 'L':
            do_login(conn, msgs, sql_method)
        elif msgs[0] == 'R':
            do_register(conn, msgs, sql_method)

    conn.close()

    socket.close()


def main():
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', 8088))
    s.listen(5)

    sql_method = Sql_method()

    while True:
        try:
            conn, addr = s.accept()
        except KeyboardInterrupt as e:
            print(e)
            break

        handle_request(conn, sql_method)


if __name__ == '__main__':
    main()
