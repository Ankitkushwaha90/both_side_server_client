import socket

# Define the server address and port
server_host = '192.168.77.28'
server_port = 9999

# Define the client address and port
client_host = '127.0.0.1'
client_port = 12345

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_host, server_port))

# Receive data from the server
data = client_socket.recv(1024)
print("Received:", data.decode('utf-8'))

# Close the connection
client_socket.close()
