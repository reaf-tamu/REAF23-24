import socket

# Set up the server on the Jetson
server_ip = '0.0.0.0'  # Listen on all available interfaces
server_port = 12345  # Choose an available port
buffer_size = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((server_ip, server_port))
    server_socket.listen()

    print(f"Listening for connections on {server_ip}:{server_port}")

    # Wait for a client to connect
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    while True:
        # Receive data from the client
        data = client_socket.recv(buffer_size).decode('utf-8')

        if not data:
            break  # Break the loop if no data is received

        print(f"Received data: {data}")

print("Connection closed.")

