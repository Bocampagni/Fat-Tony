from socket import * 

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_DGRAM)

serverSocket.bind(('',serverPort))

print('O servidor está pronto para uso')

while True:
    message, clientAdress = serverSocket.recvfrom(2048)
    print("Requisição de: ", clientAdress)
    print("Com a mensagem:", message.decode())
    modifiedMessage = message.decode().upper()
    print("Resposta:", modifiedMessage)
    serverSocket.sendto(modifiedMessage.encode(), clientAdress)
