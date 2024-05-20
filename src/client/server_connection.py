import socket

HOST = "localhost"  # The server's hostname or IP address
PORT = 8888        # The port used by the server
CONNECTION_SUCCESS = b"Connection successful"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))  # Connect to the server
    s.sendall(b"Connection request")  # Send data to the server

    data = s.recv(1024)  # Receive data from the server

if data == CONNECTION_SUCCESS:
    print("Connection successful!")
else:
    print(f"Unexpected response: {data.decode()}")