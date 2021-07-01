import socket

host = '192.168.43.62'
port = 9990

s=socket.socket()

s.bind((host,port))
s.listen(5)
print("Server is ready.")
while True:
    c,addr = s.accept()
    print("Got Connection from " ,addr) 
    c.send('Connection established')
    c.close()
    s.close()