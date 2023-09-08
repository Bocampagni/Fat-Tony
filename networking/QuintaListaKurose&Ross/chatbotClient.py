from socket import *
import json

serverName = gethostname()
serverPort = 12000

clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

ESTADO_INICIAL = 0

print("Diga olá ao chatbot da turma: ")
while 1:

    #Se estado final, sai do while.
    if ESTADO_INICIAL == 3:
        break

    entrada = input()
    data = str(ESTADO_INICIAL)+"-"+entrada
    clientSocket.send(data.encode())

    responseMessage = clientSocket.recv(1024)
    print(responseMessage.decode())

    #Se estado de escolha dos serviços, e o valor digitado for diferente das opções, mandar para o servidor processar e sair do while.
    if ESTADO_INICIAL == 2 and entrada not in [1,2,3]:
        break

    ESTADO_INICIAL+=1



clientSocket.close()







