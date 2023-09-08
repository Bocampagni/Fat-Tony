from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))

serverSocket.listen(5)
print('Servidor pronto para ser usado')

while True:
    connectionSocket, addr = serverSocket.accept()
    print("Requisição de:", addr)

    while 1:
        naturalNumber = connectionSocket.recv(2048)
        if naturalNumber.decode() == "":
            break
        print(naturalNumber)

    connectionSocket.close()