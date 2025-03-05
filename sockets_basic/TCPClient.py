from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

sentence = input('Please type your sentences: ')

clientSocket.send(sentence.encode())

modifiedSentence = clientSocket.recv(2048)
print("From server message recieved is %d", modifiedSentence)
clientSocket.close()