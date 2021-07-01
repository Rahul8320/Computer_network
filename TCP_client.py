# simple TCP client

import socket

host = "0.0.0.0"
port = 9990

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client to server 
client.connect((host, port))

# send some data to the server
a = raw_input('Enter msg : ')
client.send(a)

# receive some data from server 
response = client.recv(4096)
print (response)