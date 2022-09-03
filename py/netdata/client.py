import socket
import screen

client = socket.socket()
ip = input("请输入IP：")
port = input("请输入端口：")
client.connect((ip, port))
png_bytes = screen.screen_cap_from_phone()
client.send(png_bytes)
client.close()
