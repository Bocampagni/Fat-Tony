from socket import *
import json

serverName = gethostname()
serverPort = 12000

clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))


usuario = input('login: ')
senha = input('password: ')

requestData = {
    "user": usuario,
    "password": senha
}

jsonData = json.dumps(requestData)

clientSocket.send(jsonData.encode())

responseMessage = clientSocket.recv(1024)
print('Message from server: ', responseMessage.decode())



clientSocket.close()







