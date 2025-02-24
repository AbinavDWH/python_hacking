import socket

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ADDR='localhost'
HOST=5050

sock.bind((ADDR,HOST))

sock.connect((ADDR,HOST))

while True:
    message=input("enter ur message :")
    sock.send(message.encode())
    data=sock.recv(1024).decode()
    if message == "q":
        break
    if not data:
        break
    print(f"server {data}")



sock.close()
print("connection closed")
