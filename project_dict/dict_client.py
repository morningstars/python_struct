from socket import *

socket = socket(AF_INET, SOCK_STREAM)

socket.connect(('0.0.0.0', 8088))

while True:
    style = input("login or register：")
    if not style:
        break

    username = input("username:")
    password = input("password:")
    msg = None

    if style == 'login':
        msg = 'L ' + username + ' ' + password
    elif style == 'register':
        msg = 'R ' + username + ' ' + password

    socket.send(msg.encode())

    data = socket.recv(1024)
    print("receive from server:", data.decode())

socket.close()
