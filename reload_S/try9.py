import socket

# Define the server address and port
server_host = '10.88.0.4'
server_port = 9999

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_host, server_port))

# Function to receive messages from server
def receive_from_server():
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print("Server:", data.decode('utf-8'))

# Function to send messages to server
def send_to_server():
    while True:
        message = input("Client: ")
        client_socket.sendall(message.encode())
        if message.lower() == 'exit':
            break

# Start receiving and sending messages concurrently
import threading
receive_thread = threading.Thread(target=receive_from_server)
send_thread = threading.Thread(target=send_to_server)

receive_thread.start()
send_thread.start()

# Wait for both threads to finish
receive_thread.join()
send_thread.join()

# Close the connection
client_socket.close()
