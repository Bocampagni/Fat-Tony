from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))

serverSocket.listen(1)
print('Servidor pronto para ser usado')

while True:
    connectionSocket, addr = serverSocket.accept()
    print("Requisição de:", addr)

    while 1:
        sentence = connectionSocket.recv(1024).decode()
        print("Mensagem:", sentence)
        if sentence == 'close':
            break
        capitalizedSentence = sentence.upper()
        connectionSocket.send(capitalizedSentence.encode())

    connectionSocket.close()