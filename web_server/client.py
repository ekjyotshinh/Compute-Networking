# Import socket library
from socket import *

def create_client_request(server_ip, server_port, filename):
    # Create a socket and connect to the server
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((server_ip, server_port))

    # Construct the HTTP GET request
    request = f"GET /{filename} HTTP/1.1\r\nHost: {server_ip}\r\n\r\n"
    clientSocket.send(request.encode())

    # Receive the response from the server and print it
    response = clientSocket.recv(2048).decode()
    for line in response.split('\n'):
        print(line)

    clientSocket.close()

if __name__ == "__main__":
    server_ip = "127.0.0.1"  # Use the IP of the server, in this case, localhost is used
    server_port = 12000
    filename = "test.html"
    create_client_request(server_ip, server_port, filename)

