import socket

# Create a socket object
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = 'localhost'
port = 12345

# Connection to hostname on the port.
socket.connect((host, port))

# Receive no more than 1024 bytes
msg = socket.recv(1024)

socket.close()

print(msg.decode())
