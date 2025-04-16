from socket import *
import sys
import os

# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(('', int(sys.argv[1])))
tcpSerSock.listen(5)

while True:
    # Start receiving data from the client
    print('Ready to serve...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('Received a connection from:', addr)

    message = tcpCliSock.recv(1024).decode()
    print('Message received from client:\n', message)

    if not message:
        tcpCliSock.close()
        continue

    # Extract the filename from the message
    try:
        filename = message.split()[1][1:]  # Remove leading '/'

        # Clean URL
        if filename.startswith("http://"):
            filename = filename[7:]

        host_path_split = filename.split("/", 1)
        hostname = host_path_split[0]
        path = '/' + host_path_split[1] if len(host_path_split) > 1 else '/'

        # Use hostname and path to form a safe cache filename
        cache_filename = hostname + path.replace("/", "_")

        if os.path.exists(cache_filename):
            print('Cache hit! Serving from cache.')
            with open(cache_filename, "rb") as f:
                outputdata = f.read()
                tcpCliSock.sendall(outputdata)
        else:
            print('Cache miss. Fetching from origin server...')
            # Create a socket on the proxy server
            c = socket(AF_INET, SOCK_STREAM)
            c.connect((hostname, 80))

            # Create a temporary file on this socket and ask port 80 for the file requested by the client
            request = f"GET {path} HTTP/1.0\r\nHost: {hostname}\r\n\r\n"
            c.sendall(request.encode())

            with open(cache_filename, "wb") as cache_file:
                while True:
                    data = c.recv(4096)
                    if not data:
                        break
                    cache_file.write(data)
                    tcpCliSock.send(data)
            c.close()
    except Exception as e:
        print("Error:", e)

    tcpCliSock.close()

tcpSerSock.close()
# just in case fallback
