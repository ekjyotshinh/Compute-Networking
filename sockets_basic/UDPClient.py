from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input('Please type your sentences: ')

clientSocket.sendto(message.encode(),(serverName,serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
clientSocket.close()