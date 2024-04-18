import socket

# Define the server address and port
server_host = '192.168.77.28'
server_port = 9999

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_socket.bind((server_host, server_port))

# Listen for incoming connections
server_socket.listen(1)

print(f"Server listening on {server_host}:{server_port}")

# Accept incoming connections
client_socket, client_address = server_socket.accept()

print(f"Connection from {client_address}")

while True:
    # Receive data from the client
    data = client_socket.recv(1024)
    if not data:
        break
    print("Received:", data.decode('utf-8'))

# Close the connection
client_socket.close()
