from socket import *

socket = socket(AF_INET, SOCK_STREAM)

socket.connect(('0.0.0.0', 8080))

while True:
    msg = input("输入：")
    if not msg:
        break
    socket.send(msg.encode())

    data = socket.recv(1024)
    print("receive from server:", data.decode())

socket.close()
