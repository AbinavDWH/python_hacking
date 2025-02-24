import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
HOST = 'localhost'  # Use '' to listen on all available interfaces
PORT = 5050
sock.bind((HOST, PORT))

# Listen for incoming connections
sock.listen(5)
print(f"Server is listening on {HOST}:{PORT}...")

# Accept a connection
client_sock, client_addr = sock.accept()
print(f"Client connected from {client_addr} {client_sock}")

# Communicate with the client
try:
    while True:
        # Receive data from the client
        data = client_sock.recv(1024).decode()
        if not data:
            break  # Exit if the client disconnects
        print(f"Client: {data}")

        # Send a response to the client
        message = input("Enter your message: ")
        client_sock.sendall(message.encode())
        if message == "q":
            break  # Exit if the server sends 'q'
finally:
    # Clean up the connection
    client_sock.close()
    sock.close()
    print("Connection closed.")
