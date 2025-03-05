from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))  # Bind before listening
serverSocket.listen(1)  # Start listening for incoming connections

print("The Server is ready and listening...")

while True:
    connectionSocket, clientAddress = serverSocket.accept()  # Accept connection
    print(f"Connected to {clientAddress}")

    message = connectionSocket.recv(2048).decode()  # Receive data
    modifiedMessage = message.upper()

    connectionSocket.send(modifiedMessage.encode())  # Send modified data
    connectionSocket.close()  # Close connection
