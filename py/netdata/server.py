import socket
import random

server = socket.socket()
port = random.randint(1001, 9999)
server.bind(("localhost", port))
server.listen()
print("监听端口: {}".format(port))
conn, addr = server.accept()
data = conn.recv()
print(data)
