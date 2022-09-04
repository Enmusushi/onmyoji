import socket
import random

server = socket.socket()
port = 8080
server.bind(("192.168.1.56", port))
server.listen()
print("监听端口: {}".format(port))
conn, addr = server.accept()
print(conn)
print(addr)
count = 0
bytes_array = bytearray()
n_bytes = bytes()
a_byte = b''
for i in range(0, 10):
    data = conn.recv(1024)
    count += len(data)
    a_byte += data
    # print(data)
    # bytes_array.join(data)
    # a_byte.join(data)
print(a_byte)
print(len(a_byte))
f = open('test.png', 'wb')
f.write(a_byte)
f.close()
