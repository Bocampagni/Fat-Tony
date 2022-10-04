from socket import *

serverName = gethostname()
serverPort = 12000

clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))


while 1:
    sentence = input('Entre com uma palavra em minusculo: ')
    clientSocket.send(sentence.encode())

    if sentence == 'close':
        break

    modifiedMessage = clientSocket.recv(1024)
    print('From server: ', modifiedMessage.decode())



clientSocket.close()







