import socket

# Define the server address and port
host = '192.168.77.28'  # private IP address of the server
port = 8080

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(1)

print(f"Server listening on {host}:{port}")

# Accept incoming connections
client_socket, client_address = server_socket.accept()

print(f"Connection from {client_address}")

# Receive data from the client
data = client_socket.recv(1024)
print("Received:", data.decode('utf-8'))

# Send a response to the client
client_socket.sendall(b'Hello, client!')

# Close the connection
client_socket.close()
