import socket

# Create a socket object
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
# and port to listen on
host = 'localhost'
port = 12345

# Bind the socket to the port
socket.bind((host, port))

# Queue up to 5 requests
socket.listen(5)

print(f"Listening on port: {port}")

while True:
    # Establish a connection
    client, addr = socket.accept()
    print(f"Got a connection from {addr}")

    msg = 'Thank you for connecting' + "\r\n"
    client.send(msg.encode())

    client.close()
