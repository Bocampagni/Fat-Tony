from socket import *
import json

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))

serverSocket.listen(1)
print('Servidor pronto para ser usado')

USUARIO = 'SADOC'
SENHA = 'UFRJ'

while True:
    connectionSocket, addr = serverSocket.accept()
    print("Requisição de:", addr)

    while 1:
        requestData = connectionSocket.recv(1024).decode()

        if requestData == '':
            break

        requestObject = json.loads(requestData)
        
        if requestObject['user'] == USUARIO and requestObject['password'] == SENHA:
            print("Host autorizado: ", addr)
            connectionSocket.send("Autorizado".encode())
        else:
            print("Host não autorizado: ", addr)
            connectionSocket.send("Nao autorizado".encode())
            connectionSocket.close()



    connectionSocket.close()