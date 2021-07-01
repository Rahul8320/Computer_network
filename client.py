import socket

s = socket.socket()

host = '0.0.0.0'
port = 9999
s.connect((host, port))
print(s.recv(1024))
s.close()