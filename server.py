import socket
import threading

port = 3000
SERVER = socket.gethostbyname(socket.gethostname())
ADDR=(SERVER,port)
#print(socket.gethostname())

server =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn,addr):
    pass

def start():
    server.listen()
    while True:
        conn , addr =socket.accept()
        thread = threading.Thread(target=handle_client,arg=(conn,addr))
        thread.start()
        print(f'[active connections] {threading.active_count()-1}')    
#tech with tim yt channel name

start()
