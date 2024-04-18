import socket

# Define the server address and port
server_host = '192.168.77.28'
server_port = 9999

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_host, server_port))

while True:
    # Input message from user
    message = input("Enter the message to send (or 'exit' to quit): ")
    if message.lower() == 'exit':
        break
    
    # Send message to the server
    client_socket.sendall(message.encode())

# Close the connection
client_socket.close()
