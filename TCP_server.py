import socket
import threading 

host = "0.0.0.0"
port = 9990
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen(5)
print ("[*] Listening on %s:%d" % (host, port))

# this is our client-handling thread
def handle_client(client_socket):
    # print out what the client sends 
    request = client_socket.recv(4096)
    print ("[*] Received : %s" % (request))
    # send back one packet
    client_socket.send("ACK!")
    client_socket.close()
    
while True:
    client, addr = server.accept()
    print ("[*] Accepted connection from : %s:%d" % (addr[0], addr[1]))
    # spin up our client thread to handle incoming data 
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()
