from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('',serverPort))

print("The Server is ready")

while True:

    message, clientAddress = serverSocket.recvfrom(2048)
    modifyMessage = message.decode().upper()

    serverSocket.sendto(modifyMessage.encode(),clientAddress)