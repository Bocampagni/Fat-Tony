from socket import *

serverName = gethostname()
serverPort = 12000

clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))


naturalNumber = int(input('Entre com um número '))

if naturalNumber == 0:
    clientSocket.close()

for x in range(naturalNumber):
    clientSocket.send(str(x).encode())


clientSocket.close()







