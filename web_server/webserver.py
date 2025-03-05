# Import socket library
from socket import *

# Import sys package if you want to terminate the program
import sys

def create_server_socket(port):
    # Prepare a server socket
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(("", port))  # Bind the socket to the port
    serverSocket.listen(1)  # Listen for incoming connections (only one at a time)
    print(f"The server is ready to receive on port: {port}")
    return serverSocket

def handle_request(connectionSocket):
    try:
        # Receive the HTTP request
        message = connectionSocket.recv(2048).decode()
        print(f"Received request:\n{message}")
        
        if not message:
            connectionSocket.close()
            return

        # Prepare HTTP response header
        response_header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"

        # Get the requested file from the message
        filename = message.split()[1][1:]
        
        # Open the requested file and get the HTML body content
        with open(filename, "r") as file:
            response_body = file.read()

        # Send response message
        connectionSocket.send(response_header.encode() + response_body.encode())

        # Close the socket
        connectionSocket.close()

        # Terminate the program after sending the corresponding data
        # Comment it out if you want the server to be always ON
        sys.exit()

    except IOError:
        # Prepare 404 Not Found HTTP header
        response_header = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n"
        
        # Prepare the HTML body content of 404 Not Found page
        response_body = "<html><head><title>404 Not Found</title></head><body><h1>404 Not Found</h1><p>The requested file was not found on this server.</p></body></html>"

        # Send response message
        connectionSocket.send(response_header.encode() + response_body.encode())

        # Close socket
        connectionSocket.close()

if __name__ == "__main__":
    port = 12000
    serverSocket = create_server_socket(port)
    while True:
        connectionSocket, addr = serverSocket.accept()
        handle_request(connectionSocket)
