from socket import *

socket = socket(AF_INET, SOCK_STREAM)

socket.bind(('0.0.0.0', 8080))
socket.listen(5)

while True:
    try:
        conn, addr = socket.accept()
    except KeyboardInterrupt as e:
        print(e)
        break

    while True:
        data = conn.recv(1024)
        if not data:
            break

        print("接收到：", data.decode())

        msg = conn.send("accept msg".encode())
    conn.close()

socket.close()
