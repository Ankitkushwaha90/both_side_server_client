import socket

# Define the server address and port
server_host = '192.168.77.28'  # Replace with the server's private IP address
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

# Function to receive messages from client
def receive_from_client():
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Client {client_address}: {data.decode('utf-8')}")

# Function to send messages to client
def send_to_client():
    while True:
        message = input("Server: ")
        client_socket.sendall(message.encode())
        if message.lower() == 'exit':
            break

# Start receiving and sending messages concurrently
import threading
receive_thread = threading.Thread(target=receive_from_client)
send_thread = threading.Thread(target=send_to_client)

receive_thread.start()
send_thread.start()

# Wait for both threads to finish
receive_thread.join()
send_thread.join()

# Close the connection
client_socket.close()
