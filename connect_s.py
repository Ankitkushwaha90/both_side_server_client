import socket

# Define the address and port of the localhost server
host = '127.0.0.1'  # localhost
port = 8080

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((host, port))

# Send data to the server
client_socket.sendall(b'Hello, server!')

# Receive data from the server
data = client_socket.recv(1024)
print("Received:", data.decode('utf-8'))

# Close the connection
client_socket.close()
